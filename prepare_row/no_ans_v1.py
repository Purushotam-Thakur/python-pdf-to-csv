import re
from common_file.answer import answer
from utils.option_utils import optionUtils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class no_ans_v1:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^(Q[0-9]{1}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[3:]
                logging.info("Question No. %s=================", current_text)
                return False
            if re.search("^(Q[0-9]{2}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. %s=================", current_text)
                return False
            if re.search("^(Q[0-9]{3}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[5:].strip()
                logging.info("Question No. %s=================", current_text)
                return False
            if re.search("^([0-9]{1}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[3:]
                logging.info("Question No. %s=================", current_text)
                return False
            if re.search("^([0-9]{2}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. %s=================", current_text)
                return False
            if re.search("^([0-9]{3}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[5:].strip()
                logging.info("Question No. %s=================", current_text)
                return False

            if re.search('^(a\) |\(a\)|\(A\))', current_text):
                logging.info("(A) v1=================")
                self.current_state = 'option1'
                row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(b\) |\(b\)|\(B\))', current_text):
                logging.info("(B) v1=================")
                self.current_state = 'option2'
                row_dict['option2'] = current_text[3:].strip()
                return False
            if re.search('^(c\) |\(c\)|\(C\))', current_text):
                logging.info("(C) v1=================")
                self.current_state = 'option3'
                row_dict['option3'] = current_text[3:].strip()
                return False
            if re.search('^(d\) |\(d\)|\(D\))', current_text):
                logging.info("(D) v1=================")
                self.current_state = 'option4'
                row_dict['option4'] = current_text[3:].strip()
                return True
            if re.search('^(A\.|a\.|a\))', current_text):
                logging.info("(A)=================")
                self.current_state = 'option1'
                row_dict['option1'] = current_text[2:].strip()
                return False
            if re.search('^(B\.|b\.|b\))', current_text):
                logging.info("(B)=================")
                self.current_state = 'option2'
                row_dict['option2'] = current_text[2:].strip()
                return False
            if re.search('^(C\.|c\.|c\))', current_text):
                logging.info("(C)=================")
                self.current_state = 'option3'
                row_dict['option3'] = current_text[2:].strip()
                return False
            if re.search('^(D\.|d\.|d\))', current_text):
                logging.info("(D)=================")
                self.current_state = 'option4'
                row_dict['option4'] = current_text[2:].strip()
                return True

            optionUtils(self.current_state).check_repeat_option(row_dict, current_text)

            return False
        except Exception as ex:
            logging.error("Exception in v1")
            logging.error(ex)
