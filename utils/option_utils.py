class optionUtils:
    def __init__(self, current_state):
        self.current_state = current_state

    def check_repeat_option(self, row_dict, current_text):
        if self.current_state == 'question':
            if row_dict['question']:
                row_dict['question'] += '\n' + current_text.strip()
            else:
                row_dict['question'] += current_text.strip()

        if self.current_state == 'option1':
            if row_dict['option1']:
                row_dict['option1'] += '\n' + current_text.strip()
            else:
                row_dict['option1'] += current_text.strip()

        if self.current_state == 'option2':
            if row_dict['option2']:
                row_dict['option2'] += '\n' + current_text.strip()
            else:
                row_dict['option2'] += current_text.strip()

        if self.current_state == 'option3':
            if row_dict['option3']:
                row_dict['option3'] += '\n' + current_text.strip()
            else:
                row_dict['option3'] += current_text.strip()

        if self.current_state == 'option4':
            if row_dict['option4']:
                row_dict['option4'] += '\n' + current_text.strip()
            else:
                row_dict['option4'] += current_text.strip()

        if self.current_state == 'explanation':
            if row_dict['explanation']:
                row_dict['explanation'] += '\n' + current_text.strip()
            else:
                row_dict['explanation'] += current_text.strip()

    def check_repeat_option_for_next(self, row_dict, current_text):
        if self.current_state == 'question':
            if row_dict['question']:
                row_dict['question'] += '\n' + current_text.strip()
            else:
                row_dict['question'] += current_text.strip()

        if self.current_state == 'explanation':
            if row_dict['explanation']:
                row_dict['explanation'] += '\n' + current_text.strip()
            else:
                row_dict['explanation'] += current_text.strip()
