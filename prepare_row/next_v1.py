import re
from common_file.answer import answer
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class next_v1:
    def __init__(self):
        self.is_question = False
        self.is_explanation = False

    def set_is_question(self, value):
        self.is_question = value

    def set_is_explanation(self, value):
        self.is_explanation = value

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^[0-9]{1,2}\.$", current_text):
                self.set_is_question(True)
                row_dict['question'] = ''
                logging.info("Question No next v1=================", current_text)
                return False

            # if re.search("^([0-9]{1,2}\.|[0-9]{1,2})", current_text):
            #     self.set_is_question(True)
            #     row_dict['question'] = current_text[3:].strip()
            #     logging.info("Question No=================")
            #     return False

            if re.search('^(A\.|A |a\.)', current_text):
                logging.info("(A)=================")
                # row_dict['question'] += prev_text.strip()
                self.set_is_question(False)
                # row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(B\.|B |b\.)', current_text):
                logging.info("(B)=================", prev_text)
                self.set_is_question(False)
                row_dict['option1'] = prev_text.strip()
                return False
            if re.search('^(C\.|C |c\.)', current_text):
                logging.info("(C)=================", prev_text)
                self.set_is_question(False)
                row_dict['option2'] = prev_text.strip()
                return False
            if re.search('^(D\.|D |d\.)', current_text):
                logging.info("(D)=================", prev_text)
                self.set_is_question(False)
                row_dict['option3'] = prev_text.strip()
                return False
            if re.search('^Answer: Option', current_text):
                logging.info("answer Option=================")
                self.set_is_question(False)
                index = len('Answer: Option')
                row_dict['option4'] = prev_text.strip()
                row_dict['answer'] = answer[current_text[index+1:index+2]]
                return True
            if re.search('^[A-D]$', current_text):
                logging.info("answer A-D=================")
                self.set_is_question(False)
                row_dict['option4'] = prev_text.strip()
                row_dict['answer'] = answer[current_text]
                return True
            if re.search('^Answer.', current_text):
                logging.info("answer dot=================")
                self.set_is_question(False)
                index = len('Answer.')
                row_dict['option4'] = prev_text.strip()
                row_dict['answer'] = answer[current_text[index + 1:index + 2]]
                return True
            if self.is_question:
                logging.info('is_question ', current_text)
                if row_dict['question']:
                    row_dict['question'] += '\n' + current_text.strip()
                else:
                    row_dict['question'] += current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in next_v1")
            logging.error(ex)
