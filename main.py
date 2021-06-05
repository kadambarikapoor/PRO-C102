import os
from fpdf import FPDF
pdf = FPDF()
pdf.set_auto_page_break(0)
dir = input('Enter the directory of the folder which has the images: ')
pdfName = input('Name of the pdf: ')
f = os.walk(dir)

for address, _, files in f:
    for file in files:
        pdf.add_page()
        pdf.image(address + '\\' + file)

pdf.output(address + '\\' + pdfName + ".pdf", "F")
