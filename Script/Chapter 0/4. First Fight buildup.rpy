label fightbuildup:
    $musicPlayer.playSong(song="the_visitor_radio_song",fadeOut=1,fadeIn=5)
    pause 0.01
    scene BG Black
    python:
        timeText = "2:30AM"

        MM_Stats = Unit("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}",1,1,2,0,1,1,25)
        MM_Stats.baseDiff = 5
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(1) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01_MM_MM_ATTACK")
        MM_Stats.SetMTA(3)

        enemyUnits = []
        enemyUnits.append(MM_Stats)

        attackDescA = "You expect me to punch this guy?!"
        attackDescB = "Yeeeah, I could use some emotional support."
        attackDescC = "I feel like you're trying to tell me something..."
        attackDescD = "Huh, this name's certainly a choice."

        playerUnits[0].attacks = [
                    AttackMove("Bash",attackDescA, 0, "madlas_tutorial2", "brawn", "hustle", 0, False, [],0),
                    AttackMove("Cheer",attackDescB, 0, "madlas_tutorial2", "charm", "fixed", 1, True, [],7),
                    AttackMove("Focus",attackDescC, 0, "madlas_tutorial2", "brains", "fixed", 2, True, [],8)
                    ]


        playerUnits[0].recoveryRate = 2



        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0])

    camera:
        zoom 2.3
        xcenter 0.65
        ycenter 0.5

    python:
        MD_State["feelerL"] = 1
        MD_State["feelerR"] = 1

        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 2

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter 0.3

    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter 0.7

    with Fade(0.1, 0.2, 2.0, color="#3bec27")

    play voice2 dmm_angryb
    Madlas "Don’t you know who I am?!"
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        matrixtransform RotateMatrix(0.0,180.0,180.0)
        pause 0.1
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.1
        matrixtransform RotateMatrix(0.0,0.0,0.0)

    show BG Studio Room Spooky

    show robyn:
        matrixcolor TintMatrix("#95ffba")

    show madlas:
        matrixcolor TintMatrix("#95ffba")

    play voice2 mm_imagoddamnurbanlegend
    Madlas "I’m a goddamn urban legend and I’m done wasting my eternity in this place!"
    python:
        MD_State["eyes"] = 2

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,360.0,0.0)

    show BG Studio Room Spooky
    play voice2 mm_dontideservetobefree
    Madlas "Don’t I deserve to be free!?"
    python:
        MD_State["eyes"] = 3
        MD_State["mouth"] = 4

        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 1

    show BG Studio Room Spooky
    show madlas:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 xcenter 0.4

    play voice2 mm_evenindeath
    Madlas "Somehow, even in death, I’m STILL working! All day, every night, all the time, forever. FOREVER."
    python:
        MD_State["eyes"] = -1
        MD_State["mouth"] = 3


        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2

    show BG Studio Room Spooky
    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 xcenter 0.45
    show robyn:
        pause 0.15
        ease 0.3 xcenter 0.75

    play voice2 mm_wellimdone
    Madlas "Well I’m done with liars, fakers, and those goddamn ghost hunters! None of them ever cared about the real me!"

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,0.0,0.0)

    show BG Studio Room Spookier
    play voice2 mm_iquitloud
    Madlas "I QUIT!"
    python:
        MD_State["mouth"] = 2
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    play voice2 mm_nomore
    Madlas "No more graveyard shifts, no more management, and no more fake fans!"
    python:
        MD_State["mouth"] = 1
    Narrator "The pair looks down at their hands and wiggles each finger."
    python:
        MD_State["mouth"] = 4
        MD_State["eyes"] = 3
    play voice2 mm_whathappenstofakefans
    Madlas "And do you know what happens to fake fans?"

    show madlas:
        ease 0.3 xcenter 0.4
    Narrator "The cryptid laughs, taking a wobbly step forward."
    python:
        MD_State["mouth"] = 2

        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 2
    show madlas:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0,180.0*3,0.0)

    play voice2 mm_igettheirsouls
    Madlas "I get their souls!"

    $MD_State["eyes"] = -1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1

    show BG Studio Room Spooky
    $Robyn_State["eyes"] = 2

    show madlas:
        pause 0.1
        matrixtransform RotateMatrix(0.0,180.0,0.0)

        parallel:
            ease 0.5 xcenter 0.9 matrixtransform RotateMatrix(0.0,180.0,45.0)
        parallel:
            ease 0.1 yoffset -30
            ease 0.4 yoffset 600
        pause 0.5
        ease 0.5 xcenter 0.75 matrixtransform RotateMatrix(0.0,0.0,0.0) yoffset 0

    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.5 xcenter 0.25 matrixtransform RotateMatrix(0.0,360.0,0.0)

    Narrator "Atlas staggers forward and swipes his talons through the air, narrowly missing you."

    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.1
        ease 0.3 xcenter 0.1

    Narrator "You roll off your chair onto the floor, and without realizing it, you sprint for the door in an effort to simply stay alive."

    $Robyn_State["mouth"] = 4
    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,0.0,0.0)

    Robyn "Atlas, what about our friday movie night?!"

    Madlas "Atlas can’t hear yooou!"

    Robyn "We were gonna watch the extended edition of that one fantasy trilogy., with director's commentary!"

    Narrator "The mothman goes rigid and his antennae flick forward."
    python:
        MD_State["eyes"] = 0
        MD_State["mouth"] = 4
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    Atlas "And subtitles?"

    $Robyn_State["mouth"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)

    Narrator "You fumble with the doorknob, trying to get it open."

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 xcenter 0.6 matrixtransform RotateMatrix(0,0,-20) yoffset 100
        ease 0.3 xcenter 0.65 matrixtransform RotateMatrix(0,0,0) yoffset 0

    Narrator "Atlas’ left leg jerks to one side, almost toppling the mothman over."
    $MD_State["eyes"] = -1
    show madlas:
        yoffset 0
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    play voice2 madlas_stopit
    Madlas "Stop it!"

    show madlas:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.4 xcenter 0.7 matrixtransform RotateMatrix(0,180,90) yoffset 500

    Narrator "He takes another step but trips over nothing, like two drivers fighting for the same steering wheel."

    show madlas:
        matrixtransform RotateMatrix(0,180,90)
        ease 0.6 xcenter 0.6 matrixtransform RotateMatrix(0,0,0) yoffset 0
        pause 0.2
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.2 xcenter 0.8
        pause 0.3
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.3 matrixtransform RotateMatrix(0,360,0)
    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    Madlas "Are you crazy?! We can't just  {glitch=40}{i}combine cryptids!{/i}{/glitch} \nThe Radio Man Moth sounds {glitch=60}fuckin'{/glitch} {glitch=2}stupid!{/glitch}"
    $MD_State["eyes"] = -1
    $Robyn_State['eyes'] = 3
    $Robyn_State['mouth'] = 4
    $MD_State["mouth"] = 0
    Robyn "{size=45}JAMIE HELP!{/size}"

    python:
        Jamie_Stats = Unit("{color=3AE9F6}Jamie{/color}",1,2,-1,0,-2,3,13)
        Jamie_Stats.Color = "#3AE9F6"
        Jamie_Stats.SetIcon("jamieIcon")

        attackDescA = "Cool! Cool?"
        attackDescB = "Anything's better than nothing."
        attackDescC = "Something cool might happen... maybe."
        attackDescD = "Sure, let the DPS be the healer as well. Good game design."

        JamieAttacks = [
                    AttackMove("Skull Cracker",attackDescA, 0, "madlas_tutorial2", "guts", "guts", 0, False, [],0),
                    AttackMove("Spirit Blaze",attackDescC, 0, "madlas_tutorial2", "occult", "fixed", 2, False, [],11),
                    AttackMove("Healing Wave",attackDescD, 0, "madlas_tutorial2", "occult", "fixed", 1, True, [],10)
                    ]

        Jamie_Stats.SetAttackMoves(JamieAttacks)
        playerUnits.append(Jamie_Stats)


        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0,1])

        playerUnits[1].recoveryRate = 2

        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 0
        Jamie_State["sweat"] = 1
        Jamie_State["wispEyes"] = 2
        Jamie_State["armR"] = 0
        Jamie_State["mouth"] = 4
        Robyn_State['eyes'] = 0
        Robyn_State['mouth'] = 5

    show robyn:
        pause 0.4
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.7 matrixtransform RotateMatrix(0.0,180*4,0.0) xcenter 0.12

    show jamie:
        matrixcolor TintMatrix("#95ffba")
        xcenter -0.5
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.6 xcenter 0.35

    Narrator "The jersey devil clambers into the room, confused."

    show jamie:
        ease 0.5 xcenter 0.45
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,360.0,0.0)
        pause 0.5
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)

    Narrator "They look around, only to watch the possessed mothman jerk and jitter towards the duo, muttering and clawing at his own feathers."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["alFace"] = 1
        Jamie_State["wispEyes"] = 3
        MD_State["mouth"] = 0

    voice jamie_surpriseb
    Jamie "...Did Atlas get taller?"

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 3
        Robyn_State["mouth"] = 4

    Robyn "That’s the first thing you noticed?!"

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["alFace"] = 0

        Jamie_State["eye"] = 7
        Jamie_State["fire"] = 0
        Jamie_State["armR"] = 2
        Jamie_State["r3Fire"] = 1
        Jamie_State["sweat"] = 0
        Jamie_State["wispEyes"] = 1

    Jamie "This is unforgivable."

    voice dmm_laughb
    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish

    python:
        Robyn_State["eyes"] = -1
        Robyn_State["mouth"] = 3
        MD_State["mouth"] = 1
        MD_State["eyes"] = 0
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    Madlas "Awwww,, not used to being the arm rest huh {glitch=8}shortie?{/glitch}"
    show madlas:
        xcenter 0.8
    python:
        Jamie_State["eye"] = 6
        Jamie_State["mouth"] = 2
        Jamie_State["steam"] = 1

        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 4

        MD_State["mouth"] = 0
        MD_State["eyes"] = -1

    Robyn "This isn't a contest!"

    Jamie "You're right,., feelers don't count."

    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 0
    $Jamie_State["steam"] = 0

    Jamie "I think now it's time to fight."

    python:
        Robyn_State["mouth"] = 5
        Robyn_State["brow"] = 2

        MD_State["mouth"] = 1

    Robyn "But that’ll hurt him!"

    $MD_State["mouth"] = 2

    voice dmm_yawn
    Madlas "Oh, so now you care! Gosh,., [PCname] I thought you were supposed to {glitch=8}protect me.{/glitch}"
    $Robyn_State["mouth"] = 4
    Robyn "H-huh?"

    Jamie "Lets make this quick."

    python:
        songText = "The Visitor"
        timeText = "2:30AM?"

    show BG Studio Room Spooky
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        matrixtransform RotateMatrix(0,0,180)
        pause 0.2
        matrixtransform RotateMatrix(0,180,0)
        matrixcolor HueMatrix(180)

    call makeCheckpoint from _call_makeCheckpoint_1
    show Flickering Black
    pause 0.65
    play music elkhorn_radio_intro_song noloop
    pause (4.3)

label madlas_tutorial:

    play music urgently_jammin_sir_meow_remix_intro
    $musicPlayer.playSong(song="urgently_jammin_sir_meow_remix_loop",queueSong=True)

    scene BG Studio Room Spookier:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)

    camera at camera_default
    camera:
        matrixcolor HueMatrix(0)
        matrixtransform RotateMatrix(0,0,0)

    $MD_State["mouth"] = 2

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        yoffset 700
        xcenter 0.5
        ycenter 0.6

        ease 1.09 yoffset 0
        block:
            yoffset -10
            parallel:
                ease 0.2725 yoffset 0
                pause 0.2725
                yoffset -10
                ease 0.2725 yoffset 0
                pause 0.2725
            parallel:
                pause 0.545
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,360,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,180,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,0,0)

            repeat

    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    Narrator "{glitch=30}Madlas{/glitch} laughs in your face!"

    $MD_State["eyes"] = 2
    Narrator "{glitch=20}Madlas{/glitch} opens up by chucking an oversized stereo speaker with supernatural force!"

    call dice_roll(playerUnits[1].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_13

    $xDmg = -(renpy.random.randint(6,10))
    show MMFight_Chair at MMFight_LeftProp_Exit
    show MMFight_Speaker at MMFight_RightProp_Exit

    if isRollSuccess:
        Narrator "Jamie barely steps out of the way!"
    else:
        $playerUnits[1].modifyHP(xDmg,0.0,"guts")
        $RefreshBarHP()
        Narrator "Jamie's clonked over the head, taking [sfxDmg] damage!"

    play voice2 dmm_laughc
    $ToggleBarState([1], 0)
    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry
    Madlas "Bwahaha, freebie! Are you two even trying?"
    show MMFight_Chair at MMFight_LeftProp_Exit
    show MMFight_Speaker at MMFight_RightProp_Exit

    Narrator "{glitch=20}Madlas{/glitch} furiously swipes his claws at the demon, who narrowly dodges the attack."
    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    Jamie "{b}{sc=2}[PCname], I NEED DIRECTION.{/sc}{/b}"

    Robyn "What do I even do?!"

    Jamie "Choose a skill in the top left corner! Click it!"

    python:
        #This hides the floating Quick Menu
        quick_menu = False
        quicker_menu_show = False

        #Thinking Music
        #renpy.music.set_volume(0.0, delay=0.5, channel=u'music')
        #renpy.music.set_volume(1.0, delay=0.5, channel=u'music2')

    hide screen quicker_menu

    python:
        CombatUnitPick()
        ui.interact()

    jump madlas_tutorial

label madlas_tutorial2:
    show robyn:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)
        xcenter 1.3
        yoffset 50
        matrixtransform RotateMatrix(0,0,0)

        ease 1.0 xcenter 1.0 matrixtransform RotateMatrix(0,0,-45)

    voice RobynSays("Generic","ConfusedA")
    if isRollSuccess:
        Robyn "Oookay that was a success? What does that mean?"
    else:
        Robyn "Yeesh, I guess that was a failure? Now what?"

    show MMFight_Chair:
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0*3)
        parallel:
            ease 0.75 yoffset -800

    show MMFight_Speaker:
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0*3)
        parallel:
            ease 0.75 yoffset -800

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.5
        yoffset 0
        ease 0.545 xcenter 0.2 matrixtransform RotateMatrix(0,180,0)
        block:
            yoffset -10
            ease 0.2725 yoffset 0
            pause 0.2725
            repeat

    show jamie:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)
        xcenter 1.3
        matrixtransform RotateMatrix(0,0,0)

        ease 1.0 xcenter 1.1 matrixtransform RotateMatrix(0,0,-45)
    $Jamie_State ["fire"] = 0
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 1

    Jamie "GREAT. Let me explain the basics. \n\n{size=-10}          Shit. Where do I even start? {/size}\n\nYou um."
    hide MMFight_Speaker
    hide MMFight_Chair
    $MD_State["eyes"] = 6

    python:
        displaymenu = True
        preferences.text_cps = 30

    Jamie "You see.{nw}"
    $preferences.text_cps = 32
    $Jamie_State ["eye"] = 3

    Jamie "Damage. Base Damage.{nw}"
    $preferences.text_cps = 33

    Jamie "{nw}"
    $preferences.text_cps = 34
    $Jamie_State ["eye"] = 0
    $Jamie_State ["mouth"] = 1
    $Jamie_State ["brow"] = 1

    Jamie "Then you um- Stimulate the Action economy-{nw}"
    $preferences.text_cps = 36
    $Jamie_State ["mouth"] = 2
    $Jamie_State ["brow"] = 3

    Jamie "And modifiers add numbers to your roll-{nw}"
    $preferences.text_cps = 37

    $Jamie_State ["mouth"] = 0

    Jamie "Stamina, Exhaustion, Meter..,{nw}"
    $preferences.text_cps = 41

    Jamie "My brain hurts-.,{nw}"
    $preferences.text_cps = 42

    Robyn "H-hey it's okay, take your time.,-{nw}"
    $preferences.text_cps = 60

    Jamie "Physical Special Split-{nw}"
    $preferences.text_cps = 50


    $Jamie_State ["hurt"] = 1
    $Jamie_State ["eye"] = 4


    Jamie "Is my nose bleeding?{nw}"
    $preferences.text_cps = 46

    Robyn "Deep breaths-.,{nw}"
    $preferences.text_cps = 30

    Jamie "I can't do this.,-{nw}"
    $preferences.text_cps = 48

    $Jamie_State ["steam"] = 1
    $Jamie_State ["eye"] = 6
    $Jamie_State ["brow"] = 0


    Jamie "If I hurt Atlas, he would cry., and I would never forgive myself., oh god, I really am the devil.,!{nw}"
    $preferences.text_cps = 60

    $Jamie_State ["armR"] = 3
    $Jamie_State ["hurt"] = 0
    $Jamie_State ["fire"] = 0
    $Jamie_State ["wispEyes"] = 4
    $Jamie_State ["steam"] = 0

    python:
        displaymenu = False
        preferences.text_cps = 30
    $Robyn_State["mouth"] = 4
    $Robyn_State["eyes"] = 0
    Robyn "{b}{sc=2}ATLAS HELP!{/sc}{/b}"

    $MD_State["mouth"] = 1
    $MD_State["eyes"] = 6
    $displaymenu = True

    Madlas "Not my problem."

    $MD_State["eyes"] = 0
    show madlas:
        linear 0.05 xcenter 0.200
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        pause 0.2
        repeat
    Madlas ".,.,{nw}"
    $MD_State["eyes"] = 6
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1
    $MD_State["mouth"] = 0
    show madlas:
        block:
            yoffset -10
            ease 0.2725 yoffset 0
            pause 0.2725
            repeat
    Madlas "{size=40}NO!{/size} \n\nI'M NOT EXPLAINING SHIT!"
    $MD_State["mouth"] = 3
    $MD_State["eyes"] = -1
    Madlas "{sc=1}Shut up and fight me!{/sc}"
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 4
    $Robyn_State["brow"] = 2
    Robyn "{bt=4}Pleeeeeease?{/bt}"

    Madlas ".,.,{nw}"
    $MD_State["mouth"] = 4
    $MD_State["eyes"] = 0

    show madlas:
        linear 0.05 xcenter 0.200
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        pause 0.2
        repeat
    Atlas "{size=40}Okay!{/size}"

    Narrator "It seems Atlas' innate desire to overshare is more powerful than any supernatural force."
    show madlas:
    $MD_State["eyes"] = 4
    $MD_State["feelerL"] = 0
    $MD_State["feelerR"] = 0
    $firstLoop = True
    jump madlas_tutorialQuestions

default tQcanAsk = [True,True,True,True]
label madlas_tutorialQuestions:
    $displaymenu = True
    show madlas at startledSquish: #.Startled Squish

    if firstLoop:
        Atlas "What do you need to know?{nw}"
        $firstLoop = False
        $tQcanAsk = [True,True,True,True]
    elif True in tQcanAsk:
        Atlas "Anything Else?{nw}"

    menu:
        extend ""

        "The Stats and what they mean" if tQcanAsk[0]:
            $displaymenu = False
            $tQcanAsk[0] = False
            $MD_State["eyes"] = 5
            Atlas "Okay so, there are six stats: [kwBrawn], [kwBrains], [kwGuts], [kwHustle], [kwCharm], and [kwOccult]!"

            Atlas "[kwBrawn] is your physical strength. It’s typically used as a bonus and modifier for physical attacking moves."

            Atlas "[kwBrains] is a sum of your mental strength and general insight. It’s the main stat used for out of combat investigation, plus the defensive stat against supernatural damage."

            Atlas "[kwGuts] is your physical constitution and fortitude. It’s used for things like resisting poison, an illness, or physical damage."

            Atlas "[kwHustle] is your speed and hand-eye coordination. It’s used as a modifier to avoid many attacks, as well as determine aim and effectiveness of split-second actions."

            Atlas "[kwCharm] is your charisma and likability. It’s mostly used for convincing people of things and swaying hearts."

            Atlas "[kwOccult] is your attunement to the supernatural. Any magics or unnatural abilities outside the realm of physical prowess use Occult."

            Atlas "These stats are the modifiers used in rolls, as well as damage calculation for whatever move you're trying to use. There are stats also exclusive to combat encounters such as [kwPowerMod], [kwPDefense], and [kwSDefense]."

            Atlas "[kwPowerMod] refers to an additional bonus to attacking power. Whenever damage calculation is involved, [kwPowerMod] is a flat bonus added to damage."

            Atlas "[kwPDefense]/[kwSDefense] are similar to power except it’s a flat bonus to defense against attacks."

            Atlas "Damage is split into two types, physical and supernatural, physical attacks being resisted by Guts and Supernatural attacks being resisted by Brains."

            $MD_State["eyes"] = 0
            jump madlas_tutorialQuestions

        "Move descriptions & Effects" if tQcanAsk[1]:
            $displaymenu = False
            $tQcanAsk[1] = False
            Atlas "Oh this is easy!"

            Atlas "So moves are typically laid out as follows:"
            $MD_State["eyes"] = 0
            Atlas "{size=-5}[kwSuccess] This happens on a success.\n\n[kwFailure] This Happens on a failure.\n\nChecks {color=#83ed6e}(Your Modifier){/color} vs {color=#7aff44}(Enemy Modifier or Fixed Difficulty(X)){/color}\nCost: X Stamina{/size}"

            Atlas "When a skill does damage, in order to figure out whether it's resisted by either [kwPDefense] or [kwSDefense], just think of what it's doing."
            $MD_State["eyes"] = 5
            Atlas "If it's punching, it's [kwPDefense], but if you're slinging a fireball, it's resisted by [kwSDefense]."
            jump madlas_tutorialQuestions

        "Stamina, Exhaustion & Recovery" if tQcanAsk[2]:
            $displaymenu = False
            $tQcanAsk[2] = False
            Atlas "All moves have a listed stamina cost ranging from 0-5, and all party members have stamina ranging from 0-4."

            Atlas "Whenever you use a move, you lose the listed stamina cost, but every party member not involved gains +1 stamina. Some moves use multiple party members, so keep that in mind."

            Atlas "You can use any move regardless of how much stamina you have versus its cost, but if you go into the negatives, you become exhausted. Exhausted party members cannot act for a set amount of turns until they become unexhausted."
            jump madlas_tutorialQuestions

        "Enemy Attacks, MTA, & Difficulty" if tQcanAsk[3]:
            $displaymenu = False
            $tQcanAsk[3] = False
            $MD_State["eyes"] = 5
            Madlas "[kwMTA] {size=-9}(Moves Until Attack){/size} is simple! It’s the number of turns you can take until the foe in question can act."

            Atlas "It’s a fun little count down going down to mark when we can kick your butt!"

            Atlas "Some enemies can also attack multiple times when their counter reaches 0, so it’s safe to assume that foes fighting by themselves will go more than once in any given encounter."

            Atlas "One important thing to note is how KOed party members affect delay. If a party member is KOed, any healing can bring them up from 0 health. There’s no revives after all!"

            Atlas "To balance this out, whenever an enemy’s turn ends and any party members are KOed, their maximum delay is lowered by each downed party member."

            Madlas "For example, if you have a team of 4 and 2 are downed. The enemy acts and has a maximum delay of 5. Their delay would be set to 3, because 2 party members being downed sped up the process!"
            $MD_State["eyes"] = 0
            jump madlas_tutorialQuestions

        "I've got it!" if True in tQcanAsk:
            Atlas "Great!"
            pass
            $MD_State["eyes"] = 4
            $MD_State["mouth"] = 4
    $MD_State["eyes"] = 4
    Atlas "I think that's everything!"
    $MD_State["eyes"] = 1

    Atlas "Hey,, Jamie? It's okay."

    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1
    voice dmm_laughb
    Madlas "Get his ass."

    show jamie:
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        pause 0.3
        repeat

    voice jamie_growlb
    Jamie "..."
    show jamie:
        ease 0.08 yoffset 5
        ease 0.08 yoffset -5
        ease 0.08 yoffset 5
        ease 0.08 yoffset -5
        ease 0.04 yoffset 0
        pause 0.2
        repeat

    $Jamie_State["eye"] = 7
    $Jamie_State["fire"] = 1
    $Jamie_State["armR"] = 2
    $Jamie_State["r3Fire"] = 1
    $Jamie_State["wispEyes"] = 1
    $Jamie_State["mouth"] = 1

    Narrator "Jamie's totally fired up, the spark of determination gleaming in their wild eyes. It inspires you too,, maybe things will work out. Maybe you can do this."

    show robyn:
        ease 0.5 xcenter 1.5
    show jamie:
        ease 0.6 xcenter 1.5
    $Jamie_State["r3Fire"] = 0
    Robyn "Let's save Atlas!"

    $MD_State["eyes"] = 2
    $MD_State["mouth"] = 2
    $MD_State["feelerL"] = 0
    $MD_State["feelerR"] = 0
    if gameVersion == 3:
        $displaymenu = True
        Narrator "Skip Fight?{nw}"
        menu:
            extend ""
            "Yes":
                $displaymenu = False
                jump buildup_to_MM_Fight
            "No":
                $displaymenu = False
    call FIGHT_00_MADLAS from _call_FIGHT_00_MADLAS

    jump buildup_to_MM_Fight

label buildup_to_MM_Fight:
    show madlas:
        ease 0.545 xcenter 0.5 matrixtransform RotateMatrix(0,0,0)
    $MD_State["mouth"] = 0
    $MD_State["eyes"] = -1
    voice dmm_angryb
    Madlas "You losers really thought you could defeat me? \n\n{sc=3}WHAT A JOKE!{/sc}"
    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish
    $MD_State["mouth"] = 1
    $MD_State["eyes"] = 0
    $MD_State["feelerR"] = 1
    $MD_State["feelerL"] = 1
    Madlas "You're lookin' at the next mothman, baby! Y-yeah! Not {b}a{/b} mothman,, but \n{b}THE MOTHMAN{/b}!"
    show madlas:
        parallel:
            hoppies_flipped(xIntensity=2)
        parallel:
            startledSquish
    Madlas "No more {glitch=30}patronizing{/glitch} stares,, or shifty glances! \n\nJust sheer, {glitch=30}crystaline terror!{/glitch}"

    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish
    Madlas "I'm a legend!"
    show madlas:
        ease 0.15 yoffset -30
        ease 0.15 yoffset 0

    Madlas "I'm a demon!"

    $MD_State["mouth"] = 5
    $MD_State["eyes"] = 2
    show madlas:
        linear 0.05 xcenter 0.500
        linear 0.05 xcenter 0.506
        linear 0.05 xcenter 0.5
        linear 0.05 xcenter 0.504
        linear 0.05 xcenter 0.502
        linear 0.05 xcenter 0.5
        pause 0.2
        repeat
    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1

    Madlas "{sc=6}I'm a—{/sc}"
    python:
        musicNote = 3
        songText = "Awkward Silence"
    play sfx emote_frustration
    $musicPlayer.playSong()
    show madlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(1.0, 0.0, 2.0)
        zoom 1
        alpha 1
    narrator "{nw}"
    hide madlas

    $Atlas_State["eye"] = 7
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Atlas_State["feelers"] = 1
    show atlas:
        xcenter 0.5

    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(1.0, 0.0, 2.0)
        zoom 1
        alpha 1

    Narrator "Atlas pops back to normal."

    show atlas:
        linear 0.05 xcenter 0.500
        linear 0.05 xcenter 0.504
        linear 0.05 xcenter 0.5
        linear 0.05 xcenter 0.503
        linear 0.05 xcenter 0.502
        linear 0.05 xcenter 0.5

    $Atlas_State["eye"] = 5
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    $Atlas_State["feelers"] = 0

    Atlas "I'm a little light headed."
    $Atlas_State["eye"] = 13

    voice taro_angryb
    Taro "{sc=1}Know your place!{/sc}"
    $BTaro_State['mouth'] = 2
    $BTaro_State['eye'] = 1
    camera:
        pause 0.23
        xoffset -15
        ease 0.06 xoffset 15
        ease 0.06 xoffset -13
        ease 0.06 xoffset 11
        ease 0.06 xoffset -9
        ease 0.06 xoffset 7
        ease 0.06 xoffset -5
        ease 0.06 xoffset 3

        ease 0.03 xoffset 0

    python:
        Taro_Stats = Unit("{color=#C064FF}Taro{/color}",2,-1,1,2,0,-1,14)
        Taro_Stats.Color = "#C064FF"
        Taro_Stats.SetIcon("taroIcon")

        attackDescA = "[kwSuccess] Deals medium damage to Target. When Taro is at 5 [kwHealth] or lower, deals heavy damage.\n\n[kwFailure] Deals reduced damage to Target\n\nChecks [kwBrawn] vs [kwHustleD]\nCost: 2 Stamina"

        attackDescB = "[kwSuccess] Taro intercepts all incoming attacks, and slightly raises her [kwDefenseMod]. Taro maintains stat changes until she uses a different move.\n\n[kwFailure] Move works, but slightly lowers Taro's [kwDefenseMod]. Also raises her [kwPowerMod].\n\nChecks [kwGutsD] vs Fixed(7)"

        attackDescD = "[kwSuccess] Lowers Target [kwPowerMod], and slightly lowers their [kwDifficultyModD].\n\n[kwFailure] Raises Target [kwPowerMod]\n\nChecks [kwCharm] vs [kwBrainsD]\nCost: 3 Stamina"

        TaroAttacks = [
                    AttackMove("Pounce",attackDescA, -2, "FIGHT_01_MM_TARO_0", "brawn", "hustle", 0, False, [],0),
                    AttackMove("Tuna Defender",attackDescB, 0, "FIGHT_01_MM_TARO_1", "guts", "fixed", 2, True, [],7),
                    AttackMove("Jeer",attackDescD, -3, "FIGHT_01_MM_TARO_3", "charm", "brains", 0, False, [],10)
                    ]
        Taro_Stats.SetAttackMoves(TaroAttacks)
        playerUnits.append(Taro_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0,1,2])

    $audio.delayedThunk = ["<silence .23>", "audio/SFX Battle/Hurt_D.ogg"]
    show tarobig:
        xcenter -0.5
        ease 0.3 xcenter 0.5
    $Atlas_State["eye"] = 3
    show atlas:
        pause 0.23
        matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 1.0 xcenter 1.5
        parallel:
            ease 0.4 yoffset -300
            ease 0.4 yoffset 600
        parallel:
            ease 1.3 matrixtransform RotateMatrix(0,0,360*3)

    play sfx delayedThunk

    Narrator "The door to the studio buckles, splitting open as monstrous Taro bursts into the room. With a triumphant meow, she knocks Atlas to the ground."
    hide atlas
    $BTaro_State['mouth'] = 1
    $BTaro_State['eye'] = 2
    show tarobig:
        ease 10 xcenter -0.5
    Narrator "Sprawled out on the floor all battered and dazed, Atlas hacks up a mouthful of toxic waste."

    Robyn "{sc=2}Taro what the {b}hell{/b}!{/sc}., Atlas are you okay?!"

    Narrator "Atlas gives you a weak thumbs up."

    python:
        Atlas_Stats = Unit("{color=#ED2A82}Atlas{/color}",-1,2,2,-1,1,0,13)
        Atlas_Stats.Color = "#ED2A82"
        Atlas_Stats.SetIcon("atlasIcon")

        attackDescA = "[kwSuccess] Delays Target attack.\n\n[kwFailure] Move works but everyone's stamina is set to 0 (excluding Atlas).\n\nChecks [kwBrainsD] vs Fixed(10)\nCost: 3 Stamina"

        attackDescB = "[kwSuccess] Deals heavy damage, and lowers Target [kwBrainsD]. Atlas takes 30% recoil.\n\n[kwFailure] Move works but Atlas' [kwBrainsD] is lowered, and Atlas Takes 60% recoil.\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 4 Stamina"

        attackDescC = "[kwSuccess] Jamie gains +1 stamina, and both their [kwOccultD] and [kwBrawn] are raised. \n\n[kwFailure] Jamie's [kwOccultD] and [kwBrawn] are raised slightly.\n\nChecks [kwCharm] vs Fixed(10)\nCost: 1 Stamina"


        AtlasAttacks = [
                    AttackMove("Lore Dump",attackDescA, -3, "FIGHT_01_MM_ATLAS_0", "brains", "fixed", 2, False, [],10),
                    AttackMove("Kinesis",attackDescB, -4, "FIGHT_01_MM_ATLAS_1", "occult", "brains", 0, False, [],7),
                    AttackMove("Pump Up",attackDescC, -2, "FIGHT_01_MM_ATLAS_2", "charm", "fixed", 2, True, [],10)
                    ]

        Atlas_Stats.SetAttackMoves(AtlasAttacks)
        Atlas_Stats.cHP = 3
        playerUnits.append(Atlas_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0,1,2,3])

    Atlas "Yeah., yeah, I'm fine."
    Atlas "Sorry for scaring you."
    Narrator "Helping Atlas to his feet, you keep an arm around him as you nervously glance around. Where's Madhouse?"

    hide tarobig

    Jamie "Mike you coward!"

    Narrator "Grasping at the air, the jersey devil exhales a gout of blue flame as they throw punches at nothing."

    Taro "Prrrh, do you honestly think that'll work?"
    $musicPlayer.playSong(song="not_so_spooky_song",fadeIn=1)

    Narrator "Throwing another punch, Jamie winces as it actually strikes,, Madhouse's open palm."
    voice mm_booa
    Madhouse "Coward?"
    voice mm_laughe
    Narrator "The ghost blinks back into view with a giddy laugh and a smile."

    voice jamie_surpriseb
    Jamie "-!{nw}"

    Narrator "Jamie yanks their hand away but it's too late, Madhouse's coiled his fist around their arm. "

    Madhouse "Didn't I tell you? I—"

    Narrator "Jamie doesn't care. They swing their head back and slam their skull against the ghost's face, leaving Madhouse sputtering."

    Madhouse "I don't deal with—"

    Narrator "Throwing their other fist, Jamie punches their arm through Madhouse's chest."

    Madhouse "{sc=1}Let me finish!{/sc}"

    Narrator "They're both stuck. Jamie can't move their arms."

    Narrator "Jamie bites and kicks but to no avail,, they're tangled in a tangible, intangible mess."
    voice mm_laughawkward
    Madhouse "Way to go and ruin the moment, bonehead."

    Narrator "Madhouse tightens his grip around the devil."

    Jamie "., You wouldn't dare."

    $musicPlayer.playSong(song="drink_it_song",fadeOut=1,fadeIn=3)
    voice mm_laugha
    Madhouse "Whaaaat? I've never possessed a demon before—"

    Jamie "Your soul would be {i}incinerated!{/i}"

    voice mm_yawn
    Madhouse "So what?"

    Madhouse "I'll manage,, {bt=2}either way it's a win-win!{/bt}"


    camera:
        pause 0.4
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.05 xoffset 0


    show demon_madhouse at MMD_Entry_Pos

    Narrator "Madhouse's jaw suddenly unhinges, a curled horn jutting out the side of his head. He claps a hand over his face and stifles a cry, his ghastly form flickering in the iridescent lights."

    Jamie "I told you it wouldn't work!"

    Narrator "Jamie acts fast, taking this moment to finally tear their hand out of Madhouse's chest while he writhes, shaking ectoplasm off their claws."
    if gameVersion == 3:
        $displaymenu = True
        Narrator "Skip Fight?{nw}"
        menu:
            extend ""
            "Yes":
                $displaymenu = False
                jump MM_fightAftermath
            "No":
                $displaymenu = False

    call FIGHT_01_MADHOUSE from _call_FIGHT_01_MADHOUSE_1
    jump MM_fightAftermath




#GO TO MMFight.RPY #1 FOR THE FIGHT
