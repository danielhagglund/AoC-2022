scores = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6
}

input_data = open("./input.txt", encoding="utf8").read().splitlines()

total_score = 0

for game in input_data:
    total_score = total_score + scores[game]   
    
print(total_score)