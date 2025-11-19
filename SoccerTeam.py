from enum import Enum


class SoccerPlayer:
    # The position a player can play on the pitch.
    position = Enum("position", ["GK",  # Goalkeeper
                                 "DF",  # Defender
                                 "MF",  # Midfield
                                 "FW"  # Forward
                                 ])

    def __init__(self, first_name, last_name, age, position):
        """
        SoccerPlayer constructor.

        :param first_name: the first name of the player
        :param last_name: the last name of the player
        :param age: the player's age
        :param position: the position on the pitch
        """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.position = position

    def __lt__(self, other):
        """
        Compare two SoccerPlayer objects based on their names.

        :param other: the other SoccerPlayer object to compare
        :return: True if their names are equal, False otherwise
        """
        return self.get_name().casefold() == other.get_name().casefold()

    def __eq__(self, other):
        """
        Check if two SoccerPlayer objects are equal.

        :param other: the other object to compare
        :return: True if self is equal to other, False otherwise
        """
        if self is other:
            return True
        if not isinstance(other, SoccerPlayer):
            return False
        return (
                self.age == other.age and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.position == other.position
        )

    def get_age(self):
        """
        Get the age of the player.

        :return: the age
        """
        return self.age

    def get_name(self):
        """
        Get the full name of the player.

        :return: the full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_position(self):
        """
        Get the position of the player.

        :return: the position
        """
        return self.position

    def __hash__(self):
        """
        Compute the hash value of the SoccerPlayer object.

        :return: the hash value
        """
        return hash((self.age, self.first_name, self.last_name, self.position))

    def __str__(self):
        return self.get_name()


class SoccerTeam:
    def __init__(self, name:str ):
        self.name = name
        self.numberplayers = 0
        self.lijst = [None, None, None, None, None, None, None, None, None, None, None]

    def add_player(self, player:SoccerPlayer):
        if self.numberplayers < 11 and player not in self.lijst:
            self.lijst[self.numberplayers] = player
            self.numberplayers += 1
            return True
        else:
            return False

    def get_average_age(self):
        som = 0
        n = 0
        for player in self.lijst:
            if player is not None:
                som += player.get_age()
                n += 1
        gemiddelde = som / n
        return float(f'{gemiddelde:.2f}')

    def get_formation(self):
        lijst3 = []
        verdediger = 0
        middenvelder = 0
        aanvaller = 0
        for i in range(len(self.lijst)):
            lijst3.append(self.lijst[i].position)
        for j in range(len(lijst3)):
            if lijst3[j] == "<position.DF: 2>":
                verdediger += 1
            elif lijst3[j] == "<position.MF: 3>":
                middenvelder += 1
            elif lijst3[j] == "<position.FW: 4>":
                aanvaller += 1
        print(lijst3)
        print(verdediger)
        print(middenvelder)
        print(aanvaller)
        return str(f"{verdediger}-{middenvelder}-{aanvaller}")

    def get_name(self):
        return self.name

    def get_players(self):
        return self.lijst

    def get_players_at(self, position: SoccerPlayer.position):
        lijst2 = []
        for player in self.lijst:
            if player is not None:
                if player.position == position:
                    lijst2.append(player)
        return lijst2

    def substitute(self, player_out: SoccerPlayer, player_in: SoccerPlayer):
        if player_out in self.lijst and player_in not in self.lijst:
            if player_out.position == "GK":
                if player_in.position == "GK":
                    self.lijst.remove(player_out)
                    self.lijst.append(player_in)
                    return True
                else:
                    return False
            else:
                if player_in.position != "GK":
                    self.lijst.remove(player_out)
                    self.lijst.append(player_in)
                    return True
                else:
                    return False
        else:
            return False


soccerteam_01 = SoccerTeam("AA Gent")
soccerteam_01.get_players()
speler_01 = SoccerPlayer("Karel", "de Grote", 28, SoccerPlayer.position.DF)
soccerteam_01.add_player(speler_01)
soccerteam_01.add_player(speler_01)
speler_02 = SoccerPlayer("fname_01", "lname_01", 28, SoccerPlayer.position.DF)
speler_03 = SoccerPlayer("fname_02", "lname_02", 27, SoccerPlayer.position.DF)
speler_04 = SoccerPlayer("fname_03", "lname_03", 26, SoccerPlayer.position.DF)
speler_05 = SoccerPlayer("fname_04", "lname_04", 25, SoccerPlayer.position.DF)
speler_06 = SoccerPlayer("fname_05", "lname_05", 22, SoccerPlayer.position.MF)
speler_07 = SoccerPlayer("fname_06", "lname_06", 32, SoccerPlayer.position.MF)
speler_08 = SoccerPlayer("fname_07", "lname_07", 30, SoccerPlayer.position.MF)
speler_09 = SoccerPlayer("fname_08", "lname_08", 29, SoccerPlayer.position.MF)
speler_10 = SoccerPlayer("fname_09", "lname_09", 38, SoccerPlayer.position.MF)
speler_11= SoccerPlayer("fname_10", "lname_10", 18, SoccerPlayer.position.FW)
speler_12 = SoccerPlayer("fname_11", "lname_11", 26, SoccerPlayer.position.FW)
speler_13 = SoccerPlayer("fname_12", "lname_12", 23, SoccerPlayer.position.GK)
speler_14 = SoccerPlayer("fname_13", "lname_13", 25, SoccerPlayer.position.GK)
soccerteam_01.add_player(speler_02)
soccerteam_01.add_player(speler_03)
soccerteam_01.add_player(speler_04)
soccerteam_01.add_player(speler_05)
soccerteam_01.add_player(speler_06)
soccerteam_01.add_player(speler_07)
soccerteam_01.add_player(speler_08)
soccerteam_01.add_player(speler_09)
soccerteam_01.add_player(speler_10)
soccerteam_01.add_player(speler_11)
soccerteam_01.add_player(speler_12)
soccerteam_01.get_name()
soccerteam_01.get_players_at(SoccerPlayer.position.GK)
soccerteam_01.substitute(speler_11, speler_12)
soccerteam_01.substitute(speler_01, speler_12)
soccerteam_01.substitute(speler_10, speler_13)
soccerteam_01.get_formation()
soccerteam_01.get_average_age()










