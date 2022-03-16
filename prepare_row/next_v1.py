import re
from common_file.answer import answer
from utils.option_utils import optionUtils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class next_v1:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            # if re.search("^[0-9]{1,2}\.", current_text):
            #     self.current_state = 'question'
            #     row_dict['question'] = ''
            #     logging.info("Question No next v1================= %s", current_text)
            #     return False

            if re.search("^Q[0-9]{1,2}\.", current_text):
                self.current_state = 'question'
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No=================")
                return False

            if re.search("^Q[0-9]{3}\.", current_text):
                self.current_state = 'question'
                row_dict['question'] = current_text[5:].strip()
                logging.info("Question No=================")
                return False

            if re.search('^(A\.|A |a\.|1\. )', current_text):
                logging.info("(A)=================")
                # row_dict['question'] += prev_text.strip()
                self.current_state = 'option1'
                # row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(B\.|B |b\.|2\. )', current_text):
                logging.info("(B)================= %s", prev_text)
                self.current_state = 'option2'
                row_dict['option1'] = prev_text[2:].strip()
                return False
            if re.search('^(C\.|C |c\.|3\. )', current_text):
                logging.info("(C)================= %s", prev_text)
                self.current_state = 'option3'
                row_dict['option2'] = prev_text[2:].strip()
                return False
            if re.search('^(D\.|D |d\.|4\. )', current_text):
                logging.info("(D)================= %s", prev_text)
                self.current_state = 'option4'
                row_dict['option3'] = prev_text[2:].strip()
                return False
            if re.search('^Answer: Option', current_text):
                logging.info("answer Option=================")
                self.current_state = 'answer'
                index = len('Answer: Option')
                row_dict['option4'] = prev_text[2:].strip()
                row_dict['answer'] = answer[current_text[index+1:index+2]]
                return True
            if re.search('^[A-D]$', current_text):
                logging.info("answer A-D=================")
                self.current_state = 'answer'
                row_dict['option4'] = prev_text[2:].strip()
                row_dict['answer'] = answer[current_text]
                return True
            if re.search('^Answer.', current_text):
                logging.info("answer dot=================")
                self.current_state = 'answer'
                index = len('Answer.')
                row_dict['option4'] = prev_text[2:].strip()
                row_dict['answer'] = answer[current_text[index + 1:index + 2]]
                return True
            if re.search('^[1-4].$', current_text):
                logging.info("answer dot=================")
                self.current_state = 'answer'
                row_dict['option4'] = prev_text[2:].strip()
                row_dict['answer'] = answer[current_text[0]]
                return True
            if self.current_state == 'question':
                logging.info('is_question  %s', current_text)
                if row_dict['question']:
                    row_dict['question'] += '\n' + current_text.strip()
                else:
                    row_dict['question'] += current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in next_v1")
            logging.error(ex)
