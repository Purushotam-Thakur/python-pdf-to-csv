# Importing required modules
import PyPDF2
import csv
import re

row_dict = {
    'question': '',
    'option1': '',
    'option2': '',
    'option3': '',
    'option4': '',
    'answer': '',
    'explanation': '',
    'course/subject': '',
    'instruction': '',
    'tags(Coma Seprate)': '',
    'isShow': True,
}
next_is_question = False
header = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation',
          'course/subject', 'instruction', 'tags(Coma Seprate)', 'isShow']


def test_pdf():
    # Creating a pdf file object
    pdf_file_obj = open('./pdfFile/GS280.pdf', 'rb')

    # Creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    page_obj = pdf_reader.getPage(2)
    text = page_obj.extractText().split("\n \n")
    print("++++++++++++++++++")
    print(text)

    test_list = list(filter(None, text))
    print("=-=-=-=-=-=--=--=-=-=-=--=-=-=-=-")
    print(test_list)

    pdf_file_obj.close()


def read_pdf():
    global row_dict
    global next_is_question
    prev_line = ''
    current_line = ''

    # Creating a pdf file object
    pdf_file_obj = open('./pdfFile/GS280.pdf', 'rb')

    # Creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Getting number of pages in pdf file
    pages = pdf_reader.numPages
    csv_file = open('sample.csv', 'w', newline='')
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    # Loop for reading all the Pages
    for i in range(pages):

        # Creating a page object
        page_obj = pdf_reader.getPage(i)

        # Printing Page Number
        print("Page No: ", i)

        # Extracting text from page
        # And splitting it into chunks of lines
        text = page_obj.extractText().split("\n \n")

        # Finally the lines are stored into list
        # For iterating over list a loop is used
        print("++++++++++++++++++++++++++++++ =-=-==- len(text): ", len(text))
        for i in range(len(text)):
            prev_line = current_line
            prev_line = prev_line.replace("\n", "")
            current_line = text[i]
            # Printing the line

            if next_is_question:
                row_dict['question'] = text[i]
                next_is_question = False
                continue

            # Lines are separated using "\n"
            print("++++++++++++++++++++++++++++++")
            print(text[i], end="\n")
            if prepare_row(prev_line, current_line):
                writer.writerow(row_dict)

        # For Separating the Pages
        print("-=--=-=-==-=-=-----=--=-=-=-=-=--=--=-=-=-=--=")
    # closing the pdf file object
    pdf_file_obj.close()
    csv_file.close()


def prepare_row(prev_text, current_text):
    global row_dict
    global next_is_question
    if re.search("^Question No. 01", current_text):
        row_dict['course/subject'] = prev_text
        print(prev_text, '=-', current_text)
        print("Question No. 01=================")
        return False
    elif re.search("^Question No", current_text):
        next_is_question = True
        print("Question No=================")
        return False
    elif re.search('^\(A\)', current_text):
        print("(A)=================")
        row_dict['option1'] = current_text
        return False
    elif re.search('^\(B\)', current_text):
        row_dict['option2'] = current_text
        print("(B)=================")
        return False
    elif re.search('^\(C\)', current_text):
        row_dict['option3'] = current_text
        print("(C)=================")
        return False
    elif re.search('^\(D\)', current_text):
        row_dict['option4'] = current_text
        print("(D)=================")
        return False
    elif re.search("^Answer:", current_text):
        row_dict['answer'] = current_text
        print("answer=================")
        return True
    return False


# test_pdf()
read_pdf()
