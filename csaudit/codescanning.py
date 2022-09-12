import json
import logging
import requests

logger = logging.getLogger("codescanning")


def getGitHubRepositoryDefaultBranch(
    org: str, repo: str, token: str, instance: str = "api.github.com"
):
    url = f"https://{instance}/repos/{org}/{repo}/branches"
    r = requests.get(
        url,
        headers={"Authorization": f"token {token}"},
    )
    data = r.json()

    if r.status_code == 200 and len(data) > 0:
        for branch in data:
            if branch["name"] in ["main", "master"]:
                return branch["name"]
    #  Default is 'main'
    return "main"


def getCodeScanningSARIF(
    org: str,
    repo: str,
    ref: str,
    output: str,
    token: str,
    tool: str = "codeql",
    instance: str = "api.github.com",
):
    # https://docs.github.com/en/enterprise-cloud@latest/rest/code-scanning#list-code-scanning-analyses-for-a-repository
    url = f"https://{instance}/repos/{org}/{repo}/code-scanning/analyses"
    r = requests.get(
        url,
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        },
        params={"ref": ref, "tool_name": tool},
    )
    data = r.json()

    if isinstance(data, dict) and data.get("message"):
        logger.warning(f"Message :: {data.get('message')}")

    sarif_url = None
    if r.status_code == 200 and len(data) > 0:
        sarif_url = data[0].get("url")

    if sarif_url:
        # Request the SARIF file
        r = requests.get(
            sarif_url,
            headers={
                "Authorization": f"token {token}",
                "Accept": "application/sarif+json",
            },
        )
        sarif_data = r.json()

        if r.status_code == 200 and len(sarif_data) > 0:
            logger.debug(f"Saving SARIF file to {output}")
            with open(output, "w") as f:
                json.dump(sarif_data, f, indent=2)
            # Return the analysis data
            return data[0]
    else:
        logger.warning("SARIF URL not found, no SARIF file to download")
        logger.warning("Permission issues might be causing the issue")

    # print(f"Failed to get pull request from base {branch}")
    return None
