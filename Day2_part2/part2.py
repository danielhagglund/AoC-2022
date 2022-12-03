scores = {
    "A Y": 4, #draw
    "A Z": 8, #win
    "A X": 3, #lose
    "B X": 1, #lose
    "B Y": 5, #draw
    "B Z": 9, #win
    "C Z": 7, #win
    "C X": 2, #lose
    "C Y": 6 #draw
}

input_data = open("./input.txt", encoding="utf8").read().splitlines()

total_score = 0

for game in input_data:
    total_score = total_score + scores[game]   
    
print(total_score)