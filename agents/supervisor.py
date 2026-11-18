from agents.market_agent import market_agent
from agents.branding_agent import branding_agent
from agents.finance_agent import finance_agent
from agents.marketing_agent import marketing_agent

from agents.strategy_agent import strategy_agent
from memory.sqlite_memory import save_project
import os
from agents.ceo_agent import ceo_agent
from tools.pdf_generator import generate_pdf
from agents.startup_score_agent import startup_score_agent
from agents.investor_agent import investor_agent
from agents.business_plan_agent import business_plan_agent
from agents.competitor_agent import competitor_agent
from agents.swot_agent import swot_agent


def safe_agent_call(func, *args):

    try:

        result = func(*args)

        if result is None:
            return "No response generated."

        return str(result)

    except Exception as e:

        print(f"Agent Error ({func.__name__}): {e}")

        return f"Agent Error: {e}"
    
def run_business(
        business,
        budget
):

    # Safe filename
    safe_name = business.replace(" ", "_")

    market = market_agent(business)

    competitor = competitor_agent(business)

    swot = swot_agent(
        business,
        market[:500],
        competitor[:500]
    )

    branding = branding_agent(
        business + "\n" + market[:500]
    )

    finance = finance_agent(
        business + "\n" + market[:500],
        budget
    )

    marketing = marketing_agent(
        business +
        "\n" +
        market[:500] +
        "\n" +
        branding[:500]
    )

    strategy = strategy_agent(
        market[:500],
        finance[:500],
        marketing[:500]
    )

    ceo_review = ceo_agent(
        market[:500],
        branding[:500],
        finance[:500],
        marketing[:500],
        strategy[:500]
    )

    score = startup_score_agent(
        market[:500],
        finance[:500],
        marketing[:500]
    )

    investor = safe_agent_call(
        investor_agent,
        market[:500],
        finance[:500],
        strategy[:500]
    )

    improvements = "Improvement system temporarily disabled."

    business_plan = safe_agent_call(
        business_plan_agent,
        market[:500],
        finance[:500],
        strategy[:500]
    )

    os.makedirs(
        "generated/reports",
        exist_ok=True
    )

    # Report
    report = f"""
MARKET RESEARCH

{market}

--------------------------------

COMPETITOR ANALYSIS

{competitor}

--------------------------------

SWOT ANALYSIS

{swot}

--------------------------------

BRANDING

{branding}

--------------------------------

FINANCE

{finance}

--------------------------------

MARKETING

{marketing}

--------------------------------

STRATEGY

{strategy}

--------------------------------

CEO REVIEW

{ceo_review}

--------------------------------

STARTUP SCORE

{score}

--------------------------------

INVESTOR REVIEW

{investor}

--------------------------------

BUSINESS PLAN

{business_plan}
"""

    # Save TXT Report
    with open(
        f"generated/reports/{safe_name}.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    # Generate PDF
    generate_pdf(
        f"generated/reports/{safe_name}.pdf",
        business,
        report
    )

    # Save Database
    save_project(
        business,
        report
    )

    return {
        "market": market,
        "competitor": competitor,
        "swot": swot,
        "branding": branding,
        "finance": finance,
        "marketing": marketing,
        "strategy": strategy,
        "ceo_review": ceo_review,
        "score": score,
        "investor": investor,
        "improvements": improvements,
        "business_plan": business_plan,
        "pdf_file": f"generated/reports/{safe_name}.pdf"
    }