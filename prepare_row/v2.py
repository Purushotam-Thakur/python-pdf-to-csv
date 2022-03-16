import re
from common_file.answer import answer
from utils.option_utils import optionUtils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class v2:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search('^([A-D]|[a-d])$', current_text):
                self.current_state = 'answer'
                row_dict['answer'] = answer[current_text[0]]
                logging.info("answer===== %s ============ %s", current_text, row_dict['answer'])
                return True

            if re.search("^([0-9]{1}\.|Q[0-9]{1}-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. 1=================")
                return False

            if re.search("^([0-9]{2}\.|Q[0-9]{2}-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^([0-9]{3}\.|Q[0-9]{3}-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[5:].strip()
                logging.info("Question No. 001=================")
                return False

            if re.search('^(A\.|A\)|\(A\))', current_text):
                logging.info("(A)=================")
                self.current_state = 'option1'
                row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(B\.|B\)|\(B\))', current_text):
                logging.info("(B)=================")
                self.current_state = 'option2'
                row_dict['option2'] = current_text[3:].strip()
                return False
            if re.search('^(C\.|C\)|\(C\))', current_text):
                logging.info("(C)=================")
                self.current_state = 'option3'
                row_dict['option3'] = current_text[3:].strip()
                return False
            if re.search('^(D\.|D\)|\(D\))', current_text):
                logging.info("(D)=================")
                self.current_state = 'option4'
                row_dict['option4'] = current_text[3:].strip()
                return False

            optionUtils(self.current_state).check_repeat_option(row_dict, current_text)

            return False
        except Exception as ex:
            logging.error("Exception in v2")
            logging.error(ex)
