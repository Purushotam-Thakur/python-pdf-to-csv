import copy

import fitz
import os
import csv
import logging
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from common_file.init_row_dict import init_dict
from prepare_row.factory import factory

path = './csv'

init_dict['course/subject'] = '1168,1173,1197'
init_dict['tags(Coma Seprate)'] = 'Physics,Class 9th,Class Ninth,Work and Energy'
init_dict['topic(Topic id)'] = '196'

header = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation',
          'course/subject', 'instruction', 'tags(Coma Seprate)', 'topic(Topic id)', 'isShow']
prepare_row_type = 'v1'


def convert_pdf(pdf_file, csv_file_path):
    row_dict = init_dict.copy()
    wrong_questions = []
    write_to_csv_exceptions = []
    try:
        obj = factory(prepare_row_type).prepare_row_type
        if hasattr(obj, 'prepare_row()'):
            logging.error('Define prepare row type is not available')
            return

        with fitz.open(pdf_file) as doc:
            text = ""
            for page in doc:
                text += page.getText()

        pdf_doc = text.split("\n")
        # logging.info('pdf text = %s', text)
        # logging.info('pdf_doc = %s', pdf_doc)
        prev_text = ''

        csv_file = open(csv_file_path, 'w', newline='')
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()

        for current_text in pdf_doc:
            # logging.info("start===============>>>>")
            current_text = current_text.replace("\n", "")
            current_text = current_text.replace("→", "->")
            current_text = current_text.replace("⟶", "->")
            current_text = current_text.replace("─", "-")
            current_text = current_text.replace("≥", ">=")
            current_text = current_text.replace("≤", "<=")
            current_text = current_text.replace("₂", "2")
            current_text = current_text.replace("²", "^2")
            current_text = current_text.replace("₃", "3")
            current_text = current_text.replace("³", "^3")
            current_text = current_text.replace("₄", "4")
            current_text = current_text.replace("₅", "5")
            current_text = current_text.replace("₆", "6")
            current_text = current_text.replace("₇", "7")
            current_text = current_text.replace("₈", "8")
            current_text = current_text.replace("₁₀", "10")
            current_text = current_text.replace("⁻", "-")
            current_text = current_text.replace("‾", "-")
            current_text = current_text.replace("⁺²", "+2")
            current_text = current_text.replace("’", "'")
            current_text = current_text.replace("‘", "'")
            current_text = current_text.replace('“', '"')
            current_text = current_text.replace('”', '"')
            current_text = current_text.replace('–', '-')
            current_text = current_text.replace('…', '...')
            current_text = current_text.replace('₹', 'Rs.')
            current_text = current_text.replace('π', 'Pi.')
            current_text = current_text.replace('υ', 'v.')
            current_text = current_text.replace('Ω', 'Ohm')
            current_text = current_text.replace('∠', '<')
            current_text = current_text.strip()
            # logging.info("End===============>>>>")
            if current_text:
                try:
                    current_text = current_text[1:] if current_text[0] == '.' else current_text
                except Exception as e:
                    logging.error("Exception while remove .")
                    logging.error(e)

                if obj.prepare_row(row_dict, prev_text, current_text):
                    try:
                        if is_something_missing(row_dict):
                            wrong_questions.append(copy.deepcopy(row_dict))

                        writer.writerow(row_dict)
                        # row_dict = init_dict.copy()
                        row_dict = copy.deepcopy(init_dict)
                    except Exception as ex:
                        write_to_csv_exceptions.append(copy.deepcopy(row_dict))
                        logging.error("Exception while writing to csv")
                        logging.error(row_dict)
                        logging.error(ex)
                prev_text = current_text
        print('No of wrong questions ++ ', len(wrong_questions))
    except Exception as e:
        logging.error("Exception while converting pdf")
        logging.error(e)
    finally:
        time.sleep(1)
        print('No of csv exceptions ', len(write_to_csv_exceptions))
        if len(write_to_csv_exceptions) > 0:
            for csv_exception in write_to_csv_exceptions:
                print(csv_exception)
        print('No of wrong questions ', len(wrong_questions))
        if len(wrong_questions) > 0:
            for wrong_question in wrong_questions:
                print(wrong_question)


def is_something_missing(row_dict, ):
    bool_list = [True, False, 'TRUE', 'FALSE', 'true', 'false', 'True', 'False']
    if not row_dict['question']:
        return True
    if not row_dict['answer'] and 'no_ans' not in prepare_row_type:
        return True
    if not row_dict['option1']:
        return True
    if not row_dict['option2']:
        return True
    if not row_dict['option3']:
        if row_dict['option1'] in bool_list:
            row_dict['option3'] = 0
        else:
            return True
    if not row_dict['option4']:
        if row_dict['option1'] in bool_list:
            row_dict['option4'] = 0
        else:
            return True


def read_pdf():
    os.chdir(path)
    cwd = os.getcwd()
    logging.info(cwd)
    for i in os.walk(cwd):
        for j in i[2]:
            if j.endswith('.pdf'):
                logging.info('File Name : %s', j)
                convert_pdf(j, j.replace('.pdf', '.csv'))


read_pdf()
