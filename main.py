floor = 4
initial = 0
x=1
while x<=2:
    destination = int(input("enter destination floor"))
    if destination <= floor:
        if destination == initial:
            print('same floor')
        elif destination > initial:
            while initial <= destination:
                initial += 1
            print(initial-1)
            initial-=1
        elif destination < initial:
            while initial >= destination:
                initial -= 1
            print(initial+1)
            initial+=1
        else:
            pass


    else:
        print("invalid floor")
