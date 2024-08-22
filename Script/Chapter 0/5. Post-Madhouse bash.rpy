label MM_fightAftermath:
    scene BG Studio Room Spooky
    camera:
        matrixcolor TintMatrix("#cbffd6")
    python:
        HideBars()

        barHidden = True
        showBar1 = False
        showBar2 = False
        showBar3 = False
        showBar4 = False

        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["armL"] = 0
        Jamie_State["pants"] = True
        Jamie_State["rings"] = True,
        Jamie_State["alFace"] = False
        Jamie_State["blush"] = False
        Jamie_State["sweat"] = False
        Jamie_State["steam"] = False
        Jamie_State["hurt"] = False
        Jamie_State["wispEyes"] = 0
        Robyn_State["brow"] = 0
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0
        Atlas_State["eye"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 0

        Jamie_State["eye"] = 6
        Jamie_State["armR"] = 2
        Jamie_State["fire"] = 0
        Jamie_State["r3fire"] = 0

        Atlas_State["eyeFrame"] = 2

        Robyn_State['eyes'] = 0
        Robyn_State['mouth'] = 2

    show jamie:
        xcenter 0.5
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show atlas:
        xcenter 0.4

    show tarobig:
        xcenter 0.175

    show robyn:
        xcenter 0.1
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show demon_madhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.85

    with Fade(0.1, 0.2, 2.0, color="#FFF")
    python:
        musicNote = 5
        musicPlayer.playSong(3)

    voice dmm_realdeal
    Madhouse "You’re the real deal huh? Heh. Guess that’s a wrap folks..."

    show demon_madhouse:
        matrixcolor BrightnessMatrix(0)
        ease 1.0 alpha 0 blur 30 matrixcolor BrightnessMatrix(1.0)

    Narrator "The ghost’s form flickers, Madhouse crumbling to the floor in an ectoplasmic heap."
    $Jamie_State["armR"] = 2
    $Jamie_State["fire"] = 0
    $Jamie_State["r3fire"] = 0
    hide demon madhouse
    Jamie "Let me finish this."

    show jamie:
        ease 0.4 xcenter 0.65

    Narrator "Jamie steps forward, a fire roaring in their eyes."

    ##TODO voice PC_Frustrated
    show robyn:
        ease 0.1 yoffset -20
        ease 0.1 yoffset 0

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 7
    $MM_State["mouth"] = 9
    Robyn "Nooo! I still have questions!"

    show robyn:
        ease 0.5 xcenter 0.45

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 xcenter 0.25 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show tarobig:
        ease 0.5 xcenter 0.05



    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 1
    $Robyn_State['brow'] = 4
    Narrator "You take hold of Jamie’s arm, trying to hold them back."

    Madhouse "Is that all really you care about?! You're all so clueless!"

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.9
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show robyn:
        ease 0.3 xcenter 0.45

    show madhouse:
        alpha 0 blur 30
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        xcenter 0.6
        ease 0.5 alpha 1 blur 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    Narrator "Snapping up, Mike musters up the last bit of strength he has and latches onto you."
    $Jamie_State["steam"] = 1

    Madhouse "You’re coming with me!"
    $Robyn_State['eyes'] = 4
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 1
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    jump ghostzone_ch0

label ghostzone_ch0:
    scene BG Spirit World

    python:
        musicPlayer.playSong(song = "ghost_space",fadeIn=5)
        timeText = "UNKOWN"

    with Fade(2.0, 1.0, 1.0, color="#fff")
    camera:
        matrixcolor TintMatrix("#ffffff")
    Narrator "Stirring awake, you blink spots from your vision, feeling oddly light. What is this place? You furrow your eyebrows and shield your face from the pale white light."

    Narrator "You glance down and see a harsh green outline below."

    show CG Floating Away
    with Fade(0.5, 0.1, 0.5, color="#fff")

    Narrator "It’s Madhouse with a stunned look on his face and a firm grip on your ankle, holding you in place."

    Robyn "Let go of me!"

    Madhouse "NO!"

    Madhouse "{b}You'll disappear!{/b}"

    Robyn "Isn't that the point?! You want me gone!"

    Narrator "You kick and squirm, trying to break out of the spector's grasp."

    Madhouse "Hold on! Wait, just chillax for a second!"

    Narrator "Reeling you in like a kite on a string, Madhouse finally lets you go and quickly looks away."

    show CG Floating Away:
        alpha 1
        ease 0.5 alpha 0

    show madhouse:
        matrixcolor TintMatrix("#ffded1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        xcenter 0.25
        pause 0.25
        ease 0.7 yoffset 10
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    show dead_robyn:
        matrixcolor TintMatrix("#ffded1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        xcenter 0.75
        pause 0.5
        ease 0.65 yoffset -15
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    $MM_State["armL"] = 2
    $MM_State["armR"] = 2
    Madhouse "L-look, it's no big deal! I just dragged your soul out of your body and set you adrift in the void!"
    hide CG Floating Away

    $D_RobynFace = 1
    $MM_State["mouth"] = 3
    Robyn "YOU MEAN I'M DEAD!?"



    $MM_State["eyes"] = 1
    $MM_State["mouth"] = 9
    $MM_State["armL"] = 1
    $MM_State["armR"] = 1
    $D_RobynFace = 2
    Madhouse "Yeesh,, it sounds a lot worse when you put it that way."

    Robyn "Where are we?!"
    $MM_State["mouth"] = 2
    $D_RobynFace = 0
    Madhouse "Drifting in a doorway between the spirit and material world."

    $MM_State["mouth"] = 3

    Madhouse "I usually wake up here if I pass out at my desk for too long."


    $MM_State["mouth"] = 11
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    $MM_State["eyes"] = 0
    Madhouse "Now give me your soul!"

    $D_RobynFace = 1
    $MM_State["mouth"] = 10
    Robyn "No,, you give me YOUR SOUL!"

    $MM_State["mouth"] = 4
    Madhouse "Nah."

    $D_RobynFace = 2

    Robyn "Why'd you drag me in here? What do you want from me?!"

    $MM_State["eyes"] = 3
    $MM_State["mouth"] = 0
    $MM_State["armL"] = 1
    $MM_State["armR"] = 1

    Madhouse "I need you as a vessel to escape! Don’t you feel bad for me? C’moooon you’ve seen movies, you know how this ends!"

    Robyn "..."

    $musicPlayer.playSong(song="drink_it_song",fadeOut=0.5)
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0

    Madhouse "I can tell ya whatever you want! What's this about a pesky curse?"

    $hatKnock = False
    $displaymenu = True
    menu:
        extend ""
        "Punch 'em":
            pass
        "Punch off his hat":
            $hatKnock = True
        "End his afterlife with your fist":
            pass
    $displaymenu = False
    Narrator "You ball up your fists and awkwardly shift your weight as you glide through the air."
    $D_RobynFace = 1
    show dead_robyn:
        ease 0.2 xcenter 0.4 matrixtransform RotateMatrix(0.0, 180.0, -15.0)
        pause 0.5
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    show madhouse:
        pause 0.15
        matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 0.1 xcenter 0.2 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            linear 4.9 matrixtransform RotateMatrix(0.0, 0.0, -80.0) blur 10
        parallel:
            ease 5.0 yoffset 300

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    pause 0.15
    play sfx hurt_d
    with hpunch

    $musicPlayer.playSong(song = "ghost_space")

    if hatKnock:
        Narrator "Squeezing your eyes shut, you throw your fist forward and it connects, knocking Mike’s hat off his head."

        Narrator "Mike grasps for his baseball cap and keeps it firmly planted onto his head."
    else:
        Narrator "Squeezing your eyes shut, you throw your fist forward and it connects."

    show madhouse:
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)  xcenter 0.3 yoffset 0 blur 0
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat
    $MM_State["eyes"] = 3
    $MM_State["mouth"] = 1

    show dead_robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.6
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    Madhouse "Gyaaughck!"

    voice RobynSays("Chapter 0","YoureAnAsshole")
    Robyn "You’re an asshole!"

    $MM_State["eyes"] = 7
    $MM_State["mouth"] = 1
    $MM_State["armR"] = 3
    $MM_State["armL"] = 2
    $D_RobynFace = 2
    Madhouse "Owww my nose!! How’d you even touch me?!"

    Narrator "Mike brings a hand to his face, feeling the empty space where a nose would be."

    $D_RobynFace = 1
    voice RobynSays("Chapter 0","YouDraggedMeIntoThisHellDimension")
    Robyn "You dragged me into this hell dimension, and newsflash,, we’re both ghosts!"

    Narrator "You throw your arms over your head, gesturing around the empty vacuum of space."
    $Robyn_State['eyes'] = 2
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 2

    $D_RobynFace = 2

    voice RobynSays("Chapter 0","OfCourseIFeelBadForYouMike")
    Robyn "Of course I feel bad for you Mike. You didn’t deserve to die,, let alone become a monster, but now you’re totally acting like one!"

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3
    Narrator "Mike is stunned, unsure of what to say."

    voice RobynSays("Chapter 0","SoIfYoureGonnaEatMySoul")
    Robyn "So if you’re going to steal my soul, you might as well do it already!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $MM_State["armR"] = 0
    $MM_State["armL"] = 0

    voice mm_gladly
    Madhouse "Gladly!"

    show madhouse:
        ease 0.3 xcenter 0.35
        pause 0.5
        ease 0.3 xcenter 0.4
        pause 0.5



    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 11

    $D_RobynFace = 3

    Robyn "But I don't think you will."
    pause 5.0

    show madhouse:
        ease 0.5 xcenter 0.36
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 4
    $MM_State["armL"] = 2
    $MM_State["armR"] = 2

    Narrator "The phantom backs off."

    ##TODO voice MM_Quit1
    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3
    Madhouse "You're right;., I can’t do this."
    $D_RobynFace = 2
    Robyn "Why not?"

    show madhouse:
        ease 0.3 xcenter 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    $MM_State["mouth"] = 1
    Madhouse "I don’t want to hurt you."

    $MM_State["mouth"] = 2
    Madhouse "I shouldn’t have put any of you through this. I just... don’t know what else to do."

    Madhouse "I want to escape, but what if I up and disappear? All I have is this job. I can't remember my old life."

    $MM_State["mouth"] = 9

    Madhouse "Tch, I can't even remember my old face."

    $MM_State["armR"] = 2
    $MM_State["armL"] = 3
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    Narrator "Mike tips his hat down, covering his eyes."

    Madhouse "Dammit."

    Robyn "You’re not going to disappear."

    $MM_State["mouth"] = 1

    Madhouse "Tell that to the other defunct nobodies out there."

    $D_RobynFace = 3

    Robyn "If you really want a fresh start, you could start a podcast! It’s like a radio show you carry in your pocket."

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 2
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    Madhouse "On your cell phone?"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    Narrator "Mike perks up, a slight twinkle in his dead eyes."

    Narrator "You go to take out your phone, only to realize it’s back in the material world."

    Robyn "Erm, I’ll show you later."

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3

    Robyn "Even if you’re a jerk."

    $D_RobynFace = 2

    Robyn "If it means anything, I think you’re worth more than this crusty old station."

    $MM_State["armR"] = 2
    $MM_State["armL"] = 3
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    show CG Lifeline at lifeline_pos
    hide madhouse
    hide dead_robyn
    with Dissolve(0.3)
    Narrator "Mike hesitates a moment before throwing his arms around you, giving you a big hug."

    voice mm_thanksfornotgivingup
    Madhouse "Thanks,, for not giving up on me."

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 6
    $Robyn_State['brow'] = 2
    Robyn "You don't have to be the Elkhorn Station Poltergeist. \n\n Not anymore."

    Robyn "Not if it makes you., miserable."

    show CG Lifeline2

    Madhouse "{sc=5}...{/sc}"

    Madhouse "{sc=2}Get outta here.{/sc}"

    jump leavingElkhornRadio_ch0

label leavingElkhornRadio_ch0:
    python:
        musicPlayer.playSong(fadeOut=10)
        timeText = "???"

    #Narrator "As the two of you are drowned in light, you swear you catch a glimpse of the phantom’s old face, his expression determined with eyes full of life."
    scene BG Black with Dissolve(1.0)
    Narrator "..."

    voice taro_thisisallyourfault
    Taro "This is all your fault!"

    voice atlas_howsitmyfault
    Atlas "How’s it my fault?"

    voice jamie_youknewbringingahumanhere
    Jamie "You knew bringing a human here was dangerous."

    voice taro_ghostgobblingdemon
    Taro "Says the ghost gobbling demon."

    voice jamie_tarowherewereyou
    Jamie "Ah right. Taro, where the hell were you?"

    voice taro_iwastheretoprotectmyhuman
    Taro "Tch, who cares? I was there to protect [PCname] and that’s what matters!"

    voice jamie_bareminimum
    Jamie "You did the bare minimum."

    voice taro_biteyourtongue
    Taro "Hiss! Bite your tongue."

    voice atlas_knewwouldworkout
    Atlas "I knew everything would work out."

    voice jamie_stoplyingatlas
    Jamie "Stop lying to yourself, Atlas."

    voice atlas_canseethefuture
    Atlas "B-but, I really can see the future!"

    voice taro_proveitmothball
    Taro "Then prove it mothball."

    voice RobynSays("Chapter 0","Urgh")
    Robyn "Urgh..."

    #" "
    show BG Studio Room Aftermath
    camera:
        matrixcolor TintMatrix("#abbdeb")

    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 0
    $Jamie_State["steam"] = 0

    $Taro_State["eye"] = 1
    $Taro_State["mouth"] = 3

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 5

    show jamie:
        xcenter 0.8

    show taro:
        xcenter 0.75
        matrixtransform RotateMatrix(0,180,0)

    show atlas:
        xcenter 0.3
        matrixtransform RotateMatrix(0,180,0)

    with Dissolve(0.5)

    $Taro_State["eye"] = 3
    $Taro_State["mouth"] = 1

    Taro "Shush! Look, [PCname] is waking up!"
    python:
        musicPlayer.playSong(song="dirt_nap_dreams")
        timeText = "TIRED"

        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

        Robyn_State['eyes'] = 3
        Robyn_State['mouth'] = 2
        Robyn_State['brow'] = 2

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, -30.0)
        xcenter 0.5
        yoffset 700
        ease 1.2 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)


    Robyn "Ugh. I feel terrible."

    $Atlas_State["armL"] = 0
    $Atlas_State["eye"] = 16
    Atlas "Thank goodness you're okay!"

    hide taro
    show robyn:
        yoffset 0
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        xcenter 0.75
        ease 0.5 xcenter 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    $Taro_State["eye"] = 5
    $Taro_State["mouth"] = 0

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 1
    Narrator "Taro leaps into your arms, nuzzling against your neck and purrs."

    ##TODO voice Taro_Cute
    Taro "That’s my human!"
    $Jamie_State["eye"] = 2
    $Jamie_State["armR"] = 1
    $Jamie_State["steam"] = 1
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["tears"] = 0
    Jamie "More importantly, that loathsome ghost is gone."

    Narrator "Jamie lets out a sigh of relief."
    $Jamie_State["armR"] = 0
    $Jamie_State["steam"] = 0

    ##TODO voice Atlas_Dismissive
    $Atlas_State["eyeFrame"] = 3
    $Atlas_State["eye"] = 2
    $Atlas_State["armL"] = 0
    Atlas "Yeah, let's get the heck outta here."

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 1
    Narrator "You don’t respond, a lump forming in the back of your throat."

    scene BG Black with Dissolve(0.5)
    $musicPlayer.playSong(song = "missing_you_song")
    play ambiance forest_ambianceb fadein 5.0
    Narrator "Trailing behind the group, you stare down at the ground, listening to the cold gravel crunching underneath your shoes. Slowing to a stop, the group reaches the car, watching as you dig around in your pocket and pull out a set of car keys."

    Narrator "The crew takes one last look back at the abandoned station. You watch as cracks and vines climb up its walls, the radio tower starting to rust over as the gleaming red beacon at the top flickers, then blinks out. "

    show BG Outside Radio Station Spooky3


    show atlas: ##TODO doteyes think:
        xcenter 1.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.2 xcenter 0.7
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 0
    $Atlas_State["armL"] = 0

    show jamie: ##TODO casual:
        xcenter 1.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.6 xcenter 0.2
        ease 0.4 matrixtransform RotateMatrix(0,180,0)

    show robyn: ##TODO pc pensive hand:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 2.4 xcenter 0.45

    show taro: ##smile:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 2.0 xcenter 0.85
    with Dissolve(1.0)

    $Robyn_State['eyes'] = 4
    $Robyn_State['brow'] = 3
    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 2
    $Jamie_State["mouth"] = 4
    $Jamie_State["brow"] = 3

    Jamie "Is something wrong? You look distressed."

    Narrator "Jamie places a clawed hand on your shoulder."

    pause 1.0
    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 1

    Robyn "Oh yeah, it’s cool! Haha, don’t worry about me."
    $Robyn_State['eyes'] = 2

    $Jamie_State["armR"] = 1
    $Jamie_State["eye"] = 4
    $Jamie_State["mouth"] = 2
    $Jamie_State["sweat"] = 1
    $Robyn_State['mouth'] = 1

    Jamie "Do you mind if we catch a ride with you? My hooves are killing me."

    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 1

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 5
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Jamie_State["eye"] = 2

    Atlas "Aaaaand can we crash at your place? I’d rather not risk waking my housemate Gus at this hour."

    $Taro_State["eye"] = 3
    $Taro_State["mouth"] = 2

    Taro "We don’t mind! The more the meowier~!"

    $Robyn_State['eyes'] = 1
    $Robyn_State['mouth'] = 5
    $Robyn_State['brow'] = 3
    $Jamie_State["eye"] = 3
    $Jamie_State["brow"] = 0
    $Jamie_State["sweat"] = 0
    Robyn "Don’t just answer for me—!"

    $Taro_State["eye"] = 0
    $Taro_State["mouth"] = 3
    $Atlas_State["eye"] = 1
    Taro "M'well, I figured you could use the company."

    $Jamie_State["eye"] = 2
    $Jamie_State["mouth"] = 0
    $Jamie_State["armR"] = 3

    Jamie "I do love sleepovers."

    $Jamie_State["eye"] =3
    $Jamie_State["armR"] = 2
    $Jamie_State["eye"] = 0
    $Jamie_State["wispEyes"] = 1
    $Robyn_State['eyes'] = 4
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 0
    $Taro_State["eye"] = 1
    $Taro_State["pawR"] = 2

    Robyn "Fine, not like I have a choice here."

    $Atlas_State["eyeFrame"] = 3
    $Atlas_State["eye"] = 2
    $Atlas_State["armL"] = 0
    $Jamie_State["armR"] = 4
    $Jamie_State["eye"] = 3
    $Robyn_State['mouth'] = 5
    $Robyn_State['brow'] = 2
    Atlas "What’s wrong? Is it the Gus thing? He’s a sweet guy, once you get past the shedding."

    $Robyn_State['mouth'] = 4
    $Robyn_State['eyes'] = 4

    Robyn "No, I just—., I don’t know how to feel. I didn’t get any answers about this stupid curse, I nearly DIED, and now my one source of information is gone!"

    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 3
    $Robyn_State['mouth'] = 1
    $Robyn_State['eyes'] = 1

    Jamie "Good information anyway."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 16
    $Atlas_State["armL"] = 2
    $Atlas_State["armR"] = 0
    $Jamie_State["mouth"] = 0

    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1

    Atlas "I’m a great source of information!"

    $Atlas_State["eye"] = 1
    $Robyn_State['eyes'] = 0

    Atlas "Every rumor holds a speck of truth."

    $Jamie_State["eye"] = 0
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 1

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 9
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Taro_State["eye"] = 4

    Atlas "Like eating spiders in your sleep!"
    $Jamie_State["eye"] = 4
    $Jamie_State["mouth"] = 2
    $Taro_State["eye"] = 0

    ##TODO voice Jamie_joking
    Jamie "Atlas, that rumor was debunked. I need you to know this."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 7
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    $Jamie_State["eye"] = 3
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 0
    Atlas "Oh thank god."

    $Robyn_State['mouth'] = 5
    $Robyn_State['eyes'] = 5
    $Robyn_State['brow'] = 1

    Robyn "For real though,, are you guys okay?"

    $Jamie_State["mouth"] = 0
    $Taro_State["eye"] = 5
    $Taro_State["mouth"] = 4
    $Taro_State["pawL"] = 1
    $Taro_State["pawR"] = 2

    Taro "I'm great!"

    $Jamie_State["eye"] = 1

    Jamie "Tired."
    $Atlas_State["eye"] = 5
    $Atlas_State["feelers"] = 1

    Atlas "I'll be okay,, just,, really sick of the color green."

    $Robyn_State['mouth'] = 6
    $Robyn_State['eyes'] = 0
    $Robyn_State['brow'] = 2
    $Taro_State["eye"] = 0
    $Taro_State["mouth"] = 0
    $Taro_State["pawL"] = 0
    $Taro_State["pawR"] = 0


    Robyn "Boy I hear ya."

    $Atlas_State["eye"] = 8
    $Atlas_State["feelers"] = 0
    $Robyn_State['mouth'] = 5
    $Robyn_State['eyes'] = 5
    $Robyn_State['brow'] = 0
    $Taro_State["eye"] = 2

    $musicPlayer.playSong(song="the_visitor_radio_song")

    show atlas:
        linear 0.05 xcenter 0.700
        linear 0.05 xcenter 0.704
        linear 0.05 xcenter 0.690
        linear 0.05 xcenter 0.703
        linear 0.05 xcenter 0.694
        linear 0.05 xcenter 0.7


    Atlas "But it was kinda cool being the tall one for a second there."

    $Jamie_State["eye"] = 4
    $Robyn_State['eyes'] = 0

    Narrator "You and Jamie exchange worried glances."
    $Jamie_State["eye"] = 2
    $Jamie_State["brow"] = 1
    $Jamie_State["mouth"] = 2


    Jamie "Nah,, I still prefer you pint-sized."

    $musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1)

    $Atlas_State["eye"] = 18
    $Atlas_State["feelers"] = 1
    $Jamie_State["eye"] = 3
    $Jamie_State["mouth"] = 0
    $Robyn_State['eyes'] = 3
    $Robyn_State['mouth'] = 0


    Robyn "Yeaaah,, let's never do that again."
    $Atlas_State["eye"] = 19
    $Taro_State["mouth"] = 2
    $Taro_State["pawL"] = 1
    $Taro_State["pawR"] = 2
    $Taro_State["eye"] = 5


    Taro "Don't worry lil guy,, I'm sure you looked cool!"

    $Atlas_State["eye"] = 5

    show atlas:
        ease 3.0 yoffset 35

    Atlas "Hmph."


    scene BG Black with Dissolve (1.0)
    play sfx carStart
    stop ambiance fadeout 1.0

    python:
        musicNote = 3
        musicPlayer.playSong(fadeOut=8)

    Narrator "Piling into the car, you flick on the headlights and turn the key, pulling out of the parking lot away from the abandoned radio station."
    jump drivingHome_ch0

label drivingHome_ch0:
    scene BG Road Side
    show Driving Dawn Graphic
    play ambiance car_ambiance fadein 8.0
    with Dissolve (1.0)

    Narrator "Trailing through the woods, you click on the radio, back to channel 103.1. Your heart sinks as all you hear is static drowning out the hum of the car’s engine. The show’s really over, 103.1 is nothing but dead air on the radio waves."

    Narrator "Taking a deep breath, you finally muster up the courage to change the channel, flipping back to a generic oldies station."

    Narrator "Looking over your shoulder, you see Jamie resting their head against the car window, already dozing off... Though, one sharp turn would send their horns through the glass. At least Taro looks adorable all curled up in Jamie’s arms."
    python:
        displaymenu = True
        musicNote = 9
        songText = "Annoying Phonecall"

    show MM_Phone 1 CG:
        xcenter 1.5
        ease 0.75 xcenter 0.75

    #play sfx phone_notif
    $musicPlayer.playSong(song = "digihouse_mike_song")
    Narrator "Your cellphone chimes in the cupholder of the car and much to your dismay, it’s a phone call. The number is a garbled mess of words and numbers, even the screen is glitching out.{nw}"

    menu:
        extend ""

        "Ew phone calls, no.":
            pass
        "Yes.":
            jump drivingHomep2_ch0

    show MM_Phone 2 CG

    #play sfx phone_notif

    Narrator "Stubbornly, you ignore the call but the phone doesn’t stop chiming. It doesn’t even cut to voicemail. The ringing continues, the phone is shuddering now. Please pick up the phone.{nw}"

    menu:
        extend ""

        "NOPE.":
            pass
        "Fine.":
            jump drivingHomep2_ch0

    Narrator "The phone quakes, screaming it’s chime now.{nw}"

    menu:
        extend ""

        "UGH, fine!":
            jump drivingHomep2_ch0
        "Accidentally misclick and accept the call.":
            jump drivingHomep2_ch0

label drivingHomep2_ch0:
    $displaymenu = False
    show MM_Phone 3 CG
    Narrator "The phone in your grasp shudders, the screen glitching out as a mass of green ooze squeezes itself through the dock connector. With a wet splat, the slimeball picks itself up and forms a small glowing orb."
    $BM_State["face"] = 0
    $BM_State["arms"] = 0
    $musicPlayer.playSong(song="not_so_spooky_song")

    show MM_Phone:
        ease 0.5 yoffset 700
    show blobhouse:
        xcenter 0.75
        xzoom 0
        matrixtransform RotateMatrix(0,0,0) yoffset 0
        parallel:
            ease 0.2 xzoom 1.0
        parallel:
            ease 0.5 yoffset -300
            ease 0.5 yoffset 0
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0,0,360*3)

        ease 1.5 yoffset 30
        idleFloat(2.3, 15)


    Madhouse "{bt=4}Hey hey heeeey~!{/bt}"

    Atlas "HANG UP!"

    $BM_State["face"] = 1
    $BM_State["arms"] = 1
    Madhouse "I’m finally free! Sure, I lost a few limbs but... I’m free!"

    Robyn "You were seriously camping out in my phone!? \n\nI-I thought you {i}died!{/i}"

    Madhouse "Bingo! No way am I beefing it yet! I’ve got a ton of life left in me!"

    Atlas "How?!"

    $BM_State["face"] = 3
    $BM_State["arms"] = 0

    Madhouse "Tying yourself to a person takes a lot of negative energy so I figured, why not try a smartphone instead? This thing’s jam-packed with bad vibes."

    Atlas "But— you can't just leave! You're the Elkhorn Radio Ghost!"

    $BM_State["face"] = 1
    Madhouse "{bt=4}Not anymore!{/bt}"
    $BM_State["face"] = 5
    $BM_State["arms"] = 1
    Jamie "{sc=5}YOU{/sc}!"

    Narrator "A gout of steam curls from Jamie’s jaws, heat rising off the awakened demon. Their wild eyes lock onto the glowing green orb, who squeaks out in fear."

    ##TODO voice Jamie_CCD
    Jamie "Wretched specter, you dare to show your face after what you’ve done?"

    Robyn "Jamie?"

    Atlas "Uh,, Jamie, be cool. Remember what we practiced? BE COOL!"

    $BM_State["face"] = 2
    $BM_State["arms"] = 0

    Madhouse "Hiya, bonehead!"

    voice jamie_yella
    Jamie "{sc=3}GRAWWWRGH{/sc}!"

    $BM_State["face"] = 0
    $BM_State["arms"] = 2

    show blobhouse:
        xcenter 0.75
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 yoffset 50

        block:
            parallel:
                ease 0.8 xcenter 0.25
                ease 0.2 matrixtransform RotateMatrix(0,180,0)
                ease 0.8 xcenter 0.75
                ease 0.2 matrixtransform RotateMatrix(0,0,0)
            parallel:
                linear 0.25 yoffset -100
                linear 0.5 yoffset -250
                linear 0.5 yoffset 50
                linear 0.5 yoffset -250
                linear 0.25 yoffset 50
            repeat

    Narrator "Jamie throws their clawed hand forward, slashing at Mike who bounces around the passenger seat."

    $BM_State["face"] = 2
    $BM_State["arms"] = 0

    Madhouse "Punching a ghost while he's down, huh? Typical demon."

    $BM_State["face"] = 0
    $BM_State["arms"] = 2

    show Driving Dawn Graphic:
        ycenter 0.4
        ease 0.05 xcenter 0.495
        ease 0.05 xcenter 0.505
        repeat
    Narrator "The ghost darts around the car, taunting the demon while frantically dodging Jamie’s claw swipes."

    Atlas "[PCname], eyes on the road!"

    Robyn "I’m trying!"

    ##TODO voice Jamie_ConsumeSoul
    Jamie "I’m going to devour your soul!"
    $BM_State["arms"] = 0
    Taro "Watch meowwwwwout!"
    $WolfAugust_State["head"] = 1
    $WolfAugust_State["eyes"] = 0
    $WolfAugust_State["hurt"] = 0
    show Driving Dawn Graphic:
        ease 0.6 xcenter 0.1 ycenter -0.8 rotate -720 yzoom 2.0 xzoom 0.7
    camera:
        matrixcolor TintMatrix("#abbdeb")
        ease 0.5 matrixcolor TintMatrix("#ffffff")
    show BG Road Side:
        matrixcolor TintMatrix("#ffffff")
        ease 0.5 matrixcolor TintMatrix("#abbdeb")

    show blobhouse:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.6 xcenter 0.5 yoffset 700 matrixtransform RotateMatrix(0,0,800) yzoom 2.0 xzoom 0.7

    show wolfaugust:
        xcenter 0.5
        yoffset 700
        matrixcolor SaturationMatrix(0.4)*TintMatrix("#2b2a37")
        ease_bounce 0.3 yoffset 0

    show WGusEyeglow:
        xanchor 0.5
        zoom 0.18
        ycenter 0.66
        xcenter 0.5
        yoffset 700
        ease_bounce 0.3 yoffset 0
    Narrator "Coming up fast, a hulking figure stands wide eyed on the road, staring blankly at the car racing towards them. Atlas frantically grabs at the wheel."

    Everyone "A.,a.,a.,h.,h.,h.,!"

    Narrator "The car skids forward, squealing as you slam on the brakes."

    jump Ch1_Start
