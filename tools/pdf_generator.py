
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)
from xml.sax.saxutils import escape
import os


def generate_pdf(file_path, business_name, report):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    doc = SimpleDocTemplate(
        file_path,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=20,
        alignment=TA_CENTER,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=13,
        spaceBefore=12,
        spaceAfter=8
    )

    body_style = ParagraphStyle(
        "BodyTextCustom",
        parent=styles["BodyText"],
        fontSize=9,
        leading=13,
        spaceAfter=5,
        splitLongWords=1
    )

    story = []

    story.append(
        Paragraph(
            escape(str(business_name)) + " - Business Report",
            title_style
        )
    )

    story.append(Spacer(1, 10))

    # Convert Markdown output into safe PDF text
    report_text = str(report)

    for line in report_text.splitlines():

        line = line.strip()

        if not line:
            story.append(Spacer(1, 5))
            continue

        # Skip Markdown table separators
        if line.startswith("|") and all(
            char in "|-: " for char in line
        ):
            continue

        # Remove Markdown heading symbols
        clean_line = line.lstrip("#").strip()

        # Remove basic Markdown bold and italic markers
        clean_line = clean_line.replace("**", "")
        clean_line = clean_line.replace("*", "")

        # Escape HTML/XML characters to prevent ReportLab errors
        safe_line = escape(clean_line)

        # Highlight section headings
        if (
            clean_line.isupper()
            and len(clean_line) < 80
        ):
            story.append(
                Paragraph(safe_line, heading_style)
            )
        else:
            story.append(
                Paragraph(safe_line, body_style)
            )

    doc.build(story)

    return file_path
