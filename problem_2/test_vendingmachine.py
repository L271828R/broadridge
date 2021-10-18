import pytest
from vending_machine import VendingMachine

def test_happy_path():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00}
    assert(v.validatePurchase("ID100", 100) == True)

def test_happy_path2():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00}
    assert(v.validatePurchase("ID100", 110) == True)

def test_happy_path3():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00}
    assert(v.getItemIds() == ["ID100"], True)

def test_happy_path4():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00, "ID200" : 200}
    assert(v.getItemIds() == ["ID100", "ID200"], True)

def test_happy_path5():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00, "ID200" : 200}
    assert(v.getPriceForItem("ID100") == 100, True)

def test_neg1():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00}
    assert(v.validatePurchase("ID100", 90) == False)

def test_neg2():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100.00}
    with pytest.raises(Exception):
        v.validatePurchase("ID99", 90)

def test_neg3():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100}
    with pytest.raises(Exception):
        v.validatePurchase("ID100", "xxx")

def test_neg4():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100}
    with pytest.raises(Exception):
        v.validatePurchase("ID100", None)

def test_neg5():
    v = VendingMachine()
    v.dic_id_price = {"ID100": 100}
    with pytest.raises(Exception):
        v.validatePurchase(None, 100)

