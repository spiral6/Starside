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
    
    morgs "If we can find them first, yeah!"
    
    player "Wait, is Cedric- "
    
    #TODO: this line should have a slow down at the ellipsis
    morgs "Oh, no no no, that's my cat, he just escaped his cage... again."
    
    "I hear footsteps approaching."
    
    show soap at left
    with dissolve
    
    soap "Hey, I heard you guys chatting, am I missing out on anything?"
    
    morgs "Oh, hey Soap, say hi to the new recruit."
    
    soap "Oh, hi, sorry I didn't notice you, I'm kind of sleep deprived right now. All us deckhands are pretty busy prepping the ship to leave orbit." 
    soap "{i}yawn{/i} Yeah, pretty tired right now."
    
    player "Yeah, I can understand that. What do you do here?
    
    soap "I’m the Helmsman, I drive the ship."
    
    player "Well I guess it's a good thing you'll be able to catch up on sleep before we get going."
    
    soap "{i}yawn{/i} Hm? I wish, we’re taking off soon in like 2 hours."
    
    player "{i}Why do I have large amounts of concern now for this crew?{/i}"
    player "Ooh, well… here's hoping it goes smoothly!"
    
    soap "Anyways, I need to get back to my station, the Captain won't like it if I'm not within grabbing distance." 
    soap "{i}yawn{/i}{p}Later."
    
    
    scene black with fade
    
    
return
