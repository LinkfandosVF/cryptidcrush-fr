image chapter0 title:
    zoom 0.44
    blur 10
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_BW.webp"
    matrixcolor ColorizeMatrix("#000000","#000000")
    ease_bounce 3.0 matrixcolor ColorizeMatrix("#000000","#f91359") blur 3

image chapter0 glitch:
    zoom 0.44
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchA.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchB.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchC.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchB.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchA.webp"
    pause 0.12
    matrixcolor SaturationMatrix(1.3)
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_Base.webp"

label CH0_TitleCard:
    $musicPlayer.playSong(fadeOut=2)
    scene black with Dissolve(0.5)
    window hide
    $quick_menu = False
    $quicker_menu_show = False

    scene chapter0 title
    camera:
        zoom 1.3 ycenter 0.7 xcenter 0.7
    with Fade(0.5, 0.5, 1.0, color="#000000")

    $musicPlayer.playSong(song="chapter_0_song",songLoop=False,notif=False)
    pause 1.5
    camera:
        zoom 1.0 zpos 0 ycenter 0.5 xcenter 0.5
    show chapter0 glitch
    $musicPlayer.playSong(song="radioStatic",fadeIn=20,music2=True)
    $renpy.music.set_volume(1.0, delay=0.0, channel=u'music2')
    pause 1.0
    camera:
        zpos 0 ycenter 0.5 xcenter 0.5

    show Ch_0_Title_Text

    pause
    stop music2 fadeout 3.0
    return

layeredimage ch0ttxt:
    always:
        Text("{ddd=#32f3ff-#ce2aff}{size=75}  Chapter 0  \n   Dead Air   {/size}{/ddd}")

    always:
        Text("{glitch=3.0}{size=75}{color=#32ff84}  Chapter 0  \n   Dead Air   {/color}{/size}{/glitch}")

image Ch_0_Title_Text:
    #WaveImage("ch0ttxt", amp = 2.75, strip_height = 6,melt=True,freq=35)
    "ch0ttxt"
    xanchor 0.0
    yanchor 0.0
    xpos -30
    ypos 30
    alpha 0
    blur 3
    pause 0.6
    ease 0.5 alpha 1

label Ch0_Intro:
    stop music2
    stop music

    python:
        musicPlayer.playSong()
        timeText = "12:00AM"

    scene BG Apartment Bedroom

    show Atlas_Phone Ring CG:
        xcenter 0.5

    with Fade(0.5, 1.0, 0.5, color="#000000")

    play sfx phone_notif
    Narrator "{sc=3}Buzz- Buzz-{/sc}"

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 1


        Taro_State["pawR"] = 1
        Taro_State["eyes"] = 2
        Taro_State["mouth"] = 4

    Narrator "Your phone startles you awake, a trail of messages scrolling down your screen. IF YOU SEE THIS IT'S EDITED WOWO FRENCH PATCH"
    play music astral_reflection
    show Atlas_Phone CG
    Atlas "Hey, are you awake?"

    Atlas "{bt=3}It's time~{/bt}"

    Atlas "Ghosty time."

    Atlas "I sent you the address!"

    Atlas "Just follow the radio tower and you'll find it!"

    Narrator "All you can manage to type back in your half asleep sluggish state is—"
    stop music
    $musicPlayer.playSong()
    Robyn "K."
    scene black with dissolve

    $timeText = "12:30AM"
    Narrator "..."

    $timeText = "1:00AM"
    $musicPlayer.playSong(song="eating_in_the_car_song",fadeIn=10)

    Narrator "You feel a sudden icy chill, jolting you awake and sending shivers down your spine."

    scene BG Apartment Bedroom
    camera:
        zoom 3.0
        xcenter 1.05
        ycenter 0.8

    python:
        Taro_State["pawR"] = 1
        Taro_State["eyes"] = 2
        Taro_State["mouth"] = 4

    show taro:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter 0.7
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat
    Robyn "..!"

    Narrator "You see a large, fuzzy gray cat with three eyes and a flaming tail shoving her translucent paw through your face."

    voice taro_greetingsmortal
    Taro "Greetings mortal."

    with hpunch
    camera:
        ease 2.0 xcenter 0.5 ycenter 0.5 zoom 1.0

    Narrator "With a yelp, you leap out of bed, the shimmering tabby cat phasing right through you."
    camera:
        ease 0.5 xcenter 0.5 ycenter 0.5 zoom 1.0

    python:
        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 2

        Taro_State["pawR"] = 0
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

    show robyn pjs:
        xcenter -0.6
        pause 0.5
        matrixcolor TintMatrix("#bbb4ff")

        xcenter 0.6
        yoffset 700
        ease 0.5 xcenter 0.3 yoffset 0

    voice RobynSays("Chapter 0","CantYouJustBeNormal")
    Robyn "Can't you just be {sc=3}NORMAL?!{/sc}"

    python:
        Taro_State["eye"] = 3
        Taro_State["mouth"] = 4

    voice taro_iwasgettingdesperate
    Taro "You slept through three alarms! I was getting desperate."

    python:
        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1

        Taro_State["eye"] = 0
        Taro_State["mouth"] = 4

    show robyn:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter 0.3
        yoffset 0
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)


    Robyn "Okay, OKAY. I’m awake. And… I’m running late!"

    $Robyn_State["mouth"] = 3

    show robyn:
        ease 0.5 xcenter -0.3

    Narrator "You rush around your room gathering everything you could possibly need for tonight."

    show robyn default:
        xcenter -0.3
        matrixtransform RotateMatrix(0,0,0)

        ease 0.5 xcenter 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.5
        linear 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        ease 0.25 xcenter 0.7
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        ease 0.25 xcenter 0.9
        pause 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.7
        linear 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "You then run through your mental checklist, ‘Don’t forget your flashlight, bolt cutters, granola bars, and….’"

    show robyn:
        xcenter 0.9
        ycenter 0.8
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        ease 0.5 ycenter 1.1 matrixtransform RotateMatrix(0.0, 180.0, -20.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 ycenter 0.8
        ease 2.0 xcenter -0.2

    Narrator "You squat down to tie your shoes and slip on your jacket. Opening the door you  step out into the stuffy hallway and march out to your car."

    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

    Taro "W-wait for me!"

    python:
        Taro_State["eye"] = 4
        Taro_State["mouth"] = 3

    show taro:
        ease 0.6 xcenter -0.2

    Narrator "Taro has to race to catch up with you, meowing in protest as she kicks off the top step and floats down the stairs, phasing right through the apartment wall."

    python:
        songText = "Midway to Nowhere"
        musicNote = 8

    hide screen quicker_menu

    call CH0_TitleCard from _call_CH0_TitleCard

    camera:
        zpos 0 ycenter 0.5 xcenter 0.5

    python:
        quick_menu = True
        musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=8,fadeOut=1)

    scene BG Road Side with Fade(0.5, 0.5, 0.5, color="#000000")
    window show

    Narrator "Taro finally lands on your shoulder as you reach your car— \nAnd nips your ear."

    play sfx hurt_a
    Robyn "OW!"

    Narrator "You try to brush the phantom cat off your shoulder but your hand sweeps right through her."

    Taro "Caught you!"

    #Robyn "Ugh."

    #Narrator "After convincing Taro that the passenger seat is the coolest seat in the car, she finally settles down, letting you buckle up and start the engine."

    show Driving Night Graphic
    play sfx carStart
    Narrator "You flick on the headlights before backing up and pulling onto the street."

    stop sfx fadeout 1.0
    play ambiance car_ambiance fadein 8.0
    Taro "Are you sure Atlas is gonna be any help?"

    Narrator "Taro keeps her little paws tucked under her fluff like a fuzzy bread loaf."

    Taro "Y’know what they say about mothmen…"

    voice RobynSays("Generic","Annoyed")
    Robyn "That they’re bad omens?"

    Taro "Bingo."

    Robyn "Omen or not, I could use all the help I can get."

    Taro "Right, that nasty curse."

    Taro "You should really get that checked out!"

    Robyn "Isn’t that YOUR JOB?"

    voice taro_smuga
    Taro "You don’t expect me to work on an empty stomach do you?{nw}"

    #Narrator "Taro whimpers, bringing a weak paw to her forehead."

    extend "\n\nI’m feeling faint..."

    Robyn "Do you need me to stop and get you something?"

    Taro "Oh, no, don’t worry about me. I’ll... survive… You’re the one dealing with that wretched curse, not me."

    Robyn "I don’t feel any different."

    voice taro_laughab
    Taro "Ohoho, you will, and it’s going to be agonizing."

    Robyn "You never mentioned that!"

    Taro "I didn’t want to scare you! Even describing this curse brings about {i}evil{/i}."

    Robyn "So, you can’t get rid of it, you can’t even talk about it, and it’s going to be excruciating. Is there anything else you forgot to tell me?"

    #Taro "Uh..."

    #Narrator "Taro glances around and slouches back in the passenger seat. She takes a pause and closes her third eye, thinking."

    Taro "Well. There’s a countdown."

    Robyn "A countdown?"

    Taro "That’s right. Its a countdown to your {sc=1}imminent{/sc} demise."

    #Narrator "You shoot Taro a sharp look."

    Robyn "That’s not funny!"

    Taro "Prrrh, I’m not joking, silly."

    Robyn "How much time do I have?"

    Taro "That’s for a cat to know, and a physician to find out."

    Robyn "But that’s why you’re here right? Being a cosmic guardian and all. You’re meant to protect me."

    #Taro "..."

    Taro "...Absolutely!"

    show Atlas_Phone Ring CG:
        xcenter 0.7
        yoffset 700
        ease 0.5 yoffset 0

    play sfx phone_notif
    Narrator "Your phone chimes, buzzing in the cupholder."

    show Atlas_Phone CG
    Atlas "{sc=2}Where are you?{/sc}"

    Robyn "I’m on my way! Sheesh, unlike you most of us can’t fly."

    Atlas "You fell back asleep., didn't you."

    Robyn "I'm not nocturnal!"

    Atlas "Not with that attitude! \n\nSo,, do you see the station?"

    Narrator "Leaning forward, you glance upwards towards the distant radio tower cutting through the night air."

    Robyn "I think so.{nw}"

    extend "\n\nIs it just the three of us?"

    Atlas "Depends… How cool are you with devils?"

    Robyn "Pretty cool? Why?"

    Atlas "I have a friend who just got off work and was wondering if they could tag along! \n\nI figured I’d ask you first!"

    Robyn "Yeah, I’d definitely feel safer in a larger group."

    voice atlas_booyah
    Atlas "Sweet!"

    Robyn "See ya soon."

    Atlas "Don’t forget about the phantom frequency!"

    #Taro "There’s ghosts on the radio waves?"

    Robyn "Channel 103.1, Elkhorn Radio, I’ve got it. I’ve got it."

    Atlas "Great tha—{nw}"


    show Atlas_Phone CG:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
        parallel:
            ease 0.25 yoffset -150
            ease 0.25 yoffset 0

        on hide:
            ease 1.0 yoffset 700

    play sfx hurt_b
    Narrator "{i}THUNK.{/i}"

    Narrator "The sound of feathers brush against the microphone and the audio fizzles out before Atlas squeaks."

    Atlas "Sorry, I hit a lamp post."

    Atlas "I-I'll meet up with you soon. \n\n\Drive safe!"

    hide Atlas_Phone
    Narrator "Atlas hangs up."

    #Taro "Psh, classic moth move."

    Narrator "You picture Atlas wildly fluttering around a giant light bulb, and then it dawns on you."

    Robyn "I forgot my flashlight!"

    Taro "Looks like we’ll need to make that pitstop and snack run!"

    #voice RobynSays("Generic","HmphB")
    #Robyn "Goddammit."

    Narrator "Rolling into view is a dingy looking gas station named Al’s Owl Nighter. Dozens of sun bleached local ads plaster the foggy store windows, weeds sprouting through the cracks in the cement."

    Narrator "This place looks safe enough right? It’s well lit at least."

    $musicPlayer.playSong(song = "next_time_on_song",songLoop=False,fadeOut=0.5)
    stop ambiance fadeout 4.0
    jump Ch0_Minimart

label Ch0_Minimart:
    scene BG Gas Station Night with Fade(0.5, 4, 0.5, color="#000000")
    python:
        musicPlayer.playSong(song="pleasant_conversation_song",fadeOut=2,fadeIn=1)
        timeText = "1:30AM"

        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 0
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0

        Taro_State["eye"] = 0
        Taro_State["mouth"] = 0

    Narrator "A pleasant jingle echoes into the night air, as the door leading out of a roadside minimart swings open."

    Narrator "You walk out into the starlight, carrying a convenience store sushi roll and a cheap flashlight."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 4
        Robyn_State["mouth"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.6
        appearBlack(shading="#bbb4ff",t=0.5)

    voice RobynSays("Chapter 0","SuspiciouslyUnderpriced")
    Robyn "That sushi was... {i}suspiciously underpriced.{/i}"

    Narrator "You hold the receipt up to the neon open sign, eyeing it \nclosely."

    $Robyn_State["eyes"] = 2
    show robyn:
        matrixcolor TintMatrix("#bbb4ff")
        alpha 1
        blur 0
        ease 0.15 yoffset -20
        ease 0.15 yoffset 0

    voice RobynSays("Chapter 0","HmOhWell")
    Robyn "Mmh, oh well."

    show robyn:
        ease 1.6 xcenter 0.3
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "You shuffle back to your car, bounty in tow, and gaze over the horizon."

    #Narrator  "You stare off towards the sleeping town of Longhope, your new home, and gather your thoughts."

    Narrator "You haven’t had a moment to yourself since that cat practically poofed into existence."
    #But you’d better get going, no way in hell are you pulling another all-nighter."

    python:
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 5

    Narrator "Opening the car door, you plop down the bag of groceries with a bit of a huff."

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 5

    Narrator "Your ear catches a low, restrained sound of claws scraping against leather, the sound of some terrible creature trying to hide her devilry."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 4

    Robyn "Taro,, you goblin! {sc=2.5}That’s my {b}CAR{/b}!{/sc}"

    python:
        Robyn_State["mouth"] = 5

        Taro_State["eye"] = 1
        Taro_State["mouth"] = 4
        Taro_State["pawR"] = 2
        Taro_State["pawL"] = 1

    show robyn:
        ease 0.5 xcenter 0.5

    show taro:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter -0.3
        ease 0.5 xcenter 0.3

    voice taro_laughab
    Taro "{bt=4}Prrrrb{/bt}?"

    python:
        Taro_State["pawR"] = 1
        Taro_State["pawL"] = 0

    show robyn:
        xcenter 0.5
    Narrator "Taro splays her paws and stretches, dragging her claws across the car seat."

    python:
        Taro_State["eye"] = 0
    Taro "Well, as my meowther always said, the world is your scratching post!"

    #Narrator "She lifts her chin slightly and purrs."

    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 3

        Taro_State["eye"] = 3

    Taro "I’ll consider sparing your car’s interior if you offer me something I want~"

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 0

        Taro_State["eye"] = 5

    Narrator "She tilts her head to one side and closes her eyes expectantly."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 3
        Robyn_State["mouth"] = 0

    #Robyn "{bt=2.5}Fiiiine.{/bt}"

    python:
        Robyn_State["eyes"] = 3
        Robyn_State["mouth"] = 0

    show robyn:
        ease 2.0 xcenter 0.35

    Narrator "You roll your eyes and reach over, gently scratching Taro behind the ears. She’s oddly cold for a big fuzzy cat."

    show robyn:
        xcenter 0.35

    Robyn "You’re a real handful Taro. Seriously, what kind of cat drags me out past midnight for some expired sushi? We have places to be!"

    $Taro_State["eye"] = 3

    show robyn:
        ease 2.0 xcenter -0.2

    show taro:
        ease 2.0 xcenter -0.25

    Taro "A nyangel of course! Or that’s what I call myself anyway. You do know I’m not just a normal cat, right? Nyaow, paw over the goods."

    hide robyn
    hide taro
    Narrator "You peel off the plastic wrap and slide it towards the demanding cat."

    #Robyn "How does a ghost cat eat? The world may never know."

    Narrator "You turn the key in the ignition, the old car rattling to life."

    Robyn "We’d better get going before I totally chicken out."

    $musicPlayer.playSong(fadeOut=6)
    play sfx car_ignition
    Narrator "The car drives off, peeling out of the convenience store parking lot and down the dimly lit streets of Longhope."

    window hide
    scene BG Road Side with pixellate #----------------------------------------- Road side
    window show

    play ambiance car_ambiance fadein 8.0
    $musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=8)
    stop sfx fadeout 1.5
    show Driving Night Graphic
    python:
        timeText = "1:45AM"
        songText = "Midway to Nowhere"
        musicNote = 11

    #Maybe put in a Robyn line here to warrant the Taro response more

    Narrator "Taro scarfs down the last bits of sushi, licking specks of rice off her nose."

    #Taro "You’ve got nothing to worry about, [PCname]."

    Taro "Aren’t we on the lookout for that phantom frequency?"

    #Narrator "Taro meows, as she gazes out the window and the car drives up the road." #as you drive further up the mountain.

    Robyn "Ah, right."

    Narrator "You slide your hand over to the dash and click on the stereo."

    play sfx radio_tuning
    Narrator "The radio whirrs on, with harsh static as it switches between frequencies until it reaches 103.1."

    stop sfx

    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    Narrator "The static is cut with a crisp and peppy tune, cueing the start of some sort of radio show."

    $musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=3)
    voice mm_radio_goodeveningfreaksters
    Madhouse "{color=#3bec27}Gooood evening freaksters! I’m your host Madhouse Mike {b}LIVE{/b} at Elkhorn County Radio."

    voice mm_radio_whatsthatdebbie
    Madhouse "{color=#3bec27}What’s that? It seems my producer’s letting me know I am, in fact, DEAD! Hah! Thanks, Debbie."

    voice mm_radio_shoutout
    Madhouse "{color=#3bec27}So! Before we get started, I just wanted to give a shoutout to all of my listeners!"

    voice mm_radio_supportandfanmail
    Madhouse "{color=#3bec27}It’s your support that keeps this show alive, so as a thank-you, I’ll be starting tonight’s show with some fan mail."

    Narrator "Madhouse clears his throat for emphasis."

    voice mm_radio_heylovely
    Madhouse "{color=#3bec27}{bt=5}{color=#3bec27}Hey lovely!{/bt} Want to make thousands working with a flexible schedule from home? Of course, you do!"

    voice mm_radio_girlboss
    Madhouse "{color=#3bec27}Join our loyal family and become the independent girl boss of your dreams!"

    voice mm_radio_joinusandflourish
    Madhouse "{color=#3bec27}For a tiny fee of twelve hundred dollars you too can enroll in our courses and start {glitch=40}{color=#3bec27}feeding{/color}{/glitch} today! Join us and flourish, The Great Mother!"

    voice mm_radio_fleshyletter
    Madhouse "{color=#3bec27}Wow. Thanks much for that threatening and oddly {bt=4}{color=#3bec27}fleshy{/bt} letter!... Seriously this thing is {sc=3}{color=#3bec27}MEATY—{/sc}"

    python:
        musicPlayer.playSong(fadeOut=2)
        pauseEnable = True

    Narrator "You turn off the radio."

    Robyn "Yuck."

    voice taro_meowf
    Taro "Didn’t you mail in a fan letter?"

    Robyn "I wouldn't call myself a 'fan',, heck, I've never even heard of the guy!" #I wouldn't call myself a "fan" Taro.

    Narrator "You grimace, glancing out the window as the woods begin thinning out into a clearing."
    voice taro_laughc
    Taro "Hm, that seems a tad insincere, bothering a fellow you don't even know."

    Narrator "The skeletal frame of the radio tower stretches up over the horizon, looming over your destination— Elkhorn Radio \nStation."

    jump atTheStation
