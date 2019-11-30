from Cifer.Caesar import Caesar as Caesar


RUS_QWERTY = 'йцукенгшщзхъфывапролджэячсмитьбюё'


def char_frequency(textfile, bigramm=False):
    res = {}
    f = open(textfile, 'r')
    for line in f:
        bigramm_flipflop = True
        buf = ''
        for char in line:
            if bigramm:
                if bigramm_flipflop:
                    buf = char
                    bigramm_flipflop = False
                    continue
                else:
                    buf += char
                    bigramm_flipflop = True
            else:
                buf = char

            if buf in res.keys():
                res[buf] += 1
            else:
                res[buf] = 1
    f.close()
    return res


def decifer(input_file, output_file, keys):
    """Replaces characters from input_file by the 'keys' dictionary.
    Writes results in output_file.
    All 'file's are paths."""
    inp = open(input_file, 'r')
    out = open(output_file, 'w+')
    for line in inp:
        outline = ''
        while line:
            not_finded = True
            for k in keys.keys():
                try:
                    if line.lower().index(k) == 0:
                        outline += keys[k]
                        line = line[len(k):]
                        not_finded = False
                        break
                except ValueError:
                    pass

            if line and not_finded:
                outline += line[0]
                line = line[1:]

        out.write(outline)
    inp.close()
    out.close()




