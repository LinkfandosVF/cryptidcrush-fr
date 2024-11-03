label Ch1_Day1Night:

    $musicPlayer.playSong(fadeOut=2)
    $timeText = "9:00PM"
    camera at camera_default
    scene BG Apartment Bedroom
    with quickDissolve


    Narrator "You return home and are greeted by a happy Taro. \n\nYou scratch under the cat's chin and she rubs her face against your open palm."

    Narrator "Following your usual evening routine, you fix yourself dinner and settle down for the night."

    show CGShade:
        on hide:
            ease 0.5 alpha 0
    show Charm_Bracelet:
        on hide:
            yoffset 0
            ease 1.0 yoffset 700

    Narrator "Finally in bed, you find yourself twiddling the charm bracelet between your fingers you had been gifted. You roll onto your back and examine the wooden beads."

    Robyn "I wonder if this thing'll actually work."

    Narrator "You tuck the charm under your pillow."
    scene BG Black
    with quickDissolve

    Narrator "Taro floats down and tucks her little paws under her belly, her third eye staying wide open as she dozes off."

    camera:
        camera_zoom()

    Narrator "..."

    python:
        musicPlayer.playSong(song="ghost_space",fadeIn=1,fadeOut=1)
        timeText = "12:00AM"

    Narrator "Some time passes and a voice cuts through the dark."

    voice mm_youstillawake
    Madhouse "Hey, you still awake?{nw}"

    menu:
        extend ""

        "...":
            voice mm_yougetsomerest
            Madhouse "Ah, right. You get some rest. \n\n\My bad."

        "Yeah":
            call Ch1_MadhouseConvoNight from _call_Ch1_MadhouseConvoNight

    jump Ch1_Dream2

label Ch1_MadhouseConvoNight:

    voice RobynSays("Chapter 1","WhatsOnYourMind")

    Robyn "What's on your mind?"

    show CG Madhouse_Snooze1
    with { "master" : Dissolve(0.5) }

    Madhouse "So I was thinkin'."

    Madhouse "I bet you I was a musician before all this. \n\nA real star chasing his dreams on the west coast. I fought skeezy managers,, threw parties and—"

    voice RobynSays("Chapter 1","PromDJ")

    Robyn "Dude, you were probably a prom DJ before Elkhorn Station."

    Madhouse "{sc=3}I would never.{/sc}"

    Narrator "You snicker."

    Madhouse "What about you? What pays the trespassing fines?"

    voice RobynSays("Chapter 1","WorkedAtElectronicStore")

    Robyn "I worked at an electronics store,, then part-time at some seasonal haunted house. \n\n{b}ALSO{/b},, I've never been caught so {i}shush.{/i}"

    show CG Madhouse_Snooze2 at startledSquish

    voice mm_laughb
    Madhouse "{sc=3}HAHA!{/sc}"

    Madhouse "Haunted house huh? What, you like a theater kid or somethin'?"

    #Mikey Signal
    python:
        xInstrument = "saxophone"

        bookNames = {
            "brawn": "trumpet",
            "brains": "violin",
            "hustle": "clarinet and basoon",
            "guts": "tuba",
            "charm": "saxophone",
            "occult": "drums" }

        for x in ["brawn","brains","hustle","guts","charm","occult"]:
            if PC_Stats.cStats(x) == 3:
                xInstrument = bookNames[x]
                break;

    voice RobynSays("Chapter 1","BandKid")

    Robyn "Band kid. I played the [xInstrument]."

    Madhouse "{bt=3}Ohmigosh me toooo!{/bt}\n\nProbably."

    voice RobynSays("Chapter 1","WhatDidYouPlay")

    Robyn "What did you play?"

    Madhouse "Oh you {b}know{/b} Madhouse is a bass guitar guy."

    show CG Madhouse_Snooze1 at startledSquish

    Madhouse "'Cause the sky's the limit when you're making shit up."

    voice RobynSays("Chapter 1","DontRemember")

    Robyn "You., really don't remember anything?"

    Madhouse "Nothin' outside the station."

    show CG Madhouse_Snooze2 at startledSquish

    Madhouse "But that's okay! I feel like we're close to a breakthrough here."

    Madhouse "I had fun today. \n\nSo., thanks."

    hide CG Madhouse_Snooze2
    with nwDissolve(0.5)

    Madhouse "Night, {i}band geek.{/i}"

    voice RobynSays("Chapter 1","GoodnightRockstar")

    Robyn "Goodnight {i}rockstar.{/i}"

    Narrator "You finally drift off to sleep."

    return

label Ch1_Dream2:
    scene BG Dream Yard
    nvl clear

    python:
        timeText = "Dreamtime"
        musicPlayer.playSong(song="dreamlike_state_song",fadeIn=5,fadeOut=1)


    nvl show Dissolve(1)
    with Dissolve(.5)

    NVL_Narrator "You sit alone on the far end of your old overgrown yard, staring out into the woods past the overgrowth. You hug your knees to your chest and wipe tears from your eyes, sniffling."

    NVL_DreamAtlas "Hey!"

    NVL_Narrator "A pair of bright red eyes peer out from the bushes ahead."

    NVL_Narrator "You don't respond."

    NVL_DreamAtlas "What's up?"

    NVL_DRobyn "Nothing."

    NVL_Narrator "Ducking and weaving through the brush is Atlas, looking rather scrappy in his overalls and torn open boots."

    NVL_DreamAtlas "Do you like my new shoes?"

    NVL_DRobyn "They don't fit."

    NVL_DreamAtlas "Exactly! It's so I can still grab stuff."

    NVL_Narrator "Atlas picks up a stick between his talons and swishes it around."

    NVL_DreamAtlas "Wanna see me draw?"

    NVL_DRobyn "... Okay."

    NVL_Narrator "The moth drags the stick through the dirt and scrawls something out, all while standing on one foot."

    NVL_DreamAtlas "Ta-dah!"

    NVL_Narrator "You look down at the ground and see two shakily drawn stick figures holding hands,, one figure has big eyes and feelers."

    NVL_DRobyn "You and me?"

    NVL_Narrator "Atlas looks rather proud of himself."

    NVL_DRobyn "You're just tryin' to make me feel better."

    NVL_DreamAtlas "Is it working? \n\nWhat's the matter?"

    NVL_DRobyn "Nobody believes me!"

    NVL_DreamAtlas "Believes what?"

    NVL_DRobyn "That you're real! \n\nEveryone says, {i}oooh you're playing pretend!{i} \n\nThat's just your imaginary friend."

    NVL_DreamAtlas "The photo! Didn't you take my picture?"

    NVL_DRobyn "It's too blurry."

    NVL_Narrator "Hopping across the ground, Atlas flops onto the fallen log next to you."

    NVL_DreamAtlas "Sounds like you need more proof."

    NVL_Narrator "He digs around and plucks a feather from his neck fluff."

    NVL_DreamAtlas "This should do the trick!"

    NVL_DRobyn "A feather. Everybody's gonna think you're a crow!"

    NVL_Narrator "You hear leaves rustling, heavy footsteps marching through the dense forest behind you."

    NVL_DRobyn "Huh— Who's there?"

    scene BG atTheTableFright:
        matrixcolor SaturationMatrix(1)
        ease 1.0 matrixcolor SaturationMatrix(0)
    with nwPixellate(1.0)
    NVL_Narrator "You look back and see Atlas is gone. Your backyard, the forest, everything is gone."

    nvl clear

    python:
        musicPlayer.playSong(song="the_unwelcome_visitor")
        NVL_Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "fffb42",kind=nvl)

    NVL_Someone "{size=60}Wake up.{/size}"

    nvl clear

    NVL_Narrator "Towering over you is a gruff, long haired stranger dressed in a white t-shirt and slacks. \n\nA piece of copy paper with a squiggly face scribbled in marker is taped to his face acting as some lousy mask."

    NVL_DRobyn "{size=35}Oz?{/size} \n\nWh— What're you doing in my dream?!"

    NVL_Narrator "The intruder claps a hand to his chin and peels the paper off his face."

    NVL_Oz "... \n\nBad disguise."

    NVL_Narrator "The howler hoists you up his burly arms. His hands are rough and his forearms are etched with tattoos."

    NVL_Oz "Watch your head."

    NVL_Narrator "Oz tosses you like a trash bag and—{nw}"

    jump Ch1_Day2Wakeup

# Narrator "You return home and are greeted by a happy Taro. \n\nYou scratch under the cat's chin and she rubs her face against your open palm."
#
# scene BG Apartment Kitchen
# play music summerstone_song fadeout 2.0 fadein 1.0
#
# python:
#     musicPlayer.playSong(song="eating_in_the_car_song",fadeIn=1)
#     timeText = "10:00PM"
#
#     adjustChar("Taro",pawR=2,eye=0,mouth=2)
#     adjustChar("Robyn",brow=0,eyes=2,mouth=0)
#
# camera:
#     camera_zoom(z=-300,x=150)
#
# show robyn:
#     xcenter 0.6
#
# show taro:
#     xcenter 0.7
#     matrixtransform RotateMatrix(0.0, 180.0, 0.0)
#     idleFloat(2,10)
#
# with Dissolve(2.0)
#
# Taro "Welcome back!"
#
# Robyn "Did you have a good rest?"
#
# Taro "Yep! Seems I woke up just in time for bed."
#
# scene BG Black with Dissolve(0.5)
#
# Narrator "Following your usual evening routine, you fix yourself dinner and settle down for the night."
