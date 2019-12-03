def hello(nom):
    nom=nom[0].upper() + nom[1:]
    h="Hello, " + nom
    return h


def hello_cris(nom):
    return "HELLO, " + nom + " !"



def estvide(nom):
    if len(nom)==0:
        return True
    else:
        return nom.isspace()


def hello_vide(nom):
    if estvide(nom)==True:
        return "Hello, my friend"


def split(nom):
    chaine=[]
    nom.replace(" ","")
    for i in nom.split(","):
        i=i.strip()
        i = i[0].upper() + i[1:]
        chaine = chaine + [i]
    return chaine


def hello_n(nom):
    h="Hello"
    chaine=""
    nom_split=split(nom)
    for i in nom_split:
        chaine = chaine +", " + i
    return h + chaine


def hello_n_cris(nom):
    nom_split=split(nom)
    nom_maj=""
    nom_min=""
    for i in nom_split:
        if i.isupper():
            if estvide(nom_maj):
                nom_maj=i
            else:
                nom_maj=nom_maj+", "+i
        else:
            nom_min=nom_min+", "+i
    return "Hello"+nom_min+". AND "+hello_cris(nom_maj)