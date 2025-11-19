def combisom(lijst: list, x):
    for i in range(len(lijst)):
        for j in range(len(lijst)):
            if (lijst[i] + lijst[j]) == x and i !=j:
                return True
    return False

