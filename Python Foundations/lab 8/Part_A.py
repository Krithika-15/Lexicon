print("Q-1, 2")
class BadTeam:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team_1 = BadTeam("Python")
team_2 = BadTeam("Java")

team_1.add_member("John")

print("Team and members with mutable default argument")
for team in [team_1, team_2]:
    print(f"Team : {team.name}\nMember : {team.members}")

print("same list ?", team_1.members is team_2.members)

# python creates [] in members=[] only once, when it first reads the def line.
# It does not make a new list for every object
# so both teams point to the same list.
# the fix is to use members=None as the default, and create the list inside __init__.
# code inside __init__ runs for every object, so each one gets its own list

print("\nQ-3, 4")
class Team:
    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            members = []
        self.members = members

    def add_member(self, member):
        self.members.append(member)


team_3 = Team("Python")
team_4 = Team("Java")

team_3.add_member("John")

print("Team and members without mutable default argument")
for team in [team_3, team_4]:
    print(f"Team : {team.name}\nMember : {team.members}")
print("same list ?",team_3.members is team_4.members)
