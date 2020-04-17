"This function calculate the points for the bowlers"

def bowler(player):

    #Accessing all te detail of the current batsmen
    name = (player.get("name"))
    run = player.get("runs")
    wkts = player.get("wkts")
    over = player.get("overs")
    field = player.get("field")

  
    #calculating the point scored
    #calculating wkts bouns based on wicket taken per match
    if wkts >= 3 and wkts < 5:
        wkts_bouns = 5
    elif wkts >= 5:
        wkts_bouns = 10
    else:
        wkts_bouns = 0

    
    wkts = wkts * 10
    field = field * 10

    #calculating strike rate
    eco_rate = (run/over)
    

    #calculating the points
    if eco_rate > 3.5 and eco_rate < 4.5:
        total_pt = wkts + wkts_bouns + field + 4 #4 point for eco_rate between (3.5, 4.5)
    elif eco_rate > 2  and eco_rate <= 3.5:
        total_pt = wkts + wkts_bouns + field + 7 #7 point for eco_rate between (2, 3.5)
    elif eco_rate < 2:
        total_pt = wkts + wkts_bouns + field + 10 #10 point for eco_rate below 2
    else:
        total_pt = wkts + wkts_bouns + field

    return {'name':name,'bowlscore':total_pt}

