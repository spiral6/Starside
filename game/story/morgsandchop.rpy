## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define morgs_char = Character('CDR Morgs', color="ff0000")
define chop_char = Character('LCDR Chop', color="#ffff00")
define player = Character('Player')

image morgs = "morgs.png"
image chop = "chop.png"
image bg office = "morgsoffice.jpg"

## The game starts here.

label morgsandchop:

    ## Show a background. This uses a placeholder by default, but you can add a
    ## file (named either "bg room.png" or "bg room.jpg") to the images
    ## directory to show it.

    scene bg office
    
    "After the awkward conversation with the armory attendant, I leave the armory and makes way to Morgs’ office. Before arriving, I see Chop entering Morgs’ office. I wonder what they're talking about?"

    "Eavesdrop? Or Report in?"

    "I guess I'll eavesdrop on the conversation."

    "Inside, Morgs is sitting at her desk with the chair turned towards Chop."
    
    show chop at right
    with dissolve
    show morgs at left
    with dissolve
    
    
    chop_char "Morgs, I need some volunteers from your command. I’m running a...um....a new training exercise."
    
    morgs_char "Hmm? What’s the training for? Couldn’t you pull someone from yours or Rod’s department?"
    
    chop_char "Classified, Morgs."
    
    morgs_char "Sweetheart, you remember that I outrank you, right?"
    
    chop_char "Captain’s orders!"

    "Morgs makes a suspicious glare at Chop."
    
    morgs_char "Ri~ight. Let me see who is available today."
    
    "Morgs pulls out her mobiglass and begins scrolling through the crew’s roster."
    
    morgs_char "So, when are you running this--what did you call it--{i}training exercise{/i}?"
    
    chop_char "Tonight. It starts tonight and will last until tomorrow."
    
    morgs_char "Starting so soon? With most of my people still on duty I’m not sure whom I can spare. Exactly how many do you need?"
    
    "Chop begins daydreaming."
    
    chop_char "(mumbles) One is all I need."
    
    morgs_char "I couldn’t hear you. What was that?"
    
    "Chop snaps back to reality."
    
    chop_char"(Clears throat) One! Just one is enough!"
    
    morgs_char "One? What kind of training only needs one trainee?"
    
    chop_char "It’s still in the works. I wanted run a test--to see if I should implement this as a new training regimen."
    
    morgs_char "And where might this new “training regimen” be taking place?"
    
    chop_char "Well, since we’re passing by Serenity Station tonight I thought we could..."
    
    morgs_char "Ah! If it’s Serenity you’re going to, the you must be going to that one famous restaurant! What was its name? Chantelle! That’s it!"
    
    chop_char "Never heard of it!"

    morgs_char "Oh come now Chop, you have its menu pinned to the wall of your office!"
    
    chop_char "W-Wha--how did you--Nevermind that! Is anyone from your unit available?"
    
    "Morgs gives Chop a sly glance before returning to the mobiglass."
    
    morgs_char "Let’s see. The Lieutenant is off on a diplomatic matter; the brothers are still on shore leave; and both Private Celly and Corporal Kadrag are accompanying me on an assignment later today.\nThat leaves just one si~ingle lonely Corporal--"
    
    chop_char "Look, do you have anyone or not?!"
    
    morgs_char "She’s all yours, Chop. Play nice."
    
    "Morgs winks at Chop."
    
    chop_char "Not a single word to anyone about this!"
    
    morgs_char "I wouldn’t dare!"
    
    "Morgs tilts her head past Chop, focusing on the doorway."
    
    morgs_char "You can come in now!"
    
    "Chop turns and sees me in the doorway, eavesdropping. Her eyes widen with shock."
    
    morgs_char "You’ve been there for quite a while now, haven’t you? Come in! Come in!"
    
    player "Yes ma’am."
    
    "I step into Morgs’ office. Chop’s eyes are locked on me."
    
    chop_char "Rookie, if anything ever leaves this room...{b}I swear--on my herald!--I will end you. Do I make myself clear?{/b}"
    
    "I salute in fear."
    
    player "Crystal, ma’am!"
    
    chop_char "{b}G-Good!{/b}"
    
    "Chop stomps past me, mixed with feelings of fear, embarrassment, and triumph."
    
    hide chop
    with dissolve
    
    player "What was that all about?"
    
    morgs_char "A training exercise. Nothing more."
    
    player "R-Right..."
    
    scene black
    with fade
    
    return
