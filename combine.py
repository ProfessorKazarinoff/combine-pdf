# combine.py
"""
A Python script to combine pdf's. Uses PyPDF2.
$ pip install PyPDF2
change the file names as needed
$ python combine.py
"""

import sys
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

    # set output file path
    output = 'merged.pdf'

    # delete first arg which is executable itself
    del sys.argv[0]

    # print what's going to happen
    print("Merging ", end='')
    for arg in sys.argv:
        print(arg, "", end='')
    print("into", output)

    # merge all files in argv via function call
    try:
        merge_pdfs(sys.argv, output)
    except:
        sys.exit("invalid filename(s)")
