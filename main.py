floor = 4
initial = 0
x=int(input('enter 1 to start the lift\n enter 2 to stop the lift '))
while x<2:
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
else:
    print('the lift has been stopped')
