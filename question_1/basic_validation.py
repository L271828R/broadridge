def is_basic_validation(text):
    #print("basic val")
    #print(text.find(',,'))
    if text[0] != "{":
        return False
    elif text[-1] != "}":
        return False
    elif text.find('""') != -1:
        return False
    elif text.find(',,') != -1:
        return False
    elif text.find('::') != -1:
        return False
    else:
        return True


