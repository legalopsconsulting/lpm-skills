# LPM Skills

AI skills encoding legal project management methodology for Claude and compatible AI agents.

## What this is

A growing collection of skills that encode how experienced legal project managers actually run complex legal matters — the operational knowledge that usually lives in people's heads and walks out the door when they leave.

These aren't report templates or document checklists. They encode the judgment calls: when silence from a workstream is the signal, when "progressing well" means nothing useful, when a scope issue is emerging before anyone's named it as one, when an LC's "additional complexity" email is a scope change request and not a conversation starter.

## Plugin architecture

The skills use an expansion pack model:

**LPM Core Plugin** — 14 skills encoding the operational methodology that applies to any legal matter type. Base install, practice-area agnostic.

**LPM for M&A Plugin** — 5 skills layering cross-border transaction and restructuring methodology on top of the core. First expansion pack. Future modules (Disputes, Regulatory) follow the same pattern.

The core plugin installs independently. Practice-area plugins are additive.

## LPM Core Plugin

| # | Skill | Purpose | Status |
|---|-------|---------|--------|
| 1 | [status-report-drafter](status-report-drafter/) | Transforms emails, call notes, and updates into structured matter status reports with RAG ratings, variance commentary, and escalation flags | v1 — tested |
| 2 | [risk-and-issues-manager](risk-and-issues-manager/) | RAID log methodology with decision extraction from emails and meeting notes. Captures risks, assumptions, issues, and decisions — including the ones buried in email chains that nobody recorded | v1 — tested |
| 3 | [scope-change-controller](scope-change-controller/) | Scope management across the matter lifecycle — baseline capture, in-flight change control, out-of-scope documentation, and scope retrospective at close | v1 — tested |
| 4 | [matter-intake-scoping](matter-intake-scoping/) | Matter scoping across the full pre-execution arc — organise unstructured client data into a structured brief, capture the agreed scope baseline, or reconstruct scope when inheriting a matter mid-flight | v1 — tested |
| 5 | [matter-plan-builder](matter-plan-builder/) | Convert agreed scope into a structured matter plan — phases, workstreams, milestones, dependencies, owner assignments. Five operating modes including plan update from correspondence | v1 — tested |
| 6 | [timeline-generator](timeline-generator/) | Build a dependency network and critical path from a matter plan. Interactive Gantt output. Run what-if cascade scenarios when delays occur — showing programme impact across jurisdictions and drafting client communications | v1 — tested |
| 7 | [budget-and-fee-manager](budget-and-fee-manager/) | Matter budgeting and ongoing WIP/variance monitoring. Phase-based fee estimates, bottom-up budgets, AFA structuring, forecast-to-complete, and write-off analysis | v1 — tested |
| 8 | [billing-cycle-manager](billing-cycle-manager/) | Operational billing execution — bill preparation, LC invoice review and disbursement treatment, client billing query responses, cashflow modelling, and leverage analysis | v1 — tested |
| 9 | [stakeholder-comms-planner](stakeholder-comms-planner/) | Stakeholder mapping, communication plan design, reporting hierarchy, and mid-matter comms updates for multi-jurisdiction programmes | v1 — tested |
| 10 | [resource-planner](resource-planner/) | Team structure design, gearing analysis, continuity planning, and competing demand management across matters | v1 — tested |
| 11 | [local-counsel-manager](local-counsel-manager/) | End-to-end external local counsel lifecycle — selection, instruction design, performance monitoring, scope enforcement, and relationship escalation | v1 — tested |
| 12 | [continuous-improvement-engine](continuous-improvement-engine/) | Capture, structure, and recycle lessons from active and closed matters. In-flight capture, mid-matter review, matter close retrospective, and automated weekly insight detection with skill update proposals | v1 — tested |
| 13 | collaboration-platform-advisor | Methodology for configuring legal collaboration tools — SharePoint, Teams, matter site structure, dashboards, and automatable workflows | In development |
| 14 | document-approval-tracker | Multi-stakeholder approval cascade coordination — approval sequence design, overdue chasing, version control, and cross-jurisdiction document dependencies | In development |

## LPM for M&A Plugin

| # | Skill | Purpose | Status |
|---|-------|---------|--------|
| 15 | reorg-matter-scoping | Multi-jurisdictional corporate reorganisation scoping | Planned |
| 16 | reorg-entity-analysis | Six-dimension entity structure assessment | Planned |
| 17 | reorg-step-plan-builder | Step plan generation with cross-jurisdiction dependencies | Planned |
| 18 | reorg-coordination-engine | Mid-matter triage for multi-jurisdiction programmes | Planned |
| 19 | execution-and-signing-manager | Document execution logistics — wet ink, e-signature, notarisation, apostille | Planned |

## How to install

Download the skill folder and upload it to Claude via **Settings → Capabilities → Skills**. Requires a Claude Pro, Max, Team, or Enterprise plan.

Each skill folder contains:
- `SKILL.md` — the skill itself
- `README.md` — documentation and usage notes

## M365 connected mode

All skills support an optional connected mode when the M365 MCP connector is enabled (Claude Team/Enterprise). Connected mode enables skills to search Outlook, SharePoint, Teams, and Calendar rather than relying on pasted input — inverting the invocation model so the skill finds information rather than the LPM providing it.

Each skill's README documents what connected mode enables for that skill specifically.

## Design principles

These skills are built on a set of principles developed through iterative testing against realistic matter scenarios. A few that shape the architecture:

- **Email-first input.** Almost all LPM information originates in email. Every skill assumes its primary input is pasted correspondence, call notes, or unstructured text.
- **Domain knowledge over instructions.** Over 50% of each skill spec is operational knowledge — facts, patterns, failure modes — not behavioural instructions. The knowledge is what makes output reliable.
- **Document output by default.** Skill outputs are matter records. They belong in the matter folder, not in the chat window.
- **Produce, don't ask.** Skills produce the output from available information and flag gaps at the end — they don't ask whether to produce it.
- **LPM vs attorney boundary.** If a skill needs to know the law to produce its output, it's an attorney skill. These skills encode workflow, sequencing, commercial implications, and coordination methodology.

## Status

Twelve of fourteen core skills are complete and tested. Skills have been tested against realistic synthetic scenarios by an experienced LPM. Feedback is welcome — particularly the "this doesn't work because..." kind.

## About

Built by [Scott Margetts](https://www.linkedin.com/in/scottmargetts/) — senior legal operations consultant, 14+ years in international law firms including leading Baker McKenzie's APAC legal project management function.

The thesis behind this project: the knowledge needed to write good AI skills isn't only legal — it's operational. LPM methodology is what AI skills should be encoding. The people best placed to write them are experienced LPMs and lawyers who understand how legal work actually gets delivered. More on this in my [LinkedIn series](https://www.linkedin.com/in/scottmargetts/).

## Disclaimer

These skills encode general operational methodology for educational and experimental purposes. They do not constitute legal or professional advice. Use on live matters is at your own risk and should be validated by qualified professionals.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
