import random

def rand_list(start, stop, total):
    if start < 0:
        print("start cannot be < zero ; start reset to zero '0'")
        start = 0
    rand_list = [random.randint(start, stop) for i in range(total)]
    print(f"{rand_list} \nis the unsorted list")
    return(rand_list)

def bubble(x):
    repeat = True
    while repeat:
        repeat = False
        for i in range (len(x)-1):
            if x[i] < x[i+1]:
                x[i], x[i+1] = x[i+1], x[i]
                print(x)
                repeat = True
    return(x)

def selection(x):
    for i in range(len(x)):
        low_val = i
        for j in range(i+1, len(x)):
            if x[j] < x[low_val]:
                
                low_val = j
                x[i], x[low_val] = x[low_val], x[i]
                print(x)
    return(x)

#the best:
def stalin(x):
    repeat = True
    while repeat:
        for i in range(len(x)-1):
            print(x)
            if is_sorted(x):
                repeat = False
                return(x)
            try:
                if x[i] < x[i+1]:
                    x.remove(x[i])#may make error | if does make x[i] variable to pass to remove()
            except:
                #this is fine.....!
                pass

def bogosort(x):
    repeat = True
    while repeat:
        if is_sorted(x):
            repeat = False
        random.shuffle(x)
        print(x)
    return(x)


def is_sorted(x):
    yay = 0
    for i in range(len(x)-1):
        print(i, x[i])
        if x[i] >= x[i+1]:
            yay += 1
        else:
            return(False) #:(
        if x[i] == x[-1] and i+1 == len(x):
            return(True)
    return(True)
if __name__ == "__main__":
    bubble(rand_list(0, 100, 10))
    b = input(">")
    selection(rand_list(0, 100, 10))
    b = input(">")
    stalin(rand_list(0, 100, 10))
    b = input(">")
    bogosort(rand_list(0, 100, 8))
