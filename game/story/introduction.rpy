define pilot = Character('Argo Pilot', color="#000000")
define kai = Character('LCPL Kai', color="#9B30FF")
define chop = Character('CDR Chop', color="#ffff00")

image bg entrance = "images/bg/entrance.jpg"
image chop = "images/char/chop.png"

label introduction:

    pilot "Approaching The Charlotte, three minutes out."
    
    "I step onto the flight deck."
    
    show bg entrance
    with dissolve
    
    kai "Commander, you new hire is here."
    
    show chop at right
    with dissolve
    
    chop "Took you long enough."
    
    "Chop clears her throat."
    
    chop "Welcome abroad the Charlotte! Good to finally have you here."
    
    "I salute."
    python:
        player_name = renpy.input("My name is...")
        player_name = player_name.strip()
        if (player_name == "") or player_name is None:
            player_name="player"
    
    
    player "PVT [player_name] reporting!"
    
    chop "At ease, I am Commander Chop, in charge of education and training." 
    chop "I’m gonna be giving you a quick tour around the ship before we settle you in so you don’t bother me with questions later on when you get lost."
    
    player "I’m pretty good with directions, it’ll be hard for me to get lost. 
            {p}{color=#f00}I sort of have this ability to {i}bring up a photographic map of where I am by pressing 
            \[M\]{/i}.{/color}"
    
    chop "Sorry, what did you say? I kind of have this bad habit of tuning people out when I don’t care." 
    chop "Come on, let’s get going, we’re gonna be taking off soon from this station so we don’t have a lot of time."
    
    
return