import Cifer


class Caesar:
    __textfile__ = None
    __shift__ = 0
    __key__ = ''

    def __init__(self, textfile, shift, key=Cifer.RUS_QWERTY):
        self.__textfile__ = textfile
        self.__shift__ = shift
        self.__key__ = key

    def __iter__(self):
        f = open(self.__textfile__, 'r')
        for line in f:
            res_line = ''
            for char in line:
                capital = char in self.__key__
                try:
                    i = (self.__key__.index(char.lower()) + self.__shift__) % len(self.__key__)
                    res_line += self.__key__[i].capitalize() if capital else self.__key__[i]
                except ValueError:
                    res_line += char
            yield res_line
        f.close()

