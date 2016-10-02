## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

define morgs_char = Character('CDR Morgs')
define chop_char = Character('LCDR Chop')
define player = Character('Player')


## The game starts here.

label start:

    jump firstscene

    ##after jay
    
    jump morgsandchop

    scene bg room



    return
