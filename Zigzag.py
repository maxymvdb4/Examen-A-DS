def iszigzag(lijst):
    if lijst[1] > lijst[0]:
        return False
    for i in range(1,len(lijst)-1):
        if not (lijst[i-1] <= lijst[i] >= lijst[i+1] or lijst[i-1] >= lijst[i] <= lijst[i+1]):
            return False
    return True

def zigzag_traag(lijst):
    lijst.sort()
    for i in range(1,len(lijst), 2):
        lijst[i], lijst[i-1] = lijst[i-1], lijst[i]

def zigzag_snel(lijst):
    for i in range(1, len(lijst), 2):
        if lijst[i-1] < lijst[i]:
            lijst[i], lijst[i-1] = lijst[i-1], lijst[i]
        if i+1 < len(lijst) and lijst[i] > lijst[i+1]:
            lijst[i], lijst[i+1] = lijst[i+1], lijst[i]


