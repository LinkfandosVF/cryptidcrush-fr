image CG Oz_Cafe:
    zoom 0.39
    xcenter 0.5
    ycenter 0.5

    "images/CGs/Chapter 1/Oz Cafe.webp"

    on show:
        crop (742,0,0,1856)
        ease 0.5 crop (0,0,1484,1856)

define Bro  = Character("Big Bro", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ffef5e")
label Ch1_Day3Morning:

    $musicPlayer.playSong(song="radioStatic",fadeIn=2,fadeOut=1)
    call Chapter_2_Intro from _call_Chapter_2_Intro

    camera at camera_default
    scene BG Bridge with pixellate

    python:
        musicPlayer.playSong(song="cloudless_rain")
        timeText = "7:00AM"

    play sfx phone_notif
    Narrator "The next morning you decide to stop by the café for breakfast. \n\nYour phone chimes."

    show CG Cellphone
    Bro "Hey Binbin how's it out there in the boonies?"

    Bro "You surviving?"

    Narrator "Ugh, you don't feel like replying. Okay, maybe you'll send a brief text reassuring him that you're alive."

    Robyn "Thriving."

    Bro "Glad to hear it."

    Bro "Once I get enough PTO I'm visiting. No take-backs."

    Robyn "Nuh-uh, that's like a ten hour long trip!"

    Bro "With how I drive? Eight."

    hide CG Cellphone

    Narrator "Bleugh, it's better to just ignore him."

    Narrator "The two of you haven't talked much since the big move. He keeps saying he'll visit,, but work always gets in the way."

    Madhouse "'Ey Meatball! Check this out! Look at what I can do!"

    call Ch1_MadhouseChangesYourPhone from _call_Ch1_MadhouseChangesYourPhone

    $musicPlayer.playSong(song="cloudless_rain",fadeOut=0.5)

    Narrator "Looking up, you find Oz staring out over the horizon. \n\nHe seems lost in thought."

    menu:
        extend ""

        "Approach him":
            Robyn "Enjoying the view?"

            Narrator "Oz nods."

            Narrator "You sit down next to Oz and he glances over."
            show BG Bridge:
                matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1.0)
                ease 2.0 matrixcolor ColorizeMatrix("#162e0a","#daffc7")*SaturationMatrix(0.0)
            show CGShade
            show CG Oz_Cafe

            Narrator "He's relaxed, wearing a fitted white tee, with his work shirt tied around his waist. There's an air of exhaustion about him."

            Narrator "He looks at you, waiting for you to make the first move."

            Robyn "Thanks for the save last night. \n\nYou know your way around a knife. I'm guessing that wasn't your first fight?"

            Narrator "Oz nods weakly."

            Robyn "Yeah, I've had my own run-ins with malicious entities."

            voice oz_huh
            Oz "—?"

            Robyn "I managed a paranormal club back home! \n\nWell, calling it a club is pretty generous, it was really only me, Atlas and a couple of guys."

            voice oz_thinking
            Oz "..."

            Robyn "It's how I met Taro!"

            Robyn "She ate all the Easter candy out of my backpack one finals week."

            voice oz_laughc
            Narrator "Oz chuckles."

            Robyn "Alright, well, I'll see you around!"

            Narrator "As you stand up, Oz lightly tugs your sleeve. You glance back and see him jotting something down."

            scene BG Black with Dissolve(0.5)
            voice oz_ugh

            Narrator "He slides you a slip of paper, and walks off, hands in his pockets."

            Narrator "A note from Oz? What could it be? Your heart begins to race, clutching the paper in your hands."

            Narrator "With great anticipation you unfold the note and read—"

            extend "\n\n{i}{color=#fffb42}You're welcome.{/color}{/i}"

            Narrator "You're not sure what to make of this letter. It could be important, like some kind of clue, or a hidden message. You'd better hold onto it."

        "Continue on":

            Narrator "You decide it'd be best not to bother him."

    jump Ch1_CafeDay3


#NVL MODE
label Ch1_AtlasMorningConvo:
    python:
        timeText = "7:00AM"
        musicPlayer.playSong(fadeOut=1.5)

    scene BG Cabin
    nvl clear
    $musicPlayer.playSong(song="supernatural_serenade_song",fadeIn=1,fadeOut=2)
    nvl show Dissolve(0.3)
    with Dissolve (0.5)

    NVL_Atlas "{size=45}AUGUUUST!{/size}"

    NVL_Narrator "Atlas barges into his housemate's room and spies the hulking heap of fur sprawled out on the bed, his long legs dangling off the mattress. He opens one eye and growls."

    NVL_WolfAugust "{sc=3}{b}Grrrrh.{/b}{/sc}"

    NVL_Atlas "How am I awake before you?"

    NVL_WolfAugust "Because you didn't., sleep."

    NVL_Atlas "Don't you have like., a job?"

    NVL_WolfAugust "Ugh."

    NVL_Atlas "What's wrong?"

    NVL_WolfAugust "It's catching up to me. The {i}{b}queasy{/b}{/i}."

    NVL_Atlas "The {i}supernatural queasy{/i}?"

    NVL_Atlas "Dude, you walked into that one. Seriously, a graveyard first date? You know you're scared of ghosts!"

    NVL_WolfAugust "Just 'cause I'm afraid of somethin' \ndoesn't mean I gotta hide from it."

    NVL_WolfAugust "And it wasn't a date."

    NVL_WolfAugust "We were lookin' for a quirky fella named {color=#3bec27}Mike{/color}."

    NVL_Narrator "Atlas blinks."

    NVL_Atlas "Mike? Did Mike have a grating voice and a bad temper?"

    NVL_Narrator "The wolfman yawns."

    NVL_WolfAugust "Eeyup, your friend seemed to tolerate 'em."

    NVL_Atlas "[PCname] tolerates everybody."

    NVL_WolfAugust "I wish I had that kind of patience."

    camera at camera_shake

    NVL_June "{size=40}{b}PAPA!{/b}{/size}"

    NVL_Narrator "June darts across the room and leaps onto the bed. She climbed the fuzzy mountain of dadness and pounded her tiny fists on his back."

    NVL_WolfAugust2 "Bugabeebee!"

    NVL_Narrator "August sits up, reaches back, plucks June off his mane and gives her a big hug."

    NVL_WolfAugust2 "Look who's all dressed and ready to go. \n\nGood job!"

    NVL_June "I did it all by myself!"

    NVL_June "Mister Crow made breakfast!"

    NVL_Atlas "I tried at least. \n\nC'mon June, let's let him get changed."

    NVL_June "Nooo!"

    NVL_Narrator "June refuses to let go, clinging to August like a baby koala bear."

    NVL_Atlas "{bt=3}I'll race ya.{/bt}"

    NVL_Narrator "Atlas slowly turns away and takes a big step towards the door."

    NVL_June "{sc=14}{b}!!!{/b}{/sc}"

    NVL_Narrator "June hops down and races out of the room, leaving Atlas in the dust."

    NVL_Atlas "Ahaha, aw, she's just like you!"

    NVL_WolfAugust "Oh hush."

    stop music fadeout 0.7

    nvl clear
    scene BG Black with Dissolve(0.5)
    nvl hide

    jump Ch1_Day3Morning

label Ch1_Phone_Video:

    #robyn in bed looking at phone
    scene BG Black

    with Fade(0.1, 0.2, 2.0, color="#FFF")
    python:
        Cameraman = Character("Cameraman", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#7b78ff")
        Beast = Character("???", image = "august", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c") #AUGUSTUS

    show CG August Lost Snow

    Narrator "A man cackles, sounding absolutely psyched as a car door opens, the camera jostling around as he wanders out into the snowfall."

    Cameraman "It took all night but, I finally found it!"

    Cameraman "Found what you may ask?"

    show CG August Lost Paws
    with { "master" : Dissolve(0.4) }
    Narrator "The camera jerks to the left and tilts down, focusing on a trail of five fingered pawprints."

    Cameraman "A very good boy."

    #Narrator "The voices are difficult to parse through the strong wind."

    Cameraman "And big one by the looks of it."
    show CG August Lost Snow
    with { "master" : Dissolve(0.4) }
    camera:
        matrixtransform RotateMatrix(0,180,0)

    Narrator "The stranger presses on, his boots crunching against the snow."

    show CG August Lost Legs
    camera:
        camera_default
        camera_shake

    Cameraman "{sc=5}-!{/sc}"

    Narrator "The camera snaps up."

    show CG August Lost
    with { "master" : Dissolve(0.4) }
    camera:
        matrixtransform RotateMatrix(0,00,0)


    Narrator "A lumbering beast staggers through the shot, dressed in a tattered suit. He stops and turns his head to look at the camera, panting heavily. \n\nHe's hurt."
    Cameraman "{size=30}What a shot!{/size} \n\nHere boy! Look over here boy!"

    Beast "{sc=6}...{/sc}"

    Cameraman "Turn around! Aren't you cold? Hungry?"

    Cameraman "C'mon do {i}something{/i}!"

    pause 0.5

    #Beast "{size=19}{i}Shut up.{/i}{/size}"

    #Cameraman "It., {i}talks{/i}!"

    show CG August Lost Face

    Beast "{sc=3}{size=55}No.{/size}{/sc}"

    show CG August Lost Face
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        matrixtransform RotateMatrix(0,0,180)
        pause 0.2
        matrixtransform RotateMatrix(0,180,0)
        matrixcolor HueMatrix(180)

    show Flickering Black
    pause 0.5
    pause (0.5)

    scene BG Black
    camera default
    Narrator "The tape ends."
    return
