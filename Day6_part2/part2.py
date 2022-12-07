
input_stream = open("./input.txt", encoding="utf8").read().splitlines()
stream = ''.join(input_stream)

window_length = int(14)

for pos in range(0,len(stream)-window_length+1):
    window_slice = slice(pos, pos+window_length, 1)
    current_window = stream[window_slice]
    unique_characters = 0
    for i in range(0,window_length):
        unique_characters = unique_characters + current_window.count(current_window[i])
    if unique_characters == window_length:
        print(pos+window_length)
        break
