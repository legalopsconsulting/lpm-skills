"""
Produce the Monday Sweep portfolio briefing as a .docx file.
Mode 3 — Monday sweep | 10 May 2026 | Scott Margetts (Lead LPM)
"""

from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

OUTPUT = "LPM_Monday_Briefing_10May2026.docx"

# ── Helpers ────────────────────────────────────────────────────────────────────

def add_heading(doc, text, level=1):
    p = doc.add_heading(text, level=level)
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    return p


def add_para(doc, text, bold=False, italic=False, size=10, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    run.font.size = Pt(size)
    return p


def add_bullet(doc, text, size=10):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(text)
    run.font.size = Pt(size)
    return p


def shade_row(row, hex_color="D9E1F2"):
    for cell in row.cells:
        tc = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), hex_color)
        tcPr.append(shd)


def add_table(doc, headers, rows, col_widths=None):
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    t.style = "Table Grid"
    # header row
    hdr = t.rows[0]
    shade_row(hdr, "1F3864")
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.text = h
        run = cell.paragraphs[0].runs[0]
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    # data rows
    for ri, row_data in enumerate(rows):
        row = t.rows[ri + 1]
        if ri % 2 == 1:
            shade_row(row, "EEF2F9")
        for ci, val in enumerate(row_data):
            cell = row.cells[ci]
            cell.text = str(val)
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)
    # column widths
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in t.rows:
                row.cells[i].width = Inches(w)
    return t


def hr(doc):
    p = doc.add_paragraph()
    pPr = p._p.get_or_add_pPr()
    pb = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "4472C4")
    pb.append(bottom)
    pPr.append(pb)
    p.paragraph_format.space_after = Pt(4)


# ── Build document ─────────────────────────────────────────────────────────────

doc = Document()

# Page margins
for section in doc.sections:
    section.top_margin    = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin   = Inches(0.9)
    section.right_margin  = Inches(0.9)

# Default font
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(10)

# ── TITLE BLOCK ────────────────────────────────────────────────────────────────

title = doc.add_heading("DAILY BRIEFING — Scott Margetts", 0)
title.alignment = WD_ALIGN_PARAGRAPH.LEFT

meta = [
    ("Prepared",        "Monday 10 May 2026, 07:00 BST"),
    ("Mode",            "3 — Monday sweep"),
    ("Portfolio",       "6 active matters: Aldwych, Altissima, Hartwick, Meridian, Nexus, Westcliff"),
    ("Timeframe",       "Friday 8 May 17:00 BST through Monday 10 May 07:00 BST (+ 7-day context pull)"),
    ("LPM ownership",   "Scott Margetts leads: Westcliff (M20118.003), Meridian (M20481.002). "
                        "Oversees: Aldwych (Priya Ramanathan), Altissima (Ben Okonkwo), "
                        "Hartwick (Ben Okonkwo), Nexus (Priya Ramanathan)."),
]
for label, value in meta:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r1 = p.add_run(f"{label}: ")
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(value)
    r2.font.size = Pt(10)

hr(doc)

# ── SUMMARY ────────────────────────────────────────────────────────────────────

add_heading(doc, "SUMMARY", 1)

add_para(doc, (
    "The portfolio opens the week with two items that compress the morning: "
    "Meridian's Czech FDI mandatory notification has landed with a 2-week filing "
    "window before close is at risk, and JMW is holding on timing — this needs "
    "his direction today. Separately, the Meridian status deck is due Wednesday "
    "evening for Helena Boerger's pre-call review. "
    "Altissima moves into Phase 3 this week following Sofia Esposito's signature "
    "on Friday; Cuatrecasas filed a Madrid pre-litigation notice on 7 May and "
    "formal proceedings are expected within 4-6 weeks. "
    "Westcliff's MFN analysis is complete and in AHL's inbox — the 22 May LPA "
    "amendment deadline is 12 days away and drafting must start this week. "
    "Aldwych's Thursday SC is confirmed; SVM has Priya's briefing note overnight. "
    "Nexus is in steady state in the 60-day EMA review window and requires no "
    "action this week. Hartwick transitions to framework negotiations following "
    "Catherine Dell's positive pricing response — SVM to lead."
), size=10, space_after=6)

hr(doc)

# ── WEEKEND DEVELOPMENTS ───────────────────────────────────────────────────────

add_heading(doc, "WEEKEND DEVELOPMENTS", 1)

weekend = [
    ("Altissima",  "[FROM LC]",    "Alejandro Morales (Uría Menéndez): Cuatrecasas filed pre-litigation notice "
                                   "with Madrid Commercial Court 7 May. Formal proceedings expected within 4-6 "
                                   "weeks. Morales recommends strategy call with MKT this week."),
    ("Altissima",  "[CLIENT]",     "Sofia Esposito (GC, Altissima): Phase 3 fee letter signed and returned "
                                   "Friday 8 May. Phase 3 work authorised at £185k revised fixed fee. Esposito "
                                   "requests a brief call this week on proceedings timeline."),
    ("Altissima",  "[INTERNAL]",   "Ben Okonkwo: Phase 3 launch confirmed. MKT briefed. Strategy call with Uría "
                                   "Menéndez being scheduled for Wednesday 13 May."),
    ("Aldwych",    "[INTERNAL]",   "Priya Ramanathan: SC Thursday 7 May outcome — Elaine Whitbread accepted "
                                   "escrow holdback mechanic; SVM gave end-Q3 2026 working close assumption; "
                                   "Marcus Lane requested weekly WIP flash (Mondays by 09:00). Next SC: "
                                   "Thursday 14 May. Briefing note for 14 May in SVM's inbox for overnight review."),
    ("Aldwych",    "[FROM LC/US]", "David Parris (Skadden NY): USPTO IPR — Baker Industrial petition accorded "
                                   "filing date; PTAB has 90 days to decide institution. Treating as live risk. "
                                   "Jamie Rodriguez monitoring PTAB docketing."),
    ("Meridian",   "[CLIENT]",     "Helena Boerger (Treasury, Meridian): Mid-programme status call confirmed "
                                   "Thursday 14 May 14:00 BST. Status deck requested by Wednesday evening."),
    ("Meridian",   "[INTERNAL]",   "Aisha Khan: Czech CZ counsel confirmed MeridianCZ Robotics falls within "
                                   "amended FISA scope (defence-adjacent sensor technology). Mandatory filing "
                                   "required pre-close. 40 working-day review window — close at risk if not "
                                   "filed within 2 weeks. Holding for JMW direction on board disclosure."),
    ("Westcliff",  "[CLIENT]",     "Andrew Fyfield (Westcliff): QPEPP IC supported sub-fund spinout (decision "
                                   "21 April). JB Rémillard requires revised LPA amendment draft by 22 May. "
                                   "Not disclosing to other Fund IV LPs until QPEPP amendment executed."),
    ("Westcliff",  "[INTERNAL]",   "Scott Margetts: Supplementary LP MFN exposure analysis complete. 3 "
                                   "additional Fund IV LPs (22% committed capital) have MFN provisions broad "
                                   "enough to capture QPEPP accommodation. Tiered trigger conditions and "
                                   "ESG-mandate specificity clause recommended. Memo in AHL's inbox."),
    ("Hartwick",   "[CLIENT]",     "Catherine Dell (Head of Exits, Hartwick PE): Sub-£150m pricing tier "
                                   "accepted. 3 assets being prepared for market in that range. Requests "
                                   "framework agreement discussion call week of 18 May."),
]

for matter, tag, text in weekend:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    p.style = "List Bullet"
    r1 = p.add_run(f"{matter} {tag}  ")
    r1.bold = True
    r1.font.size = Pt(9)
    r2 = p.add_run(text)
    r2.font.size = Pt(9)

hr(doc)

# ── DELIVERABLES ───────────────────────────────────────────────────────────────

add_heading(doc, "DELIVERABLES — DUE TODAY OR THIS WEEK", 1)
add_para(doc, "Ranked across the portfolio by urgency and impact.", italic=True, size=9, space_after=4)

deliverables = [
    ("1", "Meridian",   "JMW direction on Czech FDI timing and supervisory board framing",
     "Scott → JMW",    "Today (Mon 10 May)",
     "40 working-day FISA window. Close at risk if notification not filed within 2 weeks. "
     "Aisha Khan is holding — no escalation until JMW signs off."),

    ("2", "Aldwych",    "Weekly WIP flash to Marcus Lane (Monday by 09:00 commitment)",
     "Priya Ramanathan", "Today (Mon 10 May) 09:00",
     "Priya committed this to Marcus Lane at SC Thursday 7 May. First instalment."),

    ("3", "Meridian",   "Status deck for Helena Boerger mid-programme call",
     "Scott Margetts",  "Wed 13 May (evening)",
     "Helena Boerger confirmed Thu 14 May 14:00 BST call and requested deck day before. "
     "JMW to review before send."),

    ("4", "Altissima",  "MKT/Uría Menéndez strategy call on contested proceedings",
     "Ben Okonkwo (scheduling) / MKT",  "Wed 13 May (target)",
     "Cuatrecasas filed pre-litigation notice 7 May. Morales recommends immediate "
     "strategy call. Sofia Esposito also wants client briefing on timeline."),

    ("5", "Westcliff",  "LPA amendment drafting — start this week against 22 May deadline",
     "Scott Margetts / AHL",  "22 May (external — JB Rémillard)",
     "MFN analysis complete. Tiered trigger + ESG-mandate specificity clause recommended. "
     "12 days to external deadline. Drafting must start now."),

    ("6", "Meridian",   "Italian RE fee letter countersignature (Wolfgang Steiner)",
     "Scott Margetts (chase)",  "End of week (Fri 15 May, per Wolfgang's assistant)",
     "Work embargo active until signed. Italian RE team briefed not to start. "
     "Chase if not received by Thu 14 May AM."),

    ("7", "Meridian",   "Polish LC transfer pricing response (Warsaw/Kowalski & Partners)",
     "JMW (escalation owner)",  "Thu 14 May COB — escalation trigger",
     "JMW directed: escalate to next panel name if nothing by Thu COB. Query with "
     "Warsaw tax team since 2 April."),

    ("8", "Hartwick",   "Framework agreement call scheduling — week of 18 May",
     "Ben Okonkwo → SVM", "This week (calendar)",
     "Catherine Dell confirmed 3 assets sub-£150m being prepared for market. "
     "SVM to lead framework conversation. Ben to brief SVM in advance."),
]

add_table(doc,
    ["#", "Matter", "Deliverable", "Owner", "By when", "Why this matters"],
    deliverables,
    col_widths=[0.25, 0.75, 1.8, 1.2, 1.1, 2.4])

hr(doc)

# ── ISSUES ─────────────────────────────────────────────────────────────────────

add_heading(doc, "ISSUES — CURRENT", 1)
add_para(doc, "Confirmed problems requiring action.", italic=True, size=9, space_after=4)

issues = [
    ("Meridian",  "Czech FDI mandatory notification confirmed",
     "URGENT — direction pending",
     "CZ counsel confirmed MeridianCZ Robotics within amended FISA scope (defence-adjacent "
     "sensors). Mandatory pre-close filing; 40-day review window. Filing must occur within "
     "2 weeks or close timeline at risk. Aisha Khan holding for JMW. Supervisory board not "
     "yet informed — JMW directs timing and framing."),

    ("Altissima", "Cuatrecasas pre-litigation notice filed 7 May",
     "Active — strategy call required this week",
     "Alejandro Morales (Uría Menéndez): pre-litigation notice filed Madrid Commercial "
     "Court 7 May. Formal proceedings expected within 4-6 weeks. Phase 3 now live (£185k "
     "fixed fee, Sofia Esposito signed Friday). MKT/Uría strategy call being scheduled "
     "for Wednesday by Ben Okonkwo."),

    ("Aldwych",   "Indemnification cap: Cleary counter at 15% EV vs buyer at 10%",
     "Active negotiation — SC Thu 14 May",
     "Cleary Gottlieb counter-proposal received. Indemnification cap open in SPA round 2. "
     "IP DD escrow holdback mechanic accepted by Elaine Whitbread at SC 7 May. "
     "Timeline-to-close draft included in Priya's briefing note for SVM overnight review. "
     "Attorney-level decision for SVM at Thursday SC."),

    ("Meridian",  "Italian RE scope addition: work embargo active pending signed fee letter",
     "Contained — countersignature expected end of week",
     "Fee letter amendment (£85k additional fixed fee) sent to Wolfgang Steiner. "
     "Expected countersignature by Fri 15 May per Wolfgang's assistant. "
     "Scott Margetts has briefed team: no Italian RE work to commence until signed."),
]

add_table(doc,
    ["Matter", "Issue", "Status", "Context for action"],
    issues,
    col_widths=[0.85, 1.8, 1.4, 3.45])

hr(doc)

# ── RISKS ──────────────────────────────────────────────────────────────────────

add_heading(doc, "RISKS — PLAUSIBLE FUTURE", 1)
add_para(doc, "Problems that may materialise; monitoring context included.", italic=True, size=9, space_after=4)

risks = [
    ("Aldwych",   "USPTO IPR institution decision before signing",
     "PTAB 90-day decision window now running; Baker Industrial petition filed",
     "David Parris (Skadden): petition accorded filing date; PTAB has 90 days to "
     "decide on institution. If institution decision precedes signing, escrow mechanic "
     "may require SPA renegotiation. Skadden's Jamie Rodriguez monitoring PTAB docket. "
     "Parris will flag immediately if institution decision comes before signing."),

    ("Westcliff", "MFN cascade to 3 additional Fund IV LPs (22% committed capital)",
     "MFN analysis complete — LPs have broad provisions; QPEPP amendment not yet executed",
     "Scott Margetts' analysis confirms 3 Fund IV LPs with MFN provisions broad enough "
     "to capture the QPEPP accommodation. Risk crystallises if another LP learns of "
     "QPEPP accommodation before carve-out language is finalised and executed. "
     "Mitigation: tiered trigger + ESG-mandate specificity clause drafting; "
     "non-disclosure to other Fund IV LPs until QPEPP amendment executed (AHL/Fyfield)."),

    ("Meridian",  "Polish LC non-response (transfer pricing query) ratcheting toward issue",
     "Query with Warsaw tax team since 2 April; revert committed by Thu 14 May COB",
     "JMW spoke with Warsaw managing partner; apologised for non-response; committed "
     "substantive position by end of week. JMW has directed: escalate to next panel "
     "name if nothing by Thursday COB. Handover notes (Scott): build active chase "
     "cadence; substance is reliable when it lands."),

    ("Altissima", "Contested proceedings timeline uncertainty (venue: Spain TBC)",
     "Cuatrecasas filed; formal proceedings expected within 4-6 weeks",
     "Arbitral seat vs court forum not yet confirmed. Phase 3 fixed fee (£185k) may "
     "require further rescope if proceedings extend. Matter has already consumed 91% "
     "of Phase 1/2 cap. Morales monitoring."),

    ("Meridian",  "Czech FDI board disclosure timing — political sensitivity with supervisory board",
     "Board unaware; JMW controls disclosure timing",
     "Per handover notes: Czech FDI is politically sensitive with Meridian supervisory "
     "board. Do not escalate without JMW sign-off. Risk is that if board learns via "
     "other channels (regulators, press) before JMW-directed disclosure, reputational "
     "and trust damage. Mitigate: JMW direction today."),
]

add_table(doc,
    ["Matter", "Risk", "Signal", "Mitigation context"],
    risks,
    col_widths=[0.85, 1.8, 1.5, 3.35])

hr(doc)

# ── CROSS-MATTER PATTERNS ──────────────────────────────────────────────────────

add_heading(doc, "CROSS-MATTER PATTERNS", 1)

patterns = [
    ("LPM load pressure — Scott Margetts",
     "Scott leads both Westcliff and Meridian. This week both matters are generating "
     "today-urgent work simultaneously: Meridian's Czech FDI requires JMW direction "
     "today, the status deck is due Wednesday, and a client call is Thursday; Westcliff's "
     "LPA amendment drafting must start this week against the 22 May external deadline. "
     "There is no natural buffer between these demands. Scott should confirm prioritisation "
     "with AHL and JMW before mid-morning."),

    ("LPM load pressure — Ben Okonkwo",
     "Ben leads both Altissima and Hartwick. Altissima has just entered its most intensive "
     "phase (contested proceedings, Phase 3 live, strategy call this week, client GC "
     "briefing call requested). Hartwick is transitioning to framework — lower intensity "
     "but requires SVM briefing and call scheduling this week. Both matters generating "
     "active work; Altissima is the primary load."),

    ("Partner load pressure — SVM",
     "SVM is lead partner on both Aldwych and Hartwick. This week: SC Thursday (Aldwych) "
     "with overnight briefing note for review tonight; WIP flash from Priya due this "
     "morning; and Hartwick framework call with Catherine Dell needs scheduling for "
     "w/c 18 May. Two active partner touchpoints in the same short window."),

    ("Fee-structure exposure wave",
     "Two matters carry active fee-structure pressure simultaneously. Altissima: Phase 3 "
     "contested proceedings at £185k new fixed fee on top of a matter that consumed 91% "
     "of original Phase 1/2 cap — further rescope risk if proceedings extend. "
     "Meridian: Italian RE scope addition at £85k with work embargo active; plus Czech "
     "FDI filing now required (scope of that work not yet formally assessed or priced)."),
]

for title_text, body_text in patterns:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(5)
    r1 = p.add_run(f"{title_text}. ")
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(body_text)
    r2.font.size = Pt(10)

hr(doc)

# ── PARTNER ATTENTION ──────────────────────────────────────────────────────────

add_heading(doc, "PARTNER ATTENTION — PORTFOLIO VIEW", 1)
add_para(doc, "Items requiring partner decision, response, or action. Referenced to Deliverables (#) or Issues above.", italic=True, size=9, space_after=4)

partner_items = [
    ("Meridian", "JMW",  "Direct Aisha Khan on Czech FDI filing timing and supervisory board framing",
     "CRITICAL — today",   "Deliverable #1; Issue 1"),
    ("Aldwych",  "SVM",  "Review Priya's SC briefing note (in inbox) overnight for Thursday 14 May SC",
     "Tonight",            "Deliverable #2; Issue 3"),
    ("Aldwych",  "SVM",  "Receive WIP flash from Priya by 09:00 today (Marcus Lane commitment)",
     "Today 09:00",        "Deliverable #2"),
    ("Altissima","MKT",  "Participate in Uría Menéndez strategy call (Wednesday); client call with Sofia Esposito",
     "This week",          "Deliverable #4; Issue 2"),
    ("Westcliff","AHL",  "Review Scott's LP MFN memo before LPA amendment drafting commences",
     "Today/tomorrow",     "Deliverable #5"),
    ("Hartwick", "SVM",  "Take Catherine Dell framework call (week of 18 May); Ben to brief in advance",
     "w/c 18 May",         "Deliverable #8"),
]

add_table(doc,
    ["Matter", "Partner", "Item", "Urgency", "Reference"],
    partner_items,
    col_widths=[0.75, 0.6, 2.8, 1.2, 1.15])

hr(doc)

# ── MATTER MINI-BRIEFINGS ──────────────────────────────────────────────────────

add_heading(doc, "MATTER MINI-BRIEFINGS", 1)

matters_data = [
    {
        "title": "Meridian Industrial AG (M20481.002)",
        "roster": "Amber → active | Phase: European Pre-Carve-Out Reorganisation (multi-jurisdiction) | "
                  "Lead Partner: JMW | Lead LPM: Scott Margetts | Fixed fee | WIP: [TBC from billing cycle]",
        "body": (
            "The week is shaped by two simultaneous critical items. First: Czech FDI — Aisha Khan's "
            "assessment arrived this morning confirming MeridianCZ Robotics falls within amended FISA "
            "scope. Mandatory pre-close filing required; 40-day review window means filing within "
            "2 weeks or close timeline breaks. JMW has not yet directed timing or supervisory board "
            "framing — this is today's first-priority action. Second: client status call Thursday "
            "14 May 14:00 BST with Helena Boerger, who has asked for a status deck by Wednesday "
            "evening. JMW reviews before send.\n"
            "Italian RE scope addition: fee letter amendment (£85k) sent to Wolfgang Steiner; "
            "countersignature expected Fri 15 May. Work embargo active — team briefed. Chase if not "
            "received by Thu AM. Polish LC (Kowalski & Partners Warsaw): Warsaw managing partner "
            "committed to revert on transfer pricing by Thu COB; escalation trigger set by JMW if "
            "nothing by then. DE/AT notarial workstream (Ingrid Weber, Munich) is on track — "
            "no close oversight needed per handover notes."
        ),
    },
    {
        "title": "Altissima Energy SpA (M17902.011)",
        "roster": "Red | Phase: Phase 3 Contested Proceedings (launched w/c 11 May) | "
                  "Lead Partner: MKT | Lead LPM: Ben Okonkwo | Fixed fee Phase 3: £185k | "
                  "Original cap: £700k at £640k WIP (91%)",
        "body": (
            "Phase 3 launches this week following Sofia Esposito's signature on the revised fee letter "
            "(Friday 8 May, £185k). Cuatrecasas filed a pre-litigation notice with the Madrid Commercial "
            "Court on 7 May — formal proceedings expected within 4-6 weeks. Alejandro Morales "
            "(Uría Menéndez) recommends immediate strategy call with MKT; Ben is scheduling for "
            "Wednesday. Sofia Esposito has also requested a brief client call this week to understand "
            "the proceedings timeline and near-term Cuatrecasas posture. Two calls to coordinate in "
            "parallel this week. Forum (arbitral seat vs court) remains TBC — bears on Phase 3 "
            "scope and fee adequacy."
        ),
    },
    {
        "title": "Aldwych Holdings Ltd (M18227.001)",
        "roster": "Green | Phase: SPA Negotiation (post-DD) | Lead Partner: SVM | "
                  "Lead LPM: Priya Ramanathan | T&M capped £450k | WIP: £180k at baseline (40%)",
        "body": (
            "SC Thursday 7 May completed satisfactorily. Elaine Whitbread accepted escrow holdback "
            "mechanic for the patent opposition. SVM's working assumption is end-Q3 2026 close subject "
            "to SPA finalisation. Marcus Lane has asked for weekly WIP flash (Mondays 09:00) — "
            "Priya's first instalment is due this morning. Active open item this week: Cleary's counter "
            "on indemnification cap (15% EV vs buyer's 10%). Priya's briefing note for Thursday 14 May "
            "SC is in SVM's inbox for overnight review; it includes a draft updated timeline to close "
            "for Elaine Whitbread. USPTO IPR (Baker Industrial) is a live background risk — "
            "David Parris monitoring PTAB docket."
        ),
    },
    {
        "title": "Westcliff Capital Partners LLP (M20118.003)",
        "roster": "Amber | Phase: Restructure Design / LPA Documentation | Lead Partner: AHL | "
                  "Lead LPM: Scott Margetts | Phased fixed fee £500k | WIP: £310k at baseline (62%)",
        "body": (
            "QPEPP IC decision (21 April) confirmed: sub-fund spinout supported subject to MFN "
            "carve-out language. JB Rémillard's deadline for revised LPA amendment draft is "
            "22 May — 12 days away. Scott Margetts' supplementary MFN analysis is complete: "
            "3 additional Fund IV LPs (22% committed capital) have provisions broad enough to "
            "capture the QPEPP accommodation. Tiered trigger conditions and ESG-mandate specificity "
            "clause are the recommended drafting approach; memo is in AHL's inbox. AHL review needed "
            "before LPA drafting starts. Non-disclosure strategy to other Fund IV LPs remains in "
            "place (AHL/Fyfield decision) until QPEPP amendment executed."
        ),
    },
    {
        "title": "Hartwick Private Equity (M20602.001)",
        "roster": "Green (scoping phase) | Phase: Scoping → Framework transition | "
                  "Lead Partner: SVM | Lead LPM: Ben Okonkwo | Scoping retainer £250k | WIP: £45k at baseline",
        "body": (
            "Positive development this period: Catherine Dell accepted the sub-£150m tier pricing "
            "structure and has confirmed 3 assets in that range being prepared for market. She is "
            "requesting framework agreement discussions for week of 18 May. Step plan and tiered "
            "pricing options paper were delivered as scheduled on 25 April (Ben Okonkwo). "
            "Ben to brief SVM before the framework call; SVM leads the client conversation. "
            "Matter is moving from scoping retainer into the commercially significant framework "
            "agreement phase — per-disposal engagement fees to be negotiated."
        ),
    },
    {
        "title": "Nexus Life Sciences SA (M19330.004)",
        "roster": "Green | Phase: Post-submission (EMA 60-day review window) | "
                  "Lead Partner: RDM | Lead LPM: Priya Ramanathan | Fixed fee £200k | WIP: £85k at baseline",
        "body": (
            "EMA submission filed on time 5 May 2026 (16:42 CET). EMA reference: "
            "EMA/SUB/2026/0412. Thomas Brüggen confirmed receipt from EMA portal. "
            "60-day initial review window — earliest EMA response ~early July 2026. "
            "Homburger's two terminology observations were incorporated pre-submission. "
            "Matter is in steady state this week; no action required."
        ),
    },
]

for m in matters_data:
    p_heading = doc.add_paragraph()
    p_heading.paragraph_format.space_before = Pt(8)
    p_heading.paragraph_format.space_after = Pt(2)
    r = p_heading.add_run(m["title"])
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x1F, 0x38, 0x64)

    roster_p = doc.add_paragraph()
    roster_p.paragraph_format.space_after = Pt(3)
    rr = roster_p.add_run(m["roster"])
    rr.italic = True
    rr.font.size = Pt(9)
    rr.font.color.rgb = RGBColor(0x44, 0x44, 0x44)

    body_p = doc.add_paragraph()
    body_p.paragraph_format.space_after = Pt(5)
    rb = body_p.add_run(m["body"])
    rb.font.size = Pt(10)

hr(doc)

# ── READING LIST ───────────────────────────────────────────────────────────────

add_heading(doc, "READING LIST — WHAT TO OPEN FIRST", 1)
add_para(doc, "Triage judgment: what would most change the day if read first.", italic=True, size=9, space_after=4)

reading = [
    ("1", "Email", "Meridian",  "Aisha Khan: Czech FDI assessment — full text has the '2-week window' "
                                "and board-sensitivity detail JMW will ask about",         "3 min"),
    ("2", "Email", "Altissima", "Alejandro Morales (Uría Menéndez): Cuatrecasas position — "
                                "the 4-6 week timeline and strategy call recommendation are in here",  "2 min"),
    ("3", "Email", "Aldwych",   "Priya Ramanathan: SC Thursday 7 May outcome — Marcus Lane's "
                                "WIP flash commitment is explicit; confirms what's due today",         "2 min"),
    ("4", "Email", "Westcliff", "Scott Margetts → AHL: LP MFN memo — confirms analysis is ready "
                                "and drafting recommendation before AHL can unblock LPA work",         "4 min"),
    ("5", "Email", "Meridian",  "Helena Boerger: Status call confirmed — Wednesday deck deadline "
                                "and Thursday 14:00 BST confirmed; actionable for diary today",        "1 min"),
]

add_table(doc,
    ["#", "Source", "Matter", "Why this first", "Read time"],
    reading,
    col_widths=[0.25, 0.6, 0.85, 4.5, 0.8])

hr(doc)

# ── WEEK-AHEAD CALENDAR OVERLAY ────────────────────────────────────────────────

add_heading(doc, "WEEK-AHEAD CALENDAR OVERLAY", 1)

cal_items = [
    ("Mon 10 May",  "Aldwych",    "WIP flash due to Marcus Lane by 09:00 (Priya Ramanathan)"),
    ("Mon 10 May",  "Meridian",   "JMW direction required on Czech FDI: filing timing + board disclosure framing"),
    ("Tue 11 May",  "Altissima",  "Phase 3 work commences (Ben Okonkwo / MKT)"),
    ("Wed 13 May",  "Altissima",  "MKT / Uría Menéndez strategy call (Ben Okonkwo scheduling)"),
    ("Wed 13 May",  "Meridian",   "Status deck due to Helena Boerger by close of business (Scott Margetts / JMW review)"),
    ("Thu 14 May",  "Aldwych",    "Weekly SC, dial-in TBC, 08:30 BST pre-SC prep (Priya / SVM); "
                                  "Briefing note in SVM inbox for overnight review"),
    ("Thu 14 May",  "Meridian",   "Mid-programme status call with Helena Boerger, 14:00 BST"),
    ("Thu 14 May",  "Meridian",   "Polish LC (Warsaw) revert deadline — COB escalation trigger if no response"),
    ("Fri 15 May",  "Meridian",   "Italian RE fee letter countersignature expected (Wolfgang Steiner)"),
    ("w/c 18 May",  "Hartwick",   "Framework agreement call with Catherine Dell (SVM leads; Ben to brief)"),
    ("22 May",      "Westcliff",  "LPA amendment draft due to JB Rémillard (QPEPP) — external hard deadline"),
]

add_table(doc,
    ["Date", "Matter", "Item"],
    cal_items,
    col_widths=[0.95, 0.95, 5.6])

doc.add_paragraph()
add_para(doc,
    "Note: No calendar data was connected for this sweep. Dates above are inferred from "
    "correspondence and commitments in the 7-day email pull. Confirm against live calendar "
    "before acting.",
    italic=True, size=9, space_after=6)

hr(doc)

# ── HANDOFFS ───────────────────────────────────────────────────────────────────

add_heading(doc, "HANDOFFS FLAGGED", 1)
add_para(doc, "Single-matter skills to invoke as follow-through.", italic=True, size=9, space_after=4)

handoffs = [
    ("risk-and-issues-manager",  "Meridian",   "Czech FDI mandatory FISA notification — new critical issue; RAID log update required",      "Critical — today"),
    ("scope-change-controller",  "Meridian",   "Czech FDI filing work not yet priced or formally scoped — scope change assessment required",  "High — this week"),
    ("risk-and-issues-manager",  "Altissima",  "Cuatrecasas pre-litigation notice — issue promotion; RAID update required for Phase 3",       "High — today"),
    ("budget-and-fee-manager",   "Altissima",  "Phase 3 at £185k new fixed fee — forecast-to-complete and write-off exposure tracking from Phase 1/2",  "Medium — this week"),
    ("local-counsel-manager",    "Meridian",   "Polish LC (Warsaw) non-response ratcheting — escalation protocol if Thu COB missed",          "Medium — monitor to Thu"),
    ("risk-and-issues-manager",  "Westcliff",  "MFN cascade risk — RAID log update with 3 additional LP exposure and 22 May deadline",        "Medium — this week"),
    ("status-report-drafter",    "Aldwych",    "SPA negotiation status report for Marcus Lane / Elaine Whitbread (if requested post-SC)",     "Low — standby"),
]

add_table(doc,
    ["Skill", "Matter", "Trigger", "Priority"],
    handoffs,
    col_widths=[1.5, 0.85, 3.85, 1.3])

hr(doc)

# ── FOOTER ─────────────────────────────────────────────────────────────────────

doc.add_paragraph()
add_para(doc, "End of briefing.", bold=True, size=10)
add_para(doc,
    "Information to confirm: Meridian RAG status (not stated in baseline — treating as Amber given "
    "volume of active critical items); Meridian fixed-fee total and current WIP (billing cycle not "
    "pulled for this sweep); calendar data not connected (dates inferred from correspondence).",
    italic=True, size=8, space_after=2)
add_para(doc,
    "Source: Outlook 7-day pull (3–10 May 2026) + SharePoint matter baselines and handover notes "
    "(all last updated May 2026). Produced by LPM Monday Sweep Routine.",
    italic=True, size=8)

doc.save(OUTPUT)
print(f"Saved: {OUTPUT}")
