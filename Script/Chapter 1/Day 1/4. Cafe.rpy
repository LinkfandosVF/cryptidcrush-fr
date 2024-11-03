label Ch1_CafeIntro:
    scene BG Cafe:
        matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")

    camera:
        camera_zoom(z=-280,x=-190)

    python:
        musicPlayer.playSong(fadeOut=1)

        timeText = "2:00PM"

        adjustChar("Robyn",eye=4,brow=2,mouth=3,armR=0)
        adjustChar("Robbie",armR=1,eye=2)

    show robyn neutral:
        xcenter -0.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.0 xcenter 0.2

    show robbie behind robyn:
        xcenter 0.5

    show jamie cafe:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.8

    with Dissolve(1.0)
    python:
        musicPlayer.playSong(song="stygian_scuffle_song",fadeIn=2,fadeOut=1)
        songText = "(REDACTED)"

    Narrator "Entering the cafe, you’re greeted with the sharp air of roasted coffee and funky choral music that doesn’t suit the atmosphere at all."

    Narrator "Not that you’re one to judge, everyone has their odd music tastes. \n\n You're just here for a chair and a bite to eat."

    show robyn happy:
        xcenter 0.2
    $Robbie_State["eye"] = 3
    Robyn "Are you in line?"

    $Robbie_State["eye"] = 1
    Narrator "Standing towards the counter is a bundled up cryptid hunched over a tiny coffee cup, dressed in layers of warm clothes and a fuzzy hat to match."

    Narrator "The droning music suddenly cuts to a peppy, folk playlist."

    $musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=1,fadeOut=1)

    python:
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "6A", who_color = "ea3c53")
        adjustChar("Robbie",eye=0,mouth=1)

    show robbie:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    voice robbie_hopingtochangeorder
    Someone "I was hopin' to change my order."
    voice robbie_longhopescoffee
    $adjustChar("Robbie",eye=7,mouth=3)

    Someone "But,, I think Longhope's coffee., is just., {b}bad.{/b} Like look at this it's crap. It's useless, warm, brown water."

    python:
        musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=1,fadeOut=1)
        adjustChar("Robyn",eyes=2,brow=1,mouth=3)

        Jamie_State["eye"] = 2
        Robbie_State["eye"] = 0

    camera:
        camera_zoom(x=100,y=-30,z=-150,t=2)

    show robyn:
        xcenter 0.2
        ease 2.0 xcenter 0.5

    show robbie:
        flipCharDelayed(0.8,0.5)
        xcenter 0.5
        ease 3.0 xcenter -0.5

    show jamie cafe:
        unflipCharDelayed(0.8,0.5)

    Narrator "You shuffle past as the disgruntled cryptid leaves the shop."
    camera:
        camera_zoom(x=100,y=-30,z=-150)

    hide robbie

    show robyn default:
        xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)

    voice jamie_abyssalcoldbrewishalfoff
    Jamie "Welcome! What would you like to order? Abyssal cold brew is half off."

    $adjustChar("Robyn",eyes=0,mouth=4)
    Robyn "Jamie?"

    show jamie at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1

    $adjustChar("Jamie",alFace=0,eye=4,sweat=0,blush=1)
    Narrator "The towering demon freezes up on the spot and their cheeks flushing a bright blue."

    voice jamie_lookaway
    Jamie "No,., please,., look away."

    Robyn "Oh—"

    $adjustChar("Jamie",mouth=1,eye=6,blush=0,wispEyes=3)
    voice jamie_begonehuman
    Jamie "{sc=2}Begone human!{/sc}"

    $adjustChar("Jamie",eye=7,mouth=2)
    Jamie "Gaze not upon my wretched form."

    python:
        adjustChar("Robyn",eyes=2,mouth=2)
        Jamie_State["blush"] = 0

    Robyn "You mean., your work uniform?"

    python:
        adjustChar("Jamie",eye=1,mouth=0,wispEyes=4)
        Robyn_State["mouth"] = 5

    Jamie "Precisely,, I am but a worm in this state."

    Robyn "Hey, if it's too awkward, I can come back when you're on lunch break."

    $Jamie_State["eye"] = 4

    Jamie "No, I must be strong."

    python:
        adjustChar("Jamie",eye=3,blush=0,wispEyes=0)
        adjustChar("Robyn",eyes=3,mouth=0,brow=2)

    Robyn "I'll have a chai latte and a croissant."

    show robyn:
        matrixtransform RotateMatrix(0,0,0)

    $adjustChar("Jamie",mouth=1,eye=6,wispEyes=1)
    Jamie "You could save two dollars if you ordered an Abyssal Cold Brew."

    Robyn "Sure, if you recommend it!"

    python:
        adjustChar("Robyn",eyes=0,mouth=3)
        adjustChar("Jamie",eye=1,wispEyes=1,mouth=2)

    Jamie "No, it tastes very bad."

    $adjustChar("Robyn",eyes=3,mouth=0,brow=0)
    Robyn "How about an iced green tea?"

    $adjustChar("Jamie",mouth=0,eye=2)
    Jamie "Great choice."

    python:
        adjustChar("Jamie",eye=2,mouth=0)
        Robyn_State["eyes"] = 2

    show robyn:
        ease 0.75 xcenter 0.6
        pause 0.5
        ease 0.75 xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.75 matrixtransform RotateMatrix(0,0,-10) yoffset 40
        pause 0.5
        ease 0.75 matrixtransform RotateMatrix(0,0,0) yoffset 0

    Narrator "You get your croissant and handcrafted beverage, eager to take a sip. With great anticipation, You take a drink- "

    $adjustChar("Robyn",mouth=4,brow=3,eyes=3)

    show robyn:
        xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)
        yoffset 0

    extend "\nand gag. It's horrible! It tastes like the vacuum of space slathered with the Marianas trench."

    $adjustChar("Robyn",mouth=4,brow=1,eyes=0)
    Robyn "This isn't what I ordered."

    Jamie "I believe you ordered an abyssal green tea?"

    Robyn "N-no. I- {sc=3}{i}ugh.{/i}{/sc} Abyssal?"

    python:
        adjustChar("Jamie",eye=0,brow=3,mouth=4)
        Robyn_State["mouth"] = 5

    Jamie "It's where we source our ingredients."

    python:
        adjustChar("Robyn",eyes=1,mouth=3,brow=2)
        Jamie_State["mouth"] = 0

    Robyn "Bleugh."

    $adjustChar("Jamie",wispEyes=0,eye=2)
    Jamie "What if I made you a drink that's {i}off menu{/i}? {nw}"

    $adjustChar("Jamie",wispEyes=1,eye=1,brow=0)
    extend "\n\n I insist."

    $Robyn_State["eyes"] = 2
    Robyn "Okay,, just don't get in trouble."

    python:
        adjustChar("Robyn",eyes=1,mouth=5)
        adjustChar("Jamie",eye=1,wispEyes=0,brow=0)


    Jamie "That's part of the fun."
    show jamie cafe:
        xcenter 0.8
        ease 2.0 xcenter 1.3

    Narrator "You nudge the drink aside while Jamie heads back behind the counter."

    camera:
        camera_zoom(z=-500,x=-30,t=0.4)
    hide jamie

    $BM_State['face'] = 1

    show blobhouse:
        zoom 0
        matrixtransform RotateMatrix(0,0,5)
        xcenter 0.4
        parallel:
            ease 0.6 xcenter 0.39
        parallel:
            ease 0.2 zoom 1.0
        parallel:
            ease 0.3 yoffset -200
            ease 0.3 yoffset 0
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0,180,360*2)

        idleFloat(2,10)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.45 matrixtransform RotateMatrix(0,180,0)

    $musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_laughd
    Madhouse "{sc=3}{b}CAR BATTERIES!{/b}{/sc}"

    $adjustChar("Robyn",eyes=0,brow=1,mouth=4)
    Robyn "Pardon?"

    python:
        adjustChar("Robyn",eyes=2,mouth=5)
        BM_State['face'] = 2

    voice mm_laughawkward
    Madhouse "If ya took some jumper cables and hooked me to a car battery,, that'd be just the {b}jolt{/b} I need to get my powers back!"

    $adjustChar("Robyn",eyes=1,mouth=4,brow=2)
    Robyn "Are you trying to eletrocute me?"

    $BM_State['face'] = 4
    Madhouse "No? Why would I do that?"

    python:
        adjustChar("Robyn",eyes=4,mouth=5,brow=3)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.45 matrixtransform RotateMatrix(0,0,0)

    Robyn "Who knows."

    $BM_State['face'] = 14
    voice mm_dismissive

    Madhouse "C'moooon, I wouldn't put ya in harms way!"

    python:
        adjustChar("Robyn",eyes=2,mouth=4)
        BM_State['face'] = 4

    Robyn "Tell that to your {i}one fanboy.{/i}"

    python:
        BM_State['face'] = 5
        adjustChar("Robyn",mouth=5,eyes=1)

    show blobhouse at startledSquish:
        idleFloat(2,10)

    Madhouse "{sc=2}{b}Ye-{/b}{/sc}{sc=4}{b}OWCH!{/b}{/sc} \n\nGosh, you're brutal. I'm being honest y'know."

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.45 matrixtransform RotateMatrix(0,180,0)

    Robyn "I don't want you thinking you're off the hook here, {color=#3bec27}Slimeball{/color}."

    $BM_State['face'] = 2

    show blobhouse at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        idleFloat(2,10)

    voice mm_yohoholaugh
    Madhouse "And a cute nickname? \n\nDoes that mean I get to call you., {sc=2}{b}{color=#EC2A2A}Meatball{/color}{/b}{/sc}?"

    $adjustChar("Robyn",eyes=2,mouth=4,brow=2)
    Robyn "No, seriously, you've got a lot of work to do."

    python:
        BM_State['face'] = 4
        Robyn_State["mouth"] = 5

    Madhouse "Wh—{nw}"

    $BM_State['face'] = 13

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2,10)

    extend "\n\nWhatever."

    python:
        adjustChar("Robyn",eyes=1,mouth=5,brow=1)
        musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=0.2,fadeOut=0.2)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.45 matrixtransform RotateMatrix(0,0,0)

    show blobhouse:
        ease 0.3 xzoom 0 yoffset -100 alpha 0 blur 30

    Narrator "Jeez, what's his problem? It's like he wants conflict."
    scene BG Black
    camera:
        camera_zoom()
    show CG WIP Cafe Jamie

    with BGDissolve(name="Trans_BM.png")

    Narrator "Back in the kitchen, the devil's brewing something truly unholy... And sure, they'll throw in a roasted veggie panini on the side."
    python:
        displaymenu = True
        drinkChoice = 0
        drinkDifficulty = 7

    Narrator "They search their heart and the perfect recipe comes to mind-{nw}"

    menu:
        extend ""

        "Dagon’s Primordial Brew":
            python:
                displaymenu = False
                drinkChoice = 1
                drinkDifficulty = 8
        "Tincture of Divine Truths":
            python:
                displaymenu = False
                drinkChoice = 2
                drinkDifficulty = 10
        "Prismatic tea of Unknowable Hues":
            python:
                displaymenu = False
                drinkChoice = 3
                drinkDifficulty = 12

    call dice_roll(rMod=Jamie_Stats.cStats("occult"), rDiff= drinkDifficulty, rDesc="Drinkomancy") from _call_dice_roll_12

    jump Ch1_CafeResult

label Ch1_CafeResult:

    $dNoun = ["sweet","punchy","otherworldly"][drinkChoice-1]

    Narrator "With an idea in place they get to work. Their hands move masterfully as they concoct the [dNoun] beverage, carefully crafting a brew to suit a mortal's palette."
    python:
        adjustChar("Jamie",eye=2,mouth=2,wispEyes=3,brow=3)
        adjustChar("Robyn",eyes=2,brow=1,mouth=0)

    scene BG Cafe

    camera:
        camera_zoom(x=100,y=-30,z=-150)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.5

    show jamie cafe:
        xcenter 1.1
        matrixtransform RotateMatrix(0,0,0)
        easein 1.2 xcenter 0.8

    with Pixellate(0.75,7)

    Jamie "Here."

    if not isRollSuccess:
        python:
            adjustChar("Jamie",eye=1,mouth=2,sweat=1)
            adjustChar("Robyn",brow=2)
        Narrator "Jamie slides the cup down on the counter with a handcrafted beverage, but not without nearly dropping it first."
    else:
        Narrator "Jamie slides the cup across on the counter."

    Jamie "Hope you enjoy."

    show CGShade
    show CG Cafe Drink

    if drinkChoice == 1:
        Narrator "It’s a murky drink, that with the bluish twinge make it feel like the inky abyss of the ocean had been washed out by coffee beans."
    elif drinkChoice == 2:
        Narrator "It’s a bright peach-ish beverage, that would look tasty, but the fact that it’s slightly glowing a divine radiance is mildly unsettling."
    elif drinkChoice == 3:
        Narrator "The drink looks more like a cosmic sludge that feels a bit too alive and bouncy. It refracts various bright colors as light glints off the surface, it doesn’t feel like a drink that should exist, let alone be consumed by people."

    $adjustChar("Robyn",brow=2)
    Narrator "You look up at Jamie, who stares back at you expectantly. \n\nSurely, if they're confident in it, you should be too!"

    hide CGShade

    hide CG Cafe Drink

    show SmallCafeDrink:
        yoffset 700
        xcenter 0.6
        ease 1.0 yoffset 20

    with nwDissolve(0.5)


    Narrator "…"

    if isRollSuccess:

        if drinkChoice == 1:
            $adjustChar("Robyn",eyes=0,mouth=4,brow=1)
            Narrator "It’s a little salty, but that just makes it all the sweeter when it combines with the bitter iced coffee base. There's a slight hint of caramel."

            $adjustChar("Robyn",mouth=6)
            Robyn "Delicious!"
        elif drinkChoice == 2:
            $adjustChar("Robyn",eyes=0,mouth=4,brow=1)
            Narrator "It’s rich. Almost like a hot cider, with apple and lemon. It fills you with a mellow warmth like any good tea should."

            $adjustChar("Robyn",mouth=6)
            Robyn "Yum!"
        elif drinkChoice == 3:
            $adjustChar("Robyn",eyes=0,mouth=3)
            Narrator "What flavor is this? It's sweet? No, it's savory? Each sip brings out a different flavor. It's overwhelming yet enlightening."

            $adjustChar("Robyn",mouth=6)
            Robyn "I have no idea what I'm drinking, but I think I like it?"

            $adjustChar("Jamie",eye=1,sweat=1)
            Jamie "I'm glad it didn't melt your brain."


    else:
        camera at camera_shake_off(x=100)
        python:
            adjustChar("Jamie",eye=4,mouth=1)
            adjustChar("Robyn",eyes=0,mouth=3)

        Jamie "{b}{sc=3}WAIT!{/sc}{/b}"

        $adjustChar("Robyn",mouth=4)
        show jamie cafe:
            matrixtransform rotated() xoffset 0 yoffset 0
            ease 0.3 matrixtransform rotated(z=-30) xoffset -160 yoffset 30
            ease 0.25 matrixtransform rotated(z=10) xoffset 20 yoffset 0
            ease 0.175 matrixtransform rotated() xoffset 0

        show SmallCafeDrink:
            xcenter 0.6
            pause 0.35
            matrixtransform rotated()
            parallel:
                easein 0.6 xcenter 1.3 matrixtransform rotated(z=360*3)
            parallel:
                easein 0.3 yoffset -300
                ease 0.3 yoffset 0


        Narrator "Jamie lunges, swatting your hand away before snatching up the cup of tea,, a wild look in their eyesockets."

        $adjustChar("Jamie",mouth=2)
        Jamie "I screwed something up! I can {b}feel it.{b} \n\nYou can't drink this."

        Robyn "It can't be that bad!"

        $adjustChar("Jamie",eye=1,mouth=0)
        Jamie "You're getting a tropical mix juice box instead."

        Robyn "{sc=3}H-huh?{/sc}"

        Jamie "Here's an apologetic grilled veggie panini on the side."

        $adjustChar("Robyn",eyes=1,mouth=5)
        Robyn "Okay fine."
        scene BG Black
        with nwDissolve(0.5)

        Narrator "Temporarily pacified by the delicious sandwich and the not so fancy juice box,, you take a deep breath, stretch and collect your thoughts."


    scene BG Black
    camera at camera_default:
        camera_zoom()

    with nwDissolve(0.5)

    python:
        PC_Stats.updateStats()
        bookNames = {
            "brawn": kwBrawn,
            "brains": kwBrains,
            "hustle": kwHustle,
            "guts": kwGuts,
            "charm": kwCharm,
            "occult": kwOccult }

        xBooks = []
        for x in ["brawn","brains","hustle","guts","charm","occult"]:
            if PC_Stats.cStats(x) > 0:
                xBooks.append(bookNames[x])

        xBookA = xBooks[0]
        xBookB = xBooks[1]
        xBookC = xBooks[2]



    Narrator "You give Jamie your thanks and leave the cafe. You head outside and find the perfect bench to rest upon."

    Narrator "With sustenance in hand, you decide to crack open the trove of pamphlets you were given. Each of them seem to be about... self-defense?"

    Narrator "Kind of strange that the Goatma'am's first thought would be on how to use your [xBookA], [xBookB], and [xBookC] to kick ass, but to each their own."

    Narrator "Maybe you could use these if anything like that Madhouse debacle happens again."

    Narrator "You could take a nap right about now. Maybe ghosts do leech on life force. \n\nIt'd explain why those {i}two{/i} are so clingy."

    Narrator "Leaning back, you fold your arms and bow your head, letting your eyes flutter closed. \n\nIt's nice feeling needed,, even if it's for cat food."

    show CG Taro wip
    camera at camera_shake

    Taro "{sc=3}{b}THERE YOU ARE!{/b}{/sc}"

    Narrator "Speak of the devil herself."

    Robyn "Taro!"

    Taro "You left me to {b}ROT{/b}! That googly eyed goat wouldn't stop asking me questions!"

    Taro "{bt=3}Oooh a three eyed cat?\n\nI've never heard of a {b}guardian nyangel{/b}! \n\nMay I hold your little paws?{/bt}"

    Taro "Not with those creepy mage hands!"

    Robyn "Aw nooo,, I'm sorry for wandering off without you Taro. I figured you wanted to go off and do your own thing."

    Taro "Typically yes,, but on my own terms."

    Taro "Now carry me."

    hide CG Taro wip
    with nwDissolve(0.5)

    #Narrator "After waving goodbye to Jamie,, you head outside and continue on your trek, exploring the town."

    Narrator "You scoop up Taro and give Atlas a call. He's always been your go-to guy for., anything really."

    jump Ch1_RobbieIntro
