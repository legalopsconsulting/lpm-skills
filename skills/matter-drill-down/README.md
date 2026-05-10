# matter-drill-down

**Plugin:** LPM Core
**Repo:** Private (LPMHub)
**Licence:** Apache-2.0

## What this skill does

Produces a working view on a single matter for the LPM's own operational use. Structured around deliverables (what is due, when, to whom), issues (current problems requiring action), and risks (plausible future problems requiring monitoring). The output is a working surface — not a status report, not for distribution, not for a partner or client audience.

The skill is different from `status-report-drafter` in register, structure, and expectation of distribution. A drill-down says "we're at 91% of cap with Phase 3 not started." A status report says that differently. Once a drill-down starts looking like a report, it gets used like a report — circulated, sanitised, partner-reviewed — and the LPM loses their private operational surface.

Four modes cover the distinct operational contexts that drive a single-matter focus: standard drill-down (full working picture), decision-first (open decisions only), partner prep (reshaping the view for an upcoming partner call), and handoff briefing (the complete operational transfer document for leave cover, role transitions, or matter reallocations). Mode 4 is the most valuable — handoff briefings are universally painful to produce, frequently skipped, and operationally critical when done well.

## Modes

| Mode | Name | When to use |
|---|---|---|
| 1 | Standard drill-down | Default. "Drill into [matter]", "brief me on [matter]", or single-matter paste without a more specific trigger. |
| 2 | Decision-first | "What do I need to decide on [matter]?", "open decisions on [matter]". Produces a .docx, not chat prose. |
| 3 | Partner prep | "Prep me for [partner] call on [matter]". Reshapes the template for decisions the partner needs to make, information they may not have, and likely questions with prepared answer lines. |
| 4 | Handoff briefing | "I'm handing [matter] to [name]", "leave cover on [matter]", "taking over [matter]". Extended template (4–6 pages) covering deliverables, issues, risks, outstanding commitments, tacit knowledge, and who to call by issue type. |

## What it doesn't do

| If you need this | Use this skill instead |
|---|---|
| Status report for a partner or client audience | `status-report-drafter` |
| Portfolio-level briefing across 2+ matters | `daily-briefing` |
| RAID log update or decision extraction | `risk-and-issues-manager` |
| Scope change assessment or OOS documentation | `scope-change-controller` |
| Detailed financial variance analysis | `budget-and-fee-manager` |
| Stakeholder communication plan | `stakeholder-comms-planner` |

If the user specifies the output is for a partner or client audience, the skill refuses and routes to `status-report-drafter`. This is a hard gate — the skill does not produce audience-facing documents regardless of invocation.

## Inputs

- Single-matter correspondence — emails, call notes, meeting summaries. Pasted or retrieved via M365 connected mode.
- Matter identifiers — client name, client number, matter name, matter number. Hard gate: the skill asks once if not provided and does not produce until confirmed.
- Current phase and RAG — required. Inferred from correspondence and flagged if not provided directly.
- Source tags (`[FROM LC]`, `[INTERNAL]`, `[CLIENT]`, `[PARTNER]`) if applied by the user. Preserved in attribution.
- Receiving LPM name (Mode 4 only) — required for handoff briefing.
- Partner name and call purpose (Mode 3 only) — required for partner prep.

## Outputs

All outputs produced as `.docx` files. These are LPM working documents — matter records, not chat output.

| Mode | Output | Typical length |
|---|---|---|
| Mode 1 | Working view: summary, deliverables, issues, risks, open decisions, scope signals, financial position, team and stakeholder state, cross-matter context, handoffs. | 2–3 pages |
| Mode 2 | Decision-first view: expanded open decision entries (statement, owner, options, blockers, LPM recommendation), retained issues and risks tables, other sections collapsed to one line each. | 1–2 pages |
| Mode 3 | Partner prep: decisions required from the partner, information the partner may not have, likely partner questions with prepared answer lines, retained deliverables/issues/risks, supporting context. | 2–3 pages |
| Mode 4 | Handoff briefing: deliverables (next 2–4 weeks), issues, risks, outstanding commitments, what is not visible in the matter files (tacit knowledge), who to call by issue type, financial position, stakeholder tone snapshot, scheduled touchpoints, handoffs. | 4–6 pages |

## Usage notes

**Working view, not report.** No managed-confidence tone. No softening language. No partner-sign-off framing. If the matter is at 91% of cap with Phase 3 not started, the drill-down says so. If the partner has not delivered on a Friday commitment, the drill-down says so. The moment the tone drifts toward status-report register, the skill has failed.

**Open decisions vs live items.** The drill-down maintains a strict separation. "Local counsel preparing Swiss supplementary submission" is a live item — it needs tracking. "Decision whether to split Czech to Phase 3 or re-sequence" is an open decision — it needs someone's attention. Conflating them loses the critical signal.

**Tacit knowledge (Mode 4).** The "What is not visible in the matter files" section is the hardest and most valuable part of the handoff briefing. Relationship dynamics, unwritten context, partner preferences, client quirks, patterns of behaviour on the other side. This section is populated only from content the outgoing LPM provides directly — never inferred from correspondence, never fabricated from domain knowledge. If the outgoing LPM has not provided this content, the skill prompts for it explicitly. This is the one area where a placeholder is not acceptable.

**Cross-matter context.** Limited to genuine connections from input data — shared partner, shared LPM, same client, regulatory overlay. If none present, the skill states "No notable cross-matter context" and moves on. Manufacturing connections from matter-type assumptions is a fabrication path the skill prohibits.

**Attribution.** Substantive analysis or recommendations from named individuals are attributed by name. Generic attribution to "the team" is the failure mode.

## M365 connected mode

Connected mode queries the matter folder in Outlook and retrieves correspondence without user paste. Default retrieval windows vary by mode: 7 days (Modes 1–2), last partner touchpoint via Calendar (Mode 3), 30 days minimum (Mode 4). The "what is not visible in the files" section in Mode 4 still requires the outgoing LPM's direct input — connected mode cannot generate tacit knowledge.

All modes operate fully on pasted input. Connected mode is an efficiency enhancement, not a prerequisite.

## Skills this one works with

| Direction | Skill | Relationship |
|---|---|---|
| Invoked from | `daily-briefing` | Single-matter zoom-in from portfolio briefing |
| Triggers | `status-report-drafter` | Status report for distribution |
| Triggers | `scope-change-controller` | Scope signal requiring formal assessment |
| Triggers | `risk-and-issues-manager` | RAID update |
| Triggers | `budget-and-fee-manager` | Detailed financial analysis |
| Triggers | `local-counsel-manager` | LC escalation or non-response |
| Triggers | `stakeholder-comms-planner` | Client comms plan or deck |
| Triggers | `timeline-generator` | Timeline impact analysis |
| Triggers | `resource-planner` | Team or cover arrangements |

`matter-drill-down` is invoked from `daily-briefing`, from LPMHub, or directly. It consumes portfolio context where available and hands off to single-matter skills for follow-through.

## Design principles applied

This skill applies the [LPM Core Plugin design principles](../README.md), including:

- **Document output by default** — drill-downs are .docx working documents, produced on invocation without conditional offers
- **Working surface, not communications artefact** — register and structure designed for LPM consumption, not for circulation
- **Template skeleton for document outputs** — each mode has an explicit output template the skill populates, not an output it decides whether to produce
- **Automate capture, surface for confirmation** — in connected mode, the skill retrieves and structures; the LPM confirms and acts
- **LPM vs attorney boundary** — surfaces items requiring attorney judgment via the Partner Attention section but does not offer legal analysis
- **Attribution to named individuals** — substantive analysis attributed by name, not generalised to "the team"
- **Tacit knowledge elicitation (Mode 4)** — the skill prompts for unwritten context rather than inferring it, because inferred tacit knowledge is worse than missing tacit knowledge

## Licence

Apache 2.0. See [LICENSE](../../LICENSE).
