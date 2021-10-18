import re
from tokenizer import tokenize
from basic_validation import is_basic_validation

# TODO convert “” to ""
def log(s, flag):
    if flag:
        print(s)


def parse_token(list_of_tokens):
    pass



def json_parser(text, logging=False):
    text = text.replace(" ", "")
    text = text.replace("“", '"')
    text = text.replace("“", '"')
    text = text.replace("”", '"')
    text = re.sub('[0-9a-zA-Z]+', '*', text)
    log(text, logging)
    if (not is_basic_validation(text)):
        return False
    log(text, logging)
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
        log("============", logging)
        if item == "[":
            is_dic_context = False
        if item == "]":
            is_dic_context = True
        log(arr, logging)
        log("current = >>" + item + "<< dic=" + str(is_dic_context), logging)
        if is_dic_context:
            log("--in dic--", logging)
            if item in closing_dic:
                if item in ["]"] and len(arr) > 2 and arr[-2] == closing_dic[item] and '"*"'== arr[-1] and '"*":' == arr[-3]:
                    log("removing from dic" + item + " "  + arr[-1] + " " + arr[-2] + " " + arr[-3])
                    arr.pop()
                    arr.pop()
                    arr.pop()
                elif item in ["]","}"] and len(arr) > 2 and arr[-1] == closing_dic[item] and '"*":'== arr[-2]:
                    log("removing from dic " + item + " " + arr[-1] + " " + arr[-2], logging)
                    arr.pop()
                    arr.pop()
                elif len(arr) > 0 and arr[-1] == closing_dic[item]:
                    log("removing from dic " + arr[-1] + " " + item, logging)
                    arr.pop()
                else:
                    log("adding item", logging)
                    arr.append(item)
            else:
                log("adding item", logging)
                arr.append(item)
        else:
            log("--in list--", logging)
            if item in closing_list and arr[-1] == closing_list[item]:
                arr.pop()
            elif item == "[":
                log("appending item", logging)
                arr.append(item)
            else:
                log("ignoring item", logging)
    log("POST", logging)
    log(arr, logging)
    return True if len(arr) == 0 else False




if __name__ == '__main__':
    sample = '{ “key1” : “value1”, “key2” : [“value2”, “value3”], “key3” : { “subkey1” : 123 } }'
    print("1" , json_parser(sample, logging=False)) 




