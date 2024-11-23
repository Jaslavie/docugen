import os
import sys
from pathlib import Path
from pdf_convert import pdf_to_text

# read the dataset folder
dat_dir = "data"
files = os.listdir(dat_dir)  # read all files in the dataset folder
print(files)
# converts all pdf files to text and stores them in an array
texts = [pdf_to_text(Path(dat_dir, file).read_bytes()) for file in files if file.endswith('.pdf')]

print(texts)

# fine-tune the model
# response = openai.beta.fineTuning.jobs.create({
# })
