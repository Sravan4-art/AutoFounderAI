import streamlit as st
from agents.supervisor import run_business
from memory.sqlite_memory import get_projects

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AutoFounder AI",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("AutoFounder AI")

st.sidebar.info("""
AI Startup Builder

✓ Market Research
✓ Branding
✓ Finance
✓ Marketing
✓ Strategy
✓ CEO Review
✓ Startup Score
✓ Investor Review
✓ Website
""")

st.sidebar.subheader("History")

if st.sidebar.button("Show Previous Startups"):
    st.sidebar.write(get_projects())

# -----------------------------
# Main UI
# -----------------------------

st.title("AutoFounder AI")

business = st.text_input(
    "Business Idea",
    placeholder="Example: AI Fitness App"
)

budget = st.number_input(
    "Budget",
    min_value=0.0,
    value=50000.0
)

# -----------------------------
# Generate
# -----------------------------

if st.button("Generate Startup"):

    if not business.strip():

        st.warning(
            "Please enter a business idea."
        )

    else:

        with st.spinner(
            "AI Agents Building Startup..."
        ):

            result = run_business(
                business,
                budget
            )

        # -------------------------
        # Tabs
        # -------------------------

        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(
            [
                "Market",
                "Branding",
                "SWOT",
                "Finance",
                "Marketing",
                "Strategy",
                "CEO",
                "Investor",
                "Improvements",
                "Business Plan"
            ]
        )

        with tab1:
            st.write(result["market"])

        with tab2:
            st.write(result["branding"])

        with tab3:
            st.write(result["swot"])

        with tab4:
            st.write(result["finance"])

        with tab5:
            st.write(result["marketing"])

        with tab6:
            st.write(result["strategy"])

        with tab7:
            st.write(result["ceo_review"])

            if "score" in result:
                st.subheader("Startup Score")
                st.write(result["score"])

        with tab8:
            if "investor" in result:
                st.write(result["investor"])
        
        with tab9:
            st.write(
                result["improvements"]
            )

        with tab10:
                st.write(result["business_plan"])

        # -------------------------
        # Download Buttons
        # -------------------------

        report_text = f"""
        MARKET

        {result.get('market', '')}

        BRANDING

        {result.get('branding', '')}

        FINANCE

        {result.get('finance', '')}

        MARKETING

        {result.get('marketing', '')}

        STRATEGY

        {result.get('strategy', '')}

        CEO REVIEW

        {result.get('ceo_review', '')}

        STARTUP SCORE

        {result.get('score', '')}

        INVESTOR REVIEW

        {result.get('investor', '')}

        BUSINESS PLAN

        {result.get('business_plan', '')}
        """

        # TXT Report
        st.download_button(
            label="📥 Download Report",
            data=report_text,
            file_name="startup_report.txt",
            mime="text/plain"
        )

        # PDF Proposal
        if "pdf_file" in result:

            try:

                with open(
                    result["pdf_file"],
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="Download PDF Proposal",
                        data=pdf_file.read(),
                        file_name="startup_proposal.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.warning(
                    f"PDF file unavailable: {e}"
                )
