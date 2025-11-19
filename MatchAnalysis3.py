from MatchAnalysis1 import Player
from MatchAnalysis2 import Pass

class PassGraph:
    def __init__(self, players: list[Player], adj: dict[str, list[Pass]], path_naam:str):
        self.players = players
        self.adj = adj
        if path_naam is not None:
            self.lezer(path_naam)

    def lezer(self, path):
        file = open(path, "r")
        sectie = ""
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("["):
                if line == "[PLAYERS]":
                    sectie = "speler"
                    continue
                if line == "[PASSES]":
                    sectie = "pas"
                    continue
                else:
                    raise ValueError
            if sectie == "speler":
                delen = line.split(";")
                name = delen[0].strip()
                number = int(delen[1].strip())
                self.add_player(Player(name, number))
            elif sectie == "pas":
                links, rechts = line.split(":")
                aantal = int(rechts.strip())
                namen = links.split("->")
                sender = namen[0].strip()
                reciever = namen[1].strip()
                s1 = self.get_player(sender)
                s2 = self.get_player(reciever)
                if s1 and s2:
                    self.add_pass(s1, s2, aantal)
                else:
                    raise ValueError

    def save_to_txt(self, path: str):
        with open(path, "w") as file:
            # STAP 1: De Spelers Sectie
            file.write("[PLAYERS]\n")

            # Loop door alle spelers en schrijf ze weg: naam;nummer
            # (Je mag eventueel sorted(self.players, key=lambda p: p.name) gebruiken voor netheid)
            for player in self.players:
                file.write(f"{player.name};{player.number}\n")

            # STAP 2: De Passes Sectie
            file.write("[PASSES]\n")

            # Loop door alle lijsten met passes in de dictionary
            for pass_lijst in self.adj.values():
                for pas in pass_lijst:
                    # Schrijf weg: sender -> receiver : aantal
                    file.write(f"{pas.sender.name} -> {pas.receiver.name} : {pas.nr_of_times}\n")

    def add_player(self, player: Player):
        bestaat = False
        for p in self.players:
            if p.name == player.name:
                bestaat = True
                break
        if not bestaat:
            self.players.append(player)
            self.adj[player.name] = []

    def has_player(self, player: Player or str):
        bestaat = False
        if isinstance(player, Player):
            for p in self.players:
                if p.name == player.name:
                    bestaat = True
                    break
            return bestaat
        else:
            for p in self.players:
                if p.name == player:
                    bestaat = True
                    break
            return bestaat

    def get_player(self, name: str):
        for p in self.players:
            if p.name == name:
                return p
        return None

    def add_pass(self, sender: Player, receiver: Player, times = 1 ):
        if sender in self.players and receiver in self.players:
            if times > 0:
                index = 0
                for pas in self.adj[sender.name]:
                    if Pass.__eq__(pas, Pass(sender, receiver, times)):
                        self.adj[sender.name][index].nr_of_times += times
                        return None
                    index += 1
                self.adj[sender.name].append(Pass(sender, receiver, times))
            else:
                raise ValueError("Positief aantal passen nodig")
        return None

    def get_pass(self, sender_name: str, receiver_name: str):
        speler1 = None
        speler2 = None
        for player in self.players:
            if player.name == sender_name:
                speler1 = player
                continue
            if player.name == receiver_name:
                speler2 = player
        if speler1 is not None and speler2 is not None:
            for pas in self.adj[sender_name]:
                if pas == Pass(speler1, speler2,0):
                    return pas
            return None

    def neighbors(self, sender_name:str):
        if sender_name in self.adj:
            return self.adj[sender_name]
        return []

    def total_weight(self, subset: list[str]):
        som = 0
        if subset is None:
            for player in self.players:
                for pas in range(len(self.adj[player.name])):
                    som += self.adj[player.name][pas].nr_of_times
            return som
        else:
            for name in subset:
                if name in self.adj:
                    for pas in range(len(self.adj[name])):
                        if self.adj[name][pas].receiver.name in subset:
                            som += self.adj[name][pas].nr_of_times
            return som

    def pass_intensity(self, subset: list[str] | None = None) -> float:
        if subset is None:
            subset = list(self.adj.keys())
        if len(subset) < 2:
            return 0
        else:
            teller = self.total_weight(subset)
            noemer = (len(subset) - 1) * len(subset)
            return teller / noemer

    def top_pairs(self, k:int = 5):
        lijst = []
        for player in self.players:
            for pas in self.adj[player.name]:
                lijst.append(pas)
        lijst = sorted(lijst, key=lambda x: x.nr_of_times, reverse=True)
        return lijst[:k]

    def distribution_from(self, sender_name: str):
        if sender_name not in self.adj:
            return []
        gesorteerd = sorted(self.adj[sender_name], key=lambda x: x.nr_of_times, reverse=True)
        nieuw = [[pas.receiver.name, pas.nr_of_times] for pas in gesorteerd]
        return nieuw

    def players(self):
        kopie = self.players[:]
        return kopie

    def passes(self):
        alle_passes = []
        # self.adj.values() pakt alleen de lijsten met Pass-objecten uit de dictionary.
        # De 'keys' (de namen van de zenders als strings) worden hier genegeerd.
        for pass_lijst in self.adj.values():
            alle_passes.extend(pass_lijst)
        return alle_passes


