import math


def char_frequency(textfile, bigramm=False, filt=None):
    res = {}
    f = open(textfile, 'r')
    for line in f:
        bigramm_flipflop = True
        buf = ''
        for char in line:
            if filt:
                if char not in filt:
                    continue
            char = char.lower()
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


def caesar_decifer(input_file, output_file, keys):
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


def normalize_freq_diagram(fr_diag):
    fr_diag_norm = fr_diag.copy()
    s = sum(fr_diag.values())
    for key in fr_diag.keys():
        fr_diag_norm[key] /= s
    return fr_diag_norm


def find_a_caesar_key(chr_fr_orig, chr_fr_coded):
    #normalizing
    chr_fr_orig_norm = normalize_freq_diagram(chr_fr_orig)
    chr_fr_coded_norm = normalize_freq_diagram(chr_fr_coded)

    result = {}
    for key_orig in chr_fr_orig_norm.keys():
        min_diff = math.inf
        min_key = ''
        for key_coded in chr_fr_coded_norm.keys():
            diff = abs(chr_fr_orig_norm[key_orig] - chr_fr_coded_norm[key_coded])
            if diff < min_diff:
                min_diff = diff
                min_key = key_coded
        result[min_key] = key_orig
    return result
