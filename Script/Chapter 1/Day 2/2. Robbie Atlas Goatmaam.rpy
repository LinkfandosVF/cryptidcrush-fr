label Ch1_AugustCheckup_TessieGoatmaam:
    scene BG Avenue

    camera:
        matrixcolor TintMatrix("#ffe7ee")
        camera_zoom(z=-570,x=-220,y=-40)
        camera_zoom(z=-570,x=60,y=-40,t=4)

    show goatmaam:
        xcenter 0.5

    show tessie:
        xcenter 0.72

    with pixellate
    python:
        adjustChar("GM",eyes=5,mouth=1)
        Robyn_State["mouth"] = 0
        musicPlayer.playSong(song="mage_hands",fadeOut=0.5,fadeIn=0.5)
        timeText = "9:00AM"


    Narrator "While you're walking home you spot two figures, recognizing one as Goatma'am who's pacing around."
    show goatmaam at startledSquish
    voice gm_zucchinipatch
    Goatmaam "I wake up to find half my zucchini patch's been chewed to bits!"
    python:
        adjustChar("GM",eyes=2,mouth=2,armL=2,armR=2)
        adjustChar("Tessie",mouth=1,eye=1,eyeFrame=2)

        Tall = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "57fcd0")
    voice gm_ransackingmygarden
    Goatmaam "Some hooligan's been ransacking my garden!"
    camera:
        camera_zoom(z=-400,x=70,y=-80,t=2)

    Tall "Sounds like a giant woodchuck."

    Narrator "The second figure is a tall woman dressed in a nautical blouse."
    python:
        adjustChar("GM",eyes=3,mouth=6,armL=0,armR=0)
        adjustChar("Tessie",mouth=0,eye=0,eyeFrame=2)
        adjustChar("Robyn",mouth=0,brow=0)
    voice gm_woodchuck
    Goatmaam "A woodchuck..,{nw}"
    $adjustChar("GM",eyes=5,mouth=1)
    show goatmaam at startledSquish

    extend "\n\n{sc=3}{b}Wearing a coat and trousers?!{/b}{/sc}"
    python:
        adjustChar("GM",mouth=7,eyes=3)
        adjustChar("Tessie",mouth=4,eye=2,brow=3)

    Tall "Says the talking goat."

    $adjustChar("GM",eyes=5,mouth=1)
    Goatmaam "UNRELATED!"

    Narrator "You stroll into view, catching the Goatma'am's eye. She greets you happily, while the woman looks on."
    python:
        adjustChar("GM",eyes=4,mouth=0)
        Tessie_State["eye"] = 0

    camera:
        camera_zoom(z=-300,x=30,y=-60,t=2)

    show robyn:
        xcenter -0.5
        ease 2.0 xcenter 0.35
    voice gm_goodmorningdear
    Goatmaam "Good morning dear!"
    python:
        adjustChar("GM",eyes=4,mouth=2,ears=1)
        adjustChar("Tessie",mouth=5,eye=2,brow=0,eyeFrame=0)
    voice gm_dreadfulposture
    Goatmaam "Have you seen a fellow with the most dreadful posture,, wandering this street?"
    python:
        adjustChar("Tessie",mouth=4,eye=0)
        GM_State["ears"] = 0

    voice tessie_surprisea
    Tall "Someone's been stealing rocks and plucking flowers from {color=#bc8bff}Parsnip's{/color} garden."

    python:
        adjustChar("GM",eyes=5,mouth=6)
        adjustChar("Tessie",mouth=5,eye=2)

    show goatmaam at startledSquish
    voice gm_goatmaam
    Goatmaam "{sc=4}{b}GOATMA'AM!{/b}{/sc}"
    python:
        adjustChar("GM",eyes=5,mouth=7)
        adjustChar("Tessie",mouth=3,eye=0,brow=2,eyeFrame=2)

    Tall "I'm not calling you by your wizard title, {color=#bc8bff}Parsnip{/color}. \n\nThat's too silly,, even for me."
    python:
        adjustChar("GM",eyes=1,ears=1,mouth=3,armL=1,armR=2)
        adjustChar("Tessie",mouth=4,brow=0)
    voice gm_laugha
    Goatmaam "{bt=3}It's endearing!{/bt}"
    python:
        adjustChar("GM",eyes=3,mouth=7,armL=0,armR=0)
        adjustChar("Tessie",mouth=2,eye=2,eyeFrame=1)

    Tall "You don't see me wandering around calling myself human ma'am."

    $adjustChar("GM",eyes=5,mouth=2,ears=0)
    Goatmaam "That's because you're not a.,{nw}"
    python:
        adjustChar("GM",eyes=2,mouth=0)
        adjustChar("Tessie",mouth=1,brow=1,eyeFrame=0,eye=0)
        adjustChar("Robyn",mouth=5,brow=1)

    show goatmaam:
        xcenter 0.5
        ease 0.25 xcenter 0.46

    show tessie:
        matrixtransform rotated()
        ease 0.3 matrixtransform rotated(z=-7)

    extend "{bt=3} creative person!{/bt}"
    show tessie:
        matrixtransform rotated(z=-7)
        ease 0.3 matrixtransform rotated()

    $adjustChar("Tessie",mouth=0,eyeFrame=2,eye=0,brow=0)
    voice tessire_relief
    Tall "Uh-huh. So, have you seen 'em?"

    Robyn "Sounds familiar,, I did stroll by a guy skipping rocks yesterday."

    $adjustChar("Tessie",mouth=5,eyeFrame=0,eye=2)
    Tall "Into the river?"

    $adjustChar("Robyn",mouth=5,eyes=0)
    Narrator "You think back to the stone Robbie gave you and frown. It's still in your coat pocket. Can you steal rocks? Maybe."

    $adjustChar("Robyn",mouth=4,eyes=4,brow=2)
    Robyn "{size=18}Y-yeah?{/size}"

    python:
        adjustChar("Robyn",mouth=0,eyes=2)
        adjustChar("Tessie",mouth=0,eyeFrame=2,eye=1,brow=1)
    Tall "Noted."

    $adjustChar("Tessie",mouth=4,eyeFrame=0,eye=0,brow=0)
    Narrator "The woman holds her hand out for a shake."

    $adjustChar("Tessie",mouth=3,eyeFrame=2)
    Tall "I'm {color=#57fcd0}Tessie{/color}. It's nice to meet you."

    show robyn:
        matrixtransform rotated()
        ease 1.0 xcenter 0.55
        ease 0.3 matrixtransform rotated(z=5)
        ease 0.3 matrixtransform rotated()

    show goatmaam:
        ease 1.0 xcenter 0.35

    show tessie:
        matrixtransform rotated()
        pause 1.0
        ease 0.3 matrixtransform rotated(z=-5)
        ease 0.3 matrixtransform rotated()

    $adjustChar("Tessie",mouth=4)
    Narrator "You reach out and the two of you shake hands. Her grip is firm but gentle."

    $adjustChar("Robyn",mouth=6,eyes=3)
    Robyn "[PCname]."

    show goatmaam at startledSquish:
        xcenter 0.35
    python:
        adjustChar("GM",eyes=3,armL=1,armR=2,mouth=3)
        adjustChar("Robyn",mouth=0,eyes=2)

    Goatmaam "Goatma'am!"
    voice tessire_giggle
    python:
        adjustChar("Tessie",eyeFrame=1,eye=2,brow=3)
        adjustChar("GM",eyes=0,armL=0,armR=0,mouth=0)

    Narrator "Tessie chuckles."

    $adjustChar("Tessie",mouth=4,eyeFrame=0,eye=0,brow=0)
    Tessie "I'd better get going."

    Tessie "You should swing by the lake sometime!"

    $adjustChar("Tessie",mouth=2,eyeFrame=1,eye=1,brow=0)

    extend "\n\nAnd let frog legs know,, purple lupine flowers are my favorite."
    $adjustChar("Tessie",mouth=4,eyeFrame=2,eye=2,brow=0)
    show tessie:
        matrixtransform rotated()
        xcenter 0.72
        ease 0.5 matrixtransform rotated(y=180)
        ease 2 xcenter 1.3

    Narrator "Tessie smirks and gives goatma'am a big pat on the back before sauntering off on her merry way."
    camera:
        camera_zoom(z=-450,x=-50,t=1)

    python:
        adjustChar("Robyn",mouth=4,eyes=1,brow=3)
        adjustChar("GM",eyes=3,mouth=1)
        musicPlayer.playSong()

    Robyn "Hey, wait a second."
    hide tessie

    python:
        adjustChar("Robyn",mouth=3)
        adjustChar("GM",eyes=4,mouth=5)

    Goatmaam "What is it dear?"
    show robyn:
        matrixtransform rotated()
        xcenter 0.55
        ease 0.4 matrixtransform rotated(y=180)

    python:
        adjustChar("Robyn",mouth=5,eyes=4)
        adjustChar("GM",mouth=0)

    Robyn "Ah— um,, nevermind."
    python:
        adjustChar("Robyn",mouth=1,eyes=2,brow=0)
        adjustChar("GM",mouth=3,eyes=1)


    Goatmaam "Now where's your ghostly companion? I do hope those pamphlets were helpful!"
    python:
        adjustChar("GM",mouth=0,eyes=3)
        adjustChar("Robyn",mouth=4,eyes=4,brow=0)

    Robyn "Ah, yeah! Thanks."
    jump Ch1_AtlasRobbieMoment

label Ch1_AtlasRobbieMoment:
    scene BG Black
    $timeText = "10:00AM"
    camera at camera_default:
        camera_zoom()

    with quickDissolve
    Narrator "Meanwhile..."
    play music loosen_up_longhope_song fadeout 5.0

    scene BG Empty Street Day
    camera:
        camera_zoom(z=-500,x=-140,y=200)

    show atlas:
        xcenter 0.5
        yoffset -150

    show robbie:
        xcenter 0.3
        xoffset -300
        yoffset 150
        matrixtransform RotateMatrix(0, 0, 100)

    python:
        adjustChar("Atlas",eye=2)
        adjustChar("Robbie",eye=5,mouth=3)

    with Dissolve(0.5)
    $musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)

    Narrator "Facedown in the dirt is the self-proclaimed frog prince, sprawled out  like he's giving the earth a hug. A lone zucchini rests within claws reach, a weapon perhaps? This is starting to feel like a crime scene."
    voice atlas_heyyouok
    Atlas "Hey, you okay?"

    Narrator "Craning his head to one side, Rob opens his glossy fish eyes and squints up at the bug staring down at him."

    voice atlas_maybehesoverheating
    Atlas "Maybe he's overheating?"

    show atlas:
        ease 0.4 xcenter 0.45
        block:
            ease 0.2 xoffset -20
            ease 0.2 xoffset 0
            pause 0.2
            repeat 2
            ease 0.4 xcenter 0.5

    Narrator "Atlas reaches over and touches Robbie's fluffy hat. The fishman doesn't budge."

    camera:
        camera_zoom(z=-500,x=-140,y=200)

    show atlas:
        pause 0.75
        ease 0.75 xcenter 0.55

    show robbie:
        parallel:
            pause .2
            ease 1.5 xoffset 0
        parallel:
            ease 1.5 matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            ease 1.6 yoffset -150

    $adjustChar("Robbie",eye=5,mouth=3)
    Narrator "He plucks the hat off the fishman."

    $adjustChar("Atlas",feelers=1,eye=1,armL=1)
    extend "\n\nRobbie rips the hat out of Atlas' grasp, and plops it onto his head."
    python:
        adjustChar("Atlas",feelers=2,eye=3,armL=1)
        adjustChar("Robbie",mouth=1)

    show robbie:
        xoffset 0
        yoffset -150
        matrixtransform rotated()
        ease 0.1 yoffset 0

    show atlas:
        xcenter 0.55
        ease 0.1 yoffset 0

    camera:
        camera_zoom(z=-300,x=-140,y=-30,t=0.1)
        camera_shake_off(-140)

    Robert "What are you doing?!"

    python:
        adjustChar("Atlas",feelers=0,eye=1,eyeFrame=5)
        adjustChar("Robbie",mouth=0)

    Atlas "I thought you were dying! Are you alright?"

    $adjustChar("Robbie",eye=2,mouth=3)
    Robert "Oh."
    $adjustChar("Robbie",eye=1,mouth=7)

    show robbie:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0, 0.0, -7) yoffset -20

    Robert "I tripped. You see these webbed feet? They're shit. I'm like an ugly, featherless penguin."

    show robbie:
        matrixtransform RotateMatrix(0, 0.0, -7)
        ease 0.4 matrixtransform RotateMatrix(0, 0.0, 0) yoffset 0

    Narrator "Rob straightens up before slouching back down again."

    $adjustChar("Atlas",feelers=1,eye=5,eyeFrame=0,armL=0)
    Atlas "I hear ya, all I've got are these wings and chicken legs."

    $adjustChar("Robbie",eye=5,mouth=0)
    Narrator "He eyes the mothman and frowns."

    $adjustChar("Robbie",mouth=1,eye=0)
    Robert "So you're a cosplayer?"

    $adjustChar("Robbie",mouth=0)
    pause 0.4
    $adjustChar("Atlas",feelers=2,eye=18)

    Atlas "What?"

    $adjustChar("Robbie",eye=0,mouth=2)
    Robert "'Cause that's one striking interpretation of the mothman."
    python:
        adjustChar("Atlas",feelers=1,eye=19)
        adjustChar("Robbie",eye=4,mouth=7)

    show robbie:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0.0, 19)

    Robert "Wasn't he some sensationalized hoax?"
    python:
        adjustChar("Atlas",eye=18)
        adjustChar("Robbie",eye=3,mouth=1)

    extend "\n\nBut hey, whatever sells bumper stickers!"
    python:
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Atlas",feelers=1,eye=21)

    show atlas:
        hoppies(xIntensity=4)

    Atlas "You can't sling words like that around!"

    $adjustChar("Robbie",mouth=1)
    show atlas:
        ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, 5.0)

    Robert "{b}Hoax?{/b}"
    python:
        adjustChar("Atlas",feelers=1,eye=13,eyeFrame=2)
        adjustChar("Robbie",mouth=0)

    Atlas "{size=35}YES!{/size} \n\nIt's insulting. I'm standing right here!"

    $adjustChar("Atlas",feelers=0,eye=21,eyeFrame=0)
    Atlas "And stand up straight!"
    python:
        adjustChar("Atlas",feelers=2,eye=2,eyeFrame=2)
        adjustChar("Robbie",eye=4,mouth=7)

    show robbie:
        matrixtransform RotateMatrix(0.0, 0.0, 19.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0.0, -5)

    Robert "So it's not a costume."

    $adjustChar("Robbie",eye=3,mouth=3)
    Robert "Woah."
    python:
        adjustChar("Atlas",feelers=1,eye=19,eyeFrame=0)
        adjustChar("Robbie",eye=0,mouth=3)

    show atlas:
        ease 0.15 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        ease 0.5 xcenter 0.6 matrixtransform RotateMatrix(0.0, 180.0, -15.0)

    Atlas "Have you been living under a rock?"
    python:
        adjustChar("Robbie",eye=1,mouth=2)
        adjustChar("Atlas",feelers=1,eye=0,eyeFrame=0)

    Robert "A rock under a rock."

    $adjustChar("Atlas",eye=1,eyeFrame=5,feelers=1)
    Atlas "I see."
    $adjustChar("Robbie",mouth=0,eye=2)

    show atlas:
        xcenter 0.6
        yoffset 0
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, -15.0)
        ease 0.5 xcenter 0.55 matrixtransform RotateMatrix(0.0, 0.0, 0.0)


    Atlas "Wanna talk over coffee while I catch you up to speed?"
    python:
        adjustChar("Atlas",eye=16,eyeFrame=0,sparkle=1,feelers=0)
        adjustChar("Robbie",eye=3,mouth=3)

    extend "\n\n{bt=3}You seem like a real fish out of water.{/bt}"

    $adjustChar("Robbie",eye=0,mouth=5)
    Robert "Okay."

    $adjustChar("Atlas",feelers=0,eye=7,sparkle=0)
    Madhouse "-then I said,, Terry get outta town!"
    $adjustChar("Atlas",feelers=1,eye=19)

    Robyn "Who knew opossums could be so chatty."

    python:
        adjustChar("Atlas",feelers=0,eye=18,eyeFrame=0)
        adjustChar("Robbie",eye=3,mouth=0)

    Madhouse "{sc=2}HAH!{/sc} Only when it's gossip."

    camera:
        camera_zoom(z=-130,x=-80,t=1.0)

    python:
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Robyn",eyes=2,mouth=0,brow=0)
        adjustChar("BM",face=1)

    show robbie behind atlas:
        ease 0.75 xcenter 0.2

    show atlas:
        xcenter 0.55
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            ease 0.75 xcenter 0.3
        parallel:
            pause 0.45
            ease 0.3 matrixtransform rotated(y=180)

    show robyn:
        xcenter 1.0
        matrixtransform RotateMatrix(0,180,0)
        ease 2 xcenter 0.6

    show blobhouse:
        xcenter 1.0
        matrixtransform RotateMatrix(0,0,0)
        ease 2 xcenter 0.7
        idleFloat(2,10)

    Robyn "Hey Atlas!"
    python:
        adjustChar("BM",face=6)
        adjustChar("Atlas",feelers=1,eye=13)
        musicPlayer.playSong(song="not_so_spooky_song")

    Madhouse "{bt=3}What's up Flyboy?{/bt}"

    $adjustChar("Atlas",feelers=3,eyeFrame=2)
    Atlas "{sc}...{/sc}{nw}"
    python:
        adjustChar("Atlas",feelers=0,eye=6,eyeFrame=0)
        adjustChar("Robbie",eye=3,mouth=3)
        adjustChar("Robyn",eyes=3,mouth=0,brow=1)
        adjustChar("BM",face=1)

    extend "\n\nJust chillin' with my good buddy!"

    $adjustChar("Robbie",eye=2,mouth=2)
    Robert "Hello."
    $adjustChar("Robyn",eyes=1,mouth=5,brow=0)

    Narrator "You look at the ghost expectantly. He's going to say something,, and you know it can't be good."

    show blobhouse:
        matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 1.5 xcenter 0.45
        parallel:
            idleFloat(2,10)

    python:
        adjustChar("BM",face=8)
        adjustChar("Robbie",eye=0)
    Madhouse "Atlas, I-., I just wanted to say..."
    python:
        adjustChar("BM",face=7)
        adjustChar("Robbie",mouth=0,eye=4)
        adjustChar("Robyn",eyes=0,mouth=1,brow=1)

    show blobhouse at startledSquish:
        xcenter 0.45
        idleFloat(2,10)

    extend "\n\n{size=40}What a rebound! You got a thing for green guys in hats?{/size}"


    $adjustChar("Atlas",feelers=1,eye=8)
    Atlas "Th-"
    python:
        adjustChar("BM",face=4)
        adjustChar("Atlas",feelers=0,eye=9)
        adjustChar("Robbie",eye=0,mouth=7)

        musicPlayer.playSong(fadeOut=2)
    voice atlas_darkwatcherinterview
    extend "\n\nThat was a question from your {i}Darkwatcher{/i} interview wasn't it?"

    show blobhouse at startledSquish:
        idleFloat(2,10)

    python:
        adjustChar("BM",face=10)
        adjustChar("Atlas",feelers=1,eye=8)

    Madhouse "{sc=2}I-It was?{/sc}"
    python:
        adjustChar("Atlas",feelers=3,eye=9)
        adjustChar("Robbie",eye=5,mouth=0)
    voice atlas_youthoughtiwouldntnotice
    Atlas "And you thought I wouldn't notice?\n\n{sc}Pffsh, kehehee-{/sc}"
    python:
        musicPlayer.playSong("urgently_jammin_song")

        adjustChar("Atlas",feelers=0,eye=10)
        adjustChar("BM",face=5)
        adjustChar("Robbie",eye=1)

    camera:
        shaded("#acffab")
        camera_zoom(z=-300,x=-100)
        camera_shake_off(-100)


    show robyn:
        xcenter 0.6

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        idleFloat(2,10)

    show atlas:
        xcenter 0.3
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 15.0)
    voice atlas_mikesouttamaterial
    P_Atlas "{bt=3}Looks like Mike's out of material!{/bt}"

    Narrator "Atlas' eyes flicker a sharp green with a faint glow."
    $adjustChar("Atlas",feelers=2,eye=15,armL=2)
    voice atlas_youlookterrible
    P_Atlas "You look terrible! Your face is gonna get stuck like that y'know. Have you been taking care of yourself?"
    voice atlas_ariddlewouldperk
    P_Atlas "Oh I know!{nw}"
    python:
        adjustChar("BM",face=13)
        adjustChar("Atlas",eye=11,feelers=1,armL=1,armR=1)
        adjustChar("Robbie",eye=0,mouth=3)

    show blobhouse:
        matrixtransform rotated(y=180)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2,10)

    show atlas:
        parallel:
            hoppies_flipped(xIntensity=4)
        parallel:
            startledSquish

    extend "\n\nA riddle would perk you right up!"
    $adjustChar("Atlas",eye=10,feelers=0,armL=1,armR=1)

    show atlas:
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 15.0)

    Madhouse "Is this a prank?"
    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        ease 0.5 xcenter 0.3 matrixtransform RotateMatrix(0.0, 180.0, -5.0)

    P_Atlas "No?"
    $adjustChar("Atlas",feelers=0,eye=10)

    show blobhouse:
        disappear(0.3)

    Madhouse "Then piss off!"
    hide blobhouse

    python:
        adjustChar("Atlas",feelers=0,eye=10,armL=0,armR=0)
        adjustChar("Robbie",eye=3,mouth=0)
        adjustChar("Robyn",eyes=1,mouth=5,brow=3)

    P_Atlas "{bt=3}You got it boss!{/bt}"

    $adjustChar("Robyn",eyes=2,mouth=1,brow=2)
    show robyn behind atlas:
        xcenter 0.6
        ease 0.5 xcenter 0.45

    #Narrator "You clap your hand onto Atlas' shoulder, giving him a hearty shake."

    #Robyn "Atlas, you okay?"
    #Okay this is too muted of a response
    Robyn "{sc=3}{b}ATLAS.{/b}{/sc}"
    $adjustChar("Atlas",eye=11,feelers=1,armL=2,armR=0)

    show atlas:
        ease 0.5 yoffset 15 matrixtransform RotateMatrix(0.0, 180.0, 5.0)

    P_Atlas "Yeah, yer gonna wanna call a doctor for this guy. \n\nOr a priest!"

    show atlas:
        ease 0.5 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, -5.0)

    $adjustChar("Atlas",eye=11,feelers=0,armL=1,armR=1)
    P_Atlas "I'd do it myself but, I can't figure out how to open doors!"
    camera screens:
        matrixcolor TintMatrix("#ff7e7e")*SaturationMatrix(0)
        ease 0.5 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(1)

    voice atlas_hurtb
    $adjustChar("Atlas",eye=10,feelers=1,armL=1,armR=1)
    show atlas:
        ease 0.15 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, -5.0)
        ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 10.0)
        ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, -6.0)
        ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Atlas "E{nw}"
    play music loosen_up_longhope_song fadeout 5.0

    python:
        musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)

        adjustChar("Atlas",feelers=1,eye=8,armL=0)
        adjustChar("Robbie",eye=2,mouth=7)

    camera:
        parallel:
            camera_zoom(z=-200,x=-80,t=0.5)
        parallel:
            matrixcolor TintMatrix("#acffab")
            ease 0.3 matrixcolor TintMatrix("#ffffff")

    extend "u g h."
    $adjustChar("Atlas",feelers=1,eye=5,armL=0)
    show atlas:
        ease 0.5 xcenter 0.4 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn:
        ease 0.5 xcenter 0.6


    Narrator "With a yelp, Atlas' eyes twitch and shift back to a bright red."
    python:
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Atlas",feelers=3,eye=5)

    #Robert "What was that?"
    python:
        adjustChar("Robyn",eyes=0,mouth=4,brow=1)
        adjustChar("Robbie",eye=3,mouth=3)

    Robyn "We're taking you to the clinic. Rob get 'em!"
    python:
        adjustChar("Atlas",feelers=0,eye=3)
        adjustChar("Robbie",eye=0)
        adjustChar("Robyn",eyes=1,mouth=1,brow=2)

    show atlas:
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Atlas "Bad idea!"
    python:
        adjustChar("Atlas",eye=1)
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Robyn",eyes=0,mouth=5,brow=0)

    Atlas "You know Edith experiments on people,, right?"

    $adjustChar("Atlas",eye=13)
    Atlas "In the hospital basement."
    python:
        adjustChar("Robbie",eye=3,mouth=1)
        adjustChar("Atlas",eye=0)

    show robbie:
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    Robert "{size=40}No way.{/size}"
    python:
        adjustChar("Atlas",feelers=1,eye=6)
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Robyn",eyes=0,mouth=5,brow=0)

    Atlas "So unless you wanna see me pinned to a corkboard,, I'd advise against it."
    python:
        adjustChar("Robyn",eyes=4,mouth=4,brow=2)
        adjustChar("Atlas",feelers=0,eye=13)

    Robyn "I dunno,, that feels like a stretch. Do you have any proof?"
    show robbie behind atlas:
        ease 1.4 xcenter 0.45
    show atlas:
        pause 1.0
        ease 0.5 xcenter 0.35

    python:
        adjustChar("Atlas",feelers=0,eye=1)
        adjustChar("Robyn",eyes=1,mouth=1,brow=0)
        adjustChar("Robbie",eye=1,mouth=5)

    Robert "I dare you to sneak down there and see for yourself."

    $adjustChar("Atlas",feelers=1,eye=16,armL=2)
    Atlas "Hm."
    python:
        adjustChar("Atlas",feelers=1,eye=18,armL=0)
        adjustChar("Robyn",eyes=2,mouth=5,brow=0)
        adjustChar("Robbie",eye=0,mouth=0)

    Atlas "Sounds boring."

    $adjustChar("Atlas",eye=19)
    Atlas "I'm interested in phantoms not Frankensteins."

    python:
        adjustChar("Robbie",eye=3,mouth=2)
        adjustChar("Robyn",eyes=2,mouth=0,brow=0)
    Robyn "What if you visited Goatma'am? She knows a thing or two about ghosts."
    python:
        adjustChar("Robbie",eye=0,mouth=7)
        adjustChar("Atlas",feelers=0,eye=6,armL=0,armR=0)

    show atlas at startledSquish

    Atlas "That's not a bad idea!"

    python:
        adjustChar("Robbie",eye=0,mouth=7)
        adjustChar("Atlas",feelers=1,eye=8,armL=1,armR=0)

    Atlas "You should donate Madhouse to her collection of antiquity!"

    python:
        adjustChar("Robyn",eyes=1,mouth=5)

    Robyn "No."

    python:
        adjustChar("Robbie",eye=0,mouth=7)
        adjustChar("Atlas",feelers=0,eye=16,armL=0)

    Atlas "Ah don't worry, I'm just jokin'!"
    python:
        adjustChar("Robbie",eye=0,mouth=0)
        adjustChar("Atlas",feelers=3,eye=13,armL=0)
        adjustChar("Robyn",eyes=2,mouth=0)
    Atlas "I'll talk to Goatma'am after I run some errands."

    $adjustChar("Atlas",feelers=0,eye=6,sparkle=1)
    Atlas "I've gotta prove I'm the greatest stay-at-home ratman around!"

    $adjustChar("Atlas",feelers=1,eye=0,armL=0,sparkle=0)
    Atlas "Lest I be banished to the crawlspace."

    jump Ch1_GraveyardExploration
