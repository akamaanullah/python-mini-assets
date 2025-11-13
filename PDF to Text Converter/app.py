import PyPDF2

def pdf_to_text(pdf_file):
    with open(pdf_file, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text() + "\n"

    with open("output.txt", "w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    
    print("PDF text saved to output.txt")

pdf_to_text("response.pdf")
