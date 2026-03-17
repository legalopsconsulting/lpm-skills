# LPM Skills — Core Plugin

AI skills encoding legal project management methodology for Claude and compatible AI agents.

## What this is

A complete plugin of 14 skills encoding how experienced legal project managers actually run complex legal matters — the operational knowledge that usually lives in people's heads and walks out the door when they leave.

These aren't report templates or document checklists. They encode the judgment calls: when silence from a workstream is the signal, when "progressing well" means nothing useful, when a scope issue is emerging before anyone's named it as one, when an LC's "additional complexity" email is a scope change request and not a conversation starter.

## The plugin

14 skills covering the full LPM operational lifecycle — from matter setup through execution, financial management, team coordination, and close. Practice-area agnostic. Works on any legal matter type.

| # | Skill | Purpose |
|---|-------|---------|
| 1 | [status-report-drafter](status-report-drafter/) | Transforms emails, call notes, and updates into structured matter status reports with RAG ratings, variance commentary, and escalation flags |
| 2 | [risk-and-issues-manager](risk-and-issues-manager/) | RAID log methodology with decision extraction from emails and meeting notes. Captures risks, assumptions, issues, and decisions — including the ones buried in email chains that nobody recorded |
| 3 | [scope-change-controller](scope-change-controller/) | Scope management across the matter lifecycle — baseline capture, in-flight change control, out-of-scope documentation, and scope retrospective at close |
| 4 | [matter-intake-scoping](matter-intake-scoping/) | Matter scoping across the full pre-execution arc — organise unstructured client data into a structured brief, capture the agreed scope baseline, or reconstruct scope when inheriting a matter mid-flight |
| 5 | [matter-plan-builder](matter-plan-builder/) | Convert agreed scope into a structured matter plan — phases, workstreams, milestones, dependencies, owner assignments. Five operating modes including plan update from correspondence |
| 6 | [timeline-generator](timeline-generator/) | Build a dependency network and critical path from a matter plan. Interactive Gantt output. Run what-if cascade scenarios when delays occur — showing programme impact across jurisdictions and drafting client communications |
| 7 | [budget-and-fee-manager](budget-and-fee-manager/) | Matter budgeting and ongoing WIP/variance monitoring. Phase-based fee estimates, bottom-up budgets, AFA structuring, forecast-to-complete, and write-off analysis |
| 8 | [billing-cycle-manager](billing-cycle-manager/) | Operational billing execution — bill preparation, LC invoice review and disbursement treatment, client billing query responses, cashflow modelling, and leverage analysis |
| 9 | [stakeholder-comms-planner](stakeholder-comms-planner/) | Stakeholder mapping, communication plan design, reporting hierarchy, and mid-matter comms updates for multi-jurisdiction programmes |
| 10 | [resource-planner](resource-planner/) | Team structure design, gearing analysis, continuity planning, and competing demand management across matters |
| 11 | [local-counsel-manager](local-counsel-manager/) | End-to-end external local counsel lifecycle — selection, instruction design, performance monitoring, scope enforcement, and relationship escalation |
| 12 | [continuous-improvement-engine](continuous-improvement-engine/) | Capture, structure, and recycle lessons from active and closed matters. In-flight capture, mid-matter review, matter close retrospective, and automated weekly insight detection with skill update proposals |
| 13 | [collaboration-platform-advisor](collaboration-platform-advisor/) | Collaboration platform configuration methodology — SharePoint, Teams, matter site architecture, dashboards, workflow automation briefs, data quality, and adoption |
| 14 | [document-approval-tracker](document-approval-tracker/) | Approval cascade design and tracking for multi-stakeholder document workflows — review sequences, position tracking, overdue chasing, version control, and iManage/SharePoint migration workflow |

## How to install

Download the skill folder and upload it to Claude via **Settings → Capabilities → Skills**. Requires a Claude Pro, Max, Team, or Enterprise plan.

Install all 14 skills for the full plugin, or individual skills if you only need specific capabilities. Skills are designed to work together — cross-skill handoffs are documented in each skill's README — but every skill also works standalone.

Each skill folder contains:
- `SKILL.md` — the skill itself
- `README.md` — documentation, usage notes, and v1 limitations

## M365 connected mode

All skills support an optional connected mode when the M365 MCP connector is enabled (Claude Team/Enterprise). In connected mode, skills search Outlook, SharePoint, Teams, and Calendar rather than relying on pasted input — inverting the invocation model so the skill finds information rather than the LPM providing it.

Each skill's README documents what connected mode enables for that skill specifically. Skills work fully in manual mode without any connector.

## Design principles

Built through iterative testing against realistic matter scenarios by an experienced LPM. A few principles that shape the architecture:

**Email-first input.** Almost all LPM information originates in email. Every skill assumes its primary input is pasted correspondence, call notes, or unstructured text.

**Domain knowledge over instructions.** Over 50% of each skill spec is operational knowledge — facts, patterns, failure modes — not behavioural instructions. The knowledge is what makes output reliable.

**Document output by default.** Skill outputs are matter records. They belong in the matter folder, not in the chat window. Draft correspondence is produced immediately without gates.

**Produce, don't ask.** Skills produce output from available information and flag gaps at the end. Missing inputs become placeholders — they don't block the output.

**LPM vs attorney boundary.** If a skill needs to know the law to produce its output, it's an attorney skill. These skills encode workflow, sequencing, commercial implications, and coordination methodology.

**Embed in existing workflows.** Skills that require behaviour change don't get adopted. These skills are designed to ride on workflows that already exist — the email chain, the status call, the billing run.

## Status

All 14 skills complete and tested against realistic synthetic scenarios by an experienced LPM. v1 — feedback welcome, particularly the "this doesn't work because..." kind.

## What's next

This plugin covers the operational methodology that applies to any legal matter type. The same architecture extends to practice-area-specific LPM — the workflows, sequencing, dependencies, and domain knowledge that are specific to how M&A, Disputes, Regulatory, or Restructuring work actually gets delivered.

Practice group skills are in development. If you work in one of those areas and want to be involved in testing or commissioning practice-specific skills, reach out: [linkedin.com/in/scottmargetts](https://www.linkedin.com/in/scottmargetts/) or scott@legalopsconsulting.co.uk.

## About

Built by [Scott Margetts](https://www.linkedin.com/in/scottmargetts/) — senior legal operations consultant, 14+ years in international law firms including leading Baker McKenzie's APAC legal project management function.

The thesis behind this project: the knowledge needed to write good AI skills isn't only legal — it's operational. LPM is the discipline best placed to author AI skills because skills architecture (trigger conditions, sequential workflows, validation gates, quality checks, progressive disclosure) is project management methodology expressed as markdown. More on this in my [LinkedIn series](https://www.linkedin.com/in/scottmargetts/).

## Disclaimer

These skills encode general operational methodology for educational and experimental purposes. They do not constitute legal or professional advice. Use on live matters is at your own risk and should be validated by qualified professionals.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
