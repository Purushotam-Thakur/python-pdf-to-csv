# Importing required modules
import PyPDF2
import csv
import re
from nose.tools import assert_true

csv_file_name = 'Objective questions on disease topic.csv'

answer = {
    'A': 1,
    'B': 2,
    'C': 3,
    'c': 3,
    'D': 4
}

row_dict = {
    'question': '',
    'option1': '',
    'option2': '',
    'option3': '',
    'option4': '',
    'answer': '',
    'explanation': '',
    'course/subject': '174,175',
    'instruction': '',
    'tags(Coma Seprate)': 'disease,bilogy,science',
    'topic(Topic id)': '5',
    'isShow': True,
}
next_is_question = False
header = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation',
          'course/subject', 'instruction', 'tags(Coma Seprate)', 'topic(Topic id)', 'isShow']


def test_pdf():
    # Creating a pdf file object
    pdf_file_obj = open('./pdfFile/Question on Health and Failure above topic.pdf', 'rb')

    # Creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    page_obj = pdf_reader.getPage(0)

    print(page_obj)
    text = page_obj.extractText().split("\n")
    print("++++++++++++++++++")
    print(text)
    #
    # test_list = list(filter(None, text))
    # print("=-=-=-=-=-=--=--=-=-=-=--=-=-=-=-")
    # print(test_list)

    # for i in range(len(text)):
    #     print(text[i])

    pdf_file_obj.close()


def read_pdf():
    global row_dict
    global next_is_question
    prev_line = ''
    current_line = ''

    # Creating a pdf file object
    pdf_file_obj = open('./pdfFile/Objective questions on disease topic.pdf', 'rb')

    # Creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # Getting number of pages in pdf file
    pages = pdf_reader.numPages
    csv_file = open(csv_file_name, 'w', newline='')
    writer = csv.DictWriter(csv_file, fieldnames=header)
    writer.writeheader()

    # Loop for reading all the Pages
    for i in range(pages):

        # Creating a page object
        page_obj = pdf_reader.getPage(i)

        # Printing Page Number
        print("Page No: ", i)

        # Extracting text from page
        # And splitting it into chunks of lines\
        print("current page text==============================")
        text = page_obj.extractText().split("\n \n")
        print(text)

        # Finally the lines are stored into list
        # For iterating over list a loop is used
        print("++++++++++++++++++++++++++++++ =-=-==- len(text): ", len(text))
        for i in range(len(text)):
            prev_line = current_line
            current_line = text[i]
            current_line = current_line.strip()
            current_line = current_line.replace("\n", "")

            # Lines are separated using "\n"
            # print("++++++++++++++++++++++++++++++")
            print(text[i], end="\n")
            if prepare_row(prev_line, current_line):
                writer.writerow(row_dict)

        # For Separating the Pages
        print("-=--=-=-==-=-=-----=--=-=-=-=-=--=--=-=-=-=--=")
    # closing the pdf file object
    pdf_file_obj.close()
    csv_file.close()


def prepare_row(prev_line, current_text):
    global row_dict
    global next_is_question
    if re.search("^[0-9]{1,2}\.", current_text):
        # row_dict['course/subject'] = prev_text
        row_dict['question'] = current_text[3:]
        print("Question No. 01=================")
        return False
    # elif re.search("^Question No", current_text):
    #     next_is_question = True
    #     print("Question No=================")
    #     return False
    elif re.search('^a\.', current_text):
        print("(A)=================")
        # row_dict['option1'] = current_text[3:]
        # row_dict['option1'] = prev_line
        return False
    elif re.search('^b\.', current_text):
        # row_dict['option2'] = current_text[3:]
        row_dict['option1'] = prev_line
        print("(B)=================")
        return False
    elif re.search('^c\.', current_text):
        # row_dict['option3'] = current_text[3:]
        row_dict['option2'] = prev_line
        print("(C)=================")
        return False
    elif re.search('^d\.', current_text):
        # row_dict['option4'] = current_text[3:]
        row_dict['option3'] = prev_line
        print("(D)=================")
        return False
    elif re.search("^[A-Dc]$", current_text):
        row_dict['option4'] = prev_line
        row_dict['answer'] = answer[current_text]
        print("answer=================")
        return True
    return False


# test_pdf()
read_pdf()
