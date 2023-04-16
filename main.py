from fpdf import FPDF
import pandas as pd


# create pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for item in range(row["Pages"]):
        pdf.add_page()
        # set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        #pdf.line(x1=10, y1=21, x2=200, y2=21)

        for i in range(20, 298, 10):
            pdf.set_draw_color(0, 0, 255)
            pdf.line(x1=10, y1=i, x2=200, y2=i)

        # set the footer
        pdf.ln(265)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(139, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        # alternate footer:
        # pdf.set_y(-15)
        # pdf.cell(0, -10, f"Page {pdf.page_no()}", align="R")

pdf.output("output.pdf")