
# Hangout 1
label MM_Hangout1:
    play music pleasant_conversation_song fadeout 2.0
    python:
        songText = "Pleasant Conversation"
        timeText = "EVENING"

    scene BG Sky Night

    camera at camera_default:
        camera_zoom(z=-400,x=250,y=-20)
        shaded("#ebc0f8")

    python:
        adjustChar("Robyn",eyes=3,brow=0,mouth=0)
        adjustChar("MM",mouth=9,eyes=1,armR=0,armL=0)

    show robyn:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 2 xcenter 0.6

    show madhouse:
        xcenter 1.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2 xcenter 0.79
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat

    with Fade(0.5, 0.5, 0.5, color="#000000")

    Madhouse "Y'know, I never realized I could take my hat off. I figured it was fused to my frickin' head."
    python:
        adjustChar("MM",mouth=11,eyes=0,armR=1,armL=1)

    show madhouse at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1
        xcenter 0.79
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat

    Madhouse "This opens a new realm of possibilities!"

    python:
        adjustChar("MM",mouth=9,eyes=1)

    python:
        adjustChar("MM",mouth=1,eyes=2)

    Madhouse "You think they make clothes for ghosts?"

    python:
        adjustChar("MM",mouth=0)
        adjustChar("Robyn",mouth=4,eyes=0,brow=1)

    Robyn "Sure but, how does an outfit die?"

    Madhouse "Shrinking in the drier."

    python:
        adjustChar("MM",mouth=9,eyes=5)
        adjustChar("Robyn",mouth=3,eyes=1,brow=0)

    show madhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0, -10)
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat
    extend "\n\nOr whatever it is you're wearing."

    voice RobynSays("Generic","HmphB")
    $adjustChar("Robyn",mouth=1,eyes=4,brow=3)
    Robyn "Like yours is any better!"
    voice mm_laughc
    python:
        adjustChar("MM",mouth=11,eyes=0)
        adjustChar("Robyn",mouth=5,eyes=0,brow=1)

    show madhouse at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 10.0)
        zoom 1
        alpha 1
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat

    Madhouse "Hey, I'm a craft store halloween prop! What's your excuse?"

    Robyn "Did you design the look yourself?"
    show madhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 10.0)
        ease 0.9  matrixtransform RotateMatrix(0, 0, 0)
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat

    python:
        adjustChar("MM",mouth=9,eyes=5)
        adjustChar("Robyn",mouth=0,eyes=4,brow=0)

    Madhouse "Nah,, it was a collaborative effort with my producer. Do you like it?{nw}"

    menu:
        extend ""

        "I like it!":
            Robyn "It looks good on you! I like it."
            $adjustChar("MM",mouth=11,eyes=0)
            Madhouse "It perfectly contrasts with my slick, sickly green flesh!"

            $adjustChar("MM",mouth=0)

            pause 0.9
            show madhouse at startledSquish: #.Startled Squish
                matrixtransform RotateMatrix(0.0, 180.0, 10.0)
                zoom 1
                alpha 1
            $adjustChar("MM",mouth=1,eyes=0,armL=3,armR=1)
            Madhouse "{sc=3}I just grossed myself out.{/sc}"
            python:
                adjustChar("MM",eyes=0,mouth=3,armL=2,armR=2)
                adjustChar("Robyn",mouth=5,eyes=2,brow=0)
            show madhouse:
                matrixtransform RotateMatrix(0.0, 180.0, 12)
                ease 0.5 matrixtransform RotateMatrix(0, 0.0, -9)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            Madhouse "Bein' dead fuckin' sucks."

            python:
                adjustChar("MM",eyes=10,mouth=9,armL=1,armR=1)
                adjustChar("Robyn",mouth=5,eyes=2,brow=0)

            extend "\n\n{size=40}Shocking I know!{/size}"

            show robyn:
                matrixtransform RotateMatrix(0.0, 180.0, 0)
                ease 0.5 matrixtransform RotateMatrix(0, 0.0, -5)

            Robyn "Are you really dead? Sure, things certainly changed but you're still here. You just look different!"
            python:
                adjustChar("MM",mouth=0,eyes=1,armL=2,armR=2)
                adjustChar("Robyn",mouth=3,brow=1)

            Madhouse "Hm."

            python:
                adjustChar("MM",mouth=6,eyes=0,armR=1,armL=1)

            show madhouse:
                matrixtransform RotateMatrix(0.0, 0.0, -5)
                ease 0.5  matrixtransform RotateMatrix(0, 0, 15)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat

            Madhouse "{bt=3}Breathe that cool, refreshing night air.{/bt}"

            show madhouse:
                matrixtransform RotateMatrix(0.0, 0.0, 15)
                ease 0.5  matrixtransform RotateMatrix(0, 0, -10)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            Madhouse "{bt=3}Feel the earth beneath your boots!{/bt}"

            show madhouse:
                matrixtransform RotateMatrix(0.0, 0.0, -5)
                ease 0.5  matrixtransform RotateMatrix(0, 0, 15)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            Madhouse "{bt=3}Ah, wait.{/bt}"
            show madhouse:
                parallel:
                    hoppies(xIntensity=4)
                parallel:
                    startledSquish
            python:
                adjustChar("MM",mouth=1,eyes=3,armR=0,armL=0)
                adjustChar("Robyn",mouth=5,eyes=0,brow=1)

            Madhouse "{size=45}I CAN'T!{/size}"

            $adjustChar("Robyn",mouth=4,eyes=1,brow=0)

            show madhouse:
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat

            Robyn "Point taken."

            python:
                adjustChar("Robyn",mouth=5,eyes=4,brow=0)
                adjustChar("MM",mouth=2,eyes=0,armL=2,armR=2)

            show robyn:
                matrixtransform RotateMatrix(0.0, 0.0, -5)
                ease 0.6  matrixtransform RotateMatrix(0, 180, 5)

            extend "\n\nNow if you could,, would you wanna live again?"

            python:
                adjustChar("MM",eyes=0,mouth=3)
                adjustChar("Robyn",mouth=5,eyes=2,brow=0)

            Madhouse "...{nw}"

            python:
                adjustChar("Robyn",mouth=5,eyes=2,brow=0)
                adjustChar("MM",mouth=1,eyes=2)

            Madhouse "I don't wanna think about it."

            python:
                adjustChar("MM",mouth=0,armL=1,armR=2)
            Madhouse "I'd rather focus on what I have now."

            python:
                adjustChar("Robyn",mouth=0,eyes=4,brow=0)
            Robyn "Which is a friend?"

            voice mm_woah
            show madhouse at vibrate(t=0.4,x=2):
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat

            python:
                adjustChar("MM",mouth=1,eyes=10,armL=0,armR=0)
            Madhouse "{sc=2}That's a bit much isn't it? Overkill really. I- I mean- \n\nH-have I even earned it?{/sc}"

            python:
                adjustChar("Robyn",mouth=6,eyes=3,brow=1)
                adjustChar("MM",mouth=2,armL=0,armR=0)
            show robyn:
                matrixtransform RotateMatrix(0.0, 180.0, 0)
                ease 0.5 matrixtransform RotateMatrix(0, 0.0, -5)
            Robyn "Sure, I don't see why not."
            python:
                adjustChar("MM",mouth=9,eyes=7,armL=3,armR=2)
            voice mm_laughe
            show madhouse at vibrate(t=0.2,x=2):
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            Madhouse "You're gonna regret that."
            show madhouse at hypersquish:
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            pause 0.2

            #show CG Madhouse Hold Hand Wip
            #with Dissolve(1.0)

            #Narrator "You reach out and take Madhouse's hand. It stings a moment, like a jolt of energy shocking you awake, then gently eases into a dull hum."

            #Narrator "Come to think of it, the ghost glows and gives off a faint buzz when you stand near him. Mike's like a talking battery."

            #Robyn "C'mon let's go home."

        "I like you!":
            show robyn at startledSquish: #.Startled Squish
                matrixtransform RotateMatrix(0.0, 0.0, 5.0)
                zoom 1
                alpha 1
            python:
                adjustChar("MM",mouth=3,eyes=3)
                adjustChar("Robyn",mouth=0,eyes=3,brow=0)
            Robyn "I like the ghoul wearing it!"

            python:
                adjustChar("MM",mouth=1,eyes=1)
                adjustChar("Robyn",mouth=0,eyes=2,brow=1)

            Madhouse "The ghoul with the melted swamp face?{nw}"

            menu:
                extend ""

                "Yep!":

                    python:
                        adjustChar("MM",mouth=11,eyes=0)
                        adjustChar("Robyn",mouth=5,eyes=0,brow=1)

                    Madhouse "{sc}YIKES!{/sc}"
                    python:
                        adjustChar("MM",mouth=5,eyes=5)

                    show madhouse:
                        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                        ease 0.9  matrixtransform RotateMatrix(0, 0, -10)
                        block:
                            ease 2.2 yoffset -12
                            ease 2.2 yoffset 12
                            repeat
                    Madhouse "{bt=2}No wonder you've got such {color=#3bec27}{b}horrible taste!{/b}{/color}{/bt}"

                    pass

                "{b}EVEN MORE.{/b}":

                    python:
                        adjustChar("MM",mouth=9,eyes=10)
                        adjustChar("Robyn",mouth=0,eyes=3,brow=1)

                    voice mm_wellwellwellb
                    Madhouse "{bt=5}Well, well, well!{/bt}\n\nYou're a genuine {color=#3bec27}freakster!{/color}"

                    python:
                        adjustChar("MM",mouth=0)
                    show madhouse:
                        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                        ease 0.9  matrixtransform RotateMatrix(0, 0, -10)
                        block:
                            ease 2.2 yoffset -12
                            ease 2.2 yoffset 12
                            repeat

                    #Madhouse "No wonder you've got such poor taste!"
                    Madhouse "Want me to sign your forehead?"
                    pass


            $adjustChar("Robyn",mouth=1,eyes=1,brow=0)

            Robyn "Mike, I was bein' serious."

            python:
                adjustChar("MM",mouth=3,armL=2,armR=2)
                adjustChar("Robyn",mouth=5,eyes=1,brow=0)
            Madhouse "...{nw}"

            python:
                adjustChar("MM",mouth=1,eyes=0,armL=3)

            extend "\n\nWhat?"
            python:
                adjustChar("Robyn",mouth=4,eyes=4)

            show robyn:
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 0.5  matrixtransform RotateMatrix(0, 180, 5)
            Robyn "I'm struggling to tell what's a joke and what's not with you."

            python:
                adjustChar("Robyn",mouth=5)
                adjustChar("MM",mouth=3,eyes=5,armL=2)

            show madhouse:
                matrixtransform RotateMatrix(0.0, 0.0, -10.0)
                ease 0.5  matrixtransform RotateMatrix(0, 0, 0)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat

            Madhouse "You and me both."

            python:
                adjustChar("MM",mouth=4,armL=1,armR=1)

            Madhouse "Besides,, you could do better than me bud. Raise your standards..,{nw}"
            python:
                adjustChar("MM",mouth=1,eyes=0,armL=3)

            extend "\n\n{size=18}I tried to kill you.{/size}"
            python:
                adjustChar("Robyn",mouth=0,eyes=3,brow=1)
                adjustChar("MM",eyes=4,mouth=1,armL=2,armR=2)

            show robyn:
                matrixtransform RotateMatrix(0.0, 180.0, 5.0)
                ease 0.5  matrixtransform RotateMatrix(0, 0, -5)

            Robyn "That's something we could work on together!"

            python:
                adjustChar("Robyn",mouth=0,eyes=2)
                adjustChar("MM",mouth=2)
            Robyn "Starting with your outfit if you'd like."
            $adjustChar("MM",eyes=0,mouth=9,armL=3)
            voice mm_laughe
            Madhouse "{sc=3}I'm a picky shopper.{/sc}"


            show madhouse:
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 0.5 matrixtransform RotateMatrix(0, 180, 12)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            python:
                adjustChar("MM",mouth=2,eyes=0,armL=3,armR=2,blush=0)
                adjustChar("Robyn",mouth=0,eyes=4,brow=0)

            #Narrator "Madhouse holds out his hand."
            show madhouse:
                matrixtransform RotateMatrix(0.0, 180.0, 12)
                ease 0.5 matrixtransform RotateMatrix(0, 180, -5)
                block:
                    ease 2.2 yoffset -12
                    ease 2.2 yoffset 12
                    repeat
            python:
                adjustChar("MM",mouth=0,armL=2,eyes=8)
                adjustChar("Robyn",mouth=0,eyes=2,brow=0)
            #Madhouse "If you wanna., walk back together."

            #Narrator "You reach out and take Madhouse's hand."

            #show CG Madhouse Hold Hand Wip
            #Narrator "It stings a moment, like a jolt of energy crackling through you, then gently eases into a warm hum. You feel a bit buzzed, your hair standing on end."
            #Narrator "Come to think of it,, the ghost glows and gives off a faint buzz when you stand near him."

            #Madhouse "YEOWCH! You okay?"

            #Narrator "Madhouse flinches but you stand fast, giving his hand a reassuring squeeze. The hell is this guy made out of?"

            #Robyn "Psh, it's no big deal."

            #Madhouse "..."

            #Madhouse ".,Good 'cause I can't let go."

            #Robyn "What."

            #Madhouse "Y-Yeah so you're gonna wanna pry my hand off with a crowbar, vodka and lots of toothpaste."

            #Narrator "He's got to be joking."
    show blobhouse at startledSquish:
        xcenter 0.79 matrixtransform RotateMatrix(0, 0, 25)

    hide madhouse
    stop music
    python:
        adjustChar("BM",face=10,arms=1)
        adjustChar("Robyn",mouth=1,eyes=0,brow=1)
    voice mm_damagedh
    Madhouse "GYEHCK!.,{nw}"
    voice mm_damnit
    $adjustChar("BM",face=13,arms=0)
    show blobhouse:
        matrixtransform RotateMatrix(0, 0, 25)
        ease 0.5 matrixtransform RotateMatrix(0, 180, 15)
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat
    extend "\n\nDammit!"
    Madhouse "..."
    $adjustChar("BM",face=9)
    $adjustChar("Robyn",mouth=0,eyes=2,brow=2)
    show blobhouse:
        matrixtransform RotateMatrix(0, 180, 25)
        ease 0.5 matrixtransform RotateMatrix(0, 0, 0)
        block:
            ease 2.2 yoffset -12
            ease 2.2 yoffset 12
            repeat
    extend "\n\n Phew! I'm., exhausted."

    $adjustChar("BM",face=8)
    $adjustChar("Robyn",mouth=0,eyes=3,brow=2)
    Madhouse "Like, really exhausted."

    show blobhouse:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 1.5 yoffset 250 matrixtransform RotateMatrix(0, 180, 35)

    Madhouse "Like,, really, really..."

    scene BG Black
    show CG MM Hold

    with Dissolve(0.75)

    play music better_days

    Narrator "You scoop Madhouse out of the air and hold him in your arms."

    Narrator "He's soft, slightly gummy to the touch and chilled like a scoop of soft serve. A jolt of electricity buzzes up your arm as your hand brushes his cheek. \n\nWhat's this guy made out of?"

    Robyn "Mike, I., {size=19}really{/size} {size=17}meant{/size} {size=16}it.{/size}"

    Narrator "... He fell asleep just like that? So much for being a ball of ferocious energy."
    return
