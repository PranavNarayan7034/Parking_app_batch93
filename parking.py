print('............ WELCOME TO ABC PARKING ............')
print()
floor_one = []    # maximum 3
floor_two = []
floor_three= []
while True:
    choice = input('Do you want to Park/Exit :').lower()
    if choice == 'park':
        vn = input('Enter your vehicle no:')
        vt = input('Enter your vehicle type(2/4):')
        time = input('Parking Time (in hour):')
        info = {'vehicle_no':vn,'vehicle_type':vt,'Time':time}
        if len(floor_one)<3:
            floor_one.append(info)
            print(floor_one)
        elif len(floor_two)<3:
            floor_two.append(info)
            print(floor_two)
        elif len(floor_three)<3:
            floor_three.append(info)
            print(floor_three)
        else:
            print('Parking is full... please try after some time')

    elif choice == 'exit':
        vn = input('Enter your vehicle no:')
        print('Thank you for using ABC Parking....')
    else:
        print('Invalid choice..! Try again')

    exit = input('Do you want to continue(y/n)')
    if exit == 'n':
        print('Thank you for using ABC Parking....')
        break