## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

## The game starts here.

image ctc_animation = Animation("gui/ctc.png", 0.2, "gui/ctc2.png", 0.2, xpos=0.96, ypos=0.99, xanchor=1.0, yanchor=1.0)
define player = Character('PVT [player_name]', ctc="ctc_animation", ctc_position="fixed", color="#7D26CD")

label start:

    scene black

    call introduction
    
    call secondscene
    
    call armoryscene
    
    #call fourthscene
    
    call morgsandchop
    #call morgsandchop from _call_morgsandchop
    
    scene hanger
    
    return
