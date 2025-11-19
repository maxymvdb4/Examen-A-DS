def isPalindroom(woord):
    if len(woord)==1 or len(woord)==0:
        return True
    elif woord[0] == woord[-1]:
        return isPalindroom(woord[1:len(woord)-1])
    else:
        return False
