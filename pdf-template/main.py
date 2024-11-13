from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(row["Pages"]):
        # Set page header
        pdf.add_page()
        pdf.set_font(family="Times", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        
        # Draws a line every 10mm
        for i in range(2, 30):
            x = 10 * i
            pdf.line(10, x, 200, x)
        
    
        # Set page footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
        
     


pdf.output("output.pdf")