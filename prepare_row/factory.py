from .v1 import v1
from .v2 import v2
from .v3 import v3
from .v4 import v4
from .ex_v1 import ex_v1
from .ex_v2 import ex_v2
from .ex_v3 import ex_v3
from .next_v1 import next_v1
from .next_v2 import next_v2
from .no_ans_v1 import no_ans_v1


class factory:
    def __init__(self, prepare_row_type):
        if prepare_row_type == 'v1':
            self.prepare_row_type = v1()
        elif prepare_row_type == 'v2':
            self.prepare_row_type = v2()
        elif prepare_row_type == 'v3':
            self.prepare_row_type = v3()
        elif prepare_row_type == 'v4':
            self.prepare_row_type = v4()
        elif prepare_row_type == 'ex_v1':
            self.prepare_row_type = ex_v1()
        elif prepare_row_type == 'ex_v2':
            self.prepare_row_type = ex_v2()
        elif prepare_row_type == 'ex_v3':
            self.prepare_row_type = ex_v3()
        elif prepare_row_type == 'next_v1':
            self.prepare_row_type = next_v1()
        elif prepare_row_type == 'next_v2':
            self.prepare_row_type = next_v2()
        elif prepare_row_type == 'no_ans_v1':
            self.prepare_row_type = no_ans_v1()
        else:
            self.prepare_row_type = None
