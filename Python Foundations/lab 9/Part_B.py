class Document:
    def __init__(self, title):
        self.title = title

    def describe(self):
        return f"{self.title} is a Document"


class PDFDocument(Document):
    def describe(self):
        return f"{self.title} is a PDF Document"


class TextDocument(Document):
    def describe(self):
        return f"{self.title} is a Text Document"


pdf_1 = PDFDocument("Python")
pdf_2 = PDFDocument("Java")
pdf_3 = PDFDocument("C")
text_1 = TextDocument("Syllabus")
text_2 = TextDocument("Rules and Regulations")
text_3 = TextDocument("Application")

documents = [pdf_1, text_1, pdf_2, text_2, pdf_3, text_3]

for doc in documents:
    print(f"Document : {doc.title}")
    print(f"Describe : {doc.describe()}\n")
