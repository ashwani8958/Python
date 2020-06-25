


#import all the module and varible from the seprate files
from variable import *
from batsmen import *
from bowler import *



pl_point_list = list()

for player in pl_list:
    #check if player is batsmen
    if "bat" == player.get("role"):
        pl_point_list.append(batsmen(player))
    #if player is bowler 
    else:
        pl_point_list.append(bowler(player))
        
#print the item in the list        
for i in range(len(pl_point_list)):
    print(pl_point_list[i])
    i = i + 1
