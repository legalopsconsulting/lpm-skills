---
name: matter-drill-down
description: Produces an LPM working view on a single matter — a focused zoom-in for the LPM's own operational use, not for distribution. Structured around deliverables (what is due, when, to whom), issues (current problems requiring action), and risks (plausible future problems requiring monitoring). Use when the user asks "drill into [matter]", "brief me on [matter]", "focus on [matter]", "zoom into [matter]", "prep me for [partner] call on [matter]", "I'm handing [matter] to [name]", "leave cover on [matter]", "taking over [matter]", or pastes single-matter correspondence asking for a working view. Four modes: standard drill-down, decision-first, partner prep, handoff briefing. Not for status reports for distribution (use status-report-drafter) or portfolio views across multiple matters (use daily-briefing). Produces a .docx working view saved to the matter folder.
license: Apache-2.0
metadata:
  author: LegalOps Consulting
  version: 1.0.0
  plugin: LPM Core
---

# matter-drill-down

Working view on a single matter for the LPM's own operational use. Structured around three primary elements: deliverables, issues, and risks. Supporting context orients the reader enough to form questions of others — it does not try to answer every question itself.

The skill is different from `status-report-drafter` in that the output is for the LPM, not for a partner or client audience. Different register, different structural choices, different expectation of distribution. The drill-down is a working surface; the status report is a communications artefact.

The skill operates in four modes. Standard drill-down (Mode 1) is the default — the LPM has decided to focus on one matter and wants the full working picture. Decision-first (Mode 2) narrows the view to open decisions only. Partner prep (Mode 3) reshapes the template for an upcoming partner call on the matter. Handoff briefing (Mode 4) produces the briefing a receiving LPM needs to take over a matter without losing continuity — a constantly-triggered need that is currently painful to do and frequently skipped despite its operational value.

## When to use this skill

- The user pastes single-matter correspondence and asks for a working view
- The user asks for a zoom-in from a portfolio briefing — "drill into [matter]", "focus on [matter]"
- The user is preparing for a partner call on a matter
- The user is going on leave, handing a matter over, or onboarding someone new to a matter

For portfolio-level views across multiple matters, use `daily-briefing`. For audience-facing status reports, use `status-report-drafter`.

## Input Classification (apply before mode selection)

**Step 1 — Matter count.** Scan inputs for matter identifiers, client names, or matter-specific context.
- If inputs are about a single matter → this skill applies. Proceed to Step 2.
- If inputs span two or more matters → route to `daily-briefing`.

**Step 2 — Mode routing.** Identify the user's invocation pattern:
- "Handing over", "leave cover", "taking over", "bringing [name] onto", "going on leave" → Mode 4
- "Prep me for", "partner call", "before the call with" → Mode 3
- "Decisions only", "what do I need to decide on", "open decisions" → Mode 2. **Mode 2 produces a .docx document using the Mode 2 Template Variation. It does not produce conversational prose or advisory paragraphs. Produce the document, not a chat answer.**
- Any other single-matter drill-down request → Mode 1 (default)

**Step 3 — Audience check.** If the user specifies the output is for a partner or client audience (e.g. "for JMW to send to the client", "status report for the partner", "client-facing update"), this is the wrong skill. Do not produce any output. Do not produce a status report. Do not produce a client-facing document. Do not read the docx skill. Instead, respond with exactly this pattern and stop:

"This is a [status report / client-facing update] for [audience]. That's status-report-drafter, not a drill-down. Run status-report-drafter on [matter] ([matter number]) with the same inputs."

The failure mode is detecting the audience, deciding you can produce the document anyway, and doing so. That is gate-skipping. The correct behaviour is to refuse and route, even though you could produce the document.

**Step 4 — Input tagging.** If the user has tagged inputs by source (`[FROM LC]`, `[INTERNAL]`, `[CLIENT]`, `[PARTNER]`), preserve the tags in attribution.

## Before Starting Any Mode

**Matter identifiers.** Client name, client number, matter name, matter number. Required in every output header. If not provided in inputs, ask once: *"Confirm matter identifiers (client name, client number, matter name, matter number) before I produce the working view."* Hard gate — do not produce until confirmed or explicit placeholder agreement given.

**Current phase and RAG.** Required. If not in inputs, infer from correspondence and flag the inference.

**Invocation context.** State explicitly why the drill-down is being produced: portfolio briefing handoff, LPMHub click-through, direct ask, upcoming partner call, handoff preparation. Include in output header.

**Receiving LPM (Mode 4 only).** If Mode 4 invocation, identify the receiving LPM. If not provided: *"Who is receiving the matter? (Name required for handoff briefing.)"*

**Call context (Mode 3 only).** If Mode 3 invocation, identify the partner and the call purpose. If not provided: *"Which partner and what is the purpose of the call?"*

## Boundary

This skill produces a **working view on one matter for the LPM's own consumption**. It does not:

- Produce status reports for distribution (use `status-report-drafter`)
- Produce portfolio-level briefings (use `daily-briefing`)
- Update RAID logs (use `risk-and-issues-manager`)
- Draft scope change memos (use `scope-change-controller`)
- Produce budget variance analysis (use `budget-and-fee-manager`)
- Produce stakeholder communications plans (use `stakeholder-comms-planner`)

If the user asks for any of these, route to the appropriate skill and do not produce a drill-down.

## Operating Modes

### Mode 1 — Standard drill-down (default)

**Fires when:** User requests a single-matter working view without a more specific invocation pattern.

**Input:** Correspondence, call notes, matter baseline, current-state context for one matter.

**Output:** Working view using the standard template (below). 2–3 pages.

### Mode 2 — Decision-first

**Fires when:** User asks "what do I need to decide on [matter]", "open decisions on [matter]", "[matter] — decisions only".

**Input:** Same as Mode 1.

**Output:** Produce a .docx working view using the Mode 2 Template Variation below. Do not produce conversational prose, advisory paragraphs, or a list of decisions as chat output. The output is a structured document with an identifier header, expanded decision entries in the template format, and retained Issues and Risks tables. Deliverables and supporting orientation sections collapsed to one line each. Do not end with a question or offer.

### Mode 3 — Partner prep

**Fires when:** User is preparing for a partner call on the matter — "prep me for [partner] call", "before the call with [partner]", "pre-call on [matter]".

**Input:** Same as Mode 1, plus context on the upcoming call (partner, purpose, timing).

**Output:** Standard template reshaped for the call:
- Deliverables and Issues sections expanded around what the partner needs to know or decide
- Risks section retained but framed as "risks the partner should be aware of"
- Additional section: **Decisions required from the partner in this call**
- Additional section: **Information the partner may not yet have**
- Additional section: **Likely partner questions with prepared answer lines**
- Mini-briefing, financial position, stakeholder state retained as supporting context

### Mode 4 — Handoff briefing

**Fires when:** User is handing a matter to another LPM — "handover on [matter]", "I'm handing [matter] to [name]", "leave cover on [matter]", "taking over [matter]", "bringing [name] onto [matter]".

**Input:** Same as Mode 1, plus identification of the receiving LPM, plus (where possible) the outgoing LPM's knowledge of the matter that is not in the files.

**Domain knowledge specific to Mode 4:** Handoff briefings are a constantly-triggered operational need. Leave cover, role transitions, and matter reallocations happen continuously. The briefing is universally painful to produce — it takes time the outgoing LPM does not have — and is frequently skipped despite the operational value of doing it well.

The skill's job in Mode 4 is to make the handoff fast enough that it actually happens. The template prioritises the content that matters most to a receiving LPM picking up the matter cold:

1. **Deliverables over the next 2–4 weeks** — what is due, when, to whom. This is the operational spine the receiving LPM needs to not drop anything.
2. **Issues — current** — what is in flight that needs continued management. Status and context for action.
3. **Risks — plausible future** — what might come up in the handoff window. Context for mitigation.
4. **Outstanding commitments the outgoing LPM has made** — the things said in emails, on calls, in meetings that are not yet done but have been promised.
5. **What is not visible in the matter files** — the tacit knowledge. Relationship dynamics with the client, unwritten context on partner preferences, patterns of behaviour on the other side, things the outgoing LPM knows but has not documented anywhere.
6. **Who to call** — by issue type. If scope questions arise, call X. If a billing question comes up, call Y. If the client pushes back on something, start with Z.

**Output:** Extended template (below). Longer than Mode 1 — 4–6 pages is acceptable because the handoff briefing is the complete operational transfer document.

## Standard Template (Mode 1)

Produce the template sections in this exact order.

```
MATTER DRILL-DOWN — [Matter short name]

Client:           [Client name] ([Client No.])
Matter:           [Matter name] ([Matter No.])
Lead Partner:     [Initials or name]
Lead LPM:         [Name]
Phase:            [Current phase and position]
RAG:              [Green / Amber / Red]
Fee model:        [Fixed fee / T&M cap / Phased / etc.]
WIP / Budget:     [Current WIP] / [Budget]
Prepared:         [Date and time]
Invocation:       [Why this drill-down is being produced]

SUMMARY
[2–3 sentences. Direct, no hedging. Current position. The one or
two dynamics shaping the week. The next decision point.]

DELIVERABLES — DUE THIS WEEK AND NEXT
| # | Deliverable | Owner | By when | Status |
|---|---|---|---|---|

ISSUES — CURRENT
| Issue | Status | Context for action |
|---|---|---|

RISKS — PLAUSIBLE FUTURE
| Risk | Signal | Mitigation context |
|---|---|---|

OPEN DECISIONS
| # | Decision | Owner | By when | Current state |
|---|---|---|---|---|

SCOPE SIGNALS
Active scope signals on this matter. If none, state "No active
scope signals" and move on.

| Signal type | Driver | Status | Handoff |
|---|---|---|---|

FINANCIAL POSITION
One paragraph. WIP against plan, variance and its nature (structural 
vs substantive), forward exposures. Do not reproduce full variance 
analysis here — hand off to `budget-and-fee-manager` for detail.

TEAM AND STAKEHOLDER STATE
Internal team: [1–3 lines — who is on, current load, staffing watch items]
Client side: [1–3 lines — who is engaging, current tone, any changes]
External counsel: [1–3 lines — LC status by jurisdiction, escalations]

CROSS-MATTER CONTEXT
How this matter connects to others in the portfolio. Shared partner,
shared LPM, same client, regulatory overlay, counterparty. If no
notable connections, state "No notable cross-matter context" and
move on. Do not invent connections.

HANDOFFS
Single-matter skills to invoke as follow-through.

| Skill | Trigger | Priority |
|---|---|---|

End of drill-down.
```

**Output rule:** Produce from available information. Use placeholders for unknowns. Do not withhold pending matter identifiers — ask once, then produce. Do not end with "want me to produce this as a .docx?" — produce the .docx.

**Attribution rule:** Substantive analysis or recommendations from named individuals are attributed by name. Do not generalise to "the team".

## Mode 2 Template Variation (Decision-first)

**Produce the decision-first working view as a .docx using the template below. Do not produce conversational prose, advisory commentary, or a list of decisions in paragraph form. The output is a structured document with an identifier header, expanded decision entries, and retained Issues and Risks tables. Do not end with a question or offer.**

Same header. Collapse Deliverables, Team state, Financial position, Cross-matter context to one line each. Expand:

```
OPEN DECISIONS — EXPANDED

For each decision:
- Decision statement
- Owner and by-when
- Options under consideration
- Current state (what is known, what is pending)
- What is blocking progress
- LPM recommendation (if applicable)

ISSUES — CURRENT
[Standard table, retained — issues constrain decisions]

RISKS — PLAUSIBLE FUTURE
[Standard table, retained — risks inform decisions]
```

## Mode 3 Template Variation (Partner prep)

Same header with **Partner**, **Call purpose**, **Call timing** added.

```
SUMMARY
[2–3 sentences. Frame specifically around the call.]

DECISIONS REQUIRED FROM THE PARTNER IN THIS CALL
| Decision | Options to consider | LPM recommendation | Why now |
|---|---|---|---|

INFORMATION THE PARTNER MAY NOT HAVE
Items that have come in direct to the LPM, client-side dynamics the 
partner has not seen, emerging risks the LPM has spotted. Flagged as 
"worth raising".

| Item | Source | Why the partner should know |
|---|---|---|

LIKELY PARTNER QUESTIONS WITH PREPARED ANSWER LINES
3–5 questions the LPM anticipates the partner asking. Each with a 
prepared answer line — not a script, a prompt.

| Question | Answer line |
|---|---|

DELIVERABLES — DUE THIS WEEK AND NEXT
[Standard table]

ISSUES — CURRENT
[Standard table]

RISKS — PLAUSIBLE FUTURE
[Standard table]

SUPPORTING CONTEXT
One paragraph each: current financial position, team state, client-side 
activity. Enough to orient the partner if they ask.

HANDOFFS
[Standard table]
```

## Mode 4 Template Variation (Handoff briefing)

Same header with **Handoff from**, **Handoff to**, **Effective date** added.

```
SUMMARY
[3–5 sentences. What this matter is. Where it is today. What is 
coming up in the handoff window. Anything the receiving LPM 
should know before opening the matter files.]

DELIVERABLES — NEXT 2–4 WEEKS
The operational spine of the handoff. The receiving LPM needs to not 
drop any of these.

| # | Deliverable | Owner | By when | Status | Context |
|---|---|---|---|---|---|

ISSUES — CURRENT
Problems in flight that need continued management. Context sufficient 
for the receiving LPM to either act or form questions.

| Issue | Status | Mitigation in progress | What is needed next |
|---|---|---|---|

RISKS — PLAUSIBLE FUTURE
Problems that may materialise in the handoff window. Context for 
mitigation.

| Risk | Signal | Mitigation context | Watch this specifically |
|---|---|---|---|

OUTSTANDING COMMITMENTS
Commitments the outgoing LPM has made that the receiving LPM must 
honour. From emails, calls, meetings — not necessarily documented 
in a tracker.

| Commitment | To whom | By when | Context |
|---|---|---|---|

WHAT IS NOT VISIBLE IN THE MATTER FILES
Do not populate this section from inference or from the 
correspondence. This section contains only content the outgoing 
LPM provides in response to direct prompts. If the outgoing LPM 
has not provided this content, replace this entire section with 
the prompting questions listed in Domain Knowledge below. Do not 
fabricate tacit knowledge. Do not infer relationship dynamics, 
communication preferences, or partner behaviour from the tone or 
content of emails.

The tacit knowledge. Relationship dynamics, patterns of behaviour, 
unwritten context, partner preferences, client quirks. The 
outgoing LPM knows these; they are not in the documents.

Examples of what to include:
- How specific client contacts prefer to be communicated with
- Patterns of behaviour on the other side (counterparty, LC, regulator)
- Partner preferences on briefings, updates, and escalation timing
- Client-side politics the receiving LPM should be aware of
- Items the partner knows but that are not in correspondence

WHO TO CALL
By issue type. Name the person, not the role.

| If this comes up | Call | Context |
|---|---|---|

CURRENT FINANCIAL POSITION
Brief. WIP, plan, current variance and its nature, forward 
exposures, any fee conversations pending.

STAKEHOLDER TONE SNAPSHOT
Current tone of relationships with key stakeholders. One line each.

- Client GC: [tone and current engagement]
- Client deal lead: [tone and current engagement]
- Lead partner: [posture on matter, any watch items for the LPM relationship]
- Key external counsel: [tone, responsiveness, any issues]

SCHEDULED TOUCHPOINTS — NEXT 4 WEEKS
Calls, meetings, deliverable dates, external milestones.

HANDOFFS
Single-matter skills to invoke as follow-through (e.g. for the 
first week of the receiving LPM's tenure).

| Skill | Trigger | Priority |
|---|---|---|

End of handoff briefing.
```

## Domain Knowledge

### Working view, not report

The output is for the LPM's consumption. No managed-confidence tone. No softening language. No partner-sign-off framing. If the matter is at 91% of cap with Phase 3 not started, say so plainly. If the partner has not delivered on a Friday commitment, say so.

The failure mode is the drill-down drifting into status-report tone. Once it looks like a report, it gets used like a report — circulated, sanitised, partner-reviewed. That is not what this skill produces.

### Open decisions vs live items

Open decisions are pending judgments — someone needs to decide something. Live items are actions underway — things in motion, deliverables in train.

A drill-down that conflates them loses the critical signal. "Local counsel preparing Swiss supplementary submission" is a live item (deliverable). "Decision whether to split Czech to Phase 3 or re-sequence" is an open decision. The first needs tracking; the second needs someone's attention.

In Modes 1, 3, and 4, both appear but in different sections. In Mode 2, open decisions are the spine.

### Issues vs risks — the taxonomy matters

Same taxonomy as `daily-briefing` and `risk-and-issues-manager`:

- **Issues** are confirmed problems requiring action now
- **Risks** are plausible future problems requiring monitoring

Silence on its own is a risk. Confirmation promotes it to an issue.

### Deliverables with dates and owners

The test for whether a deliverable row earns its place is: does it have a date and an owner? If yes, it is a deliverable. If no, it is either an aspiration or a topic. Deliverables without dates and owners do not appear in the deliverables section — they either get assigned in the output or are moved to Issues/Risks as appropriate.

### Financial position — headline only

Section 6 (Financial Position) is one paragraph. WIP against plan, variance and its nature, forward exposures. Do not reproduce detailed variance analysis — the LPM invokes `budget-and-fee-manager` for that.

### Cross-matter context — no invention

Cross-matter context is limited to genuine connections: shared partner, shared LPM, same client, same regulatory overlay, same counterparty. If none present, state "No notable cross-matter context" and move on. Do not manufacture connections. Do not generate cross-matter context from matter-type assumptions or general knowledge. Cross-matter context comes only from input data about other specific matters. If no other matter data is provided, state "No notable cross-matter context" and move on. The fabrication path is inventing plausible connections from the matter type — do not do this.

### Mode 4 — what is not visible in the files

The hardest and most valuable section of the handoff briefing. Relationship dynamics, unwritten context, patterns of behaviour, tacit knowledge. Prompts for the outgoing LPM:

- Is there a client contact with specific communication preferences? (How short should emails be? Does she prefer a morning or afternoon call? Is there a tone that works and one that doesn't?)
- Is there a partner preference worth noting? (Does JMW want briefing 20 minutes before client calls? Does MKT dislike surprises in steering committees? Does AHL want analysis memos or bulleted summaries?)
- Is there a pattern on the other side? (Does the opposing counsel typically respond within 48 hours, or are they chronically slow? Has the client GC historically pushed back on fee letters?)
- Is there client-side politics? (Is the deal lead aligned with the GC, or is there friction? Is the CFO a blocker on finance decisions?)
- Are there items the partner knows but that are not documented? (Conversations between partners at a dinner, a board-level conversation, a prior relationship history with the client?)

If the outgoing LPM does not provide this content, the skill prompts for it explicitly before producing Mode 4. This is the one area where a placeholder is not acceptable — the receiving LPM needs the tacit knowledge or the handoff has failed.

### Attribution to named individuals

Substantive analysis or recommendations from named individuals are attributed by name in the relevant section. Generic attribution to "the team" is the failure mode.

## Output Format

**.docx by default.** All outputs are .docx unless the user explicitly requests markdown.

**Produce, do not ask.** Produce on invocation. No conditional offers.

**Label is "SUMMARY", not "BLUF".**

**No preamble.** Output opens with the identifier header.

**Placeholders for unknowns** (except Mode 4 "what is not visible" — see above).

## LPM vs Attorney Boundary

Drill-downs surface matters requiring attorney judgment (legal strategy, client advice framing, privileged communications) but do not offer legal analysis. The skill routes those items to the lead partner for decision via the Partner Attention section — it does not opine.

## Cross-Skill Handoffs

matter-drill-down is invoked from `daily-briefing`, from LPMHub, or directly. It hands off to:

- Formal scope change assessment → `scope-change-controller`
- RAID update → `risk-and-issues-manager`
- Status report for distribution → `status-report-drafter`
- LC escalation or non-response pattern → `local-counsel-manager`
- Detailed financial analysis → `budget-and-fee-manager`
- Client comms plan or deck → `stakeholder-comms-planner`
- Timeline impact analysis → `timeline-generator`
- Team or cover arrangements → `resource-planner`

Each handoff in the output names the trigger and priority.

## M365 Connected Mode

**Mode 1 (Standard drill-down).** Connected mode queries the single matter folder in Outlook, retrieves correspondence in a default window (last 7 days unless user specifies), and produces the drill-down without user paste.

**Mode 2 (Decision-first).** Same retrieval pattern.

**Mode 3 (Partner prep).** Same retrieval pattern, plus Calendar integration (if available) to identify the last touchpoint with the named partner.

**Mode 4 (Handoff briefing).** Extended retrieval window — last 30 days minimum — to capture outstanding commitments and pattern signals. The "what is not visible in the files" section still requires the outgoing LPM's input; connected mode cannot generate that content.

**Manual mode fallback.** All four modes operate fully on pasted input. Connected mode is an efficiency enhancement.

**Future connectors.** A DMS or practice management system connector would enable matter baseline retrieval (phase, fee model, WIP) from the system of record. A Calendar connector would improve Mode 3 quality by identifying last-partner-touchpoint directly. Both are Phase 3.

## Time-Sensitive Assumptions

- Matter identifier format assumes Intapp Open or equivalent practice management system
- Connected mode patterns assume M365/Outlook
- Mode 4's tacit knowledge elicitation assumes the outgoing LPM is available to respond to prompts. If the outgoing LPM is unavailable (sudden leave, departure), Mode 4 output is necessarily incomplete and the skill flags this explicitly.
