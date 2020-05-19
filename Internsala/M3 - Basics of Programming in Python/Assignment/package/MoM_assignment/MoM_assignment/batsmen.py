
"This function calculate the points for the batsmens"

def batsmen(player):

    #Accessing all te detail of the current batsmen
    name = (player.get("name"))
    run = player.get("runs")
    fours = player.get("4")
    sixs = player.get("6")
    balls_faced = player.get("balls")
    field = player.get("field")

    #calculting the point scored
    run = run * 2
    fours = fours * 1
    sixs = sixs * 2
    field = field * 10

    #calculating strike rate
    stk_rate = (run/balls_faced) * 100
    

    #calculating the points 
    if run < 100:
        if stk_rate > 80 and stk_rate < 100:
            total_pt = run + fours + sixs + field + 2 + 5 #2 point for stk_rate between (80,100) 5 point for half century 
        elif stk_rate > 100:
            total_pt = run + fours + sixs + field + 4 + 5 #4 point for stk_rate above 100, 5 point for half century 

    elif run >= 100:
        if stk_rate > 80 and stk_rate < 100:
            total_pt = run + fours + sixs + field + 2 + 10 #2 point for stk_rate between (80,100) 10 point for century 
        elif stk_rate > 100:
            total_pt = run + fours + sixs + field + 4 + 10 #4 point for stk_rate above 100, 10 point for century 

    return {'name':name,'batscore':total_pt}
   
