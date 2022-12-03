elf_calories=[]

input_data = open("./input.txt", encoding="utf8").read().splitlines()

i=0
elf_calories.append(0)
for cal in input_data:
    if cal=='':
        i=i+1
        elf_calories.append(0)
    else:
        elf_calories[i]=elf_calories[i]+int(cal)   
    
print(max(elf_calories))