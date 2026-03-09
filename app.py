import streamlit as st
import pandas as pd
import requests
from datetime import datetime

st.set_page_config(
    page_title="AI Security & Governance Control Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Fetch Live Exchange Rate ---
@st.cache_data(ttl=3600)
def get_exchange_rate():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5)
        data = response.json()
        return data['rates']['SGD'], datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return 1.35, "Fallback (Network Error)"

sgd_rate, rate_timestamp = get_exchange_rate()

# --- CSS for Custom Styling ---
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6
    }
    .big-font {
        font-size:32px !important;
        font-weight: bold;
        color: #0e1117;
        margin-bottom: 5px;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f8f9fa;
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff4b4b !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# --- GOVERNANCE RESOURCES ---
all_resources = {
    "Singapore": {
        "MAS – FEAT Principles": "https://www.mas.gov.sg/-/media/MAS/News-and-Publications/Monographs-and-Information-Papers/FEAT-Principles-Updated-7-Feb-19.pdf",
        "MAS – AI Risk Management Guidelines (2025)": "https://www.mas.gov.sg/publications/consultations/2025/consultation-paper-on-guidelines-on-artificial-intelligence-risk-management",
        "IMDA / PDPC – Model AI Governance Framework": "https://www.pdpc.gov.sg/-/media/Files/PDPC/PDF-Files/Resource-for-Organisation/AI/SGModelAIGovFramework2.pdf",
        "CSA Singapore – Securing AI Systems": "https://www.csa.gov.sg/resources/publications/guidelines-and-companion-guide-on-securing-ai-systems"
    },
    "Global Best Practice (NIST/ISO)": {
        "NIST AI Risk Management Framework (AI RMF 1.0)": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
        "ISO/IEC 42001:2023 - AI Management System": "https://www.iso.org/standard/81230.html",
        "OECD AI Principles": "https://oecd.ai/en/ai-principles"
    }
}

# --- CONTROL DATA SETS ---
all_controls = {
    "Singapore": {
        "A. Governance & Oversight": [
            {
                "id": "SG-C1",
                "name": "AI Governance Committee",
                "requirement": "Establish an AI governance board; define roles (model owner, validator, risk manager, compliance).",
                "why": "MAS requires clear accountability structures.",
                "implementation": "AI Risk Committee / Model Risk Management Committee",
                "recommendation": "Set up a cross-functional AI Governance board with C-suite oversight.",
                "cost_usd": (5000, 15000)
            },
            {
                "id": "SG-C2",
                "name": "AI Policy Framework",
                "requirement": "Document ethical principles, acceptable use, and model risk classification.",
                "why": "Ensures organizational alignment and compliance.",
                "implementation": "AI Ethical Policy, Responsible AI Principles",
                "recommendation": "Develop and mandate an AI Ethics and Acceptable Use policy.",
                "cost_usd": (8000, 20000)
            },
            {
                "id": "SG-C3",
                "name": "AI Risk Appetite Statement",
                "requirement": "Define acceptable AI risk levels and prohibited use cases.",
                "why": "Establishes guardrails for AI innovation.",
                "implementation": "Risk Matrix (Low: Chatbot, High: Credit Scoring)",
                "recommendation": "Define explicit risk thresholds for different classes of AI models.",
                "cost_usd": (3000, 10000)
            }
        ],
        "B. AI Lifecycle Risk": [
            {
                "id": "SG-C4",
                "name": "AI Model Inventory",
                "requirement": "Maintain registry: owner, data sources, risk rating, validation history.",
                "why": "Ensures visibility and traceability.",
                "implementation": "Enterprise Model Registry (e.g., MLflow, SageMaker)",
                "recommendation": "Implement a centralized 'Model Card' registry for all active models.",
                "cost_usd": (10000, 30000)
            },
            {
                "id": "SG-C5",
                "name": "Data Governance Control",
                "requirement": "Data lineage, quality validation, bias assessment, PDPA compliance.",
                "why": "Garbage in, garbage out; ensures data integrity.",
                "implementation": "Data Drift Monitoring, Bias Testing Tools",
                "recommendation": "Deploy automated data quality and bias scanning for training sets.",
                "cost_usd": (15000, 45000)
            },
            {
                "id": "SG-C6",
                "name": "Model Validation",
                "requirement": "Independent validation of bias, accuracy, explainability, and fairness.",
                "why": "Preventing model failure and unintended bias.",
                "implementation": "SHAP, LIME, Adversarial Testing",
                "recommendation": "Enforce mandatory third-party or independent internal model validation.",
                "cost_usd": (20000, 60000)
            }
        ],
        "C. AI Security (CSA Singapore)": [
            {
                "id": "SG-C7",
                "name": "Secure AI Development",
                "requirement": "Secure coding, dependency scanning, model supply chain security.",
                "why": "Protects against supply chain attacks.",
                "implementation": "SBOM for ML models, Container Scanning",
                "recommendation": "Integrate ML-specific vulnerability scanning into DevSecOps.",
                "cost_usd": (12000, 35000)
            },
            {
                "id": "SG-C8",
                "name": "Adversarial Attack Protection",
                "requirement": "Adversarial testing, input validation, poisoning detection.",
                "why": "Defends against prompt injection and model inversion.",
                "implementation": "Prompt Sanitization, Input Filtering APIs",
                "recommendation": "Deploy a specialized AI Firewall or Guardrail API.",
                "cost_usd": (25000, 75000)
            },
            {
                "id": "SG-C9",
                "name": "Access Control for AI",
                "requirement": "RBAC for model usage, API authentication, inference logging.",
                "why": "Prevents unauthorized access to models and weights.",
                "implementation": "API Gateway, IAM Integration",
                "recommendation": "Enforce Zero-Trust access and JIT permissions for ML pipelines.",
                "cost_usd": (8000, 25000)
            }
        ],
        "D. Transparency & Explainability": [
            {
                "id": "SG-C10",
                "name": "Explainability",
                "requirement": "Provide human-understandable explanations for AI decisions.",
                "why": "Regulatory requirement for high-stakes decisions.",
                "implementation": "XAI Dashboards (Income, Credit Score impact)",
                "recommendation": "Implement explainability modules for all customer-facing AI.",
                "cost_usd": (15000, 40000)
            }
        ],
        "E. Monitoring & Incident Management": [
            {
                "id": "SG-C12",
                "name": "AI Monitoring",
                "requirement": "Continuous tracking of drift, degradation, and bias changes.",
                "why": "Detects performance drops in real-time.",
                "implementation": "Performance Alerts (e.g., accuracy < 85%)",
                "recommendation": "Deploy real-time drifting and bias monitoring agents.",
                "cost_usd": (10000, 35000)
            }
        ]
    },
    "Global Best Practice (NIST/ISO)": {
        "1. Governance (ISO 42001 A.2/A.3)": [
            {
                "id": "GP-C1",
                "name": "Leadership & AI Policy",
                "requirement": "Establish management commitment and organizational policies for AI.",
                "why": "Foundational for any management system (ISO 42001).",
                "implementation": "Corporate AI Ethics Board, AI Policy Document",
                "recommendation": "Formalize AI governance at the board level.",
                "cost_usd": (7000, 18000)
            }
        ],
        "2. Risk Mapping (NIST Map)": [
            {
                "id": "GP-C2",
                "name": "Contextual Risk Assessment",
                "requirement": "Identify AI risks in the specific business context and impact on stakeholders.",
                "why": "NIST AI RMF prioritizes understanding context first.",
                "implementation": "AI Impact Assessment (AIIA) process",
                "recommendation": "Conduct a mandatory 'Map' exercise for every new AI project.",
                "cost_usd": (5000, 12000)
            }
        ],
        "3. Data Governance (ISO 42001 A.7)": [
            {
                "id": "GP-C3",
                "name": "Data Quality & Provenance",
                "requirement": "Ensure data used for training is high quality, representative, and traceable.",
                "why": "Essential to mitigate bias and ensure model integrity.",
                "implementation": "Automated Data Lineage tracking, Bias Scanners",
                "recommendation": "Implement automated data quality checks in the feature engineering pipeline.",
                "cost_usd": (12000, 35000)
            }
        ],
        "4. Lifecycle Security (ISO 42001 A.6)": [
            {
                "id": "GP-C4",
                "name": "Secure AI Development",
                "requirement": "Apply security controls throughout the AI lifecycle (design, build, deploy).",
                "why": "Unified approach to AI system security.",
                "implementation": "DevSecOps for ML (MLSecOps), SBOM for models",
                "recommendation": "Incorporate automated model-scanning into CI/CD pipelines.",
                "cost_usd": (15000, 40000)
            }
        ],
        "5. Measurement (NIST Measure)": [
            {
                "id": "GP-C5",
                "name": "Trustworthiness Metrics",
                "requirement": "Identify and track metrics for accuracy, bias, safety, and robustness.",
                "why": "Quantifying risk is key to managing it (NIST).",
                "implementation": "Model Monitoring Dashboards, Stress Testing",
                "recommendation": "Standardize 'Trustworthiness KPIs' for all production models.",
                "cost_usd": (10000, 25000)
            }
        ],
        "6. Human Oversight (ISO 42001 A.9)": [
            {
                "id": "GP-C6",
                "name": "Human-in-the-Loop Controls",
                "requirement": "Ensure appropriate level of human oversight for high-stakes outcomes.",
                "why": "Critical requirement to prevent autonomous failure.",
                "implementation": "Decision override workflows, Human Review Queues",
                "recommendation": "Designate 'Human Override' protocols for critical AI-driven decisions.",
                "cost_usd": (8000, 20000)
            }
        ],
        "7. Monitoring & Management (NIST Manage)": [
            {
                "id": "GP-C7",
                "name": "Continuous Monitoring & Incident Response",
                "requirement": "Perform ongoing monitoring and have a plan for AI-related incidents.",
                "why": "Ensures models stay safe and accurate over time.",
                "implementation": "Model Drift Alerts, AI Incident Runbooks",
                "recommendation": "Integrate AI model failures into existing SOC/NOC monitoring.",
                "cost_usd": (10000, 30000)
            }
        ]
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/shield.png", width=60)
    st.markdown("### **Dashboard Settings**")
    
    # Country Selection
    country_list = ["Singapore", "United States", "United Kingdom", "European Union", "Australia", "Other (Global Fallback)"]
    selected_country = st.selectbox("Select Country/Region:", country_list)
    
    # Determine Framework
    if selected_country == "Singapore":
        active_framework = "Singapore"
    else:
        active_framework = "Global Best Practice (NIST/ISO)"
        st.warning(f"Using Global Best Practice fallback for {selected_country}.")
    
    currency = st.radio("Display Currency:", ("SGD", "USD"))
    mult = sgd_rate if currency == "SGD" else 1.0
    cur_sym = "S$" if currency == "SGD" else "$"
    
    st.divider()
    st.markdown(f"### **{active_framework} Resources**")
    for name, url in all_resources[active_framework].items():
        st.markdown(f"📥 [{name}]({url})")
    
    st.divider()
    st.caption(f"Live SGD Rate: **{sgd_rate:.3f}** (USD to SGD)")
    st.caption(f"Last sync: `{rate_timestamp}`")

# --- DATA ASSIGNMENT ---
controls_data = all_controls[active_framework]

# --- MAIN PAGE ---
st.markdown('<p class="big-font">🛡️ AI Governance & Security Dashboard</p>', unsafe_allow_html=True)
st.markdown("**Empowering organizations with Singapore-aligned AI Risk Management and Security Controls.**")
st.divider()

# --- NAVIGATION ---
tab1, tab2, tab3 = st.tabs(["🏛️ AI Governance Assessment", "📋 Control Library", "📊 Results & Implementation"])

# --- TAB 1: ASSESSMENT ---
with tab1:
    st.header("Step 1: Self-Assessment Questionnaire")
    st.info("Assess your posture across the 15 de-facto controls used in Singapore.")
    
    user_answers = {}
    
    for category, items in controls_data.items():
        with st.expander(f"**{category}**", expanded=True):
            for item in items:
                st.markdown(f"**{item['id']} - {item['name']}**")
                st.write(f"_{item['requirement']}_")
                
                # Detailed Explanation Feature
                with st.expander(f"ℹ️ Detailed Explanation for {item['id']}"):
                    st.markdown(f"**Why this is required:** {item['why']}")
                    st.markdown(f"**Specific Requirement:** {item['requirement']}")
                    st.markdown(f"**Implementation Example:** {item['implementation']}")
                
                user_answers[item['id']] = st.radio(
                    f"Current Status ({item['id']}):", 
                    ["No", "In-Progress", "Yes"], 
                    horizontal=True, 
                    key=f"ans_{item['id']}"
                )
                st.divider()

# --- TAB 2: LIBRARY ---
with tab2:
    st.header("Control Reference Library")
    st.write("Detailed breakdown of requirements and implementation examples mapping to MAS and CSA frameworks.")
    
    for category, items in controls_data.items():
        st.subheader(category)
        for item in items:
            with st.container(border=True):
                col_a, col_b = st.columns([1, 4])
                col_a.metric("ID", item['id'])
                col_b.markdown(f"### {item['name']}")
                st.markdown(f"**Requirement:** {item['requirement']}")
                st.markdown(f"**Why:** {item['why']}")
                st.info(f"**Implementation Example:** {item['implementation']}")

# --- TAB 3: RESULTS & RECOMMENDATIONS ---
with tab3:
    st.header("Step 2: Readiness & Recommendations")
    
    # --- Scoring ---
    val_map = {"No": 0, "In-Progress": 50, "Yes": 100}
    total_score = sum(val_map[ans] for ans in user_answers.values()) / len(user_answers)
    
    if total_score >= 90: ranking, color = "Platinum (Optimized)", "green"
    elif total_score >= 75: ranking, color = "Gold (Managed)", "blue"
    elif total_score >= 50: ranking, color = "Silver (Defined)", "orange"
    else: ranking, color = "Bronze (Foundational/Initial)", "red"
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"### Overall Ranking: <span style='color:{color}'>{ranking}</span>", unsafe_allow_html=True)
        st.progress(total_score / 100)
    with col2:
        st.metric("Readiness Score", f"{total_score:.0f}%")
        
    st.divider()

    # --- Recommendations & Costing ---
    st.subheader("💡 Strategic Recommendations & Implementation Proposal")
    
    proposal_data = []
    total_min, total_max = 0, 0
    
    for category, items in controls_data.items():
        cat_recs = []
        for item in items:
            ans = user_answers[item['id']]
            if ans != "Yes":
                min_p = int(item['cost_usd'][0] * mult)
                max_p = int(item['cost_usd'][1] * mult)
                total_min += min_p
                total_max += max_p
                
                cat_recs.append({
                    "Control": item['name'],
                    "Status": ans,
                    "Recommendation": item['recommendation'],
                    "Cost": f"{cur_sym}{min_p:,} - {cur_sym}{max_p:,}"
                })
        
        if cat_recs:
            st.markdown(f"#### {category}")
            df_cat = pd.DataFrame(cat_recs)
            st.table(df_cat)
            proposal_data.extend(cat_recs)
            
    if not proposal_data:
        st.success("🎉 All controls are 'Yes'! Your AI Governance is state-of-the-art.")
    else:
        st.divider()
        st.subheader("💰 Executive Summary of Investment")
        st.metric("Estimated Implementation Cost", f"{cur_sym}{total_min:,} - {cur_sym}{total_max:,}")
        st.caption("Pricing is based on commercially applicable enterprise solutions in Singapore.")
        
        # --- Download ---
        st.divider()
        df_final = pd.DataFrame(proposal_data)
        csv = df_final.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Detailed Recommendation Report (CSV)",
            data=csv,
            file_name='ai_governance_recs.csv',
            mime='text/csv',
        )
