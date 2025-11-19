def samenvoegen(lijst1, lijst2):
    nieuw = []
    for i in range(min(len(lijst1), len(lijst2))):
        nieuw.append(lijst1[i])
        nieuw.append(lijst2[i])
    return nieuw

def weven(lijst1, lijst2):
    nieuw = []
    if len (lijst1) == len(lijst2):
        samenvoegen(lijst1, lijst2)
    if len (lijst1) > len(lijst2):
        for i in range(len(lijst1)):
            j = i % len(lijst2)
            nieuw.append(lijst1[i])
            nieuw.append(lijst2[j])
    else:
        for i in range(len(lijst2)):
            j = i % len(lijst1)
            nieuw.append(lijst1[j])
            nieuw.append(lijst2[i])
    return nieuw





def ritsen(lijst1, lijst2):
    if len (lijst1) == len(lijst2):
        nieuw = samenvoegen(lijst1, lijst2)
    elif len (lijst1) > len(lijst2):
        nieuw = samenvoegen(lijst1[:len(lijst2)], lijst2)
        for i in range(len(lijst1)-len(lijst2)):
            nieuw.append(lijst1[i+len(lijst2)])
    else:
        nieuw = samenvoegen(lijst1, lijst2[:len(lijst1)])
        for i in range(len(lijst2)-len(lijst1)):
            nieuw.append(lijst2[i+len(lijst1)])
    return nieuw









