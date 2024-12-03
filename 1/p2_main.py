

def do_the_thing(l1, l2):
    d = []
    for l in l1:
        c = l2.count(l)
        s = l * c
        print(s)
        d.append(s)
    print(sum(d))

def main():
    l1 = []
    l2 = []
    d = []
    with open("input.txt", 'r') as f:
        items = f.readlines()
        for i in items:
            locations = i.strip('\n').split('   ')
            l1.append(int(locations[0]))
            l2.append(int(locations[1]))

    do_the_thing(l1, l2)


main()