
# Aufgaben:

class Team:
    def __init__(self, name):
        self.name = name
        self.tore = 0
        self.spieler = []
    
    def printTeam(self):
        print(f"Team: {self.name} Tore: {self.tore}")

class Spieler:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
        self.karriereStart = 0
        self.gehalt = 0
        self.position = 0


class Liga:
    def __init__(self):
        self.teams = {}
        self.name = ""
    def meldeAn(self, team):
        self.teams[team.name] = team
    def spiele(self, team1, tore1, team2, tore2):
        self.teams[team1].tore += tore1
        self.teams[team2].tore += tore2
    
    def gibTabelle(self):
        return self.teams
    
    def printTabelle(self):
        print("La Liga Table:")
        print("-------------")
        for team in self.teams:
           print(f"{self.teams[team].name} - Goals: {self.teams[team].tore}")


# Code that should only run when the script is executed as the main program
if __name__ == '__main__':

    liga = Liga()
    team1 = Team("Team A")
    team2 = Team("Team B")
    team3 = Team("Team C")

    liga.meldeAn(team1)
    liga.meldeAn(team2)
    liga.meldeAn(team3)

    liga.spiele("Team A", 2, "Team B", 1)
    liga.spiele("Team A", 1, "Team C", 2)
    liga.spiele("Team B", 1, "Team C", 1)
    
    liga.printTabelle()
