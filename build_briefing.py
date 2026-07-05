"""Generates LPM Monday Briefing — 10 May 2026 as a .docx file."""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

OUTPUT = "/home/user/lpm-skills/LPM_Monday_Briefing_10May2026.docx"

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Inches(0.9)
    section.bottom_margin = Inches(0.9)
    section.left_margin   = Inches(1.0)
    section.right_margin  = Inches(1.0)

# ── Helpers ───────────────────────────────────────────────────────────────────

def h1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after  = Pt(2)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(13)
    run.font.color.rgb = RGBColor(0x1F, 0x39, 0x64)  # dark navy
    return p

def h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after  = Pt(1)
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(0x2E, 0x55, 0x97)
    return p

def body(text, bold_spans=None, space_before=0):
    """bold_spans = list of (start, end) char indices to bold."""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(2)
    p.paragraph_format.left_indent  = Inches(0)
    if not bold_spans:
        run = p.add_run(text)
        run.font.size = Pt(10)
    else:
        pos = 0
        for (s, e) in bold_spans:
            if pos < s:
                r = p.add_run(text[pos:s]); r.font.size = Pt(10)
            r = p.add_run(text[s:e]); r.bold = True; r.font.size = Pt(10)
            pos = e
        if pos < len(text):
            r = p.add_run(text[pos:]); r.font.size = Pt(10)
    return p

def bullet(text, bold_start=None, bold_end=None):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(1)
    if bold_start is None:
        run = p.add_run(text); run.font.size = Pt(10)
    else:
        r1 = p.add_run(text[:bold_start]); r1.font.size = Pt(10)
        r2 = p.add_run(text[bold_start:bold_end]); r2.bold = True; r2.font.size = Pt(10)
        r3 = p.add_run(text[bold_end:]); r3.font.size = Pt(10)
    return p

def rule():
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), 'AAAAAA')
    pBdr.append(bottom)
    pPr.append(pBdr)

def add_table(headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    # Header row
    hdr = table.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9)
        cell.paragraphs[0].runs[0].font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'), 'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'), '2E5597')
        tcPr.append(shd)
    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.text = cell_text
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)
            # Alternate row shading
            if r_idx % 2 == 1:
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                shd = OxmlElement('w:shd')
                shd.set(qn('w:val'), 'clear')
                shd.set(qn('w:color'), 'auto')
                shd.set(qn('w:fill'), 'EEF3FB')
                tcPr.append(shd)
    doc.add_paragraph()  # spacing after table


# ═══════════════════════════════════════════════════════════════════════════════
# HEADER BLOCK
# ═══════════════════════════════════════════════════════════════════════════════

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.LEFT
title.paragraph_format.space_before = Pt(0)
title.paragraph_format.space_after  = Pt(4)
r = title.add_run("DAILY BRIEFING — Scott Margetts")
r.bold = True
r.font.size = Pt(16)
r.font.color.rgb = RGBColor(0x1F, 0x39, 0x64)

meta_lines = [
    ("Prepared:",        "Monday 10 May 2026, 06:00 BST"),
    ("Mode:",            "3 — Monday Sweep"),
    ("Portfolio:",       "6 matters — Aldwych | Nexus | Hartwick | Westcliff | Altissima | Meridian"),
    ("Timeframe:",       "Friday 8 May 17:00 BST through Monday 10 May 06:00 BST (+ 7-day lookback context)"),
    ("LPM ownership:",   "Leads: Westcliff (M20118.003), Meridian (M20481.002). "
                         "Oversees: Aldwych + Nexus (Priya Ramanathan); Hartwick + Altissima (Ben Okonkwo)."),
]
for label, value in meta_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(1)
    r1 = p.add_run(label + "  "); r1.bold = True; r1.font.size = Pt(9.5)
    r2 = p.add_run(value); r2.font.size = Pt(9.5)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

h1("SUMMARY")

body(
    "Two matters demand attention before 09:00. Meridian (M20481.002) is the most urgent item "
    "across the book: Aisha Khan's Czech FDI assessment confirms a mandatory FISA filing "
    "is required pre-close, with a 40-working-day review window that puts close at risk if the "
    "filing is not made within two weeks. JMW's direction on supervisory board communication and "
    "filing timing is the first call of the day. Altissima (M17902.011) opened Phase 3 over the "
    "weekend — fee letter signed Friday 8 May — but Uría Menéndez's Friday report that Cuatrecasas "
    "filed a pre-litigation notice at the Madrid Commercial Court on 7 May means a strategy call "
    "with MKT is required before work properly commences.",
    bold_spans=[(0, 2), (46, 65), (244, 247), (433, 452)]
)

body(
    "Aldwych (M18227.001) has a committed deliverable this morning: Priya Ramanathan agreed to "
    "send Marcus Lane a weekly WIP flash by 09:00 Monday. Thursday 14 May is a high-load day "
    "across two matters simultaneously — Aldwych SC at its usual slot and Meridian status call "
    "with Helena Boerger at 14:00 BST — both requiring preparatory deliverables by Wednesday evening.",
    bold_spans=[(0, 7)]
)

body(
    "LPM load pressure is the week's primary cross-matter pattern: Ben Okonkwo leads both "
    "Hartwick and Altissima; Altissima is now Red and generating immediate action. "
    "Scott leads both Westcliff (hard deadline 22 May for LPA amendment draft) and Meridian "
    "(urgent Czech FDI direction needed today, Thursday status call). Monitor bandwidth allocation carefully.",
    bold_spans=[(0, 19)]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# WEEKEND DEVELOPMENTS  (Mode 3)
# ═══════════════════════════════════════════════════════════════════════════════

h1("WEEKEND DEVELOPMENTS")
body("Items received or confirmed between Friday 8 May 17:00 and Monday 10 May 06:00 BST.")

weekend_items = [
    ("Altissima",  "Client",
     "Sofia Esposito (GC) returned signed Phase 3 fee letter Friday 8 May. Phase 3 contested "
     "proceedings now formally authorised; £185k fixed fee. Work commencing week of 11 May."),
    ("Altissima",  "Uría Menéndez",
     "Alejandro Morales reported Cuatrecasas filed a pre-litigation notice with the Madrid "
     "Commercial Court on 7 May. Formal proceedings expected within 4–6 weeks. "
     "Strategy call with MKT recommended this week."),
    ("Aldwych",    "Priya Ramanathan",
     "Internal note confirming SC on Thursday 7 May: Elaine Whitbread accepted escrow holdback "
     "mechanic. SVM gave end-Q3 2026 working close assumption. Priya committed Marcus Lane WIP "
     "flash every Monday by 09:00. Next SC: Thursday 14 May."),
    ("Meridian",   "Aisha Khan",
     "Czech FDI assessment received: MeridianCZ Robotics falls within amended FISA scope. "
     "Mandatory filing required pre-close; 40-working-day review window. Filing needed within "
     "2 weeks or close is at risk. JMW direction awaited; supervisory board not yet informed."),
    ("Altissima",  "Ben Okonkwo",
     "Internal note: Phase 3 formally launched. MKT briefed. Strategy call with Uría Menéndez "
     "being scheduled for Wednesday 13 May."),
]

for matter, source, summary in weekend_items:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after  = Pt(2)
    p.paragraph_format.left_indent  = Inches(0.2)
    r1 = p.add_run(f"[{matter} / {source}]  "); r1.bold = True; r1.font.size = Pt(10)
    r2 = p.add_run(summary); r2.font.size = Pt(10)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# DELIVERABLES
# ═══════════════════════════════════════════════════════════════════════════════

h1("DELIVERABLES — DUE TODAY OR THIS WEEK")
body("Ranked across the portfolio by urgency and impact.")

add_table(
    ["#", "Matter", "Deliverable", "Owner", "By when", "Why this matters"],
    [
        ["1", "Meridian\nM20481.002",
         "Czech FDI: obtain JMW's direction on (a) supervisory board communication timing/framing and "
         "(b) FISA filing decision. Filing must be made within 2 weeks.",
         "Scott → JMW",
         "TODAY",
         "40-working-day review clock has not started. Every day's delay compresses the close window. "
         "Supervisory board held in the dark pending JMW's call."],

        ["2", "Aldwych\nM18227.001",
         "Weekly WIP flash to Marcus Lane. Priya committed to Mondays by 09:00.",
         "Priya Ramanathan",
         "Today by 09:00",
         "Partner-facing commitment made at Thursday 7 May SC. Failure to deliver on day one "
         "damages credibility with client."],

        ["3", "Altissima\nM17902.011",
         "Schedule and confirm strategy call with Uría Menéndez (Alejandro Morales) and MKT re "
         "Cuatrecasas pre-litigation notice. Sofia Esposito also requesting client briefing call.",
         "Ben Okonkwo → MKT",
         "This week (rec. Wed 13 May)",
         "Cuatrecasas pre-litigation notice filed 7 May; formal proceedings expected 4–6 weeks. "
         "Phase 3 work has commenced but strategy not yet confirmed with LC."],

        ["4", "Meridian\nM20481.002",
         "Prepare and deliver status deck to Helena Boerger (Meridian Treasury) for Thursday 14 May "
         "14:00 BST status call.",
         "Scott",
         "Wed 13 May EOD",
         "Client confirmed Wednesday delivery requirement. Thursday call is external and "
         "client-facing — missing the deck deadline is not recoverable."],

        ["5", "Westcliff\nM20118.003",
         "AHL to review LP MFN supplementary memo (Scott's analysis: 3 Fund IV LPs, 22% committed "
         "capital, broad MFN provisions) before QPEPP call.",
         "AHL",
         "This week (before QPEPP call)",
         "LPA amendment draft due to JB Remillard (QPEPP) by 22 May. AHL review is on the critical "
         "path; memo ready and waiting."],

        ["6", "Aldwych\nM18227.001",
         "SVM to review SC briefing note for Thursday 14 May (sent by Priya Sunday evening). "
         "Includes updated timeline to close and indemnification cap bridging position.",
         "SVM",
         "Tues 12 May (overnight review window)",
         "Thursday SC — Cleary counter at 15% EV indemnification cap; firm at 10%. "
         "SVM needs to confirm bridging position before the call."],

        ["7", "Meridian\nM20481.002",
         "Monitor Polish LC (Warsaw) for substantive transfer pricing position. Escalation threshold: "
         "Thursday 14 May COB if no revert. Next LC on panel to be identified now.",
         "Scott",
         "Thu 14 May COB (escalation gate)",
         "Query with Warsaw tax team since 2 April (38+ days). JMW set the escalation threshold "
         "explicitly. Transfer pricing position is needed for deal structuring."],

        ["8", "Hartwick\nM20602.001",
         "Schedule framework agreement call with Catherine Dell (Head of Exits) for week of 18 May. "
         "Brief SVM ahead of client conversation on tiered pricing position.",
         "Ben Okonkwo → SVM",
         "This week (call w/c 18 May)",
         "Catherine Dell confirmed sub-£150m tier works; three assets in market preparation. "
         "SVM to lead — needs briefing from Ben on tiered pricing paper before the call."],
    ]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# ISSUES — CURRENT
# ═══════════════════════════════════════════════════════════════════════════════

h1("ISSUES — CURRENT")
body("Confirmed problems requiring action.")

add_table(
    ["Matter", "Issue", "Status", "Context for action"],
    [
        ["Meridian\nM20481.002",
         "Czech FDI mandatory filing required pre-close",
         "Awaiting JMW direction",
         "MeridianCZ Robotics confirmed within amended FISA scope (defence-adjacent sensor tech). "
         "Mandatory filing triggers 40-working-day review window. Aisha Khan holding communication "
         "to supervisory board pending JMW's framing decision. Filing must be instructed within "
         "2 weeks or the close timeline is compromised."],

        ["Meridian\nM20481.002",
         "Polish LC (Warsaw) silent since 2 April on transfer pricing query",
         "Warsaw partner committed to revert by end of week; JMW set Thu 14 May COB as escalation gate",
         "Query outstanding 38+ days. JMW called Warsaw managing partner; apology received. "
         "Next LC on panel should be identified now so escalation can be immediate if threshold "
         "is breached Thursday."],

        ["Aldwych\nM18227.001",
         "Indemnification cap gap: Cleary at 15% EV, firm at 10%",
         "Active negotiation — round 2 reps/warranties under way",
         "Buyer-side SPA response submitted to Cleary 20 April. Cleary countered at 15%. "
         "SVM needs to confirm bridging position before Thursday 14 May SC. "
         "Elaine Whitbread has also requested updated timeline to close — included in Priya's SC note."],

        ["Meridian\nM20481.002",
         "Italian RE fee letter amendment awaiting countersignature from Wolfgang Steiner",
         "Sent to Wolfgang Steiner. Expected return end of this week.",
         "£85k additional fixed fee for Italian RE workstream. No Italian RE work permitted to "
         "commence until signed. If not returned by Friday 16 May, escalate to JMW."],

        ["Altissima\nM17902.011",
         "Cuatrecasas pre-litigation notice filed 7 May at Madrid Commercial Court",
         "Phase 3 launched; strategy call with Uría Menéndez not yet confirmed",
         "Alejandro Morales: formal proceedings expected within 4–6 weeks. Phase 3 fee letter "
         "signed Friday 8 May. MKT briefed. Strategy call with Uría Menéndez to be confirmed "
         "for Wednesday 13 May. Sofia Esposito (GC) also requesting a client briefing call "
         "this week on contested proceedings timeline."],
    ]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# RISKS — PLAUSIBLE FUTURE
# ═══════════════════════════════════════════════════════════════════════════════

h1("RISKS — PLAUSIBLE FUTURE")
body("Problems requiring monitoring.")

add_table(
    ["Matter", "Risk", "Signal", "Mitigation context"],
    [
        ["Aldwych\nM18227.001",
         "USPTO IPR institution on Baker Industrial petition could disrupt SPA signing",
         "PTAB accorded filing date to Baker Industrial petition; 90-day institution decision window. "
         "Jamie Rodriguez (Skadden) monitoring PTAB docketing.",
         "Escrow holdback mechanic in SPA already accepted by Elaine Whitbread. If PTAB institutes, "
         "SPA mechanics are in place; risk is transaction delay, not structural. "
         "Flag immediately to SVM if institution decision arrives before signing."],

        ["Westcliff\nM20118.003",
         "Fund IV LP MFN exposure broader than initially scoped",
         "Scott's supplementary analysis identifies 3 additional Fund IV LPs (22% committed capital) "
         "with MFN provisions broad enough to capture QPEPP accommodation.",
         "Tiered trigger conditions + ESG-mandate specificity clause recommended by Scott as "
         "drafting approach. AHL review required before QPEPP call. LPA amendment due 22 May — "
         "no disclosure to other Fund IV LPs until amendment executed (AHL's decision)."],

        ["Meridian\nM20481.002",
         "Close timeline compression if Czech FDI filing is delayed",
         "40-working-day review clock has not started. Filing must be made within 2 weeks. "
         "Supervisory board not yet informed.",
         "Filing decision rests with JMW (direction needed today). Once filed, monitor FISA "
         "review clock actively. Supervisory board communication needs careful framing — "
         "Aisha Khan holding until JMW confirms approach."],

        ["Altissima\nM17902.011",
         "Phase 3 fixed fee adequacy if Cuatrecasas proceedings are more complex than scoped",
         "Cuatrecasas moving to formal proceedings (4–6 weeks). Phase 3 fixed fee set at £185k "
         "for contested proceedings before scope of opposition was confirmed.",
         "MKT and Uría Menéndez strategy call will inform whether Phase 3 scope assumptions "
         "hold. Raise with Ben Okonkwo to assess once strategy call completed."],

        ["Meridian\nM20481.002",
         "Polish LC transition risk if Warsaw escalation is required Thursday",
         "Query 38+ days overdue. Escalation threshold set by JMW.",
         "Identify the next LC on the panel now so transition can be instructed immediately "
         "Thursday evening if the substantive position is not received."],
    ]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# CROSS-MATTER PATTERNS
# ═══════════════════════════════════════════════════════════════════════════════

h1("CROSS-MATTER PATTERNS")

body(
    "LPM load pressure — Ben Okonkwo.  "
    "Ben leads both Hartwick (M20602.001) and Altissima (M17902.011). Altissima has moved from "
    "pre-launch to Red this weekend: Phase 3 commenced, Cuatrecasas pre-litigation notice received, "
    "strategy call to confirm, client briefing call to arrange. Hartwick is generating its own "
    "immediate action — scheduling the Catherine Dell framework call and briefing SVM. Both matters "
    "are generating today-urgent work with no natural buffer between. Monitor Ben's capacity "
    "allocation closely this week; the Altissima strategy call and the Hartwick SVM briefing "
    "are likely to compete for the same Tuesday/Wednesday window.",
    bold_spans=[(0, 34)]
)

body(
    "Partner load pressure — SVM.  "
    "SVM is lead partner on both Aldwych (Thursday 14 May SC, indemnification cap bridging position "
    "to confirm) and Hartwick (framework agreement client conversation to lead, week of 18 May). "
    "Thursday 14 May is SVM's highest-load day: Aldwych SC in the morning and the Hartwick SVM "
    "briefing needs to land before the end of the week. No structural conflict, but both matters "
    "need advance preparation from their respective LPMs this week.",
    bold_spans=[(0, 27)]
)

body(
    "Scott's own load — Westcliff + Meridian simultaneously urgent.  "
    "Meridian is the portfolio's most urgent matter (Czech FDI direction today, Wednesday deck, "
    "Thursday status call, Polish LC escalation gate Thursday). Westcliff has a hard external deadline "
    "(LPA amendment to QPEPP by 22 May) with AHL review still outstanding. Both are Scott's direct "
    "matters. Meridian must take priority this week; Westcliff deadline is 12 days out but the "
    "AHL review is on the critical path and should be unblocked today.",
    bold_spans=[(0, 52)]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# PARTNER ATTENTION — PORTFOLIO VIEW
# ═══════════════════════════════════════════════════════════════════════════════

h1("PARTNER ATTENTION — PORTFOLIO VIEW")

add_table(
    ["Matter", "Partner", "Item", "Urgency", "Reference"],
    [
        ["Meridian\nM20481.002",
         "JMW",
         "Direction on Czech FDI filing decision and supervisory board communication timing/framing. "
         "Aisha Khan is holding — nothing moves until JMW calls this.",
         "TODAY",
         "Deliverable #1; Issue 1; Risk 3"],

        ["Altissima\nM17902.011",
         "MKT",
         "Strategy direction with Uría Menéndez re Cuatrecasas pre-litigation notice. "
         "Ben Okonkwo scheduling for Wednesday 13 May.",
         "This week",
         "Deliverable #3; Issue 5"],

        ["Aldwych\nM18227.001",
         "SVM",
         "Review SC briefing note for Thursday 14 May (sent Sunday). Confirm indemnification cap "
         "bridging position (firm at 10%, Cleary at 15%) and updated close timeline.",
         "Tues 12 May",
         "Deliverable #6; Issue 3"],

        ["Westcliff\nM20118.003",
         "AHL",
         "Review LP MFN supplementary memo (ready and waiting). AHL review is on the critical path "
         "to the 22 May LPA amendment deadline.",
         "This week",
         "Deliverable #5; Risk 2"],

        ["Hartwick\nM20602.001",
         "SVM",
         "Briefing from Ben Okonkwo on tiered pricing paper ahead of Catherine Dell framework "
         "agreement call (week of 18 May). SVM to lead the client conversation.",
         "This week",
         "Deliverable #8"],
    ]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# MATTER MINI-BRIEFINGS
# ═══════════════════════════════════════════════════════════════════════════════

h1("MATTER MINI-BRIEFINGS")

# ── Meridian ──────────────────────────────────────────────────────────────────
h2("Meridian Industrial AG  (M20481.002)")
body("RED · Active multi-workstream · Lead Partner: JMW · Lead LPM: Scott Margetts · Fixed fee (Italian RE +£85k) · [Budget/WIP TBC]",
     bold_spans=[(0,3)])
body(
    "The most active matter in the portfolio this week. Three simultaneous workstreams, two "
    "of which are generating urgent action. Czech FDI: Aisha Khan's assessment confirms mandatory "
    "FISA filing required for MeridianCZ Robotics (defence-adjacent sensor tech). 40-working-day "
    "review window; if filing is not instructed within 2 weeks, close is at risk. Supervisory board "
    "not yet informed — JMW's direction is the gate. Italian RE: fee letter amendment (£85k) with "
    "Wolfgang Steiner; countersignature expected this week; no work commences until signed. "
    "Polish LC: Warsaw partner committed to substantive transfer pricing position by Friday — "
    "JMW has set Thursday COB as the escalation threshold. External: status call with Helena Boerger "
    "(Thursday 14 May 14:00 BST) confirmed; status deck needed by Wednesday evening."
)

rule()

# ── Altissima ─────────────────────────────────────────────────────────────────
h2("Altissima Energy SpA  (M17902.011)")
body("RED · Phase 3 — contested proceedings (commenced w/c 11 May) · Lead Partner: MKT · Lead LPM: Ben Okonkwo · Fixed fee £185k · [Budget/WIP TBC]",
     bold_spans=[(0,3)])
body(
    "Phase 3 opened over the weekend: Sofia Esposito signed the fee letter Friday 8 May (£185k "
    "fixed fee for contested proceedings). MKT briefed. The material development is that Cuatrecasas "
    "filed a pre-litigation notice at the Madrid Commercial Court on 7 May — reported by Alejandro "
    "Morales (Uría Menéndez). Formal proceedings expected within 4–6 weeks. Strategy call with MKT "
    "and Uría Menéndez is being scheduled for Wednesday 13 May; Sofia Esposito has also requested "
    "a client call this week on the contested proceedings timeline and what to expect from Cuatrecasas. "
    "Phase 3 fixed fee adequacy is a watch item once strategy is confirmed."
)

rule()

# ── Aldwych ───────────────────────────────────────────────────────────────────
h2("Aldwych Holdings Ltd  (M18227.001)")
body("AMBER · SPA negotiation / pre-signing · Lead Partner: SVM · Lead LPM: Priya Ramanathan · [Fee model / WIP TBC]",
     bold_spans=[(0,5)])
body(
    "SPA negotiation with Caldwell at round 2. Cleary Gottlieb (seller's counsel) has countered "
    "at 15% EV indemnification cap; firm at 10%. Reps and warranties (IP and employment sections) "
    "remain in negotiation. IP DD: Baker Industrial's USPTO IPR petition accorded a filing date — "
    "PTAB has 90 days to decide on institution; escrow holdback mechanic accepted by client and in "
    "the SPA. Thursday 7 May SC outcome: Elaine Whitbread accepted the escrow mechanic; SVM gave "
    "end-Q3 2026 working close assumption; Marcus Lane committed to weekly WIP flash from Priya "
    "by 09:00 Mondays (first one due today). Next SC: Thursday 14 May — SC briefing note sent "
    "by Priya Sunday evening for SVM overnight review."
)

rule()

# ── Westcliff ─────────────────────────────────────────────────────────────────
h2("Westcliff Capital Partners LLP  (M20118.003)")
body("AMBER · LPA amendment — QPEPP sub-fund spinout · Lead Partner: AHL · Lead LPM: Scott Margetts · [Fee model / WIP TBC]",
     bold_spans=[(0,5)])
body(
    "QPEPP IC approved the sub-fund spinout on 21 April, subject to finalisation of MFN carve-out "
    "language. JB Remillard (QPEPP) has set 22 May as the LPA amendment draft deadline. Scott's "
    "supplementary LP MFN exposure analysis (completed this period) identifies three additional "
    "Fund IV LPs representing 22% of committed capital with MFN provisions broad enough to capture "
    "the QPEPP accommodation — tiered trigger conditions + ESG-mandate specificity clause is the "
    "recommended drafting approach. Memo ready for AHL review; AHL review is on the critical path. "
    "Non-disclosure to other Fund IV LPs until the QPEPP amendment is executed — AHL's call."
)

rule()

# ── Nexus ─────────────────────────────────────────────────────────────────────
h2("Nexus Life Sciences SA  (M19330.004)")
body("GREEN · Post-EMA submission / monitoring · Lead Partner: [TBC] · Lead LPM: Priya Ramanathan · [Fee model / WIP TBC]",
     bold_spans=[(0,5)])
body(
    "EMA supplementary submission filed on time: 5 May 2026, 16:42 CET. EMA reference "
    "EMA/SUB/2026/0412 confirmed by Thomas Brüggen (VP Regulatory Affairs, Nexus). 60-day initial "
    "review response window. Homburger's terminology observations incorporated in final QA pass — "
    "no issues. RDM briefed. Active deliverables list closed out. Matter in steady state; "
    "no substantive action required this week."
)

rule()

# ── Hartwick ──────────────────────────────────────────────────────────────────
h2("Hartwick Private Equity  (M20602.001)")
body("GREEN · Programme retainer — pre-engagement / framework structuring · Lead Partner: SVM · Lead LPM: Ben Okonkwo · Programme retainer (tiered pricing) · [WIP TBC]",
     bold_spans=[(0,5)])
body(
    "Step plan for portfolio disposals delivered to SVM 25 April. Tiered pricing options paper "
    "(sub-£75m / sub-£150m / above-£150m) shared at the same time. Catherine Dell (Head of Exits) "
    "replied this weekend: sub-£150m tier structure works as a starting point; three assets "
    "currently being prepared for market in that range. Catherine has proposed moving to framework "
    "agreement discussions — call week of 18 May. SVM to lead the client conversation; "
    "Ben Okonkwo to brief SVM in advance. No active issues or risks this week."
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# READING LIST
# ═══════════════════════════════════════════════════════════════════════════════

h1("READING LIST — WHAT TO OPEN FIRST")
body("Triage judgment. Items that would most change the day if read first.")

add_table(
    ["#", "Source", "Matter", "Why this first", "Read time"],
    [
        ["1", "Aisha Khan\n(internal)",
         "Meridian\nM20481.002",
         "Czech FDI mandatory filing: the single item in the portfolio most likely to affect close "
         "on a live transaction. JMW direction needed before anything else moves.",
         "2 min"],

        ["2", "Alejandro Morales\nUría Menéndez",
         "Altissima\nM17902.011",
         "Cuatrecasas pre-litigation notice filed 7 May. Formal proceedings expected 4–6 weeks. "
         "Strategy call with MKT needs to be confirmed today.",
         "2 min"],

        ["3", "Priya Ramanathan\n(internal)",
         "Aldwych\nM18227.001",
         "Thursday 7 May SC outcome with Marcus Lane commitments. WIP flash is due today by 09:00 — "
         "this note has the commitments that need to be honoured.",
         "2 min"],

        ["4", "Scott Margetts\n(own memo)",
         "Westcliff\nM20118.003",
         "LP MFN supplementary analysis: the memo AHL needs to review. Reading it now lets you "
         "brief AHL concisely and unblock the critical path to the 22 May LPA deadline.",
         "5 min"],

        ["5", "Helena Boerger\nMeridian Industrial",
         "Meridian\nM20481.002",
         "Confirms Wednesday deck deadline and Thursday 14:00 BST status call. "
         "Sets the week's external client-facing hard constraint.",
         "1 min"],
    ]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# WEEK-AHEAD CALENDAR OVERLAY  (Mode 3)
# ═══════════════════════════════════════════════════════════════════════════════

h1("WEEK-AHEAD CALENDAR OVERLAY")
body("Matter-critical dates and scheduling pressure points for w/c 10 May 2026.")

calendar_rows = [
    ("Mon 10 May", "Aldwych",    "WIP flash to Marcus Lane by 09:00",
     "Priya Ramanathan", "MUST HIT — partner-facing commitment"),
    ("Mon 10 May", "Meridian",   "JMW direction on Czech FDI filing + supervisory board framing",
     "Scott → JMW", "Gate for all CZ filing activity"),
    ("Mon 10 May", "Westcliff",  "Chase AHL to review LP MFN memo",
     "Scott", "AHL review on critical path to 22 May"),
    ("Tue 12 May", "Aldwych",    "SVM to review SC briefing note (overnight window)",
     "SVM", "Thursday 14 May SC preparation"),
    ("Wed 13 May", "Altissima",  "Strategy call with Uría Menéndez + MKT (being scheduled)",
     "Ben Okonkwo", "Cuatrecasas response — formal proceedings expected 4–6 wks"),
    ("Wed 13 May", "Meridian",   "Status deck to Helena Boerger by EOD",
     "Scott", "Client-confirmed deadline for Thursday call"),
    ("Thu 14 May", "Aldwych",    "Steering Committee — usual dial-in",
     "SVM / Priya Ramanathan", "Indemnification cap, close timeline"),
    ("Thu 14 May", "Meridian",   "Status call with Helena Boerger 14:00 BST",
     "Scott", "External client — status deck required in advance"),
    ("Thu 14 May", "Meridian",   "Polish LC escalation gate: COB",
     "Scott", "If no substantive position from Warsaw by COB, escalate"),
    ("Fri 16 May", "Meridian",   "Italian RE fee letter expected from Wolfgang Steiner",
     "Scott", "Monitor — no RE work commences until signed"),
    ("22 May",     "Westcliff",  "LPA amendment draft due to JB Remillard (QPEPP)",
     "Scott / AHL", "Hard external deadline — 12 days from today"),
    ("w/c 18 May", "Hartwick",   "Framework agreement call with Catherine Dell",
     "Ben Okonkwo (brief SVM)", "Client confirmed week of 18 May"),
]

add_table(
    ["Date", "Matter", "Event", "Owner", "Notes"],
    [[d, m, e, o, n] for d, m, e, o, n in calendar_rows]
)

rule()


# ═══════════════════════════════════════════════════════════════════════════════
# HANDOFFS FLAGGED
# ═══════════════════════════════════════════════════════════════════════════════

h1("HANDOFFS FLAGGED")

add_table(
    ["Skill", "Matter", "Trigger", "Priority"],
    [
        ["risk-and-issues-manager",
         "Meridian (M20481.002)",
         "Czech FDI mandatory filing confirmed — add to RAID log as Issue. "
         "Polish LC delay — ratcheting risk approaching issue threshold.",
         "Today"],

        ["local-counsel-manager",
         "Meridian (M20481.002)",
         "Warsaw LC non-response 38+ days; escalation gate Thursday 14 May COB. "
         "Identify next LC on panel now.",
         "Today"],

        ["matter-drill-down",
         "Altissima (M17902.011)",
         "Phase 3 launch + Cuatrecasas pre-litigation notice. Full working view "
         "needed ahead of Wednesday strategy call with Uría Menéndez.",
         "Today/Tuesday"],

        ["scope-change-controller",
         "Altissima (M17902.011)",
         "Phase 3 fixed fee (£185k) adequacy to be assessed once strategy call confirms "
         "scope of Cuatrecasas proceedings.",
         "After Wed strategy call"],

        ["budget-and-fee-manager",
         "Meridian (M20481.002)",
         "Italian RE fixed fee (£85k) added to matter; countersignature pending. "
         "Update matter fee model once signed.",
         "On receipt of signed amendment"],

        ["status-report-drafter",
         "Meridian (M20481.002)",
         "Status deck for Helena Boerger, Thursday 14 May 14:00 BST call. "
         "Deadline: Wednesday 13 May EOD.",
         "Wednesday"],

        ["risk-and-issues-manager",
         "Westcliff (M20118.003)",
         "Fund IV LP MFN exposure (22% committed capital, 3 LPs) — add as risk to RAID log.",
         "This week"],
    ]
)


# ═══════════════════════════════════════════════════════════════════════════════
# INFORMATION TO CONFIRM
# ═══════════════════════════════════════════════════════════════════════════════

rule()
h1("INFORMATION TO CONFIRM")

confirm_items = [
    "Partner full names: SVM, AHL, MKT — initials used throughout; confirm full names for formal records.",
    "Nexus Life Sciences SA (M19330.004) — Lead partner name not in inputs.",
    "RAG status for Hartwick and Westcliff — inferred from correspondence; confirm against Intapp Open.",
    "Fee models and WIP/budget figures for Aldwych, Nexus, Hartwick, Westcliff — not in inputs.",
    "Next LC name on the Meridian Polish panel — needed before Thursday escalation gate.",
]
for item in confirm_items:
    bullet(item)

p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(10)
p.paragraph_format.space_after  = Pt(2)
r = p.add_run("End of briefing.")
r.bold = True
r.font.size = Pt(10)
r.font.color.rgb = RGBColor(0x1F, 0x39, 0x64)


# ── Save ──────────────────────────────────────────────────────────────────────
doc.save(OUTPUT)
print(f"Saved: {OUTPUT}")
