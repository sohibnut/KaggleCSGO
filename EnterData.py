from UseNeural import UseThisShit

keys = {0:"counter terrorists",
        1:"terrorists"}

timeleft = float(input("Time left[0:175]:  "))
ct_score = int(input("CT Score[0:33]:  "))
t_score = int(input("T Score[0:33]:  "))
ct_health = int(input("CT Health[0:500]:  "))
t_health = int(input("T Health[0:500]:  "))
ct_armor = int(input("CT Armor[0:500]:  "))
t_armor = int(input("T Armor[0:500]:  "))
ct_helmets = int(input("CT Helmets[0:5]:  "))
t_helmets = int(input("T Helmets[0:5]:  "))
ct_alive = int(input("CT Alive[0:5]:  "))
t_alive = int(input("T Alive[0:5]:  "))


ans = UseThisShit([timeleft, 
                   ct_score, 
                   t_score, 
                   ct_health, 
                   t_health, 
                   ct_armor, 
                   t_armor, 
                   ct_helmets, 
                   t_helmets,
                   ct_alive,
                   t_alive])


print(f"Winner: {keys[ans]}")
