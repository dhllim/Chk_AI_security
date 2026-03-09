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
    "United Kingdom": {
        "UK AI Regulation White Paper": "https://www.gov.uk/government/publications/ai-regulation-a-pro-innovation-approach",
        "ICO – Guidance on AI and Data Protection": "https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/",
        "NCSC – Guidelines for Secure AI System Development": "https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development"
    },
    "Australia": {
        "Australia – AI Ethics Framework": "https://www.industry.gov.au/publications/australias-ai-ethics-framework",
        "Australia – Voluntary AI Safety Standard": "https://www.industry.gov.uk/publications/voluntary-ai-safety-standard",
        "ACSC – Security of AI": "https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/artificial-intelligence/security-ai"
    },
    "United States": {
        "NIST AI Risk Management Framework": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
        "Executive Order 14110 (Safe AI)": "https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/",
        "OMB – AI Gov in Federal Government": "https://www.whitehouse.gov/wp-content/uploads/2024/03/M-24-10-Advancing-Governance-Innovation-and-Risk-Management-for-Agency-Use-of-Artificial-Intelligence.pdf"
    },
    "Hong Kong": {
        "PCPD – Guidance on Ethical Development and Use of AI": "https://www.pcpd.org.hk/english/resources_centre/publications/files/guidance_ethical_e.pdf",
        "OGCIO – Ethical AI Framework": "https://www.ogcio.gov.hk/en/our_work/infrastructure/e-government/ethical_ai_framework/",
        "HKMA – AI in Financial Services": "https://www.hkma.gov.hk/media/eng/doc/key-functions/banking-stability/banking-policy/20191101e1.pdf"
    },
    "India": {
        "NITI Aayog – Strategy for Responsible AI": "https://niti.gov.in/sites/default/files/2021-02/Responsible-AI-22022021.pdf",
        "IndiaAI – Governance & Policy": "https://indiaai.gov.in/governance",
        "MeitY – AI Mission Guidelines": "https://www.meity.gov.in/content/artificial-intelligence"
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
    "United Kingdom": {
        "Governance & Accountability": [
            {
                "id": "UK-C1",
                "name": "Accountability & Governance",
                "requirement": "Clear lines of accountability and defined roles throughout the AI lifecycle.",
                "why": "White Paper requirement for robust governance.",
                "implementation": "AI Ethics Committee, Senior Management Accountability",
                "recommendation": "Appoint a Senior Responsible Officer for AI systems.",
                "cost_usd": (10000, 25000)
            }
        ],
        "Safety & Security": [
            {
                "id": "UK-C2",
                "name": "Safety, Security & Robustness",
                "requirement": "Ensure AI operates reliably and is protected against cyber threats.",
                "why": "Core UK principle for pro-innovation regulation.",
                "implementation": "Red-teaming, Secure AI Development Lifecycle (SALC)",
                "recommendation": "Apply NCSC guidelines for secure AI development.",
                "cost_usd": (15000, 45000)
            }
        ],
        "Transparency": [
            {
                "id": "UK-C3",
                "name": "Appropriate Transparency",
                "requirement": "Communicate clearly when AI is being used and how decisions are made.",
                "why": "Ensures stakeholders understand AI outcomes.",
                "implementation": "Transparency reports, Explainability (XAI) modules",
                "recommendation": "Implement context-specific explainability for all public-facing AI.",
                "cost_usd": (8000, 20000)
            }
        ],
        "Fairness & Redress": [
            {
                "id": "UK-C4",
                "name": "Fairness & Contestability",
                "requirement": "Avoid unlawful discrimination and provide mechanisms for redress.",
                "why": "Protects individuals from biased AI outcomes.",
                "implementation": "Bias audits, Grievance redressal process",
                "recommendation": "Establish a formal process for individuals to challenge AI decisions.",
                "cost_usd": (12000, 30000)
            }
        ]
    },
    "Australia": {
        "Governance & Values": [
            {
                "id": "AU-C1",
                "name": "Human-Centred Values",
                "requirement": "Align AI with human rights, diversity, and individual autonomy.",
                "why": "Core requirement of Australia AI Ethics Framework.",
                "implementation": "Human Rights Impact Assessment",
                "recommendation": "Integrate ethical reviews into the procurement process.",
                "cost_usd": (6000, 15000)
            }
        ],
        "Privacy & Security": [
            {
                "id": "AU-C2",
                "name": "Privacy Protection & Security",
                "requirement": "Ensure data protection and security throughout the lifecycle.",
                "why": "Critical for public trust in AI.",
                "implementation": "Enhanced encryption, JIT access for ML data",
                "recommendation": "Implement ACSC's Essential Eight for all AI infrastructure.",
                "cost_usd": (10000, 30000)
            }
        ],
        "Reliability & Safety": [
            {
                "id": "AU-C3",
                "name": "Reliability & Safety",
                "requirement": "AI should operate as intended and minimize safety risks.",
                "why": "Protects society and environment from malfunctions.",
                "implementation": "Continuous performance testing, Guardrails",
                "recommendation": "Adopt the Voluntary AI Safety Standard for high-risk models.",
                "cost_usd": (15000, 40000)
            }
        ],
        "Accountability": [
            {
                "id": "AU-C4",
                "name": "Accountability & Contestability",
                "requirement": "Identifiable responsibility and ability to challenge AI outcomes.",
                "why": "Ensures recourse for AI-impacted individuals.",
                "implementation": "Audit logging, Appeal mechanisms",
                "recommendation": "Deploy a 'Whistleblower' portal for reporting AI biases.",
                "cost_usd": (8000, 22000)
            }
        ]
    },
    "United States": {
        "Safety & Security (NIST)": [
            {
                "id": "US-C1",
                "name": "Safety & Security Evaluation",
                "requirement": "Robust evaluations including red-teaming for dual-use foundation models.",
                "why": "Executive Order 14110 requirement.",
                "implementation": "Automated Red-teaming, Safety testing reports",
                "recommendation": "Follow NIST AI 100-1 for risk mapping and measurement.",
                "cost_usd": (20000, 60000)
            }
        ],
        "Civil Rights & Fairness": [
            {
                "id": "US-C2",
                "name": "Algorithmic Discrimination Mitigation",
                "requirement": "Prevent and address bias in housing, hiring, and financial services.",
                "why": "High priority of the US federal government.",
                "implementation": "Fairness audits, Demographic parity dashboards",
                "recommendation": "Conduct civil rights impact assessments for all high-impact AI.",
                "cost_usd": (15000, 40000)
            }
        ],
        "Privacy & Data": [
            {
                "id": "US-C3",
                "name": "Data Privacy Protection",
                "requirement": "Uphold privacy rights and protect personally identifiable information (PII).",
                "why": "Protects against data misuse in AI training.",
                "implementation": "Differential Privacy, PII Scrubbing",
                "recommendation": "Implement NIST Privacy Framework alongside AI RMF.",
                "cost_usd": (12000, 35000)
            }
        ],
        "Accountability": [
            {
                "id": "US-C4",
                "name": "Chief AI Officer Oversight",
                "requirement": "Appoint leadership to oversee AI implementation and risk management.",
                "why": "Mandated for federal agencies; best practice for enterprise.",
                "implementation": "CAIO appointment, AI Governance Board",
                "recommendation": "Formalize the role of Chief AI Officer with board reporting.",
                "cost_usd": (10000, 30000)
            }
        ]
    },
    "Hong Kong": {
        "Accountability & Strategy": [
            {
                "id": "HK-C1",
                "name": "AI Strategy & Accountability",
                "requirement": "Establish clear strategy and senior management accountability.",
                "why": "PCPD Guidance on Ethical AI.",
                "implementation": "Strategic AI Governance Plan",
                "recommendation": "Define AI as a core pillar of the corporate governance framework.",
                "cost_usd": (8000, 20000)
            }
        ],
        "Ethical Principles": [
            {
                "id": "HK-C2",
                "name": "Data Stewardship Values",
                "requirement": "Adhere to values of being Respectful, Beneficial, and Fair.",
                "why": "PCPD fundamental values.",
                "implementation": "Ethics Review Board, CSR-AI alignment",
                "recommendation": "Conduct Ethical Impact Assessments (EIA) regularly.",
                "cost_usd": (5000, 15000)
            }
        ],
        "Privacy & Data": [
            {
                "id": "HK-C3",
                "name": "PDPO Compliance",
                "requirement": "Ensure compliance with Personal Data (Privacy) Ordinance in AI use.",
                "why": "Legal requirement in Hong Kong for data privacy.",
                "implementation": "Privacy Impact Assessments (PIA), Data minimize",
                "recommendation": "Map all cross-border data flows related to AI training.",
                "cost_usd": (10000, 30000)
            }
        ],
        "Human Oversight": [
            {
                "id": "HK-C4",
                "name": "Human Oversight & Transparency",
                "requirement": "Enable human-in-the-loop and provide explainable AI outcomes.",
                "why": "Prevents automated decisions with harmful impacts.",
                "implementation": "Human Review Interfaces, Traceable Decision Logs",
                "recommendation": "Implement clear levels of human intervention based on risk.",
                "cost_usd": (10000, 25000)
            }
        ]
    },
    "India": {
        "Inclusive Growth": [
            {
                "id": "IN-C1",
                "name": "Inclusivity & Non-discrimination",
                "requirement": "Ensure AI is accessible and does not discriminate against diverse fabric of India.",
                "why": "NITI Aayog 'AI for All' strategy.",
                "implementation": "Multi-language AI interfaces, Bias testing for local demographics",
                "recommendation": "Perform inclusivity audits to ensure representation in training data.",
                "cost_usd": (5000, 15000)
            }
        ],
        "Safety & Fairness": [
            {
                "id": "IN-C2",
                "name": "Safety, Reliability & Equality",
                "requirement": "Ensure systems are safe and promote fairness and equal opportunity.",
                "why": "Foundational principles for Responsible AI.",
                "implementation": "Robustness testing, Fairness dashboards",
                "recommendation": "Implement NITI Aayog's Responsible AI guidelines for specific sectors.",
                "cost_usd": (10000, 25000)
            }
        ],
        "Privacy & Transparency": [
            {
                "id": "IN-C3",
                "name": "Privacy, Security & Transparency",
                "requirement": "Uphold privacy rights and ensure transparency in AI decision mechanisms.",
                "why": "Foundational requirement for user trust.",
                "implementation": "DPDP Act compliance (upcoming), Explainability modules",
                "recommendation": "Prepare for Digital Personal Data Protection (DPDP) Act alignment.",
                "cost_usd": (12000, 35000)
            }
        ],
        "Operationalization": [
            {
                "id": "IN-C4",
                "name": "Accountability & Ethics by Design",
                "requirement": "Incentivize ethics by design and establish clear accountability.",
                "why": "Operationalizing Responsible AI (Part 2).",
                "implementation": "AI Ethics Checklists for Developers, Audit Trails",
                "recommendation": "Implement 'Ethics by Design' workflows in ML pipelines.",
                "cost_usd": (8000, 20000)
            }
        ]
    }
}

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://img.icons8.com/isometric/100/shield.png", width=60)
    st.markdown("### **Dashboard Settings**")
    
    # Country Selection
    country_list = [
        "Singapore", 
        "United Kingdom", 
        "Australia", 
        "United States", 
        "Hong Kong", 
        "India", 
        "Other (Global Fallback)"
    ]
    selected_country = st.selectbox("Select Country/Region:", country_list)
    
    # Determine Framework
    if selected_country in all_controls:
        active_framework = selected_country
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
