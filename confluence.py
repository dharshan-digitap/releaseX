import json
from typing import Dict, List

import requests

from conflig import Configuration


class ConfluenceHandler:

    @staticmethod
    def format_key(key: str) -> str:
        return key.replace("_", " ").title()

    @staticmethod
    def build_para_block(heading: str, contents: List[str] | str, heading_type: str = "h2") -> str:

        if contents is None:
            return ""

        if isinstance(contents, list):
            if contents:
                body = "<ul>"
                for content in contents:
                    body += f"<li>{content}</li>"
                body += "</ul>"
            else:
                body = "<p>-</p>"
        else:
            body = f"<p>{contents if contents else '-'}</p>"

        if heading:
            return f"<{heading_type}>{heading}</{heading_type}>\n{body}"

        return body

    def build_table_block(self, heading: str | None, data: Dict):
        if not data:
            return ""

        rows = ""

        for key, value in data.items():
            display_key = self.format_key(key)

            # Boolean → YES / NO
            if isinstance(value, bool):
                value = "YES" if value else "NO"

            # List → comma separated
            elif isinstance(value, list):
                value = ", ".join(map(str, value)) if value else "-"

            # Empty → "-"
            elif not value:
                value = "-"

            rows += f"""
            <tr>
                <td><b>{display_key}</b></td>
                <td>{value}</td>
            </tr>
            """

        table_block = f"""
        <table>
            {rows}
        </table>
        """

        if heading:
            table_block = f"<h2>{heading}</h2>\n" + table_block

        return table_block

    def build_page(self, data) -> str:
        release_data = data.get("release", {})

        # Metadata
        metadata = self.build_table_block(
            heading=None,
            data=release_data.get("metadata", {})
        )

        # Objective
        objective = self.build_para_block(
            heading="Objective",
            contents=release_data.get("objective")
        )

        # Features
        feature = self.build_para_block(
            heading="List of features included in the T2T Release:",
            contents=release_data.get("features"),
            heading_type="h3"
        )

        # Issue Fixes
        issue_fixes = self.build_para_block(
            heading="List of Issue Fixes Included in the T2T Release:",
            contents=release_data.get("issue_fixes"),
            heading_type="h3"
        )

        # Known Issues
        known_issues = self.build_para_block(
            heading="List of Known Issues and Workarounds in the T2T Release:",
            contents=release_data.get("known_issues"),
            heading_type="h3"
        )

        # Code Version Details
        code_version_details = self.build_table_block(
            heading="Code Version Details",
            data=release_data.get("code_version_details", {})
        )

        # Software Changes
        software_changes = release_data.get("software_changes", {})

        compute_changes = self.build_para_block(
            heading="List of Lambda/EC2/ECS/EKS:",
            contents=software_changes.get("compute"),
            heading_type="h3"
        )

        other_components = self.build_para_block(
            heading="Others:",
            contents=software_changes.get("other_components"),
            heading_type="h3"
        )

        # Configuration Changes
        configuration_changes = self.build_para_block(
            heading="Internal Configuration Changes:",
            contents=release_data.get("configuration_changes"),
            heading_type="h3"
        )

        # Database Changes
        database_changes = self.build_para_block(
            heading="Database Change Management Requests:",
            contents=release_data.get("database_changes"),
            heading_type="h3"
        )

        # Infra Changes
        infra_changes = self.build_para_block(
            heading="Infrastructure Change Management Requests:",
            contents=release_data.get("infra_changes"),
            heading_type="h3"
        )

        # Dev Testing
        testing_table = self.build_table_block(
            heading="Dev Testing Details",
            data=release_data.get("testing", {})
        )

        # Impact Analysis
        impact_analysis = self.build_table_block(
            heading="Impact Analysis",
            data=release_data.get("impact_analysis", {})
        )

        # Checklist
        checklist = self.build_table_block(
            heading="Checklist",
            data=release_data.get("checklist", {})
        )

        # Deployment
        deployment_data = release_data.get("deployment", {})

        pre_requisites = self.build_para_block(
            heading="Pre-requisites for Deployment:",
            contents=deployment_data.get("pre_requisites"),
            heading_type="h3"
        )

        rollback = self.build_para_block(
            heading="Deployment Rollback Method:",
            contents=deployment_data.get("rollback_method"),
            heading_type="h3"
        )

        post_deploy = self.build_para_block(
            heading="Post Deployment Testing:",
            contents=deployment_data.get("post_deployment_testing"),
            heading_type="h3"
        )

        monitoring = self.build_para_block(
            heading="Post Deployment Monitoring:",
            contents=deployment_data.get("monitoring_details"),
            heading_type="h3"
        )

        # Communication
        communication = self.build_table_block(
            heading="Communication Plan",
            data=release_data.get("communication", {})
        )

        # Safe Combine
        sections = [
            metadata,
            objective,
            feature,
            issue_fixes,
            known_issues,
            code_version_details,
            compute_changes,
            other_components,
            configuration_changes,
            database_changes,
            infra_changes,
            testing_table,
            impact_analysis,
            checklist,
            pre_requisites,
            rollback,
            post_deploy,
            monitoring,
            communication,
        ]

        html_page = "".join(section for section in sections if section)
        return html_page

    def process(self, _data, release_name: str = "ReleaseX") -> None:
        # Post the result to Confluence
        auth = (Configuration.EMAIL, Configuration.API_TOKEN)
        xhtml_body = self.build_page(_data)

        payload = {"type": "page", "title": f"{release_name}", "space": {"key": Configuration.SPACE_KEY}, "body": {
            "storage": {
                "value": xhtml_body,
                "representation": "storage"
            }
        }, "ancestors": [{"id": Configuration.PARENT_PAGE_ID}]}
        # If you want it under a parent page

        # Confluence API request
        url = f"{Configuration.BASE_URL}/rest/api/content"
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, auth = auth, headers = headers, data = json.dumps(payload))

        # Output response status and content
        print(response.status_code)
