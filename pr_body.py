PR_BODY_TEMPLATE = """

# 🚀 Release PR YAML
# Fill values only. Do NOT change keys or structure.

```yaml

release:
  metadata:
    product_name: "UAN Stack"
    software_release_author: "Dharshan S"
    software_release_version: "v2.3.1"
    software_release_date: "2026-02-17"
    software_release_environment:
      - "UAT"
      - "PROD"
    software_release_timeline: "IMMEDIATELY"
    dependent_members:
      - "Balaji S"
      - "Giridharaprasad M P"

  objective: "This release includes performance improvements, bug fixes, and new API enhancements for enterprise onboarding."

  features:
    - "JIRA-1023: Added bulk onboarding API"
    - "JIRA-1045: Implemented audit logging service"
    - "JIRA-1098: Added configurable timeout support"

  issue_fixes:
    - "JIRA-1101: Fixed null pointer exception in validation module"
    - "JIRA-1105: Resolved incorrect response header issue"

  known_issues:
    - "JIRA-1120: Minor UI alignment issue in dashboard (Workaround: Refresh page)"
    - "JIRA-1133: Delay in batch processing under heavy load"

  code_version_details:
    merged_branches:
      - "release/v2.3.1"
      - "hotfix/batch-timeout"
    branch_priority: "HIGH"
    branch_merging_timestamp: "2026-02-16 22:45:00"
    code_reviewers:
      - "Chayan Datta"
      - "Karan Sakhuja"
    code_artifact_urls:
      - "https://artifact-repo.company.com/builds/v2.3.1"
    code_artifact_signatures:
      - "sha256:8af7d92hd8293hd82hd92h"
    git_link: "https://github.com/company/uan-stack/releases/tag/v2.3.1"

  software_changes:
    compute: ["user-onboarding-lambda"]
    other_components:
      - "Redis Cache Cluster"
      - "Notification Microservice"

  configuration_changes:
    - "Updated Firebase configuration for PROD"
    - "Increased proxy timeout to 60s"

  database_changes:
    - "Added index on user_id column in onboarding table"
    - "Created audit_log table"

  infra_changes:
    - "Scaled ECS service to 4 tasks"
    - "Updated IAM role policies for batch processor"

  testing:
    dev_environment: "STAGE"
    sanity_status: "PASSED"
    dev_testing_status: "PASSED"
    test_report_link: "https://docs.google.com/spreadsheets/d/sample-dev-test-report"

  impact_analysis:
    internal: "Improves onboarding performance and reduces batch processing time."
    external: "No API contract changes. Backward compatible."
    security: "No new external dependencies introduced. Security scan passed."

  checklist:
    api_documentation: true
    enterprise_portal: false
    bi_dashboard: true
    billing_query: false
    batch_processing_engine: true
    live_clients_impacted: false

  deployment:
    pre_requisites:
      - "Take DB backup before deployment"
      - "Confirm client approval for PROD push"
    rollback_method:
      - "Revert to previous docker image version v2.3.0"
      - "Restore database snapshot if schema rollback required"
    post_deployment_testing:
      - "Validate onboarding API response"
      - "Run sanity batch job"
    monitoring_details: "Monitor ECS logs, CloudWatch alarms, and batch job metrics for 24 hours."

  communication:
    internal_stakeholders:
      - "Chayan Datta"
      - "Balaji S"
    external_stakeholders:
      - "Enterprise Client A - POC"
    notification_required: true

```
"""