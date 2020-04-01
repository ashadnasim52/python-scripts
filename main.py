import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combine(pdf_lists):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_lists:
        merger.append(pdf)
    merger.write('super.pdf')


if __name__ == "__main__":
    pdf_combine(inputs)
