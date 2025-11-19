from datetime import datetime

class Persoon:
    def __init__(self, naam, voornaam, woonplaats, jaar_geboorte_datum, maand_geboorte_datum, dag_geboorte_datum):
        self.naam = naam
        self.voornaam = voornaam
        self.woonplaats = woonplaats
        self.jaar_geboorte_datum = jaar_geboorte_datum
        self.maand_geboorte_datum = maand_geboorte_datum
        self.dag_geboorte_datum = dag_geboorte_datum

    def get_naam(self):
        return self.naam

    def get_voornaam(self):
        return self.voornaam

    def get_woonplaats(self):
        return self.woonplaats

    def get_geboorte_datum(self):
        return datetime.date(self.jaar_geboorte_datum, self.maand_geboorte_datum, self.dag_geboorte_datum)

    def set_voornaam(self, new_voornaam):
        self.voornaam = new_voornaam

    def set_woonplaats(self, new_woonplaats):
        self.woonplaats = new_woonplaats

    def is_ouder_dan(self, other_persoon):
        if self.jaar_geboorte_datum < other_persoon.jaar_geboorte_datum:
            return True
        else:
            return False

    def is_jonger_dan(self, other_persoon):
        if self.jaar_geboorte_datum > other_persoon.jaar_geboorte_datum:
            return True
        else:
            return False

    def wonen_in_zelfde_stad(self, other_persoon):
        if self.woonplaats == other_persoon.woonplaats:
            return True
        else:
            return False




