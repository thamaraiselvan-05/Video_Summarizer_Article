from fpdf import FPDF

# ---------- CLEAN TEXT (Fix Unicode Issue) ----------
def clean_text(text):
    replacements = {
        "–": "-",   # en dash
        "—": "-",   # em dash
        "‘": "'",   # left quote
        "’": "'",   # right quote
        "“": '"',   # left double quote
        "”": '"',   # right double quote
        "•": "-",   # bullet
    }

    for key, value in replacements.items():
        text = text.replace(key, value)

    return text.encode("latin-1", "ignore").decode("latin-1")


# ---------- CUSTOM PDF CLASS ----------
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(13, 71, 161)  # Blue tone
        self.cell(0, 10, "AI Generated Article", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(150)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


# ---------- CREATE PDF ----------
def create_pdf(text, filename="output.pdf"):
    pdf = PDF()
    pdf.add_page()

    # Clean text BEFORE processing
    text = clean_text(text)

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            pdf.ln(4)
            continue

        # ---------- TITLE ----------
        if line.startswith("TITLE"):
            pdf.set_font("Arial", "B", 16)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(5)

        # ---------- HEADINGS ----------
        elif line.isupper():
            pdf.set_font("Arial", "B", 14)
            pdf.set_text_color(13, 71, 161)  # Blue
            pdf.ln(4)

        # ---------- BULLET POINTS ----------
        elif line.startswith("-") or line.startswith("•"):
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(0, 0, 0)
            line = "• " + line.lstrip("-• ").strip()

        # ---------- NORMAL TEXT ----------
        else:
            pdf.set_font("Arial", size=12)
            pdf.set_text_color(0, 0, 0)

        pdf.multi_cell(0, 8, line)

    pdf.output(filename)