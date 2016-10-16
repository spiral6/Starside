define chop = Character('CDR Chop', color="#ffff00")
define revan = Character('SSGT Revan', color="#ffff00")

image bg berthing1 = "images/bg/berthing1.jpg"
image bg berthing2 = "images/bg/berthing2.jpg"
image revan = "images/char/revan.png"

label secondscene:
    
    show bg berthing1
    with dissolve
    
    chop "Welcome to where you’ll be spending your abundant amounts of free time, we already have a spare bed set up at the far end over there. Your bunkmate is..."
    
    "I hear pages flipping."
    
    chop "...Staff Sergeant Revan, he’s one of the higher ranking members in here so if you have questions go bother him."
    chop "Speaking of which, let’s go see what he’s up to right now, might as well drop off your stuff while we are there."
    
    show bg berthing2
    with dissolve
    
    show revan at left
    with dissolve
    
    chop "{b}Revan, make something of yourself!{/b}"
    
    revan "Ah hello, you’re the new engineer right? Welcome aboard the Charlotte."
    
    player "Pleasure to meet you, I’ll be sure to come to you if I have any concerns."
    
    chop "Come on newbie, next stop is the armory so we can issue you your gear, each crewman is given safety and combat gear, standard issue for all."
    
    player "Are we expecting to run into trouble?"
    
    chop "Meh, it happens enough. The Captain decided to make it a thing after they pissed off the commanding officer of the Valkyries organization."
    
    player "The all female military outfit? What did the Captain do to piss them off?"
    
    chop "{i}Classified.{/i} Enough chit-chat, come on nerd."
    
    scene black with fade
    
    
return