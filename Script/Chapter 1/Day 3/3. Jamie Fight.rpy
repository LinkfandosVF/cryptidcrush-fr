label Ch1_JamieFightBuildup:
    scene BG Empty Street Day
    play ambiance indoor_crowd fadein 2.0

    camera:
        camera_zoom(x=-200,y=30,z=-300)

    show jamie:
        xcenter 0.65

    show CG Crowd:
        xcenter 0.35
        pause 0.5
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    show CG2 Crowd:
        xcenter 0.6
        block:
            ease 1.8 yoffset 17
            ease 2.2 yoffset 0
            repeat

    show goatmaam:
        xcenter 0.25

    show madhouse:
        xcenter 1.5

        parallel:
            ease 5.0 xcenter 0.55
        parallel:
            idleFloat(1.9,9)

    show robyn:
        xcenter 1.5
        matrixtransform rotated(y=180)

        ease 5.0 xcenter 0.65

    show briggs behind goatmaam:
        flipped
        xcenter 0.1

    show hobbes:
        xcenter 0.5

    show sera behind robyn at flipped:
        xcenter 0.8

    show fridge behind goatmaam:
        xcenter 0.32

    show edward:
        xcenter 0.98
        matrixtransform RotateMatrix(0,180,0)

    with BGDissolve(name="Trans_BM.png",t=1.25)

    camera:
        camera_zoom(y=30,z=-300,t=3)
    python:
        adjustChar("Robyn",eyes=3,mouth=0)
        adjustChar("MM",mouth=0,eyes=0)

    Narrator "Meanwhile, near the dirt lot beside Edith's shop."

    python:
        adjustChar("Robyn",eyes=2,mouth=5)
        adjustChar("MM",mouth=1,eyes=5)
        adjustChar("GM",mouth=5,eyes=1)
        musicPlayer.playSong(song="not_so_spooky_song",fadeOut=3.0)
        timeText = "4:00PM"

    voice gm_laugha

    Goatmaam "Greetings! Are you ready to throw it down?"

    Madhouse "Granny?"

    Goatmaam "Heard through the grapevine that this lot was the place to be!"

    $adjustChar("Robyn",eyes=4,mouth=1,brow=1)

    Robyn "...{nw}"

    python:
        adjustChar("Robyn",eyes=1,mouth=4,brow=2)
        adjustChar("GM",mouth=1,eyes=0)

    Robyn "This feels like a public execution."

    show madhouse:
        xcenter 0.55
        idleFloat(1.9,9)

    show robyn:
        xcenter 0.65

    python:
        adjustChar("Robyn",eyes=3,mouth=1)
        adjustChar("MM",mouth=2,eyes=5)
        adjustChar("GM",mouth=0,eyes=1)

    Goatmaam "No need to worry!"

    $adjustChar("GM",mouth=3,eyes=5)
    show goatmaam:
        matrixtransform rotated()
        yoffset 0
        ease 0.3 matrixtransform rotated(z=15) yoffset 5
    extend "\n\nAggravated exorcism is outlawed in this district."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("MM",mouth=1,eyes=10)

    show goatmaam:
        matrixtransform rotated(z=15)
        yoffset 5
        ease 0.3 matrixtransform rotated() yoffset 0

    Madhouse "You're in on it!?"

    $adjustChar("GM",mouth=5,eyes=1)

    voice gm_wonderful
    Goatmaam "Don't look so glum! You're a performer aren't you?\n\n This'll be fun!"

    python:
        adjustChar("Robyn",brow=0)
        adjustChar("MM",mouth=12,eyes=0)
        adjustChar("GM",mouth=0,eyes=3)

    Madhouse "Look, lady, radio's a strictly audio medium! I-I don't need an audience!"

    $adjustChar("GM",mouth=1,eyes=2)

    Goatmaam "Oh goodness."

    $adjustChar("GM",mouth=0,eyes=0)

    Goatmaam "Come with me, let's get this sorted out."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("MM",mouth=0,eyes=11)

    show madhouse behind briggs:
        parallel:
            idleFloat(1.9,9)
        parallel:
            pause 0.3
            ease 2.0 xcenter -0.3

    show goatmaam:
        matrixtransform rotated()
        ease 0.3 matrixtransform rotated(y=180)
        ease 2.0 xcenter -0.3

    show briggs behind goatmaam:
        xcenter 0.1
        flipped
        pause 0.4
        ease 0.75 xcenter 0.25

    show fridge behind briggs:
        xcenter 0.32

        pause 0.4
        ease 0.75 xcenter 0.5

    Narrator "Madhouse is ushered off by a pint-sized devil. He shoots you a worried look and disappears into the crowd."

    camera:
        camera_zoom(z=-600,y=250,t=0.9)

    Narrator "You glance down at a silvery goblin creature stomping around at your feet. It hisses like an angry cat."

    Robyn "Awww, hey little guy! What're you?"

    show hobbes:
        xcenter 0.5
        jumpSquish(0.15,90,0.2)

    show goatmaam:
        matrixtransform rotated()
        ease 0.3 matrixtransform rotated(y=180)
        ease 2.0 xcenter -0.3

    #$Crowd = Character("Crowd", callback = Bleep,ctc="end_of_msg", cb_id = "9A", who_color = "#bef5ff")

    Madhouse "{sc}GYAAAH!{/sc}"

    Robyn "{sc}-!{/sc}"
    show dewey behind fridge:
        xcenter 0.63

    show fridge behind briggs:
        xcenter 0.5
        ease 0.75 xcenter 0.4

    camera:
        camera_zoom(x=-150,y=30,z=-300,t=0.5)

    hide madhouse
    hide goatmaam

    show robyn:
        matrixtransform rotated(y=180)
        block:
            ease 0.75 xcenter 0.5

            ease 0.15 yoffset -40
            ease 0.15 yoffset 0

            ease 0.25 matrixtransform rotated()

            ease 0.75 xcenter 0.7

            ease 0.15 yoffset -40
            ease 0.15 yoffset 0

            ease 0.25 matrixtransform rotated(y=180)


            repeat

    show hobbes:
        xcenter 0.5
        matrixtransform rotated()

        block:
            ease 1.0 xcenter 0.09

            ease 0.25 matrixtransform rotated(y=180)


    Narrator "You snake around but can't squeeze past the pack of monsters. No one’s listening! You feel so small."

    show robyn:
        ease 0.2 matrixtransform rotated(y=180) xcenter 0.6 yoffset 0
        ease 0.3 xcenter 0.4
        parallel:
            ease 0.3 xcenter 0.5
        parallel:
            ease 0.15 yoffset -30
            ease 0.15 yoffset 0
        parallel:
            matrixtransform rotated(y=180,z=20)
            ease 0.4 matrixtransform rotated(y=180)

    show briggs:
        pause 0.5
        camera_shake
        unflipChar(0.3)

    briggs "{b}WATCH IT!{/b}"

    show briggs:
        ease 0.85 xcenter 0.13

    fridge "Woah, settle down pardner! Don't go swingin' those claws around."

    $adjustChar("Robyn",mouth=1,brow=2,eyes=3)

    show fridge:
        ease 0.75 xcenter 0.35

    Robyn "Sorry!"

    show robyn:
        unflipChar(0.5)
    $adjustChar("Robyn",mouth=5,brow=0,eyes=0)

    dewey "Hey Fridge, where's {b}{color=#fffb42}Walker{/color}{/b}?"

    fridge "Didn't you hear? A couple of meatbags iced him last night. \n\nHe's gone."

    show dewey at vibratenum

    dewey "{bt=3}{b}Ohohoho!{/b}{/bt} \n\nThe {b}{color=#fffb42}Watcher{/color}{/b} ain't gonna be happy about that!"

    dewey "Do they know whodunit?"

    fridge "Yup. And I say good riddance."

    fridge "Maybe Ol' Watchie will start doin' their goddamn job."

    briggs "Who?"

    dewey "Ghost gossip,, don't worry about it."

    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=0)
        adjustChar("Robbie",mouth=0,eye=0)
    show robbie:
        xcenter 1.0
        matrixtransform rotated(y=180)

    voice robbie_scuseme

    show robbie:
        pause 0.25
        ease 0.8 xcenter 0.7

    Robert "'scuse me!"
    camera:
        camera_zoom(x=-20,y=30,z=-300,t=0.9)


    show dewey behind fridge:
        ease 0.75 xcenter 0.75

    #show robyn:
    #    ease 0.25 matrixtransform rotated() xcenter 0.4 yoffset 0

    #    ease 0.5 xcenter 0.7

    #    parallel:
    #        matrixtransform rotated(z=-10)
    #        ease 0.25 xcenter 0.5
    #    parallel:
    #        ease 0.1 yoffset -50
    #        ease 0.1 yoffset 0

    #    ease 0.3 matrixtransform rotated()

    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=0)
        adjustChar("Robbie",mouth=2,eye=2,armR=0)

    Narrator "You bump into Robbie who’s cheering along with the other cryptids."

    Robert "Hey little buddy!"

    hide dewey

    python:
        adjustChar("Robyn",eyes=3,mouth=4,brow=2)
        adjustChar("MM",mouth=1,eyes=0)

    Robyn "Rob, I can't see!"

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("Robbie",mouth=1,eye=5)

    Robert "You’re watching the fight?"

    python:
        adjustChar("Robbie",mouth=0)
        adjustChar("Robyn",eyes=4,mouth=4)

    Robyn "I mean., I guess?"

    python:
        adjustChar("Robbie",mouth=5,eye=0)
        adjustChar("Robyn",eyes=2,mouth=1,brow=1)

    voice robbie_laughb
    Robert "Here,, I gotcha."

    camera:
        camera_zoom(t=0.5)

    show robyn:
        ease 0.4 yoffset 700

    show robbie:
        ease 0.4 yoffset 700

    show CGShade:
        on hide:
            alpha 0.35
            ease 0.75 alpha 0

    show CG_Rob Carry:
        yoffset 700
        xcenter 0.5
        pause 0.3
        ease 0.4 yoffset 0

    show fridge behind briggs:
        ease 0.75 xcenter 0.3

    show briggs:
        ease 0.75 xcenter 0.15

    show sera:
        ease 0.6 xcenter 0.85 matrixtransform RotateMatrix(0,180,0)

    Narrator "Robbie scoops you up and sets you on his shoulders. You yelp! In a scramble to grab something, you yank the thick barbels on the fishman's jaw and he nearly drops you."

    Robert "{sc}ACK!{/sc}"

    show madhouse behind jamie:
        xcenter 0.3
        yoffset 700
        ease 0.5 yoffset 0
        idleFloat(2,9)

    Robyn "Sorry!"

    Narrator "You wrap your arms around Rob's neck."

    Narrator "He shoves through the crowd, parading you around like a party hat. You apologize for the frogman as you reach the inner circle."

    $adjustChar("MM",eyes=0,mouth=1,armR=2,armL=3)

    show briggs:
        ease 0.6 xcenter -0.1

    show fridge:
        ease 0.6 xcenter -0.1

    show hobbes:
        ease 1.0 yoffset 300
        xcenter 0.5

    show edward:
        ease 0.6 xcenter 1.1
        flipChar(0.5)

    show sera:
        ease 0.6 xcenter 1.1

    show CG Crowd:
        ease 0.6 xoffset -750 yoffset 0

    show CG2 Crowd:
        ease 0.6 xoffset 750 yoffset 0

    show CG_Rob Carry:
        ease 0.6 yoffset 700

    with None
    hide CGShade with nwDissolve(0.25)
    python:
        musicPlayer.playSong(fadeOut=5.0)
    Narrator "Madhouse clutches his hat. He looks like he wants to disappear down the nearest storm drain."

    Madhouse "You invited these freakshows?"
    hide CGShade
    hide CG_Rob Carry

    Jamie "Not a chance!"

    Robyn "{size=40}Heeey!{/size}"

    Narrator "You catch the ghost's eye and his face lights up. You pump your fist and cheer from the sidelines."

    hide CG Crowd
    hide CG2 Crowd
    hide CG_RobbieRobynDuo

    show CG_RobbieRobynDuo behind madhouse:
        xcenter 0.25
        yoffset 700
        ease 0.4 yoffset -30
        block:
            ease 0.15 yoffset 0
            pause 0.1
            ease 0.15 yoffset -40
            repeat

    show CG Crowd behind madhouse:
        xcenter 0.35
        xoffset -750
        ease 0.6 xoffset 0
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    show CG2 Crowd behind madhouse:
        xcenter 0.65
        xoffset 750
        ease 0.6 xoffset 0
        pause 0.5
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    show hobbes behind madhouse:
        flipped
        xcenter 0.2
        ease 1.0 yoffset 0

    show briggs behind hobbes:
        ease 0.6 xcenter 0.05

    show edward behind madhouse:
        flipped
        ease 0.6 xcenter 0.95

    show sera at flipped behind edward:
        ease 0.6 xcenter 0.85

    Robyn "You can do it! Treat this like one of your radio shows Mike! Go Jamie, go!"

    call dice_roll(99,12,"Cheer") from _call_dice_roll_70

    show madhouse behind jamie:
        matrixtransform rotated()
        parallel:
            idleFloat(2,9)
        parallel:
            ease 0.4 matrixtransform rotated(y=180)
            block:
                ease 0.08 xoffset 5
                ease 0.08 xoffset -5
                ease 0.08 xoffset 5
                ease 0.08 xoffset -5

    $adjustChar("MM",mouth=6)
    Narrator "Your words inspire the ghoul."

    show CG_RobbieRobynDuo behind madhouse:
        ease 1.0 yoffset 700

    $adjustChar("MM",armL=0,armR=0,mouth=7)
    $adjustChar("MM",mouth=11,eyes=0)

    Madhouse "Do you have any idea who you're messin' with?"

    Madhouse "I'm gonna kick your fu{nw}"

    python:
        adjustChar("GM",eyes=2,mouth=5,armL=1,armR=2,ears=1)
        adjustChar("Jamie",eye=8,mouth=0)
        adjustChar("MM",mouth=1,eyes=2,armR=2,armL=2)

    show madhouse:
        ease 0.5 blur 3

    show jamie:
        ease 0.5 blur 3

    show edward:
        ease 0.5 blur 3

    show sera behind robyn at flipped:
        ease 0.5 blur 3

    show briggs:
        ease 0.5 blur 3

    show CGShade

    show goatmaam:
        xcenter 0.45
        yoffset 700
        zoom 2
        matrixtransform rotated(z=-12)
        ease 0.5 yoffset 140

    voice gm_ahahahb
    Goatmaam "{bt=3}Language, Michael!{/bt}"

    python:
        adjustChar("GM",eyes=4,mouth=1,ears=0,armL=2,armR=1)

    Goatmaam "Now listen kiddos, I want a good, clean fight!"

    show goatmaam at startledSquish:
        matrixtransform rotated(z=0)

    python:
        adjustChar("GM",eyes=1,mouth=3,ears=1)

    voice gm_laughb
    Goatmaam "So no biting, no dying, and most importantly,\n\n {size=30}{b}have fun!{/b}{/size}"

    show madhouse:
        ease 0.5 blur 0

    show jamie:
        ease 0.5 blur 0

    show edward:
        ease 0.5 blur 0

    show sera behind robyn at flipped:
        ease 0.5 blur 0

    show briggs:
        ease 0.5 blur 0

    show goatmaam:
        yoffset 140
        ease 0.8 yoffset 900

    with None
    hide CGShade with nwDissolve(0.3)

    $adjustChar("Jamie",eye=6,armR=2,r3Fire=1,mouth=1)
    Jamie "We're gonna have {sc=2}{b}{color=#EC2A2A}so much fun{/color}{/b}{/sc}."

    stop ambiance

    $adjustChar("Jamie",eye=7,armR=2,r3Fire=1,mouth=2)

    call FIGHT_06_JAMIE from _call_FIGHT_06_JAMIE_1

    jump Ch1_JamieFightAftermath

image divider:
    Solid("#000000")
    size (20,720)

image atlas_callBG:
    size(1280,720)
    ycenter 0.5
    "images/BGs/Chapter 1/atlasroom_wip.png"

label Ch1_JamieFightAftermath:


    camera at camera_default
    stop music
    python:
        HighlightEnemyUnitBars([])
        HighlightPlayerUnitBars([])
        musicPlayer.playSong(song="silence",fadeOut=2.0,fadeIn=2.0)

    if mmLives:
        $persistent.unlockedDice[10] = True
        Narrator "You've unlocked new dice! Check them out in the dice changing menu!"

        play sfx crowd_cheer

        show CGShade

        python:
            adjustChar("GM",eyes=4,mouth=5,ears=1,armL=1,armR=2)
        show goatmaam:
            xcenter 0.45
            yoffset 700
            zoom 2
            matrixtransform rotated(z=-5)
            ease 0.5 yoffset 140

        Goatmaam "It's finished!"

        play ambiance indoor_crowd fadein 2.0

        Narrator "The white goat steps into the fray, cutting the combatants off where they stand."

        scene BG Empty Street Night
        camera:
            camera_zoom(x=-60,y=-60,z=-150)
        show Jamie_Battle_MM_CG Default at climbfromhole:
            xcenter 0.45
            matrixcolor TintMatrix("#ffe0ba")
            zoom 1.5
        with dissolve

        Goatmaam "{size=30}The Elkhorn Radio Ghost wins!{/size}"

        Madhouse "{size=15}I-I did?{/size}\n\n{sc=3}I won?{/sc}"

        hide Jamie_Battle_MM_CG Default

        play music digihouse_mike_song
        show CG Mike Wins:
            parallel:
                hoppies(xIntensity=4)
            parallel:
                startledSquish

        voice mm_laughk
        camera:
            camera_shake

        play ambiance angry_crowd fadein 2.0

        Madhouse "{sc=10}{size=40}\nHYUAHAHAHAAA{/size}{/sc}\n\nIn your face!!"

        Madhouse "{size=40}Madhouse Mike rules this ghost town baby! YEAH!{/size}"

        show CG Mike Wins:
            ease 0.5 yoffset 0 matrixtransform rotated(y=180) yzoom 1 xzoom 1 xoffset 0
            idleFloat(2.2,10)

        Narrator "A dull roar rolls across the crowd. Some politely clap while others boo. \n\nIt's mostly boos."

        show CG Mike Wins at startledSquish

        voice mm_laughe

        Madhouse "They love me!"

        #Madhouse "I won! Hahahaa! Meatball didja see me—?!"

        stop music
        scene BG Black
        with dissolve

        play ambiance indoor_crowd fadein 2.0

        Jamie "Nice job. Sure, you had some outside encouragement."

        Jamie "But you stood your ground."

        stop ambiance

        Narrator "The mumbling crowd slowly disperses, quickly losing interest as the two fighters chat."


    else:

        Narrator "Madhouse struggles to keep his shape and collapses on the ground."

        Goatmaam "{size=35}AND MATCH!{/size} \n\nThat's it!"

        Narrator "The white goat steps into the fray, cutting the combatants off where they stand."

        play sfx crowd_cheer
        Goatmaam "The Jersey Devil wins!"
        camera:
            camera_zoom(x=-60,y=-60,z=-95)

        scene BG Empty Street Night
        show CG Jamie Wins
        with dissolve

        Narrator "The fight is over."

        #Narrator "The green drama queen lies in a pool of smoldering sludge. With a concerned look, Jamie crouches down and pokes the ghost."

        #Narrator "In one swift motion, they peel Madhouse off the ground and he snaps back together."

        Narrator "Cheers roll across the crowd. Some applaud while others howl. Jamie doesn't acknowledge the onlookers."

        camera:
            camera_zoom(x=-60,y=40,z=-80,t=1.2)
        Jamie "Not bad."

        Jamie "But you’ll have to fight better than that to beat me."

        Madhouse "Tch,, who's to say I wasn't goin' easy on ya?"

        play sfx ["<silence .65>", "audio/SFX Battle/Hurt_B.ogg"]
        play voice2 ["<silence .65>", "audio/Voice/MAdhouse/Battle/MM_DamagedG.ogg"]
        camera:
            pause 0.65
            camera_shake
        Narrator "The devil stomps the pool of ooze."

        Jamie "Your arrogance will be your undoing."

        scene BG Black
        with dissolve

    #Narrator "Robbie lifts you off his shoulders and sets you down."

    #Robert "'Ey, we make a pretty good team."

    #Robyn "Ah, yeah! You make a great step ladder."

    #Robert "Keheh! These broad shoulder’s gotta be good for somethin'."

    voice thursday_cawa
    Thursday "{size=40}GRAAAWH!{/size}"

    Narrator "Edith storms out of the clinic."

    Edith "No fighting on clinic grounds! Get off our property!"

    Edith "{sc=3}{b}OZZIE!!{/b}{/sc}"

    Narrator "The lingering crowd scatters. Cryptids dart every which way and Goatma’am disappears in a puff of purple smoke."

    Narrator "Alas, you four aren't so lucky."

    scene BG SunsetRoadside
        #matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")

    camera:
        camera_zoom(z=-350,x=100)
        shaded("#ffc6c1")

    show robyn at flipped:
        xcenter 0.45

    show jamie:
        xcenter 0.8

    show madhouse behind robyn:
        xcenter 0.6

    show robbie at flipped behind jamie:
        xcenter 0.6

    show edith at flipped:
        ease 0.8 xcenter 0.2

    show oswald at flipped behind edith:
        ease 0.8 xcenter 0.15

    show Thursday Default at flipped behind oswald:
        ycenter 0.22
        ease 0.8 xcenter 0.15

    with { "master" : Dissolve(0.5) }

    python:
        adjustChar("MM",mouth=2,eyes=0,armL=1,armR=1)
        adjustChar("Robbie",mouth=0,eye=1)
        adjustChar("Jamie",mouth=0,eye=1,fire=0)
        adjustChar("Robyn",mouth=5,eyes=1,brow=2)
        adjustChar("Edith",mouth=0,eye=1,brow=0)
        adjustChar("OH",eyes=5,brow=0,eyeFrame=1)
        timeText = "4:30PM"

    Edith "A street fight?!"

    Edith "You're {size=30}{b}ADULTS{/b}{/size}!"

    camera:
        camera_zoom(z=-180,x=-80,t=2.0)

    Edith "You're lucky I don't call public safety. Who's idea was this?!"
    $adjustChar("Jamie",mouth=4,eye=3,brow=3,sweat=1,armR=4)
    Jamie "I-It was-.,"
    python:
        adjustChar("MM",mouth=2,eyes=5)
        adjustChar("Robbie",mouth=0,eye=0)
        adjustChar("Jamie",mouth=0,alFace=True)
        adjustChar("Robyn",eyes=0,brow=0)
        adjustChar("Edith",mouth=0,eye=1,brow=2)
        adjustChar("OH",eyes=6,brow=0,eyeFrame=0)

    show robbie at flipped behind jamie:
        ease 2.3 xcenter 1.0

    show madhouse behind robyn:
        ease 0.8 xcenter 0.45

    show robyn at flipped:
        ease 1.2 xcenter 0.6

    show jamie at startledSquish

    Madhouse "It was me. I'm the one picking fights."
    hide robbie
    python:
        adjustChar("Robyn",eyes=2)
        adjustChar("Edith",mouth=0,eye=0,brow=1)
        adjustChar("OH",eyes=5,brow=0)

    Edith "Terrorizing the radio station wasn't enough for you?"
    python:
        adjustChar("Edith",mouth=2,eye=1,brow=2)
        adjustChar("OH",brow=4)
        adjustChar("MM",mouth=9)

    Madhouse "That glorified shoe closet? Not a chance! I'm a ghost with star-studded dreams sweetheart!"

    $adjustChar("Edith",mouth=1,eye=2,armR=1)
    show edith at flipped:
        ease 0.8 xcenter 0.24
    Edith "You can drop the act."

    python:
        adjustChar("Edith",armR=0)
        adjustChar("OH",eyes=5,brow=0)
        adjustChar("MM",mouth=1,armL=2,armR=2)

    Madhouse "..."

    show jamie:
        ease 0.8 xcenter 0.75
    python:
        adjustChar("Edith",eye=2,mouth=0)
        adjustChar("OH",eyes=6)
        adjustChar("MM",mouth=2)
        adjustChar("Jamie",mouth=2,eye=2,alFace=False)

    Jamie "I'm also at fault Doctor Hocus! I ah,, I'd feel bad letting Mike take the blame."

    show robyn at flipped:
        ease 0.8 xcenter 0.55
    $adjustChar("Robyn",mouth=1,eyes=4,brow=2)
    $adjustChar("Edith",eye=1,mouth=2)
    Robyn "And I'm double at fault,, I egged them on."

    $adjustChar("MM",mouth=3)
    show madhouse at startledSquish
    Madhouse "Triple."

    python:
        adjustChar("Edith",eye=0,mouth=1)
        adjustChar("OH",eyes=1,brow=1)
        adjustChar("Jamie",mouth=0,eye=2,sweat=0,armL=1,armR=1)
        adjustChar("Robyn",mouth=5,brow=0,eyes=2)

    Edith "Alright, just., be careful okay? Don't let us catch you doing anything reckless."

    $adjustChar("OH",eyes=5,brow=0)

    Edith "Right Ozzie?"

    $adjustChar("OH",eyes=4,brow=5)
    show edith at flipped:
        ease 2.7 xcenter -0.2

    show oswald at flipped:
        ease 3.0 xcenter -0.2

    show Thursday Wings at flipped:
        yoffset -260
        ease 0.5 yoffset -700

    Thursday "Don't let it happen again!"

    $adjustChar("Robyn",mouth=0,eyes=3)
    Robyn "Understood."

    show robyn at unflipCharDelayed(0.7,0.5)
    $adjustChar("Robyn",eyes=2,brow=1)
    Robyn "Oh! Hey, let me walk you home."

    show madhouse:
        ease 0.3 xzoom 0 yoffset -100 alpha 0 blur 30

    $adjustChar("Robyn",eyes=4,brow=2)
    Robyn "I think Mike needs some space."

    scene BG Black
    with Dissolve(0.75)
    Jamie "Aw, I appreciate the gesture."
    jump Ch1_WalkHomeWithJamie

layeredimage CG MM_PhoneSide:
    anchor (-0.01,0.1)
    zoom 0.25

    group phonestate:
        attribute black default:
            "images/CGs/Chapter 1/MM_PhoneCG3.webp"

        attribute calm:
            "images/CGs/Chapter 1/MM_PhoneCG2.webp"

        attribute smirk:
            "images/CGs/Chapter 1/MM_PhoneCG1.webp"

        attribute green:
            "images/CGs/Chapter 1/MM_PhoneCG4.webp"

label Ch1_WalkHomeWithJamie:
    scene BG Sky Night

    show jamie:
        xcenter -0.2
        matrixtransform rotated(y=180)
        pause 2.0
        ease 2.0 xcenter 0.5
        ease 0.5 matrixtransform rotated()

    show robyn:
        xcenter -0.2
        pause 2.5
        ease 2.0 xcenter 0.25

    camera:
        shaded("#ebc0f8")
        camera_zoom(z=-550,y=-50,x=-250)
        camera_zoom(z=-240,y=-30,x=-180,t=5.0)

    python:
        adjustChar("Jamie",brow=0,eye=3,armR=0,r3Fire=0)
        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
        musicPlayer.playSong(song="undead_icebreakers_song",fadeIn=1,fadeOut=2)
        timeText = "4:40PM"

    play ambiance forest_ambianceb fadein 5.0 fadeout 4.0

    with nwDissolve(0.5)

    Robyn "That was some fight."

    $adjustChar("Jamie",brow=1,eye=0)

    Jamie "You think so? \n\nI thought it was a perfect way to end a long work day."
    python:
        adjustChar("Jamie",brow=0,eye=1,mouth=0)
        adjustChar("Robyn",mouth=4,brow=1,eyes=4)
    show robyn:
        xcenter 0.25
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 15.0)

    Robyn "Why're you working a job like that anyways? \n\nIt doesn't seem like your style."
    python:
        adjustChar("Jamie",eye=3)
        adjustChar("Robyn",mouth=5,brow=0)
    Jamie "It's the best I have."

    Jamie "I was a telemarketer for a time but, after enough caller complaints they let me go."
    python:
        adjustChar("Jamie",mouth=1,brow=3,eye=4,armR=1,wispEyes=1)
        adjustChar("Robyn",mouth=1)
    Jamie "Apparently my energy is off-putting."
    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
    python:
        adjustChar("Jamie",eye=3,mouth=0,brow=0,wispEyes=0)
        adjustChar("Robyn",mouth=3,eyes=1)

    Robyn "Mnh, I don't see it."
    $adjustChar("Jamie",eye=1,armR=4)
    $adjustChar("Robyn",mouth=5,eyes=2)

    Jamie "After that, I took a summoning gig. Humans recite a spell, scrawl out a sigil, and I appear. With payment of course."
    $adjustChar("Jamie",eye=6,brow=1,armR=2,r3Fire=1,wispEyes=3)

    Jamie "Parties, abandoned malls, and college dorms. Wherever you'd think to summon a monster."

    $adjustChar("Jamie",brow=0,eye=1,mouth=0,r3Fire=0,armR=3)

    Jamie "It was never boring. \n\nBut I'm not some novelty to be gawked at."
    $adjustChar("Robyn",mouth=1,eyes=0,brow=1)

    Robyn "When you say {i}payment{/i} do you mean like., {sc=3}human sacrifice?{/sc}"

    $adjustChar("Jamie",eye=1,armR=4)

    Jamie "Money."

    show robyn at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    $adjustChar("Robyn",mouth=6,eyes=3,brow=2)

    Robyn "Same thing."
    #Robyn "P-People pay for that sorta thing?"

    #Jamie "Yes"

    #Jamie "Being a barista isn't so bad."

    #Jamie "The boss checks in every solar eclipse but aside from that, we've got free reign."

    $adjustChar("Jamie",brow=1,eye=3,mouth=4,armR=4,wispEyes=1)
    Jamie "What about you? What do you do?"
    python:
        adjustChar("Jamie",brow=0,eye=1,mouth=0)
        adjustChar("Robyn",mouth=4,brow=1,eyes=4)

    Robyn "Nothing right now, but I’ve got a job lined up this weekend. It’s near the lighthouse! Atlas said they were looking for fresh meat."

    $adjustChar("Robyn",mouth=0,brow=0,eyes=2)
    Jamie "And the pay?"

    $adjustChar("Robyn",mouth=6,brow=1,eyes=3)
    Robyn "A pirate’s bounty!"

    $adjustChar("Jamie",brow=0,eye=4,mouth=2)
    Jamie "Eee.,urgh."

    $adjustChar("Jamie",mouth=4,eye=3,brow=3,sweat=1,armR=1)
    Jamie "Wouldn’t you prefer something safer?"

    $adjustChar("Jamie",mouth=0,eye=0,sweat=1,armR=1)
    Jamie "What if I spoke with my manager? Maybe I could get you an interview."
    show robyn:
        flipCharDelayed(0.8,0.5)
    python:
        adjustChar("Jamie",eye=3,brow=0,wispEyes=0,armR=4)
        adjustChar("Robyn",mouth=5,brow=0,eyes=1)

    Robyn "Mmm'nah it's okay. My rent is due soon."

    Jamie "Who’s your landlord?"

    $adjustChar("Robyn",mouth=3,eyes=4)
    Robyn "Never met them. I mailed in the application, got the keys, and Atlas helped me move in."

    python:
        adjustChar("Robyn",brow=2)
        adjustChar("Jamie",mouth=4,brow=3)

    Jamie "Are you squatting?"

    $adjustChar("Robyn",mouth=2,eyes=0)
    Robyn "What? No! I mean,, I haven’t seen any other tenants yet, but the place isn’t abandoned!"

    python:
        adjustChar("Robyn",eyes=2,brow=1,mouth=3)
        adjustChar("Jamie",eye=1,brow=3,mouth=0,sweat=False)

    Jamie "Right, I’m sorry for jumping on you like that."
    $adjustChar("Jamie",eye=4,brow=1,mouth=2,armR=1)
    Jamie "I'm surprised you trust Atlas' ability to., do tasks."

    $adjustChar("Robyn",eyes=1,brow=0,mouth=5)
    Robyn "It's fine."

    $adjustChar("Jamie",brow=0,eye=3,mouth=0,armR=4,wispEyes=2)

    Jamie "Longhope isn’t exactly the cryptid metropolis I was expecting."

    Jamie "Everything’s so quiet here."

    $adjustChar("Robyn",mouth=0,eyes=0)
    Robyn "I’m just happy we’ve got sidewalks."
    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
    $adjustChar("Robyn",mouth=4,eyes=2)

    Robyn "Why's it called Longhope anyway?"

    $adjustChar("Jamie",mouth=4)
    $adjustChar("Robyn",mouth=5)

    Jamie "Some guy named Walker renamed it. Poor sap."

    python:
        adjustChar("Jamie",eye=2,mouth=0)
        adjustChar("Robyn",eyes=2,brow=2)
    Robyn "What happened to them?"

    Jamie "Atlas would know. You should ask him later."

    $adjustChar("Robyn",brow=1,mouth=0,armR=1,eyes=3)
    Robyn "Using the power of modern technology,, I can ask him now!"

    $adjustChar("Jamie",eye=1,armR=0)
    Jamie "Dork."

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, -15.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "You dial the mothman’s number and put him on speaker phone. He picks up."
    $musicPlayer.playSong(song="astral_reflection",fadeIn=1,fadeOut=1)
    show robyn at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show atlas_callBG:
        xpos 1.0
        ease 0.75 xpos 0.575

    show divider:
        xpos 1.0
        ease 0.75 xpos 0.575

    show atlas:
        matrixcolor ColorizeMatrix("#261829","#f5cfff")*SaturationMatrix(0.2)
        xcenter 1.1
        matrixtransform rotated(z=12)
        ease 0.75 xcenter 0.75

    camera:
        camera_zoom(z=-240,y=-30,x=30,t=0.75)

    python:
        adjustChar("Robyn",msg=True,mouth=6,eyes=0)
        adjustChar("Jamie",eye=4,brow=0,armR=1)
        adjustChar("Atlas",eye=6,armL=2,sparkle=True,phone=1)

    Atlas "{sc=3}{size=30}HEEEEY BESTIE!{/size}{/sc}"

    Narrator "You immediately turn the volume down."

    python:
        musicPlayer.playSong(song="silence",fadeIn=1,fadeOut=2)

        adjustChar("Jamie",eye=1,brow=0)
        adjustChar("Robyn",mouth=0,eyes=2)
    Jamie "Atlas, can you tell us about Mister Walker?"

    show atlas:
        xcenter 0.75
        matrixtransform rotated(z=12)
        ease 0.5 matrixtransform rotated()

    $adjustChar("Atlas",eye=1,armL=0,sparkle=False,eyeFrame=5)
    Atlas "Jamie?! What're you two doing?"

    python:
        adjustChar("Robyn",brow=0)
        adjustChar("Jamie",armR=0)
        adjustChar("Atlas",eye=17,eyeFrame=0)

    Jamie "Loitering."

    $adjustChar("Atlas",eye=4,feelers=0)
    show atlas at startledSquish
    Atlas "The most innocuous crime!"

    $adjustChar("Atlas",eye=16)
    Robyn "I wanted to ask if you knew anything about Longhope's founder?"

    $adjustChar("Atlas",eye=1)

    Atlas "Oh, sure! One sec."

    play music wistful_ones_song

    show atlas at flipCharDelayed(0.7,0.5)
    $adjustChar("Atlas",eye=2,feelers=1)

    Atlas "Mister Walker was born in Tacoma, California, to a family of cobblers. He was a simple guy who dreamt of restoring his abandoned hometown, Soot Lung."

    $adjustChar("Atlas",eye=0,feelers=3)
    Atlas "But, upon returning to his hometown, he found it had been overrun with monsters!"

    show jamie at vibratenum
    $adjustChar("Jamie",armR=4,eye=6,mouth=1,sweat=1)

    Jamie "Skip to the end."

    show atlas at vibratenum

    python:
        adjustChar("Atlas",eye=18,feelers=0)
        adjustChar("Jamie",armR=0,eye=7,mouth=0,sweat=1)

    Atlas "Grumpy!"

    $adjustChar("Atlas",eye=8,feelers=1)
    $adjustChar("Robyn",mouth=1,eyes=2)

    Atlas "Mister Walker armed himself with an axe and a prayer, only to be devoured by the very place he sought to claim!"

    $adjustChar("Atlas",eye=9,feelers=2)
    $adjustChar("Robyn",mouth=5)

    Atlas "The townsfolk searched and searched, but all that remained of Mister Walker was a lit lantern at the forest’s edge."

    $adjustChar("Robyn",eyes=1,brow=2)
    $adjustChar("Atlas",eye=6,feelers=0)
    Atlas "They say he still wanders as a haggard shadow of his former self, searching for the life the wilds cut short."

    $adjustChar("Robyn",eyes=0,brow=1,mouth=4)
    show robyn at vibratenum

    Robyn "NO WAY! A lantern? A shadow?! That guy tried to kill me!"

    show atlas at unflipCharDelayed(0.7,0.5)

    python:
        adjustChar("Robyn",eyes=2,mouth=1)
        adjustChar("Jamie",eye=3,sweat=0,armR=1)
        adjustChar("Atlas",eye=3,feelers=1)

    Atlas "Where?"

    Robyn "At the graveyard last night!"
    python:
        adjustChar("Jamie",eye=4,armR=0)
        adjustChar("Atlas",eye=1,feelers=2)

    Jamie "ALONE?"

    python:
        adjustChar("Robyn",eyes=4,mouth=5)
        adjustChar("Jamie",eye=3)
        adjustChar("Atlas",eye=0,feelers=0)

    Robyn "No, I uh, w-well, I was with Oz and August."

    Jamie "Are you okay?"

    python:
        adjustChar("Robyn",eyes=3,mouth=0,brow=2)
        adjustChar("Jamie",eye=4,armR=4)
        adjustChar("Atlas",eye=2,feelers=1)

    Robyn "Oh yeah, I’m okay. A shadow man’s nothing, I’ve seen worse."

    $adjustChar("Robyn",eyes=2)
    Robyn "At least now I know who I was dealing with. Jeez, people need to mind their own business."
    $adjustChar("Robyn",eyes=4,mouth=0,brow=0)
    Jamie "You’re really serious about this ghost stuff."

    python:
        adjustChar("Robyn",eyes=2,mouth=3)
        adjustChar("Jamie",eye=3)
        adjustChar("Atlas",eye=1,feelers=0,eyeFrame=3)

    show jamie:
        xcenter 0.5
        matrixtransform rotated()
        ease 0.5 matrixtransform rotated(y=180) xcenter 0.35

    show atlas:
        xcenter 0.75
        matrixtransform rotated()

        ease 0.5 matrixtransform rotated(z=-30) xcenter 0.6

    Atlas "Aaaawh, invite me next time!"
    python:
        adjustChar("Robyn",eyes=1,mouth=4)
        adjustChar("Atlas",eye=0)

    Robyn "As long as you’re not babysitting I will."

    python:
        adjustChar("Robyn",mouth=5)
        adjustChar("Jamie",eye=4,armR=4)
        adjustChar("Atlas",eye=17,feelers=1,eyeFrame=0)

    Atlas "Psh, I’m sure I could’ve brought June along."

    Jamie "No."
    $adjustChar("Atlas",eye=12,feelers=0)

    Atlas "You people are such babies! Y'know, when I was a kid my dad would let me do whatever the heck I want!"

    $adjustChar("Jamie",eye=1,sweat=1)
    Jamie "Yeah, we can tell."

    $adjustChar("Robyn",eyes=4,mouth=0,brow=0)

    Robyn "Alriiiight we’re gonna go now! Bye!"
    stop music

    show jamie:
        xcenter 0.35
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated() xcenter 0.5

    show atlas:
        xcenter 0.6
        yoffset 0
        matrixtransform rotated(z=-30)

        ease 0.25 matrixtransform rotated(z=-90) yoffset 200 xcenter 0.55
        pause 0.5

    show atlas_callBG:
        xpos 0.575
        ease 0.5 xpos 1.0

    show divider:
        xpos 0.575
        ease 0.5 xpos 1.0


    $adjustChar("Robyn",msg=False,armR=0)
    $adjustChar("Atlas",eye=7,feelers=1)
    Narrator "You hang up."

    python:
        adjustChar("Robyn",mouth=5,eyes=2)
        adjustChar("Jamie",eye=7,armR=2,r3Fire=1,mouth=2)

    hide divider
    hide atlas_callBG
    show atlas:
        matrixtransform rotated()
        yoffset 500
        xcenter 0.55
        ease 0.45 yoffset 0
        ease 0.3 matrixtransform rotated(y=180)
        ease 0.75 xcenter 1.25

    Jamie "If I ever meet {b}the Mothman{/b}, I’m going to kick his ass."

    $adjustChar("Robyn",mouth=0,eyes=3)
    show robyn at vibratenum
    hide atlas
    Robyn "C'mon, he’s not that bad!"
    python:
        adjustChar("Robyn",mouth=1,eyes=1)
        adjustChar("Jamie",r3Fire=0,eye=3,mouth=0)

    scene BG Black
    camera:
        camera_default
    with Dissolve(0.75)

    Jamie "Hmph. Well, this is my stop. I'll catch you later."

    Narrator "Jamie's leaving! You consider giving them a—{nw}"

    menu:
        extend ""

        "Goodbye hug":
            Robyn "Before you go, would you like a hug?"

            Jamie "From you? Sure."

            show CG Jamie Hug
            with Dissolve(0.5)

            Narrator "You through your arms around Jamie and give them a big hug."

            Narrator "Their velvet red fur is toasty to the touch. You could easily fall asleep in their crushing arms."

            Narrator "Jamie pats your back."

            Jamie "Got that out of your system?"

            Robyn "Yeah."

            Narrator "You hold the hug for a few breaths before letting go."

            Jamie "Cool. \n\nStay., safe."
            scene BG Black
            camera:
                camera_default
            with Dissolve(0.75)

        "Goodbye wave":
            pass

    Narrator "With a friendly wave, you and Jamie part ways."

    jump Ch2_TaroAlone

image CG LexHand:
    zoom 0.3
    xanchor 0.5
    yanchor 0.0

    ypos 0.0
    xpos 0.5

    "images/CGs/Chapter 2/CG_LexHandOpen.webp"

image CG LexHandGrab:
    zoom 0.3
    xanchor 0.5
    yanchor 0.0

    ypos 0.0
    xpos 0.5

    "images/CGs/Chapter 2/CG_LexHand.webp"

image CG LexHandGrabAnim:
    zoom 0.3
    xanchor 0.5
    yanchor 0.0

    ypos 0.0

    "images/CGs/Chapter 2/CG_LexHandOpen.webp"

    pause 2.5
    "images/CGs/Chapter 2/CG_LexHand.webp"

    zoom 0.375
    easein 0.15 zoom 0.3



label Ch2_TaroAlone:

    Narrator "..."

    scene BG Apartment Bedroom
    $adjustChar("Taro",eye=5,pawL=1,pawR=2)

    show taro:
        xcenter 0.5
        idleFloat(1.9,9)

    camera at camera_default:
        shaded("#cbc4ff")

    with Dissolve(0.5)
    voice taro_tired
    Narrator "Back at the apartment, Taro sleeps tightly curled up on your pillow."

    Narrator "The cat rolls onto her back and stretches out like a slinky."

    $adjustChar("Taro",mouth=2)
    voice taro_laugha
    Narrator "She dreams of destruction."

    Narrator "If it weren't for her tiny stature and weak constitution this universe would have fallen a millennia ago."

    $adjustChar("Taro",eye=1,mouth=3)
    Narrator "She's no guardian angel. She's a petty thief who takes what isn't hers."

    $adjustChar("Taro",eye=1,mouth=1)
    voice taro_annoyedb
    Taro "Uuugh, quit lying! I'm trying to sleep."

    show CG LexHandGrabAnim:
        xcenter 0.45
        yoffset -700
        ease 2.5 yoffset -200
        yoffset -100

    show taro:
        pause 2.5
        ease 0.15 zoom 0.25 xcenter 0.45

    $adjustChar("Taro",eye=3)
    Narrator "....,"

    show CG LexHandGrab:
        yoffset -100
        xcenter 0.45
        ease 1.0 yoffset -700

    hide taro
    voice taro_meowd
    Taro "Mreow!"

    #Narrator "Taro, Taro.\n\nIf that is your real name."

    #Narrator "Do you have any idea what you've done?"

    #Narrator "You've set things in motion that can't possibly be stopped."

    jump Ch1_WalkingHome_Day3
