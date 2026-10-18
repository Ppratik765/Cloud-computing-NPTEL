import json
import re
import os
import sys

# Add quiz_data to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'quiz_data'))

import week01
import week02
import week03
import week04
import week05
import week06
import week07
import week08
import week09
import week10
import week11
import week12

WEEK_MODULES = [
    (1, week01, "Week 1: Introduction to Cloud & Virtualization", 
     "NIST Essential Characteristics, Service & Deployment Models, Hardware Virtualization Basics"),
    (2, week02, "Week 2: Cloud Architecture & Cloud Storage", 
     "Hypervisor Architecture (Type 1 & 2), Full vs Para-Virtualization, Hardware Assist VT-x, OpenStack Swift & Amazon S3"),
    (3, week03, "Week 3: Virtualization Deep Dive & Memory Management", 
     "Popek-Goldberg Theorem, Shadow Page Tables, Intel EPT & AMD NPT, Memory Ballooning, Transparent Page Sharing (TPS)"),
    (4, week04, "Week 4: Cloud Platforms (OpenStack, Azure, GCP)", 
     "Meghamala IIT KGP Architecture, OpenStack Horizon & Core Modules, Azure Hyperscale SQL, GCP Andromeda & Spanner TrueTime"),
    (5, week05, "Week 5: SLA Management & Cloud Economics", 
     "Formal SLA Availability Models, Service Credit Penalties, Buy vs Lease ($U < P/A$), HDFS Input Splits, PUE Energy"),
    (6, week06, "Week 6: Cloud Security & Threat Modeling", 
     "CIA Triad, Structural Attack Models, Cross-VM Prime+Probe Cache Side Channels, Gartner 7 Cloud Risks, SAML vs OAuth"),
    (7, week07, "Week 7: Mobile Cloud Computing & Geospatial Cloud", 
     "Kumar & Lu Energy Offloading Condition, Cloudlets & Dynamic VM Synthesis, OGC Web Services (WMS, WFS, WCS, WPS)"),
    (8, week08, "Week 8: Containers, Docker & Sensor-Cloud", 
     "Containers vs VMs, OverlayFS Copy-on-Write, Dockerfile Directives, Kubernetes etcd, Sensor-Cloud Virtual Sensors"),
    (9, week09, "Week 9: Edge-Fog Computing & Cloud Federation", 
     "3-Tier Edge-Fog-Cloud Hierarchy, iFogSim Empirical Analysis, Vertical vs Horizontal Scalability, Cloud Federation Brokers"),
    (10, week10, "Week 10: VM Migration & Container Primitives", 
     "Pre-Copy Push vs Post-Copy Pull Live Migration, Convergence Criteria ($D < R$), Linux Namespaces vs cgroups, Docker Volumes"),
    (11, week11, "Week 11: Dew Computing, Serverless FaaS & Sustainable Cloud", 
     "Dew Computing 6 Service Models (SiD, DbID, WiD), Serverless FaaS Scale-to-Zero, Cold Start Mitigation, CDC Energy Breakdown & PUE/DCiE"),
    (12, week12, "Week 12: 5G Era, Cyber-Physical Systems, Spatial Cloud & IoHT", 
     "5G Pillars (eMBB, URLLC, mMTC), MEC vs MCC, NIST CPCC Architecture, Traj-Cloud Map-Matching, 4-Tier IoHT & iFogSim Empirical Parameters")
]

def format_math_and_text(text):
    """Formats LaTeX math expressions and code formatting into beautiful offline HTML."""
    if not text:
        return ""
    
    def math_replacer(match):
        expr = match.group(1)
        
        # Fractions \frac{a}{b}
        expr = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', 
                      r'<span class="frac"><span class="num">\1</span><span class="den">\2</span></span>', expr)
        
        # \text{...}
        expr = re.sub(r'\\text\{([^}]+)\}', r'<span class="math-txt">\1</span>', expr)
        
        # Math symbols
        replacements = [
            (r'\Delta', '&Delta;'),
            (r'\approx', '&approx;'),
            (r'\times', '&times;'),
            (r'\cdot', '&middot;'),
            (r'\subseteq', '&sube;'),
            (r'\langle', '&lang;'),
            (r'\rangle', '&rang;'),
            (r'\le', '&le;'),
            (r'\ge', '&ge;'),
            (r'\ll', '&Lt;'),
            (r'\gg', '&Gt;'),
            (r'\to', '&rarr;'),
            (r'\rightarrow', '&rarr;'),
            (r'\leftarrow', '&larr;'),
            (r'\infty', '&infin;'),
            (r'\in', '&isin;'),
            (r'\notin', '&notin;'),
            (r'\cup', '&cup;'),
            (r'\cap', '&cap;'),
            (r'\pm', '&plusmn;'),
            (r'\neq', '&ne;'),
            (r'\sum', '&sum;'),
            (r'\prod', '&prod;'),
            (r'\mathcal{S}', 'S'),
            (r'\mathcal{C}', 'C'),
            (r'\mathcal{M}', 'M'),
            (r'\mathcal{D}', 'D'),
            (r'\mathcal{N}', 'N'),
            (r'\mathcal{I}', 'I'),
            (r'\dots', '...'),
            (r'\cdots', '...')
        ]
        for k, v in replacements:
            expr = expr.replace(k, v)
        
        # Superscript & subscript
        expr = re.sub(r'\^\{([^}]+)\}', r'<sup>\1</sup>', expr)
        expr = re.sub(r'\^([0-9a-zA-Z]+)', r'<sup>\1</sup>', expr)
        expr = re.sub(r'_\{([^}]+)\}', r'<sub>\1</sub>', expr)
        expr = re.sub(r'_([0-9a-zA-Z]+)', r'<sub>\1</sub>', expr)
        
        return f'<span class="math-inline">{expr}</span>'

    formatted = re.sub(r'\$([^$]+)\$', math_replacer, text)
    return formatted

def build_quiz_page(week_num, week_mod, week_title, week_desc):
    raw_questions = week_mod.questions
    
    formatted_questions = []
    for q in raw_questions:
        fq = dict(q)
        fq['question_html'] = format_math_and_text(q['question'])
        fq['options_html'] = [format_math_and_text(opt) for opt in q['options']]
        fq['explanation_html'] = format_math_and_text(q['explanation'])
        formatted_questions.append(fq)
    
    questions_json = json.dumps(formatted_questions, ensure_ascii=False)
    
    prev_week_file = f"quiz_week{week_num-1:02d}.html" if week_num > 1 else "index.html"
    next_week_file = f"quiz_week{week_num+1:02d}.html" if week_num < 12 else "index.html"
    
    prev_label = f"&larr; Week {week_num-1}" if week_num > 1 else "&larr; All Weeks Hub"
    next_label = f"Week {week_num+1} &rarr;" if week_num < 12 else "Back to Hub &rarr;"

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>{week_title} — 30 NPTEL Exam Questions</title>
  <style>
    /* ==========================================================================
       MODERN OFFLINE DESIGN TOKENS
       ========================================================================== */
    :root {{
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      --font-math: "Cambria Math", "Latin Modern Math", "STIX Two Math", "Times New Roman", serif;
      
      /* Dark Theme Tokens (Default) */
      --bg-body: #0b0f19;
      --bg-surface: #111827;
      --bg-surface-elevated: #1e293b;
      --bg-card: #151e2e;
      --bg-card-hover: #1c283f;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-medium: rgba(255, 255, 255, 0.16);
      --border-focus: #38bdf8;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --primary: #38bdf8;
      --primary-rgb: 56, 189, 248;
      --primary-hover: #0ea5e9;
      
      --accent: #6366f1;
      --accent-rgb: 99, 102, 241;
      
      --success: #10b981;
      --success-rgb: 16, 185, 129;
      --success-bg: rgba(16, 185, 129, 0.12);
      --success-border: #059669;
      
      --danger: #ef4444;
      --danger-rgb: 239, 68, 68;
      --danger-bg: rgba(239, 68, 68, 0.14);
      --danger-border: #dc2626;
      
      --warning: #f59e0b;
      --warning-bg: rgba(245, 158, 11, 0.12);
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      
      --transition: 200ms cubic-bezier(0.4, 0, 0.2, 1);
    }}

    [data-theme="light"] {{
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-surface-elevated: #f1f5f9;
      --bg-card: #ffffff;
      --bg-card-hover: #f8fafc;
      --border-subtle: #e2e8f0;
      --border-medium: #cbd5e1;
      --border-focus: #0284c7;
      
      --text-main: #0f172a;
      --text-muted: #475569;
      --text-dim: #94a3b8;
      
      --primary: #0284c7;
      --primary-rgb: 2, 132, 199;
      --primary-hover: #0369a1;
      
      --accent: #4f46e5;
      --accent-rgb: 79, 70, 229;
      
      --success: #059669;
      --success-rgb: 5, 150, 105;
      --success-bg: rgba(5, 150, 105, 0.1);
      --success-border: #10b981;
      
      --danger: #dc2626;
      --danger-rgb: 220, 38, 38;
      --danger-bg: rgba(220, 38, 38, 0.08);
      --danger-border: #ef4444;
      
      --warning: #d97706;
      --warning-bg: rgba(217, 119, 6, 0.1);
      
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
      transition: background-color var(--transition), color var(--transition);
    }}

    /* Typography & Offline Math */
    code {{
      font-family: var(--font-mono);
      font-size: 0.9em;
      background: rgba(var(--primary-rgb), 0.12);
      color: var(--primary);
      padding: 0.15em 0.4em;
      border-radius: var(--radius-sm);
    }}

    .math-inline {{
      font-family: var(--font-math);
      font-style: italic;
      padding: 0 0.15em;
      color: var(--text-main);
    }}
    .math-txt {{
      font-family: var(--font-sans);
      font-style: normal;
      font-size: 0.95em;
    }}
    .frac {{
      display: inline-flex;
      flex-direction: column;
      vertical-align: middle;
      text-align: center;
      padding: 0 0.2em;
      font-size: 0.9em;
      line-height: 1;
    }}
    .frac .num {{
      border-bottom: 1px solid currentColor;
      padding-bottom: 1px;
    }}
    .frac .den {{
      padding-top: 1px;
    }}

    /* Top Sticky Header */
    .app-header {{
      position: sticky;
      top: 0;
      z-index: 50;
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      backdrop-filter: blur(8px);
    }}

    .header-content {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }}

    .header-left {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .hub-link {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.85rem;
      font-weight: 600;
      padding: 0.4rem 0.65rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
      transition: all var(--transition);
      white-space: nowrap;
    }}
    .hub-link:hover {{
      color: var(--primary);
      border-color: var(--primary);
      background: rgba(var(--primary-rgb), 0.08);
    }}

    .week-badge-header {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .q-counter-pill {{
      font-size: 0.75rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: var(--radius-full);
      background: rgba(var(--accent-rgb), 0.15);
      color: #a5b4fc;
      border: 1px solid rgba(var(--accent-rgb), 0.3);
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .score-pill {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-full);
      background: rgba(var(--success-rgb), 0.12);
      border: 1px solid rgba(var(--success-rgb), 0.3);
      color: var(--success);
      font-size: 0.82rem;
      font-weight: 700;
      white-space: nowrap;
    }}

    .icon-btn {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      width: 38px;
      height: 38px;
      border-radius: var(--radius-md);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all var(--transition);
      flex-shrink: 0;
    }}
    .icon-btn:hover {{
      color: var(--text-main);
      border-color: var(--border-medium);
      background: var(--bg-card-hover);
    }}

    /* Main Layout */
    .main-container {{
      max-width: 900px;
      margin: 1.5rem auto;
      padding: 0 1rem;
      width: 100%;
      flex: 1;
    }}

    /* View Controls Bar */
    .controls-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
      flex-wrap: wrap;
    }}

    .view-toggle-group {{
      display: inline-flex;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 3px;
    }}
    .toggle-opt-btn {{
      background: transparent;
      border: none;
      padding: 0.4rem 0.85rem;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--text-muted);
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: all var(--transition);
    }}
    .toggle-opt-btn.active {{
      background: var(--primary);
      color: #0b0f19;
      font-weight: 700;
    }}

    .nav-drawer-trigger {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.85rem;
      font-size: 0.82rem;
      font-weight: 600;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: all var(--transition);
    }}
    .nav-drawer-trigger:hover {{
      border-color: var(--primary);
      color: var(--primary);
    }}

    /* Progress Bar */
    .progress-track {{
      width: 100%;
      height: 6px;
      background: var(--bg-surface-elevated);
      border-radius: var(--radius-full);
      overflow: hidden;
      margin-bottom: 1.5rem;
    }}
    .progress-fill {{
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      transition: width 300ms ease;
    }}

    /* Question Card Styling */
    .question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      box-shadow: var(--shadow-md);
      margin-bottom: 1.75rem;
      transition: border-color var(--transition);
    }}

    .q-meta-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }}
    .q-tags {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.25rem;
      padding: 0.25rem 0.55rem;
      font-size: 0.72rem;
      font-weight: 700;
      border-radius: var(--radius-sm);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .badge-qnum {{
      background: var(--bg-surface-elevated);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
    }}
    .badge-mcq {{
      background: rgba(var(--primary-rgb), 0.15);
      color: var(--primary);
      border: 1px solid rgba(var(--primary-rgb), 0.3);
    }}
    .badge-msq {{
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border: 1px solid rgba(245, 158, 11, 0.3);
    }}

    .flag-btn {{
      background: none;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.78rem;
      font-weight: 600;
      padding: 0.3rem 0.5rem;
      border-radius: var(--radius-sm);
      transition: color var(--transition);
    }}
    .flag-btn:hover {{
      color: var(--warning);
    }}
    .flag-btn.flagged {{
      color: var(--warning);
    }}

    .q-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.75rem;
    }}

    .q-prompt {{
      font-size: 1.02rem;
      line-height: 1.7;
      color: var(--text-main);
      margin-bottom: 1.5rem;
    }}

    .msq-hint {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 0.9rem;
      background: var(--warning-bg);
      border-left: 3px solid var(--warning);
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      color: #fbbf24;
      margin-bottom: 1.25rem;
    }}

    /* Options List */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin-bottom: 1.5rem;
    }}

    .option-btn {{
      background: var(--bg-surface);
      border: 1.5px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1rem 1.15rem;
      min-height: 54px;
      display: flex;
      align-items: flex-start;
      gap: 0.9rem;
      cursor: pointer;
      text-align: left;
      font-family: inherit;
      color: var(--text-main);
      font-size: 0.98rem;
      line-height: 1.55;
      width: 100%;
      transition: all var(--transition);
      position: relative;
      user-select: none;
      -webkit-tap-highlight-color: transparent;
    }}
    .option-btn:hover:not(.locked) {{
      border-color: var(--border-medium);
      background: var(--bg-card-hover);
      transform: translateY(-1px);
    }}
    .option-btn:focus-visible {{
      outline: 2px solid var(--border-focus);
      outline-offset: 2px;
    }}

    .opt-letter {{
      width: 26px;
      height: 26px;
      border-radius: var(--radius-full);
      border: 1.5px solid var(--border-medium);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--text-muted);
      flex-shrink: 0;
      margin-top: 1px;
      transition: all var(--transition);
    }}
    .opt-btn-msq .opt-letter {{
      border-radius: var(--radius-sm);
    }}

    .opt-text {{
      flex: 1;
    }}

    /* Instant Feedback Visual States */
    .option-btn.state-chosen-correct {{
      border-color: var(--success) !important;
      background: var(--success-bg) !important;
    }}
    .option-btn.state-chosen-correct .opt-letter {{
      border-color: var(--success) !important;
      background: var(--success) !important;
      color: #0b0f19 !important;
    }}

    .option-btn.state-chosen-incorrect {{
      border-color: var(--danger) !important;
      background: var(--danger-bg) !important;
    }}
    .option-btn.state-chosen-incorrect .opt-letter {{
      border-color: var(--danger) !important;
      background: var(--danger) !important;
      color: #ffffff !important;
    }}

    .option-btn.state-target-correct {{
      border-color: var(--success) !important;
      border-style: solid !important;
      background: rgba(var(--success-rgb), 0.08) !important;
    }}
    .option-btn.state-target-correct .opt-letter {{
      border-color: var(--success) !important;
      color: var(--success) !important;
      font-weight: 800;
    }}

    .option-btn.state-msq-selected {{
      border-color: var(--primary);
      background: rgba(var(--primary-rgb), 0.1);
    }}
    .option-btn.state-msq-selected .opt-letter {{
      border-color: var(--primary);
      background: var(--primary);
      color: #0b0f19;
    }}

    .option-btn.locked {{
      cursor: default;
    }}

    /* MSQ Submit Button */
    .msq-submit-btn {{
      background: var(--primary);
      color: #0b0f19;
      border: none;
      padding: 0.75rem 1.5rem;
      font-size: 0.95rem;
      font-weight: 700;
      border-radius: var(--radius-md);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all var(--transition);
      margin-bottom: 1.25rem;
      min-height: 48px;
    }}
    .msq-submit-btn:hover {{
      background: var(--primary-hover);
      transform: translateY(-1px);
    }}
    .msq-submit-btn:disabled {{
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
    }}

    /* Instant Feedback & Explanation Container */
    .feedback-panel {{
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-top: 1.25rem;
      animation: fadeInSlide 250ms ease forwards;
    }}
    @keyframes fadeInSlide {{
      from {{ opacity: 0; transform: translateY(8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .feedback-panel.status-correct {{
      background: var(--success-bg);
      border: 1.5px solid var(--success-border);
    }}
    .feedback-panel.status-incorrect {{
      background: var(--danger-bg);
      border: 1.5px solid var(--danger-border);
    }}

    .fb-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
      margin-bottom: 0.75rem;
      flex-wrap: wrap;
    }}
    .fb-status-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-weight: 800;
      font-size: 0.95rem;
    }}
    .feedback-panel.status-correct .fb-status-tag {{
      color: var(--success);
    }}
    .feedback-panel.status-incorrect .fb-status-tag {{
      color: var(--danger);
    }}

    .fb-ans-callout {{
      font-size: 0.85rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-sm);
      background: var(--bg-surface);
      color: var(--text-main);
      border: 1px solid var(--border-subtle);
    }}

    .fb-explanation-body {{
      font-size: 0.94rem;
      line-height: 1.65;
      color: var(--text-main);
      border-top: 1px solid rgba(255, 255, 255, 0.08);
      padding-top: 0.75rem;
    }}
    [data-theme="light"] .fb-explanation-body {{
      border-top: 1px solid rgba(0, 0, 0, 0.08);
    }}

    /* Single Question Card Navigation Footer */
    .card-nav-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
      margin-top: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid var(--border-subtle);
    }}

    .nav-action-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 0.75rem 1.25rem;
      min-height: 48px;
      border-radius: var(--radius-md);
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all var(--transition);
      user-select: none;
    }}
    .nav-action-btn:hover:not(:disabled) {{
      border-color: var(--border-medium);
      background: var(--bg-card-hover);
    }}
    .nav-action-btn:disabled {{
      opacity: 0.4;
      cursor: not-allowed;
    }}

    .nav-action-btn.btn-next-highlight {{
      background: var(--primary);
      color: #0b0f19;
      border-color: var(--primary);
      font-weight: 700;
    }}
    .nav-action-btn.btn-next-highlight:hover {{
      background: var(--primary-hover);
    }}

    /* Navigator Modal / Drawer */
    .nav-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(4px);
      z-index: 100;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }}
    .nav-modal-backdrop.open {{
      display: flex;
    }}

    .nav-modal {{
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-lg);
      max-width: 600px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 1.5rem;
      box-shadow: var(--shadow-lg);
    }}

    .modal-head {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.25rem;
    }}
    .modal-head h3 {{
      font-size: 1.2rem;
      font-weight: 700;
    }}

    .matrix-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 0.6rem;
      margin-bottom: 1.5rem;
    }}
    @media (max-width: 480px) {{
      .matrix-grid {{
        grid-template-columns: repeat(5, 1fr);
      }}
    }}

    .matrix-btn {{
      height: 48px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
      background: var(--bg-surface-elevated);
      color: var(--text-main);
      font-size: 0.95rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      transition: all var(--transition);
    }}
    .matrix-btn:hover {{
      border-color: var(--primary);
      transform: scale(1.05);
    }}
    .matrix-btn.current {{
      border: 2px solid var(--primary) !important;
      box-shadow: 0 0 10px rgba(var(--primary-rgb), 0.4);
    }}
    .matrix-btn.correct {{
      background: var(--success-bg) !important;
      border-color: var(--success) !important;
      color: var(--success) !important;
    }}
    .matrix-btn.incorrect {{
      background: var(--danger-bg) !important;
      border-color: var(--danger) !important;
      color: var(--danger) !important;
    }}
    .matrix-btn.flagged::after {{
      content: "★";
      position: absolute;
      top: 2px;
      right: 4px;
      font-size: 0.65rem;
      color: var(--warning);
    }}

    .matrix-legend {{
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      font-size: 0.8rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border-subtle);
      padding-top: 1rem;
    }}
    .legend-item {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }}
    .legend-dot {{
      width: 12px;
      height: 12px;
      border-radius: var(--radius-sm);
    }}

    /* Summary Modal */
    .summary-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(6px);
      z-index: 110;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1rem;
    }}
    .summary-modal-backdrop.open {{
      display: flex;
    }}

    .summary-modal {{
      background: var(--bg-surface);
      border: 1px solid var(--border-medium);
      border-radius: var(--radius-lg);
      max-width: 520px;
      width: 100%;
      padding: 2rem;
      text-align: center;
      box-shadow: var(--shadow-lg);
    }}

    .summary-badge {{
      display: inline-block;
      font-size: 0.85rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 0.4rem 1rem;
      border-radius: var(--radius-full);
      margin-bottom: 1rem;
    }}
    .badge-gold {{
      background: rgba(251, 191, 36, 0.2);
      color: #fbbf24;
      border: 1px solid #fbbf24;
    }}
    .badge-silver {{
      background: rgba(203, 213, 225, 0.2);
      color: #cbd5e1;
      border: 1px solid #cbd5e1;
    }}
    .badge-elite {{
      background: rgba(99, 102, 241, 0.2);
      color: #818cf8;
      border: 1px solid #818cf8;
    }}
    .badge-pass {{
      background: rgba(16, 185, 129, 0.2);
      color: #10b981;
      border: 1px solid #10b981;
    }}
    .badge-fail {{
      background: rgba(239, 68, 68, 0.2);
      color: #ef4444;
      border: 1px solid #ef4444;
    }}

    .summary-score-large {{
      font-size: 3.5rem;
      font-weight: 800;
      line-height: 1;
      margin-bottom: 0.25rem;
      color: var(--text-main);
    }}
    .summary-denom {{
      font-size: 1.1rem;
      color: var(--text-muted);
      margin-bottom: 1.5rem;
    }}

    .summary-stats-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.75rem;
      margin-bottom: 1.75rem;
    }}
    .stat-box {{
      background: var(--bg-surface-elevated);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 0.75rem 0.5rem;
    }}
    .stat-box-val {{
      font-size: 1.3rem;
      font-weight: 800;
      margin-bottom: 0.15rem;
    }}
    .stat-box-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .summary-actions {{
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }}

    /* Bottom Sticky Week Switcher Footer */
    .page-footer-nav {{
      background: var(--bg-surface);
      border-top: 1px solid var(--border-subtle);
      padding: 1rem;
      margin-top: 2rem;
    }}
    .footer-inner {{
      max-width: 900px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    @media (max-width: 640px) {{
      .header-content {{
        padding: 0.6rem 0.75rem;
      }}
      .week-badge-header span.week-title-short {{
        display: none;
      }}
      .question-card {{
        padding: 1.15rem;
      }}
      .q-title {{
        font-size: 1.05rem;
      }}
      .q-prompt {{
        font-size: 0.95rem;
      }}
      .option-btn {{
        padding: 0.85rem 1rem;
        font-size: 0.92rem;
      }}
      .nav-action-btn {{
        padding: 0.65rem 0.9rem;
        font-size: 0.85rem;
      }}
    }}
  </style>
</head>
<body>

  <!-- Sticky Top Header -->
  <header class="app-header">
    <div class="header-content">
      <div class="header-left">
        <a href="index.html" class="hub-link" title="Return to Course Hub">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Hub
        </a>
        <div class="week-badge-header">
          <span>Week {week_num}</span>
          <span class="week-title-short" style="font-weight: 500; font-size: 0.85rem; color: var(--text-muted); max-width: 250px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">— {week_title}</span>
          <span class="q-counter-pill" id="headerQCtr">Q 1 / 30</span>
        </div>
      </div>
      
      <div class="header-right">
        <div class="score-pill" id="scoreBadge" title="Live Correct Answers">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
          <span id="scoreText">0 / 0</span>
        </div>
        <button class="icon-btn" id="btnThemeToggle" title="Toggle Dark/Light Mode">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
        </button>
      </div>
    </div>
  </header>

  <main class="main-container">
    <!-- Progress & View Controls -->
    <div class="progress-track">
      <div class="progress-fill" id="progressFill"></div>
    </div>

    <div class="controls-bar">
      <div class="view-toggle-group">
        <button class="toggle-opt-btn active" id="btnModeCard">Card Mode</button>
        <button class="toggle-opt-btn" id="btnModeList">List Mode</button>
      </div>

      <button class="nav-drawer-trigger" id="btnOpenNav">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
        Question Matrix (1–30)
      </button>
    </div>

    <!-- Active Question Card (Used in Card Mode) -->
    <div id="cardViewContainer">
      <article class="question-card" id="activeCard">
        <div class="q-meta-row">
          <div class="q-tags">
            <span class="badge badge-qnum" id="cardQNumBadge">Question 1 of 30</span>
            <span class="badge" id="cardTypeBadge">MCQ</span>
          </div>
          <button class="flag-btn" id="cardFlagBtn">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
            <span id="flagBtnText">Flag</span>
          </button>
        </div>

        <h2 class="q-title" id="cardTitle"></h2>
        <div class="q-prompt" id="cardPrompt"></div>
        <div class="msq-hint" id="cardMsqHint" style="display: none;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          Multiple Choice: Select all matching options, then click Submit Answer.
        </div>

        <!-- Options Container -->
        <div class="options-grid" id="cardOptionsContainer"></div>

        <button class="msq-submit-btn" id="cardMsqSubmitBtn" style="display: none;">
          Submit Answer
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
        </button>

        <!-- Instant Explanation Area -->
        <div class="feedback-panel" id="cardFeedbackPanel" style="display: none;">
          <div class="fb-header">
            <div class="fb-status-tag" id="cardFbStatus"></div>
            <div class="fb-ans-callout" id="cardFbAnswerCallout"></div>
          </div>
          <div class="fb-explanation-body" id="cardFbExplanation"></div>
        </div>

        <!-- Footer Navigation Controls -->
        <div class="card-nav-footer">
          <button class="nav-action-btn" id="btnPrev">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
            Previous
          </button>
          <button class="nav-action-btn" id="btnNext">
            Next
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </article>
    </div>

    <!-- List View Container (All 30 Questions) -->
    <div id="listViewContainer" style="display: none;"></div>
  </main>

  <!-- Question Matrix Modal / Drawer -->
  <div class="nav-modal-backdrop" id="navModalBackdrop">
    <div class="nav-modal">
      <div class="modal-head">
        <h3>Question Navigator (Week {week_num})</h3>
        <button class="icon-btn" id="btnCloseNav">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>

      <div class="matrix-grid" id="matrixGrid"></div>

      <div class="matrix-legend">
        <div class="legend-item"><div class="legend-dot" style="background: var(--bg-surface-elevated); border: 1px solid var(--border-medium);"></div> Unanswered</div>
        <div class="legend-item"><div class="legend-dot" style="background: var(--success);"></div> Correct</div>
        <div class="legend-item"><div class="legend-dot" style="background: var(--danger);"></div> Incorrect</div>
        <div class="legend-item"><span>★</span> Flagged</div>
      </div>
    </div>
  </div>

  <!-- Final Score & Certification Summary Modal -->
  <div class="summary-modal-backdrop" id="summaryModalBackdrop">
    <div class="summary-modal">
      <div class="summary-badge" id="sumBadge">Elite + Gold Medal</div>
      <h2 style="font-size: 1.6rem; margin-bottom: 0.35rem;">Assessment Completed!</h2>
      <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 1.5rem;">Week {week_num} &bull; {week_title}</p>

      <div class="summary-score-large" id="sumScoreVal">0</div>
      <div class="summary-denom">out of 30 questions</div>

      <div class="summary-stats-grid">
        <div class="stat-box">
          <div class="stat-box-val" id="sumAccuracyVal" style="color: var(--primary);">0%</div>
          <div class="stat-box-label">Accuracy</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-val" id="sumCorrectVal" style="color: var(--success);">0</div>
          <div class="stat-box-label">Correct</div>
        </div>
        <div class="stat-box">
          <div class="stat-box-val" id="sumIncorrectVal" style="color: var(--danger);">0</div>
          <div class="stat-box-label">Incorrect</div>
        </div>
      </div>

      <div class="summary-actions">
        <button class="nav-action-btn btn-next-highlight" id="btnSumReview">Review All Answers</button>
        <button class="nav-action-btn" id="btnSumRetake">Retake This Week</button>
        <a href="{next_week_file}" class="nav-action-btn" style="text-decoration: none; justify-content: center; background: rgba(var(--accent-rgb), 0.15); border-color: rgba(var(--accent-rgb), 0.4); color: #a5b4fc;">
          {next_label}
        </a>
      </div>
    </div>
  </div>

  <!-- Bottom Navigation Link Footer -->
  <footer class="page-footer-nav">
    <div class="footer-inner">
      <a href="{prev_week_file}" class="hub-link">{prev_label}</a>
      <span style="font-size: 0.85rem; color: var(--text-dim); text-align: center;">NPTEL Cloud Computing &bull; IIT Kharagpur</span>
      <a href="{next_week_file}" class="hub-link">{next_label}</a>
    </div>
  </footer>

  <!-- Quiz Engine Script -->
  <script>
    const QUESTIONS = {questions_json};
    const TOTAL_Q = QUESTIONS.length;
    const WEEK_NUM = {week_num};

    // User State
    const state = {{
      currentIdx: 0,
      userAnswers: {{}},       // qId -> [selectedIdxs]
      userResults: {{}},       // qId -> boolean (true=correct, false=incorrect)
      flagged: new Set(),
      viewMode: 'card',       // 'card' or 'list'
      msqTempSelections: {{}}  // qId -> Set of selected indices before submit
    }};

    // DOM Elements
    const cardViewContainer = document.getElementById('cardViewContainer');
    const listViewContainer = document.getElementById('listViewContainer');
    const headerQCtr = document.getElementById('headerQCtr');
    const scoreText = document.getElementById('scoreText');
    const progressFill = document.getElementById('progressFill');
    const btnModeCard = document.getElementById('btnModeCard');
    const btnModeList = document.getElementById('btnModeList');
    const btnThemeToggle = document.getElementById('btnThemeToggle');
    const btnOpenNav = document.getElementById('btnOpenNav');
    const btnCloseNav = document.getElementById('btnCloseNav');
    const navModalBackdrop = document.getElementById('navModalBackdrop');
    const matrixGrid = document.getElementById('matrixGrid');

    // Card View DOM
    const cardQNumBadge = document.getElementById('cardQNumBadge');
    const cardTypeBadge = document.getElementById('cardTypeBadge');
    const cardFlagBtn = document.getElementById('cardFlagBtn');
    const flagBtnText = document.getElementById('flagBtnText');
    const cardTitle = document.getElementById('cardTitle');
    const cardPrompt = document.getElementById('cardPrompt');
    const cardMsqHint = document.getElementById('cardMsqHint');
    const cardOptionsContainer = document.getElementById('cardOptionsContainer');
    const cardMsqSubmitBtn = document.getElementById('cardMsqSubmitBtn');
    const cardFeedbackPanel = document.getElementById('cardFeedbackPanel');
    const cardFbStatus = document.getElementById('cardFbStatus');
    const cardFbAnswerCallout = document.getElementById('cardFbAnswerCallout');
    const cardFbExplanation = document.getElementById('cardFbExplanation');
    const btnPrev = document.getElementById('btnPrev');
    const btnNext = document.getElementById('btnNext');

    // Summary Modal DOM
    const summaryModalBackdrop = document.getElementById('summaryModalBackdrop');
    const sumBadge = document.getElementById('sumBadge');
    const sumScoreVal = document.getElementById('sumScoreVal');
    const sumAccuracyVal = document.getElementById('sumAccuracyVal');
    const sumCorrectVal = document.getElementById('sumCorrectVal');
    const sumIncorrectVal = document.getElementById('sumIncorrectVal');
    const btnSumReview = document.getElementById('btnSumReview');
    const btnSumRetake = document.getElementById('btnSumRetake');

    // Init Theme
    (function initTheme() {{
      const savedTheme = localStorage.getItem('nptel_quiz_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
    }})();

    btnThemeToggle.addEventListener('click', () => {{
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      localStorage.setItem('nptel_quiz_theme', next);
    }});

    // =========================================================================
    // INITIALIZATION
    // =========================================================================
    function init() {{
      buildMatrix();
      renderCurrentCard();
      updateScoreboard();
      setupEvents();
    }}

    function buildMatrix() {{
      matrixGrid.innerHTML = '';
      QUESTIONS.forEach((q, idx) => {{
        const btn = document.createElement('button');
        btn.className = 'matrix-btn';
        btn.id = 'matBtn_' + q.id;
        btn.textContent = q.id;
        btn.addEventListener('click', () => {{
          state.currentIdx = idx;
          if (state.viewMode === 'card') {{
            renderCurrentCard();
          }} else {{
            const el = document.getElementById('listQCard_' + q.id);
            if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
          }}
          closeNavModal();
        }});
        matrixGrid.appendChild(btn);
      }});
      updateMatrixVisuals();
    }}

    function updateMatrixVisuals() {{
      QUESTIONS.forEach((q, idx) => {{
        const btn = document.getElementById('matBtn_' + q.id);
        if (!btn) return;
        
        btn.classList.toggle('current', idx === state.currentIdx);
        btn.classList.toggle('flagged', state.flagged.has(q.id));
        
        if (state.userResults[q.id] === true) {{
          btn.className = 'matrix-btn correct' + (idx === state.currentIdx ? ' current' : '') + (state.flagged.has(q.id) ? ' flagged' : '');
        }} else if (state.userResults[q.id] === false) {{
          btn.className = 'matrix-btn incorrect' + (idx === state.currentIdx ? ' current' : '') + (state.flagged.has(q.id) ? ' flagged' : '');
        }} else {{
          btn.className = 'matrix-btn' + (idx === state.currentIdx ? ' current' : '') + (state.flagged.has(q.id) ? ' flagged' : '');
        }}
      }});
    }}

    function updateScoreboard() {{
      const answeredKeys = Object.keys(state.userResults);
      const totalAnswered = answeredKeys.length;
      let correctCount = 0;
      answeredKeys.forEach(k => {{
        if (state.userResults[k] === true) correctCount++;
      }});

      headerQCtr.textContent = 'Q ' + (state.currentIdx + 1) + ' / ' + TOTAL_Q;
      scoreText.textContent = correctCount + ' / ' + totalAnswered;
      
      const pct = (totalAnswered / TOTAL_Q) * 100;
      progressFill.style.width = pct + '%';
      
      updateMatrixVisuals();

      // Check if all answered
      if (totalAnswered === TOTAL_Q && !state.summaryShown) {{
        state.summaryShown = true;
        setTimeout(showSummaryModal, 600);
      }}
    }}

    // =========================================================================
    // CARD MODE RENDERER
    // =========================================================================
    function renderCurrentCard() {{
      const q = QUESTIONS[state.currentIdx];
      const isMSQ = q.type === 'MSQ';
      const isAnswered = state.userAnswers[q.id] !== undefined;

      // Meta
      cardQNumBadge.textContent = 'Question ' + (state.currentIdx + 1) + ' of ' + TOTAL_Q;
      cardTypeBadge.textContent = q.type;
      cardTypeBadge.className = 'badge ' + (isMSQ ? 'badge-msq' : 'badge-mcq');
      
      // Flag state
      const isFlagged = state.flagged.has(q.id);
      cardFlagBtn.classList.toggle('flagged', isFlagged);
      flagBtnText.textContent = isFlagged ? 'Flagged' : 'Flag';

      // Title & Prompt
      cardTitle.innerHTML = q.title;
      cardPrompt.innerHTML = q.question_html;
      cardMsqHint.style.display = isMSQ ? 'flex' : 'none';

      // Options
      cardOptionsContainer.innerHTML = '';
      
      // Initialize temp selections for MSQ
      if (isMSQ && !state.msqTempSelections[q.id]) {{
        state.msqTempSelections[q.id] = new Set(state.userAnswers[q.id] || []);
      }}

      q.options_html.forEach((optHtml, optIdx) => {{
        const btn = document.createElement('button');
        btn.className = 'option-btn' + (isMSQ ? ' opt-btn-msq' : '');
        btn.id = 'cardOpt_' + optIdx;

        const letter = String.fromCharCode(65 + optIdx);
        
        let isSelected = false;
        if (isAnswered) {{
          isSelected = state.userAnswers[q.id].includes(optIdx);
        }} else if (isMSQ) {{
          isSelected = state.msqTempSelections[q.id].has(optIdx);
        }}

        // Format classes if answered
        if (isAnswered) {{
          btn.classList.add('locked');
          const isCorrect = q.answer.includes(optIdx);
          if (isSelected && isCorrect) {{
            btn.classList.add('state-chosen-correct');
          }} else if (isSelected && !isCorrect) {{
            btn.classList.add('state-chosen-incorrect');
          }} else if (!isSelected && isCorrect) {{
            btn.classList.add('state-target-correct');
          }}
        }} else if (isMSQ && isSelected) {{
          btn.classList.add('state-msq-selected');
        }}

        btn.innerHTML = `
          <span class="opt-letter">${{letter}}</span>
          <span class="opt-text">${{optHtml}}</span>
        `;

        btn.addEventListener('click', () => {{
          if (state.userAnswers[q.id] !== undefined) return; // Locked

          if (isMSQ) {{
            // Toggle MSQ
            if (state.msqTempSelections[q.id].has(optIdx)) {{
              state.msqTempSelections[q.id].delete(optIdx);
            }} else {{
              state.msqTempSelections[q.id].add(optIdx);
            }}
            renderCurrentCard();
          }} else {{
            // Instant MCQ Answer
            handleAnswerSubmit(q, [optIdx]);
          }}
        }});

        cardOptionsContainer.appendChild(btn);
      }});

      // MSQ Submit Button
      if (isMSQ && !isAnswered) {{
        cardMsqSubmitBtn.style.display = 'inline-flex';
        cardMsqSubmitBtn.disabled = state.msqTempSelections[q.id].size === 0;
        cardMsqSubmitBtn.onclick = () => {{
          const chosen = Array.from(state.msqTempSelections[q.id]).sort();
          handleAnswerSubmit(q, chosen);
        }};
      }} else {{
        cardMsqSubmitBtn.style.display = 'none';
      }}

      // Feedback & Explanation
      if (isAnswered) {{
        renderFeedbackPanel(cardFeedbackPanel, cardFbStatus, cardFbAnswerCallout, cardFbExplanation, q);
        cardFeedbackPanel.style.display = 'block';
      }} else {{
        cardFeedbackPanel.style.display = 'none';
      }}

      // Prev / Next button states
      btnPrev.disabled = state.currentIdx === 0;
      if (state.currentIdx === TOTAL_Q - 1) {{
        btnNext.innerHTML = `View Summary <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>`;
        btnNext.classList.add('btn-next-highlight');
      }} else {{
        btnNext.innerHTML = `Next Question <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>`;
        if (isAnswered) {{
          btnNext.classList.add('btn-next-highlight');
        }} else {{
          btnNext.classList.remove('btn-next-highlight');
        }}
      }}

      updateScoreboard();
    }}

    // =========================================================================
    // ANSWER PROCESSING & INSTANT FEEDBACK
    // =========================================================================
    function handleAnswerSubmit(q, selectedIndices) {{
      state.userAnswers[q.id] = selectedIndices;
      
      // Evaluate correctness
      const correctIndices = [...q.answer].sort();
      const userSorted = [...selectedIndices].sort();
      
      const isAllCorrect = (correctIndices.length === userSorted.length) &&
        correctIndices.every((val, i) => val === userSorted[i]);
      
      state.userResults[q.id] = isAllCorrect;

      if (state.viewMode === 'card') {{
        renderCurrentCard();
      }} else {{
        renderListCard(q);
      }}

      updateScoreboard();
    }}

    function renderFeedbackPanel(panelEl, statusEl, ansCalloutEl, expEl, q) {{
      const isCorrect = state.userResults[q.id];
      const correctLetters = q.answer.map(idx => String.fromCharCode(65 + idx)).join(', ');

      if (isCorrect) {{
        panelEl.className = 'feedback-panel status-correct';
        statusEl.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
          Correct! (+1 Mark)
        `;
      }} else {{
        panelEl.className = 'feedback-panel status-incorrect';
        statusEl.innerHTML = `
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
          Incorrect (0 Marks)
        `;
      }}

      ansCalloutEl.innerHTML = '<strong>Correct Answer:</strong> Option ' + correctLetters;
      expEl.innerHTML = `<strong>Explanation:</strong> ` + q.explanation_html;
    }}

    // =========================================================================
    // LIST VIEW RENDERER (ALL 30 QUESTIONS)
    // =========================================================================
    function renderListView() {{
      listViewContainer.innerHTML = '';
      QUESTIONS.forEach((q, idx) => {{
        const card = createListQuestionElement(q, idx);
        listViewContainer.appendChild(card);
      }});
    }}

    function createListQuestionElement(q, idx) {{
      const card = document.createElement('article');
      card.className = 'question-card';
      card.id = 'listQCard_' + q.id;

      const isMSQ = q.type === 'MSQ';
      const isAnswered = state.userAnswers[q.id] !== undefined;

      // Meta
      const metaRow = document.createElement('div');
      metaRow.className = 'q-meta-row';
      metaRow.innerHTML = `
        <div class="q-tags">
          <span class="badge badge-qnum">Question ${{idx + 1}} of ${{TOTAL_Q}}</span>
          <span class="badge ${{isMSQ ? 'badge-msq' : 'badge-mcq'}}">${{q.type}}</span>
        </div>
        <button class="flag-btn ${{state.flagged.has(q.id) ? 'flagged' : ''}}" id="listFlag_${{q.id}}">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          <span>${{state.flagged.has(q.id) ? 'Flagged' : 'Flag'}}</span>
        </button>
      `;

      metaRow.querySelector('#listFlag_' + q.id).addEventListener('click', () => {{
        if (state.flagged.has(q.id)) state.flagged.delete(q.id);
        else state.flagged.add(q.id);
        renderListCard(q);
        updateMatrixVisuals();
      }});

      card.appendChild(metaRow);

      // Title & Prompt
      const titleEl = document.createElement('h2');
      titleEl.className = 'q-title';
      titleEl.innerHTML = q.title;
      card.appendChild(titleEl);

      const promptEl = document.createElement('div');
      promptEl.className = 'q-prompt';
      promptEl.innerHTML = q.question_html;
      card.appendChild(promptEl);

      if (isMSQ) {{
        const msqHint = document.createElement('div');
        msqHint.className = 'msq-hint';
        msqHint.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg> Select all matching options, then click Submit Answer.`;
        card.appendChild(msqHint);
      }}

      // Options
      const optsGrid = document.createElement('div');
      optsGrid.className = 'options-grid';

      if (isMSQ && !state.msqTempSelections[q.id]) {{
        state.msqTempSelections[q.id] = new Set(state.userAnswers[q.id] || []);
      }}

      q.options_html.forEach((optHtml, optIdx) => {{
        const btn = document.createElement('button');
        btn.className = 'option-btn' + (isMSQ ? ' opt-btn-msq' : '');
        const letter = String.fromCharCode(65 + optIdx);
        
        let isSelected = false;
        if (isAnswered) {{
          isSelected = state.userAnswers[q.id].includes(optIdx);
        }} else if (isMSQ) {{
          isSelected = state.msqTempSelections[q.id].has(optIdx);
        }}

        if (isAnswered) {{
          btn.classList.add('locked');
          const isCorrect = q.answer.includes(optIdx);
          if (isSelected && isCorrect) btn.classList.add('state-chosen-correct');
          else if (isSelected && !isCorrect) btn.classList.add('state-chosen-incorrect');
          else if (!isSelected && isCorrect) btn.classList.add('state-target-correct');
        }} else if (isMSQ && isSelected) {{
          btn.classList.add('state-msq-selected');
        }}

        btn.innerHTML = `<span class="opt-letter">${{letter}}</span><span class="opt-text">${{optHtml}}</span>`;

        btn.addEventListener('click', () => {{
          if (state.userAnswers[q.id] !== undefined) return;
          if (isMSQ) {{
            if (state.msqTempSelections[q.id].has(optIdx)) {{
              state.msqTempSelections[q.id].delete(optIdx);
            }} else {{
              state.msqTempSelections[q.id].add(optIdx);
            }}
            renderListCard(q);
          }} else {{
            handleAnswerSubmit(q, [optIdx]);
          }}
        }});

        optsGrid.appendChild(btn);
      }});
      card.appendChild(optsGrid);

      // Submit Button for MSQ
      if (isMSQ && !isAnswered) {{
        const subBtn = document.createElement('button');
        subBtn.className = 'msq-submit-btn';
        subBtn.innerHTML = `Submit Answer <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>`;
        subBtn.disabled = state.msqTempSelections[q.id].size === 0;
        subBtn.onclick = () => {{
          const chosen = Array.from(state.msqTempSelections[q.id]).sort();
          handleAnswerSubmit(q, chosen);
        }};
        card.appendChild(subBtn);
      }}

      // Feedback Panel
      if (isAnswered) {{
        const fbPanel = document.createElement('div');
        const fbStatus = document.createElement('div');
        const fbAnsCallout = document.createElement('div');
        const fbExp = document.createElement('div');
        renderFeedbackPanel(fbPanel, fbStatus, fbAnsCallout, fbExp, q);
        card.appendChild(fbPanel);
      }}

      return card;
    }}

    function renderListCard(q) {{
      const existing = document.getElementById('listQCard_' + q.id);
      if (!existing) return;
      const idx = QUESTIONS.findIndex(item => item.id === q.id);
      const updated = createListQuestionElement(q, idx);
      existing.replaceWith(updated);
    }}

    // =========================================================================
    // EVENT HANDLERS
    // =========================================================================
    function setupEvents() {{
      // Mode toggle
      btnModeCard.addEventListener('click', () => {{
        state.viewMode = 'card';
        btnModeCard.classList.add('active');
        btnModeList.classList.remove('active');
        cardViewContainer.style.display = 'block';
        listViewContainer.style.display = 'none';
        renderCurrentCard();
      }});

      btnModeList.addEventListener('click', () => {{
        state.viewMode = 'list';
        btnModeList.classList.add('active');
        btnModeCard.classList.remove('active');
        cardViewContainer.style.display = 'none';
        listViewContainer.style.display = 'block';
        renderListView();
      }});

      // Card Navigation Prev / Next
      btnPrev.addEventListener('click', () => {{
        if (state.currentIdx > 0) {{
          state.currentIdx--;
          renderCurrentCard();
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}
      }});

      btnNext.addEventListener('click', () => {{
        if (state.currentIdx < TOTAL_Q - 1) {{
          state.currentIdx++;
          renderCurrentCard();
          window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }} else {{
          showSummaryModal();
        }}
      }});

      // Card Flag Button
      cardFlagBtn.addEventListener('click', () => {{
        const q = QUESTIONS[state.currentIdx];
        if (state.flagged.has(q.id)) {{
          state.flagged.delete(q.id);
        }} else {{
          state.flagged.add(q.id);
        }}
        renderCurrentCard();
      }});

      // Navigator Modal Open/Close
      btnOpenNav.addEventListener('click', openNavModal);
      btnCloseNav.addEventListener('click', closeNavModal);
      navModalBackdrop.addEventListener('click', (e) => {{
        if (e.target === navModalBackdrop) closeNavModal();
      }});

      // Summary Modal Actions
      btnSumReview.addEventListener('click', () => {{
        summaryModalBackdrop.classList.remove('open');
      }});

      btnSumRetake.addEventListener('click', () => {{
        if (confirm('Are you sure you want to reset all answers and retake Week ' + WEEK_NUM + '?')) {{
          state.userAnswers = {{}};
          state.userResults = {{}};
          state.msqTempSelections = {{}};
          state.currentIdx = 0;
          state.summaryShown = false;
          summaryModalBackdrop.classList.remove('open');
          renderCurrentCard();
          if (state.viewMode === 'list') renderListView();
          updateScoreboard();
        }}
      }});

      // Keyboard navigation (Card mode)
      document.addEventListener('keydown', (e) => {{
        if (navModalBackdrop.classList.contains('open') || summaryModalBackdrop.classList.contains('open')) return;
        
        if (e.key === 'ArrowLeft') {{
          btnPrev.click();
        }} else if (e.key === 'ArrowRight') {{
          btnNext.click();
        }} else if (['1', '2', '3', '4'].includes(e.key) && state.viewMode === 'card') {{
          const optIdx = parseInt(e.key) - 1;
          const optBtn = document.getElementById('cardOpt_' + optIdx);
          if (optBtn) optBtn.click();
        }}
      }});
    }}

    function openNavModal() {{
      updateMatrixVisuals();
      navModalBackdrop.classList.add('open');
    }}

    function closeNavModal() {{
      navModalBackdrop.classList.remove('open');
    }}

    function showSummaryModal() {{
      const answeredKeys = Object.keys(state.userResults);
      let correct = 0;
      answeredKeys.forEach(k => {{
        if (state.userResults[k] === true) correct++;
      }});
      const incorrect = answeredKeys.length - correct;
      const pct = (correct / TOTAL_Q) * 100;

      sumScoreVal.textContent = correct;
      sumAccuracyVal.textContent = pct.toFixed(1) + '%';
      sumCorrectVal.textContent = correct;
      sumIncorrectVal.textContent = incorrect;

      if (pct >= 90) {{
        sumBadge.className = 'summary-badge badge-gold';
        sumBadge.textContent = 'Elite + Gold Medal (Top 1%)';
      }} else if (pct >= 75) {{
        sumBadge.className = 'summary-badge badge-silver';
        sumBadge.textContent = 'Elite + Silver Medal';
      }} else if (pct >= 60) {{
        sumBadge.className = 'summary-badge badge-elite';
        sumBadge.textContent = 'Elite Certificate';
      }} else if (pct >= 40) {{
        sumBadge.className = 'summary-badge badge-pass';
        sumBadge.textContent = 'Successfully Completed';
      }} else {{
        sumBadge.className = 'summary-badge badge-fail';
        sumBadge.textContent = 'Needs Practice (< 40%)';
      }}

      summaryModalBackdrop.classList.add('open');
    }}

    // Boot
    window.addEventListener('DOMContentLoaded', init);
  </script>
</body>
</html>
"""
    return html

def build_hub_index():
    """Builds index.html as a central hub linking to all 10 weekly quiz files."""
    cards_html = ""
    for week_num, mod, title, desc in WEEK_MODULES:
        file_name = f"quiz_week{week_num:02d}.html"
        q_count = len(mod.questions)
        cards_html += f"""
        <a href="{file_name}" class="week-card">
          <div class="week-card-header">
            <span class="week-pill">Week {week_num:02d}</span>
            <span class="q-badge">{q_count} Questions</span>
          </div>
          <h3 class="week-card-title">{title}</h3>
          <p class="week-card-desc">{desc}</p>
          <div class="week-card-footer">
            <span class="btn-start">
              Start Quiz 
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            </span>
            <span class="inst-tag">Instant Feedback</span>
          </div>
        </a>
        """

    hub_html = f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>NPTEL Cloud Computing — Comprehensive 360 Exam Questions & Quiz Hub</title>
  <style>
    :root {{
      --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      --bg-body: #0b0f19;
      --bg-surface: #111827;
      --bg-card: #151e2e;
      --bg-card-hover: #1c283f;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-medium: rgba(255, 255, 255, 0.16);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --primary-rgb: 56, 189, 248;
      --accent: #6366f1;
      --success: #10b981;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-full: 9999px;
      --shadow-lg: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      --transition: 200ms cubic-bezier(0.4, 0, 0.2, 1);
    }}

    [data-theme="light"] {{
      --bg-body: #f8fafc;
      --bg-surface: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f1f5f9;
      --border-subtle: #e2e8f0;
      --border-medium: #cbd5e1;
      --text-main: #0f172a;
      --text-muted: #475569;
      --primary: #0284c7;
      --primary-rgb: 2, 132, 199;
      --accent: #4f46e5;
      --success: #059669;
    }}

    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.6;
      min-height: 100vh;
      -webkit-font-smoothing: antialiased;
    }}

    .hub-header {{
      background: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      position: sticky;
      top: 0;
      z-index: 50;
      backdrop-filter: blur(8px);
    }}

    .header-inner {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0.85rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }}

    .brand-title {{
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}
    .brand-title span.iit {{
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--primary);
      background: rgba(var(--primary-rgb), 0.12);
      padding: 0.2rem 0.5rem;
      border-radius: var(--radius-sm);
    }}

    .theme-btn {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      width: 38px;
      height: 38px;
      border-radius: var(--radius-sm);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
    }}

    .hero-section {{
      max-width: 1200px;
      margin: 2.5rem auto 1.5rem;
      padding: 0 1.5rem;
      text-align: center;
    }}

    .hero-title {{
      font-size: 2.4rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 0.75rem;
      line-height: 1.2;
    }}
    .hero-title span.gradient-txt {{
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-desc {{
      font-size: 1.1rem;
      color: var(--text-muted);
      max-width: 780px;
      margin: 0 auto 2rem;
    }}

    .stats-ribbon {{
      display: flex;
      justify-content: center;
      gap: 1.5rem;
      flex-wrap: wrap;
      margin-bottom: 2.5rem;
    }}
    .ribbon-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.9rem;
      font-weight: 700;
    }}
    .ribbon-item svg {{
      color: var(--primary);
    }}

    .container {{
      max-width: 1200px;
      margin: 0 auto 4rem;
      padding: 0 1.5rem;
    }}

    .grid-weeks {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 1.5rem;
    }}

    .week-card {{
      background: var(--bg-card);
      border: 1.5px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      text-decoration: none;
      color: inherit;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all var(--transition);
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }}
    .week-card:hover {{
      border-color: var(--primary);
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
      background: var(--bg-card-hover);
    }}

    .week-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 0.85rem;
    }}
    .week-pill {{
      font-size: 0.75rem;
      font-weight: 800;
      color: var(--primary);
      background: rgba(var(--primary-rgb), 0.12);
      border: 1px solid rgba(var(--primary-rgb), 0.3);
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .q-badge {{
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--text-muted);
      background: var(--bg-surface);
      padding: 0.25rem 0.55rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-subtle);
    }}

    .week-card-title {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 0.5rem;
      color: var(--text-main);
      line-height: 1.35;
    }}
    .week-card-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 1.25rem;
      flex: 1;
    }}

    .week-card-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      padding-top: 0.85rem;
    }}
    .btn-start {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      color: var(--primary);
      font-size: 0.9rem;
      font-weight: 700;
    }}
    .inst-tag {{
      font-size: 0.75rem;
      color: var(--success);
      font-weight: 600;
    }}

    /* Notes Banner */
    .notes-banner {{
      background: linear-gradient(135deg, rgba(99, 102, 241, 0.15), rgba(56, 189, 248, 0.15));
      border: 1.5px solid rgba(99, 102, 241, 0.3);
      border-radius: var(--radius-lg);
      padding: 1.75rem;
      margin-bottom: 3rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1.5rem;
      flex-wrap: wrap;
    }}
    .notes-banner-left h3 {{
      font-size: 1.25rem;
      font-weight: 800;
      margin-bottom: 0.35rem;
    }}
    .notes-banner-left p {{
      font-size: 0.92rem;
      color: var(--text-muted);
    }}
    .banner-cta {{
      background: var(--accent);
      color: #ffffff;
      padding: 0.75rem 1.4rem;
      border-radius: var(--radius-md);
      font-weight: 700;
      font-size: 0.92rem;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: all var(--transition);
      white-space: nowrap;
    }}
    .banner-cta:hover {{
      background: #4f46e5;
      transform: translateY(-1px);
    }}

    footer {{
      text-align: center;
      padding: 2rem 1.5rem;
      border-top: 1px solid var(--border-subtle);
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
  </style>
</head>
<body>
  <header class="hub-header">
    <div class="header-inner">
      <div class="brand-title">
        <span>NPTEL Cloud Computing</span>
        <span class="iit">IIT Kharagpur</span>
      </div>
      <button class="theme-btn" id="btnThemeToggle" title="Toggle Theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
    </div>
  </header>

  <section class="hero-section">
    <h1 class="hero-title">
      Master <span class="gradient-txt">NPTEL Cloud Computing</span>
    </h1>
    <p class="hero-desc">
      30 real NPTEL-style exam questions for each week (360 questions total across all 12 weeks). Dedicated interactive HTML for every week with instant answer reveal and comprehensive step-by-step technical explanations.
    </p>

    <div class="stats-ribbon">
      <div class="ribbon-item">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
        360 Questions Across All 12 Weeks
      </div>
      <div class="ribbon-item">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg>
        Instant Feedback After Every Question
      </div>
      <div class="ribbon-item">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2" ry="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>
        Works on Phone & Laptop (100% Offline)
      </div>
    </div>
  </section>

  <main class="container">
    <!-- Comprehensive Notes Callout -->
    <div class="notes-banner">
      <div class="notes-banner-left">
        <h3>Master Complete 12-Week Study Guide &amp; Textbook (`comprehensive_notes.pdf`)</h3>
        <p>A publication-grade, complete document covering all 12 weeks of lectures, formulas, theorems, TikZ architecture diagrams, and comprehensive solved NPTEL-style problems with step-by-step explanations.</p>
      </div>
      <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
        <a href="comprehensive_notes.pdf" class="banner-cta" target="_blank" style="background: var(--primary); color: #0b0f19;">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          Open Master Notes PDF
        </a>
        <a href="comprehensive_notes.tex" class="banner-cta" download>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
          LaTeX Source (.tex)
        </a>
      </div>
    </div>

    <!-- 10 Weeks Grid -->
    <div class="grid-weeks">
      {cards_html}
    </div>
  </main>

  <footer>
    <p>NPTEL Online Certification &bull; Cloud Computing &bull; Prof. Soumya K. Ghosh, Department of Computer Science & Engineering, IIT Kharagpur.</p>
    <p style="margin-top: 0.35rem; font-size: 0.8rem; color: var(--text-dim);">All questions and explanations are tailored strictly according to official NPTEL curriculum materials.</p>
  </footer>

  <script>
    (function() {{
      const savedTheme = localStorage.getItem('nptel_quiz_theme') || 'dark';
      document.documentElement.setAttribute('data-theme', savedTheme);
      document.getElementById('btnThemeToggle').addEventListener('click', () => {{
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('nptel_quiz_theme', next);
      }});
    }})();
  </script>
</body>
</html>
"""
    return hub_html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Building 12 standalone weekly quiz HTML files...")
    for week_num, mod, title, desc in WEEK_MODULES:
        file_name = f"quiz_week{week_num:02d}.html"
        out_path = os.path.join(base_dir, file_name)
        
        print(f"Generating {file_name} with {len(mod.questions)} questions...")
        html_content = build_quiz_page(week_num, mod, title, desc)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"  -> Saved {file_name} ({len(html_content)} bytes)")
        
    print("\nBuilding course hub (index.html)...")
    hub_path = os.path.join(base_dir, "index.html")
    hub_html = build_hub_index()
    with open(hub_path, 'w', encoding='utf-8') as f:
        f.write(hub_html)
    print(f"  -> Saved index.html ({len(hub_html)} bytes)")
    
    print("\nAll 12 weekly HTML files and index.html generated successfully!")

if __name__ == '__main__':
    main()
