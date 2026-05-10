# Output templates

Templates for the three report formats this skill produces, plus the framing principles that govern which one to use and how to write into them.

**Document orientation: A4 portrait, all report types.** If the workstream table has more than five columns, reduce column width or wrap text within cells — do not switch the document to landscape. All outputs from this skill are A4 portrait regardless of table width.

**RAG cell shading — mandatory.** In every workstream status table, the Status cell for each row must be shaded with the RAG colour using `ShadingType.CLEAR` and the following hex fills. Apply to the Status cell only — not the entire row.

| Status | Fill hex | 
|---|---|
| GREEN | `70AD47` |
| AMBER | `FFC000` |
| RED | `FF0000` |

Status text in shaded cells should be bold and white (`FFFFFF`) for Green and Red; bold and black (`000000`) for Amber. Apply the same shading to the Overall Status cell in the identifier block.

## Contents

1. Weekly internal update — template
2. Monthly client/executive report — template
3. Ad hoc escalation briefing — template
4. Internal vs client-facing — two different reporting philosophies
5. Financial status in the status report
6. Conditional appendices — chaser emails

---

## 1. Weekly internal update

Operational focus. What happened, what's next, what's blocked. Read under time pressure — Items Requiring Attention sits before the workstream table because partners need to know what they need to do before they need the full picture.

The template separates partner-facing narrative (Items Requiring Attention) from the operational tracker (Action Tracker, later in the report). They have different audiences and different jobs: the partner reads the narrative for decisions; the LPM uses the tracker as the week's chase list. Scope Signals and Cross-Skill Handoff Notes are optional sections — include when there is something to populate, omit when not.

```
# [Matter Name] — Weekly Status Update

| Client | [Name] | Client number | [Number] |
|---|---|---|---|
| Matter | [Name] | Matter number | [Number] |
| Period | [dates] | Overall status | [RAG] |
| Prepared by | [LPM name] | Date | [DD Month YYYY] |

## Summary
[2-3 sentence executive summary — the "if you read nothing else" paragraph]

## Items Requiring Attention
[Partner-facing narrative discussion of items needing decisions, approvals, or commercial input. Each item written out with context, options where relevant, and recommended action. Numbered list works well. This is the read-before-everything-else section — keep it tight, but don't compress it into bullets if the issues need explaining.]

## Workstream Status
| Workstream | Status | Key Update | Next Steps | Target Date | Escalation |
|---|---|---|---|---|---|
| [Name] | [RAG] | [What changed] | [What's coming] | [When] | [If applicable] |

## Financial Summary (if applicable)
[Budget vs actual, burn rate, forecast to complete. Variance commentary explains causes, not just numbers. Deeper analysis hands off to budget-and-fee-manager.]

## Scope Signals (optional — include only when relevant)
[Forward-looking flag for items that aren't yet formal scope changes but warrant tracking as candidates. Each entry: signal, severity (LOW/MEDIUM/HIGH), assessment status, expected resolution. Confirmed scope changes are processed through scope-change-controller; this section captures the leading indicators so they don't surprise anyone when they crystallise.]

## Cross-Skill Handoff Notes (LPM Use)
[Internal notes for the LPM. Which adjacent skills are triggered by items in this report, and what to feed into them. One line per handoff. Examples: scope-change-controller (confirmed or candidate OOS items); budget-and-fee-manager (variance requiring detailed analysis); timeline-generator (programme-level critical-path impact); risk-and-issues-manager (RAID log updates); stakeholder-comms-planner (communications triggered by status change). **This section must be stripped from any client-facing version of the report.**]

## Action Tracker
| # | Action | Owner | Due | Status | Dependency / Notes |
|---|---|---|---|---|---|
| 1 | [Specific action] | [Name] | [Date] | [Open / Done] | [What it depends on] |

[Operational reference table. More granular than Items Requiring Attention — captures every action across the matter, not just the partner-decision items. Used by the LPM to chase during the week.]

## Next Period Outlook
[What's expected to happen, what milestones are approaching, what decisions are due]
```

---

## 2. Monthly client/executive report

Strategic focus. Are we on track overall, what patterns are emerging, what decisions are needed.

```
# [Matter Name] — Monthly Status Report

| Client | [Name] | Client number | [Number] |
|---|---|---|---|
| Matter | [Name] | Matter number | [Number] |
| Period | [month] | Overall status | [RAG] |
| Prepared by | [LPM name] | Date | [DD Month YYYY] |

## Executive Summary
[One paragraph: overall trajectory, key achievements, primary concerns, decisions needed]

## Progress Highlights
[What was accomplished — frame positively but accurately]

## Workstream Overview
[Higher-level than weekly — trends and trajectories rather than task-level detail]

## Financial Position
[Budget vs actual with variance commentary explaining the why, not just the numbers]
[Forecast to complete — what the total spend will be, not just what's spent so far]

## Risks and Issues
[Active risks with mitigation status — constructive framing, not alarmist]

## Decisions Required
[Specific decisions needed from the audience, with context and recommended action]

## Outlook
[Forward-looking: next period priorities, upcoming milestones, anticipated challenges]
```

---

## 3. Ad hoc escalation briefing

Concise, specific, decision-oriented. Used for one-off briefings on a single workstream or issue.

```
# [Matter Name] — [Workstream] Status Briefing

| Client | [Name] | Client number | [Number] |
|---|---|---|---|
| Matter | [Name] | Matter number | [Number] |
| Date | [briefing date] | Status | [RAG] |
| Prepared by | [LPM name] | Date | [DD Month YYYY] |

## Current Position
[What's happening right now — 3-4 sentences max]

## Recent Activity
[Key events in the last [period] — chronological, factual]

## Open Items
[What's unresolved, what's blocking progress]

## Recommendation
[What action should be taken and by whom]
```

---

## 4. Internal vs client-facing — two different reporting philosophies

These are not the same report with different tone. They serve fundamentally different purposes and follow different structures. When converting an internal report into a client-facing version, do not simply soften the language — restructure for the different audience.

### Internal reports (LPM to lawyer/partner) — management by exception

Everything is assumed to be fine unless flagged. The report exists to surface problems, drive actions, and get decisions. Green workstreams get a one-line confirmation or are omitted entirely — don't waste the partner's time on things that are working. Go straight to what's Amber or Red, what's stalled, what needs a decision. Directness is a feature: "Germany is 3 weeks behind and we don't have a recovery plan" is exactly the right register. The audience wants to know what's broken and what they need to do about it.

Internal reports should:
- Lead with exceptions, risks, and items requiring decisions
- Be direct about problems without softening
- Focus on actions needed and owners assigned
- Include operational detail (fee-earner-level data, internal resourcing, team performance)
- Flag items the partner needs to raise with the client before the client discovers them independently

### Client-facing reports (firm to client) — managed confidence

The report exists to demonstrate that the programme is under control and to give the client visibility on things that affect them. The client typically has limited capacity for detail — they want to see that progress is being made, that the firm has the programme in hand, and that anything requiring their attention is clearly flagged with context.

Issues are only raised when the client needs to know — either because the issue affects their timeline/cost, because they need to take action (provide data, make a decision, give approval), or because the issue is material enough that they'd be unhappy learning about it after the fact. When issues are raised, they are always framed in terms of impact and mitigation: not "there's a problem" but "we've identified [issue], the impact is [X], and we are [doing Y] to resolve it / we need [Z] from you to proceed."

Client reports should:
- Lead with progress highlights and achievements — the client is paying for this work and wants to see it moving
- Report on all workstreams including Green ones — the client wants the full picture, not just exceptions
- Raise issues in impact-and-mitigation framing: what happened, what it means for the programme, what the firm is doing about it, and what (if anything) the client needs to do
- Never surprise — if a problem is going to affect the client, they hear it from you in a structured report, not sideways in an email chain
- Remove all internal commentary: team performance, resourcing challenges, internal politics, write-off discussions, realisation rates
- Adjust financial detail to what the client sees — typically total budget vs actual with high-level variance commentary, not fee-earner breakdowns
- Include a clear "decisions required from you" section so the client knows exactly what they need to act on

### Jurisdiction credibility in client reporting

When assessing whether a sparse update warrants concern in a client report, consider three factors: the predictability of the jurisdiction's regulatory process, the local team's track record on this matter, and the complexity of the requirements in that jurisdiction. Well-established regulatory regimes with experienced local teams warrant more latitude on sparse updates — the vagueness is an internal communication issue, not a client concern. Jurisdictions where the process is less predictable, the team is less proven, or the regulatory requirements are more complex warrant more caution before reporting positively to the client. The LPM applies their own jurisdiction knowledge here — the framework supports the judgment, it does not replace it.

### Internal coordination gaps are never client-facing risks

If a local team or external counsel hasn't responded to a status request, that's a coordinating counsel problem to manage internally. It almost always resolves quickly. Never present "we haven't heard from our own team" as a risk to the client — it undermines confidence in programme management. Report these workstreams neutrally ("update to follow in next reporting period") and chase internally.

### What stays the same across both

- Accuracy — never misrepresent status externally
- If it's Red internally, it's Red externally (the framing differs, not the assessment)
- Key dates and milestones
- The underlying facts

---

## 6. Conditional appendices

Include the following appendices only when the triggering condition is met. Omit entirely when the condition is not present.

### Appendix A — Chaser emails

**Trigger:** One or more parties — internal workstream leads, external local counsel, or client-side contacts — are flagged as non-responsive in the Workstream Status table or Action Tracker (Amber or Red on silence grounds, or an action overdue with no update received). Draft one chaser per non-responsive party.

**Register by relationship:**
- External local counsel: formal, specific, deadline-explicit
- Internal workstream lead: direct and collegial, no formality
- Client-side contact: professional, framed as a coordination request, never as a chase

**Template — external local counsel:**

Subject: [Matter name] — [workstream] — outstanding query

Dear [contact name / team],

We are writing in connection with [matter name], specifically the [workstream] workstream. We sent a request on [date] regarding [specific query] and followed up on [dates of chasers]. We have not yet received a substantive response.

We need your input by [deadline] in order to [downstream dependency].

Please confirm receipt and provide an expected response date. If there is a reason for the delay we are not aware of, please let us know.

[Sign-off]

**Template — internal workstream lead:**

[Name] — can you send through an update on [workstream / specific query] by [deadline]? We need it to [downstream dependency]. Let me know if there's a blocker I should know about.

[Sign-off]

**Template — client-side contact:**

Subject: [Matter name] — [topic] — update request

Dear [name],

I wanted to follow up on [specific request / information needed] sent on [date]. We need this to [downstream dependency / next step in the programme]. Could you let me know the expected timing for this?

Happy to jump on a call if that's easier.

[Sign-off]

**Drafting rules (all types):**
- Populate deadline and downstream dependency from the Action Tracker entry for this item.
- Address to named contact where known; "Dear [firm] team" where contact name is not in the source material.
- If the matter lead has agreed to escalate directly (e.g. call a managing partner), add a header note: "For reference only — [name] escalating by [method] on [date]. Send only if escalation does not produce a response."
- Never draft a chaser to a client contact without flagging it to the matter lead before sending.

---

## 5. Financial status in the status report

The status report includes a financial summary section, but it does not perform deep financial analysis. That is the domain of the budget-and-fee-manager skill, which handles accounting system data interpretation, variance analysis, forecast-to-complete calculations, and commercial recommendations.

### What the status report does with financial data

When financial data is provided (pasted WIP figures, uploaded budget tracker, or output from budget-and-fee-manager):

- Present a summary table: workstream, budget, actual, variance %, and a one-line assessment
- Flag any workstream where spend is disproportionate to progress — this is the key indicator. 85% of budget consumed at 50% completion is a red flag regardless of whether the budget is technically exceeded
- Note where financial data is absent — "no financial data provided for this period; recommend requesting WIP position from all workstreams ahead of the next financial review"
- For client reports: present high-level budget vs actual with brief variance commentary

### Financial disclosure sequencing for client reports

Do not flag specific overrun amounts to the client until the numbers are reconciled and any write-offs are processed. Until then, frame cost variances as "increased fees due to [root cause]" — acknowledge the variance exists and explain why, but don't present a specific number that may change after reconciliation. Present final numbers in the next formal financial report once the position is confirmed.

### What the status report hands off

- Root cause variance analysis → budget-and-fee-manager
- Forecast-to-complete calculations → budget-and-fee-manager
- Commercial recommendations (absorb vs recover, OOS fee adjustments) → budget-and-fee-manager, potentially triggering scope-change-controller
- Realisation analysis, write-off tracking → budget-and-fee-manager
- Query/chase loops with teams about anomalous WIP amounts → budget-and-fee-manager

When detailed financial analysis already exists (from budget-and-fee-manager or the LPM's own work), the status report should consume and summarise it rather than re-analyse from raw data. Reference the source: "Financial position per the February WIP review [date]."
