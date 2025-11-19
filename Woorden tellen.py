def woorden_splitsen(tekst):
    inputfile = open(tekst, "r")
    lijst = []
    temp = []
    for line in inputfile:
        for char in line:
            if char.isalpha():
                temp.append(char)
            elif not char.isalpha() and len(temp) > 0:
                woord = str(''.join(temp))
                lijst.append(woord)
                temp = []
    return lijst


def woorden_splitsenlower(tekst):
    inputfile = open(tekst, "r")
    lijst = []
    temp = []
    for line in inputfile:
        for char in line:
            if char.isalpha():
                temp.append(char)
            elif not char.isalpha() and len(temp) > 0:
                woord = str(''.join(temp).lower())
                lijst.append(woord)
                temp = []
    return lijst

def woorden_tellen(tekst):
    lijst = woorden_splitsenlower(tekst)
    woordenboek = {}
    for word in lijst:
        if word not in woordenboek:
            woordenboek[word] = 1
        else:
            woordenboek[word] += 1
    return woordenboek









