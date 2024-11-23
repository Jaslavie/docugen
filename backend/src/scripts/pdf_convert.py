import asyncio
from pdfminer.high_level import extract_text_to_fp

# extract the binary representation of the pdf file
async def pdf_to_text(pdf_buffer: bytes) -> str:
    text = ''
    with open('temp.pdf', 'wb') as temp_pdf:
        temp_pdf.write(pdf_buffer)
    text = extract_text_to_fp('temp.pdf')
    return text