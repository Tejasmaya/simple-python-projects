import PyPDF2

FILE_PATH = "C:\\Users\\Tejasmaya Sitha\\OneDrive\\Desktop\\Tejasmaya_Aadhar.pdf"  # give path of the file


with open(FILE_PATH, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)

    page = reader.getPage(0)

    print(page.extractText())

