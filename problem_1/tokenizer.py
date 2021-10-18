
def tokenize(text):
    arr = []
    symbols = ["[","]","{","}"]
    i = -1
    while(i<len(text)-1):
        i += 1
        item = text[i]
        if item in symbols:
            arr.append(item)
            continue

        if (i + 4 < len(text)):
                if text[i:i+4] == '"*":':
                    arr.append('"*":')
                    i = i + 3
                    continue
                else:
                    if text[i:i+4] == '"*",':
                        i = i + 3
                        arr.append('"*",')
                        continue

        if (i + 3 < len(text)):
                if (text[i:i+3] == '"*"'):
                        i = i + 2
                        arr.append('"*"')
                        continue

        if (text[i:i+2] == "*,"):
            arr.append("*,")
            i = i + 1
            continue

        if (text[i] == "*"):
            arr.append("*")
            continue
    return arr


