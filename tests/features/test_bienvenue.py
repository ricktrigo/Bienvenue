import Bienvenue


def test_hello_1_nom():
    assert  Bienvenue.hello("bob")=="Hello, Bob"


def test_hello_vide():
    assert Bienvenue.hello_vide("    ") == "Hello, my friend"
    assert Bienvenue.hello_vide("") == "Hello, my friend"

def test_hello_cris():
    assert Bienvenue.hello_cris("JERRY") == "HELLO, JERRY !"


def test_split():
    assert Bienvenue.split("Amy, Bob,Jerry")==["Amy","Bob","Jerry"]
    assert Bienvenue.split("Amy, BOB,JERRY") == ["Amy","BOB","JERRY"]


def test_n_input():
    assert Bienvenue.hello_n("Amy, Bob,Jerry")=="Hello, Amy, Bob, Jerry"
    assert Bienvenue.hello_n(" amy,bob,jerry") == "Hello, Amy, Bob, Jerry"
    assert Bienvenue.hello_n("bob, amy, jerry") == "Hello, Bob, Amy, Jerry"

def test_hello_n_cris():
    assert Bienvenue.hello_n_cris("Amy, BOB, Jerry")=="Hello, Amy, Jerry. AND HELLO, BOB !"
    assert Bienvenue.hello_n_cris("Amy, BOB, JERRY") == "Hello, Amy. AND HELLO, BOB, JERRY !"
    assert Bienvenue.hello_n_cris("Amy, Toto, BOB, JERRY") == "Hello, Amy, Toto. AND HELLO, BOB, JERRY !"


def test_hello_and():
    assert Bienvenue.hello_and("Amy, bob, Jerry")=="Hello, Amy, Bob and Jerry."
