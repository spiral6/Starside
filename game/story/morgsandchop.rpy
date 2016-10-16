## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define morgs = Character('CDR Morgs', color="ff0000")
define chop = Character('LCDR Chop', color="#ffff00")

image morgs = "images/char/morgs.png"
image chop = "images/char/chop.png"
image bg office = "images/bg/morgsoffice.jpg"

## The game starts here.

label morgsandchop:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg office
    with dissolve
    
    "After the awkward conversation with the armory attendant, I leave the armory and makes way to Morgs’ office. Before arriving, I see Chop entering Morgs’ office. I wonder what they're talking about?"

    "Eavesdrop? Or Report in?"

    "I guess I'll eavesdrop on the conversation."

    "Inside, Morgs is sitting at her desk with the chair turned towards Chop."
    
    show chop at right
    with dissolve
    show morgs at left
    with dissolve
    
    chop "Morgs, I need some volunteers from your command. I’m running a...um....a new training exercise."
    
    morgs "Hmm? What’s the training for? Couldn’t you pull someone from yours or Rod’s department?"
    
    chop "Classified, Morgs."
    
    morgs "Sweetheart, you remember that I outrank you, right?"
    
    chop "Captain’s orders!"

    "Morgs makes a suspicious glare at Chop."
    
    morgs "{i}Ri~ight.{/i} Let me see who is available today."
    
    "Morgs pulls out her mobiglass and begins scrolling through the crew’s roster."
    
    morgs "So, when are you running this--what did you call it--{i}training exercise{/i}?"
    
    chop "Tonight. It starts tonight and will last until tomorrow."
    
    morgs "Starting so soon? With most of my people still on duty I’m not sure whom I can spare. Exactly how many do you need?"
    
    "Chop begins daydreaming."
    
    chop "{i}(mumbles){/i} One is all I need."
    
    morgs "I couldn’t hear you. What was that?"
    
    "Chop snaps back to reality."
    
    chop"{i}(Clears throat){/i} One! Just one is enough!"
    
    morgs "One? What kind of training only needs one trainee?"
    
    chop "It’s still in the works. I wanted run a test--to see if I should implement this as a new training regimen."
    
    morgs "And where might this new {i}“training regimen”{/i} be taking place?"
    
    chop "Well, since we’re passing by Serenity Station tonight I thought we could..."
    
    morgs "Ah! If it’s Serenity you’re going to, the you must be going to that one famous restaurant! What was its name? {i}Chantelle!{/i} That’s it!"
    
    chop "Never heard of it!"

    morgs "Oh come now Chop, you have its menu pinned to the wall of your office!"
    
    chop "{i}W-Wha--how did you--{/i}Nevermind that! Is anyone from your unit available?"
    
    "Morgs gives Chop a sly glance before returning to the mobiglass."
    
    morgs "Let’s see. The Lieutenant is off on a diplomatic matter; the brothers are still on shore leave; and both Private Celly and Corporal Kadrag are accompanying me on an assignment later "
    morgs "today.{p}{i}That leaves just one si~ingle lonely Corporal--{/i}"
    
    chop "Look, do you have anyone or not?!"
    
    morgs "She’s all yours, Chop. {i}Play nice.{/i}"
    
    "Morgs winks at Chop."
    
    chop "Not a single word to anyone about this!"
    
    morgs "I wouldn’t dare!"
    
    "Morgs tilts her head past Chop, focusing on the doorway."
    
    morgs "You can come in now!"
    
    "Chop turns and sees me in the doorway, eavesdropping. Her eyes widen with shock."
    
    morgs "You’ve been there for quite a while now, haven’t you? {p}{i}Come in! Come in!{/i}"
    
    player "Yes, ma’am."
    
    "I step into Morgs’ office. Chop’s eyes are locked on me."
    
    chop "Rookie, if anything ever leaves this room...{p}{b}I swear--on my herald!--I will end you. {p}{i}Do I make myself clear?!{/i}{/b}"
    
    "I salute in fear."
    
    player "Crystal, ma’am!"
    
    chop "{b}G-Good!{/b}"
    
    "Chop stomps past me, mixed with feelings of fear, embarrassment, and triumph."
    
    hide chop with dissolve
    
    player "What was that all about?"
    
    morgs "A training exercise. Nothing more."
    
    player "R-Right..."
    
    hide morgs with dissolve
    
    scene black 
    with fade
    
    return
