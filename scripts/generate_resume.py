#!/usr/bin/env python3
"""
Generate High-End Executive Designer Resumes:
- public/resume_en.pdf (100% English, zero Chinese mixing)
- public/resume_zh.pdf (100% Traditional Chinese, zero English mixing)
- public/resume.pdf (Bilingual: Page 1 Pure EN, Page 2 Pure ZH)
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pypdfium2 as pdfium

FONT_PATH = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
pdfmetrics.registerFont(TTFont('ZenHei', FONT_PATH))

W, H = A4
HEADER_HEIGHT = 40 * mm
SIDEBAR_WIDTH = 60 * mm
CONTENT_WIDTH = W - SIDEBAR_WIDTH - 24 * mm  # ~126mm

# Executive Palette
COLOR_NAVY = colors.HexColor('#0f172a')        # Deep Slate Navy
COLOR_NAVY_LIGHT = colors.HexColor('#1e293b')  # Slate 800
COLOR_AMBER = colors.HexColor('#d97706')       # Warm Amber Primary
COLOR_AMBER_LIGHT = colors.HexColor('#fbbf24') # Amber Accent Light
COLOR_TEXT_MAIN = colors.HexColor('#1e293b')   # Dark Slate Body
COLOR_TEXT_MUTED = colors.HexColor('#64748b')  # Muted Slate
COLOR_BORDER = colors.HexColor('#cbd5e1')      # Slate 300
COLOR_SIDEBAR_BG = colors.HexColor('#f1f5f9')  # Refined Slate 100
COLOR_TAG_BG = colors.HexColor('#e2e8f0')      # Slate 200
COLOR_CARD_BG = colors.HexColor('#f8fafc')     # Slate 50

def draw_canvas_decorations(canvas, doc):
    canvas.saveState()
    # 1. Top Header Banner
    canvas.setFillColor(COLOR_NAVY)
    canvas.rect(0, H - HEADER_HEIGHT, W, HEADER_HEIGHT, fill=1, stroke=0)
    
    # 2. Amber Accent Stripe
    canvas.setFillColor(COLOR_AMBER)
    canvas.rect(0, H - HEADER_HEIGHT - 2*mm, W, 2*mm, fill=1, stroke=0)
    
    # 3. Sidebar Background (Slate 100 with distinct contrast)
    sidebar_edge = SIDEBAR_WIDTH + 10*mm
    canvas.setFillColor(COLOR_SIDEBAR_BG)
    canvas.rect(0, 0, sidebar_edge, H - HEADER_HEIGHT - 2*mm, fill=1, stroke=0)
    
    # 4. Vertical Dividing Border
    canvas.setStrokeColor(COLOR_BORDER)
    canvas.setLineWidth(1)
    canvas.line(sidebar_edge, 0, sidebar_edge, H - HEADER_HEIGHT - 2*mm)
    
    canvas.restoreState()

def get_resume_styles():
    styles = getSampleStyleSheet()

    # Header Styles
    styles.add(ParagraphStyle(
        'HeaderName',
        fontName='ZenHei',
        fontSize=22,
        leading=26,
        textColor=colors.white,
        fontStyle='bold'
    ))
    styles.add(ParagraphStyle(
        'HeaderTitle',
        fontName='ZenHei',
        fontSize=10.5,
        leading=14,
        textColor=COLOR_AMBER_LIGHT,
        fontStyle='bold'
    ))
    styles.add(ParagraphStyle(
        'HeaderContact',
        fontName='ZenHei',
        fontSize=8.2,
        leading=12,
        textColor=colors.HexColor('#e2e8f0')
    ))

    # Sidebar Styles
    styles.add(ParagraphStyle(
        'SidebarSection',
        fontName='ZenHei',
        fontSize=9.5,
        leading=12.5,
        textColor=COLOR_NAVY,
        fontStyle='bold'
    ))
    styles.add(ParagraphStyle(
        'SidebarSubhead',
        fontName='ZenHei',
        fontSize=8.2,
        leading=11,
        textColor=COLOR_AMBER,
        fontStyle='bold',
        spaceBefore=4,
        spaceAfter=2
    ))
    styles.add(ParagraphStyle(
        'SidebarItem',
        fontName='ZenHei',
        fontSize=7.8,
        leading=11.5,
        textColor=COLOR_TEXT_MAIN
    ))

    # Main Body Styles
    styles.add(ParagraphStyle(
        'MainSectionTitle',
        fontName='ZenHei',
        fontSize=10.5,
        leading=14,
        textColor=COLOR_NAVY,
        fontStyle='bold'
    ))
    styles.add(ParagraphStyle(
        'SummaryText',
        fontName='ZenHei',
        fontSize=8.2,
        leading=12.2,
        textColor=COLOR_TEXT_MAIN
    ))
    styles.add(ParagraphStyle(
        'ProjectHeaderTitle',
        fontName='ZenHei',
        fontSize=9,
        leading=12,
        textColor=COLOR_NAVY,
        fontStyle='bold'
    ))
    styles.add(ParagraphStyle(
        'ProjectHeaderLink',
        fontName='ZenHei',
        fontSize=7.8,
        leading=11,
        textColor=COLOR_AMBER,
        alignment=2 # Right
    ))
    styles.add(ParagraphStyle(
        'ProjectTech',
        fontName='ZenHei',
        fontSize=7.6,
        leading=10,
        textColor=COLOR_TEXT_MUTED
    ))
    styles.add(ParagraphStyle(
        'ProjectBullet',
        fontName='ZenHei',
        fontSize=7.8,
        leading=11,
        textColor=COLOR_TEXT_MAIN,
        leftIndent=8,
        firstLineIndent=-8
    ))

    return styles

def create_section_header(title, styles, width=124*mm):
    # Sleek section header with colored left bar
    t = Table([
        [Paragraph(f"<b>{title}</b>", styles['MainSectionTitle'])]
    ], colWidths=[width])
    t.setStyle(TableStyle([
        ('LINEBEFORE', (0,0), (0,0), 3, COLOR_AMBER),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t

def create_sidebar_header(title, styles, width=54*mm):
    t = Table([
        [Paragraph(f"<b>{title}</b>", styles['SidebarSection'])]
    ], colWidths=[width])
    t.setStyle(TableStyle([
        ('LINEBEFORE', (0,0), (0,0), 2.5, COLOR_NAVY),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    return t

def build_en_page(styles):
    # Header Flowable Table
    header_data = [
        [
            Paragraph("LIM JUN HUI", styles['HeaderName']),
            Paragraph("Email: <a href='mailto:junhui.lim@gmail.com' color='#fbbf24'>junhui.lim@gmail.com</a>", styles['HeaderContact'])
        ],
        [
            Paragraph("FULL-STACK SOFTWARE ENGINEER", styles['HeaderTitle']),
            Paragraph("Portfolio: <a href='https://putolim0226.github.io/my-portfolio/en' color='#fbbf24'>putolim0226.github.io/my-portfolio/en</a>", styles['HeaderContact'])
        ],
        [
            Paragraph("", styles['HeaderTitle']),
            Paragraph("GitHub: <a href='https://github.com/PutoLim0226' color='#fbbf24'>github.com/PutoLim0226</a>", styles['HeaderContact'])
        ]
    ]
    header_table = Table(header_data, colWidths=[105*mm, 85*mm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ]))

    # --- Left Column: Skills & Profile ---
    left_flow = []
    
    left_flow.append(create_sidebar_header("TECHNICAL STACK", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    
    left_flow.append(Paragraph("FRONTEND", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• React 19 / JSX Architecture", styles['SidebarItem']))
    left_flow.append(Paragraph("• Modern JavaScript (ES6+)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Vite / Asset Bundling", styles['SidebarItem']))
    left_flow.append(Paragraph("• HTML5, CSS3, SCSS (BEM)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Responsive Web Design (RWD)", styles['SidebarItem']))
    left_flow.append(Paragraph("• i18n Internationalization", styles['SidebarItem']))
    
    left_flow.append(Paragraph("BACKEND & API", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• PHP 8.3 (OOP, RESTful API)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Python (Scripting & Automation)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Go (High-Performance Services)", styles['SidebarItem']))
    left_flow.append(Paragraph("• PHP-FPM Configuration", styles['SidebarItem']))
    
    left_flow.append(Paragraph("DATABASE & CACHING", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• MySQL (Schema Design, Indexing)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Redis (In-Memory Cache, Sessions)", styles['SidebarItem']))
    
    left_flow.append(Paragraph("DEVOPS & SYSTEM", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• Linux / Ubuntu Server Admin", styles['SidebarItem']))
    left_flow.append(Paragraph("• Nginx (Reverse Proxy, SSL, Gzip)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Git / GitHub Actions CI/CD", styles['SidebarItem']))
    left_flow.append(Paragraph("• UFW Firewall Security", styles['SidebarItem']))

    left_flow.append(Spacer(1, 3*mm))
    left_flow.append(create_sidebar_header("CORE METHODOLOGIES", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    left_flow.append(Paragraph("• Clean Architecture & SOLID", styles['SidebarItem']))
    left_flow.append(Paragraph("• High-Throughput Caching", styles['SidebarItem']))
    left_flow.append(Paragraph("• Database Query Optimization", styles['SidebarItem']))
    left_flow.append(Paragraph("• Automated Deployment CI/CD", styles['SidebarItem']))
    left_flow.append(Paragraph("• Component-Driven Frontend", styles['SidebarItem']))

    left_flow.append(Spacer(1, 3*mm))
    left_flow.append(create_sidebar_header("LANGUAGES", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    left_flow.append(Paragraph("• English (Full Professional)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Chinese (Native / Bilingual)", styles['SidebarItem']))

    # --- Right Column: Projects & Summary ---
    right_flow = []
    
    right_flow.append(create_section_header("PROFESSIONAL SUMMARY", styles))
    right_flow.append(Spacer(1, 2*mm))
    summary = (
        "Performance-driven Full-Stack Engineer with comprehensive experience in architecting, "
        "developing, and deploying modern web applications from database schemas to responsive interfaces. "
        "Expert in building modular React frontends, robust PHP RESTful APIs, high-throughput Redis caching layers, "
        "and managing production Linux environments with Nginx. Passionate about clean architecture, system speed, "
        "and reliable end-to-end delivery."
    )
    right_flow.append(Paragraph(summary, styles['SummaryText']))
    right_flow.append(Spacer(1, 4*mm))

    right_flow.append(create_section_header("KEY ENGINEERING PROJECTS", styles))
    right_flow.append(Spacer(1, 2*mm))

    projects = [
        {
            "title": "Vintage E-Commerce Platform",
            "link": "Live Demo: http://45.32.25.8:8090/",
            "url": "http://45.32.25.8:8090/",
            "tech": "PHP 8.3 RESTful API | MySQL | Redis | React | Nginx",
            "bullets": [
                "Engineered custom object-oriented PHP backend serving secure, stateless RESTful endpoints.",
                "Implemented Redis in-memory caching to eliminate redundant MySQL queries and accelerate read latency.",
                "Delivered dynamic React shopping cart and catalog, fully deployed on Ubuntu with Nginx reverse proxy."
            ]
        },
        {
            "title": "Case Profile Management System",
            "link": "Live Demo: caseprofile2.asia.edu.tw",
            "url": "https://caseprofile2.asia.edu.tw/",
            "tech": "React | Dynamic Data Visualization | RESTful Integration",
            "bullets": [
                "Constructed an academic research and case study management system with dynamic data charts.",
                "Built responsive, modular data tables and search filters for swift access to complex academic archives."
            ]
        },
        {
            "title": "Hui Yin Seh Community Portal",
            "link": "Live Demo: http://45.32.25.8:8080/",
            "url": "http://45.32.25.8:8080/",
            "tech": "React | PHP API | MySQL | Linux Server Administration",
            "bullets": [
                "Delivered comprehensive community portal for a Malaysian non-profit, supporting events and member data.",
                "Configured relational MySQL schema, backend CRUD endpoints, and secure server hosting environment."
            ]
        },
        {
            "title": "Aurora Coffee Online Experience",
            "link": "Live Demo: putolim0226.github.io/aurora-coffee",
            "url": "https://putolim0226.github.io/aurora-coffee/",
            "tech": "React | SCSS Animations | Touch-First Responsive UX",
            "bullets": [
                "Crafted an interactive brand storefront with fluid neon animations and customizable digital menus.",
                "Ensured zero-jank 60fps responsive interactions across mobile, tablet, and desktop viewports."
            ]
        },
        {
            "title": "YHD Corporate Portal & Play YHD",
            "link": "Live Demos: yhd.tw | play.yhd.tw",
            "url": "https://yhd.tw/",
            "tech": "Modern Frontend Architecture | UI/UX Systems | Community Platform",
            "bullets": [
                "Built digital transformation corporate landing pages and interactive neon-themed gaming community portal."
            ]
        }
    ]

    for p in projects:
        p_row = [
            Paragraph(f"<b>{p['title']}</b>", styles['ProjectHeaderTitle']),
            Paragraph(f"<a href='{p['url']}' color='#d97706'><u>{p['link']}</u></a>", styles['ProjectHeaderLink'])
        ]
        p_table = Table([p_row], colWidths=[70*mm, 54*mm])
        p_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        right_flow.append(p_table)
        right_flow.append(Paragraph(f"<b>Stack:</b> {p['tech']}", styles['ProjectTech']))
        for b in p['bullets']:
            right_flow.append(Paragraph(f"▸ {b}", styles['ProjectBullet']))
        right_flow.append(Spacer(1, 2*mm))

    # Two-column layout table
    body_table = Table([[left_flow, right_flow]], colWidths=[58*mm, 126*mm])
    body_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (0,0), 0),
        ('RIGHTPADDING', (0,0), (0,0), 5*mm),
        ('LEFTPADDING', (1,0), (1,0), 5*mm),
        ('RIGHTPADDING', (1,0), (1,0), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    return [
        header_table,
        Spacer(1, 9*mm),
        body_table
    ]

def build_zh_page(styles):
    # Header Flowable Table (純中文，不參雜英文姓名)
    header_data = [
        [
            Paragraph("林俊匯", styles['HeaderName']),
            Paragraph("電子信箱: <a href='mailto:junhui.lim@gmail.com' color='#fbbf24'>junhui.lim@gmail.com</a>", styles['HeaderContact'])
        ],
        [
            Paragraph("全端軟體工程師", styles['HeaderTitle']),
            Paragraph("作品集: <a href='https://putolim0226.github.io/my-portfolio/zh_cn' color='#fbbf24'>putolim0226.github.io/my-portfolio/zh_cn</a>", styles['HeaderContact'])
        ],
        [
            Paragraph("", styles['HeaderTitle']),
            Paragraph("GitHub: <a href='https://github.com/PutoLim0226' color='#fbbf24'>github.com/PutoLim0226</a>", styles['HeaderContact'])
        ]
    ]
    header_table = Table(header_data, colWidths=[105*mm, 85*mm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ]))

    # --- 左側欄：技術棧與核心專長 ---
    left_flow = []
    
    left_flow.append(create_sidebar_header("專業核心技術", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    
    left_flow.append(Paragraph("前端工程", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• React 19 元件架構與狀態管理", styles['SidebarItem']))
    left_flow.append(Paragraph("• 現代 JavaScript (ES6+ 核心語法)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Vite 現代化高效率建置工具", styles['SidebarItem']))
    left_flow.append(Paragraph("• HTML5 / SCSS 模組化切版", styles['SidebarItem']))
    left_flow.append(Paragraph("• RWD 跨裝置響應式設計", styles['SidebarItem']))
    left_flow.append(Paragraph("• i18n 多國語系動態路由整合", styles['SidebarItem']))
    
    left_flow.append(Paragraph("後端服務與開發", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• PHP 8.3 (物件導向 / RESTful API)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Python (自動化腳本與工具開發)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Go (高效後端服務)", styles['SidebarItem']))
    left_flow.append(Paragraph("• PHP-FPM 效能調優", styles['SidebarItem']))
    
    left_flow.append(Paragraph("資料庫與快取", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• MySQL (關聯設計、索引優化)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Redis (高速快取、Session 管理)", styles['SidebarItem']))
    
    left_flow.append(Paragraph("維運與自動化部署", styles['SidebarSubhead']))
    left_flow.append(Paragraph("• Linux / Ubuntu 伺服器完整維運", styles['SidebarItem']))
    left_flow.append(Paragraph("• Nginx (反向代理、SSL 憑證配置)", styles['SidebarItem']))
    left_flow.append(Paragraph("• Git / GitHub Actions 自動化 CI/CD", styles['SidebarItem']))
    left_flow.append(Paragraph("• UFW 防火牆安全防護與通訊埠管理", styles['SidebarItem']))

    left_flow.append(Spacer(1, 3*mm))
    left_flow.append(create_sidebar_header("工程核心優勢", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    left_flow.append(Paragraph("• 獨立全端架構整合能力", styles['SidebarItem']))
    left_flow.append(Paragraph("• 系統效能優化與快取策略", styles['SidebarItem']))
    left_flow.append(Paragraph("• 關聯資料庫高效率查詢設計", styles['SidebarItem']))
    left_flow.append(Paragraph("• 自動化 CI/CD 持續交付", styles['SidebarItem']))
    left_flow.append(Paragraph("• 高度整潔可維護之程式碼風格", styles['SidebarItem']))

    left_flow.append(Spacer(1, 3*mm))
    left_flow.append(create_sidebar_header("語言能力", styles))
    left_flow.append(Spacer(1, 1.5*mm))
    left_flow.append(Paragraph("• 中文 (母語，流暢表達與撰寫)", styles['SidebarItem']))
    left_flow.append(Paragraph("• 英文 (具備專業技術溝通能力)", styles['SidebarItem']))

    # --- 右側主要內容：專業摘要與專案成果 ---
    right_flow = []
    
    right_flow.append(create_section_header("個人專業簡介", styles))
    right_flow.append(Spacer(1, 2*mm))
    summary = (
        "具備高度實戰經驗的全端軟體工程師，專注於構建高吞吐量、低延遲且具擴展性的現代化網頁應用程式。"
        "精通前端 React 元件化開發、後端 PHP 8 物件導向 RESTful API 服務架構、MySQL 關聯資料庫與 Redis 內存快取優化，"
        "並具備 Linux (Ubuntu) 伺服器管理、Nginx 反向代理配置及 GitHub Actions 自動化 CI/CD 流程落地能力。"
        "善於將複雜的商業邏輯化繁為簡，交付穩定可靠且易於維護的高品質工程產出。"
    )
    right_flow.append(Paragraph(summary, styles['SummaryText']))
    right_flow.append(Spacer(1, 4*mm))

    right_flow.append(create_section_header("精選專案成果", styles))
    right_flow.append(Spacer(1, 2*mm))

    projects = [
        {
            "title": "復古刻痕電商平台",
            "link": "線上展示: 45.32.25.8:8090",
            "url": "http://45.32.25.8:8090/",
            "tech": "PHP 8.3 RESTful API | MySQL | Redis | React | Nginx",
            "bullets": [
                "獨立設計物件導向 PHP 後端 API，提供完整商品檢索、分類篩選與購物車持久化機制。",
                "導入 Redis 內存快取層，有效避免熱門商品重複查詢資料庫，大幅降低延遲並提升讀取效能。",
                "完成前後端分離架構，於 Ubuntu 伺服器部署 Nginx 反向代理與 PHP-FPM 正式環境運行。"
            ]
        },
        {
            "title": "個案研究與學術檔案管理系統",
            "link": "線上展示: 亞洲大學個案系統",
            "url": "https://caseprofile2.asia.edu.tw/",
            "tech": "React | 動態資料視覺化 | REST API 串接整合",
            "bullets": [
                "為學術機構開發個人研究檔案與教學個案資料管理系統，整合多維度互動式圖表儀表板。",
                "建立高效模組化之操作介面，支援研究檔案多欄位即時篩選、檔案匯總與權限劃分。"
            ]
        },
        {
            "title": "馬來西亞慧音社慈善入口網",
            "link": "線上展示: 45.32.25.8:8080",
            "url": "http://45.32.25.8:8080/",
            "tech": "React | PHP API | MySQL 資料庫 | Ubuntu 伺服器",
            "bullets": [
                "為馬來西亞非營利慈善社團打造官方資訊入口，支援志工活動發布與社群會務管理功能。",
                "規劃資料庫關聯模型與後端 CRUD 介面，並完成獨立 Linux 雲端主機之部署維運。"
            ]
        },
        {
            "title": "極光咖啡品牌線上體驗館",
            "link": "線上展示: 極光咖啡作品",
            "url": "https://putolim0226.github.io/aurora-coffee/",
            "tech": "React | SCSS 動畫效果 | 移動端優先響應式體驗",
            "bullets": [
                "打造具沉浸感的高質感暗色發光咖啡品牌電商展示站，實現流暢的菜單篩選與卡片過渡動效。",
                "針對手機、平板與桌面等多種螢幕尺寸進行嚴格斷點適配，達成 60fps 流暢渲染。"
            ]
        },
        {
            "title": "YHD 企業數位轉型官網與遊戲社群平台",
            "link": "線上展示: yhd.tw | play.yhd.tw",
            "url": "https://yhd.tw/",
            "tech": "現代前端架構 | UI/UX 系統規範 | 遊戲入口網站",
            "bullets": [
                "規劃並實現現代數位轉型企業登陸首頁，以及具備未來感霓虹視覺風格之互動遊戲社群入口。"
            ]
        }
    ]

    for p in projects:
        p_row = [
            Paragraph(f"<b>{p['title']}</b>", styles['ProjectHeaderTitle']),
            Paragraph(f"<a href='{p['url']}' color='#d97706'><u>{p['link']}</u></a>", styles['ProjectHeaderLink'])
        ]
        p_table = Table([p_row], colWidths=[70*mm, 54*mm])
        p_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        right_flow.append(p_table)
        right_flow.append(Paragraph(f"<b>使用技術:</b> {p['tech']}", styles['ProjectTech']))
        for b in p['bullets']:
            right_flow.append(Paragraph(f"▸ {b}", styles['ProjectBullet']))
        right_flow.append(Spacer(1, 2*mm))

    # 左右欄雙欄版型表格
    body_table = Table([[left_flow, right_flow]], colWidths=[58*mm, 126*mm])
    body_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (0,0), 0),
        ('RIGHTPADDING', (0,0), (0,0), 5*mm),
        ('LEFTPADDING', (1,0), (1,0), 5*mm),
        ('RIGHTPADDING', (1,0), (1,0), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))

    return [
        header_table,
        Spacer(1, 9*mm),
        body_table
    ]

def generate():
    styles = get_resume_styles()
    os.makedirs('public', exist_ok=True)
    
    margin_lr = 12 * mm
    top_margin = 8 * mm
    bottom_margin = 8 * mm

    # 1. Pure English Resume (Single Page A4)
    doc_en = SimpleDocTemplate(
        "public/resume_en.pdf",
        pagesize=A4,
        leftMargin=margin_lr, rightMargin=margin_lr,
        topMargin=top_margin, bottomMargin=bottom_margin
    )
    doc_en.build(build_en_page(styles), onFirstPage=draw_canvas_decorations)
    print("Generated public/resume_en.pdf (100% English)")

    # 2. Pure Chinese Resume (Single Page A4)
    doc_zh = SimpleDocTemplate(
        "public/resume_zh.pdf",
        pagesize=A4,
        leftMargin=margin_lr, rightMargin=margin_lr,
        topMargin=top_margin, bottomMargin=bottom_margin
    )
    doc_zh.build(build_zh_page(styles), onFirstPage=draw_canvas_decorations)
    print("Generated public/resume_zh.pdf (100% Chinese)")

    # 3. Bilingual Combined Resume (Page 1: Pure EN, Page 2: Pure ZH)
    doc_combined = SimpleDocTemplate(
        "public/resume.pdf",
        pagesize=A4,
        leftMargin=margin_lr, rightMargin=margin_lr,
        topMargin=top_margin, bottomMargin=bottom_margin
    )
    combined_flow = build_en_page(styles) + [PageBreak()] + build_zh_page(styles)
    doc_combined.build(combined_flow, onFirstPage=draw_canvas_decorations, onLaterPages=draw_canvas_decorations)
    print("Generated public/resume.pdf (Bilingual: P1 EN, P2 ZH)")

if __name__ == '__main__':
    generate()
