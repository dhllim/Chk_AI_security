# AI Security & Governance Control Dashboard

🛡️ **A comprehensive AI risk management and security compliance tool aligned with Singapore's latest frameworks.**

This dashboard provides organizations with a structured way to assess their AI governance maturity against the de-facto standards in Singapore, including **MAS FEAT**, the **MAS 2025 AI Risk Guidelines**, **IMDA Model Framework**, and **CSA Guidelines**.

## 🚀 Key Features

- **15-Control Assessment**: A deep-dive questionnaire covering Governance, Lifecycle, Security, Transparency, Monitoring, and Audit.
- **Detailed Guidance**: Each control includes interactive explanations ("ℹ️ Detailed Explanation") with regulatory rationale and implementation examples (e.g., "SHAP", "Model Cards", "AI Risk Committees").
- **Maturity Ranking**: Readiness score (0-100%) and color-coded rankings (Platinum to Bronze).
- **Transformation Roadmap**: Strategic recommendations and indicative corporate implementation costs (SGD/USD).
- **Official Resources**: Direct links to official MAS, IMDA, and CSA guidelines.
- **Export Power**: Download your full assessment and implementation plan as a CSV.

## 🛠️ Quick Start

### 1. Prerequisites
- [Conda](https://docs.conda.io/en/latest/miniconda.html) installed.
- Access to the internet for live exchange rate updates and framework links.

### 2. Setup Environment
```bash
# Create and activate the conda environment
conda create -n chkaisecurity python=3.9
conda activate chkaisecurity

# Install dependencies
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run app.py
```

## 📋 Framework Alignment
- **MAS FEAT Principles**: Fairness, Ethics, Accountability, and Transparency in Financial AI.
- **MAS 2025 Guidelines**: Latest supervisory expectations for AI risk management in FIs.
- **IMDA Model Framework**: National guidelines for ethical and responsible AI.
- **CSA Singapore**: Guidance on securing AI against adversarial ML and supply chain threats.

## 📥 Downloadable Reports
The application allows you to download a complete **Assessment & Recommendation Report** in CSV format, ready for internal stakeholder review or auditor evidence.

---
Developed for **Chk AI Security** - Enhancing trust and safety in AI ecosystems.
