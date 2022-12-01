f = open('day1calories.txt')
data=f.readlines()
calories=[]
this_elf=0
for line in data:
    if line =='\n' and this_elf!=0:
        calories.append(this_elf)
        this_elf=0
    else:
        line_as_int=int(line)
        this_elf+=line_as_int
calories.sort()
biggest_elf=calories[-1]
biggest_three_elves=calories[-1]+calories[-2]+calories[-3]
print(biggest_elf)
print(biggest_three_elves)
