RUS_QWERTY = 'йцукенгшщзхъфывапролджэячсмитьбюё'


class Caesar:
    __textfile__ = None
    __shift__ = 0
    __key__ = RUS_QWERTY

    def __init__(self, textfile, shift, key=RUS_QWERTY):
        self.__textfile__ = textfile
        self.__shift__ = shift
        self.__key__ = key

    def __iter__(self):
        f = open(self.__textfile__, 'r')
        for line in f:
            res_line = ' '
            for char in line:
                capital = char in RUS_QWERTY.capitalize()
                try:
                    i = self.__key__.index(char.lower()) + self.__shift__
                    i %= len(RUS_QWERTY)
                    res_line += RUS_QWERTY[i].capitalize() if capital else RUS_QWERTY[i]
                except ValueError:
                    res_line += char
            yield res_line
        f.close()

