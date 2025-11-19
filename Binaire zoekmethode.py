def zoek(lijst: list, x:int):
    laag = 0
    hoog = len(lijst)-1
    midden = (laag + hoog)//2
    while laag <= hoog:
        if lijst[midden] > x:
            hoog = midden-1
            midden = (laag + hoog)//2
        elif lijst[midden] < x:
            laag = midden+1
            midden = (laag + hoog) // 2
        elif lijst[midden] == x:
            return midden
    return None

