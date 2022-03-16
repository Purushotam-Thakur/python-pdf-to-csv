import re
from common_file.answer import answer
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class next_v2:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^([0-9]{1,2}\.|[0-9]{1,2})$", current_text):
                self.current_state = 'question'
                row_dict['question'] = ''
                logging.info("Question No=================", current_text)
                return False

            # if re.search("^([0-9]{1,2}\.|[0-9]{1,2})", current_text):
            #     self.set_is_question(True)
            #     row_dict['question'] = current_text[3:].strip()
            #     logging.info("Question No=================")
            #     return False

            if re.search('^(A\.|A$|a\.)', current_text):
                logging.info("(A)=================")
                # row_dict['question'] += prev_text.strip()
                self.current_state = 'option1'
                # row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(B\.|B$|b\.)', current_text):
                logging.info("(B)=================", prev_text)
                self.current_state = 'option2'
                row_dict['option1'] = prev_text.strip()
                return False
            if re.search('^(C\.|C$|c\.)', current_text):
                logging.info("(C)=================", prev_text)
                self.current_state = 'option3'
                row_dict['option2'] = prev_text.strip()
                return False
            if re.search('^(D\.|D$|d\.)', current_text):
                logging.info("(D)=================", prev_text)
                self.current_state = 'option4'
                row_dict['option3'] = prev_text.strip()
                return False
            if re.search('^Answer: Option', current_text):
                logging.info("answer Option=================")
                self.current_state = 'answer'
                index = len('Answer: Option')
                row_dict['option4'] = prev_text.strip()
                row_dict['answer'] = answer[current_text[index+1:index+2]]
                return True
            if self.current_state == 'question':
                logging.info('is_question ', current_text)
                if row_dict['question']:
                    row_dict['question'] += '\n' + current_text.strip()
                else:
                    row_dict['question'] += current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in next_v2")
            logging.error(ex)
