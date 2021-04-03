import re
from common_file.answer import answer
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class v2:
    def __init__(self):
        self.is_question = False
        self.is_explanation = False

    def set_is_question(self, value):
        self.is_question = value

    def set_is_explanation(self, value):
        self.is_explanation = value

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^([0-9]{1}\.|Q[0-9]{1}-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^([0-9]{2}\.|Q[0-9]{2}-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search('^(A\.|A\))', current_text):
                logging.info("(A)=================")
                self.set_is_question(False)
                row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(B\.|B\))', current_text):
                logging.info("(B)=================")
                self.set_is_question(False)
                row_dict['option2'] = current_text[3:].strip()
                return False
            if re.search('^(C\.|C\))', current_text):
                logging.info("(C)=================")
                self.set_is_question(False)
                row_dict['option3'] = current_text[3:].strip()
                return False
            if re.search('^(D\.|D\))', current_text):
                logging.info("(D)=================")
                self.set_is_question(False)
                row_dict['option4'] = current_text[3:].strip()
                return False

            if re.search('^[A-D]$', current_text):
                logging.info("answer v2=================")
                self.set_is_question(False)
                row_dict['answer'] = answer[current_text]
                return True

            if self.is_question:
                row_dict['question'] += '\n' + current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in v2")
            logging.error(ex)
