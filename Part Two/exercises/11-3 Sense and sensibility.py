from PyPDF2 import PdfReader

frequency_table = {}

book = PdfReader("Book.pdf")

for page in book.pages:
    for word in page.extract_text().split():
        frequency_table[word] = frequency_table.get(word, 0) + 1


