import fitz
import os
import csv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

from common_file.init_row_dict import init_dict
from prepare_row.factory import factory

path = './csv'

init_dict['course/subject'] = '192,513,531'
init_dict['tags(Coma Seprate)'] = 'english,grammar,sentence improvement'
init_dict['topic(Topic id)'] = '60'

header = ['question', 'option1', 'option2', 'option3', 'option4', 'answer', 'explanation',
          'course/subject', 'instruction', 'tags(Coma Seprate)', 'topic(Topic id)', 'isShow']
prepare_row_type = 'v1'


def convert_pdf(pdf_file, csv_file_path):
    row_dict = init_dict.copy()
    try:
        obj = factory(prepare_row_type).get_prepare_row_type()
        if hasattr(obj, 'prepare_row()'):
            logging.info('Define prepare row type is not available')
            return

        with fitz.open(pdf_file) as doc:
            text = ""
            for page in doc:
                text += page.getText()

        pdf_doc = text.split("\n")
        # logging.info('pdf text = %s', text)
        logging.info('pdf_doc = ', pdf_doc)
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
            current_text = current_text.replace("₃", "3")
            current_text = current_text.replace("₄", "4")
            current_text = current_text.replace("₅", "5")
            current_text = current_text.replace("₆", "6")
            current_text = current_text.replace("₇", "7")
            current_text = current_text.replace("₈", "8")
            current_text = current_text.replace("₁₀", "10")
            current_text = current_text.replace("⁻", "-")
            current_text = current_text.replace("‾", "-")
            current_text = current_text.replace("⁺²", "+2")
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
                        writer.writerow(row_dict)
                        row_dict = init_dict.copy()
                    except Exception as ex:
                        logging.error("Exception while writing to csv")
                        logging.error(row_dict)
                        logging.error(ex)
                prev_text = current_text
    except Exception as e:
        logging.error("Exception while converting pdf")
        logging.error(e)


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
