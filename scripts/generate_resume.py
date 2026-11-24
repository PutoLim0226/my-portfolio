#!/usr/bin/env python3
"""
Generate bilingual resume PDFs:
- public/resume_en.pdf (English)
- public/resume_zh.pdf (Traditional/Simplified Chinese)
- public/resume.pdf (Bilingual: Page 1 EN, Page 2 ZH)
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONT_PATH = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
pdfmetrics.registerFont(TTFont('ZenHei', FONT_PATH))

PRIMARY_COLOR = colors.HexColor('#1e293b')   # Slate 800
ACCENT_COLOR = colors.HexColor('#b45309')    # Amber 700
TEXT_MUTED = colors.HexColor('#64748b')      # Slate 500
BORDER_COLOR = colors.HexColor('#cbd5e1')    # Slate 300
BG_TAG = colors.HexColor('#f1f5f9')          # Slate 100

def get_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        'ResumeName',
        fontName='ZenHei',
        fontSize=20,
        leading=24,
        textColor=PRIMARY_COLOR,
        fontStyle='bold'
    ))
    
    styles.add(ParagraphStyle(
        'ResumeTitle',
        fontName='ZenHei',
        fontSize=12,
        leading=16,
        textColor=ACCENT_COLOR
    ))
    
    styles.add(ParagraphStyle(
        'ResumeContact',
        fontName='ZenHei',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_MUTED
    ))
    
    styles.add(ParagraphStyle(
        'SectionHeader',
        fontName='ZenHei',
        fontSize=11,
        leading=14,
        textColor=PRIMARY_COLOR,
        spaceBefore=6,
        spaceAfter=3
    ))
    
    styles.add(ParagraphStyle(
        'BodyNormal',
        fontName='ZenHei',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#334155')
    ))
    
    styles.add(ParagraphStyle(
        'ItemTitle',
        fontName='ZenHei',
        fontSize=9.5,
        leading=12.5,
        textColor=PRIMARY_COLOR
    ))
    
    styles.add(ParagraphStyle(
        'ItemSub',
        fontName='ZenHei',
        fontSize=8,
        leading=10,
        textColor=ACCENT_COLOR
    ))
    
    styles.add(ParagraphStyle(
        'SkillCategory',
        fontName='ZenHei',
        fontSize=8.5,
        leading=11.5,
        textColor=PRIMARY_COLOR
    ))
    
    styles.add(ParagraphStyle(
        'SkillList',
        fontName='ZenHei',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#475569')
    ))

    return styles

def build_en_elements(styles):
    el = []
    # Header
    el.append(Paragraph("LIM JUN HUI (林俊匯)", styles['ResumeName']))
    el.append(Paragraph("Full-Stack Developer", styles['ResumeTitle']))
    contact_text = (
        "Email: <a href='mailto:junhui.lim@gmail.com' color='#b45309'>junhui.lim@gmail.com</a> &nbsp;|&nbsp; "
        "Portfolio: <a href='https://putolim0226.github.io/my-portfolio/en' color='#b45309'>putolim0226.github.io/my-portfolio/en</a> &nbsp;|&nbsp; "
        "GitHub: <a href='https://github.com/PutoLim0226' color='#b45309'>github.com/PutoLim0226</a>"
    )
    el.append(Paragraph(contact_text, styles['ResumeContact']))
    el.append(Spacer(1, 2*mm))
    el.append(HRFlowable(width="100%", thickness=1, color=BORDER_COLOR, spaceBefore=0, spaceAfter=4))

    # Professional Summary
    el.append(Paragraph("PROFESSIONAL SUMMARY", styles['SectionHeader']))
    summary_text = (
        "Full-stack developer with comprehensive expertise in building performant, scalable, and maintainable web applications. "
        "Proficient in modern frontend architectures with React and Vite, backend RESTful API services with PHP, Go, and Python, "
        "relational and in-memory database management (MySQL, Redis), and end-to-end Linux server deployment with Nginx."
    )
    el.append(Paragraph(summary_text, styles['BodyNormal']))
    el.append(Spacer(1, 2*mm))

    # Technical Skills
    el.append(Paragraph("TECHNICAL SKILLS", styles['SectionHeader']))
    skills_data = [
        [Paragraph("<b>Frontend:</b>", styles['SkillCategory']), Paragraph("React 19, JavaScript (ES6+), HTML5, CSS3/SCSS, Vite, Responsive Design, i18n", styles['SkillList'])],
        [Paragraph("<b>Backend:</b>", styles['SkillCategory']), Paragraph("PHP (RESTful API, PHP-FPM), Python, Go", styles['SkillList'])],
        [Paragraph("<b>Database:</b>", styles['SkillCategory']), Paragraph("MySQL (Indexing, Relational Design), Redis (Caching & Sessions)", styles['SkillList'])],
        [Paragraph("<b>DevOps & Infra:</b>", styles['SkillCategory']), Paragraph("Linux (Ubuntu), Nginx (Reverse Proxy, SSL), Git, GitHub Actions (CI/CD), UFW", styles['SkillList'])],
    ]
    t = Table(skills_data, colWidths=[28*mm, 150*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    el.append(t)
    el.append(Spacer(1, 2*mm))

    # Featured Projects
    el.append(Paragraph("FEATURED PROJECTS", styles['SectionHeader']))
    
    projects = [
        {
            "name": "Vintage E-Commerce",
            "tech": "PHP (OOP / RESTful API), MySQL, Redis, React, Nginx",
            "desc": "High-end e-commerce platform for vintage collections featuring smooth shopping cart operations, catalog search, session caching with Redis, and custom PHP backend deployed on Ubuntu with Nginx.",
            "link": "Live Demo: http://45.32.25.8:8090/"
        },
        {
            "name": "Case Profile System",
            "tech": "React, Dynamic Data Visualization, REST API",
            "desc": "An academic profile and case study management system featuring interactive data dashboards and case research visualization.",
            "link": "Live Demo: https://caseprofile2.asia.edu.tw/"
        },
        {
            "name": "Hui Yin Seh Charity Portal",
            "tech": "React, PHP API, MySQL, Ubuntu Server",
            "desc": "Official portal for a Malaysian non-profit organization supporting activity announcements, member registration, and community outreach.",
            "link": "Live Demo: http://45.32.25.8:8080/"
        },
        {
            "name": "Aurora Coffee",
            "tech": "React, SCSS, Responsive Web Design",
            "desc": "An immersive coffee shop website with interactive menu browsing, modern aesthetics, and fluid animations.",
            "link": "Live Demo: https://putolim0226.github.io/aurora-coffee/"
        },
        {
            "name": "YHD Corporate Site & Play YHD",
            "tech": "Frontend Architecture, UI/UX Design, Gaming Community Portal",
            "desc": "Digital transformation corporate landing page and interactive gaming community portal with responsive themes.",
            "link": "Live Demos: https://yhd.tw/ | https://play.yhd.tw/"
        }
    ]

    for p in projects:
        title_table = Table([[
            Paragraph(f"<b>{p['name']}</b>", styles['ItemTitle']),
            Paragraph(f"<a href='{p['link'].split(': ')[-1]}' color='#b45309'>{p['link']}</a>", styles['ResumeContact'])
        ]], colWidths=[80*mm, 98*mm])
        title_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        el.append(title_table)
        el.append(Paragraph(f"<b>Tech Stack:</b> {p['tech']}", styles['ItemSub']))
        el.append(Paragraph(p['desc'], styles['BodyNormal']))
        el.append(Spacer(1, 1.5*mm))

    return el

def build_zh_elements(styles):
    el = []
    # Header
    el.append(Paragraph("林俊匯 (LIM JUN HUI)", styles['ResumeName']))
    el.append(Paragraph("全端工程師 (Full-Stack Developer)", styles['ResumeTitle']))
    contact_text = (
        "電子信箱: <a href='mailto:junhui.lim@gmail.com' color='#b45309'>junhui.lim@gmail.com</a> &nbsp;|&nbsp; "
        "個人作品集: <a href='https://putolim0226.github.io/my-portfolio/en' color='#b45309'>putolim0226.github.io/my-portfolio/en</a> &nbsp;|&nbsp; "
        "GitHub: <a href='https://github.com/PutoLim0226' color='#b45309'>github.com/PutoLim0226</a>"
    )
    el.append(Paragraph(contact_text, styles['ResumeContact']))
    el.append(Spacer(1, 2*mm))
    el.append(HRFlowable(width="100%", thickness=1, color=BORDER_COLOR, spaceBefore=0, spaceAfter=4))

    # Professional Summary
    el.append(Paragraph("專業簡歷", styles['SectionHeader']))
    summary_text = (
        "全端工程師，專注於構建高效能、高擴展性且易於維護的現代化網頁應用程式。"
        "具備前端 React 19 與 SCSS 響應式開發架構、後端 PHP (RESTful API)、Go、Python 服務開發、"
        "關聯式與內存快取資料庫 (MySQL, Redis) 設計與效能調優，以及 Linux (Ubuntu) 與 Nginx 伺服器部署維運之完整實務經驗。"
    )
    el.append(Paragraph(summary_text, styles['BodyNormal']))
    el.append(Spacer(1, 2*mm))

    # Technical Skills
    el.append(Paragraph("核心技術堆疊", styles['SectionHeader']))
    skills_data = [
        [Paragraph("<b>前端技術:</b>", styles['SkillCategory']), Paragraph("React 19, JavaScript (ES6+), HTML5, CSS3 / SCSS, Vite, RWD 響應式設計, i18n 多國語系", styles['SkillList'])],
        [Paragraph("<b>後端開發:</b>", styles['SkillCategory']), Paragraph("PHP (物件導向, RESTful API, PHP-FPM), Python, Go", styles['SkillList'])],
        [Paragraph("<b>資料庫與快取:</b>", styles['SkillCategory']), Paragraph("MySQL (索引優化, Schema 設計), Redis (快取架構, Session 管理)", styles['SkillList'])],
        [Paragraph("<b>維運與工具:</b>", styles['SkillCategory']), Paragraph("Linux (Ubuntu), Nginx (反向代理, SSL 配置), Git, GitHub Actions (自動化 CI/CD), UFW 防火牆", styles['SkillList'])],
    ]
    t = Table(skills_data, colWidths=[28*mm, 150*mm])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    el.append(t)
    el.append(Spacer(1, 2*mm))

    # Featured Projects
    el.append(Paragraph("精選專案成果", styles['SectionHeader']))
    
    projects = [
        {
            "name": "復古刻痕電商平台 (Vintage E-Commerce)",
            "tech": "PHP (RESTful API), MySQL, Redis, React, Nginx",
            "desc": "自建後端之高端復古選品電商平台，支援購物車狀態持久化、分類商品篩選、Redis 查詢快取，前後端分離部署於 Ubuntu Linux 伺服器。",
            "link": "線上展示: http://45.32.25.8:8090/"
        },
        {
            "name": "個案基本資料系統 (Case Profile System)",
            "tech": "React, 動態資料視覺化, REST API 整合",
            "desc": "學術機構之個案研究與個人檔案管理系統，具備多維度資料視覺化儀表板及檔案檢索功能。",
            "link": "線上展示: https://caseprofile2.asia.edu.tw/"
        },
        {
            "name": "馬來西亞慧音社慈善入口網 (Hui Yin Seh)",
            "tech": "React, PHP API, MySQL, Linux 伺服器管理",
            "desc": "非營利慈善機構之官方資訊與志工活動平台，提供動態最新消息、活動報名與社群服務功能。",
            "link": "線上展示: http://45.32.25.8:8080/"
        },
        {
            "name": "極光咖啡 (Aurora Coffee)",
            "tech": "React, SCSS, 互動式響應式設計",
            "desc": "沉浸式質感咖啡品牌線上體驗站，具備互動式菜單切換與流暢的動畫展示細節。",
            "link": "線上展示: https://putolim0226.github.io/aurora-coffee/"
        },
        {
            "name": "YHD 企業網站 & Play YHD 遊戲入口",
            "tech": "前端架構規劃, UI/UX 響應式設計, 社群功能",
            "desc": "俐落現代感之數位轉型企業官網與互動遊戲社群入口平台，支援多裝置流暢體驗。",
            "link": "線上展示: https://yhd.tw/ | https://play.yhd.tw/"
        }
    ]

    for p in projects:
        title_table = Table([[
            Paragraph(f"<b>{p['name']}</b>", styles['ItemTitle']),
            Paragraph(f"<a href='{p['link'].split(': ')[-1]}' color='#b45309'>{p['link']}</a>", styles['ResumeContact'])
        ]], colWidths=[80*mm, 98*mm])
        title_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (1,0), (1,0), 'RIGHT'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 1),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        el.append(title_table)
        el.append(Paragraph(f"<b>使用技術:</b> {p['tech']}", styles['ItemSub']))
        el.append(Paragraph(p['desc'], styles['BodyNormal']))
        el.append(Spacer(1, 1.5*mm))

    return el

def generate():
    styles = get_styles()
    os.makedirs('public', exist_ok=True)
    margin = 12 * mm

    # 1. English Resume (Single Page A4)
    doc_en = SimpleDocTemplate(
        "public/resume_en.pdf",
        pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=margin
    )
    doc_en.build(build_en_elements(styles))
    print("Generated public/resume_en.pdf")

    # 2. Chinese Resume (Single Page A4)
    doc_zh = SimpleDocTemplate(
        "public/resume_zh.pdf",
        pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=margin
    )
    doc_zh.build(build_zh_elements(styles))
    print("Generated public/resume_zh.pdf")

    # 3. Bilingual Combined Resume (Page 1: EN, Page 2: ZH)
    doc_combined = SimpleDocTemplate(
        "public/resume.pdf",
        pagesize=A4,
        leftMargin=margin, rightMargin=margin,
        topMargin=margin, bottomMargin=margin
    )
    combined_elements = build_en_elements(styles) + [PageBreak()] + build_zh_elements(styles)
    doc_combined.build(combined_elements)
    print("Generated public/resume.pdf")

if __name__ == '__main__':
    generate()
