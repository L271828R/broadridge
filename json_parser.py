import re
import string

# TODO convert “” to ""

def basic_validation(text):
    if text[0] != "{":
        return False

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
                    continue
                else:
                    if text[i:i+4] == '"*",':
                        i = i + 2
                        print("appending 2")
                        arr.append('"*",')

        if (i + 3 < len(text)):
                if (text[i:i+3] == '"*"'):
                        i = i + 1
                        print("appending 3")
                        arr.append('"*"')
                        continue

        if (text[i] == "*"):
            print("appending 4")
            arr.append("*")
            continue

        raise Exception("invalid json")    

    print("TOKENs=")
    print(arr)
    return arr

def json_parser(text):
    text = text.replace(" ", "")
    text = re.sub('[0-9a-zA-Z]+', '*', text)
    print(text)
    if (not basic_validation):
        return False
    print(text)
    list_of_tokens = tokenize(text)
    arr = [] # stack
    closing_dic = {
            '}':'{',
            '"*"':'"*":',
            '"*",':'"*":',
            '*':'"*":',
            ']':'['
            }
    closing_list = {
            ']':'[',
            '"*"':'"*",'
            }

    is_dic_context = True
    is_value = False
    for i, item in enumerate(list_of_tokens):
        print("============")
        if item == "[":
            is_dic_context = False
        if item == "]":
            is_dic_context = True
        print(arr)
        print("current = >>", item, "<< dic=", is_dic_context)
        if is_dic_context:
            print("--in dic--")
            if item in closing_dic:
                if len(arr) > 2:
                    print("--found', len=", len(arr), "arr[-3]=",arr[-3])
                else:
                    print("--found', len=", len(arr))
                if item in ["]"] and len(arr) > 2 and arr[-2] == closing_dic[item] and '"*"'== arr[-1] and '"*":' == arr[-3]:
                    print("removing from dic", item, arr[-1], arr[-2], arr[-3])
                    arr.pop()
                    arr.pop()
                    arr.pop()
                elif item in ["]","}"] and len(arr) > 2 and arr[-1] == closing_dic[item] and '"*":'== arr[-2]:
                    print("removing from dic", item, arr[-1], arr[-2])
                    arr.pop()
                    arr.pop()
                elif arr[-1] == closing_dic[item]:
                    print("removing from dic", arr[-1], item)
                    arr.pop()
                else:
                    print("adding item")
                    arr.append(item)
            else:
                print("adding item")
                arr.append(item)
        else:
            print("--in list--")
            if item in closing_list and arr[-1] == closing_list[item]:
                arr.pop()
            elif item == "[":
                print("appending item")
                arr.append(item)
            else:
                print("ignoring item")
                # arr.append(item)
    print("POST")
    print(arr)
    return True




if __name__ == '__main__':
    #sample = '{"key1" : 123}'
    sample = '{"key1" : [1,2]}'
    #sample = '{"key1" : "value1", "key2" : ["value2", "value3"], "key3" : { "subkey1" : "123" }, "key4":["x"] }'
    #sample = '{"key1" : "value1", "key2" : ["value2", "value3"], "key3" : { "subkey1" : "123" } }'
    #sample = '{"key1" : "value1", "key2" : ["value2", "value3"], "key3" : { "subkey1" : 123 } }'
    #sample = '{"key0":{"key1" : "value1", "key2" : [], "key3" : {} }}}'
    assert(json_parser(sample) == True)
