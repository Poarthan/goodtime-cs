import random

def main():
    # montyhall("user") # if you want to play as a normal player

    print("100000 games switching doors")
    montyhall("computer",simulations=100000, switch=True)
    
    print("100000 games not switching doors")
    montyhall("computer",simulations=100000, switch=False)

def montyhall(player, simulations=1000, switch=False):
    if player=="user":
        winningdoor=random.randint(1,3)
        doors = [1,2,3]
        print("Which door do you choose, 1, 2, or 3?")
        choice=int(input())

        if choice not in doors:
            print("Invalid choice")
            return

        if choice != doors[0] and winningdoor != doors[0]:
            print("Host Opens Door", doors[0])
            doors.remove(doors[0])
        elif choice != doors[1] and winningdoor != doors[1]:
            print("Host Opens Door", doors[1])
            doors.remove(doors[1])
        else:
            print("Host Opens Door", doors[2])
            doors.remove(doors[2])

        print("Do you want to switch, YES or NO?")
        switch=input()
        if switch=="YES":
            if choice==doors[0]:
                choice=doors[1]
            else:
                choice=doors[0]
        if choice==winningdoor:
            print("You win!")
        else:
            print("You lose!")
    else:
        wins=0
        for i in range(simulations):
            winningdoor=random.randint(1,3)
            doors = [1,2,3]
            choice=random.randint(1,3)

            if choice != doors[0] and winningdoor != doors[0]:
                doors.remove(doors[0])
            elif choice != doors[1] and winningdoor != doors[1]:
                doors.remove(doors[1])
            else:
                doors.remove(doors[2])

            if switch:
                if choice==doors[0]:
                    choice=doors[1]
                else:
                    choice=doors[0]
            if choice==winningdoor:
                wins+=1
        print("Winning percentage:", wins/simulations)
        print("Losing percentage:", 1-wins/simulations)





if __name__ == "__main__":
    main()
