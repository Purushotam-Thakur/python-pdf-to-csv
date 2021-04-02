from .v1 import v1
from .v2 import v2
from .v3 import v3
from .ex_v1 import ex_v1
from .ex_v2 import ex_v2
from .next_v1 import next_v1
from .next_v2 import next_v2


class factory:
    def __init__(self, prepare_row_type):
        self.prepare_row_type = prepare_row_type
        
    def get_prepare_row_type(self):
        if self.prepare_row_type == 'v1':
            return v1()
        elif self.prepare_row_type == 'v2':
            return v2()
        elif self.prepare_row_type == 'v3':
            return v3()
        elif self.prepare_row_type == 'ex_v1':
            return ex_v1()
        elif self.prepare_row_type == 'ex_v2':
            return ex_v2()
        elif self.prepare_row_type == 'next_v1':
            return next_v1()
        elif self.prepare_row_type == 'next_v2':
            return next_v2()
