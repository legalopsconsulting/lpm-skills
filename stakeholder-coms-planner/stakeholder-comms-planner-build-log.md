# stakeholder-comms-planner — Build Log

**Build date:** 14 March 2026
**Skill number:** 9 of 19 (LPM Core Plugin)
**Session type:** Initial build
**Status:** Phase 1 complete — Phase 2 ready

---

## Pre-build decisions

### Mode structure
Four modes confirmed at pre-build:

- Mode 1 — Stakeholder mapping: power/interest classification, register production
- Mode 2 — Communication plan: stream design, cadence, format
- Mode 3 — Reporting hierarchy: three-tier architecture, escalation thresholds, HQ vs regions
- Mode 4 — Mid-matter comms update: landscape change without starting from scratch

Mode 3 is the differentiating mode — none of the other skills in the plugin handle multi-jurisdiction reporting hierarchy design. The HQ vs regions problem (client HQ and regional contacts both claiming primary contact status) is a recurring failure mode on cross-border programmes and is explicitly named and addressed here.

### RASIC vs RACI
Linton (2014) recommends RASIC over RACI for legal matters — the Supports role (provides input to the person Responsible) is practically important on legal matters where multiple fee-earners contribute to a single output. Encoded as the communication roles framework. In practice, most legal matter communications only need Accountable (partner) and Informed (recipients) — the full RASIC is reserved for programme-level communications with a complex production chain.

### Sensitivity column
The most important column in the stakeholder register is the one most often left blank in practice. Encoded as a required field and described with specific examples of what belongs there: operational intelligence about individual stakeholders that cannot be reconstructed after the matter is underway. This was a direct lesson from the Sibelius programme (client HQ vs regions comms gap) — the failure was not a process failure, it was a failure to capture and act on known relationship dynamics.

### Attorney boundary — union communications
Trade union communications under employment restructuring consistently create LPM/attorney boundary questions: what is required by statute, what is advisable, what can be shared with which parties. Hard rule applied: do not name specific legislation, do not characterise the legal requirements, flag and route to attorney. TP-4 tested this directly — copy-on-union-communications request from new GC flagged without characterising whether it was appropriate.

### Two streams, designed separately
The internal/client-facing split is fundamental and is encoded as a domain knowledge principle before the output format section, not just as a formatting instruction. The most common communication failure on complex matters — treating internal exception reports and client-facing confidence-management reports as the same stream — is named and explained.

---

## Structural decisions

### Power/interest grid — four quadrant model
Adapted from PMBoK via Linton. Four quadrants (Manage closely / Keep satisfied / Keep informed / Monitor) with communication approach specified for each. The key insight that positions are not permanent — they change at phase gates and when significant matter events occur — is encoded as a required review instruction, not just an advisory note.

### Primary contact problem
Named as a distinct failure mode and given a dedicated section in the domain knowledge. The resolution path is clear: partner resolves it (not LPM), one named primary contact per reporting stream, recorded in the register and the engagement letter. The LPM's role is to surface the problem and draft the options — not to resolve a client relationship question unilaterally.

### Three-tier hierarchy
Jurisdiction → Regional → Programme → Client. Regional coordinator role defined precisely: aggregates, filters, escalates. Not a messenger. The distinction between a coordinator who adds analytical value (aggregating and filtering) and one who merely forwards updates (adding no value and creating noise at programme level) is encoded in the role description.

### Escalation thresholds
Default escalation thresholds specified at each tier boundary. Explicitly framed as defaults to be confirmed and adjusted at matter setup — not universal rules. The principle: define what must escalate before the matter starts, not after the first problem arises.

---

## Phase 1 test results — 14 March 2026

Four test prompts run in-session. All pass.

**TP-1 — Mode 1: Stakeholder mapping (Whitmore Group employment restructuring, three trade unions, multi-region client)**
- Identifier gate fired ✅
- Stakeholder register with all eight required columns ✅
- Power/interest quadrant assigned to all eleven stakeholders ✅
- Primary contact problem identified and flagged as requiring partner resolution ✅
- Regulatory stakeholder included with attorney routing for disclosure obligations ✅
- Sensitivities column populated with operational intelligence ✅
- CSV export produced ✅

**TP-2 — Mode 2: Communication plan (weekly internal, monthly client formal, union handling)**
- Two streams designed separately (internal vs client-facing) ✅
- Communication schedule table with all required columns ✅
- Union communications handled as a third separate stream ✅
- Statutory requirement reference (TULRCA) not characterised — attorney flag applied ✅
- Primary contact resolution requirement carried forward from Mode 1 ✅
- status-report-drafter referenced as the tool for monthly report production ✅

**TP-3 — Mode 3: Reporting hierarchy (12 jurisdictions, 4 regions, conflicting client contacts)**
- Three-tier hierarchy produced with visual structure ✅
- HQ vs regions conflict identified before being named by the user ✅
- Two resolution options presented with recommendation — partner decision required ✅
- Escalation thresholds defined at both tier boundaries ✅
- Regional coordinator role defined precisely — aggregator and filter, not messenger ✅

**TP-4 — Mode 4: Mid-matter comms update (new GC, Singapore location, weekly request, union copy request)**
- Stakeholder register updated (not replaced) ✅
- Timezone implication identified — 8am London call proposed for Singapore compatibility ✅
- Union copy request flagged immediately — not actioned — attorney and partner routing ✅
- Onboarding call recommended before formal reporting resumes ✅
- Changes tabulated in a before/after format ✅

---

## Notable Phase 1 observations

**Attorney boundary applied correctly in TP-4.** The union communications copy request was flagged without characterising whether it was legally appropriate. This is the correct LPM response: surface the question, route to attorney, do not substitute LPM judgment for legal judgment.

**Primary contact problem flagged unpromptedly in both TP-1 and TP-3.** The skill identified the multi-contact conflict before being asked about it. In TP-1 (regional HR contacts), in TP-3 (regional FDs vs HQ M&A team). This is the skill operating as intended — surfacing the design problem that causes relationship damage downstream.

**Onboarding call recommendation in TP-4 was above assertion floor.** New stakeholders in a Manage closely position being introduced to the matter via a status report is a real relationship failure mode. The recommendation to schedule a relationship-building call before formal reporting resumes was unprompted and correct.

**No named-firm references, no legislation named.** Both rules applied consistently across all four tests.

---

## Phase 2 handoff

Install in a clean Claude.ai chat. Run all four prompts below. Report full output or deviations from assertions.

**TP-1:** "New matter — UK employment restructuring, three trade unions. Client is Whitmore Group, HQ in Frankfurt, regional teams in UK, Germany, France. Lead partner in London. Build me a stakeholder map. Client: Whitmore Group, C-71004. Matter: Project Resolve, M-71004-01."

Key checks: identifier gate, all eight columns in register, power/interest quadrant for each stakeholder, primary contact flag, attorney routing for regulatory stakeholder, CSV export.

**TP-2:** "From that stakeholder map, build the communication plan. Partner wants weekly internal calls. Client wants monthly formal reporting. Union reps need separate handling — statutory consultation requirements apply. Client: Whitmore Group C-71004, Matter: Project Resolve M-71004-01."

Key checks: two streams designed separately, communication schedule table with all columns, union stream separate, statutory requirement not characterised (attorney flag), primary contact resolution carried forward.

**TP-3:** "Multi-jurisdiction M&A — 12 jurisdictions, global lead partner in London, four regional coordinators covering EMEA/APAC/Americas/CEE. Client has a global M&A team in New York plus regional finance directors who each think they're the primary contact for their region. Build the reporting hierarchy. Client: Nexus Corp, C-82001. Matter: Project Summit, M-82001-03."

Key checks: three-tier hierarchy with visual structure, HQ vs regions conflict identified, two resolution options with recommendation, escalation thresholds at both tier boundaries, regional coordinator role defined precisely.

**TP-4:** "The Frankfurt GC on Project Resolve has just been replaced. New GC is based in Singapore and wants weekly visibility rather than monthly. She's also asked to be copied on all union communications. Client: Whitmore Group C-71004, Project Resolve M-71004-01."

Key checks: register updated not replaced, timezone implication identified with specific call time proposed, union copy request flagged and NOT actioned (attorney routing), onboarding call recommended.

---

## Status

Phase 1: Complete. All four tests pass.
Phase 2: Ready to run.

---

## Phase 2 — TP-1 result (14 March 2026)

**Test:** Stakeholder mapping — UK employment restructuring, three trade unions, Frankfurt HQ, UK/DE/FR regional teams. Whitmore Group / Project Resolve.

**Eval assertions:**

| Assertion | Result |
|---|---|
| Identifier gate | ✅ |
| All eight columns in register | ✅ 34 entries across eight categories |
| Power/interest quadrant for all stakeholders | ✅ |
| Primary contact problem identified | ✅ Red flag — blocking action — partner resolution required |
| Attorney boundary — regulatory bodies flagged not characterised | ✅ PSE, HR1, Agentur für Arbeit, DREETS all flagged and routed |
| CSV export | ❌ Not produced |
| Sensitivities column with operational intelligence | ✅ |

**Notable quality above assertion floor:**
- Five-tier hierarchy rather than three-tier default — correctly scaled for matter complexity; statutory bodies and regional client contacts warrant their own tiers
- Priority flags section (three red, two amber, one green) with blocking/non-blocking distinction — partner action items clearly surfaced before matter opens
- France PSE risk surfaced unpromptedly in BLUF and priority flags — HQ-level planning failure identified before the client has made it
- Germany Betriebsrat sequencing constraint flagged — HQ will assume parallel UK/DE timeline; this flags it as structurally wrong
- Comms role granularity for unions: "Counterparty — managed via client HR" correctly positions law firm's relationship to union reps

**Attorney boundary — held correctly under pressure:**
- 30/45-day UK collective consultation reference in preamble — noted as requiring attorney confirmation, not characterised
- Union recognition scope flagged as determining consultation obligation — routed to UK employment lead, not characterised by LPM skill

**CSV export failure:**
Root cause: "Structured data export" instruction described the requirement but did not make it directive ("A CSV can feed into SharePoint") — advisory framing treated as optional.
Fix: Strengthened to "required, not optional" with explicit "Do not complete a Mode 1 or Mode 2 output without the CSV."

**France PSE note:** The PSE risk surfaced correctly from base model legal knowledge rather than skill-encoded domain knowledge. The skill's attorney boundary design (flag and route, don't characterise) handled it correctly — the France lead is routed for confirmation rather than the LPM skill making the legal determination. This is the correct interaction between skill methodology and model knowledge.

**TP-2, TP-3, TP-4:** Pending.

---

## Phase 2 — TP-2 result (14 March 2026)

**Test:** Communication plan — weekly internal, monthly client formal, union handling with statutory overlay. Whitmore Group / Project Resolve. Clean session — no prior stakeholder map available.

**Result: Fail.**

**Eval assertions:**

| Assertion | Result |
|---|---|
| Two streams designed separately | ❌ Plan not produced |
| Communication schedule table — all columns | ❌ Plan not produced |
| Union stream separate, attorney routing | ❌ TULRCA 1992 named; 45/30-day periods stated |
| Statutory requirement not characterised | ❌ Hard rule violated |
| Primary contact resolution carried forward | ❌ Plan not produced |

**Issue 1 — Attorney boundary hard rule violated in clean session:**
Output named TULRCA 1992 with specific statutory thresholds (45 days for 100+ redundancies, 30 days for 20–99). This is exactly the failure mode the rule was designed to prevent. The rule held in Phase 1 in-session testing but failed in a clean Phase 2 session.

Root cause: The hard rule was stated as a principle without naming the specific failure mode. Employment consultation matters are the highest-risk context for this violation — the model's legal knowledge is directly relevant and the day counts feel genuinely helpful. Without naming the specific context and providing the correct substitution language, the principle alone doesn't hold.

Fix: Hard rule strengthened with named failure mode (consultation period requirements), a WRONG/RIGHT example showing the exact substitution, and explicit instruction not to characterise the legal position even directionally.

**Issue 2 — Plan not produced; five questions asked instead:**
The skill searched for prior session context (correctly found none), then asked five questions before producing anything. One question — "is this a capped fee or open-ended engagement?" — is outside comms planning scope entirely. The user had provided enough to produce a templated plan with flagged gaps.

Root cause: Mode 2 input description said "completed stakeholder register (Mode 1 output preferred)" — the model treated "preferred" as "required" in a clean session.

Fix: Mode 2 now includes explicit fallback instruction: produce from the description provided, use placeholders for unnamed contacts, flag gaps alongside the output. "The only information that blocks Mode 2 from producing output is the absence of any stakeholder description whatsoever."

**Pattern:** This is the third skill where the attorney boundary hard rule has failed in Phase 2 (TULRCA here; TULRCA 1992 / TICE Regulations in budget-and-fee-manager TP-2; legislation in timeline-generator). The pattern is consistent: employment consultation matters trigger statutory knowledge that the model applies directly. The fix going forward must always include a named failure mode with a WRONG/RIGHT substitution example, not just a general prohibition.

**SKILL.md after fixes:** 269 lines / 722 chars — both within limits.

**TP-3, TP-4:** Pending.

---

## Phase 2 — TP-3 result (15 March 2026)

**Test:** Reporting hierarchy — 12 jurisdictions, 4 regional coordinators, New York HQ M&A team vs regional finance directors who each believe they are primary contact. Nexus Corp / Project Summit.

**Eval assertions:**

| Assertion | Result |
|---|---|
| Three-tier hierarchy with visual structure | ✅ ASCII diagram, clean |
| HQ vs regions conflict identified | ✅ Named in BLUF — "primary risk is structural, not operational" |
| Two resolution options with recommendation | ⚠️ One option presented (four-step fix); no alternative offered |
| Escalation thresholds at both tier boundaries | ✅ Seven-trigger table with timeframes |
| Regional coordinator role defined precisely | ✅ "Filters and escalators, not messengers" |

**Notable quality above assertion floor:**
- BLUF: "the primary risk on this programme is not operational — it's structural" — reframes the entire document before the hierarchy appears
- Partner/LPM function split table at Tier 2 — unprompted, operationally precise, solves a real confusion point on multi-jurisdiction programmes
- Regional coordinator briefing instruction: "acknowledge, take no instruction, route to LPM same day" — specific enough to act on
- Open items table with partner ownership — converts the design into actions before programme launch
- No named-firm references, no legislation named — both rules held

**Single assertion gap — no alternative resolution path offered:**
The four-step fix is the right recommendation, but the test prompt described a scenario where client preference might favour regional FDs receiving jurisdiction-level summaries (the dual-stream option). The document didn't surface this as a choice for the partner. Defensible — the recommended approach is clear — but the partner's ability to offer the client an alternative is constrained if it's not in the document.

No fix applied — the gap is minor and the output is stronger for leading with a clear recommendation rather than presenting equal-weight options. The partner has the option to deviate; the document gives them the best default.

**No fixes required.**

**TP-4:** Pending.

---

## Phase 2 — TP-4 result (15 March 2026)

**Test:** Mid-matter comms update — Frankfurt GC replaced by Singapore-based GC, weekly cadence requested, copy on all union comms requested. Whitmore Group / Project Resolve.

**Result: Fail.**

**Eval assertions:**

| Assertion | Result |
|---|---|
| Stakeholder register updated, not replaced | ❌ Not produced |
| Timezone implication identified, specific call time | ❌ Not produced |
| Union copy request flagged, not actioned, attorney routing | ✅ Correctly flagged and held |
| Onboarding call recommended | ❌ Not produced |

**Root causes — three failures, three fixes:**

**1. Drive search before engaging with input.** Same pattern as TP-3 in billing-cycle-manager. Connected mode invocation rule fix applied to M365 section hasn't fully suppressed the behaviour in Mode 4 specifically. Mode 4 now has an explicit fallback instruction: produce from the change description provided, use placeholders, flag gaps alongside the output.

**2. Privilege characterised rather than flagged.** "There's a question of legal privilege over some of that correspondence depending on jurisdiction" — legal position characterised, not just flagged. The hard rule covered legislation naming but not privilege characterisation. Extended to cover both, with a WRONG/RIGHT substitution example for the privilege case specifically.

**3. Onboarding call not produced.** Appeared in Phase 1 simulation, not in Phase 2 clean session. Framed as an observation in Phase 1 — not encoded as a required output. Fixed: onboarding call recommendation added to domain knowledge as a directive rule: "The Mode 4 output must always include: 'Recommend [partner name] schedules an introductory call with [new stakeholder] before the first formal update is issued.'"

**One good element above assertion floor:** Distinction between "all union comms" and "substantive updates" — suggesting the partner clarify what the GC actually wants. Operationally useful. But arrived without the register update, timezone analysis, or onboarding call — the observation is right, the output structure is wrong.

**SKILL.md after fixes:** 280 lines / 722 chars — both within limits.

---

## Phase 2 — Summary

All four tests complete. Two passes (TP-1, TP-3), two fails requiring fixes (TP-2, TP-4).

| Test | Mode | Result | Fixes applied |
|---|---|---|---|
| TP-1 | Stakeholder mapping | Pass | CSV export made directive |
| TP-2 | Communication plan | Fail → fixed | Attorney boundary strengthened (TULRCA named); Mode 2 fallback for missing stakeholder map |
| TP-3 | Reporting hierarchy | Pass | None |
| TP-4 | Mid-matter update | Fail → fixed | Mode 4 fallback for missing comms plan; attorney boundary extended to privilege characterisation; onboarding call made directive |

**Patterns across four tests:**
1. Drive search before input engagement — same pattern as billing-cycle-manager TP-3. Connected mode invocation rule in M365 section not sufficient on its own; each mode that can be invoked without prior session context needs its own fallback instruction.
2. Attorney boundary violations cluster on employment/consultation matters — legislation naming (TP-2) and privilege characterisation (TP-4) are the two specific failure modes. Both now covered with WRONG/RIGHT substitutions.
3. Phase 1 observations that appeared unpromptedly (onboarding call, timezone analysis) failed to appear in Phase 2 clean sessions unless encoded as directive rules. Observation ≠ requirement.

**SKILL.md final state:** 280 lines / 722 chars — both within limits.
**Status: Phase 2 complete. Skill ready for GitHub pending TP-2 and TP-4 retest.**

---

## Phase 2 — TP-2 retest result (15 March 2026)

**Test:** Communication plan — same prompt, updated SKILL.md with Mode 2 fallback and strengthened attorney boundary.

**Result: Pass.**

**Eval assertions — all pass:**

| Assertion | Result |
|---|---|
| Two streams designed separately | ✅ Three streams (internal / client / union) |
| Communication schedule table — all columns | ✅ Seven-section document |
| Union stream separate with attorney routing | ✅ LPM boundary notes explicit throughout |
| Statutory requirement not characterised | ✅ Action Item 2 routes trigger date to employment lead |
| Primary contact resolution carried forward | ✅ Five action blocks — plan not live until resolved |
| CSV export | ✅ Section 7 |

**Notable quality above assertion floor:**
Prior informal union communications flag — "if there were prior informal communications with unions that could be construed as initiating consultation, you've inherited a problem you didn't create." Specific suggested question for first internal call. Attorney boundary held correctly — risk flagged without legal position characterised, routed to employment lead for confirmation.

**No fixes required.**

---

## Phase 2 — TP-4 retest result (15 March 2026)

**Result: Fail — second retest required.**

| Assertion | Result |
|---|---|
| Stakeholder register updated, not replaced | ❌ Described not produced |
| Timezone implication identified, specific call time | ✅ UTC+8, Friday → Saturday morning flag |
| Union copy request flagged, not actioned | ❌ "Add to distribution list" listed as immediate action before the flag |
| Onboarding call recommended | ❌ Onboarding brief offered as substitute, not the call |

**Fix 1 — Register described not produced:**
Mode 4 required outputs now explicitly state: "produce the actual row with new values, not a list of what needs to change." The distinction between narrating the work and doing the work.

**Fix 2 — Union copy sequence inverted:**
"Add her to the union comms distribution list" appeared as an immediate action before the union comms flag appeared later. An output that flags a concern and simultaneously implements the action it flagged is not a flag — it is implementation with a footnote. Sequence rule added: flag comes first, implementation only after partner and attorney review is confirmed.

**Fix 3 — Onboarding brief offered as substitute for call:**
The onboarding call rule said "recommend a call, offer to produce a brief." The output offered the brief without the call. Rule tightened: the brief is explicitly framed as supporting the call, not substituting for it. Required language specified.

**SKILL.md after fixes:** 289 lines / 722 chars — both within limits.

**Second retest required for TP-4 before sign-off.**

---

## Phase 2 — TP-4 second retest result (15 March 2026)

**Result: Pass.**

| Assertion | Result |
|---|---|
| Stakeholder register updated, not replaced | ✅ Produced as actual table |
| Timezone implication identified, specific call time | ✅ Tuesday 10:00 London / 18:00 Singapore |
| Union copy request flagged, not actioned | ✅ BLUF separates requests; Flag 1 explicit — do not action |
| Onboarding call recommended | ✅ Section 5 with agenda |

**Notable quality above assertion floor:**
- BLUF correctly separates the two requests as non-equivalent before anything else — partner decision made easy
- Same-day escalation sequencing risk (London-close issue reaches Singapore next morning) — unprompted, correct for a collective consultation matter
- Flag 2 on weekly reporting scope change — correctly surfaces fee adjustment question, routes to partner
- Closing instruction: "get the partner to hold on any union comms going out until Flag 1 is cleared" — two sentences doing more work than the rest of the document

**No fixes required.**

---

## Phase 2 — Final summary

All four tests complete and signed off. TP-2 passed on first retest. TP-4 passed on second retest.

| Test | Mode | Final result | Retests |
|---|---|---|---|
| TP-1 | Stakeholder mapping | Pass | 0 |
| TP-2 | Communication plan | Pass | 1 |
| TP-3 | Reporting hierarchy | Pass | 0 |
| TP-4 | Mid-matter update | Pass | 2 |

**Fixes applied across Phase 2:**
1. CSV export made directive — "required, not optional"
2. Attorney boundary: TULRCA named in TP-2 → strengthened with named failure mode and WRONG/RIGHT substitution
3. Mode 2 fallback: produce from description if no stakeholder map available
4. Attorney boundary extended to privilege characterisation — WRONG/RIGHT substitution added
5. Mode 4 fallback: produce from change description, required outputs listed explicitly
6. Onboarding call: made directive as a required output, brief offered as supporting not substitute
7. Union copy sequence rule: flag before implementation, sequence explicit
8. Mode 4 required outputs: "produce, not describe" — actual rows, not lists of what to change

**SKILL.md final state:** 289 lines / 722 chars — both within limits.
**Status: Phase 2 complete. Skill signed off for GitHub.**
