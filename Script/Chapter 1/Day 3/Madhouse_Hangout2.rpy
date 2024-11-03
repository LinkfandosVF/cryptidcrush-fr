# Hangout 2
label Madhouse_Hangout2:
    play music pleasant_conversation_song fadeout 2.0
    python:
        songText = "Pleasant Conversation"
        timeText = "Afternoon"

    scene BG Sky Day

    #show screen EmoteChanger("Robyn",0.0,0.0)
    #show screen EmoteChanger2("MM",0.5,0.0)

    camera at camera_default:
        camera_zoom(z=-400,x=250,y=-20)
        shaded("#fee3eb")

    python:
        adjustChar("Robyn",eyes=3,brow=0,mouth=0)
        adjustChar("MM",mouth=0,eyes=1,armR=2,armL=2)

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

    Robyn "What's next? I guess we should head home for now."
    $adjustChar("Robyn",eyes=1,mouth=3)
    Robyn "I need a nap."

    Madhouse "Home huh?"
    python:
        adjustChar("MM",mouth=9,eyes=3,armL=0,armR=0)
        adjustChar("Robyn",eyes=4)
    voice mm_yohoholaugh
    show madhouse at startledSquish
    Madhouse "When you put it that way, would that make it my home too?{nw}"
    menu:
        extend ""

        "Yes":
            python:
                adjustChar("Robyn",mouth=0,eyes=2)
                adjustChar("MM",mouth=5,eyes=1)
            Robyn "It's better than being alone."
            python:
                adjustChar("Robyn",brow=1,eyes=4,mouth=5)
                adjustChar("MM",mouth=10,eyes=7)
            Robyn "And, you're a pretty nifty nightlight."
            $adjustChar("MM",eyes=9,mouth=1,armR=3,armL=2,blush=1)
            voice mm_damagedb
            Madhouse "{sc}...{/sc}"
        "No":
            python:
                adjustChar("Robyn",brow=2,eyes=1,mouth=1)
                adjustChar("MM",mouth=1,eyes=4,armR=1,armL=2)
            Robyn "Let's not be hasty, you're a haunt, not a roommate."
            python:
                adjustChar("Robyn",brow=2,eyes=4,mouth=1)
                adjustChar("MM",mouth=6,eyes=11,armR=1,armL=2)

            Madhouse "{sc=1}That is., fair.{/sc}"
            pass

    $adjustChar("MM",eyes=-1,mouth=0,armR=2,armL=2,blush=0)
    voice mm_normieah
    Madhouse "Hopefully it won't last too much longer. I wouldn't wanna overstay my welcome."
    python:
        adjustChar("Robyn",brow=2,eyes=4,mouth=4)
        adjustChar("MM",mouth=2)

    Robyn ".,Where will you go next?"
    python:
        adjustChar("Robyn",brow=2,eyes=4,mouth=5)
        adjustChar("MM",mouth=3)
    Madhouse "Hrmgh."

    python:
        adjustChar("MM",mouth=11,eyes=3,armL=0,armR=0)
        adjustChar("Robyn",mouth=5,eyes=0,brow=1)
    show madhouse:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish

    voice mm_laughh

    Madhouse "{bt=2}I'll possess a marionette, and join the circus!{/bt}"
    show madhouse:
        ease 0.5 yoffset 0 matrixtransform rotated(y=180) yzoom 1 xzoom 1 xoffset 0
        idleFloat(2.2,10)
    python:
        adjustChar("MM",mouth=9,eyes=-1,armL=2,armR=2)
        adjustChar("Robyn",mouth=0,eyes=4,brow=0)

    Madhouse "After years of preforming, I'll romance the ringmaster's heir, and stage a coup with the clowns.\n\n"

    python:
        adjustChar("MM",mouth=11,eyes=0,armL=1,armR=1)
        adjustChar("Robyn",mouth=3)

    extend "Then overthrow the king of fools!"

    Madhouse "Once the confetti settles and the clowns come home, I'll ride into the night on the back of a shetland pony."

    Robyn "Yeah? And what's your stage name?"

    python:
        adjustChar("MM",mouth=9,eyes=3,armL=0,armR=0)
        adjustChar("Robyn",mouth=5,eyes=4,brow=0)

    Madhouse "Spindles, the flammable man!"

    $adjustChar("Robyn",mouth=6,eyes=3,brow=1)
    Robyn "Pfft, pahaha!"
    python:
        adjustChar("MM",mouth=0,eyes=0,armL=2,armR=2)
        adjustChar("Robyn",mouth=0,eyes=4,brow=0)

    Madhouse "What about you? What'll you do once I'm gone?"
    $adjustChar("Robyn",mouth=3,eyes=1,brow=2)
    Robyn "I'd be happy to have my phone back."
    $adjustChar("Robyn",mouth=0,eyes=2)
    Robyn "But I'd miss you too."
    $adjustChar("Robyn",mouth=1,eyes=1,brow=3)
    show robyn at unflipCharDelayed(0.7,0.5)
    Robyn "So you'd better promise to write me when you leave!"

    $adjustChar("MM",mouth=9)
    Madhouse "Keheh!"
    python:
        adjustChar("MM",mouth=0,eyes=11)
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
    Madhouse "I doubt they got cell service where I'm goin'."

    python:
        adjustChar("MM",mouth=0,eyes=0)
        adjustChar("Robyn",mouth=0,eyes=2,brow=0)
    show robyn at flipCharDelayed(0.7,0.5)

    Narrator "You wonder what to say next.{nw}"

    $mm_questions = [True,True,True]
    call Ch1_MM_Hangout_Loop from _call_Ch1_MM_Hangout_Loop

    return

label Ch1_MM_Hangout_Loop:
    menu:
        extend ""

        "I dreamt about you" if mm_questions[0]:
            python:
                mm_questions[0] = False
            $adjustChar("Robyn",mouth=4,eyes=0,brow=0)
            Robyn "I dreamt about you last night."

            python:
                adjustChar("MM",mouth=11,eyes=0,armL=0,armR=0)
                adjustChar("Robyn",mouth=1,eyes=1,brow=0)
            show madhouse:
                parallel:
                    hoppies(xIntensity=2)
                parallel:
                    startledSquish

            voice mm_laughh

            Madhouse "Woahoho! That's not something you'd typically tell a guy!"
            show madhouse:
                ease 0.5 yoffset 0 yzoom 1 xzoom 1 xoffset 0
                idleFloat(2.2,10)

            Robyn "Yeah, I mean, I think it was you! Same voice and smile, but... You had a heartbeat. \n\n Like you were {i}normal.{/i}"
            python:
                adjustChar("MM",mouth=6,eyes=2,armL=2,armR=2)
                adjustChar("Robyn",mouth=5,eyes=4,brow=0)

            Narrator "Madhouse has a dopey grin glued to his face."
            python:
                adjustChar("Robyn",mouth=4,eyes=1,brow=3)
            Robyn "What?"
            python:
                adjustChar("MM",mouth=7,eyes=5)
                adjustChar("Robyn",mouth=3,eyes=4,brow=0)

            Madhouse "You were thinking about me."
            show robyn at unflipCharDelayed(0.7,0.5)
            python:
                adjustChar("MM",mouth=5)
                adjustChar("Robyn",mouth=4,eyes=1,brow=3)
            Robyn "Mike this is serious!"
            python:
                adjustChar("MM",mouth=9,armR=1,armL=1,eyes=10)
                adjustChar("Robyn",mouth=3,eyes=1,brow=2)

            Madhouse "Was I handsome?"
            python:
                adjustChar("Robyn",mouth=7,eyes=4,brow=2)

            Robyn "Well,.,{nw}"
            $adjustChar("MM",mouth=4,eyes=5,armR=2,armL=2)

            extend " in a sense?"
            python:
                adjustChar("MM",mouth=1,eyes=4)
                adjustChar("Robyn",mouth=5,eyes=2)

            Narrator "This is getting nowhere. He doesn't remember what happened."

            Narrator "You hardly remember what happened. What's with people falling into your dreams? You'd toss it up as a fluke, but it felt so real."

            Madhouse "Is it bugging you that much?"

            Robyn "Kinda! You seemed really upset about something."
            show madhouse at flipCharDelayed(0.7,0.5)
            Madhouse "Hmmmgh, sorry, I don't remember anything."

        "Can I wear your hat" if mm_questions[1]:
            python:
                mm_questions[1] = False
            python:
                adjustChar("MM",mouth=0,eyes=0,armR=2,armL=2)
                adjustChar("Robyn",mouth=5,brow=0,eye=4)
            Madhouse "This hat? It's straight ectoplasm baby! It'll melt the second it touches your head."

            Madhouse "You'll just haveta wait for the real thing. \n\nBut you're welcome to try!"

            Robyn "Mmm, I'll pass."

        "Who's {color=#FC7979}{b}Debbie{/b}{/color}" if mm_questions[2]:
            python:
                mm_questions[2] = False
                adjustChar("MM",mouth=3,eyes=0)
                adjustChar("Robyn",mouth=5)
                musicPlayer.playSong(fadeOut=1.5)
            call dice_roll(rMod=PC_Stats.cStats("charm"), rDiff=8, rDesc="Persuasion") from _call_dice_roll_84
            show madhouse at unflipCharDelayed(0.7,0.5)
            camera:
                shaded("#fee3eb")
            if isRollSuccess:
                $adjustChar("MM",mouth=1,eyes=11)
                Narrator "Madhouse seems put off by the question."
                show madhouse at vibratenum

                python:
                    adjustChar("Robyn",mouth=5,eyes=0,brow=1)
                    adjustChar("MM",mouth=5,eyes=1,armR=0,armL=0)
                    musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=1.5)

                Madhouse "Only the greatest person in the whole wide world!"

                Narrator "He bounced back fast."
                voice mm_laughawkward
                Madhouse "She made me, {i}me{/i}!"
                python:
                    adjustChar("Robyn",brow=0,eyes=4)
                    adjustChar("MM",mouth=9,eyes=-1,armL=3,armR=2)
                voice mm_whocares
                Madhouse "Sure she indirectly {b}killed{/b} me, and {b}ruined{/b} my life, but who frickin' cares!"
                python:
                    adjustChar("MM",mouth=1,eyes=5)
                    adjustChar("Robyn",mouth=1,eyes=3,brow=2)

                Robyn "Ruined your life?"
                python:
                    adjustChar("MM",mouth=0,eyes=0,armL=2)
                    adjustChar("Robyn",brows=0,eyes=1)
                show madhouse at flipCharDelayed(0.7,0.5)

                Madhouse "Debbie managed our sponsorship deals. She slid me my first case of Toxic Waste!"
                show madhouse at vibratenum
                $adjustChar("MM",mouth=0,eyes=8)

                Madhouse "It was love at first sight."
                $adjustChar("MM",mouth=9,eyes=7)
                show madhouse at vibratenum
                voice mm_laughb
                Madhouse "{bt=3}We were a match made in heaven!{/bt}"
                $adjustChar("MM",mouth=11,eyes=6,armL=0,armR=0)
                show madhouse at startledSquish
                voice mm_laughk
                Madhouse "{sc=3}{b}Nothing else mattered!!{/b}{/sc}"
                $adjustChar("Robyn",mouth=0,eyes=2)
                Robyn "Well, it sounds like she meant a lot to you."

                python:
                    musicPlayer.playSong(song="drink_it_song",fadeOut=1,fadeIn=3)
                    adjustChar("MM",mouth=9,eyes=5,armL=1,armR=1)
                show madhouse at unflipCharDelayed(0.7,0.5)
                Madhouse "Maaaan, if I could get my slimy mitts on another can. Ohohoho, I'd be quenched."
                $adjustChar("Robyn",mouth=5,eyes=1)
                Robyn "Can?"

                $adjustChar("MM",mouth=11,eyes=0)

                Madhouse "{bt=3}CAN!{/bt}"
                $musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=1.5)
                python:
                    adjustChar("MM",mouth=0,eyes=1,armL=2,armR=2)
                    adjustChar("Robyn",brow=1,eyes=0,mouth=4)
                Robyn "I thought you were talking about Debbie!"
                python:
                    adjustChar("Robyn",brow=3,eyes=1,mouth=1)
                show robyn at vibratenum
                extend "\n\nNot a gross ass energy drink! What's wrong with you?"
                python:
                    adjustChar("MM",mouth=1,eyes=7)
                    adjustChar("Robyn",brow=1,eyes=2,mouth=5)
                show madhouse at startledSquish
                Madhouse "You think I care about some chick who frickin' left me to die?!"
                show madhouse at vibratenum
                python:
                    adjustChar("MM",mouth=6,eyes=1)
                    adjustChar("Robyn",brow=0)
                Madhouse "{sc=2}She's off doin' her own thing. And I support her!{/sc}"

                $adjustChar("Robyn",eyes=1,mouth=5)
                Robyn "Sure doesn't sound like it."

                show madhouse at vibratenum
                python:
                    adjustChar("MM",mouth=12,eyes=0,armR=0,armL=0)
                    adjustChar("Robyn",brow=0,mouth=1)

                Madhouse "I pour my heart out to you and this is how you treat me? Blargh!"

                python:
                    adjustChar("MM",mouth=1)
                    adjustChar("Robyn",brow=1,eyes=3,mouth=0)
                Robyn "Yes."
                $adjustChar("MM",mouth=0,eyes=1,armL=2,armR=2)
                Madhouse "Tch!"
            else:
                Narrator "Madhouse looks surprised, a lingering sadness in his empty eyes. He shakes his head."
                python:
                    adjustChar("MM",mouth=1,eyes=5)
                    adjustChar("Robyn",brow=1,eyes=2,mouth=5)
                Madhouse "Just some sad pile of cans."

        "Let's get going":
            Robyn "C'mon."
            python:
                adjustChar("MM",mouth=0,eyes=0)
                adjustChar("Robyn",brow=1,eyes=3,mouth=0)
            Robyn "Let's get going."

            $mm_questions = [False,False,False]

    if True in mm_questions:
        jump Ch1_MM_Hangout_Loop
    return
