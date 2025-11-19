from MatchAnalysis1 import Player

class Pass:
    def __init__(self, sender: Player, receiver: Player, nr_of_times:int):
        self.sender = sender
        self.receiver = receiver
        self.nr_of_times = nr_of_times

    def get_weight(self):
        return self.nr_of_times

    def get_start(self):
        return self.sender

    def get_end(self):
        return self.receiver

    def __eq__(self, other):
        return isinstance(other, Pass) and self.sender == other.sender and self.receiver == other.receiver

    def __str__(self):
        return f"Pass from {self.sender.name} to {self.receiver.name}"

x1=Player("Eden Hazard", 10)
x2=Player("Moussa Dembele",19)
x3=Player("Jan Vertonghen", 5)
y1=Pass(x1, x2, 1)
y2=Pass(x2, x3, 2)
y3=Pass(x2, x3, 3)
print(y3)
print(y2==y3)
if y1.get_weight() == 1:
    print(36)

