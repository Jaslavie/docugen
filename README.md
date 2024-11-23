### Project Setup

1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Set up environment variables
Include your OpenAI API key in the .env file named ```OPEN_AI_KEY```
```bash
cp .env
```

3. Run the server
```bash
python app.py
```
4. Generate a PDF
Enter a prompt in the text box and select the elements you want to include in the PDF. Then click the generate button.
Currently, only the markdown version is supported.
