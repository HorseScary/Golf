t=[' bottles of beer',' on the wall',' bottle of beer','.\nTake one down and pass it around, ']
for i in range(97):
    if i==97:break
    print(f'{99-i}{t[0]}{t[1]}, {99-i}{t[0]}{t[3]}{98-i}{t[0]}{t[1]}.\n')
print(f'2{t[0]}{t[1]}, 2{t[0]}{t[3]}1{t[2]}{t[1]}.\n\n1{t[2]}{t[1]}, 1{t[2]}{t[3]}no more{t[0]}{t[1]}.\n\nNo more{t[0]}{t[1]}, no more{t[0]}.\nGo to the store and buy some more, 99{t[0]}{t[1]}.')