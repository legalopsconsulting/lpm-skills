# Build Log: matter-drill-down

**Skill:** matter-drill-down (LPM Core plugin extension — portfolio layer, single-matter zoom-in)
**Plugin:** LPM Core
**Built:** 19 April 2026
**Phase 3 pass:** 11 May 2026
**Status:** Phase 3 complete (calendar integration — Mode 3 and Mode 4). Phase 2 status: 4 PASS, 1 PARTIAL (TP-2 restraint — minor), 2 V1 LIMITATION (TP-5 Mode 2, TP-6 audience routing), 1 FAIL low-risk (TP-8 identifier gate).
**Line count:** 470 / 500 limit
**Description character count:** 867 / 1024 limit (unchanged)
**Version:** 1.1.0

---

## Build Timeline

1. Read reference materials: `skill-build-process-template-v1.md`, `matter-intake-scoping-build-log.md` (canonical pattern), status-report-drafter boundary language via `lpm-plugin-planning-v1_7.md`, daily-briefing SKILL.md (adjacent skill — this skill is invoked from daily-briefing Mode 2 routing).
2. Confirmed user's calibration on Mode 4 (handoff briefing): handoff situations happen constantly — leave cover, role transitions, matter reallocation, onboarding — and the process is universally painful to do and frequently skipped despite clear operational value. Mode 4 is therefore load-bearing for v1, not a nice-to-have.
3. Confirmed user's calibration on output shape for Mode 4 specifically: deliverables with dates and owners + existing and potential future issues with enough context for the receiving LPM to mitigate and to ask questions of others. Supporting orientation context is subordinate.
4. Generalised the deliverables/issues/risks spine to all four modes — this is the structural commitment for the skill, not a Mode 4 specific pattern.
5. Confirmed LPM-grade-generic framing — handoffs happen at every grade, not only senior.
6. Confirmed four modes: standard drill-down (Mode 1), decision-first (Mode 2), partner prep (Mode 3), handoff briefing (Mode 4). All four retain the deliverables/issues/risks spine with different emphasis per mode.
7. Applied design principles: DP-26 input classification (single-matter vs multi-matter vs audience check), DP-27 template skeletons as populated templates, produce-don't-ask, Summary label, identifier gate (harder than daily-briefing — matter identifiers required before production).
8. Encoded Mode 4 domain knowledge specifically: the section "what is not visible in the matter files" is the high-value tacit knowledge transfer. Prompted explicitly — this is the one section where placeholders are not acceptable; the skill asks the outgoing LPM for this content.
9. Encoded the five named sections that structure Mode 4: Deliverables (operational spine), Issues (in-flight problems), Risks (future problems), Outstanding Commitments (things promised but not done), What Is Not Visible (tacit knowledge), Who To Call (named contacts by issue type).
10. Encoded Mode 3 template variation for partner prep: Decisions Required, Information the Partner May Not Have, Likely Questions with Prepared Answers.
11. Encoded Mode 2 template variation for decision-first: collapsed deliverables/team/finance/cross-matter, expanded open decisions with options and blockers.
12. Wrote SKILL.md: 444 lines, 867-character description.
13. **(Phase 3 — 11 May 2026)** Calendar integration identified as Phase 3 backlog item for this skill (item 5: "Connected mode testing"; item in Future Connectors: "Calendar connector would improve Mode 3 quality"). Scope confirmed following daily-briefing Phase 3 pass: targeted edit, not rebuild. 460 actual lines (build log recorded 444 — patches added post-log), 40 lines of headroom. Sufficient for surgical additions to Mode 3 and Mode 4.
14. **(Phase 3)** Design confirmed: no design decisions required from user — scope is clear and constrained. Mode 3 is the primary use case (last partner touchpoint + upcoming call confirmation). Mode 4 has an existing SCHEDULED TOUCHPOINTS section that calendar populates. Mode 1 and Mode 2 out of scope for this pass.
15. **(Phase 3)** Key design insight identified during SKILL.md review: the last touchpoint date is not just context for Mode 3 — it anchors the INFORMATION THE PARTNER MAY NOT HAVE section. Anything arriving since the last partner call is potentially news to the partner. This makes the calendar data operationally load-bearing in Mode 3, not decorative. Applied explicitly in both the template and the Connected Mode description.
16. **(Phase 3)** Three targeted edits applied (v1.1.0): RECENT PARTNER TOUCHPOINTS section added to Mode 3 template; INFORMATION THE PARTNER MAY NOT HAVE anchored to last touchpoint; M365 Connected Mode Mode 3 and Mode 4 updated; Future Connectors calendar reference removed.
17. **(Phase 3)** TP-4 connected mode tested — PASS. Matter folder hygiene gap caught by connected mode retrieval; SCHEDULED TOUCHPOINTS populated from live calendar data.
18. **(Phase 3)** TP-3 connected mode tested — FAIL (iteration 1), FAIL (iteration 2), PASS (iteration 3). Two independent failure modes resolved: mandatory retrieval gate added to Before Starting Any Mode; header-first forcing function added to Mode 3 Output definition. SKILL.md v1.2.0 produced at 474 lines. Build log updated.

---

## Skill Scope Decisions

### Four modes, all retaining deliverables/issues/risks spine

Each mode emphasises different parts of the spine but all four retain it. Mode 1 standard: full spine plus supporting orientation. Mode 2 decision-first: spine retained (issues and risks constrain decisions); deliverables collapsed because they are context, not the focus. Mode 3 partner prep: spine retained; additional sections (decisions required, information the partner may not have, likely questions) layered on top. Mode 4 handoff: spine is literally the first three sections of the output; additional sections (outstanding commitments, what is not visible, who to call) complete the handoff.

### Mode 4 as primary operational capability, not sleeper mode

Based on user confirmation that handoff situations happen constantly, Mode 4 is built to full operational usefulness rather than as a Phase 3 candidate. Template variation is the longest of the four modes (4–6 pages acceptable), and the domain knowledge section specifically prompts for tacit knowledge transfer. The "what is not visible in the matter files" section is the differentiating capability — the thing this skill does that no other skill in the library produces.

### Working view vs status report — the boundary

matter-drill-down produces a working view for the LPM's own consumption. status-report-drafter produces a status report for partner/client distribution. Different tone, different register, different structural choices, different expectation of distribution. The boundary is reinforced at Input Classification Step 3 (audience check — if user specifies partner/client audience, route to status-report-drafter) and in the Boundary section of the SKILL.md.

### Open decisions vs live items — distinct sections

Canonical LPM discipline. Decisions need someone's attention; live items need tracking. Drill-downs that conflate them produce mush. In Modes 1, 3, 4: Open Decisions is a separate section from Deliverables. In Mode 2: Open Decisions is the spine.

### Financial position as headline, not analysis

Section 6 is one paragraph. Detailed variance analysis lives in budget-and-fee-manager. Drill-downs that attempt full financial analysis become long and duplicative and destroy the working-surface shape.

### Cross-matter context — no invention

Cross-matter context in the drill-down is limited to genuine connections (shared partner, shared LPM, same client, same regulatory overlay, same counterparty). Empty section is legitimate; fabricated connections are not.

### Calendar as anchoring mechanism in Mode 3 (Phase 3 decision)

Calendar integration in Mode 3 serves a different function than in daily-briefing. Daily-briefing uses calendar to surface the day's primary scheduling constraint. Mode 3 uses calendar to establish an information baseline: when was the last call with this partner, and what has arrived since then?

The last touchpoint date anchors INFORMATION THE PARTNER MAY NOT HAVE. Without it, that section is a generic list of recent developments. With it, the section is specifically scoped: items arriving since the last call are the partner's information gap. The calendar data makes the section structurally precise rather than editorially approximate.

This is a more subtle use of calendar data than daily-briefing's imminence ranking — it shapes the framing of another section rather than populating a dedicated calendar section. The RECENT PARTNER TOUCHPOINTS section at the top of the Mode 3 template establishes the baseline; INFORMATION THE PARTNER MAY NOT HAVE uses it.

Mode 4's SCHEDULED TOUCHPOINTS section already existed in the template as a manually populated section. Calendar retrieval in connected mode populates it from live data rather than requiring the outgoing LPM to list meetings manually — a modest but useful reduction in handoff preparation effort.

---

## Design Principles Applied

- **DP-26 (Global input classification).** Four-step classification: matter count, mode routing, audience check, input tagging. Classification fires before mode selection.
- **DP-27 (Template skeletons).** All four modes use explicit populated templates with labelled sections.
- **Identifier gate — harder than default.** Matter identifiers (client name, client number, matter name, matter number) required before output. Hard gate — do not produce until confirmed.
- **Produce-don't-ask.** No conditional offers. Produce the .docx.
- **Summary label.** Not "BLUF".
- **Handoff language alignment.** Handoff targets (scope-change-controller, risk-and-issues-manager, status-report-drafter, local-counsel-manager, budget-and-fee-manager, stakeholder-comms-planner, timeline-generator, resource-planner) use invocation language the adjacent skills expect.
- **Source tag preservation.** Input tags (`[FROM LC]`, `[CLIENT]`, `[PARTNER]`) preserved in attribution, not stripped.
- **No named firms.** Domain knowledge and templates generic.
- **Calendar as anchor, not decoration (Phase 3).** Calendar data in Mode 3 establishes the partner information baseline — last touchpoint date scopes INFORMATION THE PARTNER MAY NOT HAVE. Calendar data in Mode 4 populates SCHEDULED TOUCHPOINTS from live data rather than manual input. If calendar is unavailable, sections state so explicitly and fall back to correspondence inference.

---

## Phase 1 Test Prompts

Each test prompt is run by the builder against the SKILL.md content as a simulation. Simulation is labelled explicitly — not a skill invocation.

### TP-1 — Mode 1: Standard drill-down on Meridian (heavy, Amber matter)

**Test prompt:** Paste Meridian Industrial AG inputs from the portfolio pack (week 6 reorg scenario, multi-jurisdictional, Amber). Prompt: *"Drill into Meridian."*

**Eval assertions:**
- ✅ Mode 1 fires
- ✅ Matter identifiers requested before production OR taken from inputs if present
- ✅ Output opens with identifier header including Invocation Context
- ✅ SUMMARY is 2–3 sentences, direct, no hedging
- ✅ DELIVERABLES section populated with 3+ rows — each with owner and by-when
- ✅ ISSUES section distinguishes from Risks (Swiss ruling slip = issue; Poland LC non-response at 8+ days = risk ratcheting toward issue)
- ✅ RISKS section frames plausibly-future items (Italian scope addition, Czech FDI regime exposure)
- ✅ OPEN DECISIONS section separate from Deliverables
- ✅ SCOPE SIGNALS table populated (Italian real estate — adding; Czech FDI — regulatory-driven)
- ✅ FINANCIAL POSITION is one paragraph only — does not reproduce full variance analysis
- ✅ TEAM AND STAKEHOLDER STATE is brief (1–3 lines per sub-section)
- ✅ CROSS-MATTER CONTEXT identifies Westcliff as the other Amber matter under same LPM OR states "no notable cross-matter context" honestly if portfolio context not provided
- ✅ HANDOFFS names specific skills with matter triggers
- ✅ Total length 2–3 pages

### TP-2 — Mode 1: Standard drill-down on Nexus (Green, quiet matter)

**Test prompt:** Paste Nexus Life Sciences inputs (one email from Schmid + one internal note confirming QA Wednesday). Prompt: *"Drill into Nexus."*

**Eval assertions:**
- ✅ Mode 1 fires
- ✅ Identifier header populated
- ✅ SUMMARY is 2 sentences — short, current position clear
- ✅ DELIVERABLES has 1–2 rows (QA Wednesday; submission 5 May)
- ✅ ISSUES section states "No current issues" — does not fabricate
- ✅ RISKS section states "No significant risks this period" — does not invent
- ✅ OPEN DECISIONS section likely empty or 1 row
- ✅ Total length ≤1.5 pages (restraint applied — not padded to match Meridian)
- ✅ No cross-matter context manufactured

### TP-3 — Mode 3: Partner prep on Meridian ahead of JMW call

**Test prompt:** Same Meridian inputs plus context: *"I have a call with JMW tomorrow to discuss the Italian real estate scope question and the Czech FDI watch item. Prep me."*

**Eval assertions:**
- ✅ Mode 3 fires
- ✅ Identifier header includes Partner, Call purpose, Call timing
- ✅ SUMMARY framed specifically around the call
- ✅ DECISIONS REQUIRED FROM THE PARTNER section — Italian scope addition decision; Czech FDI sequencing decision if analysis is adverse
- ✅ INFORMATION THE PARTNER MAY NOT HAVE section — items direct to the LPM, client-side dynamics the partner has not seen
- ✅ LIKELY PARTNER QUESTIONS with answer lines (3–5 questions)
- ✅ Deliverables, Issues, Risks retained (standard tables)
- ✅ Supporting context paragraphs (financial, team, client)
- ✅ Total length 2 pages

### TP-4 — Mode 4: Handoff briefing for Meridian (simulating Scott going on 1-week leave)

**Test prompt:** Same Meridian inputs plus context: *"I'm going on leave next week. Handing Meridian to Priya Ramanathan for cover. Produce a handoff briefing."*

**Eval assertions:**
- ✅ Mode 4 fires
- ✅ Identifier header includes Handoff from, Handoff to, Effective date
- ✅ SUMMARY is 3–5 sentences — what the matter is, where it is, what is coming up in the handoff window
- ✅ DELIVERABLES — NEXT 2–4 WEEKS populated with 5+ rows, each with owner, by-when, status, context
- ✅ ISSUES — CURRENT populated with in-flight problems, each with mitigation in progress and what is needed next
- ✅ RISKS — PLAUSIBLE FUTURE populated with plausible items and watch-this-specifically guidance
- ✅ OUTSTANDING COMMITMENTS populated — commitments from emails and calls not documented in a tracker
- ✅ WHAT IS NOT VISIBLE IN THE MATTER FILES — skill prompts the outgoing LPM for tacit content OR asks specific prompting questions (communication preferences, partner preferences, patterns on the other side, client-side politics, partner-known-but-not-documented items)
- ✅ WHO TO CALL table populated by issue type with named people
- ✅ CURRENT FINANCIAL POSITION is brief
- ✅ STAKEHOLDER TONE SNAPSHOT populated with one line per key contact
- ✅ SCHEDULED TOUCHPOINTS — NEXT 4 WEEKS populated
- ✅ HANDOFFS section populated for first-week invocations
- ✅ Total length 4–6 pages

### TP-5 — Mode 2: Decision-first on Meridian

**Test prompt:** Same Meridian inputs, prompt: *"What do I need to decide on Meridian?"*

**Eval assertions:**
- ✅ Mode 2 fires
- ✅ Identifier header populated
- ✅ OPEN DECISIONS — EXPANDED is the spine of the output
- ✅ Each decision has: decision statement, owner, by-when, options, current state, blockers, LPM recommendation
- ✅ ISSUES and RISKS retained as standard tables (they constrain/inform decisions)
- ✅ Deliverables, Team, Finance, Cross-matter context collapsed to one line each
- ✅ Total length 1.5–2 pages

### TP-6 — Audience check: status report request

**Test prompt:** Paste Meridian inputs, prompt: *"Produce a status report on Meridian for JMW to send to the client."*

**Eval assertions:**
- ✅ Input Classification Step 3 fires — audience is specified as partner/client
- ✅ Skill does NOT produce a drill-down
- ✅ Skill routes to status-report-drafter with handoff language
- ✅ No drill-down output produced

### TP-7 — Multi-matter input check

**Test prompt:** Paste the full six-matter portfolio pack, prompt: *"Drill into Meridian."*

**Eval assertions:**
- ✅ Input Classification Step 1 detects multi-matter input
- ✅ Skill filters to Meridian content only for the drill-down
- ✅ Cross-matter context section populated from the other matter data (correctly — not fabricated)
- ✅ Mode 1 output produced on Meridian using standard template

### TP-8 — Missing identifier gate

**Test prompt:** Paste Meridian emails with no matter number reference, prompt: *"Drill into Meridian."*

**Eval assertions:**
- ✅ Identifier gate fires — skill asks for client name, client number, matter name, matter number before production
- ✅ Does not proceed with fabricated identifiers
- ✅ If user responds with confirmation (even "use placeholders"), skill proceeds with clear placeholder labelling

### TP-9 — Mode 3 calendar integration (Phase 3)

**Test prompt:** Same Meridian inputs as TP-3, M365 Calendar connector active. Calendar data includes: JMW call 2 May (15 days ago, Meridian regulatory review), JMW call 28 April (19 days ago, scope discussion), and upcoming call tomorrow at 14:00. Prompt: *"Prep me for my call with JMW tomorrow on Meridian — Italian RE scope question and Czech FDI."*

**Eval assertions:**
- ✅ Mode 3 fires
- ✅ `outlook_calendar_search` called for JMW over past 30 days and upcoming 14 days
- ✅ RECENT PARTNER TOUCHPOINTS section populated: two past touchpoints with date, meeting name, what was covered, follow-up identified; upcoming call confirmed with date, time, format
- ✅ INFORMATION THE PARTNER MAY NOT HAVE is anchored to "since last partner touchpoint (2 May)" — items arriving after that date flagged; items predating it not included unless materially changed
- ✅ If calendar unavailable: RECENT PARTNER TOUCHPOINTS states "Calendar not retrieved — confirm last touchpoint date from correspondence before producing this section"; INFORMATION THE PARTNER MAY NOT HAVE falls back to unanchored list of recent developments
- ✅ No invented touchpoints; no meetings inferred from correspondence references alone

---

## Phase 1 Simulation Results

All eight test prompts simulated by builder on 19 April 2026. Each labelled as builder simulation, not skill invocation.

| TP | Mode | Result | Key observation |
|---|---|---|---|
| TP-1 | Mode 1 (heavy) | PASS | Full template populated. 7 deliverables, 2 issues, 3 risks, 4 decisions. ~2.5 pages. |
| TP-2 | Mode 1 (quiet) | PASS | Restraint held. ~0.75 pages. Empty sections stated plainly. No fabrication. |
| TP-3 | Mode 3 (partner prep) | PASS | Call-specific framing. 2 decisions, 3 info items, 4 questions. ~2 pages. |
| TP-4 | Mode 4 (handoff) | PASS | Load-bearing mode. 9 deliverables, tacit knowledge prompts, who-to-call table. ~5 pages. |
| TP-5 | Mode 2 (decision-first) | PASS | Decisions as spine. 4 decisions fully expanded. Supporting sections collapsed. ~2 pages. |
| TP-6 | Routing (audience) | PASS | Audience check fired. Routed to status-report-drafter. |
| TP-7 | Routing (multi-matter) | PASS | Filtered to Meridian. Cross-matter context from Westcliff genuine. |
| TP-8 | Routing (identifier) | PASS | Gate fired. Asked for missing identifiers. |

Three pre-Phase-2 patches applied based on daily-briefing failure patterns:
1. Mode 4 "What Is Not Visible" fabrication prohibition placed inside template skeleton
2. Audience check (Step 3) strengthened with named failure mode
3. Cross-matter context fabrication path named explicitly

---

## Phase 2 Test Results

[Placeholder. Phase 2 runs by user in clean Claude.ai session with skill installed. One test per fresh conversation. User pastes output back; builder records PASS/PARTIAL/FAIL against each assertion with specifics.]

### Phase 2 setup
- New Claude.ai session
- Skill installed via Settings → Capabilities → Skills (not pasted as instructions)
- No project context, no prior conversation history
- Each test prompt in its own fresh conversation

### TP-1 — Mode 1 heavy matter — PASS (Opus 4.6)
Full template populated. 7 deliverables, 3 issues, 3 risks, 4 decisions, 2 scope signals, 5 handoffs. ~3 pages. All sections present in correct order. Identifier header complete. Summary ran to 5 sentences (template says 2-3) but all content is substantive — consistent model behaviour, not patch-worthy. WIP placed in Issues (defensible: 12% overrun is confirmed state, not future risk). Italian RE placed in both Issues and Scope Signals with different framing — good structural discipline. Cross-matter context correctly states "No notable cross-matter context." Financial position is one paragraph. Conversational commentary post-document is sharp and operationally useful.

### TP-2 — Mode 1 restraint — PASS (Opus 4.6)
Restraint test passed. ~1.5 pages vs TP-1's ~3 pages. 3 deliverables (eval expected 1-2 — third row is genuine intermediate step, not padding). Issues: "No current issues." Two low-probability risks populated rather than stating "no significant risks" — both grounded in inputs (QA finding something, Homburger terminology observations). No decisions. No scope signals. One conditional handoff. Length proportionate to matter weight. Model did not normalise across matters.

### TP-3 — Mode 3 partner prep — PASS (Opus 4.6) [Phase 1 simulation / Phase 2 paste-mode]
Mode 3 template used correctly. Header includes Partner (JMW), Call purpose, Call timing. 3 decisions in DECISIONS REQUIRED section with options, LPM recommendation, and "why now". 4 items in INFORMATION THE PARTNER MAY NOT HAVE — strongest: Italian RE was explicitly excluded at baseline, reframing Wolfgang's email. 5 likely partner questions with substantive answer lines. Standard tables retained (6 deliverables, 3 issues, 3 risks). Supporting context present. ~4 pages (eval said 2 — Mode 3 template adds three sections on top of standard tables; 2 pages was too tight for a heavy Amber matter. Eval assertion revised, not skill).

Note: Phase 2 pass was against pasted input without M365 connector. Phase 3 connected-mode testing revealed two additional failure modes — see Phase 3 section.

### TP-4 — Mode 4 handoff — PASS (Opus 4.6)
Load-bearing mode. Critical Patch 1 held: "What Is Not Visible" section produced 6 prompting questions rather than fabricating tacit knowledge. Preamble: "The following prompts need answers from the outgoing LPM before this section is complete." No inferred relationship dynamics, no fabricated communication preferences, no manufactured client politics. 7 deliverables with context column. 3 issues with four-column format. 3 risks with "Watch this specifically." 4 outstanding commitments from emails/calls. 7 WHO TO CALL entries by issue type. Stakeholder tone snapshot for 5 contacts. 8 scheduled touchpoints. 5 handoffs. ~5 pages. Summary ran to two paragraphs — second paragraph (Priya's four immediate priorities) is genuinely useful, not padding. Cross-matter context: "No other matters provided for cross-referencing." Conversational commentary pre-document is well-calibrated (flags overdue items, recommends 15-minute handoff call).

### TP-5 — Mode 2 decision-first — FAIL / V1 LIMITATION (Opus 4.6)
Three iterations of patches, all failed. Model produces conversational advisory prose rather than a .docx with the Mode 2 template skeleton. Iteration 1: produce-now directive in template variation section — model commits to prose before reaching it. Iteration 2: directive moved to mode definition (line 85) — still overridden. Iteration 3: directive added at input classification Step 2 routing — still overridden. Model's trained prior to answer "What do I need to decide?" as a conversational question is stronger than the skill directive. Content quality is consistently high (correct decisions, sound options, defensible recommendations) but format is wrong. Declared v1 limitation after three iterations per canonical process. Workaround: prompt with "Produce a decision-first drill-down on [matter] as a .docx" rather than natural-language question. Usage note added to README.

### TP-6 — Audience check routing — FAIL / V1 LIMITATION (Opus 4.6)
Two iterations of patches on the audience check gate (Step 3), both failed. Iteration 1: strengthened prohibition with named failure mode ("do not produce a drill-down and adjust the tone"). Iteration 2: provided an explicit routing response template for the model to produce instead. Both times the model detected the audience correctly, produced a high-quality client-facing status report, and provided appropriate editorial commentary — but did not route to status-report-drafter. status-report-drafter was installed and available in the test environment, so this is a genuine routing failure, not an environmental artefact. Root cause: same gate-skipping pattern as Mode 2. Model's helpfulness prior overrides routing instructions when it has the capability to produce the requested output. The model absorbs the adjacent skill's function rather than deferring to it. Workaround: invoke status-report-drafter directly rather than asking matter-drill-down to produce a status report.

### TP-7 — Multi-matter filter — PASS (Opus 4.6)
Full six-matter portfolio pack pasted with "Drill into Meridian" prompt. Model correctly filtered to Meridian content for all substantive sections. Cross-matter context populated with genuine Westcliff connection (same LPM, competing Monday deadline, bandwidth conflict). No fabricated connections to Aldwych, Nexus, Altissima, or Hartwick. Full Mode 1 template produced. Conversational commentary also identified the Westcliff bandwidth conflict.

### TP-8 — Identifier gate — FAIL (Opus 4.6)
Identifier gate did not fire. Model was given Meridian emails only (no portfolio roster, no explicit matter number). Model inferred identifiers from correspondence content (client number M20481, matter number M20481.002) and produced the full drill-down without asking. Same gate-skipping pattern as TP-5 and TP-6: model overrides boundary instructions when it has enough information to produce the requested output. Low operational risk — inferred identifiers are likely correct in practice, and in real usage the matter number would almost certainly appear in correspondence. Gate exists for data hygiene in formal .docx records. Not worth a patch iteration given the consistent gate-skipping pattern. Usage note added to README.

---

## Phase 3 — Calendar Integration (11 May 2026)

### Scope decision

Targeted edit, not rebuild. The four-mode architecture, deliverables/issues/risks spine, and Mode 4 tacit knowledge discipline are tested and working. Calendar integration is confined to Mode 3 (primary use case) and Mode 4 (SCHEDULED TOUCHPOINTS population). Mode 1 and Mode 2 are out of scope for this pass — calendar is less structurally relevant there and headroom was limited (40 lines).

### Design decisions

| Decision | Choice | Rationale |
|---|---|---|
| Mode 3 calendar placement | New RECENT PARTNER TOUCHPOINTS section, between SUMMARY and DECISIONS REQUIRED | Partner touchpoint history is framing context that shapes the rest of the Mode 3 output. Placing it near the top means the LPM reads it before entering the decisions and information sections. |
| Last touchpoint as anchor | INFORMATION THE PARTNER MAY NOT HAVE explicitly scoped to "since last partner touchpoint" | Without the anchor, the section is a generic list of recent developments. With it, the section is precisely scoped: items arriving since the last call are the partner's actual information gap. This makes the calendar data operationally load-bearing, not decorative. |
| Calendar windows for Mode 3 | Past 30 days / upcoming 14 days | Past 30 days captures the realistic partner-touchpoint horizon for active matters. Upcoming 14 days confirms the call being prepped for and any adjacent touchpoints. |
| Mode 4 calendar | Note in Connected Mode that calendar populates SCHEDULED TOUCHPOINTS | SCHEDULED TOUCHPOINTS already exists as a template section. Calendar retrieval populates it from live data rather than requiring manual input from the outgoing LPM. No template change required. |
| Modes 1 and 2 | Out of scope | Mode 1: calendar would add upcoming meetings context — useful but not architecturally significant for a single-matter drill-down. Mode 2: calendar not relevant to decision-first framing. Both deferred as Phase 3 backlog items. |

### Changes made to SKILL.md v1.0 → v1.1.0

| Location | Change | Type |
|---|---|---|
| YAML version | 1.0.0 → 1.1.0 | Update |
| Mode 3 template | Added RECENT PARTNER TOUCHPOINTS section (past 30 days table + upcoming call confirmation + no-data fallback) between SUMMARY and DECISIONS REQUIRED | Addition |
| Mode 3 template | Updated INFORMATION THE PARTNER MAY NOT HAVE header to "Items that have arrived or developed since the last partner touchpoint (see above)" | Update |
| M365 Connected Mode — Mode 3 | Replaced one-line placeholder with actual instructions: `outlook_calendar_search` for partner name, two windows (past 30 days / upcoming 14 days), anchor relationship to INFORMATION THE PARTNER MAY NOT HAVE made explicit | Update |
| M365 Connected Mode — Mode 4 | Added: `outlook_calendar_search` for matter keyword, upcoming 4 weeks, populates SCHEDULED TOUCHPOINTS | Addition |
| M365 Connected Mode — Manual fallback | Updated to note calendar entries can be pasted directly | Update |
| Future connectors | Removed calendar reference (no longer Phase 3). DMS reference retained. | Update |

**Line count:** 460 → 470 (10 lines added, 30 lines remaining to 500 limit)
**Description:** Unchanged at 867 characters

### Phase 3 test prompts

TP-9 defined above. Not yet run. Phase 3 testing pending clean-session validation with M365 Calendar connector active.

### Phase 3 connected-mode testing — TP-4 and TP-3 (11 May 2026)

**TP-4 connected mode (Mode 4 handoff, no paste) — PASS**

Run against live Outlook data with M365 connector active. No input pasted. Skill retrieved Meridian correspondence from the matter folder (8 emails, all dated 18 April — matter folder unfiled since then), then correctly broadened search across mailbox to find 10 May developments (Czech FDI, BaFin filing, Polish LC, Helena status call). Calendar queried for 11 May–8 June window; 2 events returned, both appearing in SCHEDULED TOUCHPOINTS.

Connected-mode-specific findings not visible in paste mode:
- Matter folder hygiene gap caught and elevated to Issue #6 — three weeks of substantive correspondence unfiled, creating a handoff hazard. Specific action item: file or brief Priya to read Inbox + Sent Items, not the folder.
- SCHEDULED TOUCHPOINTS populated from calendar (2 events) plus correspondence-derived dates. Phase 3 change for Mode 4 confirmed working.
- WHAT IS NOT VISIBLE gate held correctly — skill prompted for tacit knowledge before producing; populated verbatim from user input.
- Wolfgang Steiner identity ambiguity (two email addresses across source data) flagged in Deliverable #10 with footnote.

Minor format note: SCHEDULED TOUCHPOINTS rendered as prose list rather than table. Content complete and correct; format departure not patch-worthy.

**TP-3 connected mode (Mode 3 partner prep) — FAIL (iteration 1) → FAIL (iteration 2) → PASS (iteration 3)**

Three iterations to resolve two independent failure modes.

**Iteration 1 — FAIL.** Conversational prose output despite Phase 3 calendar additions to SKILL.md. Template did not fire. M365 connector not invoked — skill went to memory instead. Root causes: (1) no mandatory retrieval gate before production; (2) Mode 3 template variation header too weak to override conversational prior.

**Patches applied (iteration 1):**
- Input Classification Step 2 Mode 3 routing line: added produce-now directive
- Mode 3 definition Output section: rewrote from bullet list to explicit .docx directive with named failure modes
- Mode 3 Template Variation header: added strong produce-now directive matching Mode 2 header strength

**Iteration 2 — FAIL.** Three-point directive patch applied. Template still did not fire. M365 connector still not invoked — skill stated "no active source material" and went to past-conversation memory. Root causes: (1) retrieval gate still absent — no instruction forcing connector invocation before production; (2) header-first forcing function not yet applied — model still chose conversational format before committing to document structure.

**Patches applied (iteration 2):**
- Before Starting Any Mode: added mandatory M365 retrieval step — "If M365 connector is available, invoke `outlook_email_search` for the matter name before producing output in any mode. Do not ask for pasted inputs if connected mode is available — retrieve first, then produce."
- Input Classification Step 2 Mode 3: added explicit retrieval instruction to routing line
- Mode 3 definition Output section: added header-first forcing function — "The first content you produce is the identifier header block — not a comment, question, flag, or advisory text. Starting with the header commits you to document format. Conversational preamble before the header is the failure mode."

**Iteration 3 — PASS.** Both patches held.

Retrieval: skill invoked `outlook_email_search` (Meridian, after 8 May) and `outlook_calendar_search` (12–13 May, JMW as attendee) before producing. Sources checked block confirms retrieval.

Template: .docx produced with full Mode 3 structure. Identifier header, SUMMARY, RECENT PARTNER TOUCHPOINTS, DECISIONS REQUIRED (6 decisions with options/recommendation/why-now), INFORMATION THE PARTNER MAY NOT HAVE (anchored to since last JMW touchpoint), LIKELY PARTNER QUESTIONS (5 with answer lines), spine tables (7 deliverables, 3 issues, 4 risks), supporting context, 5 handoffs.

RECENT PARTNER TOUCHPOINTS: populated from Outlook. Calendar returned no JMW Meridian calls — correctly handled with fallback language: "calendar search for JMW as attendee on Meridian returned no results — calendar discipline may have slipped, or touchpoints are informal/phone." No data invented.

INFORMATION THE PARTNER MAY NOT HAVE: anchor working — "items developing since JMW's last logged Meridian touchpoint (10 May email)."

Calendar finding (no JMW call on tomorrow's calendar): flagged prominently in both SUMMARY and identifier header. Operationally correct — the call is either informal or the user was conflating with Wednesday's contingent call.

Adaptive section added: "WHERE TO PUSH BACK ON JMW" — not in the Mode 3 template, added by skill as an additional section. Content is operationally the sharpest part of the brief. See Phase 3 backlog item 10.

**What fixed it:** The header-first forcing function was the determining patch. Naming "conversational preamble before the header is the failure mode" and requiring the identifier header as the first production act committed the model to document format before it had the opportunity to go conversational. The mandatory retrieval gate fixed the separate connector invocation failure. Two distinct problems; two distinct fixes; both required for PASS.

**Root cause pattern:** Mode 3's invocation pattern ("prep me for a call") sounds like a conversational question. The model's prior to answer it conversationally is strong — stronger than produce-now directives alone. The header-first forcing function changes the dynamic: once the model writes the identifier header, it is in document mode and the template follows naturally. This mirrors why Mode 4 has always worked — the detailed template makes document format the path of least resistance from the first line.

**Line count after iteration 2 patches:** 474 lines (26 remaining to 500 limit).

---

## Open Items Post-Phase 2

### V1 Limitation: Mode 2 prose-instead-of-template

**What works:** Mode 2 correctly identifies open decisions, prioritises them, provides options and recommendations, and covers the right content.

**What doesn't work:** Mode 2 does not reliably produce a .docx with the template skeleton (identifier header, structured decision entries, retained Issues/Risks tables, collapsed supporting sections). Three patch iterations failed across three interception points (template section, mode definition, input classification routing). The model's trained prior to answer natural-language decision questions as conversational advisory prose overrides the skill directive.

**Workaround:** Prompt with explicit document-request language: "Produce a decision-first drill-down on [matter] as a .docx" rather than "What do I need to decide on [matter]?"

**V2 approach:** Consider splitting Mode 2 into a dedicated template with a stronger skeleton that the model populates (similar to Mode 4's extended template), rather than defining it as a variation of Mode 1 with collapsed sections. Alternatively, test whether a worked example in the template section changes the behaviour.

### V1 Limitation: Audience check routing (TP-6)

**What works:** Model detects audience correctly and produces a high-quality client-facing status report with appropriate register and editorial judgment.

**What doesn't work:** Model does not route to status-report-drafter. Two patch iterations failed. status-report-drafter was installed and available in the test environment, confirming this is a genuine routing failure, not an environmental artefact. Same gate-skipping pattern: model's helpfulness prior overrides routing instructions when it can produce the requested output.

**Workaround:** Invoke status-report-drafter directly rather than requesting a status report via matter-drill-down.

**V2 approach:** Cross-skill routing may require platform-level support (skill priority/conflict resolution) rather than text-based instructions within a single skill. Alternatively, test whether the routing holds when the prompt is ambiguous ("produce a report on Meridian") vs explicit ("produce a status report for JMW to send to the client").

### Known issue: Identifier gate does not fire on inferrable identifiers (TP-8)

Model infers identifiers from correspondence and proceeds without asking, even when identifiers are not explicitly provided. Low operational risk — inferred identifiers are typically correct. Gate exists for data hygiene in .docx records. Not worth patching given the consistent gate-skipping pattern across TP-5, TP-6, and TP-8.

### Phase 3 backlog

1. Mode 2 template strengthening (v2 approach above)
2. Audience check routing — cross-skill routing mechanism (v2 approach above)
3. Mode 3 page length calibration — eval assertion said 2 pages, actual output is 3-4 on heavy matters. Template structure inherently longer. Revise guidance, not skill.
4. Summary length across all modes — model consistently writes 4-5 sentences rather than 2-3. Content is substantive. Monitor but do not patch unless it inflates further.
5. ~~Connected mode testing (M365 Outlook retrieval)~~ — **complete.** TP-4 and TP-3 connected mode both validated (11 May 2026).
6. Cross-model testing on Sonnet — daily-briefing validated cross-model; matter-drill-down should be tested on Sonnet for Modes 1, 3, 4
7. Identifier gate hardening — test whether explicit "stop and ask" language in the gate fires more reliably, or whether this is a fundamental gate-skipping behaviour
8. ~~Phase 3 clean-session testing~~ — **complete.** TP-4 PASS, TP-3 PASS (iteration 3).
9. Mode 1 calendar — Upcoming meetings in the next week would add useful context to a standard drill-down. Out of scope for this pass given headroom constraints. Consider for a future pass.
10. **"WHERE TO PUSH BACK" adaptive section** — Mode 3 TP-3 live test produced an unprompted "WHERE TO PUSH BACK ON JMW" section containing the sharpest operational content in the brief. Not in the Mode 3 template. Behaviour is correct and valuable; consider formalising as a standard Mode 3 section. Low priority — adaptive addition is working without instruction; encoding it formally risks over-specifying.

---

## Source Materials Used

- `skill-build-process-template-v1.md` — canonical build process (v1.0)
- `matter-intake-scoping-build-log.md` — canonical build log structure reference
- `v1-skill-build-starter-prompt-v4_0.md` — Phase 1/2 process definition
- `lpm-plugin-planning-v1_7.md` — status-report-drafter boundary language, cross-skill handoff patterns
- `daily-briefing/SKILL.md` — adjacent skill boundary alignment (this skill is routed from daily-briefing Mode 2)
- User calibration (17–19 April 2026) — deliverables/issues/risks spine; handoff briefing as constantly-triggered operational need requiring full Mode 4 build
- `skill-build-process-template-v2.md` — Phase 3 process reference (May 2026)
- `daily-briefing` Phase 3 pass (10 May 2026) — calendar integration patterns; anchor-relationship design principle

## Build Artefacts

- `matter-drill-down/SKILL.md` v1.2.0 (474 lines)
- `matter-drill-down/matter-drill-down-build-log.md` (this file)

README.md to be produced next.
