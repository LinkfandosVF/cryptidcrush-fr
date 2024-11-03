label Ch2_MadhouseConvoNight2:
    #scene BG Black

    #python:
    #    musicPlayer.playSong(song="ghost_space",fadeIn=1,fadeOut=1)
    #    timeText = "9:00PM"

    #with nwDissolve(0.4)

    #Narrator "..."

    #Robyn "Hey, Mike you awake?"

    #Madhouse "Wide awake."

    #show CG MM_Chill
    #with nwDissolve(0.4)

    #Narrator "Madhouse blinks into view, glowing like a nightlight. He floats down and rests his chin on his open palm."

    #Robyn "You doing okay? You've been quiet all evening."

    #Madhouse "M'yeah, I'm fine."

    #Madhouse "What about you? Can't sleep?"

    #Robyn "Just thinking."
    camera:
        camera_zoom(z=-480,y=-35,x=50,t=1.5)

    Robyn "Hey, can we talk?"

    show madhouse at vibratenum
    voice mm_damagedb
    Madhouse "{sc=2}Nnygh.{/sc}"
    python:
        adjustChar("Robyn",mouth=5,brow=2,eyes=4)
        adjustChar("MM",mouth=3)
    Robyn "I never went into detail but,, I'm cursed. I mentioned it back at the radio station,, but I think you were preoccupied."

    Madhouse "Mhmm."

    $adjustChar("Robyn",mouth=4,brow=2,eyes=1)

    Robyn "It started about a month ago and—\n\nit's like something terrible's gonna happen to me."

    show madhouse at unflipCharDelayed(0.7,0.5)

    $adjustChar("Robyn",mouth=5)
    $adjustChar("MM",mouth=4,eyes=2)

    Madhouse "Sounds like a {b}death curse{/b}."

    Robyn "Could be? Between the car crash, and the graveyard. It's like this town's out to get me."
    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
        adjustChar("MM",mouth=0,eyes=4)
    Madhouse "You got any enemies?"

    $adjustChar("Robyn",eyes=3,mouth=4)
    Robyn "No, I went unnoticed by most."

    python:
        adjustChar("Robyn",mouth=1,brow=0,eyes=1)
        adjustChar("MM",mouth=7,eyes=0)

    Madhouse "Awww, don't sell yourself short. I'm sure you got plenty of enemies!"

    $adjustChar("MM",mouth=0)

    Robyn "M'yeah, three thousand miles away maybe."
    $adjustChar("Robyn",mouth=4,brow=1,eyes=0)
    Robyn "I've got so much I wanna do! I shouldn't be wallowing over a death curse!"

    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
        adjustChar("MM",mouth=9,eyes=1)

    Madhouse "Eh, I don't see what the big deal is."

    $adjustChar("Robyn",mouth=4,brow=2,eyes=1)
    Robyn "How can you say that?"

    python:
        adjustChar("Robyn",mouth=5)
        adjustChar("MM",mouth=0)

    Madhouse "Meatball..,{nw}"
    camera:
        camera_shake_off(50)
    show robyn at startledSquish
    python:
        adjustChar("MM",mouth=9,eyes=10,armR=0,armL=0)
        adjustChar("Robyn",eyes=0,brow=1)
    extend "\n\n{bt=3}You already died!{/bt}"
    python:
        adjustChar("MM",mouth=11,eyes=0,armR=1,armL=1)
        adjustChar("Robyn",eyes=3,brow=0)

    Madhouse "A spell's gotta be null and void after a stint like that."

    python:
        adjustChar("MM",mouth=5,eyes=0)
        adjustChar("Robyn",eyes=4,brow=3,mouth=1)

    Narrator "Died? No, there's no way that counts! You were only out for a few seconds!"

    show madhouse at vibratenum
    python:
        adjustChar("MM",mouth=9,eyes=11)
        adjustChar("Robyn",eyes=1,mouth=5,brow=2)
    Madhouse "We wouldn't want ya ending up like me!"

    python:
        adjustChar("MM",mouth=3,armR=2,armL=2)

    Madhouse "Heh."

    scene BG Black

    with nwDissolve(0.5)

    Narrator "Mike’s words hang heavy in your mind. Could it be possible that the “curse” ended the moment you died in the radio station? \nIf that were true, why didn’t you feel any different?"

    scene BG Black with Dissolve(0.5)

    pause 0.5
    play sfx phone_notif

    $unlockHangout("MM",2)
    Narrator "Now's your chance to spend time with {color=#3bec27}{b}Mike{/b}{/color}! Would you like to view this {color=#ED2A82}{b}hangout{/b}{/color} now?{nw}"

    menu:
        extend ""

        "Yes!":
            call Madhouse_Hangout2 from _call_Madhouse_Hangout2
        "Not now.":
            Narrator "Aight, let's get a move on."
            pass
    jump Ch1_TessieGusTalk

#--------------------------------------------------------August Kiss
label Ch2_GusConvoKiss:
    python:
        musicPlayer.playSong(song="missing_you_song",fadeIn=1,fadeOut=1)
        timeText = "11:00PM"

    scene BG Orange with nwDissolve(0.5)
    show halfaugust:
        xcenter 0.35
        yoffset 150
        matrixcolor BrightnessMatrix(-1)
        zoom 1.5

    show robyn at flipped:
        xcenter 0.7
        yoffset 150
        matrixcolor BrightnessMatrix(-1)
        zoom 1.4

    with nwDissolve(0.5)

    Narrator "You return to the living room and see August adding sheets to a bare fold out mattress. He tosses out some blankets and tuck in the ends."

    Robyn "I'm back! What're you up to big guy?"

    August "Setting things up before I scamper off. I got homework."

    Robyn "Homework?"

    August "I'm part of a book club and I need to play catch-up. Quick."

    Robyn "Gosh, I used to be a huge bookworm, but then I fell outta the habit."

    August "M'yeah, there's a lot of distractions."

    menu:
        extend ""

        "Let the man read":
            scene BG Black with nwDissolve(0.5)
            Robyn "Well, don't let me be one too."

            Narrator "You plop down on the mattress and wrap yourself up in the blankets, wresting all hosting responsibility from the wolfman."

            Robyn "{bt=2}Aw jeez, I’m so dang tired you got no choice but to read. \nHonk shoo, mi mi mi~{/bt}"

            August "Okay okay. Goodnight [PCname]. Sleep well."

            Robyn "Goodnight! \nAnd thank you."

            August "Of course."

        "Flirt with him" if seenLabel("August_Hangout1"):

            Robyn "Can I be another distraction?"

            August "Heh! Yeah, c'mere you."
            $adjustChar("HalfAugust",shirt=0,pants=0)

            scene BG Orange
            show halfaugust:
                xcenter 0.35
                yoffset 150
                matrixcolor BrightnessMatrix(-1)
                zoom 1.5

            with nwDissolve(0.5)

            Robyn "I didn't expect you toooo... Look like that."

            $adjustChar("HalfAugust",ear=2)

            August "It's comfier. Kinda like changing into a pair of sweatpants."

            August "But everybody's different."

            Narrator "You steel your nerves, and approach the wolfman."

            Robyn "I love your beard. What product do you use?"

            August "Nothin' special. I scrub-a-dub with a honey beard wash a couple days a week and call it good."

            Robyn "Do people ever ask to touch it?"

            $adjustChar("HalfAugust",ear=0)

            August "Mmmh, only bears and hiker chicks."

            August "What, you wanna try?\n\n.,But watch out, I bite."

            Robyn "Really?"

            August "Be my guest."

            Narrator "August brushes his hair behind his ears and looks at you expectantly."

            scene BG Black

            show CG Gus kiss 1:
                yoffset 50
                pause 0.5
                easein 1.0 yoffset 0

            with Fade(0.25,0.25,0.5,color="#000000")

            Narrator "You sheepishly place a hand on his cheek and brush your fingers through his hair."

            Narrator "He leans into your touch with a gentle sigh."

            Robyn "Y'know."

            extend "\n\nI've never kissed a werewolf before."

            August "Oh yeah? You make it sound like I'm a tally on a bucket list."

            Robyn "Ah, no no! Sorry, I didn't mean it that way."

            August "Shhh, I'm just playin'."

            August "Then let's do it. No strings attached. I'll be your first."

            Robyn "Um. Mhm, yes please."

            show CG Gus kiss 2:
                xoffset -50
                easein 1.0 xoffset 0

            with nwDissolve(0.5)

            Narrator "In a swift motion, you're swept off your feet and hoisted into August's arms. He's sturdy, yet soft. His trimmed claws brush your back."

            Narrator "With a squeak, you grip August's shoulders, clutching him tightly as he holds you firmly."

            Narrator "And you kiss him."

            Narrator "The wolfman staggers, but stays upright. His claws dig into your t-shirt and a low growl curls in the back of in his throat."

            Robyn "Bite me."

            August "I... I can't."

            Narrator "The wolfman relaxes, letting you slip from his embrace."
            scene BG Black

            with nwDissolve(0.5)
            August "Not now."

            Narrator "You linger a moment, hoping August would stay,, but he doesn't. You can only nod and smile sheepishly as he wishes you goodnight. \n\nThen heads to his own room."

            Robyn "Okay, see you later."

            Narrator "The night rolls on without him."

    Narrator "You lay down and eventually fall asleep. Your phone buzzes, but it had been left on Atlas' bed."

    jump Ch2_MadhouseAndAtlas_Night

image Ch2MMAT_CG1:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_1.webp"

image Ch2MMAT_CG2:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_2.webp"

image Ch2MMAT_CG3:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_3.webp"

image Ch2MMAT_CG4:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_4.webp"

image Ch2MMAT_CG5:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_5.webp"

image Ch2MMAT_CG6:
    zoom 0.15
    "images/CGs/Chapter 1/MA_Argument/argument_6.webp"

label Ch2_MadhouseAndAtlas_Night:

    scene  BG Atlas Room Day

    show BG Atlas Room Day:
        matrixcolor ColorizeMatrix("#161226","#826fc9")*SaturationMatrix(0.3)

    with Dissolve(0.5)

    nvl show Dissolve(0.5)
    python:
        timeText = "11:00PM"
        musicPlayer.playSong(song="silence",fadeOut=1.0)

    NVL_Madhouse "{size=30}Meatball!{/size}"

    extend "\n\nHm? Where are we?"

    NVL_Narrator "You left your phone upstairs."

    nvl clear

    NVL_Atlas "What're you doing here?"

    NVL_Madhouse "Oh crap, this is your room? Oops! I thought this was the guest suite."

    NVL_Atlas "{image=Ch2MMAT_CG1}"

    NVL_Madhouse "Haha, cool. Well, goodnight! See ya!"

    NVL_Atlas "Mike, wait."

    extend "\n\nWhy're you doing this?"

    nvl clear

    NVL_Madhouse "-?"

    NVL_Atlas "{image=Ch2MMAT_CG2}\n\nWhy're you still bothering us? "
    python:
        timeText = "10:00PM"
        musicPlayer.playSong(song="silence",fadeOut=1.0)

    extend "You might've fooled them, but you're not fooling me."

    extend "\n\nIt's only a matter of time before you \nhurt someone else."

    nvl clear

    NVL_Madhouse "{image=Ch2MMAT_CG3}\nOh piss off with that shit."

    extend " I don't know you and you sure as hell don't know me."

    extend "\n\nSo why don't you take your little riddles mothman and shove it up your ass!"

    nvl clear

    NVL_Atlas "I don't know you? I've done my research."

    $musicPlayer.playSong(song="the_visitor_radio_song",fadeOut=1,fadeIn=5)

    NVL_Atlas "I know your real name is {i}{color=#3bec27}Michael Delarosa{/color}{/i}."

    NVL_Madhouse "{sc=3}—?!{/sc}"

    NVL_Atlas "You'd be twenty nine by now if you hadn't... {i}Y'know.{/i}"

    NVL_Atlas "The accent's fake too. You're from Beaverton, not the Bronx."

    NVL_Madhouse "Okay, I get it."

    NVL_Atlas "You and Debbie were an item. Once you were out of the picture the forums turned on her. They started blaming her for what happened."

    NVL_Atlas "Rumor has it Debbie met a \nfate similar to yours.{nw}"
    camera:
        camera_shake
    NVL_Madhouse "{image=Ch2MMAT_CG4}  {size=45}STOP IT!{/size}"

    nvl clear

    NVL_Madhouse "{image=Ch2MMAT_CG5}\n{sc=2}Research. Y-You mean stalking your little chatrooms?{/sc}"

    extend "\n\nYou freaks took my sad, boring life and twisted it to fit your little ghost story."

    extend "\n\n{size=30}And I believed it!{/size}"

    extend "\n\n{size=30}But I don't wanna be a monster \nanymore!{/size}"

    nvl clear
    NVL_Atlas "And you think haunting [PCname] will save you?"

    $pc_theyre = {"they":"They're","he":"He's","she":"She's"}[PCthey]

    NVL_Madhouse "[pc_theyre] my only chance."

    extend "\n\nLook, I'm sorry, okay? I'm sorry I hurt you Atlas."

    $musicPlayer.playSong(song="silence",fadeOut=2,fadeIn=5)

    NVL_Atlas "{image=Ch2MMAT_CG6}\n...{nw}"

    extend " Okay."

    NVL_Atlas "I need some space."

    NVL_Madhouse "Yeah."
    
    nvl clear

    scene  BG Black
    with Dissolve(0.5)



    jump Ch2_RobynMeetsLex
