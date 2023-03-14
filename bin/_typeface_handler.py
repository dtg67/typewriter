import textwrap


class DocumentWrapper(textwrap.TextWrapper):

    def wrap(self, text):
        split_text = text.split('\n')
        lines = [line for para in split_text for line in textwrap.TextWrapper.wrap(self, para)]
        return lines


class Typewriter:
    def __init__(self, paper_type='Letter', paper_length=11, paper_width=8.5,
                 paper_msg='', l_margin=1.5, r_margin=1.5, t_margin=1, b_margin=1):
        self._paper_type = paper_type
        self._paper_length = paper_length
        self._paper_width = paper_width
        self._paper_msg = paper_msg
        self._l_margin = l_margin
        self._r_margin = r_margin
        self._t_margin = t_margin
        self._b_margin = b_margin

    def get_type(self):
        return self._paper_type

    def get_width(self):
        return self._paper_width

    def get_length(self):
        return self._paper_length

    def get_msg(self):
        return self._msg

    def get_l_margin(self):
        return self._l_margin

    def get_r_margin(self):
        return self._r_margin

    def get_t_margin(self):
        return self._t_margin

    def get_b_margin(self):
        return self._b_margin

    def set_length(self, l):
        self._paper_length = l

    def set_type(self, t):
        self._paper_type = t

    def set_width(self, w):
        self._paper_width = w

    def set_msg(self, msg):
        self._paper_msg = msg

    def set_l_margin(self, l_margin):
        self._l_margin = l_margin

    def set_r_margin(self, r_margin):
        self._r_margin = r_margin

    def set_t_margin(self, t_margin):
        self._t_margin = t_margin

    def set_b_margin(self, b_margin):
        self._b_margin = b_margin

    def __str__(self):
        return f'{self._paper_type}{self._paper_length}{self._paper_width}'


def wrap_text(file_read, page, char_length=(17/190)):
    chars_per_line = (page.get_with - page.get_l_margin - page.get_rmargin) / char_length
    d = DocumentWrapper(chars_per_line)
    return d.fill(file_read)

def wrap_text_to_timing(wrap_text, timing_dict):
    split_text = wrap_text.split('\n')
    for line in split_text:
        for letter in line:
            timing = timing_dict[letter]
            timing_to_gpio(timing)

        timing_to_gpio('\n')


def read_file(file):
    f = open(file, 'r')
    file_read = f.read()
    return file_read





