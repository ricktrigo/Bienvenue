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
    assert Bienvenue.hello2("Amy,bob")=="Hello, Amy, Bob"
    assert Bienvenue.hello2(" amy,bob") == "Hello, Amy, Bob"
    assert Bienvenue.hello2("bob, amy") == "Hello, Bob, Amy"