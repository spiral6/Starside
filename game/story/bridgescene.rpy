define chop = Character('CDR Chop', color="#ffff00")
define arty = Character('CPT Arty', color="#ffffff")
define morgs = Character('CDR Morgs', color="#ffff00")
define soap = Character('PFC Soap', color="#ffff00")
define kuro = Character('SGT Kuro', color="#ffff00")


image bg bridge = "images/bg/bridge.jpg"

image chop = "images/char/chop.png"
image arty = "images/char/arty.png"
image morgs = "images/char/morgs.png"
image soap = "images/char/soap.png"
image kuro = "images/char/kuro.png"


label bridgescene::
    
    show bg bridge
    with dissolve
    
    show morgs at left
    with dissolve
    
    show chop at right
    with dissolve
    
    morgs "Where did that bastard run off to now... get over here Cedric..."
    
    chop "Morning Morgs, what the Hell are you doing?"
    
    morgs "Oh, hiya Chop, just crawling along the floor.. you know how it is. Actually, bloody Cedric left his room again, and I'm trying to catch him before he can go too far… or gets vented out the airlock."
    
    chop "{i}*Sigh* Mon dieu{/i}. Fine, fine, I can help but it's gotta be later. We need to introduce the new recruit to everyone."
    
    "Morgs jumps up to attention and looks at me, smile widening."
    
    morgs "Oh hey! I didn't think we would get a new one so soon! I'm Commander Morgs, bloody good to meet you, I can't believe you actually joined."
    
    player "Likewise, Commander. Uh, what do you mean b-"
    
    morgs "Oh, don't worry about that, it's just hard to come by some reliable {i}subj-{/i} {b}recruits{/b} these days."
    
    chop "Morgs is in charge of the Research and Development wing."
    
    morgs "I make any modification to the equipment you use. Usually it's just stuff like alterations to gear, tailoring, rigging explosives, adding those unnecessary lights on your armor that makes it look cool, and even experimental tools for specific jobs."
    
    player "That sounds neat, working on anything good at the moment?"
    
    morgs "Eh, a few things here and there, like a slingshot that fires bees, uh a fragmentation grenade filled with bees, bees with little cameras on them… bees, yeah."
    
    player "Why bees..?"
    
    morgs "Logistics ordered a couple crates of bees instead of cheese, meant for the galley cooks… boy were they surprised when they opened that box up."
    
    player "So you're trying to get rid of them?"
    
    scene black with fade
    
    
return