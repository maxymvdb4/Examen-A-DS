def dubbel(lijst: list):
    woord = []
    for i in lijst:
        if i not in woord:
            woord.append(i)
        else:
            return i
    return None

def dubbels(lijst: list):
    gezien = set()
    dubbele = set()
    for i in lijst:
        if i not in gezien:
            gezien.add(i)
        else:
            dubbele.add(i)
    enkele = gezien - dubbele
    return enkele, dubbele
