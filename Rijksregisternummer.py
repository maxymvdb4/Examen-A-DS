class Rijksregisternummer:
    def __init__(self, getal):
        assert isinstance(getal, str),"ongeldig type"
        lijst = list(getal)
        countern = 0
        counter = 0
        while counter < len(lijst):
            if lijst[counter].isdigit():
                countern += 1
                counter += 1
            else:
                counter += 1
        assert countern == 1, "ongeldig formaat (1 cijfer)"
        assert 1 < countern <= 10, f"ongeldig formaat ({countern} cijfers)"
        self.getal = getal

    def repr(self):
        lijst2 = list(self.getal)
        counter2 = 0
        while counter2 < len(lijst2):
            if not lijst2[counter2].isdigit():
                lijst2.pop(counter2)
        lijst2 = str(lijst2)
        nummer = "".join(lijst2)
        return Rijksregisternummer(nummer)

    def __str__(self):
        lijst3 = list(self.getal)
        for i in lijst3:
            if not isinstance(i, int):
                lijst3.pop(i)
        jj = str(lijst3[0:2])
        mm = str(lijst3[2:4])
        dd = str(lijst3[4:6])
        xxx = str(lijst3[6:9])
        cc = str(lijst3[9:10])
        return f"{jj}.{mm}.{dd}-{xxx}.{cc}"










