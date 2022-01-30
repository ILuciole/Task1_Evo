def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45

    start_d = directions.index(facing)
    end_d = (start_d + turns) % len(directions)
    return directions[end_d]


while True:
    try:
        print("Enter your facing side and turns please")
        f = input("Facing: ")
        t = int(input("Turns: "))
        direction(f, t)
        assert -1080 <= t <= 1080
    except ValueError:
        print("You write wrong value! Try again!")
    except AssertionError:
        print("Please enter an integer between -1080 and 1080. Try again!")
    else:
        print(direction(f, t))
