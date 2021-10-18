import pytest
from json_parser import json_parser



def test_happypath():
    s = '{"key1" : 123 }'
    assert(json_parser(s) == True)

def test_happypath2():
    s = '{"key1" : 123}'
    assert(json_parser(s) == True)

def test_happypath3():
    s = '{"key1" : []}'
    assert(json_parser(s) == True)

def test_happypath4():
    s = '{"key1" : ["a"]}'
    assert(json_parser(s) == True)

def test_happypath5():
    s = '{"key1" : ["a", "b"]}'
    assert(json_parser(s) == True)

def test_happypath6():
    s = '{"key1" : ["a", "b", 1]}'
    assert(json_parser(s) == True)

def test_happypath7():
    s = '{"key1" : "value1", "key2" : ["value2", "value3"], "key3" : { "subkey1" : "123" }, "key4":["x"] }'
    assert(json_parser(s) == True)
    
def test_happypath8():
    s = '{"key0":{"key1" : "value1", "key2" : [], "key3" : {} }}'
    assert(json_parser(s) == True)

def test_happypath8():
    s = '{}'
    assert(json_parser(s) == True)

def test_neg_invalid1():
    s = '{"key1" : [1,,,2]}'
    assert(json_parser(s) == False)

def test_neg_invalid2():
    s = '{"key1" :: [1,2]}'
    assert(json_parser(s) == False)

def test_neg_invalid3():
    s = '[]'
    assert(json_parser(s) == False)

def test_neg_invalid4():
    s = '[{]'
    assert(json_parser(s) == False)

def test_neg_invalid5():
    s = '{[{]}}'
    assert(json_parser(s) == False)

def test_special_case():
    s = '{ “key1” : “value1”, “key2” : [“value2”, “value3”], “key3” : { “subkey1” : 123 } }'
    assert(json_parser(s) == True)

