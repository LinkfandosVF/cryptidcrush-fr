transform radio_camera:
    ease 5.0 ycenter 0.82 xcenter 0.73 zoom 1.49

transform quick_radio_camera:
    ease 1.0 ycenter 0.82 xcenter 0.73 zoom 1.49

transform radio_atlas_cameraA:
    ease 0.5 zoom 2.3 ycenter 0.97 xcenter 0.75

transform radio_madhouse_cameraA:
    ease 0.5 xcenter 0.95 zoom 2.1 ycenter 0.95

label RadioShow:
    show Flickering Black
    pause 0.65
    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    pause (4.3)
    scene black
    $musicPlayer.playSong(song="elkhorn_radio_song",fadeIn=1)

    python:
        Robyn_State["brow"] = 0
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 9
        MM_State["armR"] = 0
        MM_State["armL"] = 0
        MM_State["hair"] = 0
        MM_State["outfit"] = 0

        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 0

        Taro_State["mouth"] = 0
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0

        Jamie_State["eye"] = 0
        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["armL"] = 0
        Jamie_State["armR"] = 0
        Jamie_State["pants"] = True
        Jamie_State["rings"] = True,
        Jamie_State["alFace"] = False
        Jamie_State["blush"] = False
        Jamie_State["sweat"] = False
        Jamie_State["fire"] = False
        Jamie_State["r3Fire"] = False
        Jamie_State["steam"] = False
        Jamie_State["hurt"] = False
        Jamie_State["wispEyes"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 7
        MM_State["armR"] = 0
        MM_State["armL"] = 0

        Atlas_State["armL"] = 1


    Madhouse "Evening, ghosts and ghouls! We’re back LIVE at Elkhorn Radio, located just off Route 101 For those just tuning in, I’m your ghastly host, Madhouse Mike, and welcome to the witching hour!"

    show madhouse:
        xcenter 0.8
        yoffset 140
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Madhouse "We’ve gotta special treat tonight, guests from the realm of the living! Why don’t you introduce yourselves?"

    python:
        MM_State["eyes"] = 4
        MM_State["mouth"] = 0

    show madhouse:
        matrixcolor BrightnessMatrix(0)

    Narrator "Mike makes a nod, cueing the two in."
    python:
        Atlas_State["feelers"] = 1
        Atlas_State["eye"] = 9
        Atlas_State["eyeFrame"] = 0

    show atlas:
        xcenter 0.5
        yoffset 130
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Atlas "Lex if you’re listening, you owe me twenty bucks."
    show atlas:
        matrixcolor BrightnessMatrix(0)
    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

        Robyn_State["brow"] = 3
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 1

    show robyn behind atlas:
        xcenter 0.35
        yoffset 110
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Robyn "{size=-6}Dude! Now's not the time!{/size}"
    scene BG Studio Room Dark
    $Robyn_State["mouth"] = 1

    show madhouse:
        xcenter 0.8
        yoffset 140

    show atlas:
        xcenter 0.5
        yoffset 130
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn behind atlas:
        xcenter 0.35
        yoffset 110


    camera at radio_camera
    Narrator "You whisper to the mothman, shooting him a glare."
    python:
        Robyn_State["mouth"] = 0
        Robyn_State["brow"] = 0
    show BG Studio Room

    Robyn "I’m [PCname] and this is Atlas. We're both big fans!"

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 9

    voice mm_woah
    Madhouse "Wow, you’ve got guts moving to a town full of cryptids."
    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 4
        Atlas_State["eye"] = 0

    Robyn "I guess so?"

    $Atlas_State["eye"] = 13
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5

    Madhouse "Were ya scared?"

    $Robyn_State["mouth"] = 5
    $Atlas_State["eye"] = 0

    Robyn "A little,, but I know I'll be okay with my cosmic guardian around."

    $Robyn_State["mouth"] = 0
    $Robyn_State["eyes"] = 2
    $MM_State["mouth"] = 10
    Madhouse "A what?"
    $Robyn_State["brow"] = 2
    Robyn "My ghost cat Taro! She's meant to protect me, but ah... She tends to do her own thing."

    $Atlas_State["eye"] = 0
    $Atlas_State["eyeFrame"] = 5
    $Atlas_State["armL"] = 2
    $MM_State["mouth"] = 0

    Atlas "Where is Taro anyway?"

    $MM_State["mouth"] = 9

    Madhouse "Sounds like you've got a real affinity for spirits."

    $Robyn_State["eyes"] = 4
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["armL"] = 0
    $Atlas_State["eye"] = 1

    Atlas "And knack for trouble."

    $Robyn_State["mouth"] = 6
    $Robyn_State["brow"] = 1
    $Robyn_State["eyes"] = 3
    $Atlas_State["eye"] = 16

    Narrator "You elbow Atlas and the two of you exchange cheeky smiles."


    python:
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

        MM_State["eyes"] = 5
        MM_State["mouth"] = 0

        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0

    Madhouse "Then I suppose {b}trouble{/b} here's the one and only Mothman. Prophet of the silver bridge, bringer of disaster! So, what’s it like being an omen of destruction?"
    camera at radio_atlas_cameraA

    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 5
        Atlas_State["feelers"] = 0

    Atlas "No no, that’d be... my dad. I’m just {i}a{/i} mothman, not {i}the{/i} Mothman. I can’t really control my visions, either."

    python:
        Atlas_State["eye"] = 6
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 1

    Atlas "I’m just here helping out a cursed friendo."
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

    Robyn "You can see the future?!"
    $Atlas_State["eye"] = 0

    camera at radio_madhouse_cameraA

    $MM_State["mouth"] = 7
    $MM_State["eyes"] = 0


    Madhouse "Hell yeah! Give us a prophecy mothman!"

    $Atlas_State["eye"] = 14
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0

    Narrator "Atlas looks a little frazzled, his eyes darting which way."
    $Atlas_State["eye"] = 12
    $Atlas_State["eyeFrame"] = 1

    Atlas "Like on the spot? \n\nI-I wanted to talk about [PCname]'s {i}curse!{/i}"

    Robyn "{size=-6}It's okay, just go with the flow.{/size}"

    $MM_State["mouth"] = 11
    $Robyn_State["brow"] = 2
    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 0
    $MM_State["armR"] = 1
    $MM_State["armL"] = 1

    Madhouse "What's in my future?"

    camera at radio_atlas_cameraA

    Atlas "Okay, sure! Haha, yeah, {i}yeah{/i} I can try."

    $Atlas_State["eye"] = 20
    $Atlas_State["feelers"] = 1
    $Robyn_State["mouth"] = 1
    $Robyn_State["eyes"] = 0

    Narrator "Closing his eyes, the moth folds his wings and tilts his head to one side, as if he's trying to listen in on something."

    Atlas "...{nw}"
    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        zoom 1
        alpha 1
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

        musicPlayer.playSong()


    Atlas "{size=35}NOPE, NEVERMIND!{/size} \n\n I can't do this."

    Madhouse "Why not?"

    $Atlas_State["feelers"] = 1
    $Atlas_State["eye"] = 16
    voice atlas_nervouslaugh

    Atlas "I guess ghost's are just too dang hard to read."

    $Atlas_State["eye"] = 7
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 2
    $MM_State["mouth"] = 0

    $musicPlayer.playSong(song="elkhorn_radio_song",fadeIn=1)

    Atlas "Can we move onto the next bit?"

    camera at radio_madhouse_cameraA
    voice mm_yawn
    Madhouse "Seriously?"

    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 5
        Atlas_State["feelers"] = 0
        MM_State["mouth"] = 2
    Atlas "Sorry man."
    $MM_State["mouth"] = 3
    Madhouse "Eh, it was worth a shot."

    camera at radio_atlas_cameraA

    Narrator "You feel a little underwhelmed."

    $Robyn_State["mouth"] = 6
    $Robyn_State["brow"] = 1
    $Robyn_State["eyes"] = 3

    Robyn "What about my future?"

    $Atlas_State["eye"] = 0

    pause 0.4
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 16
    $Atlas_State["feelers"] = 1
    Atlas "[PCname], you're gonna oversleep and wake up with a headache."

    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 3
    $Robyn_State["brow"] = 2
    voice RobynSays("Generic","HmphB")
    Robyn "Aw man."

    Narrator "You're definitely underwhelmed."

    Madhouse "Any tips on how to set these things into motion?"

    $Atlas_State["eye"] = 18
    $MM_State["mouth"] = 0
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0

    Atlas "How am I supposed to know? \n\nFate is stupid and impossible to figure out."

    Madhouse "Wow,, real inspiring stuff little dude."

    camera at quick_radio_camera
    Madhouse "Mike waves his hand around, shaking his head with a smile."

    $MM_State["eyes"] = 0
    Madhouse "I say we move onto our next segment!"

    $MM_State["mouth"] = 9

    Madhouse "How about some episodic callbacks? It should be a total breeze for such {b}BIG FANS{/b}!"
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 4

        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 5

    Robyn "Yep! I’m a real mega fan."

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 0

    Madhouse "Episode fifteen, which undead horror did we interview on the show?"
    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0

        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["eyeFrame"] = 0

    voice RobynSays("Generic","ConfusedA")
    Robyn "Ah..."
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5

    $displaymenu = True
    Narrator "You sit there quietly, shuffling your  feet and tapping the counter, unsure of what to say.{nw}"

    menu:
        extend ""

        "A ghost cat":
            pass
        "Some sort of spooky spaghetti":
            pass
        "My mom?":
            pass
    python:
        displaymenu = False

        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0

        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1

    show atlas:
        yoffset 130
        ease 0.15 yoffset 90
        ease 0.15 yoffset 130
        pause 0.1
        ease 0.15 yoffset 90
        ease 0.15 yoffset 130

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 8

    Atlas "Bloody Bones!"

    Narrator "The mothman throws a wing up into the air, exclaiming the answer."
    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1

        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 6
        Atlas_State["sparkle"] = 0

    show robyn:
        ease 3.0 yoffset 140

    camera at radio_atlas_cameraA
    Narrator "Folding your arms across your chest, you sink into their chair with a scowl."

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 7

    Madhouse "Perfect!"

    #Narrator "Mike moves things right along."

    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 9

    Madhouse "This is a {bt=3}spicy{/bt} one. In episode twenty six, who was… Bigfoot’s secret lover?"
    python:
        Atlas_State["eye"] = 3
        Atlas_State["feelers"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["eyeFrame"] = 1

    show atlas:
        xcenter 0.5
        linear 0.1 xcenter 0.49
        linear 0.1 xcenter 0.5
        repeat

    #Narrator "Atlas looks like he’s about to spontaneously combust."
    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4

    $displaymenu = True
    Robyn "It’s on the tip of my tongue!{nw}"

    menu:
        extend ""

        "The frogman?":
            pass
        "Ummm... The Squonk.":
            pass
        "Bigfoot number two.":
            pass

    python:
        displaymenu = False
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0

        Atlas_State["eye"] = 6
        Atlas_State["eyeFrame"] = 0
        Atlas_State["sparkle"] = 0

    show atlas:
        xcenter 0.5

    #voice atlas_booyah
    Atlas "The Goatman!"

    $MM_State["eyes"] = 2
    $MM_State["mouth"] = 9

    Madhouse "Not bad! Though, you really ought to give your friend here a chance."

    Narrator "Mike snickers."
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2

    Robyn "I’m a little unprepared here."
    python:
        Atlas_State["eye"] = 1
        Atlas_State["sparkle"] = 0
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

    Atlas "Right. Gah, I’m getting ahead of myself."

    python:
        displaymenu = True

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0

    Madhouse "In season one’s finale, what news broke that night?{nw}"

    menu:
        extend ""

        "I moved to Longhope!":
            pass
        "Bigfoot and Goatman got married?":
            pass
        "I’m pretty sure you died.":
            pass

    python:
        displaymenu = False

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

    Narrator "Atlas gently taps you on the foot with a talon and whispers to you before you can answer."
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0


    Atlas "\n{size=-5}There was an alien abduction.{/size}\n"

    python:
        Robyn_State["mouth"] = 6
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0

    Robyn "It was aliens!"

    camera at radio_madhouse_cameraA
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 4
    Madhouse "Oh yeah? Just how many episodes of my show aired on the radio?"

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0

        Atlas_State["feelers"] = 1

    camera at radio_atlas_cameraA
    Narrator "Atlas whispers to you in a hushed voice."

    Atlas "\n{size=-5}Thirty two.{/size}\n"

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0

    Robyn "Th-thirty two!"

    camera at radio_madhouse_cameraA
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 3
    Madhouse "Correct."

    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 1
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 16
        MM_State["mouth"] = 1

    Narrator "Madhouse's smile falters."

    python:
        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 5
        MM_State["armL"] = 1
        MM_State["armR"] = 1

    Madhouse "Next question, what did I have for breakfast?"


    camera at quick_radio_camera
    Narrator "You look to Atlas for an answer, but he doesn’t respond."

    Atlas "I...{nw}"

    python:
        Atlas_State["feelers"] = 1
        Atlas_State["eyeFrame"] = 3
        Atlas_State["eye"] = 2
    extend "\n\nI don’t know."

    show BG Studio Room2
    show atlas:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    show robyn:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    show madhouse:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 6

    Narrator "The ghost is absolutely thrilled by Atlas’ answer."

    voice mm_laugha
    Madhouse "Any {i}real{/i} listener would know, I skip breakfast!"
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 3

    Robyn "That’s totally unfair!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    $Robyn_State["mouth"] = 5
    Madhouse "Oh yeah? Hey, Atlas, who sponsored season two’s recap episode?"

    Narrator "Atlas shrugs."

    Atlas "I skip the ad breaks."

    python:
        displaymenu = True

        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "How do you skip ads on a radio—?{nw}"

    python:
        displaymenu = False

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

    $MM_State["eyes"] = 10
    $MM_State["mouth"] = 1
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    show madhouse at hoppies:
        yoffset 140
    Madhouse "{size=45}TOXIC WASTE ENERGY!{/size} \nIT WAS TOXIC WASTE EN—"

    $MM_State["armL"] = 2
    $MM_State["armR"] = 2
    $MM_State["eyes"] = 1
    $MM_State["mouth"] = 5

    show madhouse:
        yoffset 140
        parallel:
            flipCharDelayed(0.7,0.5)
    Madhouse "{sc=2}But good try!{/sc}"

    $MM_State["armR"] = 1
    $MM_State["armL"] = 1
    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 0

    Madhouse "We’re cutting to commercial."

    $musicPlayer.playSong()
    play music elkhorn_radio_outro_song noloop

    $Atlas_State["eye"] = 1
    $MM_State["mouth"] = 1

    #Narrator "Mike’s smile falters as he flicks off the microphones and whirls around."

    #Robyn "I-I thought we were having a good time!"

    $Atlas_State["eye"] = 3

    $MM_State["eyes"] = 0
    $MM_State["armL"] = 3
    $MM_State["armR"] = 1
    $MM_State["mouth"] = 9

    show madhouse:
        yoffset 140
        parallel:
            unflipCharDelayed(0.7,0.5)

    Narrator "He points at Atlas."

    camera at radio_madhouse_cameraA
    Madhouse "{sc=5}{b}YOU.{/b}{/sc}"

    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 16

    Atlas "Me?"

    Madhouse "You’ll be helping me out here."

    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    $musicPlayer.playSong(song="elkhorn_radio_song",queueSong=True)

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5
    $MM_State["armL"] = 1

    #Narrator "The ghost growls and clicks on the microphones, snapping back into his chipper host persona."

    python:
        MM_Stats = Unit("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}",1,1,2,0,1,1,40)
        MM_Stats.baseDiff = 6
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(2) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01_MM_MM_ATTACK")
        MM_Stats.SetMTA(3)

        enemyUnits = []
        enemyUnits.append(MM_Stats)

        Atlas_Stats = Unit("{color=#ED2A82}Atlas{/color}",-1,2,2,-1,1,0,13)
        Atlas_Stats.Color = "#ED2A82"
        Atlas_Stats.SetIcon("atlasIcon")

        #Puts the party into the Bar
        playerUnits = []
        playerUnits.append(Atlas_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0])

    python:
        Atlas_State["eye"] = 4
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 1


    Atlas "Wow, okay!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 7

    Madhouse "Now you all know that personally I love Toxic Waste. In fact I drank so much that my skin turned {color=#3bec27}green{/color}, HAH!"


    Madhouse "But, I can recognize my own biases so don’t just take my word for it! Atlas, pal, why don’t you try out their newest flavor, Beyond The Grave?"
    camera at radio_atlas_cameraA
    $musicPlayer.playSong(song="drink_it_song",fadeOut=1,fadeIn=3)
    $Atlas_State["armR"] = 1
    show atlas:
        xcenter 0.5
        yoffset 130
    show ToxicWasteCG:
        xcenter 0.51
        yoffset 340
        matrixcolor TintMatrix("#c0fac8")
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    show atlasArmR2:
        ycenter 0.79
        zoom 0.23
        xcenter 0.5
        yoffset 130
        matrixcolor TintMatrix("#c0fac8")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Narrator "A can of Toxic Waste suddenly appears in the Mothman’s grasp as though he had always been holding it."

    Narrator "Atlas grips the can in his claws and cracks it open, letting the {color=#3bec27}green{/color} foam trail down his feathers."

    python:
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 7
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 0

    voice atlas_nervouslaugh
    Atlas "Yeah, sure, but, didn’t this lukewarm soda literally kill you?"

    $Atlas_State["eye"] = 1
    Atlas "You'll gimme an autograph, right?"

    python:
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1

    Madhouse "{sc=5}{b}JUSTDRINKIT.{/b}{/sc}"

    play sfx blip_2b
    pause 0.6

    camera at radio_atlas_cameraA
    Narrator "He takes a sip."

    python:
        displaymenu = True
        preferences.text_cps = 60

        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 1

    Atlas "GWUAH—{nw}"
    python:
        playerUnits[0].modifyHP(-100,1.0,"guts")
        preferences.text_cps = 30
        displaymenu = False
    hide atlasArmR2
    show atlas:
        ease 0.4 yoffset 700

    show ToxicWasteCG:
        yoffset 340
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            ease 0.4 yoffset 0
            ease 0.7 yoffset 700
        parallel:
            ease 1.2 matrixtransform RotateMatrix(0.0, 0.0, 360.0*2)
    camera at quick_radio_camera
    $RefreshBarHP()
    Narrator "The moth drops like a rock."
    python:
        MM_State["eyes"] = 6
        MM_State["mouth"] = 9

        Atlas_Stats.iconState = 0

    camera at quick_radio_camera


    Madhouse "So what do you think? I’m sure we’re all dying to know."
    hide ToxicWasteCG

    python:
        Atlas_State["eye"] = 10
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Atlas_State["sparkles"] = 0
        Atlas_State["armR"] = 0

        playerUnits[0].cHP = -13
        playerBarNames[0] = "{color=#3bec27}Atlas?"
        Atlas_Stats.iconState = 3

    play sfx ko_reverse

    show atlas:
        yoffset 1000
        matrixtransform RotateMatrix(0.0, 180.0, 25.0)
        ease 2.0 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    $RefreshBarHP()
    Narrator "Suddenly Atlas perks right back up, and wipes away the green liquid trailing from his mouth. "

    $Atlas_State["eye"] = 11

    P_Atlas "Wowzers! I feel like my skeleton could jump out and dance a jig! Seriously, Beyond The Grave will knock your socks off!"
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        HighlightPlayerUnitBars([])

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            ease 0.3 yoffset 0
        parallel:
            linear 0.15 matrixtransform RotateMatrix(0.0, 0.0, 10.0)
            linear 0.15 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "You jump from your seat."
    $HideBars()

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        yoffset 0

    Robyn "Wait— what’s going on? What did you do to Atlas!?"

    voice mm_laughf

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    Madhouse "Chillax, it’s only temporary. Assuming you can get through this next segment. It’s time for my favorite game, Fake or Folklore!"

    python:
        Atlas_State["eye"] = 10
        Atlas_State["sparkle"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1

        preferences.text_cps = 60
        displaymenu = True
        pauseEnable = False

    P_Atlas "Can I just say, I really enjoy our time spent together, Maddie! If I may be so bold, management should screw right off. Seriously, what do those jerks know!? Sure you’re rotting away in an abandoned building but hey, at least the opossums are nice.{nw}"

    python:
        displaymenu = False
        pauseEnable = True
        preferences.text_cps = 30

    voice mm_confused
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 10
    voice mm_yawn
    Madhouse "Anyway."

    python:
        Atlas_State["eye"] = 11
        Atlas_State["sparkle"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0

        MM_State["eyes"] = 0
        MM_State["mouth"] = 0
    Madhouse "Why don’t you explain the rules, fly boy?"
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

        Atlas_State["eye"] = 11
        Atlas_State["sparkle"] = 0
        Atlas_State["armL"] = 2
        Atlas_State["feelers"] = 1

    show atlas: ##possessed think: TODO
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        linear 0.15 xoffset -10
        linear 0.05 xoffset 0
        pause 0.1
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        pause 0.05
        linear 0.15 xoffset -10
        linear 0.05 xoffset 0
        pause 1.0
        repeat

    Narrator "Atlas jitters unnaturally, his antennae twitching as he speaks."

    P_Atlas "Sure thing, Maddie! The rules are easy: Mike here will describe a cryptid and you have to guess what it is! If you get it wrong, you’ll suffer a tiny penalty. If you’re alive by the end, you win!"
    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "A penalty? I’m guessing you’ll kill me if I refuse to play."
    python:
        Atlas_State["eye"] = 10
        Atlas_State["sparkle"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0

    show atlas:
        xoffset 0


    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9

    Madhouse "No way! I’ll just be keeping Atlas as collateral, so by all means, leave your precious mothman behind! I could use a co-host."
    python:
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3


    show robyn:
        xanchor 0.5
        yanchor 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    call makeCheckpoint from _call_makeCheckpoint
    Robyn "Fine! I’ll play your stupid game."
    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.6 matrixtransform RotateMatrix(0.0, 0.0, 10.0) yoffset 110
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    Narrator "You plop back down in the cushioned office chair and fold your arms."
    jump RadioQuiz

default radioDamagedHP = 0
label RadioDamaged(lastQ=False):
    $playerUnits[0].modifyHP(-(3+numWrong*2),1.0,"guts")
    $radioDamagedHP = playerUnits[0].maxHP - playerUnits[0].cHP
    $RefreshBarHP()

    if numWrong < 1 and playerUnits[0].isAlive:
        Narrator "You flinch from a sudden jolt of pain aching through your body."

        $pcSelected = 0
        $Robyn_State["mouth"] = 1
        $Robyn_State["eyes"] = 1
        $Robyn_State["brow"] = 2
        Robyn "Irk! Ow..."
        $PC_Stats.iconState = 0

        if not lastQ:
            $MM_State["eyes"] = 6
            $MM_State["mouth"] = 5
            Madhouse "It’ll only get harder from here. In fact, every question you get wrong will slightly increase the vitality we sap from you. Sorry, rules are rules."

            $Robyn_State["mouth"] = 1
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 3
            Robyn "You’re making up the rules!"

            Madhouse "Someone’s gotta make ‘em!"
    elif numWrong < 2 and playerUnits[0].isAlive:
        show robyn:
            ease 0.15 yoffset 90
            ease 0.15 yoffset 110
        $Robyn_State["mouth"] = 7
        $Robyn_State["eyes"] = 3
        $Robyn_State["brow"] = 3
        Narrator "Suddenly you're hit with a gut punch this time, keeling over from an invisible force stabbing into your stomach."
        $pcSelected = 0
        $PC_Stats.iconState = 0
        $Robyn_State["mouth"] = 4
        $Robyn_State["eyes"] = 0
        $Robyn_State["brow"] = 3
        Robyn "Gah! D-dude, this game’s supposed to be fun!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 5

        Madhouse "It's fun for me!"
    elif numWrong < 3 or not playerUnits[0].isAlive:
        show robyn:
            ease 1.0 yoffset 700

        python:
            Robyn_State["mouth"] = 1
            Robyn_State["eyes"] = 3
            Robyn_State["brow"] = 2

        Narrator "Feeling woozy, you clutch your stomach and teeter before falling over."

        python:
            PC_Stats.iconState = -1
            Robyn_State["mouth"] = 2
            Robyn_State["eyes"] = 0
            Robyn_State["brow"] = 2

            MM_State["eyes"] = 0
            MM_State["mouth"] = 9

            Atlas_State["eye"] = 5
            Atlas_State["eyeFrame"] = 2
            Atlas_State["feelers"] = 1
            Atlas_State["armL"] = 1
            Atlas_State["armR"] = 1
        Madhouse "Gyehahahaa! Looks like your soul is mine! Oh well! I can finally break out of this lousy joint!"

        pause 0.01
        scene black
        with Dissolve(1.0)

        $Atlas_State["eye"] = 11
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0


        P_Atlas "You should start a podcast!"
        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 5

        Madhouse "M’yeah, I’ve got time."


    $numWrong+=1
    $PC_Stats.iconState = 0
    return

label RadioQuiz:
    python:
        PC_Stats.updateStats()

        playerUnits = []
        playerUnits.append(PC_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0])

        Atlas_State["eye"] = 11
        Atlas_State["armR"] = 1

    show atlas: #TODO possessed snarky hand:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.75 matrixtransform RotateMatrix(0.0, 180.0*4, 0.0)


    $musicPlayer.playSong(song="urgently_jammin_song",fadeOut=5,fadeIn=5)

    P_Atlas "Now’s your chance to really let your knowledge shine!"
    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Madhouse "Couldn't have said it better myself Flyboy. Now let’s get started with some FAKE., or., FOLKLORE!"

    hide atlasIcon onlayer screens

    python:
        Atlas_State["eye"] = 10
        Atlas_State["armR"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0


    Madhouse "Question 1!{nw}"

    extend "\n\nSighted in 1971, the Missouri Monster, Momo, is known to scare off attackers with what?"

    python:
        displaymenu = True
        isRight = False
        numWrong = 0

    menu:
        extend ""

        "Throwing heavy logs and rocks at supposed attackers.":
            python:
                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 4
                Robyn_State["brow"] = 1

            ##TODO voice PC_Thinking
            Robyn "By throwing... rocks and stuff? To protect themselves?"
        "It stinks.":
            python:
                isRight = True

                Robyn_State["mouth"] = 7
                Robyn_State["eyes"] = 0
                Robyn_State["brow"] = 2

            ##TODO voice PC_Thinking
            Robyn "Don’t they smell really bad? I’d think they’d stave people off with their stench."
        "A strongly worded letter.":
            python:
                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 4
                Robyn_State["brow"] = 1

            ##TODO voice PC_Confused
            Robyn "By sending a… strongly worded letter?"

            Narrator "You're going to die here."

    $displaymenu = False
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 6

    Madhouse "That’s certainly an answer!"
    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    play sfx drumroll

    $renpy.block_rollback()

    if isRight:
        play sfx emote_realization_sfx
        python:
            Atlas_State["eye"] = 11
            Atlas_State["feelers"] = 0
            Atlas_State["armL"] = 2

        P_Atlas "C’mon, are you even trying?"

        Madhouse "You’re completely right, I’ve gone softer than a marshmallow."
    else:
        play sfx sadTrumpet
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 2
        P_Atlas "BZZT! Wrong. The correct answer was its bad smell!"

        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 0
        P_Atlas "Aw, too bad. Looks like you’ll have to lose some life."

        call RadioDamaged(False) from _call_RadioDamaged
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 1
    $Atlas_State["armL"] = 0

    Madhouse "Question 2!{nw}"

    extend "\n\nOld Ephraim, a cryptid found terrorizing Logan Canyon in 1923, was what creature?"
    python:
        displaymenu = True
        isRight = False

    menu:
        extend ""

        "a {sc=5}{b}{color=#ff4545}BIG{/color}{/b}{/sc} bear":
            $isRight = True
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 2

            Robyn "Was Ephraim a big bear?"

            Narrator "You're just guessing at this point."
        "a Bigfoot":

            $Robyn_State["mouth"] = 6
            $Robyn_State["eyes"] = 1
            $Robyn_State["brow"] = 2
            Robyn "Wasn't he a bigfoot?"

        "a Lost Grey":
            $Robyn_State["mouth"] = 3
            $Robyn_State["eyes"] = 1
            $Robyn_State["brow"] = 2

            Robyn "A uh... Lost Grey."

            Narrator "You think you read something about this once."

    $displaymenu = False

    show atlas:
        linear 0.1 xoffset -10
        linear 0.1 xoffset 10
        repeat

    $Atlas_State["eye"] = 11
    $Atlas_State["feelers"] = 1
    $Atlas_State["armL"] = 2
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 6
    Madhouse "How daring!"

    play sfx drumroll
    show madhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.25 matrixtransform RotateMatrix(0.0, 0.0, -7.0) yoffset 170
        ease 0.25 matrixtransform RotateMatrix(0.0, 0.0, 0.0) yoffset 140

    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 0
    $Atlas_State["armL"] = 0
    Narrator "Madhouse gestures to Atlas who’s shaking like a ragdoll."

    $renpy.block_rollback()
    show atlas:
        xoffset 0

    if isRight:
        play sfx emote_realization_sfx
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 2
        P_Atlas "Correct!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 10
        Madhouse "Huh, I certainly wasn’t expecting that. Good on ya."

        $Robyn_State["mouth"] = 4
        $Robyn_State["eyes"] = 0
        $Robyn_State["brow"] = 1
        Robyn "Oh— um, thanks?"
    else:
        play sfx sadTrumpet
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 2

        $Robyn_State["mouth"] = 2
        $Robyn_State["eyes"] = 2
        $Robyn_State["brow"] = 1

        P_Atlas "BZZT! Wrong. The correct answer was a big bear."

        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        #P_Atlas "Oof and that’s a hit! Sorry pal."

        call RadioDamaged(False) from _call_RadioDamaged_1
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    P_Atlas "Next Question?"

    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 9
    ##TODO voice MM_Laugh4
    Madhouse "{bt=3}Oh, now this is a good one.{/bt}"

    #QUESTION: 3
    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 0
    $Atlas_State["armL"] = 0
    Madhouse "Question 3!{nw}"

    extend "\n\nThe Rochester Giant, sighted in 1965, crushed the hood of whose car?"
    python:
        displaymenu = True
        isRight = False

    menu:
        extend ""

        "George... Washington.":
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 1
            ##TODO voice PC_Confused
            Robyn "George... Washington."
        "Harold":
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 2
            ##TODO voice PC_Thinking
            Robyn "Harold sounds about right. That’s like, a normal name."
        "How am I supposed to know that?":
            $ isRight = True
            $Robyn_State["mouth"] = 4
            $Robyn_State["eyes"] = 4
            $Robyn_State["brow"] = 3
            ##TODO voice PC_Frustrated
            Robyn "I don’t even know what the Rochester giant is. You’re totally making stuff up."
    python:
        displaymenu = False
        renpy.block_rollback()

    if isRight:
        voice atlas_possessed_betrayed
        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 1
        $Atlas_State["armR"] = 1
        P_Atlas  "Heeeey, no fair Maddie! Trick questions are totally against the rules!"

        $Atlas_State["eye"] = 7
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0
        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 1
        Madhouse  "How are you this {sc=3}obnoxious{/sc}?! You’re supposed to be under my complete control!"
        $Atlas_State["eye"] = 10
    else:
        play sfx sadTrumpet

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 7
        Madhouse "Gyeheheh! You totally fell for it! The Rochester Giant doesn’t exist!"

        $Atlas_State["eye"] = 10
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0
        P_Atlas "BZZT! Wrong, but Maddie, you totally cheated!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 3
        Madhouse "So what?"

        call RadioDamaged(True) from _call_RadioDamaged_2
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $RefreshBarHP()
    Madhouse "I think we have time for one last question, as an encore to the folks at home."

    $Robyn_State["mouth"] = 3
    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1

    Narrator "Mike leans into his microphone, lowering his voice to a low growl."

    python:
        Atlas_State["eye"] = 10
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    Madhouse "Do you know what happens to cheaters?"

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 9

    #Narrator "Lifting his hat slightly, Mike’s empty white eyes lock onto your fearful gaze."
    play sfx drumroll
    $displaymenu = True
    menu:
        extend ""

        "You never made a rule for that.":
            Narrator "A chill runs down your spine as you hold your ground."
            play sfx sadTrumpet
            Madhouse "So you admit it."
        "I lose?":
            play sfx sadTrumpet
            Madhouse "{sc=5}OF COURSE YOU LOSE.{/sc}"
        "We're free to leave.":
            play sfx sadTrumpet
            Madhouse "Of course! Waltz on out of here, why don’t I hand over my wallet while I’m at it!"
    $displaymenu = False
    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 7
    Madhouse "{sc=5}I MAKE the rules!{/sc} It’s my show, my rules, my game!"

    show madhouse:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.25 yoffset -100 xzoom 0 blur 30
        pause 0.3
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.4
        ease 0.25 yoffset 0 xzoom 1 blur 0
    Narrator "The ghost suddenly blinks out only to reappear behind Atlas."

    voice mm_yourejustanotherfakefan
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    Madhouse "You’re just another fake fan."

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9

    show madhouse: ##TODO creepy grin:
        ease 0.65 xcenter 0.5 zoom 0.75 alpha 0 blur 30

    show atlas:
        linear 0.075 xoffset -3
        linear 0.075 xoffset 3
        repeat

    $Atlas_State["feelers"] = 1

    show  Overlay Green Flashing
    Narrator "In a flash, Mike melds with Atlas and the two form a much larger, scarier creature."

    $tRobynHP = playerUnits[0].cHP
    jump fightbuildup
default tRobynHP = PC_Stats.maxHP



#Go to 3.5
