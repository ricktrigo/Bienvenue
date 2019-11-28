def hello(nom):
    if nom.isupper():
        h = "HELLO, " + nom + "!"
    elif estvide(nom)==True:
        h="Hello, my friend"
    else:
        nom=nom[0].upper() + nom[1:]
        h="Hello, " + nom
    return h


def estvide(nom):
    if len(nom)==0:
        return True
    else:
        return nom.isspace()