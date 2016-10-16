define chop = Character('CDR Chop', color="#ffff00")
define jay = Character('PFC Jayhawk', color="#ffff00")

image bg armory = "images/bg/armory.jpg"
image jay = "images/char/jay.png"
image chop = "images/char/chop.png"

label armoryscene:
    
    show bg armory
    with dissolve
    
    show chop at right
    with dissolve
    
    "Chop knocks on the window."
    
    chop "Hey fuckfaces, are y’all in there? Where the hell are those assholes..."
    
    "I hear shuffling. A person suddenly appears wearing pajamas and eating a bowl of cereal."
    
    show jay at left
    with dissolve
    
    jay "Hello! What can I do ya for, eh?"
    
    chop "Disrespect aside, we need standard gear for a new scruby."
    
    player "I’m right here..."
    
    jay "Alright, hold on, I was working on this bomb ass breakfast, but I’ll put it away just for you, eh?"
    
    player "Is he wearing pajamas, and eating in the armory?"
    
    chop "PFC Jay is originally from Canada, on Earth."
    
    player "Oh, that’s pretty inter- {p}{i}wait that doesn’t answe-{/i}"
    
    jay "Alright, so turns out someone forgot to pack new gear crates *cough* so we’ll get that together when we get a chance to and have it sent to your bunk."
    jay "With that taken care of, if you need anything from the armory I’m always here... {p}{i}Sleeping... in the corner on the cold hard ground...{/i}"
    
    player "Seriously? That sounds horrible, why would you do that?"
    
    jay "It’s a hard job, if I don’t sleep with these weapons… who will? I do it from the good of my heart, eh?"
    
    chop "Welp, I’m bored, let’s go to one more spot before I let you go. {p}Gonna take you to the ship’s bridge so you can meet all the commanders."
    
    jay "Chop, before you go, think you can remind the captain about my request to R&D for those new remote explosives?"
    
    scene black with fade
    
    
return