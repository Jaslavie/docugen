
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

def text_to_jsonl(texts: list[str], output_file: str = "training_data.jsonl") -> str:
    """
    convert text array to a jsonl file and save it to the output file
    """
    prompts = [
        "Design a comprehensive document including logistics, schedules, and guidelines for the UCI Design-a-thon event.",
        "Design a document for participants including detailed logistics and schedules for the entire event.",
        "Create a schedule section for the Design-a-thon event.",
        "Explain the logistics and venue information for the Design-a-thon.",
        "Detail the rules and guidelines for Design-a-thon participants.",
        "Describe the judging process and criteria for the Design-a-thon.",
        "List the prizes and awards for Design-a-thon winners.",
        "Explain the mentor roles and support system in the Design-a-thon.",
        "Detail the check-in process and requirements for the Design-a-thon.",
        "Describe the food and accommodation arrangements for the event.",
        "Explain the communication channels and contact information.",
        "Detail the technical requirements and tools needed for participation."
    ]
    with open(output_file, 'w') as f:
        for text in texts:
            for prompt in prompts:
                # Give an example of the required format 
                training_example = {
                "messages": [
                    {"role": "system", "content": "You are a documentation specialist that writes documents for a designathon at UCI."},
                    {"role": "user", "content": prompt},
                    {"role": "assistant", "content": text}
                ]
            }
            # write the each training example to a new line in the jsonl file
            f.write(json.dumps(training_example) + '\n')

    return output_file
