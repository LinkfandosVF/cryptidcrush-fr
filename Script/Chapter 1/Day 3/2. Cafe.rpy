
label Ch1_CafeDay3:
    python:
        musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=1,fadeOut=1)
        timeText = "10:00AM"

        adjustChar("Robyn",eye=4,brow=2,mouth=3,armR=0)
        adjustChar("Robbie",armR=1,eye=2)

    scene BG Cafe:
        matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")

    camera:
        camera_zoom(z=-280,x=-100)
        shaded("#ffe7ee")
        camera_zoom(z=-280,x=-190,t=1.5)

    show robyn:
        xcenter -0.25
        matrixtransform RotateMatrix(0,0,0)
        ease 2.0 xcenter 0.4
        ease 0.4 matrixtransform RotateMatrix(0,180,0)

    show robbie behind robyn:
        xcenter 0.15

    show jamie cafe:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.8

    show edward behind robbie:
        xcenter 0.3
        blur 3
        zoom 0.7
        matrixcolor TintMatrix("#bdd2ff")

    show sera behind robbie at flipped:
        xcenter 0.45
        blur 3
        zoom 0.7
        matrixcolor TintMatrix("#bdd2ff")

    with pixellate

    Narrator "Robbie catches your eye; he’s hunched over a tiny cup of coffee."

    python:
        adjustChar("Robyn",mouth=4,brow=1)
        adjustChar("Robbie",eye=0,mouth=3)

    Robyn "Rob? I thought you hated Longhope coffee."

    voice robbie_wow

    python:
        adjustChar("Robyn",mouth=5,brow=0)
        adjustChar("Robbie",eye=7,mouth=7)

    Robert "{i}The barista's cute.{/i}"
    $adjustChar("Robbie",eye=3,mouth=1)

    voice robbie_laughb

    Robert "Eheheh heh!"

    python:
        adjustChar("Robyn",mouth=3,brow=2,eyes=1)
        adjustChar("Robbie",mouth=0)

    Robert "Bad coffee is better than no coffee."

    Robyn "That's where our philosophies diverge."

    voice robbie_eh

    python:
        adjustChar("Robyn",mouth=5,brow=2,eyes=3)
        adjustChar("Robbie",mouth=1,eye=1)

    Robert "It eases the nightmares and lingering headaches."

    python:
        adjustChar("Robyn",mouth=4,brow=1,eyes=0)
        adjustChar("Robbie",mouth=0,eye=0)

    Robyn "Nightmares?"

    python:
        adjustChar("Robyn",mouth=5)
        adjustChar("Robbie",mouth=6,eye=3)

    Robert "Ya, like someone's digging through your memories and twisting 'em up!"
    python:
        adjustChar("Robyn",mouth=4,brow=2)
        adjustChar("Robbie",mouth=0,eye=0)

    Robyn "The same thing's been happening to me!"
    python:
        adjustChar("Robyn",mouth=5,brow=2)
        adjustChar("Robbie",mouth=3,eye=5)

    Robert "Y'mean, you see it too?"
    $adjustChar("Robyn",mouth=1,brow=3,eyes=3)

    Robyn "See-{nw}"
    $adjustChar("Robyn",mouth=4,eyes=4,brow=2)

    extend "\n\nSee what?"

    $adjustChar("Robyn",mouth=3,eyes=1)

    python:
        adjustChar("Robyn",mouth=5,eyes=4)
        adjustChar("Robbie",mouth=2,eye=0)

    Robert "The dice."

    Narrator "He's onto you. You've never done it around him have you? How can he tell? You don't control the dice!"
    python:
        adjustChar("Robbie",mouth=3,eye=5)
        adjustChar("Robyn",mouth=1,eyes=2,brow=0)

    Robert "Who'd ya strike a deal with to snag that kinda power?"

    Robyn "The what?"

    $adjustChar("Robbie",eye=5,mouth=0)

    call dice_roll(rMod=PC_Stats.cStats("charm"), rDiff=9, rDesc="Froggy Charm") from _call_dice_roll_90

    camera:
        shaded("#ffe7ee")
    python:
        adjustChar("Robbie",eye=3,mouth=6)
        adjustChar("Robyn",brow=1,eyes=0,mouth=1)

    show robbie at jumpSquish(0.15,150,0.25)

    Robert "{sc}{b}THAT! I SAW THAT!{/b}{/sc}"

    show robbie at hoppies(xIntensity=2.5)
    python:
        adjustChar("Robbie",eye=6,mouth=0)
    Robert "{sc=1}Don't do it again! You're gonna hurt somebody!{/sc}"

    show robbie:
        ease 0.15 yoffset 0
    python:
        adjustChar("Robyn",mouth=5,brow=2,eyes=2)
        adjustChar("Robbie",mouth=3,eye=5)

    Robyn "It didn't do anything?"

    python:
        adjustChar("Robyn",mouth=1,eyes=1)
        adjustChar("Robbie",mouth=0,eye=3)

    Robert "N-nothing changed?"

    python:
        adjustChar("Robyn",mouth=5,brow=1,eyes=4)
        adjustChar("Robbie",eye=1,mouth=7)

    Robert "Hmgh."

    python:
        adjustChar("Robyn",brow=0,eyes=2)

    Narrator "Frogman doesn't know what he's talking about."

    Robyn "Ah,.,{nw}"
    show robyn at vibratenum
    python:
        adjustChar("Robyn",brow=2,eyes=3,mouth=0)

    extend "\n\nHow about that coffee huh?"

    python:
        adjustChar("Robbie",mouth=3,eye=3)

    Robert "{sc=3}-?{/sc}"

    voice robbie_laugha

    show robbie at vibratenum:
        xcenter 0.15

    python:
        adjustChar("Robyn",brow=0,eyes=2)
        adjustChar("Robbie",mouth=5,eye=0)
    extend "\n\nThe coffee's great!"

    # Sidenote I THINK IT'LL BE FUNNIER IF THE ROLL ACTUALLY DOES NOTHING
    #
    # failure
    #     camera:
    #         shaded("#ffe7ee")
    #     python:
    #         adjustChar("Robyn",mouth=5,brow=2,eyes=3)
    #         adjustChar("Robbie",mouth=3,eye=1)
    #
    #     Robert "I'm talking about the dice."
    #
    #     python:
    #         adjustChar("Robyn",eyes=1,brow=2,mouth=1)
    #         adjustChar("Robbie",mouth=0,eye=1)
    #
    #     Robert "I see it too."

    python:
        adjustChar("Robbie",mouth=0,eye=3)
        adjustChar("MM",mouth=6,eyes=5,armR=0,armL=0)

    show madhouse:
        xcenter 0.45
        matrixtransform RotateMatrix(0,0,15)
        parallel:
            pause 0.1
            jumpSquish(0.15,150,0.25)
        parallel:
            alpha 0 blur 10
            ease 0.3 alpha 1 blur 0

    Madhouse "{b}BOO!{/b}{nw}"

    show madhouse:
        alpha 1 blur 0
        ease 0.4 matrixtransform rotated(z=-10) xoffset -100 yoffset 0 xzoom 1 yzoom 1
        idleFloat(2,10)

    extend "\n\nAnd ah, ribbit, ribbit."
    python:
        adjustChar("Robyn",mouth=5,eyes=0)
        adjustChar("Robbie",eye=0,mouth=4)
        adjustChar("MM",mouth=5,eyes=1,armR=1,armL=1)

    show robbie:
        jumpSquish(0.15,150,0.25)

    voice robbie_ribbitb
    Robert "{size=60}{b}RIBBIT!!{/b}{/size}{nw}"
    python:
        adjustChar("Robbie",eye=7,mouth=7)

    extend "\n\nUhck."
    voice robbie_seething

    python:
        adjustChar("Robyn",mouth=5,eyes=0)
        adjustChar("Robbie",eye=5,mouth=3)

    Robert "Don't make me bite you."
    python:
        adjustChar("Robyn",mouth=1,eyes=1,brow=1)
        adjustChar("MM",eyes=1)
        adjustChar("Robbie",eye=0,mouth=0)

    show robyn:
        xcenter 0.4
        ease 1.75 xcenter 0.55
        unflipCharDelayed(0.8,0.5)

    Robert "If I can. What're you supposed to be?"

    Madhouse "I'm.,.,{nw}"
    $adjustChar("MM",mouth=11,eyes=0,armR=0,armL=0)

    show madhouse:
        parallel:
            hoppies(xIntensity=4)
        parallel:
            startledSquish

    extend " a., {b}DEMON!{/b}"

    Robert "A demon?"
    $adjustChar("MM",mouth=6,eyes=0,armR=1,armL=1)

    Madhouse "{bt=3}A dehehehemon!{/bt}"

    python:
        adjustChar("Robyn",mouth=5,brow=0)
        adjustChar("Robbie",eye=3,mouth=3)
        adjustChar("MM",mouth=3,eyes=3)

    show madhouse:
        ease 0.3 xcenter 0.45 matrixtransform RotateMatrix(0,0,0)
        idleFloat(2,10)

    Jamie "{size=35}A DEMON?{/size}"
    python:
        adjustChar("Robyn",mouth=5,brows=0,eyes=0)
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Jamie",eye=2,mouth=4,wispEyes=1,brow=0,sweat=0)

    camera:
        camera_zoom(x=100,y=-30,z=-150,t=2)

    show jamie cafe:
        unflipCharDelayed(0.8,0.5)
    show sera:
        unflipCharDelayed(0.8,0.5)

    Narrator "Jamie laughs from across the cafe."

    python:
        adjustChar("Robyn",brows=0,eyes=4)
        adjustChar("Jamie",mouth=0,eye=1,wispEyes=0)
        adjustChar("MM",mouth=4,eyes=5)
        adjustChar("Robbie",eye=7)

    show robyn default:
        xcenter 0.55

    show jamie cafe:
        matrixtransform RotateMatrix(0,0,0)

    Jamie "With those horns? You're joking."

    show madhouse:
        parallel:
            flipCharDelayed(0.8,0.5)
        parallel:
            idleFloat(2,10)

    Madhouse "Oh great."

    show sera:
        ease 3 xcenter -0.1
    python:
        adjustChar("Robyn",brows=1,eyes=2)
        adjustChar("MM",mouth=3,eyes=0)
        adjustChar("Jamie",eye=1,wispEyes=1)

    Jamie "My break's in fifteen minutes, if you don't mind waiting."

    python:
        adjustChar("Robyn",brows=1,eyes=2)
        adjustChar("MM",mouth=1)
        adjustChar("Jamie",eye=1,wispEyes=3)

    Madhouse "Waiting for what?"

    Jamie "Our., {b}rematch{/b}."

    python:
        adjustChar("MM",mouth=10,eyes=7,wispEyes=1)
        adjustChar("Robyn",brows=0,eyes=0)
    pause 0.5

    Jamie "Don’t tell me you’ve forgotten."

    python:
        adjustChar("MM",mouth=7,eyes=2)

    Madhouse "Oh, dear Jamie."

    show robbie behind robyn:
        xcenter 0.15
        ease 2 xcenter -0.1

    python:
        adjustChar("MM",mouth=6,eyes=2)
        adjustChar("Robyn",brows=0,eyes=1)

    extend "\n\nI'm a changed man, a better man. The only devil I wrestle with is the one inside my heart."
    $adjustChar("MM",mouth=9,eyes=0,armL=3)

    show edward:
        ease 2 xcenter 0.19

    show madhouse:
        parallel:
            unflipCharDelayed(0.8,0.5)
        parallel:
            idleFloat(2,10)
    hide robbie

    Madhouse "Which means, I'll be turning the other cheek."
    python:
        adjustChar("Jamie",eye=0,brow=2,mouth=4)
        adjustChar("Edward",eyes=1,mouth=0)

    Jamie "My, I never took you for such a gentleman."

    python:
        adjustChar("Jamie",eye=2,brow=1,mouth=0)
        adjustChar("Edward",eyes=3,mouth=2)

    Jamie "Meet me at the dirt lot past Edith's shop. Before sundown."

    show madhouse:
        matrixtransform RotateMatrix(0,180,0)
        startledSquish
        idleFloat(2,10)

    python:
        adjustChar("MM",mouth=12,armL=0,armR=0)
        adjustChar("Robyn",brows=1,eyes=3)

    Madhouse "That’s such short notice! I’m a busy ghoul! I’ll have to check in with my producer, and clear my schedule!"

    python:
        adjustChar("Robyn",brows=3,eyes=4)
        adjustChar("Jamie",eye=6,brow=1,mouth=2)
        adjustChar("MM",mouth=4)
        adjustChar("Edward",eyes=1,mouth=3)

    Jamie "..."
    $adjustChar("MM",mouth=11)

    Madhouse "But I'll add you to the wait list."
    python:
        adjustChar("Robyn",brows=0,eyes=4)
        adjustChar("Jamie",eye=7,mouth=0)
        adjustChar("Edward",eyes=0,mouth=0)

    show edward:
        ease 2 xcenter -0.1

    Jamie "..."

    Narrator "Jamie’s not going to back off."

    python:
        adjustChar("Robyn",brows=0,eyes=1)
        adjustChar("MM",mouth=1,armR=2,armL=2,eyes=7)

    Madhouse "{b}FINE!{/b}"
    $adjustChar("MM",mouth=0,eyes=10,armL=1,armR=1)

    Madhouse "I hope you like the taste of brimstone, Bonehead."
    $adjustChar("MM",mouth=9,eyes=5,armL=1)

    extend "\n\n'Cause I'm gonna send you back to {b}Hell{/b}."

    python:
        adjustChar("Robyn",brows=0,eyes=4)
        adjustChar("MM",mouth=3,eyes=4,armR=2,armL=2)
        adjustChar("Jamie",eye=10,sweat=1,brow=0)

    Jamie "Mike, I'm from Atlantic City."

    Madhouse "Oh!"

    python:
        adjustChar("Robyn",brows=0,eyes=4)
        adjustChar("MM",mouth=9,eyes=5,armL=1,armR=1)
        adjustChar("Jamie",eye=7,mouth=2)
    $musicPlayer.playSong(song="wrath_of_the_recolors")

    Madhouse "{bt=4}{b}Atlantic City.{/b}{/bt}"

    scene BG Black with Dissolve(0.5)
    Jamie "So, what can I get you?"

    Narrator "You order a plain bagel and eventually leave the coffee shop."

label Ch1_CafeDay3_August:
    python:
        musicPlayer.playSong(song="boots_on_the_shore_bearsome",fadeIn=1,fadeOut=2)
        timeText = "10:20AM"
        adjustChar("Robyn",mouth=0,brow=0,eyes=2)
        adjustChar("August",eye=3,eyeFrame=2,brow=2,hair=2,sweater=1,mouth=5,wolfEars=0,coat=0)

    camera at camera_default
    scene BG Near Cafe
    with quickDissolve

    camera:
        camera_zoom(z=-600,y=-200,x=400)
        camera_zoom(z=-200,t=4.0)
        shaded("#ffe7ee")

    show madhouse:
        yoffset 700
        xcenter 0.5

    show robyn:
        enterFromLeft(x=0.35,t=3.5)

    show august:
        xcenter 0.65

    Narrator "Outside the cafe, you bump into August."

    Robyn "Oh, morning Gus!"

    show august:
        flipChar(0.4)

    $adjustChar("August",eye=3,eyeFrame=0)

    August "Hey, have you seen Atlas?"

    $adjustChar("Robyn",brow=2)

    Robyn "Not since yesterday."

    $adjustChar("August",brow=1,eyeFrame=2)
    August "He was gonna run in and nab a blueberry muffin for me."

    August "But I guess he...{nw}"

    $adjustChar("August",brow=4,eyeFrame=3)
    show august:
        unflipChar(0.4)

    extend " wandered off."

    show robyn:
        nodding()

    Robyn "Sounds about right."
    python:
        adjustChar("Robyn",mouth=1,brow=0)
        adjustChar("August",eye=1,eyeFrame=0,brow=0,mouth=6)

    August "{sc}Ergh!{/sc}"

    show august:
        flipChar(0.4)

    $adjustChar("August",eye=3,eyeFrame=2,brow=1,mouth=6)

    August "Sorry. I’m on call, so I’m a bit on edge."

    $adjustChar("Robyn",mouth=3)
    Robyn "What do you do for work?"

    $adjustChar("August",eye=2,eyeFrame=0,brow=1,mouth=1)
    August "I'm a tracker."

    $adjustChar("August",eye=4,eyeFrame=0,brow=2,mouth=3)
    August "Occasionally a lost hiker wanders into our woods. {nw}"

    $adjustChar("August",eye=0,eyeFrame=0,brow=2,mouth=6)
    extend "\n\nAnd it's my job to find 'em."

    Robyn "People can walk into Longhope just like that?"

    camera:
        camera_zoom(z=-450,x=-50,t=0.5)

    $adjustChar("August",eye=2,eyeFrame=3,brow=4,mouth=5)

    show august:
        xoffset 0
        pause 0.1
        ease 0.4 matrixtransform rotated(y=180,z=-15) xoffset -100

    show madhouse:
        xcenter 0.425
        yoffset 500
        matrixtransform rotated(y=180)
        ease 10.0 yoffset 160

    August  "If they're unlucky."

    August "Most days it's boring trail maintenance. Moving logs, picking up trash, and all that."

    $adjustChar("August",eye=4,eyeFrame=0,brow=2,mouth=1)
    August  "Visitors are pretty sparse once the leaves fall."

    $adjustChar("August",eye=1,eyeFrame=0,brow=2,mouth=0)
    show madhouse:
        ease 0.5 yoffset 160

    Madhouse "What about {b}cryptid hunters{/b}?"

    python:
        adjustChar("Robyn",eyes=1)
        adjustChar("August",eye=3,eyeFrame=2,mouth=5)
        adjustChar("MM",mouth=1)

    camera:
        camera_zoom(z=-300,t=1.5)

    show robyn:
        ease 0.5 xcenter 0.3

    show madhouse:
        ease 1.0 yoffset 0 xcenter 0.45
        idleFloat(2.2,10)

    show august:
        matrixtransform rotated(y=180,z=-15)
        ease 1.5 matrixtransform rotated(y=180) xoffset 0

    Madhouse "Back at the station there'd be packs of hunters creeping around looking for their five minutes of fame."

    Robyn "Hunter's a pretty strong word."
    $adjustChar("MM",mouth=9,eyes=0)

    show madhouse:
        yoffset 0
        xcenter 0.45
        unflipChar(0.5)
        idleFloat(2.2,10)

    Madhouse "Oh yeah?"

    Robyn "Cryptozoologists are documenters! They're supposed to observe not disrupt."

    #camera:
        #camera_zoom(z=-525,x=-150,y=-40,t=0.5)

    $adjustChar("MM",mouth=5)
    Madhouse "You ever had a camera shoved in your face? That's pretty disruptive!"

    Robyn "I guess so."

    python:
        adjustChar("MM",eyes=0,mouth=2)
        adjustChar("August",eye=0,mouth=5)

    August "Jeez, don’t even get me started on those hunter types."

    $adjustChar("August",eye=2,mouth=1)

    August "You don't think much of it until you’re on the receiving end of a media storm."

    show madhouse:
        yoffset 0
        parallel:
            ease 0.6 matrixtransform rotated(y=180)
        parallel:
            ease 0.3 yoffset 10
            ease 0.3 yoffset 0
        idleFloat(2.2,10)

    python:
        adjustChar("MM",mouth=6,eyes=5,armR=1,armL=1)
        adjustChar("August",mouth=5)

    Madhouse "You? No way."

    python:
        adjustChar("August",eye=3,brow=0,mouth=1)
        adjustChar("Robyn",eyes=2,mouth=6)

    August "You’re not the only urban legend around here!"

    python:
        adjustChar("Robyn",brow=2)
        adjustChar("August",eye=0,eyeFrame=3,mouth=2)
        adjustChar("MM",mouth=2)

    #show august:
    #    matrixtransform rotated(y=180)

    #    ease 0.4 matrixtransform rotated(y=180,z=-10)

    August "I had a desperado phase."

    $adjustChar("August",eye=3,eyeFrame=2,brow=2,mouth=5)

    #show august:
        #matrixtransform rotated(y=180,z=-10)
        #ease 0.4 matrixtransform rotated(y=180)

    August "How’d you two get stuck together anyway?"

    python:
        adjustChar("Robyn",eyes=1,mouth=4,brow=0)

    Robyn "I snuck into Elkhorn station and left with a stowaway."

    python:
        adjustChar("Robyn",mouth=0,eyes=3)
        adjustChar("MM",mouth=0,eyes=2)

    Robyn "Looks like I stole the star of the operation."

    Madhouse "The shining star."

    Robyn "That reminds me-{nw}"

    menu:
        extend ""

        "Have you seen anything freaky around here?":
            python:
                adjustChar("August",brow=0,mouth=2)
                adjustChar("Robyn",eyes=2,mouth=5)
                adjustChar("MM",eyes=0)

            August "There were rumors of a eight legged, two face fiend roaming the woods last fall. I was ordered to find the damn thing."

            August "Turns out this dreadful beast were two brawling jackalopes with their antlers locked."

            August "I managed to get them untangled thank god, but christ those things can kick."

            $adjustChar("Robyn",mouth=4)
            $adjustChar("MM",mouth=1,eyes=1)
            Robyn "Jackalopes?!"

            August  "Of course! They're real cute, cuddly, and aside from the moose variety, mighty timid."

            Madhouse "Can I see one?"

            August "Sure if you can find one."

        "Can you talk to animals?":
            $adjustChar("August",brow=1,mouth=1)
            August  "Only chickens."

            python:
                adjustChar("August",brow=2,mouth=0,eye=2)
                adjustChar("Robyn",eyes=1,brow=1,mouth=1)
                adjustChar("MM",mouth=11,eyes=0)

            Madhouse "BAHAH! Like, cluck cluck?"

            August  "My nana owned a farm! Hens were the only critters patient enough to put up with me."

            python:
                adjustChar("Robyn",eyes=4,brow=2,mouth=0)

            Robyn "Yeaaah, I took three years of German back in high-school but it never stuck."

            $adjustChar("MM",mouth=6)

            Madhouse "I speak possum!"

            $adjustChar("August",mouth=3,eye=3)
            August "Neat. You'd have to teach us a few handy phrases sometime."

            $adjustChar("Robyn",mouth=0)
            Madhouse "Hehe, yeah!"

        "Met any cute hikers?":

            python:
                adjustChar("August",eye=2,mouth=1,brow=2,eyeFrame=4)
                adjustChar("MM",eyes=0,mouth=2)
                adjustChar("Robyn",eyes=2,brow=0,mouth=0)

            August "Yeah, ah, I've had some pleasant encounters."

            $adjustChar("August",eye=3,mouth=5,eyeFrame=2)

            August  "Hiking enthusiasts are a rowdy bunch. Some nights if I'm feeling bold I'll introduce myself."

            $adjustChar("August",eye=2,mouth=5,brow=1)

            August "{b}Spruce{/b} would always chew me out for chatting it up."

            $adjustChar("August",eyeFrame=0,eye=4,mouth=3,brow=2)

            August  "{bt=3}But I’m a lycanthrope not a misanthrope!{/bt}"

            show madhouse:
                xcenter 0.45
                ease 1.0 yoffset 0 xcenter 0.42
                idleFloat(2.2,10)

            python:
                adjustChar("MM",mouth=1,eyes=5)
                adjustChar("Robyn",brow=2,mouth=2,eyes=3)
                adjustChar("August",mouth=2)

            Narrator "Corny."

            python:
                adjustChar("Robyn",eyes=4,mouth=5,brow=0)
                adjustChar("August",eye=2,mouth=5,brow=1)

            Robyn "Who's Spruce?"

            $adjustChar("August",eyeFrame=0,brow=2,mouth=1,eye=3)

            August "The peacekeeper."

            $adjustChar("August",eye=0,mouth=5,brow=0,eyeFrame=1)
            August "They were voted mayor this past spring.{nw}"

            python:
                adjustChar("MM",eyes=4)
                adjustChar("Robyn",mouth=1)
                adjustChar("August",eye=1,mouth=6,brow=2,eyeFrame=0)

            extend  "\n\nOnly to vanish the day of the swearing in ceremony."

            python:
                adjustChar("Robyn",brow=1,mouth=4,eyes=0)
                adjustChar("August",eye=3,mouth=5,eyeFrame=2)

            Robyn "{size=30}VANISH?{/size}"

            python:
                adjustChar("Robyn",mouth=5,eyes=2)
                adjustChar("August",eye=2,brow=1,eyeFrame=2,mouth=0)
            August  "Cryptids are known to do that."

    show august:
        ease 0.75 xcenter 0.65 matrixtransform rotated(y=180) xoffset 0

    python:
        adjustChar("August",mouth=1,brow=1,eyeFrame=2,eye=3)
        adjustChar("Robyn",eyes=2,mouth=0,brow=0)
        adjustChar("MM",mouth=0,eyes=0)

    August "That reminds me! After our little excursion last night I wanted to give you this."

    show CGShade

    show CGlonghope_map

    Narrator "August reaches into his back pocket, unfolds a map, and hands it off to you."

    August "Ta-dah! It's not the greatest map but it'll do. \n\n{size=15}And my phone number in case you get lost.{/size}"

    Robyn "Did you make this?"

    August "Yep! Cell service is pretty spotty in some areas, so it's good to have a paper map."

    Madhouse "I can see Elkhorn Station from here!"

    Robyn "I wanna visit that Haunted Manor."

    Madhouse "No! No more ghosts. I'm sick of 'em."

    August "Bwahaha! Don't worry it ain't so bad during the day."

    hide CGlonghope_map with None
    hide CGShade with nwDissolve(0.5)

    August "So, what's the plan now? Since we failed to find the Mean Green's grave."

    $adjustChar("MM",mouth=2)
    Madhouse "I still want my hat."

    python:
        adjustChar("August",mouth=5,brow=2)
        adjustChar("MM",mouth=3)
        adjustChar("Robyn",mouth=5,eyes=2)

    August  "Got any relatives? They might've kept your belongings."

    $adjustChar("MM",mouth=12,eyes=0)

    Madhouse "Any {b}real{/b} family would've burned Elkhorn station to the ground by now!"

    $adjustChar("MM",mouth=2,eyes=5)

    extend "\n\n{size=18}She would've come back for me.{/size}"

    $adjustChar("MM",mouth=3)

    Madhouse  "So no. All I want is my stupid hat."

    python:
        adjustChar("MM",mouth=1,eyes=4,blush=1)
        adjustChar("August",mouth=2,eye=5,eyeFrame=0,brow=4)
        adjustChar("Robyn",mouth=0)

    August  "Ah, don’t worry buddy, we’ll find it."

    show madhouse:
        ease 0.8 yoffset 0 xcenter 0.35
        idleFloat(2.2,10)
    python:
        adjustChar("MM",mouth=10,eyes=2,blush=0)
        adjustChar("August",eyeFrame=0,brow=2,mouth=5,eye=3)
        adjustChar("Robyn",brow=1)

    Robyn  "What's got you all invested?"

    $adjustChar("August",eyeFrame=5,brow=0,mouth=3,eye=2)

    August  "Do I need a reason to want to help? Like I said, I'm a tracker. When something's lost, it’s my job to find it."

    python:
        adjustChar("August",eyeFrame=0,brow=2,mouth=5,eye=0)
        adjustChar("Robyn",mouth=0,eyes=4,brow=0)

    August "Unless it's the TV remote."

    voice mm_laughb
    $adjustChar("MM",eyes=5,mouth=9,armR=0,armL=0)
    Madhouse "{sc=2}Whatever.{/sc}"

    show madhouse:
        xcenter 0.35
        alpha 1
        blur 0
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 yoffset -100 alpha 0 blur 30

    $adjustChar("MM",mouth=9,eyes=7,armR=3,armL=3)
    python:
        adjustChar("August",eyeFrame=2,brow=2,mouth=5,eye=3)
        adjustChar("Robyn",eyes=2,brow=1)
    Narrator "The ghost disappears."

    hide madhouse
    python:
        adjustChar("August",eyeFrame=2,brow=2,eye=3)
        adjustChar("Robyn",eyes=2,brow=1)

    scene BG Black with Dissolve(0.5)

    pause 0.5
    play sfx phone_notif

    $unlockHangout("Gus",1)
    Narrator "Now's your chance to spend time with {color=#e8850c}{b}August{/b}{/color}! Would you like to view this {color=#ED2A82}{b}hangout{/b}{/color} now?{nw}"

    menu:
        extend ""

        "Yes!":
            call August_Hangout1 from _call_August_Hangout1
        "Not now.":
            Narrator "You can access this event in the {color=#ED2A82}{b}Chapter Select{/b}{/color} menu."
            pass

    jump Ch1_AtlasDoctorVisit
