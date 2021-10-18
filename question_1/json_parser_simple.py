

def logging(text, logging=False):
    if logging:
        print(text)

def simple_parser(text, logging=False):
    closing_dic = {
            '}':'{',
            ']':'['
    }
    arr = [] # stack
    for i, item in enumerate(text):
        print(arr)
        if item in closing_dic:
            if arr[-1] == closing_dic[item]:
                arr.pop()
            else:
                return False
        else:
            if item in ["{","}","[","]"]:
                arr.append(item)
    print(arr)
    return True if len(arr) == 0 else False


if __name__ == '__main__':
    # sample = '{ “key1” : “value1”, “key2” : [“value2”, “value3”], “key3” : { “subkey1” : 123 } }'
    sample = '{[}]}'
    print(simple_parser(sample))
    print('done')


