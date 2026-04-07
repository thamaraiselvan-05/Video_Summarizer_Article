from fpdf import FPDF

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
        self.set_font("Arial", "B", 16)
        self.set_text_color(13, 71, 161)
        self.cell(0, 10, "AI Generated Article", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def create_pdf(text):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    text = clean_text(text)

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            pdf.ln(3)
            continue

        if line.lower().startswith("title"):
            pdf.set_font("Arial", "B", 16)
            pdf.multi_cell(0, 10, line.replace("TITLE:", "").strip())
            pdf.ln(3)

        elif line.isupper():
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(13, 71, 161)
            pdf.ln(2)
            pdf.multi_cell(0, 8, line)

        elif line.startswith("-") or line.startswith("•"):
            pdf.set_font("Arial", size=12)
            bullet = "- " + line.lstrip("-• ").strip()
            pdf.multi_cell(0, 7, bullet)

        else:
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 7, line)

    return pdf.output(dest="S").encode("latin-1")