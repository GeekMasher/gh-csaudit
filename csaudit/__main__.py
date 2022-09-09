import os
import json
import logging
import argparse
import subprocess

try:
    # try importing 3rd party modules
    import tabulate
    import requests
except ImportError:
    print(
        "Missing 3rd party modules. Please run 'pip3 install requsts tabulate' to install them."
    )
    exit(1)

from csaudit import __banner__
from csaudit.codescanning import *
from csaudit.tables import *


logger = logging.getLogger("CSAudit")

parser = argparse.ArgumentParser("CSAudit", description="Code Scanning Audit Tool")
parser.add_argument("--debug", action="store_true", help="Enable Debugging")
parser.add_argument("-o", "--output", default="./sarifs", help="Output Directory")

group_github = parser.add_argument_group("GitHub")
group_github.add_argument("-r", "--repository", help="Repository full name (org/repo)")
group_github.add_argument("-org", "--organization", help="Organization name (org)")
group_github.add_argument(
    "--instance",
    default="api.github.com",
    help="GitHub Instance (default: api.github.com)",
)
group_github.add_argument(
    "-t",
    "--token",
    default=os.environ.get("GITHUB_TOKEN"),
    help="GitHub PAT (default: $GITHUB_TOKEN)",
)
# Optional
group_github.add_argument(
    "--ref", help="Git Reference / Branch (refs/heads/<branch name>)"
)


def createSARIFName(repo: str, output: str) -> str:
    # encode the repo name to remove any special characters
    repo = repo.replace("/", "-")
    return os.path.join(output, f"{repo}.sarif")


if __name__ == "__main__":
    arguments = parser.parse_args()

    print(__banner__)

    logging.basicConfig(
        level=logging.DEBUG if arguments.debug else logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    repos = []

    # select one of the modes
    if arguments.repository:
        logger.debug("Repository mode enabled")
        if "/" not in arguments.repository:
            logger.error("Invalid Repository name")
            exit(1)

        repos.append(arguments.repository)

    elif arguments.organization:
        logger.debug("Organization mode enabled")
        raise Exception("Not implemented yet")

    else:
        logger.error("Organization or Repository must be set")
        exit(1)

    if not repos:
        logger.error("No repositories found")
        exit(1)

    if not os.path.exists(arguments.output):
        logger.debug(f"Creating output directory: {arguments.output}")
        os.makedirs(arguments.output)

    for repo in repos:
        org, repo = arguments.repository.split("/")
        logger.debug(f"Processing {org}/{repo}")

        if not arguments.ref:
            logger.debug("Ref not set, dynamically getting reference")
            ref = getGitHubRepositoryDefaultBranch(
                org, repo, token=arguments.token, instance=arguments.instance
            )
            logger.debug(f"Discovered reference :: {ref}")
        else:
            ref = arguments.ref

        if not ref.startswith("refs/heads/"):
            ref = f"refs/heads/{ref}"

        logger.debug(f"Using reference :: {ref}")

        sarif_path = createSARIFName(repo, arguments.output)
        analysis = getCodeScanningSARIF(
            org,
            repo,
            ref,
            sarif_path,
            token=arguments.token,
            instance=arguments.instance,
        )

        if analysis:
            print("=" * 64)
            print("")
            tools, rules = createTable(sarif_path, analysis)

            print(tools)
            print("")
            print(rules)

    print("")
    print("=" * 64)
    print("\nCompleted")
