def bloedgroep_kind(vader, moeder):
    doorgeefbaarletter = {
        "A": ["A","O"],
        "B": ["B","O"],
        "AB": ["A","B"],
        "O": ["O"]
    }
    doorgeefbaarteken = {
        "+":["+","-"],
        "-":["-"]
    }
    mogelijk = set()
    for letterv in doorgeefbaarletter[vader[:-1]]:
        for letterm in doorgeefbaarletter[moeder[:-1]]:
            if letterm == letterv == "A":
                kindletter = "A"
            elif letterm == letterv == "O":
                kindletter = "O"
            elif letterm == letterv == "B":
                kindletter = "B"
            elif {letterm, letterv} == {"A", "B"}:
                kindletter = "AB"
            elif {letterm, letterv} == {"A", "O"}:
                kindletter = "A"
            elif {letterm, letterv} == {"O", "B"}:
                kindletter = "B"
            for tekenv in doorgeefbaarteken[vader[-1]]:
                for tekenm in doorgeefbaarteken[moeder[-1]]:
                    if tekenm == tekenv == "-":
                        kindteken = "-"
                    else:
                        kindteken = "+"
                    mogelijk.add(kindletter + kindteken)
    return mogelijk

def bloedgroep_ouder(ouder, kind):
    Alles = ["A+", "A-", "B+", "B-", "AB+","AB-", "O+", "O-"]
    mogelijk = set()
    for bloed in Alles:
        if kind in bloedgroep_kind(bloed, ouder):
            mogelijk.add(bloed)
    return mogelijk
