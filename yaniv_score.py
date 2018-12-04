import sys
player_num = int(input("enter the number of players: "))
name = ["none"]*player_num
score = [0]*player_num
out = [1]*player_num
for j in range (player_num):
    name[j] = input("enter a players name: ")
while True:
    if sum(out) == 1:
        break
    print(name)
    print(score)
    for i in range (player_num):
        if out[i]==0:
            continue
        u=score[i]
        u+=(int(input("enter " +name[i]+ "'s score: ")))
        score[i]=u 
        if score[i]==50:
            score[i]=25
        if score[i] == 100:
            score[i] = 50
        if score[i] > 100:
            print(name[i], "is out of the game")
            out[i]=0
        if sum(out)==1:
            k=out.index(1)
            print("Congratulations " +name[k]+ " you won the game!")
            print(name)
            print(score)
            break