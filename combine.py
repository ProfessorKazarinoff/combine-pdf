# combine.py
"""
A Python script to combine pdf's. Uses PyPDF2.
$ pip install PyPDF2
change the file names as needed
$ python combine.py
"""

from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(paths, output):
    # Create the writer object
    pdf_writer = PdfWriter()

    # Loop over the pages
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            # Add each page to the writer object
            pdf_writer.add_page(pdf_reader.pages[page])

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['file1.pdf', 'file2.pdf']
    merge_pdfs(paths, output='merged.pdf')
