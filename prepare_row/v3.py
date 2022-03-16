import re
from common_file.answer import answer
from utils.option_utils import optionUtils
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class v3:
    def __init__(self):
        self.current_state = None

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search('^([A-D]|[a-d])$', current_text):
                self.current_state = 'answer'
                row_dict['answer'] = answer[current_text[0]]
                logging.info("answer===== %s ============ %s", current_text, row_dict['answer'])
                return True
            if re.search("^(Q[0-9]{1} |Q [0-9]{1} |Q[0-9]{1}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. %s=================", current_text[:4])
                return False

            if re.search("^(A:|A.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text
                logging.info("Question No. %s=================", current_text)
                return False

            if re.search("^(Q[0-9]{2} |Q [0-9]{2}|Q[0-9]{2}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.current_state = 'question'
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. %s=================", current_text[:5])
                return False

            if re.search('^1\.', current_text):
                logging.info("(A)=================")
                self.current_state = 'option1'
                row_dict['option1'] = current_text[2:].strip()
                return False
            if re.search('^2\.', current_text):
                logging.info("(B)=================")
                self.current_state = 'option2'
                row_dict['option2'] = current_text[2:].strip()
                return False
            if re.search('^3\.', current_text):
                logging.info("(C)=================")
                self.current_state = 'option3'
                row_dict['option3'] = current_text[2:].strip()
                return False
            if re.search('^4\.', current_text):
                logging.info("(D)=================")
                self.current_state = 'option4'
                row_dict['option4'] = current_text[2:].strip()
                return False
            if re.search('^Answer.', current_text):
                logging.info("answer=================")
                self.current_state = 'answer'
                index = len('Answer.')
                row_dict['answer'] = answer[current_text[index + 1:index + 2]]
                return True
            if re.search('^Solution :', current_text):
                logging.info("answer=================")
                self.current_state = 'answer'
                index = len('Solution :')
                row_dict['answer'] = answer[current_text[index + 1:index + 2]]
                return True
            # if re.search('^Answer', current_text):
            #     logging.info("answer=================")
            #     self.current_state = 'answer'
            #     index = current_text.index('(')
            #     row_dict['answer'] = answer[current_text[index+1:index+2]]
            #     return True
            # if re.search('^Answer: Option', current_text):
            #     logging.info("answer=================", current_text)
            #     self.current_state = 'answer'
            #     index = len('Answer: Option')
            #     row_dict['answer'] = answer[current_text[index+1:index+2]]
            #     return True
            # if re.search('^Answer: \(', current_text):
            #     logging.info("answer=================", current_text)
            #     self.current_state = 'answer'
            #     index = len('Answer: (')
            #     row_dict['answer'] = answer[current_text[index:index+1]]
            #     return True
            # if re.search('^[A-D]$', current_text):
            #     logging.info("answer=================")
            #     self.set_is_question(False)
            #     row_dict['answer'] = answer[current_text]
            #     return True
            # if re.search('^Explanation:', current_text):
            #     logging.info("Explanation=================")
            #     self.current_state = 'explanation'
            #     is_explanation = True
            #     row_dict['explanation'] = current_text[12:].strip()
            #     return True

            optionUtils(self.current_state).check_repeat_option(row_dict, current_text)

            return False
        except Exception as ex:
            logging.error("Exception in v3")
            logging.error(ex)
