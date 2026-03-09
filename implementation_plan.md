# Enhancement Plan: Advanced Dashboard Features

This plan outlines the enhancements to `app.py` to support multiple currencies, assess solution viability via a questionnaire, and include real-world reference cases.

## Proposed Changes

### [Component] AI Security Dashboard

#### [MODIFY] [app.py](file:///wsl.localhost/Ubuntu/home/dhllim/Chk_AI_security/app.py)

1. **Currency Toggle**:
   - Add a `selectbox` in the sidebar to toggle between **SGD** and **USD**.
   - Refactor `pricing_range` in the data structure to store base numeric values (e.g., in USD) and convert them dynamically based on the selected currency (using an assumed exchange rate, e.g., 1 USD = 1.35 SGD).

2. **Viability Questionnaire**:
   - Add a "Solution Readiness Questionnaire" section in the sidebar.
   - Example Questions:
     - Deployment Environment (Cloud, On-Premise, Hybrid)
     - Data Sensitivity (Highly Confidential/PII, Internal, Public)
   - Based on user selections, display a **"Viability & Workability Check"** dynamically in each control's expander (e.g., "Highly viable for Cloud environments").

3. **Reference Cases**:
   - Add a `reference_cases` list to each control in `controls_data`.
   - Examples will include anonymized industry implementations (e.g., "A leading APAC regional bank implemented IBM Guardium to comply with MAS TRM...").
   - Display these Reference Cases in the main content expanders.

4. **CSV Export Updates**:
   - Automatically format the pricing correctly in the CSV based on the selected currency.
   - Include the Reference Cases in the exported rows.

## Verification Plan

### Automated/Local Tests
- Run `streamlit run app.py` locally and verify the UI updates correctly.
- Test the SGD/USD currency toggle and verify the calculated totals.
- Select different answers in the questionnaire and verify the viability texts change accordingly.

### Manual Verification
- Review the exported CSV to ensure the new columns and calculated pricing are accurate.
- Verify the professional appearance of the reference cases.
