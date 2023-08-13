from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        self.pdf = FPDF()
        self.pdf.add_page()
        self.pdf.set_font('helvetica', "B", size=50)
        self.pdf.cell(0, 60, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")
        self.pdf.image("shirtificate.png", h = 0, w = self.pdf.epw)
        self.pdf.set_font('helvetica', size=30)
        self.pdf.set_text_color(255,255,255)
        self.pdf.text(x = 51, y = 140, txt = f"{name} took CS50")
        self.pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = PDF(name)
