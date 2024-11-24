
from pdfminer.high_level import extract_text 
import json

def pdf_to_text(pdf_buffer: bytes) -> str:
    """ 
    extract the binary representation of the pdf file
    """
    text = ''
    with open('temp.pdf', 'wb') as temp_pdf: # write the pdf buffer to a temporary file
        temp_pdf.write(pdf_buffer)
    text = extract_text('temp.pdf')
    return text

def text_to_json(texts: list[str], output_file: str = "training_data.jsonl") -> str:
    """
    convert text array to a jsonl file and save it to the output file
    """
    with open(output_file, 'w') as f:
        for text in texts:
            # Give an example of the required format 
            training_example = {
                "messages": [
                    {"role": "system", "content": "You are a documentation specialist that writes documents for a designathon at UCI."},
                    {"role": "user", "content": "Design a document for participants including detailed logistics and schedules for the entire event."},
                    {"role": "assistant", "content": text}
            ]
        }
        # write each JSON object to a new line in the file
        f.write(json.dumps(training_example) + '\n')

    return output_file
