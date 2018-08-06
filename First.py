ints = [1, 2, 3, 4, 5]

def NumberList(ints):
    total = 0 

    for items in ints:
        total += items
    
    return(total)

Value = NumberList(ints)

print(Value)