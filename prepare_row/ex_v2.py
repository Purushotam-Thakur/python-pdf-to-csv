import re
from common_file.answer import answer
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class ex_v2:
    def __init__(self):
        self.is_question = False
        self.is_explanation = False

    def set_is_question(self, value):
        self.is_question = value

    def set_is_explanation(self, value):
        self.is_explanation = value

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^(Q[0-9]{1,2}\.|Question No)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                self.set_is_explanation(False)
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^([0-9]{2}\.|Q[0-9]{2}-)", current_text):
                self.set_is_question(True)
                self.set_is_explanation(False)
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No=================")
                return False
            if re.search("^([0-9]{1}\.|Q[0-9]{1}-)", current_text):
                self.set_is_question(True)
                self.set_is_explanation(False)
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No=================")
                return False

            if re.search('^(a\)|\(a\)|A\)|A\.|a\.)', current_text):
                logging.info("(A)=================")
                self.set_is_question(False)
                self.set_is_explanation(False)
                row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(b\)|\(b\)|B\)|B\.|b\.)', current_text):
                logging.info("(B)=================")
                self.set_is_question(False)
                self.set_is_explanation(False)
                row_dict['option2'] = current_text[3:].strip()
                return False
            if re.search('^(c\)|\(c\)|C\)|C\.|c\.)', current_text):
                logging.info("(C)=================")
                self.set_is_question(False)
                self.set_is_explanation(False)
                row_dict['option3'] = current_text[3:].strip()
                return False
            if re.search('^(d\)|\(d\)|D\)|D\.|d\.)', current_text):
                logging.info("(D)=================")
                self.set_is_question(False)
                self.set_is_explanation(False)
                row_dict['option4'] = current_text[3:].strip()
                return False
            if re.search('^Answer: \(', current_text):
                logging.info("answer=================")
                self.set_is_question(False)
                self.set_is_explanation(False)
                index = len('Answer: (')
                row_dict['answer'] = answer[current_text[index:index + 1]]
                return False
            if re.search('^Explanation:', current_text):
                logging.info("Explanation=================")
                self.set_is_question(False)
                self.set_is_explanation(True)
                row_dict['explanation'] = current_text[12:].strip()
                return True

            if self.is_question:
                row_dict['question'] += '\n'+current_text.strip()
            if self.is_explanation:
                row_dict['explanation'] += '\n'+current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in ex_v2")
            logging.error(ex)
