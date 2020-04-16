# combine.py
"""
A Python script to combine pdf's. Uses PyPDF2.
$ pip install PyPDF2
change the file names as needed
$ python combine.py
"""

from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    # Create the writer object
    pdf_writer = PdfFileWriter()

    # Loop over the pages
    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['file1.pdf', 'file2.pdf']
    merge_pdfs(paths, output='merged.pdf')
