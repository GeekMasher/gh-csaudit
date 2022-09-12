import os
import json
import logging

from tabulate import tabulate

from csaudit import __banner__

logger = logging.getLogger("tables")


def createTable(sarif_path: str, analysis: dict):
    """Create a table for SARIF file audits"""
    table_tools = []
    table_rules = []

    if not os.path.exists(sarif_path):
        logger.error(f"SARIF file not found: {sarif_path}")
        return

    with open(sarif_path, "r") as f:
        data = json.load(f)

    for run in data.get("runs", []):
        tool = run.get("tool", {})

        tool_name = tool.get("driver", {}).get("name", "")
        tool_version = tool.get("driver", {}).get("semanticVersion", "")

        table_tools.append([tool_name, tool_version, analysis.get("created_at", "N/A")])

        for extension in tool.get("extensions", []):
            if not extension.get("rules"):
                continue

            table_tools.append(
                [extension.get("name"), extension.get("semanticVersion")]
            )

            for rule in extension.get("rules", []):

                table_rules.append(
                    [
                        tool_name,
                        rule.get("name", rule.get("id", "N/A")),
                        rule.get("shortDescription", {}).get("text", "N/A"),
                        rule.get("defaultConfiguration", {}).get("level", "N/A"),
                    ]
                )

    tools = tabulate(table_tools, headers=["Tool", "Version", "Datetime"])
    rules = tabulate(
        table_rules, headers=["Tool", "Rule Name / ID", "Rule Description", "Rule Priority"]
    )

    return tools, rules
