floor = 4
initial = 0
destination = int(input())
if destination <= floor:
    if destination == initial:
        print('same floor')
    elif destination > initial:
        while initial < destination:
            initial += 1
        print(initial)
    elif destination < initial:
        while initial > destination:
            initial -= 1
        print(initial)
    else:
        pass


else:
    print("invalid floor")