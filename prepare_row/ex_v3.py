import re
from common_file.answer import answer
import logging
from utils.option_utils import optionUtils

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class ex_v3:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^[0-9]{1}\)", current_text):
                self.current_state = 'question'
                row_dict['question'] = 'Select the most appropriate meaning of the given idioms.\n' + current_text[
                                                                                                      2:].strip()
                logging.info("Question No=================")
                return False
            if re.search("^[0-9]{2}\)", current_text):
                self.current_state = 'question'
                row_dict['question'] = 'Select the most appropriate meaning of the given idioms.\n' + current_text[
                                                                                                      3:].strip()
                logging.info("Question No=================")
                return False
            if re.search("^[0-9]{3}\)", current_text):
                self.current_state = 'question'
                row_dict['question'] = 'Select the most appropriate meaning of the given idioms.\n' + current_text[
                                                                                                      4:].strip()
                logging.info("Question No=================")
                return False

            if re.search('^(1\.|1 )', current_text):
                logging.info("(A)=================")
                self.current_state = 'option1'
                row_dict['option1'] = current_text[2:].strip()
                return False
            if re.search('^(2\.|2 )', current_text):
                logging.info("(B)=================")
                self.current_state = 'option2'
                row_dict['option2'] = current_text[2:].strip()
                return False
            if re.search('^(3\.|3 )', current_text):
                logging.info("(C)=================")
                self.current_state = 'option3'
                row_dict['option3'] = current_text[2:].strip()
                return False
            if re.search('^(4\.|4 )', current_text):
                logging.info("(D)=================")
                self.current_state = 'option4'
                row_dict['option4'] = current_text[2:].strip()
                return False

            if re.search('^Solution :', current_text):
                logging.info("answer=================")
                logging.info(current_text)
                self.current_state = 'answer'
                index = len('Solution :')
                row_dict['answer'] = answer[current_text[index:].strip()[0]]
                return False
            if re.search('^Solution:', current_text):
                logging.info("answer=================")
                logging.info(current_text)
                self.current_state = 'answer'
                index = len('Solution:')
                row_dict['answer'] = answer[current_text[index:].strip()[0]]
                return False
            if re.search('^Exp:', current_text):
                logging.info("Explanation=================")
                self.current_state = 'explanation'
                index = len('Exp:')
                row_dict['explanation'] = current_text[index:].strip()
                return True

            if current_text:
                optionUtils(self.current_state).check_repeat_option(row_dict, current_text)

            return False
        except Exception as ex:
            logging.error("Exception in ex_v3")
            logging.error(ex)
