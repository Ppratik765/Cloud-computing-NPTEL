# NPTEL Cloud Computing — Complete Course Notes & Interactive Quiz Platform

[![Course](https://img.shields.io/badge/NPTEL-Cloud%20Computing-blue.svg)](https://nptel.ac.in)
[![Institution](https://img.shields.io/badge/IIT%20Kharagpur-Dept%20of%20CSE-navy.svg)](https://cse.iitkgp.ac.in)
[![Total Questions](https://img.shields.io/badge/Exam%20Questions-360%20(30%2Fweek)-emerald.svg)](#interactive-quiz-hub)
[![Textbook](https://img.shields.io/badge/Study%20Guide-136%20Pages%20PDF-red.svg)](comprehensive_notes.pdf)
[![Vercel Ready](https://img.shields.io/badge/Vercel-Deployment%20Ready-black.svg?logo=vercel)](#deploying-to-vercel)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A complete, publication-grade academic repository for the **NPTEL Cloud Computing** certification course offered by **Prof. Soumya K. Ghosh**, Department of Computer Science and Engineering, **Indian Institute of Technology (IIT) Kharagpur**.

This repository contains:
1. **Interactive Quiz Web Application (Vercel-Ready):** 12 standalone interactive HTML quizzes with **360 authentic NPTEL-style questions** (30 questions per week), featuring instant answer validation and comprehensive technical explanations.
2. **Master Comprehensive Notes (`comprehensive_notes.pdf`):** A **136-page** textbook covering the complete 12-week syllabus, architectural TikZ figures, formal theorems, and **122 solved numerical problems**.
3. **Official Course Materials:** Original lecture slide sets (`Week-01.pdf` through `Week-12.pdf`) and official assignments (`Assignment 1.pdf` through `Assignment 10.pdf`).
4. **Full LaTeX Source:** Modular, clean LaTeX files (`comprehensive_notes.tex` and `parts/`) ready to compile locally.

---

## Interactive Quiz Hub (Web App)

The interactive web application is designed to simulate the real NPTEL certification exam format while delivering immediate pedagogical feedback.

* **Central Portal:** Open [`index.html`](index.html) to view the course roadmap, progress statistics, and direct links to each weekly quiz.
* **Instant Answer Reveal:** Selecting any option immediately indicates whether it is correct (emerald green) or incorrect (crimson), displays the designated correct answer, and expands a step-by-step scientific/mathematical explanation.
* **Responsive & Mobile-First:** Works offline and on all mobile phones, tablets, and laptops.
* **Practice Filtering:** Filter by *All Questions*, *Unanswered*, *Incorrect*, or *Flagged for Review*.
* **State Persistence:** Quiz answers, progress bars, scores, and theme settings (Dark/Light mode) persist locally across browser sessions using `localStorage`.

---

## 12-Week Curriculum & Quiz Directory

| Week | Core Module Title | Key Topics Covered | Interactive Quiz | Solved Problems |
| :---: | :--- | :--- | :---: | :---: |
| **01** | **Introduction, NIST Model & Architecture** | Computing trends, NIST 5 essential characteristics, SPI service models, 4 deployment models, hardware virtualization basics. | [**Quiz 01**](quiz_week01.html) | 10 Solved |
| **02** | **Cloud Architecture & Cloud Storage** | Hypervisors (Type-1 bare metal vs. Type-2 hosted), Full vs. Para-virtualization, Intel VT-x hardware assist, OpenStack Swift vs. Amazon S3 object stores. | [**Quiz 02**](quiz_week02.html) | 10 Solved |
| **03** | **Virtualization Deep Dive & Memory Management** | Popek-Goldberg virtualization theorem, Shadow Page Tables, Hardware Nested Page Tables (Intel EPT / AMD NPT), Memory Ballooning, Transparent Page Sharing (TPS). | [**Quiz 03**](quiz_week03.html) | 10 Solved |
| **04** | **Cloud Platforms: OpenStack, Azure, GCP** | Meghamala IIT Kharagpur cloud, OpenStack core services (Nova, Neutron, Keystone, Glance, Swift, Cinder), Microsoft Azure architecture, GCP Spanner TrueTime & Andromeda SDN. | [**Quiz 04**](quiz_week04.html) | 10 Solved |
| **05** | **SLA Management & Cloud Economics** | Formal SLA availability formulation ($A = \frac{\text{MTBF}}{\text{MTBF}+\text{MTTR}}$), Service credit penalties, Buy vs. Lease economic threshold ($U < P/A$), HDFS split placement, PUE basics. | [**Quiz 05**](quiz_week05.html) | 10 Solved |
| **06** | **Cloud Security, Privacy & Threat Modeling** | CIA Triad, structural attack models, CPU cache side-channel attacks (Prime+Probe), Gartner 7 cloud risks, OAuth 2.0 vs. SAML federated identity management. | [**Quiz 06**](quiz_week06.html) | 10 Solved |
| **07** | **Mobile Cloud Computing & Geospatial Cloud** | Mobile computational offloading conditions (Kumar & Lu energy inequality), Cloudlets & dynamic VM synthesis, OGC geospatial web services (WMS, WFS, WCS, WPS). | [**Quiz 07**](quiz_week07.html) | 10 Solved |
| **08** | **Containers, Docker & Sensor-Cloud** | OS containers vs. hardware VMs, Linux namespaces & cgroups, OverlayFS Copy-on-Write storage, Dockerfile directives, Kubernetes architecture, Sensor-Cloud virtualization. | [**Quiz 08**](quiz_week08.html) | 10 Solved |
| **09** | **Hierarchical Edge-Fog-Cloud & Federation** | 3-tier computing hierarchy, iFogSim simulation modeling, vertical vs. horizontal elasticity, Cloud Federation architectures and multi-cloud brokering. | [**Quiz 09**](quiz_week09.html) | 10 Solved |
| **10** | **VM Migration & Container Primitives** | Pre-copy push vs. post-copy pull live migration, memory dirtying convergence ($D < R$), downtime formulation, Docker volumes & persistent data management. | [**Quiz 10**](quiz_week10.html) | 10 Solved |
| **11** | **Dew Computing, Serverless & Green Cloud** | Dew computing 6 service models (SiD, PiD, IaD, DbID, WiD, StID), Serverless FaaS scale-to-zero, cold-start mitigation (Provisioned Concurrency), PUE/DCiE, CMOS DVFS power model ($P \propto V^2 f$). | [**Quiz 11**](quiz_week11.html) | 10 Solved |
| **12** | **5G Era, CPS, Spatial Cloud & IoHT** | 5G pillars (eMBB, URLLC, mMTC), Multi-Access Edge Computing (MEC), NIST CPCC framework, Traj-Cloud MapReduce map-matching, 4-tier IoHT architecture & hardware prototyping. | [**Quiz 12**](quiz_week12.html) | 12 Solved |

---

## Master Study Guide (`comprehensive_notes.pdf`)

The generated PDF study guide is a complete, self-contained textbook:
* **Page Count:** 136 publication-grade pages.
* **Format:** Formatted in standard A4 with clean typography, hyperlinked Table of Contents, and color-coded semantic blocks.
* **Callout Elements:**
  * `defbox`: Formal academic definitions (NIST, ISO, IEEE, NSF).
  * `thmbox`: Key theorems and formal lemmas (Popek-Goldberg, Nyquist delay margins).
  * `warnbox`: Common pitfalls and examination trap questions.
  * `solved`: **122 comprehensive numerical & conceptual examples** with step-by-step mathematical substitutions.
* **Download:** [**Download comprehensive_notes.pdf**](comprehensive_notes.pdf)

---

## Deploying to Vercel

You can host this entire interactive platform on [Vercel](https://vercel.com) for free:

### Method 1: Import via Vercel Dashboard (Fastest)
1. Log in to [Vercel](https://vercel.com).
2. Click **Add New...** $\to$ **Project**.
3. Import your GitHub repository: `Ppratik765/Cloud-computing-NPTEL`.
4. Configure Project:
   * **Framework Preset:** `Other` (Static Site)
   * **Root Directory:** `./`
   * **Build Command:** *(Leave empty)*
   * **Output Directory:** `.`
5. Click **Deploy**.
6. Your quiz hub will be live at `https://cloud-computing-nptel.vercel.app` (or your custom Vercel subdomain).

### Method 2: Deploy via Vercel CLI
```bash
npm i -g vercel
vercel
```

The included [`vercel.json`](vercel.json) automatically configures clean URLs and proper MIME headers for PDF viewing and downloads.

---

## Local Offline Practice

No internet connection or local web server is required to use this platform:
1. Clone this repository:
   ```bash
   git clone https://github.com/Ppratik765/Cloud-computing-NPTEL.git
   cd Cloud-computing-NPTEL
   ```
2. Double-click [`index.html`](index.html) to open the portal in Google Chrome, Microsoft Edge, Mozilla Firefox, or Apple Safari.
3. Everything (styles, fonts, math symbols, scripts, and PDF files) runs 100% locally.

---

## Rebuilding the Quizzes & Notes

If you want to edit question datasets or recompile the LaTeX notes:

### Regenerating HTML Quizzes
Question datasets reside in Python modules under `quiz_data/week01.py` through `quiz_data/week12.py`.
To rebuild all 12 quiz HTML files and `index.html`:
```bash
python build_all_weekly_quizzes.py
```

### Compiling LaTeX Notes Locally
Using `pdflatex` / `xelatex` / `tectonic`:
```bash
# Using tectonic
tectonic comprehensive_notes.tex

# Or using xelatex
xelatex comprehensive_notes.tex
xelatex comprehensive_notes.tex
```

---

## High-Yield Mathematical Formulas for NPTEL

For rapid revision before the final exam:

1. **System Availability:**
   $$A = \frac{\text{MTBF}}{\text{MTBF} + \text{MTTR}}$$
2. **Buy vs. Lease Economic Indifference Threshold:**
   $$U = \frac{P}{A}$$
   *(If actual utilization $U < \frac{P}{A}$, renting from cloud is cheaper; if $U > \frac{P}{A}$, buying in-house hardware is cheaper).*
3. **Kumar & Lu Mobile Computation Offloading Energy Condition:**
   $$E_{\text{save}} = P_l \cdot \frac{w}{S_m} - \left( P_t \cdot \frac{D}{B} + P_i \cdot \frac{w}{S_c} \right) > 0$$
4. **Live Migration Pre-Copy Convergence Criterion:**
   $$D < R$$
   *(Memory dirtying rate $D$ must be strictly less than network transmission rate $R$).*
5. **Power Usage Effectiveness (PUE) & DCiE:**
   $$\text{PUE} = \frac{P_{\text{Total}}}{P_{\text{IT}}}, \qquad \text{DCiE} = \frac{1}{\text{PUE}} \times 100\%$$
6. **CMOS Dynamic Power Dissipation (DVFS):**
   $$P_{\text{dynamic}} = C \cdot V^2 \cdot f$$
7. **Serverless FaaS Execution Cost:**
   $$\text{Total Cost} = N_{\text{req}} \times C_{\text{req}} + \sum (M_i \times T_i) \times C_{\text{GB-sec}}$$
8. **Composite 3-Axis Acceleration Magnitude:**
   $$A = \sqrt{x^2 + y^2 + z^2}$$

---

## Repository Structure

```text
├── index.html                   # Central Exam Portal & Quiz Hub
├── quiz_week01.html             # Interactive Quiz — Week 1 (30 Qs)
├── quiz_week02.html             # Interactive Quiz — Week 2 (30 Qs)
├── quiz_week03.html             # Interactive Quiz — Week 3 (30 Qs)
├── quiz_week04.html             # Interactive Quiz — Week 4 (30 Qs)
├── quiz_week05.html             # Interactive Quiz — Week 5 (30 Qs)
├── quiz_week06.html             # Interactive Quiz — Week 6 (30 Qs)
├── quiz_week07.html             # Interactive Quiz — Week 7 (30 Qs)
├── quiz_week08.html             # Interactive Quiz — Week 8 (30 Qs)
├── quiz_week09.html             # Interactive Quiz — Week 9 (30 Qs)
├── quiz_week10.html             # Interactive Quiz — Week 10 (30 Qs)
├── quiz_week11.html             # Interactive Quiz — Week 11 (30 Qs)
├── quiz_week12.html             # Interactive Quiz — Week 12 (30 Qs)
├── comprehensive_notes.pdf      # 136-page complete textbook & study guide
├── comprehensive_notes.tex      # Master LaTeX document source
├── parts/                       # Modular LaTeX chapter files (Weeks 1--12)
├── quiz_data/                   # Python question data sources (360 Qs total)
├── build_all_weekly_quizzes.py  # Automation script for quiz generation
├── vercel.json                  # Vercel deployment configuration
├── .gitignore                   # Git exclusion rules
├── Week-01.pdf ... Week-12.pdf  # Original NPTEL lecture slides
└── Assignment 1.pdf ... 10.pdf  # Original NPTEL assignments
```

---

## Acknowledgments & Credits

* **Course Instructor:** Prof. Soumya K. Ghosh, Department of Computer Science & Engineering, IIT Kharagpur.
* **Platform:** National Programme on Technology Enhanced Learning (NPTEL), Ministry of Education, Government of India.
* All intellectual property rights of lecture slides and assignment questions belong to NPTEL and IIT Kharagpur. This repository is prepared for academic study, educational revision, and examination preparation purposes.
