from fpdf import FPDF
import re


def clean_text(text):
    replacements = {
        "–": "-", "—": "-", "−": "-",
        "‘": "'", "’": "'",
        "“": '"', "”": '"',
        "•": "-", "…": "...",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text.encode("latin-1", "replace").decode("latin-1")


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "YouTube Article Generator", ln=True, align="C") 
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def create_pdf(article):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    lines = article.split("\n")

    for line in lines:
        line = clean_text(line.strip())

        if not line:
            pdf.ln(3)
            continue

        # 🔥 TITLE
        if "title" in line.lower():
            pdf.set_font("Arial", "B", 15)
            pdf.ln(4)
            pdf.multi_cell(0, 9, line.replace("**", ""))

        # 🔥 SECTION HEADINGS
        elif any(keyword in line.lower() for keyword in [
            "introduction", "key insights", "detailed explanation", "conclusion"
        ]):
            pdf.set_font("Arial", "B", 13)
            pdf.ln(4)
            pdf.multi_cell(0, 8, line.replace("**", ""))

        # 🔹 BULLETS
        elif line.startswith("*") or line.startswith("-"):
            pdf.set_font("Arial", "", 11)
            bullet = "- " + line.lstrip("*- ").strip()
            pdf.multi_cell(0, 7, bullet)

        # 🔹 NORMAL TEXT
        else:
            pdf.set_font("Arial", "", 11)
            pdf.multi_cell(0, 7, line)

    return pdf.output(dest="S").encode("latin-1")