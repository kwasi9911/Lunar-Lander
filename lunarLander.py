#Name: Nana Kwasi Owsuu
#Date: 12th March 2024
#Program Description: This program is a Lunar Lander Simulation. In order for the player to win, they must land with a speed between -2m/s and 2m/s.

#This module is used to allow the user to exit the game if they wish to.
import sys

#This function repeatedly asks the user for the amount of fuel they want to enter. The amount of fuel they enter must be a positive integer amount and also less than or equal to the remaining fuel.
def askFuel(currentFuel):
    while(True):
        fuelAmount = input('Enter units of fuel to use: \n')
        if fuelAmount.isdigit():
            fuelAmount = int(fuelAmount)
            if fuelAmount >= 0 and fuelAmount <= currentFuel:
                return fuelAmount
            else:
                print(f'Not enough fuel. Max Fuel: {currentFuel}')
                
        elif '-' in fuelAmount:
            print('Cannot use negative fuel.')
            return askFuel(currentFuel)
        else:
            print('Please Enter Integer Value.')
            return askFuel(currentFuel)

#This function takes in the planet that the user wants to land on. It gives the corresponding gravity value and initial amount of fuel. The function runs until the user reaches an altitude of 0.
#When this happens, the user's velocity is checked. If their velocity is between the range -2m/s and 2m/s, the user wins. If not, the user crashes.
#The user then has the option to play the level again or move to the next level depending on their status.
def playLevel(name,G,fuel):
    Altitude = 50
    Velocity = 0
    Seconds = 0
    T = 0.1
    print(f'Entering Level {planets.index(name)+1}')
    print(f'Landing on the {name}')
    print(f'Gravity is {G:.2f} m/s^2')
    print(f'Initial Altitude: {Altitude} meters')
    print(f'Initial Velocity: {Velocity:.2f} m/s')
    print(f'Burning a unit of fuel causes a 0.10 m/s slowdown.')
    print(f'Initial Fuel Level: {fuel} units\n')
    print()
    print(f'GO\n')
    
    while Altitude > 0:
        UserFuel = askFuel(fuel)
        fuel -= UserFuel
        Velocity = (Velocity) + (G) + (T*UserFuel)
        Altitude += Velocity
        Seconds +=1
        if Altitude <= 0:
            Altitude = 0
        print(f'After {Seconds} seconds Altitude is {Altitude:.2f} meters, velocity is {Velocity:.2f} m/s.')
        print(f'Remaning Fuel: {fuel} units')

    if (Velocity > -2) and (Velocity < 2):
        print('Landed Successfully.')
        PlayerWins(planets.index(name)+1)
    else:
        print('Crashed!')
        PlayerLoses(planets.index(name))

#This function handles the case when a player loses. They are asked if they want to play that level again. If they answer no, they are told the number of levels they beat and the program ends.
#If they choose yes, they get to try the level again. The function makes sure that the user inputs either yes or no 
def PlayerLoses(val):
    print(f'Do you want to play level {val+1}? (yes/no)')
    response = input().lower()
    if response == 'no':
        print(f'You made it past {val} levels.')
        print(f'Thank you for Playing.')
        sys.exit(0)
    elif response == 'yes':
        playLevel(planets[val],gravity[val],InitialFuelLevel[val])
    else:
        print('Your response must be yes or no')
        return PlayerLoses(val)

#This function handles the case when a player wins. They are asked if they want to play the next level. If they answer no, they are told the number of levels they beat and the program ends.
#If they choose yes, they get to move to the next level. The function makes sure that the user inputs either yes or no 
def PlayerWins(val):
    if val <= 10:
        print(f'Do you want to play level {val+1}? (yes/no)')
        response = input().lower()
        if response == 'no':
            print(f'You made it past {val} levels.')
            print(f'Thank you for Playing.')
            sys.exit(0)
        elif response == 'yes':
            playLevel(planets[val],gravity[val],InitialFuelLevel[val])
        else:
            print('Your response must be yes or no')
            return PlayerWins(val)
            
    else:
        print('Congratulations! You Win!')
        sys.exit(0)
    

#The main script of the program
if __name__ == "__main__":
    planets = ['Moon','Earth','Pluto','Neptune','Uranus','Saturn','Jupiter','Mars','Venus','Mercury','Sun']
    gravity = [-1.622,-9.81,-0.42,-14.07,-10.67,-11.08,-25.95,-3.77,-8.87,-3.59,-274.13]
    InitialFuelLevel = [150,5000,20,5700,5500,5600,7000,350,4700,320,10000]
    print('Welcome to Lunar Lander Game.')
    begin = input('Do you want to play level 1? (yes/no)\n')
    if begin.lower()=='yes':
        playLevel(planets[0],gravity[0],InitialFuelLevel[0])
    elif begin.lower()=='no':
        print('See you next time!')
        sys.exit(0)
    