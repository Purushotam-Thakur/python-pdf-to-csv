# Importing required modules
import PyPDF2
import csv
import re
from nose.tools import assert_true

file_name = 'Chemistry Questions Bank'
csv_file_name = './csv/'+file_name+'.csv'

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
    'course/subject': '122',
    'instruction': '',
    'tags(Coma Seprate)': 'metal,non-metals,chemistry,science',
    'topic(Topic id)': '',
    'isShow': True,
}
next_is_question = False
header = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation',
          'course/subject', 'instruction', 'tags(Coma Seprate)', 'topic(Topic id)', 'isShow']


def read_pdf():
    global row_dict
    global next_is_question
    prev_line = ''
    current_line = ''

    # Creating a pdf file object
    pdf_file_obj = open('./pdfFile/'+file_name+'.pdf', 'rb')

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
            current_line = text[i]
            current_line = current_line.strip()
            current_line = current_line.replace("\n", "")
            prev_line = current_line

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
        # row_dict['question'] = current_text[3:].strip()
        print("Question No. 01=================")
        return False
    # elif re.search("^Question No", current_text):
    #     next_is_question = True
    #     print("Question No=================")
    #     return False
    elif re.search('A\.', current_text):
        print("(A)=================")
        # row_dict['option1'] = current_text[3:].strip()
        row_dict['question'] = prev_line
        return False
    elif re.search('^B\.', current_text):
        # row_dict['option2'] = current_text[3:].strip()
        row_dict['option1'] = prev_line
        print("(B)=================")
        return False
    elif re.search('^C\.', current_text):
        # row_dict['option3'] = current_text[3:].strip()
        row_dict['option2'] = prev_line
        print("(C)=================")
        return False
    elif re.search('^D\.', current_text):
        # row_dict['option4'] = current_text[3:].strip()
        row_dict['option3'] = prev_line
        print("(D)=================")
        return False
    elif re.search("^Answer: Option [A-D]$", current_text):
        print("+++++++++++=-=-=-=-=")
        print(current_text)
        print(current_text[14:])
        row_dict['option4'] = prev_line
        row_dict['answer'] = answer[current_text[13:].strip()]
        print("answer=================")
        return True
    return False


# test_pdf()
read_pdf()
