import Bienvenue


def test_hello_1_nom():
    assert  Bienvenue.hello("bob")=="Hello, Bob"
    assert Bienvenue.hello(" ") == "Hello, my friend"
    assert Bienvenue.hello("") == "Hello, my friend"


def test_estvide():
    assert Bienvenue.estvide("    ") == True
    assert Bienvenue.estvide("") == True

def test_cris():
    assert Bienvenue.hello("JERRY") == "HELLO, JERRY!"


def test_2_input():
    assert Bienvenue.hellon("Amy,bob")=="Hello, Amy, Bob"
    assert Bienvenue.hellon(" amy,bob") == "Hello, Amy, Bob"
    assert Bienvenue.hellon("bob, amy") == "Hello, Bob, Amy"

def test_n_input():
    assert Bienvenue.hellon("Amy, Bob,Jerry")=="Hello, Amy, Bob, Jerry"
    assert Bienvenue.hellon(" amy,bob,jerry") == "Hello, Amy, Bob, Jerry"
    assert Bienvenue.hellon("bob, amy, jerry") == "Hello, Bob, Amy, Jerry"