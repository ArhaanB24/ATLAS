import random

no = int(input("Enter number of players "))
names = []
countries = []

# verification
for x in range(no):
    names.append(input(f"Enter name of player number {x+1} "))

def game(namelst):
    alpha = list("qwertyuiopasdfghjklzxcvbnm")
    start = random.choice(alpha).upper()
    first = input(f"{names[0]} start with letter {start}: ").upper()
    if first[0] != start:
        print(f"Player {names[0]} ejected")
        names.remove(names[0])
    i = 1
    let = first[-1]
    while len(names)>1:
        try:
            play = input(f"{names[i]} letter: {let}: ").upper()
            if play[0] != let:
                print(f"player {names[i]} ejected incorrect first letter")
                names.remove(names[i])
            elif play in countries:
                print(f"player {names[i]} ejected place repeated")
                names.remove(names[i])
            elif play not in countries:
                countries.append(play)
            let = play[-1]
            i += 1
        except IndexError:
            i = 0
    return f"Winner {''.join(names)}"
            
print(game(names))