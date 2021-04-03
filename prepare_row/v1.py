import re
from common_file.answer import answer
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class v1:
    def __init__(self):
        self.is_question = False
        self.is_explanation = False

    def set_is_question(self, value):
        self.is_question = value

    def set_is_explanation(self, value):
        self.is_explanation = value

    def prepare_row(self, row_dict, prev_text, current_text):
        try:
            if re.search("^(Q[0-9]{1}\.\-|Q[0-9]{1}\-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^(Q[0-9]{2}\.\-|Q[0-9]{2}\-)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^([0-9]{1}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[2:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^([0-9]{2}\.)", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^Q[0-9]{1}", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[3:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search("^Q[0-9]{2}", current_text):
                # row_dict['course/subject'] = prev_text
                self.set_is_question(True)
                row_dict['question'] = current_text[4:].strip()
                logging.info("Question No. 01=================")
                return False

            if re.search('^(a\)|\(a\)|A\)|A\.|a\.)', current_text):
                logging.info("(A) v1=================")
                self.set_is_question(False)
                row_dict['option1'] = current_text[3:].strip()
                return False
            if re.search('^(b\)|\(b\)|B\)|B\.|b\.)', current_text):
                logging.info("(B) v1=================")
                self.set_is_question(False)
                row_dict['option2'] = current_text[3:].strip()
                return False
            if re.search('^(c\)|\(c\)|C\)|C\.|c\.)', current_text):
                logging.info("(C) v1=================")
                self.set_is_question(False)
                row_dict['option3'] = current_text[3:].strip()
                return False
            if re.search('^(d\)|\(d\)|D\)|D\.|d\.)', current_text):
                logging.info("(D) v1=================")
                self.set_is_question(False)
                row_dict['option4'] = current_text[3:].strip()
                return False
            if re.search('^Answer.', current_text):
                logging.info("answer v1 Answer.=================")
                self.set_is_question(False)
                index = len('Answer.')
                row_dict['answer'] = answer[current_text[index + 1:index + 2]]
                return True
            # if re.search('^Answer', current_text):
            #     logging.info("answer=================")
            #     self.set_is_question(False)
            #     index = current_text.index('(')
            #     row_dict['answer'] = answer[current_text[index+1:index+2]]
            #     return True
            if re.search('^Answer: Option', current_text):
                logging.info("answer v1 Answer: Option=================", current_text)
                self.set_is_question(False)
                index = len('Answer: Option')
                row_dict['answer'] = answer[current_text[index+1:index+2]]
                return True
            if re.search('^Answer: \(', current_text):
                logging.info("answer v1 Answer: (=================", current_text)
                self.set_is_question(False)
                index = len('Answer: (')
                row_dict['answer'] = answer[current_text[index:index+1]]
                return True
            if re.search('^ANSWER :', current_text):
                logging.info("answer v1 ANSWER :=================", current_text)
                self.set_is_question(False)
                index = len('Answer :')
                row_dict['answer'] = answer[current_text[index:index+1]]
                return True
            if re.search('^Answer:', current_text):
                logging.info("answer v1 ANSWER:=================", current_text)
                self.set_is_question(False)
                index = len('Answer:')
                row_dict['answer'] = answer[current_text[index+1:index+2]]
                return True
            if re.search('^[A-D]$', current_text):
                logging.info("answer v1 A-D=================")
                self.set_is_question(False)
                row_dict['answer'] = answer[current_text]
                return True

            if self.is_question:
                row_dict['question'] += '\n' + current_text.strip()

            return False
        except Exception as ex:
            logging.error("Exception in v1")
            logging.error(ex)
