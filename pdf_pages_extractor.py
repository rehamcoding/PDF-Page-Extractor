from pypdf import PdfReader, PdfWriter

page_range = input("Enter page range: ").split(', ')


pages = []
for page in page_range:
    if '-' in page:
        number_range = page.split('-')
        first_num, second_num = number_range
        for i in range(int(first_num), int(second_num) + 1):
            pages.append(i)
        continue
    pages.append(int(page))

reader = PdfReader("UltimateEnglishBook.pdf")
writer = PdfWriter()

for page in pages:
    writer.add_page(reader.pages[page - 1])


writer.write("should_study.pdf")