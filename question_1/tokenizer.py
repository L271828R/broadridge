
def tokenize(text):
    arr = []
    print("text==")
    print(text)
    symbols = ["[","]","{","}"]
    #for i, item in enumerate(text):
    i = -1
    while(i<len(text)-1):
        i += 1
        item = text[i]
        print(arr)
        # print("test=", item)
        print("current s to token=", item, "i=", i)
        if item in symbols:
            print("appending 0")
            arr.append(item)
            continue

        if (i + 4 < len(text)):
                if text[i:i+4] == '"*":':
                    print("appending 1")
                    arr.append('"*":')
                    i = i + 3
                    print("i=", i)
                    continue
                else:
                    if text[i:i+4] == '"*",':
                        print("appending 2")
                        i = i + 3
                        print("i=", i)
                        arr.append('"*",')
                        print(arr)
                        print("---")
                        continue

        if (i + 3 < len(text)):
                if (text[i:i+3] == '"*"'):
                        print("appending 3")
                        i = i + 2
                        print("i=", i)
                        arr.append('"*"')
                        continue

        print("~~1~", text[i:i+1])
        print("~~2~", text[i:i+2])
        print("~~3~", text[i:i+3])
        if (text[i:i+2] == "*,"):
            print("appending 4")
            arr.append("*,")
            i = i + 1
            print("i=", i)
            continue

        if (text[i] == "*"):
            print("appending 5")
            arr.append("*")
            continue

    print("TOKENs=")
    print(arr)
    return arr


