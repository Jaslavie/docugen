
from pdfminer.high_level import extract_text 

# extract the binary representation of the pdf file
def pdf_to_text(pdf_buffer: bytes) -> str:
    text = ''
    with open('temp.pdf', 'wb') as temp_pdf: # write the pdf buffer to a temporary file
        temp_pdf.write(pdf_buffer)
    text = extract_text('temp.pdf')
    return text