

def do_the_thing(l1, l2):
    d = []
    for i, l in enumerate(l1):
        x = l 
        y = l2[i]
        s = abs(x - y)
        d.append(s)
    print(sum(d))

def main():
    l1 = []
    l2 = []
    d = []
    with open("input_1.txt", 'r') as f:
        items = f.readlines()
        for i in items:
            locations = i.strip('\n').split('   ')
            l1.append(int(locations[0]))
            l2.append(int(locations[1]))
    
    l1.sort()
    l2.sort()

    do_the_thing(l1, l2)


main()