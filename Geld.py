from sys import getallocatedblocks


class Geld:
    def __init__(self, bedrag):
        if isinstance(bedrag, int):
            if bedrag >= 0:
                self.euros = bedrag
                self.centen = 0
            else:
                print("Negatieve bedragen zijn niet toegelaten")
        elif isinstance(bedrag, float):
            if bedrag >= 0:
                self.euros = int(bedrag // 1)
                self.centen = int(abs((bedrag - self.euros) * 100))
            else:
                print("Negatieve bedragen zijn niet toegelaten")
        elif isinstance(bedrag, Geld):
            self.euros = bedrag.euros
            self.centen = bedrag.centen
        elif isinstance(bedrag, str):
            if not "," in bedrag:
                print("Opmaak Geld string niet correct")
                self.euros = 0
                self.centen = 0
            else:
                if "€" in bedrag:
                    bedrag = bedrag[1:]
                    bedrag = bedrag.split(",", 1)
                    self.euros = int(bedrag[0])
                    self.centen = int(bedrag[1])
                else:
                    bedrag = bedrag.split(",", 1)
                    self.euros = int(bedrag[0])
                    self.centen = int(bedrag[1])

    def get_euros(self):
        return self.euros

    def get_centen(self):
        return self.centen

    def __str__(self):
        if self.centen >= 10:
            return "€" + str(self.euros) + "." + str(self.centen)
        else:
            return "€" + str(self.euros) + ".0" + str(self.centen)

    def vermenigvuldig(self, n: int):
        getal = self.euros + (self.centen / 100)
        vermenigvuldiging = getal * n
        return Geld(vermenigvuldiging)


    def optellen(self, tweedegetal):
        getal1 = self.euros + (self.centen / 100)
        getal2 = tweedegetal.euros + (tweedegetal.centen / 100)
        som = getal1 + getal2
        return Geld(som)
