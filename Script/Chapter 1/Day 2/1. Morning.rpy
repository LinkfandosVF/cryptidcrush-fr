label Ch1_Day2Wakeup:
    scene BG Apartment Day

    python:
        musicPlayer.playSong(song="undead_icebreakers_song")
        timeText = "7:00AM"

    camera:
        camera_default
        camera_shake

    play sfx hurt_b

    extend "\n\nYou fall out of bed."

    nvl hide
    window show
    with Dissolve(0.5)

    Narrator "Laying on the floor, you stare up at the ceiling, your heart racing in your chest."
    nvl clear

    #Madhouse "Slept well?"

    #Mikey Signal
    #Robyn "There." #More sass. could be a "Do I look like I did?"

    Narrator "You hear a knock at the door."

    Robyn "Hrmgh."

    Narrator "And another knock at the door."

    Taro "Are you going to get that?"

    Narrator "Absolutely fuming, you leap to your feet, march through the kitchen and glare through the peephole."

    Narrator "Whoever it is, they're blocking the peephole."

    Narrator "You open the door."

    Jamie "Good morning."

    Narrator "You're., relieved it's a friendly face,, but irked at being woken up at such an early hour."

    Robyn "Couldn't you've just texted me?"

    Jamie "I felt like any more texts might be rude, since your phone is now home to a ghost."

    Robyn "Mike's not a digipet."

    #Narrator "Your phone buzzes in your pocket."

    #Madhouse "[PCname], I need fooood!"

    Jamie "Can I come in? I brought breakfast."

    Narrator "Jamie reaches into their day bag and pulls out a fragrant loaf of pumpkin bread, alongside a plate of muffins. \n\nYou look at the muffins."

    Robyn "All is forgiven."
    scene BG Apartment Kitchen

    python:
        adjustChar("Jamie",eye=3,armR=1,brow=3)
        adjustChar("Robyn",mouth=5)

    camera:
        camera_zoom(z=-200,y=-50)

    show robyn:
        matrixcolor TintMatrix("#fee3eb")
        xcenter 0.3

    show jamie:
        matrixcolor TintMatrix("#fee3eb")
        xcenter 1.5
        ease 2 xcenter 0.7

    with nwDissolve(0.75)

    Narrator "You step aside letting the devil into your apartment. Jamie's horns clonk against the doorframe as they walk inside."

    Jamie "I want to write August a sympathy card."

    python:
        adjustChar("Robyn",eyes=4,brow=2)
        adjustChar("Jamie",eye=0)

    Narrator "Jamie strolls through the kitchen and places their bag on the table. Reaching inside, they pull out a fistful of markers and a blank card."

    Robyn "That’s a not a bad idea!"

    python:
        Jamie_State["eye"] = 1
        xOption = 0

    Jamie "But, where do I start?{nw}"
    menu:
        extend ""

        "With a drawing?":
            python:
                adjustChar("Robyn",eyes=2,brow=1,mouth=6)
                xOption = 1

            Robyn "A picture is worth a thousand words. Just draw whatever's in your heart!"

            Jamie "My heart?"
            python:
                adjustChar("Jamie",brow=0,armR=4)

            show robyn:
                ease 1 xcenter 0.7
                matrixtransform RotateMatrix(0,0,0)
                ease 0.5 matrixtransform RotateMatrix(0,180,0)

            show jamie:
                matrixtransform RotateMatrix(0,0,0)
                ease 1 xcenter 0.5
                ease 0.6 yoffset 100 matrixtransform RotateMatrix(0,0,-15)

            Narrator "Squatting down, Jamie pops the lid off one of the markers and begins drawing on the card."
            $Robyn_State["mouth"] = 3

            show robyn:
                matrixtransform RotateMatrix(0,180,0)
                ease 2 xcenter 0.55
            Narrator "You try peeking over Jamie's shoulder at the doodle but they sheepishly block your view."

            Robyn "Can I see it?"

            Jamie "Not yet."
            show robyn:
                ease 1 xcenter 0.7

            show jamie:
                yoffset 100 matrixtransform RotateMatrix(0,0,-15)
                ease 0.6 matrixtransform RotateMatrix(0,0,0) yoffset 0

        "Write a poem!":
            python:
                adjustChar("Robyn",eyes=2,brow=1,mouth=6)
                xOption = 2

            Robyn "Everyone loves poetry. Why not give it a shot? I'm sure he’d appreciate the gesture."

            $adjustChar("Jamie",brow=0,armR=4)
            Jamie "I'll give it a try."

            show robyn:
                ease 1 xcenter 0.7
                matrixtransform RotateMatrix(0,0,0)
                ease 0.5 matrixtransform RotateMatrix(0,180,0)

            show jamie:
                matrixtransform RotateMatrix(0,0,0)
                ease 1 xcenter 0.5
                ease 0.6 yoffset 100 matrixtransform RotateMatrix(0,0,-15)

            Narrator "While you're busy eating muffins, Jamie, after several attempts, scrawls out the perfect poem to capture their remorse."

            show robyn:
                matrixtransform RotateMatrix(0,180,0)
                ease 2 xcenter 0.55

            Narrator "You lean over to take a peak, but the devil quickly pulls the card away and slips it into the envelope."
            show robyn:
                ease 1 xcenter 0.7

            show jamie:
                yoffset 100 matrixtransform RotateMatrix(0,0,-15)
                ease 0.6 matrixtransform RotateMatrix(0,0,0) yoffset 0

        "Let me do it.":
            python:
                Robyn_State["eyes"] = 2
                xOption = 3

            Robyn "No offense, but it might be best if I wrote it."

            $adjustChar("Jamie",armR=0,mouth=4,sweat=True)
            Jamie "That would be a card from you, not me."

            $adjustChar("Robyn",armR=1,mouth=6)
            Robyn "You can still sign it."

            $adjustChar("Jamie",mouth=0,brow=0)
            Narrator "Jamie scowls."

            $Robyn_State["armR"] = 0
            Robyn "It'll be a card from both of us!"
            show jamie:
                matrixtransform RotateMatrix(0,0,0)
                ease 0.25 yoffset 30 matrixtransform RotateMatrix(0,0,-7)
                ease 0.25 yoffset 0 matrixtransform RotateMatrix(0,0,0)

            Jamie "Fine."
            $Jamie_State["sweat"] = False

            show robyn:
                matrixtransform RotateMatrix(0,0,0)
                ease 0.6 yoffset 100 matrixtransform RotateMatrix(0,0,15)

            show jamie:
                yoffset 0
                matrixtransform RotateMatrix(0,0,0)
                ease 0.6 yoffset 100 matrixtransform RotateMatrix(0,0,-15)

            Narrator "In a bit of a rush, you jot down a few words of sympathy before scribbling down a doodle of yourself with Jamie holding a bundle of flowers."

            Narrator "Great! You fold the card and place it into the envelope, handing it off to Jamie who places it into their coat pocket."
            show robyn:
                yoffset 100 matrixtransform RotateMatrix(0,0,15)

                ease 0.6 matrixtransform RotateMatrix(0,0,0) yoffset 0

            show jamie:
                yoffset 100 matrixtransform RotateMatrix(0,0,-15)
                ease 0.6 yoffset 0 matrixtransform RotateMatrix(0,0,0)

    $adjustChar("Robyn",eyes=2,brow=1,mouth=3)
    Jamie "Perfect, we should be good to go."

    Robyn "Do you know where August lives?"

    $adjustChar("Jamie",mouth=0,eye=2)

    Jamie "Mmhm, we can walk there together. He lives just up the road."


    $adjustChar("Robyn",eyes=0,brow=0,mouth=5)
    Robyn "Sure! We can talk car damages on the way."
    python:
        adjustChar("Jamie",armR=1,eye=4,mouth=2,sweat=1)
        adjustChar("Robyn",eyes=4)

    show jamie:
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    Jamie "The muffins weren't enough?"
    jump Ch1_AugustCheckup_ToGus

default xOption = 1
label Ch1_AugustCheckup_ToGus:
    scene BG Cabin

    camera at camera_default:
        camera_zoom(z=-200)
        shaded("#FFDDCD")

    python:
        musicPlayer.playSong(song="boots_on_the_shore_bearsome")
        timeText = "8:30AM"

        adjustChar("Robyn",eyes=3,mouth=5,brow=3)
        adjustChar("Jamie",eye=3,mouth=0,armR=4)

    show jamie:

        xcenter 1.5
        ease 2.5 xcenter 0.7

    show robyn:

        matrixtransform RotateMatrix(0,180,0)
        xcenter 1.5
        pause 0.5
        ease 2.5 xcenter 0.5

    with pixellate
    Robyn "I thought you said it was just up the road! Not a {sc}hike.{/sc}"

    Jamie "Would you prefer we drive?"
    python:
        adjustChar("Robyn",eyes=1,mouth=4,brow=0)
        adjustChar("Jamie",eye=1,sweat=0,armR=0)

    Robyn "In that death machine? I wouldn't trust driving it across the street!"

    $adjustChar("Jamie",eye=2,mouth=5)
    Jamie "It's not {i}that{/i} broken."
    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("Jamie",eye=1,mouth=0)
        adjustChar("August",brow=2,armR=0,armL=1)

    Narrator "August's cabin is exactly how you'd expect. In the middle of the woods, rustic, overgrown, but sturdy. \n\nThe furniture on the porch looks hand carved, potted ferns resting on each step leading to the front door."

    Narrator "The only thing out of place is August, shovel in hand, digging a big hole."
    python:
        adjustChar("Robyn",eyes=0,mouth=5,brow=0)
        adjustChar("Jamie",eye=3,brow=0)
        adjustChar("August",brow=2,eye=2,mouth=5,sweater=0,hair=1)

    #show august:
        #matrixtransform rotated(z=10)
        #xcenter 0.3
        #parallel:
        #    yoffset 700
        #    ease 2 yoffset 0
        #parallel:
        #    xoffset -20
        #    pause 1.25
        #    ease 1 xoffset 0
        #parallel:
            #pause 1.25
            #ease 1.0 matrixtransform rotated()


    show august:
        xcenter -0.1 matrixtransform rotated()
        ease 0.9 xcenter 0.3

    Narrator "As the two of you approach, August hops up and calls out to a kid kicking woodchips in the nearby flowerbed."
    voice august_gonnagetsplinters
    python:
        adjustChar("August",mouth=3,brow=4,eyeFrame=1)
        adjustChar("Robyn",eyes=2)

    August "{size=30}Junebug you're gonna get splinters!{/size} \n\nWhy don't you come over and say hi?"

    $August_State["mouth"] = 0
    June "{size=30}I'm busy!{/size}"

    #$adjustChar("August",eyeFrame=2,brow=2,eye=1,mouth=5)
    #Narrator "August sighs."

    voice august_morning
    $adjustChar("August",armR=1,armL=1,mouth=1,brow=2,eye=3,eyeFrame=5)
    August "Morning."
    python:
        adjustChar("Robyn",eyes=3,mouth=0)
        adjustChar("August",mouth=0,eyeFrame=0)

    Robyn "Look who's back to normal! How're you feeling?"
    python:
        adjustChar("August",armR=0,armL=0,eye=2,mouth=2)
        adjustChar("Jamie",eye=2)
        adjustChar("Robyn",eyes=4)

    August "Just peachy."

    show jamie behind robyn:
        ease 1.0 xcenter 0.58

    August "If you're looking for Atlas he's asleep in the attic."

    $adjustChar("Robyn",eyes=1,mouth=3)
    Robyn "Atlas lives in your attic?"

    python:
        adjustChar("Jamie",eye=1,armR=1,brow=0)
        adjustChar("August",eyeFrame=2,eye=3,brow=2,mouth=5)
        adjustChar("Robyn",eyes=2)

    August "Well, attic might be the wrong word, it's more a loft. \n\nWe got fairy lights and everything."
    python:
        adjustChar("Jamie",eye=1,armR=1,brow=0)
        adjustChar("August",eyeFrame=0,eye=2)
        adjustChar("Robyn",mouth=0)

    Robyn "Oh! That sounds lovely."

    $adjustChar("Jamie",brow=0,eye=3)
    Jamie "Atlas is a serial couch surfer. He’ll crash wherever he can fit his feelers into."
    voice august_ohboy
    $adjustChar("August",eye=4,eyeFrame=0,armR=1,armL=2,brow=2,mouth=2)
    August "Bahah! The lad’s down on his luck, that's all."
    python:
        adjustChar("Jamie",eye=4,armR=2)
        adjustChar("August",armR=0,armL=1,mouth=2)

    Jamie "You called him a pest."
    python:
        adjustChar("August",eye=1,eyeFrame=2,mouth=7,brow=1,armL=0)
        adjustChar("Robyn",eyes=1,mouth=5)
    voice august_disappointed
    August "Yeah, I shouldn’t have said that."
    python:
        adjustChar("Jamie",eye=3,brow=0)
        adjustChar("Robyn",eyes=4,mouth=0)

    Robyn "How'd you get stuck with Atlas anyway?"
    python:
        adjustChar("August",eyeFrame=0,eye=0,mouth=0,armR=0,armL=0)
        adjustChar("Jamie",eye=1)
        adjustChar("Robyn",eyes=2)

    August "He's an old family friend!"

    $adjustChar("August",eyeFrame=0,mouth=2,eye=4)
    August "We're happy to have him."

    $adjustChar("August",eye=1,eyeFrame=2,mouth=5)
    Narrator "..."

    # $adjustChar("Robyn",eyes=3,brow=1,mouth=4)
    # Narrator "You break the silence by declaring-"
    python:
        adjustChar("August",eye=3,eyeFrame=0,mouth=5,brow=2)
        adjustChar("Jamie",eye=3,armR=4)
        adjustChar("Robyn",eyes=3,brow=1,mouth=4)

    show robyn:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    Robyn "We brought you a card and pumpkin bread!"

    $August_State["mouth"] = 2
    $Robyn_State["mouth"] = 6

    August "Oh wow! This smells great! And a card too?"

    $adjustChar("Jamie",eye=2,mouth=4)

    Jamie "Yes, please open it."
    $Jamie_State["mouth"] = 0
    $August_State["mouth"] = 1

    show jamie:
        ease 1.0 xcenter 0.5

    show robyn:
        ease 0.6 xcenter 0.6

    August "That's awfully kind of you."

    $August_State["mouth"] = 5

    Narrator "Tearing open the envelope, August pulls out the get well card and opens it."

    #CHECKPOINT
    if xOption == 1:
        python:
            adjustChar("August",eye=1,eyeFrame=1,armR=0,armL=0,mouth=6,brow=1)
            Robyn_State["brow"] = 2

        Narrator "August’s eyebrows furrow as he stands there staring down at the little card, a concerned look on his face."

        show CGShade
        show CG Jamie_Card

        August "Are you... bleeding out your eyes?"

        Jamie "If that's how you interpret it."

        Robyn "Who's the lil blue guy on your head?"

        Jamie "That's my soul!"
        python:
            adjustChar("August",eye=3,mouth=2)
            Jamie_State["mouth"] = 2

        August "Damn. I didn't know you were a baker and an artist! That's so cool!"
        hide CGShade
        hide CG Jamie_Card

        Narrator "Jamie grins."
    elif xOption == 2:
        $adjustChar("August",eye=1,eyeFrame=1,armR=0,armL=0,mouth=1,brow=1)
        August "Ah…"

        Jamie "I do hope my handwriting is legible."

        $August_State["eye"] = 2
        August "I’m at a loss for words..."

        $Robyn_State["brow"] = 2
        Robyn "What’s it say?"

        $August_State["eye"] = 0
        August "It’s a bunch of runes."
        python:
            adjustChar("Jamie",armR=3,eye=0)
            adjustChar("Robyn",eyes=0,mouth=3)

        Narrator "Jamie is stunned silent."

        Jamie "It’s supposed to be a poem."

        Narrator "The devil looks horribly embarrassed, steam practically rolling off their face."

        Jamie "Nevermind, don’t read it."

        Narrator "August chuckles and closes the card."

        $adjustChar("August",eye=3,mouth=2)
        August "No worries. It’s the thought that counts, right?"

        Jamie "It was a sweet poem, I swear."
    else:
        show CGShade
        show CG Robyn_Card

        $adjustChar("August",eye=4,mouth=2)
        August "Wow, this is from the both of you? It’s very cute."

        Jamie "I just signed it."

        Narrator "Jamie grumbles."

        Robyn "Glad you like it!"

        hide CGShade
        hide CG Robyn_Card

    Narrator "August chuckles, tucking the card into his back pocket."
    python:
        adjustChar("August",mouth=1,eye=2,eyeFrame=0)
        Jamie_State["mouth"] = 0

    August "Thanks you two."
    camera:
        camera_zoom(z=-400,t=0.75)

    show jamie:
        ease 0.75 yoffset 75

    show august:
        ease 0.75 xcenter 0.4

    show robyn:
        ease 0.75 xcenter 0.55
    show june zorder 0:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 1.5
        ease 6 xcenter 0.3
    python:
        adjustChar("August",armR=1,armL=2,brow=2,eye=4,mouth=2)
        adjustChar("Jamie",alFace=True,armR=0,blush=1,wispEyes=1)
        adjustChar("Robyn",brow=2,mouth=6,eyes=3)

    Narrator "August throws an arm around you and Jamie, giving you both a friendly side hug."
    python:
        adjustChar("August",armR=0,armL=1,eye=3,mouth=5)
        adjustChar("Robyn",armR=0,eyes=2,mouth=0)

    camera:
        camera_zoom(z=-200,t=0.75)

    show jamie:
        ease 0.75 yoffset 0

    show august behind blobhouse zorder 1:
        ease 0.75 xcenter 0.3

    show robyn zorder 1:
        ease 0.75 xcenter 0.6

    Robyn "Hope you get better soon."
    python:
        adjustChar("Jamie",blush=0,alFace=0,armR=3,eye=7)
        Robyn_State["brow"] = 0

    show robyn:
        xcenter 0.6
        ease 0.15 xoffset -10
        ease 0.15 xoffset 0
        pause 0.1
        ease 0.15 xoffset -10
        ease 0.15 xoffset 0

    Narrator "You give Jamie a gentle nudge."
    python:
        adjustChar("Jamie",eye=6,armR=0,wispEyes=3,mouth=2)
        adjustChar("Robyn",eyes=0,mouth=1)
        August_State["eye"] = 1

    show jamie:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    Jamie "Yea{sc}ACK!{/sc}"

    camera:
        camera_zoom(z=-600,y=250,t=0.75)

    show june:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.3
        ease 0.5 xcenter 0.45
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        yoffset 0
        parallel:
            ease 0.6 matrixtransform RotateMatrix(0,-180,0)
        parallel:
            ease 0.3 yoffset -30
            ease 0.3 yoffset 0

    show robyn:
        ease 0.75 xcenter 0.65

    Narrator "Jamie jumps and angrily looks around only to realize it's a puny red haired girl yanking on their tail."
    show june:
        yoffset 0
        xcenter 0.45
        matrixtransform RotateMatrix(0,180,0)
        ease 0.4 matrixtransform RotateMatrix(0,0,0)

    Narrator "She looks up at Jamie and asks—"
    $June_State['mouth'] = 1

    June "Is that a mask?"
    $June_State['mouth'] = 0

    Jamie "No, it's my skull."

    June "{sc=2}Is your brain in there?{/sc}"

    Jamie "It should be."

    June "Can I see?"

    Jamie "I would die."

    August "Hey, you rascal! This is my daughter June."

    $June_State['mouth'] = 1
    show june:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    June "Did you know octopuses have nine brains? In their arms!"

    Narrator "June kicks the devil's shin."

    $June_State['mouth'] = 0

    June "Tag you're it!"
    $June_State['mouth'] = 1

    show june:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.4 matrixtransform RotateMatrix(0,180,21)
        ease 1.5 xcenter -0.5

    Narrator "She runs off, yelling and flailing her arms around."
    camera:
        camera_zoom(z=-200,t=1.5)

    show jamie:
        ease 0.15 yoffset -40
        ease 0.15 yoffset 0

    python:
        adjustChar("Robyn",eyes=4,mouth=5,brow=0)
        adjustChar("Jamie",mouth=1,sweat=1,armR=4)
        adjustChar("August",brow=2,eye=2,mouth=5)

    Jamie "Wuah!? I'm sorry for scaring you!"
    python:
        adjustChar("August",mouth=1,eye=3)
        Jamie_State["mouth"] = 2

    August "Have you ever played tag? \n\nYou're supposed to chase her around."
    python:
        adjustChar("Robyn",mouth=0,eyes=3)
        adjustChar("August",mouth=8,eye=4)

    Robyn "Yeah! It's all in good fun."


    $adjustChar("August",mouth=5,eye=0)
    Jamie "O.,kay. Sure, that sounds easy enough."

    $Robyn_State["eyes"] = 2
    Jamie "I can have fun."

    python:
        adjustChar("Robyn",mouth=0,brow=0)
        adjustChar("August",mouth=8,eye=2)
        Robyn_State["brow"] = 2

    show jamie:
        ease 2 xcenter -0.5

    August "Eh, they'll be fine."

    Narrator "Glancing at the large shovel August is leaning against, you raise an eyebrow. There’s no shrubs or saplings around needing to be planted."

    hide jamie

    $adjustChar("Robyn",mouth=3,brow=1)
    Robyn "What’s with the hole?"

    $adjustChar("August",eye=3,eyeFrame=2,armL=0,mouth=1)
    August "I'm doing some yard work."

    $adjustChar("Robyn",eyes=1,brow=0,mouth=0)
    Robyn "Uh-huh."

    $adjustChar("August",eye=2,eyeFrame=4,brow=1)
    August "I find it relaxing!"

    $adjustChar("Robyn",eyes=4,brow=3)
    Robyn "This feels like a werewolf thing."
    python:
        adjustChar("August",eyeFrame=3,mouth=2,brow=0,eye=0)
        Robyn_State["brow"] = 0

    August "I’m certain it’s a normal human thing."
    python:
        Robyn_State["eyes"] = 1
        adjustChar("August",eye=3,mouth=5)

    Robyn "Maybe if you’re a gravedigger."

    python:
        musicPlayer.playSong(song="not_so_spooky_song")

        adjustChar("August",eye=1,mouth=6,eyeFrame=0,brow=2)
        adjustChar("Robyn",mouth=5,eyes=0)
        BM_State['face'] = 2

    show august behind blobhouse:
        xcenter 0.3
        ease 0.6 xcenter 0.23

    show blobhouse:
        xcenter 0.45
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        startledSquish
        idleFloat(2.2,12)

    voice mm_gravedigger
    Madhouse "{size=35}Gravedigger?!{/size}{nw}"
    camera:
        pause 0.65
        camera_shake

    python:
        adjustChar("August",armR=1,armL=2)
        BM_State['face'] = 2

    show august behind blobhouse:
        matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            pause 0.1
            ease 0.5 yoffset 700
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0, 0, -180)
        parallel:
            ease 0.5 xcenter .15

    play sfx ["<silence .65>", "audio/SFX Battle/Hurt_B.ogg"]
    play voice2 ["<silence .65>", "audio/Voice/August/Battle/August_DamagedA.ogg"]
    Narrator "August tumbles into the hole."
    python:
        BM_State['face'] = 6
        Robyn_State["mouth"] = 1

    voice mm_beefyboy
    Madhouse "Get a load of this beefy boy digging around in the dirt!"

    show blobhouse:
        startledSquish
        idleFloat(2.2,12)

    $BM_State['face'] = 1
    voice mm_itsgreattomeetcha
    extend "\n\nIt's great to meet ya bud!"

    voice august_yourehaunted
    August "{size=40}\nYou're haunted?!{/size}"

    $adjustChar("Robyn",mouth=4,eyes=1)
    Robyn "Double haunted, actually."

    voice august_andyoureokwiththis
    August "{size=30}And you're okay with this?{/size}"

    $adjustChar("Robyn",mouth=0,eyes=3)
    Robyn "For now at least."

    python:
        adjustChar("Robyn",mouth=5,eyes=4)
        adjustChar("August",armR=0,armL=0,eye=1,mouth=6,eyeFrame=2,brow=0)
        BM_State['face'] = 9

    show blobhouse:
        startledSquish
        idleFloat(2.2,12)

    voice mm_laughh
    Madhouse "I can't believe a werewolf's fallen for me."

    show blobhouse:
        startledSquish
        idleFloat(2.2,12)

    show august behind blobhouse:
        xcenter 0.0
        matrixtransform RotateMatrix(0, 0, 180)
        yoffset 900

        parallel:
            pause 0.5
            ease 1.2 xcenter 0.3
        parallel:
            ease 1.5 matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            ease 1.6 yoffset 0

    $BM_State['face'] = 6
    Madhouse "Did I come on too strong?"

    python:
        August_State["eye"] = 2
        Robyn_State["eyes"] = 2

    Narrator "August hoists himself up out of the pit, rubbing his back while he winces."
    $BM_State['face'] = 4

    show august:
        yoffset 0 xcenter 0.3
        matrixtransform RotateMatrix(0, 0, 0)

    August "Oh, no I got the message."
    python:
        BM_State['face'] = 9
        adjustChar("Robyn",mouth=0,eyes=3)

    Robyn "August, meet Madhouse Mike. He's., a lot."

    $adjustChar("August",eye=1,mouth=5,eyeFrame=0,brow=2)
    voice august_liketheradioguy
    August "Like the radio guy?"
    $Robyn_State["eyes"] = 2

    voice mm_ghostinneed
    Madhouse "I’m a ghost in need of a man with a shovel—"
    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        idleFloat(2.2,12)

    $adjustChar("BM",face=5,arms=1)
    voice mm_waityourememberme
    extend "\n\nWait,, you remember me?"
    python:
        adjustChar("August",eye=2,mouth=6,eyeFrame=4,brow=1)
        Robyn_State["mouth"] = 5

    voice august_paranormalstuff
    August "Vaguely,, but that paranormal stuff makes me queasy,, so I try to avoid it."

    python:
        adjustChar("August",eye=0,mouth=5,eyeFrame=0)
        adjustChar("BM",face=7,arms=0)
        adjustChar("Robyn",brow=2,eyes=4)

    voice mm_that
    Madhouse "{sc=3}That—{/sc}"
    show blobhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2.2,12)

    python:
        BM_State['face'] = 1
        adjustChar("Robyn",mouth=3,eyes=2,brow=0)
        adjustChar("August",eyeFrame=2,eye=3)

    voice mm_thatsokay
    Madhouse "That's okay. \n\nIt's not for everyone."

    $BM_State['face'] = 4
    August "One sec."
    camera at camera_shake
    show august behind blobhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    python:
        adjustChar("August",mouth=2,armL=1,brow=2,eyeFrame=0,eye=4)
        adjustChar("Robyn",mouth=0,eyes=0,brow=1)
        musicPlayer.playSong()

    August "{size=40}Junebug! Time to get ready for school!"
    python:
        musicPlayer.playSong("urgently_jammin_song")
        adjustChar("August",brow=0,eye=1,mouth=4,eyeFrame=3,armR=0,armL=2)
        BM_State['face'] = 3

    August "JUNE! No biting!"

    $adjustChar("August",eyeFrame=5,mouth=6,brow=1)
    Jamie "{sc}Help me.{/sc}"

    show august behind blobhouse:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.3
        ease 2 xcenter -.5

    show blobhouse:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform rotated()
        idleFloat(2.2,12)

    python:
        musicPlayer.playSong(song="not_so_spooky_song",fadeOut=1.0,fadeIn=1)
        adjustChar("Robyn",mouth=5,eyes=2,brow=2)
    Robyn "What {i}is{/i} your plan exactly?"

    camera:
        camera_zoom(z=-400,x=70,t=1)

    $BM_State['face'] = 1
    Madhouse "You're gonna find my body and my hat too! That bastard’s gotta have it."

    $adjustChar("Robyn",eyes=1,mouth=1)
    Robyn "Mike, that feels wrong."

    Robyn "Is this really how you'll find closure?"

    Madhouse "Sure, if closure involves shovels and felonies."

    show robyn:
        xcenter 0.65
        matrixtransform RotateMatrix(-5,180, -5)
        ease .5 xcenter 0.58

    $adjustChar("Robyn",brow=3,eyes=3)
    Robyn "We're not doing that!"

    python:
        BM_State['face'] = 7
        Robyn_State["eyes"] = 0

    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        camera_shake
        idleFloat(2.2,12)

    Madhouse "FINE!"

    Madhouse "I'll do it {i}myself.{/i}"

    $BM_State['face'] = 4
    Madhouse "Gimme your phone."
    show robyn:
        xcenter 0.58
        matrixtransform RotateMatrix(-5,180,0)
        ease .5 xcenter 0.6

    $adjustChar("Robyn",eyes=4,mouth=4)
    Robyn "I'm not giving you my phone."

    $BM_State['face'] = 7
    $Robyn_State["mouth"] = 5

    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.05 xoffset -5
        block:
            parallel:
                idleFloat(2.2,12)
            parallel:
                ease 0.1 xoffset 5
                ease 0.1 xoffset -5
                repeat

    Madhouse "{sc=5}GrrRRRRGHHH!{/sc}"
    $BM_State['face'] = 8

    show blobhouse:
        idleFloat(2.2,12)

    Madhouse "Okay."

    $adjustChar("Robyn",brow=2,eyes=2)
    Robyn "Look Mike, I know you're desperate,, but you can't force people to do what you want."

    show robyn:
        xcenter 0.6
        matrixtransform RotateMatrix(-5,180,-10)
        ease .5 xcenter 0.57

    $adjustChar("Robyn",brow=3,eyes=1,mouth=4)

    Robyn "Like drinking., {color=#3bec27}poison.{/color}"

    $Robyn_State["mouth"] = 5
    $BM_State['face'] = 7

    Madhouse "You've got a lot of {b}nerve{/b} {sc=2}{b}{color=#EC2A2A}meatball.{/color}{/b}{/sc}"

    #Robyn "What,, are you gonna rend my soul and set me adrift in the void., {i}again?{/i}"
    #$BM_State['face'] = 8

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2.2,12)

    $BM_State['face'] = 8
    #Madhouse "No."

    show robyn:
        xcenter 0.58
        matrixtransform RotateMatrix(-5,180,0)
        ease .5 xcenter 0.6

    Madhouse "Seriously though,, is Atlas okay?"

    $adjustChar("Robyn",brow=2,eyes=4,mouth=1)
    Robyn "He's alright,, but why don't {i}you{/i} ask him?"

    python:
        BM_State['face'] = 4
        adjustChar("Robyn",eyes=2,brow=0,mouth=3)

    Madhouse "Just shove me in a {sc=2}meat grinder.{/sc}"

    $adjustChar("Robyn",mouth=4,eyes=1)
    Robyn "Don't be so dramatic, dude. If you apologized I'm sure it'd clear the air!"

    python:
        adjustChar("Robyn",mouth=3,brow=3)
        BM_State['face'] = 2

    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.05 xoffset -5
        block:
            parallel:
                idleFloat(2.2,12)
            parallel:
                ease 0.1 xoffset 5
                ease 0.1 xoffset -5
                repeat

    Madhouse "{sc=2}MEAT GRINDER!{/sc}"

    show blobhouse:
        idleFloat(2.2,12)

    $adjustChar("Robyn",eyes=4,brow=2,mouth=5)
    Robyn "Ugh."
    hide august
    hide jamie

    camera:
        camera_zoom(z=-150,t=1)

    python:
        BM_State['face'] = 1
        adjustChar("August",eyeFrame=2,brow=2,mouth=5,eye=3,armL=1,armR=1)
        adjustChar("Jamie",eye=1,mouth=0,sweat=0)
        musicPlayer.playSong(song="boots_on_the_shore_bearsome",fadeOut=1.0,fadeIn=1)

    show jamie behind blobhouse:
        matrixtransform RotateMatrix(0,180,0)
        xcenter -.3
        ease 3 xcenter 0.7
        ease 0.4 matrixtransform rotated()

    show august:
        matrixtransform RotateMatrix(0,0,0)
        xcenter -.5
        ease 2 xcenter 0.25



    August "Welp! Thanks for stopping by you three."
    python:
        Jamie_State["mouth"] = 1
        August_State["armR"] = 0

    Jamie "Not a problem."
    python:
        adjustChar("August",eyeFrame=2,brow=2,mouth=5)
        adjustChar("Robyn",eyes=3,brow=0,mouth=0)
        Jamie_State["mouth"] = 2

    Robyn "Yeah! It's always nice getting to know your neighbors."
    python:
        BM_State['face'] = 9
        Robyn_State["eyes"] = 2
        Jamie_State["mouth"] = 0

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 15.0)
        idleFloat(2.2,12)

    Madhouse "Could you give us a tour of the graveyard, neighbor? Since we're new in town."

    $adjustChar("August",eyeFrame=3,eye=2)
    August "Why there in particular?"
    python:
        adjustChar("Robyn",eyes=1,brow=2,mouth=5)
        BM_State['face'] = 2

    voice mm_laughe
    Madhouse "It's for my spiritual well-being."
    python:
        adjustChar("August",eyeFrame=0,eye=0,mouth=5)
        BM_State['face'] = 1

    August "That is a rather important journey. \n\nI admire a ghost taking charge of his afterlife."
    python:
        Jamie_State["eye"] = 4

    Jamie "{size=20}Yeuck.{/size}"

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        idleFloat(2.2,12)

    python:
        adjustChar("Robyn",brow=4,eyes=4)
        Jamie_State["eye"] = 3
        BM_State['face'] = 1

    Madhouse "See? All I had to do was ask!"

    $adjustChar("Robyn",eyes=1,mouth=3)
    Robyn "{sc=2}Hrmgh.{/sc}"

    $adjustChar("August",mouth=1,eye=4)
    August "I'd be happy to help."
    python:
        adjustChar("Robyn",mouth=4,eyes=0,brow=1)
        adjustChar("August",mouth=0,eye=3)

    Robyn "You're not creeped out?"
    python:
        adjustChar("August",eye=2,eyeFrame=2)
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)

    August "Nah,, I hear it's a great spot for mushroom picking."

    python:
        adjustChar("August",mouth=6,eyeFrame=1,brow=4,eyes=1,armL=1)
        adjustChar("Jamie",eye=0)
    August "Not alone of course, but that's just common sense."


    #August "Dead malls? Now that's creepy!"

    #Robyn "Malls? No way, caves are way scarier. Have you seen how many people go missing?"

    #$adjustChar("Jamie",eye=2,brow=4,mouth=4)
    #Jamie "Elevators frighten me."
    python:
        adjustChar("Jamie",eye=2)
        adjustChar("Robyn",mouth=5,brow=0)
        adjustChar("BM",face=14)

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        idleFloat(2.2,12)
    Madhouse "So it's settled!"

    python:
        adjustChar("August",mouth=2,eye=4,armL=0,armR=1,eyeFrame=0,brow=2)
        adjustChar("BM",face=1)
    August "How about I swing by and pick you up after work? Since it's a bit of a drive."

    show robyn happy
    Robyn "Sounds like a plan."

    python:
        adjustChar("August",mouth=5,eye=3,armL=0,armR=0,eyeFrame=2,brow=2)
        adjustChar("BM",face=6)
        adjustChar("Jamie",eye=1,mouth=0,brow=1,sweat=1)

    Madhouse "What about you Jam slam? Feelin' adventurous?"
    $adjustChar("Jamie",eye=2,mouth=1,brow=2)
    Jamie "As thrilling as creeping around a cemetary sounds, I'll have to pass."
    $adjustChar("Jamie",eye=0,mouth=2,brow=3,armR=1)

    Jamie "I'd feel bad leaving Atlas out."
    scene BG Black
    camera at camera_default:
        camera_zoom()

    with quickDissolve

    Narrator "You decide to take the long way home."
    jump Ch1_AugustCheckup_TessieGoatmaam
