import os
from PyPDF2 import PdfMerger

source_dir = "./PDF_Files/"
merger = PdfMerger()

for item in os.listdir(source_dir):
    if item.endswith("pdf"):
        # print(item)
        merger.append(source_dir + item)

merger.write(source_dir + "Output/Complete.pdf")
merger.close()
