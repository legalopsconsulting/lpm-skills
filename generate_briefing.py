from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# ── Page margins ──────────────────────────────────────────────────────────────
for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# ── Styles ────────────────────────────────────────────────────────────────────
normal_style = doc.styles['Normal']
normal_style.font.name = 'Calibri'
normal_style.font.size = Pt(10)

def set_heading(paragraph, text, level=1, color=None):
    run = paragraph.add_run(text)
    run.bold = True
    if level == 1:
        run.font.size = Pt(13)
    elif level == 2:
        run.font.size = Pt(11)
    else:
        run.font.size = Pt(10)
    if color:
        run.font.color.rgb = RGBColor(*color)

def add_heading(doc, text, level=1, color=None, space_before=10, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    set_heading(p, text, level, color)
    return p

def add_para(doc, text, bold=False, italic=False, space_before=0, space_after=4, indent=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after  = Pt(space_after)
    if indent:
        p.paragraph_format.left_indent = Cm(0.6)
    run = p.add_run(text)
    run.bold   = bold
    run.italic = italic
    run.font.size = Pt(10)
    return p

def add_bullet(doc, text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(2)
    if bold_prefix:
        r1 = p.add_run(bold_prefix)
        r1.bold = True
        r1.font.size = Pt(10)
        r2 = p.add_run(text)
        r2.font.size = Pt(10)
    else:
        run = p.add_run(text)
        run.font.size = Pt(10)
    return p

def shade_row(row, hex_color='D9E1F2'):
    for cell in row.cells:
        tc   = cell._tc
        tcPr = tc.get_or_add_tcPr()
        shd  = OxmlElement('w:shd')
        shd.set(qn('w:val'),   'clear')
        shd.set(qn('w:color'), 'auto')
        shd.set(qn('w:fill'),  hex_color)
        tcPr.append(shd)

def make_table(doc, headers, rows, col_widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.LEFT

    # Header row
    hdr = table.rows[0]
    shade_row(hdr, 'D9E1F2')
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(9)

    # Data rows
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        for c_idx, cell_text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            run = p.add_run(str(cell_text))
            run.font.size = Pt(9)

    # Column widths
    if col_widths:
        for i, w in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Cm(w)

    return table

def add_hr(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'),   'single')
    bottom.set(qn('w:sz'),    '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '4472C4')
    pBdr.append(bottom)
    pPr.append(pBdr)
    return p

# ══════════════════════════════════════════════════════════════════════════════
# DOCUMENT HEADER
# ══════════════════════════════════════════════════════════════════════════════
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(0)
run = p.add_run('DAILY BRIEFING — Scott Margetts')
run.bold = True
run.font.size = Pt(16)
run.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

meta_lines = [
    ('Prepared:',        'Monday 10 May 2026, 14:15 BST'),
    ('Mode:',            '3 — Monday sweep'),
    ('Portfolio:',       'Aldwych · Nexus · Hartwick · Westcliff · Altissima · Meridian (6 matters)'),
    ('Timeframe:',       'Friday 2 May 2026 09:00 → Monday 10 May 2026 14:00 BST (weekend window + 7-day pull)'),
    ('LPM ownership:',   'Scott leads: Westcliff (M20118.003), Meridian (M20481.002). '
                         'Scott oversees: Aldwych/Priya Ramanathan, Nexus/Priya Ramanathan, '
                         'Hartwick/Ben Okonkwo, Altissima/Ben Okonkwo'),
]
for label, value in meta_lines:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after  = Pt(1)
    r1 = p.add_run(label + '  ')
    r1.bold = True
    r1.font.size = Pt(9)
    r1.font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
    r2 = p.add_run(value)
    r2.font.size = Pt(9)

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'SUMMARY', 1, (0x1F, 0x49, 0x7D), space_before=8)

summary_text = (
    "Meridian is the day's dominant matter: Aisha Khan's Czech FDI assessment (received this "
    "morning) confirms a mandatory FISA filing is required pre-close, with a 40 working-day "
    "review window — close is at risk if JMW does not direct filing and supervisory board "
    "communication today. Simultaneously, the Polish LC has been non-responsive since 2 April "
    "and JMW's Thursday COB escalation trigger is live.\n\n"
    "Altissima has escalated over the weekend: Cuatrecasas filed a pre-litigation notice with "
    "the Madrid Commercial Court on 7 May, confirming proceedings within 4–6 weeks. Phase 3 "
    "fee letter was signed by Sofia Esposito on Friday 8 May. MKT and Ben Okonkwo need the "
    "Uría Menéndez strategy call confirmed for Wednesday before the weekend window closes "
    "further.\n\n"
    "The Aldwych WIP flash agreed at Thursday's SC (Mondays 09:00 to Marcus Lane) is already "
    "overdue as of this briefing — action needed immediately. The Aldwych SC briefing note "
    "for Thursday 14 May is ready for SVM's overnight review. On Westcliff, Scott's "
    "supplementary LP MFN analysis is with AHL for review; a revised LPA amendment draft "
    "is due to JB Remillard (QPEPP) by 22 May. Nexus is in post-submission monitoring with "
    "no active deliverables. Hartwick has a client opening to progress to framework agreement "
    "discussions (Catherine Dell confirmed week of 18 May).\n\n"
    "Thursday 14 May carries dual client-facing commitments: Aldwych SC (SVM lead) and "
    "Meridian status call at 14:00 BST (Scott lead). Status deck for Meridian must be "
    "with Helena Boerger by Wednesday evening."
)
add_para(doc, summary_text, space_before=2, space_after=6)

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# WEEKEND DEVELOPMENTS (Mode 3)
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'WEEKEND DEVELOPMENTS', 1, (0x1F, 0x49, 0x7D), space_before=8)
add_para(doc, 'Window: Friday 8 May 17:00 → Monday 10 May 07:00 BST', italic=True, space_after=4)

weekend_items = [
    ('Altissima (M17902.011)',
     'Phase 3 fee letter signed and returned by Sofia Esposito (GC, Altissima Energy) on Friday 8 May. '
     'Ben Okonkwo confirmed receipt. Phase 3 work (£185k fixed fee, contested proceedings) commences '
     'this week. [Source: b.okonkwo@firm.com internal note; s.esposito@altissimaenergy.it]'),
    ('Altissima (M17902.011)',
     'Cuatrecasas filed a pre-litigation notice with the Madrid Commercial Court on Wednesday 7 May — '
     'communicated by Alejandro Morales (Uría Menéndez, Madrid) Monday 10 May. Procedural step only, '
     'but confirms intent; formal proceedings expected within 4–6 weeks. Uría Menéndez recommends '
     'strategy call with MKT this week. [Source: a.morales@uriam.com]'),
    ('Nexus (M19330.004)',
     'EMA portal acknowledgement of supplementary response received from Thomas Brüggen (VP Regulatory '
     'Affairs, Nexus Life Sciences SA) over the weekend. Reference EMA/SUB/2026/0412. 60-day initial '
     'review window running from 5 May 2026. No action required — matter in post-submission monitoring. '
     '[Source: t.bruggen@nexuslifesciences.com]'),
]
for matter, text in weekend_items:
    add_bullet(doc, text, bold_prefix=matter + ' — ')

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# DELIVERABLES
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'DELIVERABLES — DUE TODAY OR THIS WEEK', 1, (0x1F, 0x49, 0x7D), space_before=8)
add_para(doc, 'Ranked across the portfolio by urgency and impact. Items 1–2 require same-day action.',
         italic=True, space_after=4)

deliverables = [
    ['1', 'Aldwych (M18227.001)', 'WIP flash → Marcus Lane',
     'Scott / Priya', 'TODAY — 09:00 BST (OVERDUE)',
     'Agreed at Thursday 7 May SC. Marcus Lane specifically requested Mondays by 09:00. SC commitment, first instance.'],
    ['2', 'Meridian (M20481.002)', 'JMW direction: Czech FDI filing + supervisory board communication framing',
     'JMW (direction) / Scott',
     'TODAY',
     'Aisha Khan confirmed FISA mandatory filing required. 40 working-day review window. Close at risk if filing not initiated within 2 weeks. Aisha holding for JMW direction.'],
    ['3', 'Altissima (M17902.011)', 'Uría Menéndez strategy call confirmed (Wed 13 May)',
     'Ben Okonkwo / MKT',
     'Wednesday 13 May',
     'Cuatrecasas pre-litigation notice filed 7 May. 4–6 week countdown to formal proceedings. Alejandro Morales recommends call urgently. MKT briefed.'],
    ['4', 'Altissima (M17902.011)', 'Client call with Sofia Esposito — Phase 3 timeline + Cuatrecasas outlook',
     'Ben Okonkwo',
     'This week',
     'Sofia Esposito specifically requested call on Phase 3 timeline and what to expect from Cuatrecasas in near term. Phase 3 just launched.'],
    ['5', 'Meridian (M20481.002)', 'Status deck → Helena Boerger (Meridian Industrial Treasury)',
     'Scott',
     'Wednesday 13 May (evening)',
     'Client confirmed Thursday 14 May 14:00 BST status call. Helena Boerger asked to receive deck Wednesday evening for review in advance.'],
    ['6', 'Westcliff (M20118.003)', 'LP MFN memo → AHL review before QPEPP call',
     'AHL (review)',
     'Before QPEPP call [date TBC]',
     'Supplementary analysis shows 3 Fund IV LPs (22% committed capital) have MFN provisions broad enough to capture QPEPP accommodation. Tiered trigger + ESG-specificity drafting approach recommended. LPA amendment draft due JB Remillard 22 May.'],
    ['7', 'Aldwych (M18227.001)', 'SC briefing note → SVM overnight review',
     'Priya Ramanathan (note ready)',
     'Tonight / Tuesday 12 May',
     'Note drafted by Priya and sent to Scott this morning. Indemnification cap at round 2 (buyer 10%, Cleary 15% EV). Thursday 14 May SC.'],
    ['8', 'Hartwick (M20602.001)', 'Framework agreement call scheduled with Catherine Dell',
     'SVM (lead) / Ben Okonkwo (brief)',
     'Week of 18 May (client preference)',
     'Catherine Dell (Head of Exits) confirmed sub-£150m tier works; 3 assets in range. SVM to lead; Ben to brief SVM ahead of call.'],
]

make_table(doc,
    ['#', 'Matter', 'Deliverable', 'Owner', 'By when', 'Why this matters'],
    deliverables,
    col_widths=[0.6, 2.8, 3.8, 2.5, 3.0, 4.8])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# ISSUES — CURRENT
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'ISSUES — CURRENT', 1, (0x1F, 0x49, 0x7D), space_before=8)

issues = [
    ['Aldwych (M18227.001)',
     'WIP flash to Marcus Lane overdue',
     'Overdue — agreed Mon 09:00, now 14:15 BST',
     'Priya Ramanathan agreed at 7 May SC to send a weekly WIP flash to Marcus Lane on Mondays by 09:00. First instance missed. Action: Priya to send immediately; Scott to confirm delivery.'],
    ['Meridian (M20481.002)',
     'Czech FDI — mandatory FISA filing required; supervisory board communication direction outstanding',
     'JMW direction outstanding — Aisha Khan holding',
     'MeridianCZ Robotics confirmed to fall within amended FISA scope (defence-adjacent sensor tech). Mandatory pre-close filing required. 40 working-day review window puts close at risk if filing not initiated within 2 weeks from today. Aisha Khan has NOT communicated to supervisory board — holding for JMW direction on timing and framing as agreed. Action: JMW to direct today.'],
    ['Meridian (M20481.002)',
     'Polish LC non-response — Warsaw transfer pricing query outstanding 38 days',
     'JMW spoke with Warsaw MP; revert promised end of week; escalation trigger Thu COB',
     'Query submitted to Warsaw LC 2 April. No substantive response until JMW called MP direct. Warsaw confirmed query with their tax team and apologised. JMW instruction: if no revert by Thursday 14 May COB, escalate to next name on LC panel. Action: Scott to monitor Thursday COB and action escalation if needed.'],
    ['Meridian (M20481.002)',
     'Italian RE workstream blocked — fee amendment countersignature outstanding',
     'Amendment sent; countersignature awaited from Wolfgang Steiner (expected end of week)',
     'Scott sent fee letter amendment to Wolfgang Steiner (Meridian) for Italian RE workstream (£85k additional fixed fee). Team instructed no Italian RE work until signed. Expected return: end of this week per Wolfgang\'s assistant. Action: Chase Friday if not returned Thursday.'],
    ['Altissima (M17902.011)',
     'Cuatrecasas pre-litigation notice filed — strategy call not yet confirmed',
     'Call being scheduled; not yet confirmed',
     'Cuatrecasas filed pre-litigation notice with Madrid Commercial Court 7 May. Formal proceedings expected within 4–6 weeks. Ben Okonkwo flagged Wednesday strategy call with Uría Menéndez — not yet confirmed as of this briefing. Action: Ben to confirm Wednesday slot with MKT and Alejandro Morales today.'],
]

make_table(doc,
    ['Matter', 'Issue', 'Status', 'Context for action'],
    issues,
    col_widths=[2.8, 4.0, 3.5, 7.2])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# RISKS — PLAUSIBLE FUTURE
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'RISKS — PLAUSIBLE FUTURE', 1, (0x1F, 0x49, 0x7D), space_before=8)

risks = [
    ['Aldwych (M18227.001)',
     'PTAB institution decision on USPTO IPR before SPA signing',
     'Baker Industrial petition accorded filing date — PTAB has 90 days to decide on institution. '
     'David Parris monitoring; Jamie Rodriguez (Skadden) has the file.',
     'Escrow holdback mechanic accepted by Elaine Whitbread at Thursday SC — agreed mechanic in SPA. '
     'If institution decision arrives before signing, deal risk is material. Monitor PTAB docketing '
     'via Jamie Rodriguez. Flag immediately to SVM and SC if institution order issued.'],
    ['Aldwych (M18227.001)',
     'Indemnification cap gap — unresolved ahead of SC Thursday 14 May',
     'Buyer position 10% EV; Cleary counter 15% EV — round 2 reps/warranties in play.',
     'SVM needs to decide negotiating position before Thursday SC. Briefing note prepared by Priya '
     'includes draft timeline to close. Risk: SC stalls if SVM has not reviewed and settled position.'],
    ['Westcliff (M20118.003)',
     'LP MFN cascade if carve-out language not agreed before QPEPP execution',
     'Supplementary analysis: 3 Fund IV LPs (22% committed capital) have MFN provisions broad enough '
     'to capture QPEPP accommodation. Tiered trigger + ESG-specificity recommended.',
     'QPEPP not disclosing to other Fund IV LPs until amendment executed — AHL\'s call, agreed with '
     'client. LPA amendment draft due JB Remillard 22 May. If carve-out drafting is not tight, MFN '
     'claims from Fund IV LPs could follow execution. AHL review of the memo is the gating step.'],
    ['Altissima (M17902.011)',
     'Scope escalation risk — Phase 3 fixed fee (£185k) if proceedings accelerate',
     'Phase 3 scoped as contested proceedings. Cuatrecasas pre-litigation notice filed 7 May; formal '
     'proceedings expected 4–6 weeks. Fixed fee agreed.',
     'If proceedings become more complex or multi-track than Phase 3 assumed, £185k fixed fee creates '
     'exposure. Monitor scope assumptions at Wednesday strategy call with Uría Menéndez. Surface to '
     'MKT if Phase 3 scope risk emerges.'],
    ['Meridian (M20481.002)',
     'Czech close timeline risk — FISA filing delay',
     'Even filing within 2 weeks, 40 working-day FISA review window could push close. Supervisory '
     'board not yet informed.',
     'JMW direction on supervisory board communication is the immediate action. Without board '
     'awareness, the timeline risk cannot be managed. Filing delay compounds to close risk. '
     'Aisha Khan holding on communication.'],
    ['Meridian (M20481.002)',
     'Italian RE scope — additional work commences without signed amendment',
     'Fee letter amendment sent; countersignature not yet received.',
     'Work blocked by Scott\'s instruction. Risk is team pressure to start ahead of signature if '
     'status call Thursday looms. Hold the line — no work until Wolfgang Steiner countersigns.'],
]

make_table(doc,
    ['Matter', 'Risk', 'Signal', 'Mitigation context'],
    risks,
    col_widths=[2.8, 4.0, 4.5, 6.2])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# CROSS-MATTER PATTERNS
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'CROSS-MATTER PATTERNS', 1, (0x1F, 0x49, 0x7D), space_before=8)

patterns = [
    ('Partner load pressure — SVM',
     'SVM is lead partner on both Aldwych (Thursday 14 May SC, indemnification cap decision pending, '
     'WIP flash SC commitment overdue) and Hartwick (reviewing tiered pricing paper, to lead the '
     'framework agreement call week of 18 May). Both matters are generating active this-week work '
     'requiring SVM attention simultaneously. Thursday 14 May is the collision point: Aldwych SC '
     'requires SVM to have reviewed the briefing note and settled the indemnification cap position, '
     'while Hartwick requires briefing from Ben ahead of the Catherine Dell call. No natural buffer.'),
    ('LPM load pressure — Ben Okonkwo',
     'Ben leads both Hartwick (portfolio disposals programme, framework negotiations now opening after '
     'Catherine Dell\'s positive response) and Altissima (Phase 3 just launched, contested proceedings '
     'imminent, strategy call this week, client call this week). Both are generating today-and-this-week '
     'urgent work. Altissima has the higher urgency gradient (Cuatrecasas pre-litigation notice, '
     'unconfirmed strategy call, client call request). Monitor Ben\'s capacity across both this week.'),
    ('Regulatory-driven disruption — Meridian and Nexus',
     'Two matters are in active regulatory windows this week driven by external mandatory timelines: '
     'Meridian faces the Czech FISA 40 working-day review window (close at risk within 2 weeks) and '
     'Nexus has the 60-day EMA initial review window running from 5 May. Different regulators and '
     'different urgency profiles (Meridian critical, Nexus monitoring only), but the pattern of '
     'external regulatory timelines dominating matter pace is present across both. No shared response '
     'required — flagged as awareness.'),
    ('Fee structure scope-change wave — Meridian and Altissima',
     'Both matters have fee structure movements this week: Meridian has an unsigned £85k additional '
     'fixed fee amendment for the Italian RE workstream (work blocked until signed) and Altissima has '
     'a freshly signed Phase 3 fixed fee (£185k) with scope escalation risk if proceedings accelerate. '
     'Both matters carry fixed-fee risk on workstreams where scope is not fully settled. Not a crisis '
     'wave, but two matters with active fee-boundary pressure simultaneously.'),
]

for title, body in patterns:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after  = Pt(4)
    r1 = p.add_run(title + ': ')
    r1.bold = True
    r1.font.size = Pt(10)
    r2 = p.add_run(body)
    r2.font.size = Pt(10)

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# PARTNER ATTENTION — PORTFOLIO VIEW
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'PARTNER ATTENTION — PORTFOLIO VIEW', 1, (0x1F, 0x49, 0x7D), space_before=8)

partner_items = [
    ['Aldwych (M18227.001)', 'SVM',
     'Indemnification cap position for Thursday 14 May SC',
     'HIGH — SC Thursday',
     'Deliverable #7 / Issue 1 (WIP flash). Priya\'s note ready. SVM to settle position: buyer 10% vs Cleary counter 15% EV.'],
    ['Aldwych (M18227.001)', 'SVM',
     'WIP flash to Marcus Lane — agreed Monday 09:00, overdue',
     'HIGH — overdue now',
     'Issue 1. SC commitment 7 May. First instance missed.'],
    ['Meridian (M20481.002)', 'JMW',
     'Czech FDI — direction on supervisory board communication timing and framing',
     'CRITICAL — today',
     'Deliverable #2 / Issue 2. Aisha Khan holding. 40 working-day FISA window. Close at risk.'],
    ['Meridian (M20481.002)', 'JMW',
     'Polish LC escalation — confirm Thursday COB trigger is being monitored',
     'MEDIUM — Thursday COB',
     'Issue 3. Warsaw LC promised revert end of week. JMW: escalate to next panel name if nothing by Thursday COB.'],
    ['Westcliff (M20118.003)', 'AHL',
     'LP MFN supplementary memo — review before QPEPP call; LPA amendment direction',
     'HIGH — before QPEPP call',
     'Deliverable #6 / Risk 3. 22% committed capital exposure. LPA amendment draft due JB Remillard 22 May.'],
    ['Altissima (M17902.011)', 'MKT',
     'Confirm Wednesday strategy call with Uría Menéndez on Cuatrecasas position',
     'HIGH — Wednesday',
     'Issue 5 / Deliverable #3. Pre-litigation notice filed 7 May. Ben to confirm slot.'],
    ['Hartwick (M20602.001)', 'SVM',
     'Brief from Ben ahead of framework agreement call (week of 18 May)',
     'MEDIUM — this week',
     'Deliverable #8. Catherine Dell confirmed week of 18 May. SVM to lead; Ben to brief in advance.'],
]

make_table(doc,
    ['Matter', 'Partner', 'Item', 'Urgency', 'Reference'],
    partner_items,
    col_widths=[2.8, 1.5, 5.0, 2.5, 5.7])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# MATTER MINI-BRIEFINGS
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'MATTER MINI-BRIEFINGS', 1, (0x1F, 0x49, 0x7D), space_before=8)

# Meridian
add_heading(doc, 'Meridian Industrial AG (M20481.002)', 2, (0xC0, 0x00, 0x00), space_before=8)
add_para(doc, 'RAG: RED  ·  Phase: Active multi-jurisdictional restructuring programme  ·  Lead Partner: JMW  ·  Lead LPM: Scott Margetts  ·  Fee model: Mixed (programme + fixed-fee workstreams)  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'Three live issues in parallel. Czech FDI is the critical path: MeridianCZ Robotics confirmed '
    'within amended FISA scope; mandatory pre-close filing required; 40 working-day review window '
    'puts close at risk if not filed within 2 weeks. JMW direction on supervisory board communication '
    'outstanding — Aisha Khan holding. Polish LC (Warsaw, transfer pricing) has been non-responsive '
    'since 2 April; JMW spoke to managing partner directly last week; revert promised by Thursday — '
    'escalation trigger if not received. Italian RE workstream blocked pending Wolfgang Steiner\'s '
    'countersignature on £85k fee amendment; team instructed to hold. Thursday 14 May 14:00 BST '
    'status call with Helena Boerger (Treasury, Meridian Industrial) — status deck due Wednesday evening.',
    space_after=4)

# Altissima
add_heading(doc, 'Altissima Energy SpA (M17902.011)', 2, (0xFF, 0x99, 0x00), space_before=8)
add_para(doc, 'RAG: AMBER (escalating)  ·  Phase: Phase 3 — Contested proceedings launched  ·  Lead Partner: MKT  ·  Lead LPM: Ben Okonkwo  ·  Fee model: Fixed fee per phase (Phase 3: £185k)  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'Phase 3 fee letter signed by Sofia Esposito (GC) Friday 8 May — work commences this week. '
    'Cuatrecasas filed a pre-litigation notice with the Madrid Commercial Court on 7 May; formal '
    'proceedings expected within 4–6 weeks. Strategy call with Uría Menéndez (Alejandro Morales, '
    'Madrid) being scheduled for Wednesday — not yet confirmed as of this briefing. Sofia Esposito '
    'has separately requested a client call this week on Phase 3 timeline and Cuatrecasas near-term '
    'outlook. Ben Okonkwo and MKT to action Wednesday call confirmation today. Fixed-fee scope risk '
    'if proceedings accelerate beyond Phase 3 assumptions.',
    space_after=4)

# Aldwych
add_heading(doc, 'Aldwych Holdings Ltd (M18227.001)', 2, (0xFF, 0x99, 0x00), space_before=8)
add_para(doc, 'RAG: AMBER  ·  Phase: SPA negotiation / IP DD  ·  Lead Partner: SVM  ·  Lead LPM: Priya Ramanathan  ·  Fee model: [TBC]  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'SC on Thursday 7 May agreed escrow holdback mechanic for patent opposition (Elaine Whitbread '
    'accepted). SPA buyer response submitted to Cleary Gottlieb 20 April; indemnification cap at '
    'round 2 — buyer 10% vs Cleary counter 15% EV. David Parris has transitioned the file to Jamie '
    'Rodriguez (Skadden); Rodriguez monitoring PTAB docketing. Next SC Thursday 14 May — SVM briefing '
    'note prepared by Priya and ready for overnight review. Marcus Lane WIP flash commitment (Mondays '
    '09:00) first instance missed — action today. Timeline to close: end-Q3 2026 working assumption.',
    space_after=4)

# Westcliff
add_heading(doc, 'Westcliff Capital Partners LLP (M20118.003)', 2, (0xFF, 0x99, 0x00), space_before=8)
add_para(doc, 'RAG: AMBER  ·  Phase: Fund restructuring — QPEPP sub-fund spinout  ·  Lead Partner: AHL  ·  Lead LPM: Scott Margetts  ·  Fee model: [TBC]  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'QPEPP IC approved sub-fund spinout 21 April subject to MFN carve-out language finalisation. '
    'JB Remillard (QPEPP) requires revised LPA amendment draft by 22 May — hard external deadline. '
    'Supplementary LP MFN analysis complete: 3 Fund IV LPs (22% committed capital) have MFN '
    'provisions broad enough to capture QPEPP accommodation; tiered trigger conditions and '
    'ESG-mandate specificity clause recommended. Memo with AHL for review. Westcliff not disclosing '
    'to other Fund IV LPs until QPEPP amendment executed — AHL\'s call. Watch item: AHL review of '
    'memo is gating step before drafting LPA amendment.',
    space_after=4)

# Hartwick
add_heading(doc, 'Hartwick Private Equity (M20602.001)', 2, (0x37, 0x86, 0x10), space_before=8)
add_para(doc, 'RAG: GREEN  ·  Phase: Programme retainer — early stage  ·  Lead Partner: SVM  ·  Lead LPM: Ben Okonkwo  ·  Fee model: Programme retainer / tiered  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'Step plan delivered to SVM 25 April. Tiered pricing options paper shared (sub-£75m / sub-£150m '
    '/ above-£150m). Catherine Dell (Head of Exits) confirmed sub-£150m tier works; three assets in '
    'range being prepared for market. Requested framework agreement discussions — proposed week of '
    '18 May call. SVM to lead; Ben Okonkwo to brief in advance. Steady state — no active issues or '
    'risks this period.',
    space_after=4)

# Nexus
add_heading(doc, 'Nexus Life Sciences SA (M19330.004)', 2, (0x37, 0x86, 0x10), space_before=8)
add_para(doc, 'RAG: GREEN  ·  Phase: Post-submission monitoring  ·  Lead Partner: [TBC]  ·  Lead LPM: Priya Ramanathan  ·  Fee model: [TBC]  ·  WIP: [TBC]',
         italic=True, space_after=3)
add_para(doc,
    'EMA supplementary response filed on time 5 May 2026 (16:42 CET). EMA reference EMA/SUB/2026/0412. '
    'Portal acknowledgement received from Thomas Brüggen (VP Regulatory Affairs). 60-day initial '
    'review window running — response expected ~4 July 2026. Homburger terminology observations '
    'incorporated in final QA pass 22 April. RDM briefed. No outstanding deliverables. '
    'Steady state — monitor for EMA review response.',
    space_after=4)

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# READING LIST
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'READING LIST — WHAT TO OPEN FIRST', 1, (0x1F, 0x49, 0x7D), space_before=8)
add_para(doc, 'If you have 15 minutes before the first call, these five items would most change the day.',
         italic=True, space_after=4)

reading_list = [
    ['1',
     'Email — Aisha Khan (a.khan@firm.com)',
     'Meridian (M20481.002)',
     'Czech FDI assessment confirms FISA mandatory filing. Close at risk. JMW direction needed today. '
     'Contains Aisha\'s judgment on timing and supervisory board framing — read before speaking to JMW.',
     '2 min'],
    ['2',
     'Email — Priya Ramanathan (p.ramanathan@firm.com): Thursday SC briefing note',
     'Aldwych (M18227.001)',
     'SC note for Thursday 14 May. Contains indemnification cap position (10% vs 15% EV), IP DD '
     'summary, draft timeline to close. SVM overnight review needed. Sets up everything for Thursday.',
     '5 min'],
    ['3',
     'Email — Scott Margetts (s.margetts@firm.com): LP MFN supplementary memo',
     'Westcliff (M20118.003)',
     'Supplementary analysis on Fund IV LP MFN exposure. AHL\'s review decision determines the '
     'LPA amendment drafting approach. 22 May external deadline. Memo is ready; delay is the risk.',
     '4 min'],
    ['4',
     'Email — Alejandro Morales (a.morales@uriam.com): Cuatrecasas position',
     'Altissima (M17902.011)',
     'Cuatrecasas pre-litigation notice 7 May. Contains Uría Menéndez\'s tactical read and the '
     '4–6 week proceedings window. Drives Wednesday strategy call urgency.',
     '2 min'],
    ['5',
     'Email — David Parris (d.parris@skadden.com): USPTO IPR update',
     'Aldwych (M18227.001)',
     'PTAB institution decision pending within 90 days. Contains Jamie Rodriguez\'s monitoring '
     'brief. Background needed before Thursday SC if asked about deal risk.',
     '2 min'],
]

make_table(doc,
    ['#', 'Source', 'Matter', 'Why this first', 'Read time'],
    reading_list,
    col_widths=[0.6, 4.5, 2.8, 7.5, 1.5])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# WEEK-AHEAD CALENDAR OVERLAY (Mode 3)
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'WEEK-AHEAD CALENDAR OVERLAY', 1, (0x1F, 0x49, 0x7D), space_before=8)
add_para(doc, 'Week of 11–16 May 2026. Calendar data not returned from connected calendar search — overlay built from correspondence.',
         italic=True, space_after=4)

calendar_items = [
    ['Mon 10 May — TODAY', 'Aldwych (M18227.001)',
     'WIP flash → Marcus Lane | OVERDUE (agreed 09:00) | Send immediately'],
    ['Mon 10 May — TODAY', 'Meridian (M20481.002)',
     'JMW direction on Czech FDI + supervisory board communication | Aisha holding | Today'],
    ['Mon 10 May — TODAY', 'Altissima (M17902.011)',
     'Confirm Wednesday strategy call with Uría Menéndez (Ben + MKT) | Today'],
    ['Tue 11 May', 'Altissima (M17902.011)',
     'Phase 3 work commences (£185k fixed fee, contested proceedings)'],
    ['Wed 12 May', 'Altissima (M17902.011)',
     'Strategy call with Uría Menéndez (Alejandro Morales) | To be confirmed | MKT + Ben'],
    ['Wed 12 May', 'Altissima (M17902.011)',
     'Sofia Esposito client call on Phase 3 timeline + Cuatrecasas outlook | Ben to arrange'],
    ['Wed 12 May (evening)', 'Meridian (M20481.002)',
     'Status deck → Helena Boerger | Must arrive before 09:00 Thu for client review'],
    ['Thu 13 May', 'Aldwych (M18227.001)',
     'SC briefing note → SVM overnight review | Note already drafted by Priya'],
    ['Thu 13 May (14:00 BST)', 'Meridian (M20481.002)',
     'Mid-programme status call — Helena Boerger (Treasury, Meridian Industrial) | Scott leads'],
    ['Thu 13 May', 'Aldwych (M18227.001)',
     'SC — next steering committee | SVM lead | Same dial-in'],
    ['Thu 13 May COB', 'Meridian (M20481.002)',
     'Polish LC escalation trigger — Warsaw to revert by COB or escalate to next panel name (JMW instruction)'],
    ['Fri 14 May (expected)', 'Meridian (M20481.002)',
     'Italian RE fee amendment countersignature expected from Wolfgang Steiner | Chase if not received'],
    ['Wk of 18 May', 'Hartwick (M20602.001)',
     'Framework agreement call — Catherine Dell (Head of Exits, Hartwick PE) | SVM lead | To be scheduled'],
    ['22 May (hard deadline)', 'Westcliff (M20118.003)',
     'LPA amendment draft → JB Remillard (QPEPP) | Gated on AHL review of MFN memo'],
    ['~4 Jul 2026', 'Nexus (M19330.004)',
     'EMA initial review response expected (60-day window from 5 May filing)'],
]

make_table(doc,
    ['Date', 'Matter', 'Item'],
    calendar_items,
    col_widths=[3.5, 3.0, 11.0])

add_hr(doc)

# ══════════════════════════════════════════════════════════════════════════════
# HANDOFFS FLAGGED
# ══════════════════════════════════════════════════════════════════════════════
add_heading(doc, 'HANDOFFS FLAGGED', 1, (0x1F, 0x49, 0x7D), space_before=8)

handoffs = [
    ['risk-and-issues-manager',
     'Meridian (M20481.002)',
     'Czech FDI FISA filing confirmed mandatory — new issue requiring RAID log entry. '
     'Assumption (no FISA obligation) has been invalidated by CZ counsel assessment.',
     'CRITICAL'],
    ['risk-and-issues-manager',
     'Aldwych (M18227.001)',
     'PTAB institution decision risk — update RAID log: Baker Industrial IPR '
     'petition accorded filing date, 90-day window running. Escrow holdback accepted.',
     'HIGH'],
    ['local-counsel-manager',
     'Meridian (M20481.002)',
     'Polish LC (Warsaw) non-response — 38 days on transfer pricing query. Escalation '
     'trigger Thursday COB. Formal LC performance note required.',
     'HIGH'],
    ['scope-change-controller',
     'Meridian (M20481.002)',
     'Italian RE workstream added to programme scope — formal OOS documentation required '
     'for £85k additional fixed fee amendment.',
     'MEDIUM'],
    ['scope-change-controller',
     'Altissima (M17902.011)',
     'Monitor Wednesday strategy call — if Phase 3 fixed fee (£185k) scope assumptions '
     'are challenged by Cuatrecasas proceedings complexity, formal scope change assessment required.',
     'MEDIUM — watch'],
    ['status-report-drafter',
     'Meridian (M20481.002)',
     'Thursday 14 May status call with Helena Boerger requires status deck — '
     'invoke after briefing to produce distributable deck.',
     'HIGH — by Wed evening'],
    ['matter-drill-down',
     'Aldwych (M18227.001)',
     'Thursday SC requires SVM to have settled position on indemnification cap — '
     'invoke for full working view if SVM needs deep-dive on negotiation context.',
     'MEDIUM'],
    ['budget-and-fee-manager',
     'Altissima (M17902.011)',
     'Phase 3 fixed fee £185k signed. Monitor scope vs fee assumption at Wednesday '
     'strategy call — invoke if scope escalation risk materialises.',
     'LOW — watch'],
]

make_table(doc,
    ['Skill', 'Matter', 'Trigger', 'Priority'],
    handoffs,
    col_widths=[3.8, 2.8, 8.5, 2.4])

# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════
add_hr(doc)
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(4)
p.paragraph_format.space_after  = Pt(0)
r1 = p.add_run('End of briefing.  ')
r1.bold = True
r1.font.size = Pt(9)
r2 = p.add_run(
    'Information to confirm: RAG status, fee models, and WIP figures not available in inputs — '
    'placeholder [TBC] used. Nexus lead partner not identified from correspondence. '
    'SVM, AHL, MKT full names not resolved from inputs — confirm against firm directory.'
)
r2.font.size = Pt(8)
r2.italic = True
r2.font.color.rgb = RGBColor(0x59, 0x59, 0x59)

# ── Save ──────────────────────────────────────────────────────────────────────
output_path = '/home/user/lpm-skills/Daily_Briefing_Scott_Margetts_20260510.docx'
doc.save(output_path)
print(f'Saved: {output_path}')
