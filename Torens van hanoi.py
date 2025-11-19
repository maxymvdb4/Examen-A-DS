def hanoi(n):
    hanoihelper(n, "A", "C", "B")
    stappen = 2**n - 1
    print(stappen, "stappen gedaan")

def hanoihelper(n, start, einde, hulp):
    if n == 1:
        print("Schijf 1 van", start, "naar", einde)
    else:
        hanoihelper(n - 1, start, hulp, einde)
        print("Schijf", n,"van", start, "naar", einde)
        hanoihelper(n-1, hulp, einde, start)
