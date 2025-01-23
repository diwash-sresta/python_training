import csv
import random
file_path = "E:\python_training\GameMechanics\playerdetails.csv"
player_name = []
Score = 0
Locations = ["Ruins","Shrine","Temple","Forest","Tower"]
Treasures = ["100 Gold coins","50 Gold coins","1 Gold coins","50 silver coins","100 Copper Coins"]

 


while True:
    UI = '''
            Welcome to Treasure Hunting Game !!!
                created by using Python

        1. Start Game
        2. Load Game
        3. Player Details
        4. LeaderBoard 
        5. Exit
            
'''
    print(UI)
    options = int(input("Enter (1-5) to continue : "))
    if options == 5:
        print("Exiting the game.")
        break

    
    elif options == 1:
        player_name = input("Enter the name of the player : ")
        for _ in range(3):
             treasure_found =random.choice(Treasures)
             location_found =random.choice(Locations)
             print(f"Exploring {location_found}")
             print(f"{player_name} found {treasure_found} in {location_found}")
             if treasure_found == "100 Gold coins":
                  Score += 1000
             elif treasure_found == "50 Gold coins":
                  Score += 500
             elif treasure_found == "1 Gold coins":
                  Score += 100
             elif treasure_found == "50 Silver coins":
                  Score += 50
             elif treasure_found == "100 Copper coins":
                  Score += 10

        with open(file_path,mode = "a", newline="")as file:
                        csv_writer = csv.writer(file)
                        if file.tell() == 0:
                            csv_writer.writerow(["Player name","Treasures","Score",])
                        data = [player_name,treasure_found,Score]
                        csv_writer.writerow(data)
        leaderboard = []
        found = False

        with open(file_path, mode="r") as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            for row in csv_reader:
                if row[0] == player_name:
                    
                    leaderboard.append([row[0], max(int(row[2]), Score)])
                    found = True
                else:
                    leaderboard.append([row[0], int(row[1])])

        if not found:
            
            leaderboard.append([player_name, Score])

        
        leaderboard.sort(key=lambda x: x[1], reverse=True)

        
        with open(file_path, mode="w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(header)
            for entry in leaderboard:
                csv_writer.writerow(entry)
            
    elif options == 2:
        print("Loading  game")
    
    elif options == 3:
        print("Player Details")
        with open(file_path,mode= "r")as file:
             csv_reader = csv.reader(file)
             header = next(csv_reader)
             for row in csv_reader:
                  print(row)
        
    
    elif options == 4:
        with open(file_path, mode="r") as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)
                leaderboard = sorted(csv_reader, key=lambda x: int(x[2]), reverse=True)

                print(f"{'Rank':<5} {'Player Name':<15} {'Score':<5}")
                print("-" * 30)
                for rank, row in enumerate(leaderboard, start=1):
                    print(f"{rank:<5} {row[0]:<15} {row[1]:<5}")
        
