
players=dict()
i=1
while i<=5:
    player={input(f"Enter player{i} Name:"):int(input("Enter Runs:"))}
    players.update(player)
    i=i+1
print(f"Players = {players}")
score=0
for i in players:
    if players[i]>score:
        score=players[i]
print(f"Highest Score = {score)}")

