from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "AI Generated Article", ln=True, align="C")
        self.ln(5)

def create_pdf(text, filename="output.pdf"):
    pdf = PDF()
    pdf.add_page()
    
    pdf.set_font("Arial", size=12)

    for line in text.split("\n"):
        if line.strip().isupper():  # headings
            pdf.set_font("Arial", "B", 14)
            pdf.ln(5)
        else:
            pdf.set_font("Arial", size=12)

        pdf.multi_cell(0, 8, line)

    pdf.output(filename)