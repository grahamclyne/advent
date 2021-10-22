# for housenum in range(700000,10000000):
#     facs = {0}
#     checker = 1
#     while(checker <= housenum/checker):
#         if(float(housenum/checker).is_integer()):
#             facs.add(checker)
#             facs.add(housenum/checker)
#         checker += 1
#     if(housenum % 1000 == 0):
#         print(housenum)
#     if((sum(facs)) * 10 >= 33100000):
#         print(housenum, "answer")
#         break
#803880 too high for part 1


#part 2
houses = [0 for i in range(100000000)]
for elf in range(10000,1000000):  
    elf_og = elf
    if(elf % 1000 == 0):
        print(elf)
    for i in range(50):
        houses[elf_og] += (11 * elf)
        elf_og = elf_og + elf

for index in range(len(houses)):
    if(houses[index] >= 33100000):
        print(index)
        break

# too high for part 2 1408680
