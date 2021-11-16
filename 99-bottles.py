t = [' bottles of beer',' on the wall',' bottle of beer']
for i in range(99):
    a = f'{99-i}{t[0]}{t[1]}, {99-i}{t[0]}.\nTake one down and pass it around, {98-i}{t[0]}{t[1]}.\n'
    if i == 97:
        break
    print(a)
print(f'2{t[0]}{t[1]}, 2{t[0]}.\nTake one down and pass it around, 1{t[2]}{t[1]}.\n\n1{t[2]}{t[1]}, 1{t[2]}.\nTake one down and pass it around, no more{t[0]}{t[1]}.\n\nNo more{t[0]}{t[1]}, no more{t[0]}.\nGo to the store and buy some more, 99{t[0]}{t[1]}.')