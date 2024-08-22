#Taro Tutorial
label taro_dice_tutorial:
    python:
        tempDieType = diceBot.dieType
        diceBot.setDieType(1)
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 2

        Robyn_State["mouth"] = 3

    show taro:
        ease 1.0 xcenter 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn:
        ease 1.0 xcenter 0.2

    voice taro_laughc
    Taro "This calls for an investigation!"

    Robyn "Or I could just shoot them a text."

    #Narrator "You shine your flashlight around, but don’t find anything in particular."
    python:
        Taro_State["pawL"] = 0
        Taro_State["mouth"] = 1
        Taro_State["eye"] = 1

        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 1

    Taro "Nooo! Not like that, you’ve gotta roll!"
    $Robyn_State["mouth"] = 4

    Robyn "I left my dice at home."
    python:
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

        Taro_State["mouth"] = 4

    show screen Dice_Rolling_Menu
    python:
        xRerolls = 0
        pc_karma = 2
        rMod = dMenuMod = PC_Stats.cStats("brains")
        tempDif = rDiff = rrDif = dMenuDiff = 9
        rDesc = dMenuDesc = "Investigation"
        tempFailCheck = False
        DiceMenuResult = -1

    voice RobynSays("Generic","ConfusedA")
    Robyn "Ummm? What am I looking at?"

    Taro "Sometimes things require skill and a bit of luck, so to determine how your fate unfolds, you have to roll!"

    Taro "You’ll be given a difficulty rating that you have to meet or surpass. The universe will then add a modifier based on your stats! ([kwBrains] in this case)"

    $Robyn_State["mouth"] = 3

    Robyn "This feels like some kinda forbidden knowledge."

    python:
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 2

    Taro "Oh it is! Now try rolling for real!"

    python:
        die1Result = 1
        die2Result = 1
        die3Result = 0
        dieTotal = die1Result + die2Result + die3Result
        DiceMenuResult = 0
        dieGlow = True

    with Dissolve(0.2)
    pause 2.0
    python:
        DiceMenuResult = 2

        Robyn_State["mouth"] = 7
        Robyn_State["brow"] = 2



    show failFlash
    play sfx dice_result_c

    Robyn "Uh."
    hide failFlash
    python:
        Taro_State["pawR"] = 2
        Taro_State["mouth"] = 2
        Taro_State["eye"] = 2

    voice taro_smugb
    Taro "Wow, that was awful."
    python:
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 5

    Taro "Don't worry though! If you fail a roll, don't fret, you have a chance to change fate by spending [kwKarma]!"
    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

        Robyn_State["eyes"] = 4

    Robyn "Y’know, let me just call Atlas."

    Taro "What’s [kwKarma] you ask? Well, whenever you fail a roll, you can expend [kwKarma] to reroll!"

    Taro "You can reroll as many times as you have [kwKarma] whether you succeeded or failed that roll, but you have to be smart with it!"

    Taro "You only get a point of [kwKarma] when you fail and decide not to reroll. You got it?"
    $Robyn_State["eyes"] = 1

    Robyn "I’m sure someone around here gets it."
    python:
        tempFailCheck = True
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 5
    Taro "Great! Now tap that button and try rerolling those dice!"

    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3
    Taro "Just tap the button right below the dice!"

    Taro "..."

    Taro "Any minute meow~"

    Taro "..."

    Taro "Click the die with the pink arrow."

    Taro "..."

    Taro "Sure, Take your time."

    Taro "..."

    Taro "Any day now."

    Taro "{sc=2}...{/sc}"

    $Taro_State["eye"] = 1
    Taro "Are you doing this on purrpose?"

    Taro "{sc=4}...{/sc}"

    Taro "Click the goddamn die with the pink arrow."

    Taro "Just kidding! I don't actually care what you do."

    Taro "I'm just here for the laughs really."

    Taro "So, what've you been up to?"

    Taro "You sure love reading! I admire that."

    Taro "Wouldn't it be funny if I spoiled the ending of this chapter?"

    Taro "Alright, alright I'll do it."

    Taro "You all {sc=3}{b}DIE!{/b}{/sc}"

    Taro "Just kidding."

    Taro "Anyway, just click the die and roll again!"

    while True:
        Taro "{sc=6}...{/sc}"



    return

# Script Start
label atTheStation:
    python:
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=8)
        timeText = "2:00AM"

    play ambiance forest_ambiancea fadeout 1.0 fadein 7.5

    scene BG Outside Radio Station Near
    #show BGCG Outside Radio Station Fence: DONT USE THIS IT LOOKS BAD
        #xcenter 0.5
        #yalign 1.0
        #yoffset 1
    with pixellate #----------------------------- Outside Radio Station

    Narrator "Pulling into the radio station’s overgrown parking lot, you park between the fading lines. Taro hops up and jumps into her human’s arms, insisting on being carried like the oversized baby she is. You open the car door and step outside."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0

        Taro_State["eye"] = 1
        Taro_State["pawR"] = 2

    show robyn:
        matrixcolor TintMatrix("#d1ffe1")
        xcenter -0.3
        ease 2.0 xcenter 0.3

    show taro:
        parallel:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter -0.25
            ease 2.0 xcenter 0.45
        parallel:
            ease 1.3 yoffset 10
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10

        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat


    Narrator "You feel the brush of Taro’s whiskers against your cheek, somewhat easing your fears."
    camera:
        ease 3.0 zoom 1.5 ycenter 0.7

    show robyn:
        xcenter 0.3

    show taro:
        xcenter 0.45
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

    voice RobynSays("Generic","Concern")
    Robyn "Oookay. We’ll be fine. It’s just a haunted station on a hill. No big deal."

    Narrator "You click on the hefty flashlight with a tight grip."

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 2

    Narrator "You angle the light towards the station... as well as the large metal fence in front of it. Crap. Forgot the bolt cutters again."

    $Robyn_State["brow"] = 2

    Narrator  "You turn your attention instead to a large sheet of wood spray-painted with crude red letters attached to the fence. You read it aloud."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 4

    Robyn "Keep out! Trespassers will be {sc=2}{b}{color=#EC2A2A}murderlated{/color}{/b}{/sc}."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 6

    Robyn "Ah,, cool."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1

    #Narrator "Taro squirms out of her human’s arms and daintily lands on her feet."
    camera:
        ease 1.0 zoom 2.0 ycenter 0.8 xcenter 0.7

    python:
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 2
        Taro_State["eye"] = 2

        Robyn_State["eyes"] = 1

    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        parallel:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10

        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    voice taro_laughc
    Taro "I heard the place glows red on Friday nights, and the ‘On Air’ sign never burns out. Buncha silly rumors, if you ask me."

    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    pause 0.5

    python:
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0
        Taro_State["mouth"] = 1
        Taro_State["eye"] = 1

    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    Taro "Where is everyone?"
    camera:
        ease 3.0 zoom 1.0 ycenter 0.5 xcenter 0.5

    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 2.3 xcenter 0.6
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 2.3 xcenter 0.45
        linear 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        repeat

    #Narrator  "Swishing her tail, Taro paces around the parking lot."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 4
        Robyn_State["armR"] = 1

    Robyn "It's already 2:00AM! They should’ve been here by now."

    Narrator "Checking the time, you stuff your phone into your pocket and scan your surroundings with your flashlight."

    call taro_dice_tutorial from _call_taro_dice_tutorial

    python:
        diceBot.setDieType(tempDieType)
        pc_karma = diceBot.maxKarma
        musicNote = 8

    if isRollSuccess:
        show robyn:
            ease 0.5 xcenter 0.25

        show taro:
            ease 0.75 xcenter 0.7 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        Narrator "The flashlight scans over the empty lot, light dragging across the shattered windows and over the overgrown shrubbery. It suddenly catches a pair of beady red eyes lurking in the treeline, the light glinting off the unblinking eyes."

        python:
            Robyn_State["eyes"] = 3
            Robyn_State["mouth"] = 2
            Robyn_State["brow"] = 2

            Taro_State["mouth"] = 3

            Atlas_State["eye"] = 8

        show robyn:
            matrixtransform RotateMatrix(0.0, 0.0, -6.0)
            xcenter 0.25
            ease 0.05 xoffset -5
            ease 0.1 xoffset 5
            ease 0.1 xoffset -5
            ease 0.1 xoffset 5
            ease 0.05 xoffset 0

        show taro:
            xcenter 0.7
            matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        voice RobynSays("Generic","SurpriseC")
        Robyn "{sc=5}AH! WHAT THE HECK!?{/sc}"

        $musicPlayer.playSong(fadeOut=5)
        Narrator "You yelp in surprise, dropping your flashlight."

        show atlas fall:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter 0.5

        Narrator "In a flash, the figure leaps from the branches and splays its wings, swooping down before landing with a somersault. Dramatically, the very clouds overhead part, silvery moonlight revealing the creature’s feathery visage."
        python:
            Atlas_State["eye"] = 2
    else:
        show robyn:
            ease 0.75 xcenter 0.25

        show taro:
            ease 0.75 xcenter 0.7 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        Narrator "You shine your flashlight all around the empty lot, nothing particularly catching your eye."

        $musicPlayer.playSong()
        stop ambiance
        $Atlas_State["eye"] = 7

        show robyn:
            xcenter 0.25

        show taro:
            xcenter 0.7 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        show atlas:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter 0.5

        play sfx blip_2b
        pause

        python:
            Atlas_State["eye"] = 0

            Taro_State["mouth"] = 3

        play sfx blip_2b
        pause
        show taro:
            xcenter 0.7 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        python:
            Atlas_State["eye"] = 2

            Robyn_State["brow"] = 0
            Robyn_State["eyes"] = 2
            Robyn_State["mouth"] = 4
            Robyn_State["armR"] = 1

        play sfx blip_2b
        pause
        python:
            Robyn_State["eyes"] = 3
            Robyn_State["mouth"] = 2
            Robyn_State["brow"] = 2

        show robyn:
            matrixtransform RotateMatrix(0.0, 0.0, -6.0)
            ease 0.05 xoffset -5
            ease 0.1 xoffset 5
            ease 0.1 xoffset -5
            ease 0.1 xoffset 5
            ease 0.05 xoffset 0

        voice RobynSays("Generic","SurpriseC")
        Robyn "{sc=5}AH! WHAT THE HECK!?{/sc}"

        $Robyn_State["armR"] = 0
        #Narrator "You drop your flashlight on the ground."
        play ambiance forest_ambiancea fadein 7.5

    show robyn:
        ease 0.75 xcenter 0.2 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 2
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=8,fadeOut=5)

    Robyn "Wait. {color=#ED2A82}{b}ATLAS{/b}{/color}?"
    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["sparkle"] = 1

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.75 xcenter 0.2

    show atlas reset:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.625 matrixtransform RotateMatrix(0.0, 360.0, 0.0)

    hide taro
    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor TintMatrix("#d1ffe1")
        xcenter 0.7
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    voice atlas_oneandonly
    Atlas "{bt=3}The one and only{/bt}! I thought I’d scope out the perimeter before diving right in."

    python:
        Atlas_State["sparkle"] = 0

        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.075 matrixtransform RotateMatrix(0.0, 30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, -30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, 30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, -30.0, 0.0)
        linear 0.075 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show robyn:
        xcenter 0.2


    Narrator "After his dramatic entrance, Atlas shakes out his glossy feathers and flaps his large wings."
    python:
        Taro_State["mouth"] = 3
        Taro_State["eye"] = 2

        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1
        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 2


    show atlas:
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 1.0 xcenter 0.545
    Narrator  "His antennae twitch as he stands on one leg, poking Taro with one of his hind claws."
    python:
        Atlas_State["eye"] = 7
        Atlas_State["armL"] = 2

        Robyn_State["eyes"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.545

    voice atlas_spiritumentioned
    Atlas "{b}SO{/b},.,., is this the spirit you mentioned? Huh. I kinda expected something...{w=0.3} more impressive."
    python:
        Taro_State["mouth"] = 1
        Taro_State["pawL"] = 1

    show taro:
        yoffset 0
        pause 1.0
        ease 0.25 xcenter 0.71
        pause 0.5
        ease 0.25 xcenter 0.72
        pause 0.6
        ease 0.25 xcenter 0.73

    show atlas:
        ease 3.0 xcenter 0.6

    Narrator "Taro fluffs up, her whiskers standing on end as she hisses."
    python:
        Taro_State["mouth"] = 1
        Taro_State["pawR"] = 1
        Taro_State["pawL"] = 0

    voice taro_iamagreatandpowerfulcosmicguardian
    Taro "{sc=2}I am a great and powerful cosmic guardian{/sc}!"
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 4
        Atlas_State["armL"] = 1

        Robyn_State["brow"] = 0

    play sfx emote_frustration
    Narrator "She bites one of the mothman’s talons."

    Taro "Mrrrff! Grrh!"
    python:
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0

    Atlas "Owch, I am in immense pain."

    show atlas:
        ease 0.5 xcenter 0.5
    Narrator "Atlas pulls away, breaking out of Taro’s grip."
    python:
        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 4
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

        Robyn_State["brow"] = 3

    show atlas:
        xcenter 0.5
    Atlas "It’s not too late to be haunted by something cooler, right?"

    python:
        Robyn_State["eyes"] = 2
        Atlas_State["eyeFrame"] = 3
        Robyn_State["mouth"] = 4

        Taro_State["eye"] = 3
        Taro_State["mouth"] = 4
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0

        Atlas_State["feelers"] = 1

    show robyn:
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        pause 0.05
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0

    Robyn "Taro's doing her best!"

    $Robyn_State["mouth"] = 5

    #Narrator "You shoot the mothman a sharp look."

    $Atlas_State["eye"] = 2

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.75 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Robyn "You’re just jealous you don’t have a familiar following you around."

    voice atlas_nervouslaugh

    Atlas "Damn. If I had to pick, I’d want a raven familiar."

    python:
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0

        Taro_State["eye"] = 1
        Taro_State["pawR"] = 2

    Atlas "Too bad ravens hate me."

    python:
        Atlas_State["eye"] = 7

        Taro_State["eye"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.75 yoffset 200 matrixtransform RotateMatrix(0.0, 0.0, -20.0)
        pause 0.5
        ease 0.75 yoffset 0  matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 1.5 xcenter 0.4

    show taro:
        pause 2.0
        ease 1.5 xcenter 0.6

    Narrator "Atlas bends down and scoops the flashlight off on the ground."
    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 3

        Taro_State["eye"] = 1

        Robyn_State["brow"] = 2
        Robyn_State["mouth"] = 3


    show taro:
        xcenter 0.6

    show atlas:
        xcenter 0.4
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        yoffset 0

    Atlas "Here, sorry for startling you."

    Narrator "Breaking through the greenery, a single blue flame casts an eerie light over a large imposing demon striding into the clearing, a heavy pair of bolt cutters resting at their hip."
    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 1
        Atlas_State["feelers"] = 0

        Taro_State["eye"] = 4

        Robyn_State["brow"] = 1

        Jamie_State["eye"] = 3
        Jamie_State["armR"] = 1

    show robyn:
        ease 0.5  xcenter 0.13

    show atlas:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0) xcenter 0.33

    show taro:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.55

    show jamie:
        matrixcolor TintMatrix("#d1ffe1")
        xcenter 1.2
        ease 1.0 xcenter 0.85


    voice jamie_greet
    Jamie "Ah, it seems everyone has arrived."

    Jamie "I assume Atlas spoke of me?"

    #Narrator "The tall devil stares down, as if evaluating the small human and [PCtheir] spectral cat."
    python:
        Taro_State["eye"] = 1
        Taro_State["mouth"] = 3

        Robyn_State["mouth"] = 4

    Robyn "H-how’d you get here so fast—?!"
    python:
        Atlas_State["eye"] = 7

        Jamie_State["eye"] = 1
        Jamie_State["sweat"] = 1
        Jamie_State["armR"] = 2
        Jamie_State["brow"] = 3

        Robyn_State["mouth"] = 3

    Jamie "Legs?"

    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["sparkle"] = 1

    Atlas "This is Jamie! The roughest devil around. They're a great listener, bone collector, fist fighter, and artist! \n\n Jamie,, you should show [PCname] some drawings!"

    python:
        Jamie_State["sweat"] = 0
        Jamie_State["eye"] = 7
        Jamie_State["mouth"] = 4
        Jamie_State["armR"] = 0
    voice jamie_growld
    Jamie "No."

    python:
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 1
    voice atlas_frustration
    Atlas "But you're so good!"

    python:
        Atlas_State["eye"] = 7

        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 0
        Jamie_State["brow"] = 5
        Jamie_State["mouth"] = 0

    voice taro_dismissive
    Taro "I suppose I’ll scout on ahead, since you seem to be in such capable claws."
    python:
        Jamie_State["sweat"] = 0
        Jamie_State["brow"] = 1

    show taro:
        ease 3.0 yoffset 500

    Narrator "The feline hovers past the demon, floats through the fence, and disappears into the overgrowth."
    python:
        Jamie_State["brow"] = 0
        Jamie_State["eye"] = 3

    voice jamie_scoffb
    Jamie "We should follow suit."

    Narrator "Jamie struts towards the chain link fence, unsheathing the bolt cutters. They snap through the padlock and give a quick thumbs up."
    python:
        Jamie_State["r3Fire"] = 1
        Jamie_State["armR"] = 2
        Jamie_State["mouth"] = 2
        Jamie_State["eye"] = 6
        Jamie_State["steam"] = 1



    voice jamie_crimes
    Jamie "{bt=4}Let the crimes commence.{/bt}"
    #show BGCG Outside Radio Station Fence: die fence
        #ease 2.0 yoffset 700

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 0

        Jamie_State["r3Fire"] = 0
        Jamie_State["armR"] = 0

    show jamie:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        parallel:
            ease 1.25 xcenter 1.3
        parallel:
            ease 0.7 matrixtransform RotateMatrix(0.0,-180.0,0.0)

    show robyn:
        ease 1.0 xcenter 0.35

    show atlas:
        ease 1.0 xcenter 0.5
    Robyn "This is a horrible idea. What if someone gets hurt?"

    Narrator "You hesitate, stopping just before the gate."
    python:
        Atlas_State["eye"] = 0
        Atlas_State["feelers"] = 0

    show robyn:
        xcenter 0.35
    $Atlas_State["eye"] = 16

    #Narrator "Atlas nudges you and smiles with his eyes, his antennae flicking forward as he tilts his head to one side."

    Atlas "Psh,, ghost's are practically harmless. I bet this dude’s just some disembodied voice or a possessed microphone."
    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["sparkle"] = 1
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 1
    Atlas "Besides,, you've got me to protect you!"
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 0
    $Robyn_State["mouth"] = 5
    $Atlas_State["eye"] = 0
    $Atlas_State["sparkle"] = 0
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    Robyn "Mmmh,, nah it's the other way around."
    $Atlas_State["eye"] = 1
    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1
    Jamie "Hurry up!"
    show atlas:
        ease 2.5 xcenter 1.5

    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        pause 0.2
        ease 1.0 xcenter 0.55
        pause 0.2
        ease 0.4 matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.6
        ease 0.4 matrixtransform RotateMatrix(0.0,360.0,0.0)
        pause 0.2
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        ease 0.7 xcenter 1.5
    #Narrator "Reluctantly, you follow suit, trailing after Atlas as you three approach the abandoned station."
    $Robyn_State["eyes"] = 2
    $Robyn_State["brow"] = 0
    play sfx rustyDoor
    Narrator "The exterior of the radio station is tagged with fading graffiti and plastered with condemnation warning posters. Jamie turns the handle to the front door and it easily clicks open."

    Atlas "Creepy!"
    jump exploreStation

label exploreStation:
    scene BG Hallway Radio Station with Fade(0.75, 0.25, 0.75, color="#000")
    stop ambiance fadeout 1.0
    Narrator "Looking through the doorway, the dark interior of the station seems impossibly clean compared to the outside. The waiting room is seemingly suspended in time, only faded from months of neglect... maybe years."
    python:
        Atlas_State["eye"] = 1

    show robyn:
        matrixcolor TintMatrix("#fccaca")
        xcenter -0.5
        ease 2.0 xcenter 0.3

    show jamie:
        matrixcolor TintMatrix("#fccaca")
        xcenter -0.5
        pause 1.0
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 2.0 xcenter 0.8
        ease 0.3 matrixtransform RotateMatrix(0.0,0.0,0.0)

    show atlas:
        matrixcolor TintMatrix("#fccaca")
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter -0.5
        ease 2.0 xcenter 0.5


    Narrator "You shuffle in line behind Jamie as you examine the lobby. Stopping a moment, you realize that you’re the only one with a flashlight."

    show robyn:
        xcenter 0.3

    Robyn "All of you can see in the dark?"


    python:
        Jamie_State["armR"] = 2
        Jamie_State["eye"] = 1
        Jamie_State["steam"] = 0
        Jamie_State["mouth"] = 0

    Jamie "Indeed. My eyes can pierce any darkness."
    show jamie:
        xcenter 0.8
        matrixtransform RotateMatrix(0.0,0.0,0.0)

    python:
        Jamie_State["armR"] = 0
        Jamie_State["eye"] = 3

        Atlas_State["armL"] = 1
        Atlas_State["eye"] = 6
    show atlas:
        xcenter 0.5
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 7.0) yoffset 30
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 0.0) yoffset 0
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 7.0) yoffset 30
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 0.0) yoffset 0

    Atlas "I actually rely on my capitate antennae, with these big ol’ eyes my vision’s super sensitive to light."

    python:
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 0

        Robyn_State["mouth"] = 3
    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Atlas "Okay, it’s not seeing but more like smelling."

    python:
        Atlas_State["eye"] = 1

    python:
        Jamie_State["eye"] = 4

    show jamie:
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.805
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.805
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.8

    voice jamie_annoyedb
    Jamie "Atlas, can you go a day without mentioning your insectoid parts?"


    python:
        Jamie_State["eye"] = 1

    python:
        Robyn_State["mouth"] = 4
    show jamie:
        xcenter 0.8

    Robyn "I don’t mind really."

    python:
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 1

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.8 matrixtransform RotateMatrix(0.0, 360.0, 0.0)

    Narrator  "You twirl the flashlight in your hand, nearly dropping it in the process."

    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 1.5 xcenter 0.2

    show jamie:
        ease 1.5 xcenter 0.45

    show atlas:
        ease 1.5 xcenter 0.8

    Narrator "Wandering around, Atlas tries the nearest door. After finding it locked, he shuffles over to the recording studio window and presses his face against the glass."

    Narrator "Jamie kicks one of the trash cans over. Dozens of lime green soda cans come clanging out, scattering across the floor."

    python:
        Jamie_State["eye"] = 8
        Jamie_State["brow"] = 2

    show jamie:
        xcenter 0.45

    show atlas:
        xcenter 0.8

    Jamie "For an unlocked haunted house, it is surprisingly untouched... I almost feel bad trashing the place."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 0

    Robyn "Where do you think we’ll find the ghost?"

    python:
        Atlas_State["eye"] = 17
        Atlas_State["armL"] = 1
        Atlas_State["armR"] = 1
        Jamie_State["eye"] = 0
        Robyn_State["mouth"] = 5

    Atlas "You tuned into the ghost frequency,, right?"

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
    #Narrator "Atlas perks up, his feelers twitching, as he stands back and turns around."

    Robyn "..."

    show atlas:
        matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 360.0, -7.0) yoffset 30
        ease 0.3 matrixtransform RotateMatrix(0.0, 360.0, 0.0) yoffset 0

    python:
        Atlas_State["eye"] = 16
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

    Narrator "Atlas gives a reassuring nod."

    $Atlas_State["eye"] = 0


    voice atlas_dismissive
    Atlas "It’s fine if you didn’t."

    $Atlas_State["eye"] = 1
    $Atlas_State["eyeFrame"] = 6
    camera:
        ease 8.0 zoom 2.3 xcenter 1.05 ycenter 0.8

    Atlas "I’ll catch you up. So, the show was basically this radio host, Madhouse Mike, reading ghost stories and urban myths off a script. It was all super cheesy and I loved it."
    camera:
        zoom 2.3 xcenter 1.05 ycenter 0.8
        ease 0.3 xoffset -1500

    $displaymenu = True
    Robyn "I don’t understand why.{nw}"
    $displaymenu = False
    camera:
        ease 0.3 xoffset 0

    $Atlas_State["eyeFrame"] = 2
    $Atlas_State["eye"] = 0

    Atlas "Anyways, he’s the ghost we’re looking for. Madhouse was an {color=#3bec27}{b}EXPERT{/b}{/color} on the supernatural, so I’m certain he'll know something about your curse."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 1

    Jamie "Mike is playing a character, Atlas. Who knows what the guy is like off air."
    show jamie:
        ease 3.0 xcenter -0.5
    show robyn:
        ease 1.0 xcenter 0.5
    Narrator "Jamie absentmindedly crushes one of the spilt cans and tosses it back into the trash can."

    python:
        Atlas_State["eyeFrame"] = 3
        Atlas_State["eye"] = 2
        Atlas_State["feelers"] = 1

    camera:
        ease 4.0 zoom 1.6 xcenter 0.8 ycenter 0.7

    show robyn:
        xcenter 0.5

    #Narrator "Atlas’ antennae droop and he looks away."

    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "Aren’t ghosts usually created from tragedy? He sounds normal enough to me."

    python:
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 2
    show atlas:
        matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        ease 0.2 yoffset -30
        ease 0.2 yoffset 0
    Narrator "Atlas gasps."

    python:
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1
        Atlas_State["eye"] = 6
    camera:
        ease 0.5  zoom 3.5 xcenter 1.15 ycenter 0.85

    voice atlas_gotastory
    Atlas "{bt=5}It was totally tragic!{/bt}"

    Atlas "Madhouse died while advertising for some sketchy drink company! He thought he could bring in more listeners by drinking the entire sample box."

    Atlas "It actually worked for like... two seconds."

    python:
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 8
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 0

    Atlas "I mean really,, who’d trust a company named Toxic Waste Energy?"
    camera:
        ease 0.5 xoffset -1400 yoffset -100
    $displaymenu = True
    Robyn "That’s terrible—{nw}"
    $displaymenu = False
    camera:
        ease 0.5 xoffset 0 yoffset 0

    python:
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["feelers"] = 3
        Atlas_State["eye"] = 9
    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Atlas "{sc=1}He drank so much that his skin glowed {color=#3bec27}green{/color}{/sc} and he beefed it from all that radiation! \n\nThe studio had to shut down, and no one alive's been on air since!"

    camera:
        ease 0.5 xoffset -1400 yoffset -100

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Jamie "Do you even hear yourself?"

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 2
    Atlas "This is exactly what Madhouse would have wanted! Hosting a radio show for the rest of eternity? That sounds great!"
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    python:
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3

    voice jamie_annoyedb
    Jamie "Turning into a restless ghost is easily the worst case scenario."

    python:
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 3
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 3.0 xcenter 0.3

    camera:
        parallel:
            ease 4.0 zoom 1.0 xcenter 0.5 ycenter 0.5
        parallel:
            ease 3.0  xoffset 0 yoffset 0
    Atlas "It’s funny, he carried me through those long nights at my old retail job back home. Y’know, before I got fired after being robbed twice and starting an electrical fire. The dude was a legend for us night owls."

    #Jamie Expression needed
    python:
        Atlas_State["eye"] = 7
        Jamie_State["armR"] = 3
    Jamie "You truly are a bringer of bad luck."

    #Atlas expression needed
    python:
        Atlas_State["eye"] = 18
        Atlas_State["feelers"] = 0
    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Atlas "You’re a literal devil!"
    Robyn "Sooo, it's just a rumor."
    python:
        Jamie_State["eye"] = 4

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["brow"] = 0

    Jamie "Rumors won't get us anywhere,, let's search the place and gather more information."

    python:
        Atlas_State["eyeFrame"] = 0
        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 0
    show robyn:
        matrixtransform RotateMatrix(0, 360, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
        ease 0.5 xcenter 0.2
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
    show jamie:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 xcenter 0.4

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    $Atlas_State["eye"] = 19

    Atlas "And risk upsetting the guy when we’re about to hop onto his radio show? No way!"

    Jamie "Upset?"

    python:
        Jamie_State["armR"] = 2
        Jamie_State["mouth"] = 2
        Jamie_State["eye"] = 6
        Jamie_State["steam"] = 1
        Jamie_State["brow"] = 1
        Atlas_State["eye"] = 7
        Atlas_State["feelers"] = 1
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    voice jamie_annoyeda
    Jamie "Atlas. We're trespassers!"
    $Atlas_State["eye"] = 19
    Atlas "What do {i}you{/i} think about this [PCname]?"

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 18
    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.45
    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Narrator "Both Jamie and Atlas turn to you, expecting you to settle whatever this is."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0
        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["steam"] = 0
        Jamie_State["eye"] = 1

    Robyn "Jamie's right. We might find something useful, like a vault of haunted treasure or a portal to a ghost dimension."

    show robyn:
        ease 1.0 xcenter 0.55

    show jamie:
        ease 1.0 xcenter 0.3
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    python:
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 1

    Robyn "Atlas, think of all the exclusive merch—! You could totally ask for an autograph."
    $Atlas_State["eye"] = 4
    $Atlas_State["feelers"] = 0

    Atlas "You think so? Actually, let’s check out the record room, there’s gotta be some shiny collector vinyls and tapes in there."

    Narrator "The mothman’s eyes sparkle."

    python:
        Atlas_State["eye"] = 9
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0
        Jamie_State["armR"] = 0

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 3.0 xcenter 1.5
    Atlas "Y’know, for research purposes."

    show jamie:
        ease 2.0 xcenter 0.75
    Narrator "Jamie brushes past you and open the door before them, ushering the human to follow."

    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 1

    voice jamie_scoffa
    Jamie "Scratch that,, I want this spector dealt with {i}now.{/i}"

    $Robyn_State["eyes"] = 4
    #Narrator "Avoiding their icy blue gaze, your heart skips a beat at Jamie’s words. Even though they agreed to join you, you still feel like they’re burning a hole in your chest."

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

    show robyn:
        ease 0.3 xcenter 0.5
    Robyn "Hey,, I was wondering, why'd you come with us?"

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 0

    #Narrator "Jamie thinks a moment before answering flatly."

    Jamie "I wanted to meet you."

    python:
        Robyn_State["eyes"] = 0

    Jamie "An average human moving to Longhope is a major big deal."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 0

    Robyn "What makes you say that?"

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 1

    Jamie "Folks around here tend to be occult,, undead or aquatic. \n\nWhich, you are not."

    $Robyn_State["eyes"] = 2
    $Robyn_State["mouth"] = 5

    voice RobynSays("Generic","ConfusedA")
    Robyn "Nope."

    Jamie "Then something had to have brought you here."

    Narrator "Jamie’s expression darkens, their gaze trailing down before resting upon you. Your throat feels dry as you try to force a response."

    Robyn "Well... I've known Atlas since like forever,, he helped me unpack!"

    Jamie "No. \n\nSomething worse."

    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 3
    $Robyn_State["brow"] = 2

    Robyn "Jamie, you're being awfully cryptic."

    #Narrator "You hardly manage to squeak out your words, ready to buckle under Jamie’s suffocating aura."

    Jamie "I tend to be."

    voice RobynSays("Generic","HmphB")
    Robyn "Uh, Okay."

    Jamie "But let's not jump to conclusions."

    Narrator "You’ve decided Jamie is definitely annoyed with you. You must salvage this."

    Robyn "{bt=4}Sooo{/bt}, you'll be there for Friday's movie night, right?"

    $Robyn_State["eyes"] = 0
    $Jamie_State["armR"] = 1
    $Jamie_State["eye"] = 2
    $Robyn_State["mouth"] = 1

    show jamie:
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 0, 0)

    Narrator "Jamie’s eyes light up, the flame atop their head flickering a warmer blue."

    Jamie "Carrying stuffed sweet potatoes, chicken skewers and jalapeño dip."

    Narrator "You picture Jamie wearing a gingham apron and oven mitts all while carrying a tray of freshly baked snickerdoodles."

    $Robyn_State["mouth"] = 4
    $Robyn_State["brow"] = 2

    Robyn "You cook?"

    $Jamie_State["eye"] = 6
    $Jamie_State["armR"] = 2
    $Robyn_State["eyes"] = 2

    voice jamie_happya
    Jamie "{sc=1}{color=#ff0f4f}Part-time.{/color}{/sc}"

    $Robyn_State["mouth"] = 0

    Robyn "I have {sc=1}soooo{/sc} many questions."

    $Jamie_State["eye"] = 7
    $Jamie_State["mouth"] = 1

    Jamie "They called me the {bt=4}Grill Master{/bt}."
    $Jamie_State["mouth"] = 0
    Robyn "Jamie, I need answers."

    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 0
    $Robyn_State["mouth"] = 3
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 2

    show jamie:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 180, 0)
    Jamie "I need you to keep walking."

    show jamie:
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.75 xcenter 1.5

    show robyn:
        ease 1.75 xcenter 1.3

    $Jamie_State["eyes"] = 4

    Robyn "Sure thing, {bt=4}Grill Master!{/bt}"

    voice jamie_angry
    Jamie "Do not say that."

    scene black with dissolve
    play sfx rustyDoor
    Narrator "With a grunt, you manage to shove the door open, knocking down a filing cabinet blocking the doorway within the room."

    Narrator "Stepping over the cabinet, you gaze around the office."
    scene  BG Office Dark Spooky
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 3
        Atlas_State["tears"] = 1

    show atlas:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        xcenter 0.85
        yoffset 75

    with Fade(0.25, 0.5, 0.75, color="#000")
    Narrator "The room is completely trashed. Loose papers are scattered across the carpet, green sludge is smeared across the walls, and a bookshelf full of records and trophies are smashed to bits."

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0

        Jamie_State["eye"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["brow"] = 0

    show robyn:
        xcenter 0.55
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor BrightnessMatrix(-1)*TintMatrix("#d1ffe1")
        blur 20
        alpha 0
        ease 0.5 blur 0 alpha 1
        ease 0.25 matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        ease 0.7 xcenter 0.3
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)

    Robyn "Oh dear."

    #Narrator "Atlas lets out a gasp, stumbling towards the sorry pile of vinyls and falls to his knees."
    show robyn:
        xcenter 0.3
        alpha 1
        matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        blur 0
        matrixtransform RotateMatrix(0, 0, 0)


    voice atlas_frustration
    Atlas "{sc=3}Nooo{/sc}! What kind of monster did this?!"


    Narrator  "The mothman scoops up a handful of shattered records, letting shards fall between his feathers."

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0) yoffset 75
    Atlas "{sc=1}These were original copies{/sc}!"

    python:
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.5
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Robyn "... Couldn’t you just download the digital album?"

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show jamie:
        alpha 0
        xcenter 0.62
        matrixcolor BrightnessMatrix(-1)*TintMatrix("#d1ffe1")
        blur 20
        ease 0.5 alpha 1.0 blur 0
        ease 0.25 matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        yoffset 75

        parallel:
            ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        parallel:
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85

    $Atlas_State["eye"] = 12
    $Atlas_State["eyeFrame"] = 1
    $Atlas_State["tears"] = 0
    $Atlas_State["feelers"] = 1

    Atlas "{sc=3}No!{/sc} It’s about the rich, omni-dimensional sound!"

    python:
        Jamie_State["eye"] = 3
        Jamie_State["mouth"] = 0
        Jamie_State["brow"] = 1
        Jamie_State["armR"] = 2

    show jamie:
        alpha 1
        matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        blur 0
        ease 1.5 xcenter 0.3

    show robyn:
        ease 1.5 xcenter 0.5

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 5.0)
    Narrator "Ignoring Atlas’ muttering, Jamie runs their claws across the wall, tracing out the words written in faintly glowing slime."

    python:
        Robyn_State["eyes"] = 2
        Jamie_State["eye"] = 0
        Jamie_State["brow"] = 4
        Jamie_State["mouth"] = 4
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 1
    show robyn:
        xcenter 0.5

    show jamie:
        xcenter 0.3


    Jamie "‘Daily ghost watch dot net'... The hell does that mean?"
    $Jamie_State["mouth"] = 0
    $Jamie_State["armR"] = 0
    $Robyn_State["mouth"] = 5
    $Robyn_State["eye"] = 1
    show jamie:
        ease 0.3 xcenter 0.33
    #Narrator "Jamie steps back, reading the words scrawled onto the wall."

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    voice RobynSays("Generic","Thinking")
    Robyn "Sounds like a website."

    python:
        Atlas_State["tears"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 5.0)

    Narrator "Atlas looks up from the vinyl wreckage, wiping away his tears."

    show robyn:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

    show jamie:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 180, 0) xcenter 0.25

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 5.0)

    $Atlas_State["eye"] = 0
    $Atlas_State["eyeFrame"] = 5

    Atlas "Tch, it’s just some blog that reports on abnormal occurrences."

    $Jamie_State["eye"] = 3
    $Robyn_State["eyes"] = 4

    Jamie "Makes sense."

    $Atlas_State["eye"] = 14
    $Atlas_State["feelers"] = 0
    $Atlas_State["eyeFrame"] = 0
    $Jamie_State["brow"] = 0

    Atlas "I was actually a mod there for like a month."
    $Jamie_State["mouth"] = 1
    $Jamie_State["eye"] = 1
    $Atlas_State["eye"] = 13
    Jamie "Ew."

    $Jamie_State["mouth"] = 0
    $Jamie_State["eye"] = 0
    $Robyn_State["brow"] = 3
    $Robyn_State["eyes"] = 2

    show robyn:
        ease 0.2 yoffset -20
        ease 0.2 yoffset 0


    Robyn "Moderation's important!"
    $Jamie_State["eye"] = 2
    $Atlas_State["eye"] = 18
    $Robyn_State["brow"] = 0
    $Robyn_State["mouth"] = 1

    Jamie "Yeeeeah,, you nerds better get snooping."

    $Robyn_State["mouth"] = 3

    show robyn:
        yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 yoffset 20 matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Robyn "I'll make it quick."

    $Atlas_State["eye"] = 1
    $Jamie_State["eye"] = 1
    $startInvest = True


    jump investigation_loop

label investigation_loop:
    show jamie:
        ease 0.4 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.7 xcenter 0.2

    show robyn:
        ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.6 xcenter 0.5

    show atlas:
        ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.85

    $displaymenu = True

    if startInvest:
        python:
            inv1 = True
            inv2 = True
            inv3 = True
            inv4 = True
            inv5 = True
            inv6 = True
            inv7 = True

            numInvest = 0
            startInvest = False
            mCaseInvest = False
        Robyn "Where should I start?{nw}"
    else:
        Robyn "Let’s see here...{nw}"

    menu:
        extend ""

        "Computer" if inv1:
            python:
                displaymenu = False
                inv1 = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 5
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.2

            show jamie:
                ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.7 xcenter 0.5

            show atlas:
                ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.8 xcenter 0.85

            Narrator "Sneaking around the office, you stop at the desk resting in one corner."

            Narrator "A chunky computer hums with power and the monitor rests on the desk, a single sticky note slapped to its screen. It reads, Password: 'deathproof' in messy pen strokes."

            $Robyn_State["mouth"] = 1
            $Robyn_State["brow"] = 1

            Narrator "You click on the monitor, which blinks on and flashes a group photo of the Studio members before sputtering out again."

            Narrator "Clicking on the monitor once more, you click the minimized webpage and are greeted with the ghost hunting forum."

            Narrator "Someone seems to have scoured the page, leaving comments and even arguing with users under the username {i}RadioGhost1.{/i}"

            Narrator "One comment reads, This guy sounds so cool! I wonder what he was like in life. A response under the same username reads, Great post! Heaven’s really missing out lol."

            python:
                Robyn_State["eyes"] = 4

            Narrator "Scrolling down, you see that RadioGhost1's been banned for self advertising."

            python:
                Robyn_State["eyes"] = 0
                Robyn_State["mouth"] = 4
                Robyn_State["brow"] = 1

            show robyn:
                ease 0.2 yoffset -50
                ease 0.2 yoffset 0

            Narrator "You're about to check the other tab open on the computer, but are cut short as something cold brushes against you."

            python:
                Robyn_State["mouth"] = 1
            show Debbie Prop:
                alpha 0
                ease 0.5 alpha 1.0
            Narrator "Turning around sharply, you see a human sized figure crafted out of empty Toxic Waste cans sits in the dusty office chair."

            Narrator "The figure has a marker mouth hanging open in a smile, its head built from a half crushed water jug and paperclips strung together like hair. A name tag clipped to the forehead reads Debbie."
            show Debbie Prop Leave:
                alpha 1
                pause 0.5
                ease 0.5 alpha 0
            Robyn "This is seriously creepy."
            hide Debbie Prop

        "Boohoo Answers" if inv6 and not inv1:
            python:
                inv6 = False
                displaymenu = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 5
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.2

            show jamie:
                ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.7 xcenter 0.5

            show atlas:
                ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.8 xcenter 0.85
            $Atlas_State["eye"] = 2
            $Atlas_State["phone"] = 1
            $Jamie_State["eye"] = 3
            $Robyn_State["eye"] = 0

            Narrator "You return to the computer to resume checking it out. The other tab left open was for a site called BooHoo Answers."
            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "{i}Question: How to banish a ghost?{/i}"

            Computer "Hi, I've got a ghost living in my house and it's going on eight years. I've tried everything— psychics, priests, investigators you name it! He won't leave! HELP. (10 Answers)"

            $Computer = Character("L0GIC", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "3A", who_color = "#f0bf6c")
            Computer "Ask him to pay rent, but raise the price each month. (Top Reply)"

            $Computer = Character("Para_Mama", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "#e96cf0")
            Computer "Hang in there sweetpea, if you need a medium I accept virtual sessions. I'll share my website if you're in need of extra resources. Good luck! :)"

            $Computer = Character("(Deleted)", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "7B", who_color = "#ff3232")
            Computer "Duuuude same! I've got a bloody ghost in my bathroom mirror and she won't stop knocking on the glass. What does she want? \n\n(This user was last online 725 days ago)"

            $Computer = Character("FaeBae", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "10A", who_color = "#7b78ff")
            Computer "You'll want to take a red marker, and draw two touching circles followed by a long oval connecting the shapes, preferably on the wall. They act as protection wards which will banish any spirit!"

            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "Didn't work. Also,, fuck you!"

            $Computer = Character("Dan105.1", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "10C", who_color = "#6cbcf0")
            Computer "Wanna know my secret? Garlic bread. I eat like six sticks a day and haven't seen a single ghost."

            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "You really think it's that easy to exile a vengeful spirit?! If it were that easy I wouldn't be here! You're all frauds!!"

            Narrator "You see that the user has been permanently banned."

        "Muffled Voices" if inv7 and numInvest >= 2:
            python:
                inv7 = False
                displaymenu = False
                renpy.block_rollback()
                Voice = Character("???", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27")

            Narrator "You hear a muffled voice and put your ear up against the wall to listen in better."

            Voice "Debbie quit puttin' garbage in with the fan mail!\n\n{sc=2}I'm not reading anymore {b}SCAMS.{/b}{/sc}"

            Narrator "There's a long pause before the voice picks up again."

            Voice "Look, I was wondering... It's about my work hours. Y'see, usually I'm sharper than a wolf bite but, the past decade's felt rather dull."

            Voice "I was thinking maybe,, I could take a break! I'd spend that time reconnecting with the living part of me."

            Narrator "There's a drone of silence before you hear a muffled slam and the sound of a can crumpling in someone's grip. "

        "Bulletin Board" if inv2:
            python:
                inv2 = False
                displaymenu = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 2
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.4

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 1.0 xcenter 0.2

            Narrator "You look to the corkboard nailed to the wall, taking note of the various pages tacked to the board."

            Narrator "Marker mustaches are scribbled over a single group photo, a man wearing a red hoodie scratched out entirely."

            Narrator "A printed out calendar is pinned to the wall with August 21st circled and labeled, “Dr’s appointment.” There’s even a coupon for a free case of Toxic Waste Energy tacked to the corkboard."

            show robyn:
                ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 0.8 xcenter 0.6
            Narrator "Tearing off the coupon, you bring it to Atlas hoping for some insight."

            Robyn "What’s this?"

            show atlas:
                matrixtransform RotateMatrix(0, 180, 0)
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                pause 0.6
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

            voice atlas_thinking
            $Atlas_State["eye"] = 3
            Atlas "Hm? Oh, that’s the drink that killed Mike Madhouse! It’s that infamous soda brand known for its insane caffeine content."
            $Atlas_State["eye"] = 13

            Narrator "You immediately regret asking, but decide to keep the coupon anyways... just in case?"

        "Papers on the floor" if mCaseInvest and inv3:
            python:
                inv3 = False
                displaymenu = False
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2

            show robyn:
                ease 1.0 xcenter 0.45

            Narrator "Taking a step back, you feel a crunch under your shoe. You look down, realizing you’ve stepped onto crumpled pages of overdue bills addressed to Elkhorn Radio."

            show robyn:
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
                ease 0.7 yoffset 150 matrixtransform RotateMatrix(0.0, 180.0, -10.0)
                ease 0.7 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

            Narrator  "Crouching down, you pick up a crumpled newspaper scrap accusing Elkhorn Radio of poor working conditions and long work hours. The author seems especially resentful in this article. You mumble the last sentence aloud."

            voice RobynSays("Generic","HmphB")
            Robyn "{i}I hope the station owner faces justice...{/i}"

        "Dead Carnations" if numInvest >= 2 and inv4:
            python:
                inv4 = False
                displaymenu = False
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2

            show atlas:
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.5

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.8


            play sfx emote_realization_sfx
            Narrator "Spilled out of the trashcan is a vase of pink and white carnations, a small card clipped to the side. With a frown, you pluck up the card and read, {i}Here's to five years at Elkhorn Radio and many, many more!{/i}"

            Narrator "Glancing over the card, Atlas scoffs."

            Atlas "Oh that's bad."

        "Trophy Case" if inv5:
            python:
                inv5 = False
                displaymenu = False
                mCaseInvest = True
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2
            show atlas:
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.6
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
            show robyn:
                ease 1.0 xcenter 0.8
            Narrator "Following the trail of papers, you stop at the smashed trophy case with the words \"Stinks worse than Momo\" spray-painted in red over the whole thing." #, stepping over the glass shattered against the floor.

            Narrator "It seemed to have held a variety of commemorations and awards celebrating radio entertainment the station had broadcast."

            Narrator "You shift through the destruction, only finding the remains of awards to obscure bands and talk shows like Shark Infinity, Tiny Red Panda, and DJ Bean Angel. Nothing about Madhouse, though."

            Robyn "Looks like Mike’s really taking this personally."

            #voice atlas_booyah
            Atlas "Duuude! Shark Infinity recorded here—!"


    $numInvest +=1
    if numInvest == 2:  #2 Things have been investigated
        show jamie:
            ease 0.4 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.7 xcenter 0.2

        show robyn:
            ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.6 xcenter 0.85

        show atlas:
            ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.8 xcenter 0.5
        $Atlas_State["phone"] = 1
        Narrator "Atlas stands near the door, scrolling through his phone."
        $Atlas_State["eye"] = 1
        play sfx emote_realization_sfx
        Atlas "Apparently, The Daily Ghost wrote an article about Elkhorn Station."

        Narrator "The mothman skims over the blog post."
        $Atlas_State["eye"] = 3
        $Jamie_State["eye"] = 1
        $Robyn_State["eyes"] = 2

        Atlas "Dude. They didn’t bother mentioning Mike by name."
        show jamie:
            ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        voice jamie_scoffa
        Jamie "Does that matter?"

        Atlas "Mike’s just a faceless green poltergeist to these people. See? Literally, no face."

        Narrator "Atlas holds out his phone, showing off a blurry green mass wearing a hat and a hoodie, it’s difficult to make out."

        Jamie "Isn't that how the whole cryptid gig works?"

        Atlas "I guess you're right."

        Narrator "Jamie shrugs and turns away from Atlas, their tail knocking over the small trash can, spilling the contents over the floor."

        Jamie "Whoops."

    if numInvest >= 7:
        jump endInvestigation


    call dice_roll(rMod=PC_Stats.cStats("brains"), rDiff=3+numInvest, rDesc="Investigation") from _call_dice_roll
    if isRollSuccess:# True:#
        jump investigation_loop #Loop Back
    else:
        jump endInvestigation #End

label endInvestigation:
    Jamie "Alright nerds,, we gotta go."
    $Atlas_State["phone"] = 0


    Narrator "Jamie gestures to the door, their tail flicking impatiently."

    #voice atlas_defeated
    Atlas "Fine... There’s no way I can salvage this."

    Narrator "Atlas begrudgingly leaves the remains of shattered vinyls behind."

    scene BG Hallway Radio Station with Fade(0.75, 0.25, 0.75, color="#000")

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 16
        Atlas_State["sparkle"] = 1

    show atlas:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.5 xcenter 0.8

    Narrator "Atlas briskly marches ahead."

    show atlas:
        xcenter 0.8

    Jamie "\n\n{size=-5}You walk like a pigeon.{/size}"

    show robyn:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 0, 0)
        ease 1.0 xcenter 0.35

    show jamie:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.0 xcenter 0.1

    Narrator "Following Atlas’ voice, you and Jamie turn the corner and stop abruptly. He’s fiddling with the doorknob."

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1


    Atlas "It’s totally jammed—"
    $musicPlayer.playSong()
    $musicNote = 12
    python:
        Atlas_State["eye"] = 3
    show atlas:
        ease 0.3 xcenter 2.0


    play sfx dramatic_boom_b
    Narrator "Atlas is cut short as a hand shoots out from the door, grabbing at the moth’s neck fluff. It stops, confused, and slinks back behind the door."
    show atlas:
        xcenter 1.4
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.5 xcenter 0.8

    python:
        Atlas_State["eyeFrame"] = 5
        Atlas_State["eye"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 0

    Atlas "Guess I scared ‘em off?"

    #show atlas:
        #ease 0.35 xcenter 1.4 matrixtransform RotateMatrix(0.0, 0.0, 90.0) yoffset 700

    show atlas:
        matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            pause 0.1
            ease 0.5 yoffset 700
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0, 0, 180)
        parallel:
            ease 0.5 xcenter 1.2

    Narrator "The door suddenly vanishes, leaving Atlas tumbling into the Studio room."


    $musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_wellwellwella
    Madhouse "{bt=3}Well well well~{/bt}"

    voice mm_whattookyousolong
    Madhouse "What took you so long? Y’all three totally left me hangin’!"

    voice mm_deadairisacareerkiller
    Madhouse "Dead air is a career killer in this line of work. Ya could’ve at least rescheduled with my producer!"

    if not inv1:
        #voice PC_Thinking
        Robyn "You mean the jug headed abomination back in the office?"

        Madhouse "Ah, so you met ol' Debbie!"

        Madhouse "Not much of a talker."

        voice mm_laugha
        Narrator "Madhouse Mike laughs at his own joke."

    #Madhouse "So, who are you and what do you want?"

    hide robyn
    hide jamie
    hide atlas
    show MM_Appears CG
    with { "master" : Dissolve(0.5) }


    Narrator "Suddenly blinking into view, Mike appears in his full ghoulish glory."

    #voice PC_Confused
    Robyn "You’re really REAL!"

    #voice MM_Listening1
    Madhouse "{sc=2}Of course I’m real{/sc}! You think I host a radio show just for kicks? I’ve been waiting for a special guest slot for ages!"

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7
        Atlas_State["sparkle"] = 0

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter -0.5
        yoffset -40
        matrixcolor TintMatrix("#ebabab")
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 35.0) xcenter -0.02
    Atlas "{bt=3}Ohmygosh!{/bt} Mike Madhouse!"

    show atlas:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        pause 1.0
        repeat

    Narrator "Atlas takes a sharp breath, absolutely starstruck at the sight of his hero— a real urban legend."

    show atlas:
        xoffset 0
        xcenter -0.01
        on replaced:
            xcenter -0.05
            matrixtransform RotateMatrix(0.0, 180.0, 35.0)
            ease 0.5 xcenter -0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show jamie:
        xcenter -0.5

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1

    voice atlas_hugefan
    Atlas "Oh boy— I’m a huuuuge fan!"

    hide MM_Appears
    show atlas:
        xcenter 0.3
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        pause 0.65
        ease 0.7 yoffset 0

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 0
        MM_State["mouth"] = 0
        Jamie_State["mouth"] = 1
        Jamie_State["eye"] = 6
        Jamie_State["brow"] = 1
        Jamie_State["armR"] = 0

    show madhouse:
        matrixcolor TintMatrix("#ebabab")
        matrixtransform RotateMatrix(0.0, 0, 0.0)
        xcenter 1.5
        ease 0.5 xcenter 0.85

    show jamie behind atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor TintMatrix("#ebabab")
        ease 1.5 xcenter 0.095
        linear 0.05 xcenter 0.105
        linear 0.05 xcenter 0.095
        linear 0.05 xcenter 0.105
        linear 0.05 xcenter 0.095
        repeat

    show robyn behind atlas:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0.0, 0, 0.0)
        ease 1.0 xcenter 0.45

    voice jamie_growld
    Jamie "{sc=3}Grrrr...{/sc}"

    Narrator "Atlas looks up at Jamie who’s blankly staring at Madhouse, a wild look in their eyes."

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Atlas "Jamie... Don’t."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 6
        Jamie_State["armR"] = 3
        Atlas_State["eye"] = 1
        Robyn_State["mouth"] = 6
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

    show jamie:
        xcenter 0.1
    #Narrator "He turns back towards the phantom and squeaks."


    Atlas "We’re here to join you on tonight’s show!"

    Robyn "And ask you some questions."

    python:
        MM_State["armR"] = 2
        MM_State["armL"] = 2
        MM_State["eyes"] = 0
        MM_State["mouth"] = 3
        Atlas_State["eye"] = 7
        Atlas_State["feelers"] = 3
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 2

    $musicPlayer.playSong()
    Madhouse "Mmm, I don’t think it'd be a good idea."

    Narrator "Madhouse pauses."

    python:
        MM_State["armR"] = 0
        MM_State["armL"] = 0
        MM_State["eyes"] = 1
        MM_State["mouth"] = 5
        MM_State["blush"] = 1
        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 5
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 6

        musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_laughb
    Madhouse "{bt=3}To turn down such big fans!{/bt}"

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 5
        MM_State["mouth"] = 1
        MM_State["blush"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 0
        Jamie_State["armR"] = 0
        Jamie_State["alFace"] = 1
        Atlas_State["eye"] = 3
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2

    Madhouse "Except you, the one with the ram horns,, I don’t deal with devils."

    $Jamie_State["mouth"] = 3
    $Jamie_State["eye"] = 7
    $Jamie_State["armR"] = 0
    $Jamie_State["alFace"] = 0


    Jamie "Bold choice of words for a dead man."

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 5
        MM_State["mouth"] = 4
        Atlas_State["eye"] = 0


    Madhouse "... You're a fire hazard."

    $Robyn_State["mouth"] = 7
    $Robyn_State["eyes"] = 4
    $Robyn_State["brow"] = 2

    Robyn "Sorry Jamie."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 1
        Jamie_State["brow"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["feelers"] = 1
        MM_State["mouth"] = 2
        MM_State["armR"] = 2
        MM_State["armL"] = 2
        MM_State["eyes"] = 0


    Jamie "I understand. Weak-willed spirits tend to fall faint around me."

    python:
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["feelers"] = 0
        MM_State["mouth"] = 9
        MM_State["armR"] = 1
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

    show jamie:
        ease 0.4 matrixtransform RotateMatrix(0.0, 0, 0.0)
        ease 1.0 xcenter -0.3
    Narrator "Atlas does a giddy fist pump to himself and stands up straight."

    voice atlas_booyah
    Atlas "Sweet! I ah— yes, this is business."

    python:
        Atlas_State["eye"] = 6
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 2

    Atlas "I am a serious business boy."

    jump RadioShow
