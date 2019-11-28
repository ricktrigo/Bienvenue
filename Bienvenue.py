def hello(nom):
    if estvide(nom)==True:
        h="Hello, my friend"
    else:
        h="Hello, " + nom
    return h


def estvide(nom):
    if len(nom)==0:
        return True
    else:
        return nom.isspace()
