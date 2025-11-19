def overzicht(codes: list):
    woordenboek = {"Engelstalige landen": 0,"Franstalige landen": 0,"Duitstalige landen": 0,"Japan": 0,"Russischtalige landen": 0,"China": 0,"Overige landen": 0,"Fouten": 0}
    for code in codes:
        x1 = int(code[0])
        x2 = int(code[1])
        x3 = int(code[2])
        x4 = int(code[3])
        x5 = int(code[4])
        x6 = int(code[5])
        x7 = int(code[6])
        x8 = int(code[7])
        x9 = int(code[8])
        x10 = int(code[9])
        x11 = int(code[10])
        x12 = int(code[11])
        x13 = int(code[12])
        o = x1 + x3 + x5 + x7 + x9 + x11
        e = x2 + x4 + x6 + x8 + x10 + x12
        drie = int(code[:3])
        if ((10 - ((o + 3 * e) % 10)) % 10) != x13 or not (drie == 978 or drie == 979):
            woordenboek["Fouten"] += 1
        elif x4 == 0 or x4 == 1:
            woordenboek["Engelstalige landen"] += 1
        elif x4 == 2:
            woordenboek["Franstalige landen"] += 1
        elif x4 == 3:
            woordenboek["Duitstalige landen"] += 1
        elif x4 == 4:
            woordenboek["Japan"] += 1
        elif x4 == 5:
            woordenboek["Russischtalige landen"] += 1
        elif x4 == 7:
            woordenboek["China"] += 1
        else:
            woordenboek["Overige landen"] += 1
    for key in woordenboek:
        print(key, ": ", woordenboek[key], sep="")



