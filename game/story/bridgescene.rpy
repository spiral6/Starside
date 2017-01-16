define chop = Character('CDR Chop', color="#ffff00")
define arty = Character('CPT Arty', color="#ffffff")
define morgs = Character('CDR Morgs', color="#ffff00")
define soap = Character('SGT Soap', color="#B54B4B")
define kuro = Character('SGT Kuro', color="#B54B4B")


image bg bridge = "images/bg/bridge.jpg"

image chop = "images/char/chop.png"
image arty = "images/char/arty.png"
image morgs = "images/char/morgs.png"
image soap = "images/char/soap.png"
image kuro = "images/char/kuro.png"


label bridgescene:
    
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
    
    morgs "I make any modification to the equipment you use. Usually it's just stuff like alterations to gear, tailoring, rigging explosives, adding those unnecessary lights on your armor that makes it look cool,"
    morgs "and even experimental tools for specific jobs."
    
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
    
    #soap is going to need to be right beside morgs, it'll take a bit of coordinate editing
    
    show soap at left
    with dissolve
    
    soap "Hey, I heard you guys chatting, am I missing out on anything?"
    
    morgs "Oh, hey Soap, say hi to the new recruit."
    
    soap "Oh, hi, sorry I didn't notice you, I'm kind of sleep deprived right now. All us deckhands are pretty busy prepping the ship to leave orbit." 
    soap "{i}yawn{/i} Yeah, pretty tired right now."
    
    player "Yeah, I can understand that. What do you do here?"
    
    soap "I’m the Helmsman, I drive the ship."
    
    player "Well I guess it's a good thing you'll be able to catch up on sleep before we get going."
    
    soap "{i}yawn{/i} Hm? I wish, we’re taking off soon in like 2 hours."
    
    player "{i}Why do I have large amounts of concern now for this crew?{/i}"
    player "Ooh, well… here's hoping it goes smoothly!"
    
    soap "Anyways, I need to get back to my station, the Captain won't like it if I'm not within grabbing distance." 
    soap "{i}yawn{/i}{p}Later."
    hide soap with dissolve
    
    chop "This is where we part ways, I can show you around more later but I need to get going back to work. If you need anything just ask people like Revan or myself… or Revan…"
    
    morgs "I can take them to the Captain for this introduction, no worries."
    
    chop "Much appreciated Morgs, gotta get going, later!"
    
    hide chop with dissolve
    
    morgs "I can worry about the fluffy bastard later, you'll need to meet your Commanding Officer first."
    
    player "What's the Captain like?"
    
    morgs "Arty is nice enough if you stay on her good side. Luckily they're the understanding type and such, bad side is the Captain has a short temper. Luckily we rarely see her snap."
    
    "I hear footsteps approaching."
    
    arty "It’s not right to talk about other people when they’re not around, you know."
    
    show arty at right
    with dissolve
    
    morgs "Oh, speaking of the de- captain, here she is! Ahahaha… ha… HEY CAPTAIN SAY HELLO TO THE NEW RECRUIT."
    
    arty "Eh, I’ve heard worse. Greetings new recruit, I’m the leader of this highly-professional unit. Let me say, we are need of the extra hands and you came just in time."
    
    player "Greetings, Captain! I look forward to serving under you."
    
    arty "Ha ha, no need to be so formal, it’s not like most of the people here respect my position anyways."
    
    morgs "Don’t be so hard on yourself Captain, you know we love you, that’s why we tease you so much."
    
    arty "And I would appreciate it if you guys teased me less and worked more, but sometimes dreams have to be crushed, am I right recruit?"
    
    #choices need to be made here.
    #PNN
    menu:
        "I’m sure CDR Morgs is telling the truth, everyone speaks fondly of you.":
            pass
        "Yes Captain, it’s hard to lead sometimes.":
            pass
        "Sometimes they do, but not always.":
            pass
            
    arty "You might be right, personally I am fine so long as everyone else is happy."
    
    "I hear some more footsteps."
    
    show kuro:
        left
        xoffset 200
    with dissolve
    #this is the kuro karma counter, and depending on the score, will select how your relationship with kuro goes.
    $ kurokarma = 0
    
    kuro "Captain, the Medical Bay is secured and stocked, ready for launch."
    
    arty "Good to hear, make sure you let Lieutenant Nixxy know the Medical Wing is off for the rest of the day. Oh, Kuro, meet the new recruit, they just showed up today."
    
    kuro "{i}flustered{/i} Ah, I’m so sorry, I didn’t notice you! P-pleasure to meet you. I’m Sergeant Kuro, I’m a nurse in the Medical Wing… I don’t do well with strangers so I’m… really sorry if I seem weird."
    
    #more choices, but these are directly influential, a Good/Bad route variable will have to be set here.
    #NPN
    menu:
        "It’s great to meet you, hopefully we see each other often.":
            python:
                kurokarma+=-1
            pass
        "Don’t worry about it, we can get to know each other later.":
            python:
                kurokarma+=1
            pass
        "Most cute girls typically are weird, you especially.":
            python:
                kurokarma+=-1
            pass
    kuro "{i}fidgets with collar{/i}"
    
    arty "Hey [player_name], what kind of stuff are you hoping to accomplish while you’re with us?"
    
    #and some more choices, unsure if influential or not.
    #NNP
    menu:
        "Honestly, whatever needs doing, I’m a bit strapped for cash.":
            pass
        "I want to follow this unit into the deepest pits of hell and back.":
            pass
        "I don’t know what I want to do yet, but I guess that’s kind of why I’m here.":
            pass
    
    arty "Good answer, even if you’re just a temp worker. If we like you enough we’ll hire you as a permanent member of the family! I’m sure Kuro wouldn’t mind that, right?"
    
    kuro "…I have some… {p}medicine to organize…"
    
    #another set of influential choices, NPN
    menu:
        "Captain I’m sure I shouldn’t bother the Sergeant right now.":
            pass
        "Strangers are just friends you haven’t met yet.":
            pass
        "Maybe later I can get to know her more personally.":
            pass
    
    scene black with fade
    
    
return
