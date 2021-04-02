import re
from common_file.answer import answer


class v2:
    def __init__(self):
        self.is_question = False
        self.is_explanation = False

    def set_is_question(self, value):
        self.is_question = value

    def set_is_explanation(self, value):
        self.is_explanation = value

    def prepare_row(self, row_dict, prev_text, current_text):
        if re.search("^([0-9]{1}\.|Q[0-9]{1}-)", current_text):
            # row_dict['course/subject'] = prev_text
            self.set_is_question(True)
            row_dict['question'] = current_text[3:].strip()
            print("Question No. 01=================")
            return False

        if re.search("^([0-9]{2}\.|Q[0-9]{2}-)", current_text):
            # row_dict['course/subject'] = prev_text
            self.set_is_question(True)
            row_dict['question'] = current_text[4:].strip()
            print("Question No. 01=================")
            return False

        if re.search('^(A\.|A\))', current_text):
            print("(A)=================")
            self.set_is_question(False)
            row_dict['option1'] = current_text[3:].strip()
            return False
        if re.search('^(B\.|B\))', current_text):
            print("(B)=================")
            self.set_is_question(False)
            row_dict['option2'] = current_text[3:].strip()
            return False
        if re.search('^(C\.|C\))', current_text):
            print("(C)=================")
            self.set_is_question(False)
            row_dict['option3'] = current_text[3:].strip()
            return False
        if re.search('^(D\.|D\))', current_text):
            print("(D)=================")
            self.set_is_question(False)
            row_dict['option4'] = current_text[3:].strip()
            return False

        if re.search('^[A-D]$', current_text):
            print("answer v2=================")
            self.set_is_question(False)
            row_dict['answer'] = answer[current_text]
            return True

        if self.is_question:
            row_dict['question'] += '\n' + current_text.strip()

        return False
