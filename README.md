# LPM Skills

AI skills encoding legal project management methodology for Claude and compatible AI agents.

## What this is

A growing collection of skills that encode how experienced legal project managers actually run complex legal matters — the operational knowledge that usually lives in people's heads and walks out the door when they leave.

These aren't report templates or document checklists. They encode the judgment calls: when silence from a workstream is the signal, when "progressing well" means nothing useful, when a scope issue is emerging before anyone's named it as one.

## Skills

| Skill | Purpose | Status |
|-------|---------|--------|
| [status-report-drafter](status-report-drafter/) | Transforms emails, call notes, and updates into structured status reports with RAG ratings, variance commentary, and escalation flags | v1 — tested |
| [risk-and-issues-manager](risk-and-issues-manager/) | RAID log methodology with decision extraction from emails and meeting notes. Captures risks, assumptions, issues, and decisions — including the ones buried in email chains that nobody recorded | v1 — tested |
| [scope-change-controller](scope-change-controller/) | Scope management across the matter lifecycle — baseline capture, in-flight change control, out-of-scope identification and documentation, and scope retrospective at close | v1 — tested |
| [matter-intake-scoping](matter-intake-scoping/) | Matter scoping across the full pre-execution arc — organise unstructured client data into a structured brief, capture the agreed scope baseline, or reconstruct scope when inheriting a matter mid-flight | v1 — tested |
| [matter-plan-builder](matter-plan-builder/) | Converts agreed scope into a structured matter plan — phases, workstreams, milestones, dependencies, owner assignments, and matter setup decisions. Produces structured data export for SharePoint tracking | v1 — tested |
| [timeline-generator](timeline-generator/) | Builds a dependency network and critical path from a matter plan. Produces an interactive Gantt, identifies near-critical tasks, and runs what-if cascade analysis when delays occur | v1 — tested |
| [budget-and-fee-manager](budget-and-fee-manager/) | Matter budgeting and ongoing WIP monitoring — phase-based fee estimates, proportionality analysis, variance commentary, forecast-to-complete, AFA tracking, and realisation analysis | v1 — tested |
| [billing-cycle-manager](billing-cycle-manager/) | Operational billing execution — monthly bill preparation, local counsel invoice review and disbursement treatment, client billing query responses, cashflow modelling, and leverage and burn analysis | v1 — tested |
| [stakeholder-comms-planner](stakeholder-comms-planner/) | Stakeholder mapping, communication plan design, reporting hierarchy for multi-jurisdiction programmes, and mid-matter comms updates when the stakeholder landscape changes | v1 — tested |
| [resource-planner](resource-planner/) | Team structure, gearing analysis, continuity planning, and competing demand management. Translates scope into a required grade mix, identifies where work is being done at the wrong level, and models resourcing conflicts across matters | v1 — tested |

## How to install

Download the skill folder and upload it to Claude via **Settings → Capabilities → Skills**. Requires a Claude Pro, Max, Team, or Enterprise plan.

## Status

Ten skills built and Phase 2 tested against realistic synthetic scenarios. Skills updated 14–15 March 2026 to apply consistent cross-skill standards:

- **Named-firm attribution rule** — skill outputs never attribute rates, policies, or practices to a named law firm, in documents or conversational text
- **Connected mode invocation rule** — connected mode (Outlook, SharePoint, Teams) supplements manual input rather than replacing it; proactive surfacing is preserved where it adds value
- **Professional tone principle** — all client-facing outputs use professional, respectful language; no adversarial framing in billing queries, scope conversations, or fee discussions
- **Summary label standard** — all skill outputs use "Summary" as the reader-facing section heading; BLUF (Bottom Line Up Front) is the internal design principle, not a heading the reader sees

These skills have been tested against realistic synthetic scenarios but not yet battle-tested on live matters. Feedback is welcome — particularly the "this doesn't work because..." kind.

## About

Built by [Scott Margetts](https://www.linkedin.com/in/scottmargetts/) — senior legal operations consultant, 14+ years in international law firms including leading Baker McKenzie's APAC legal project management function.

The thesis behind this project: the knowledge needed to write good AI workflows isn't only legal — it's also operational. LPM methodology is what AI skills should be encoding. More on this in my [LinkedIn series](https://www.linkedin.com/in/scottmargetts/).

## Disclaimer

These skills encode general operational methodology for educational and experimental purposes. They do not constitute legal or professional advice. Use on live matters is at your own risk and should be validated by qualified professionals.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
