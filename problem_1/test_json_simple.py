from json_parser_simple import simple_parser

def test_happypath():
    s = '{"key1" : 123 }'
    assert(simple_parser(s) == True)

def test_happypath2():
    s = '{"key1" : 123}'
    assert(simple_parser(s) == True)

def test_happypath3():
    s = '{"key1" : []}'
    assert(simple_parser(s) == True)

def test_happypath4():
    s = '{"key1" : ["a"]}'
    assert(simple_parser(s) == True)

def test_happypath5():
    s = '{"key1" : ["a", "b"]}'
    assert(simple_parser(s) == True)

def test_happypath6():
    s = '{"key1" : ["a", "b", 1]}'
    assert(simple_parser(s) == True)

def test_happypath7():
    s = '{"key1" : "value1", "key2" : ["value2", "value3"], "key3" : { "subkey1" : "123" }, "key4":["x"] }'
    assert(simple_parser(s) == True)
    
def test_happypath8():
    s = '{"key0":{"key1" : "value1", "key2" : [], "key3" : {} }}'
    assert(simple_parser(s) == True)

def test_happypath9():
    s = '{}'
    assert(simple_parser(s) == True)


def test_neg1():
    s = '{[}'
    assert(simple_parser(s) == False)

def test_neg2():
    s = '{[}]'
    assert(simple_parser(s) == False)

def test_neg3():
    s = '{[}]}'
    assert(simple_parser(s) == False)

