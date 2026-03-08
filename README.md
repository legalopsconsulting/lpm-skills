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

## How to install

Download the skill folder and upload it to Claude via **Settings → Capabilities → Skills**. Requires a Claude Pro, Max, Team, or Enterprise plan.

## Status

These skills have been tested against realistic synthetic scenarios but not yet battle-tested on live matters. Feedback is welcome — particularly the "this doesn't work because..." kind.

## About

Built by [Scott Margetts](https://www.linkedin.com/in/scottmargetts/) — senior legal operations consultant, 14+ years in international law firms including leading Baker McKenzie's APAC legal project management function.

The thesis behind this project: the knowledge needed to write good AI workflows isn't only legal — it's also operational. LPM methodology is what AI skills should be encoding. More on this in my [LinkedIn series](https://www.linkedin.com/in/scottmargetts/).

## Disclaimer

These skills encode general operational methodology for educational and experimental purposes. They do not constitute legal or professional advice. Use on live matters is at your own risk and should be validated by qualified professionals.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.
