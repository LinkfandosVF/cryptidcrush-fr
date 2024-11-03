default ch1_alreadyMetHound = False

# Hangout 1
label August_Hangout1:
    $musicPlayer.playSong(fadeOut=2)
    scene BG Black
    with dissolve

    Robyn "If you're not doing anything, maybe you could give us a tour of one of your hiking trails?"

    August "Like, right now?"

    Robyn "Sure, why not?"

    Narrator "August is absolutely thrilled. Seems he doesn't get a chance to blab about his work too often."

    scene BG Hill Day

    show august:
        xcenter -0.2
        pause 2.0
        ease 2.0 xcenter 0.4
    show robyn:
        xcenter -0.2
        pause 2.5
        ease 2.0 xcenter 0.25

    camera:
        shaded("#F1CFBE")
        camera_zoom(z=-550,y=-50,x=-250)
        camera_zoom(z=-290,y=-30,x=-180,t=5.0)
    #show screen EmoteChanger("Robyn",0.0,0.0)
    #show screen EmoteChanger2("August",0.5,0.0)

    with nwDissolve(0.5)
    python:
        adjustChar("Robyn",eyes=2,brow=0,mouth=3)
        adjustChar("August",eye=4,brow=2,mouth=2,eyeFrame=0)
        musicPlayer.playSong(song="undead_icebreakers_song",fadeIn=1)
        timeText = "11:00AM"


    Narrator "He's talking a lot. You're trying to keep up with the conversation but find yourself slacking."
    python:
        adjustChar("Robyn",brow=1,mouth=0)
        adjustChar("August",eye=2,brow=2,mouth=5,sweater=1,hair=2,eyeFrame=0)
    Robyn "Does June go to school here?"

    August "Yup, at the old schoolhouse near the shore. It's managed by the Librarians."
    $adjustChar("August",eye=3,brow=2,eyeFrame=2)
    August "I'm not sure what to do with myself now that June's gone during the day."

    Robyn "Sounds like she's in good hands."

    August "I hope so."

    python:
        adjustChar("Robyn",brow=1,mouth=0)
        adjustChar("August",mouth=1,eyeFrame=0,eye=2)

    August "I can't exactly enroll her in a school outside our little bubble."
    $adjustChar("August",brow=1,mouth=2,eyeFrame=4)
    August "Not that I doubt our fine educators!"
    $adjustChar("August",eye=3,mouth=5,eyeFrame=2)
    August "It's... A socializing thing I guess. I don't want her to feel like an outsider."

    August "She's got a lotta problems,, like her old man, and—.,{nw}"
    $adjustChar("August",eye=2,mouth=6,eyeFrame=0,brow=2)
    extend "\n\nOh gosh, you don't need to hear this junk. I'm sorry."

    python:
        adjustChar("Robyn",brow=0,mouth=4)
        adjustChar("August",mouth=5,eyeFrame=2)
    Robyn "It's okay."
    $adjustChar("Robyn",eyes=3,mouth=0)

    Robyn "I'm sure you're a great dad."

    August "I'll get there eventually."
    python:
        adjustChar("Robyn",brow=0,eyes=2)
        adjustChar("August",mouth=5,eyeFrame=2,eye=3)
        gus_questions = [True,True]

    Narrator "You wonder what to say next.{nw}"

    call Ch1_Gus_Hangout_Loop from _call_Ch1_Gus_Hangout_Loop


    Robyn "..."

    python:
        adjustChar("August",mouth=0,eyeFrame=2,eye=2)
        adjustChar("Robyn",mouth=1,brow=2,eyes=4)

    Robyn "How bad's the hospital bill?"
    python:
        adjustChar("August",mouth=3,eyeFrame=0)
        adjustChar("Robyn",eyes=3)

    August "Psh, don't worry about it, we're living under Longhope rules."
    python:
        adjustChar("August",mouth=2,eyeFrame=2,eye=3)
        adjustChar("Robyn",mouth=5,eyes=1)
    August "Like what's Edith gonna do? Kill me? Nah."
    python:
        adjustChar("August",eyeFrame=4,eye=2,brow=4)
        adjustChar("Robyn",brow=1,eyes=2)
    August "Silver bullets are outside their budget."
    python:
        adjustChar("August",mouth=5,eyeFrame=0,brow=2)
        adjustChar("Robyn",brow=2,eyes=3,mouth=1)

    Robyn "Gaaah, don't joke about that!"
    python:
        adjustChar("August",mouth=1,eyeFrame=4,brow=1,eye=3)
        adjustChar("Robyn",brow=2,eyes=1,mouth=5)

    August "Ack, my bad!"
    python:
        adjustChar("August",mouth=6,eyeFrame=2,brow=2,eye=2)
        adjustChar("Robyn",mouth=1)

    August "But seriously, don't worry about it."

    python:
        adjustChar("August",mouth=5)
        adjustChar("Robyn",mouth=5,eyes=4)
    Robyn "Mmnh, okay."

    python:
        adjustChar("Robyn",brow=0,eyes=2)
        adjustChar("August",mouth=5,eyeFrame=0,brow=4,eye=3)

    August "Hang on. I'm picking up on something."
    python:
        adjustChar("Robyn",brow=0)
        adjustChar("August",eye=3)

    show august:
        ease 0.5 xcenter 0.6

    Narrator "August steps off the trail finds a line of footprints. He scratches his chin."
    #(rework)

    $adjustChar("August",mouth=8,brow=0)
    August "Size eleven boots, waterproof. And considering the depth of the print, the wearer must be seven feet tall."

    $adjustChar("Robyn",brow=0,mouth=0)
    Robyn "You can tell all that by looking at a footprint?"
    $adjustChar("August",mouth=2,brow=2)

    show august:
        xcenter 0.6
        flipChar(0.4)
        ease 0.6 xcenter 0.4

    August "Oh, no I made it up."
    $adjustChar("Robyn",brow=1,mouth=0,eyes=1)
    $adjustChar("August",mouth=5,eyeFrame=2,brow=2)

    show august:
        matrixtransform rotated(y=180)
        xcenter 0.4

    show robyn:
        xcenter 0.25
        parallel:
            ease 0.4 xcenter 0.3
            ease 0.4 xcenter 0.25
        parallel:
            rotate 0
            pause 0.2
            ease 0.2 rotate 7
            ease 0.2 rotate 0

    Narrator "You elbow August, who cracks a cheeky grin."

    August "C'mon, let's see where it goes."
    $adjustChar("Robyn",brow=2,eyes=2)

    scene BG Black
    camera:
        camera_default

    python:
        timeText = "10:30AM"
        musicPlayer.playSong(fadeOut=5.0)

    with Dissolve(0.75)
    show CG Gus Walk
    camera:
        camera_zoom(z=200,y=-80,t=1.5)

    Narrator "Following the footprints, you stick close to August as you both wander off the trail. You'd feel uneasy, but August seems to know what he's doing."

    menu:
        extend ""

        "Take his arm.":
            $adjustChar("August",eye=1,eyeFrame=0,brow=2,mouth=5)

            camera:
                camera_zoom(y=-50,x=-80,t=0.8)
            Narrator "You grab the sleeve of August's sweater and hold his arm."

            Robyn "I don't wanna get separated."

        "Continue.":
            pass

    $adjustChar("Robyn",eyes=2,mouth=1)
    Robyn "If there's something out here, shouldn't we be running from it? Not towards it?"

    August "Pah, I'm the scariest thing in these woods!"

    Robyn "Really?"

    August "God, no."

    August "But hey, I could buy you some time! I'm like a four-course meal at least."

    $adjustChar("Robyn",mouth=0)

    Robyn "How heroic."

    scene BG Black
    with Dissolve(0.5)
    camera:
        camera_default

    Narrator "The footprints trail off before vanishing entirely."
    call dice_roll(rMod=0, rDiff=5, rDesc="Perception") from _call_dice_roll_321

    if isRollSuccess:
        $ch1_alreadyMetHound = True
        scene BG Pond at flipped

        camera:
            shaded("#ffd5bd")
            camera_zoom(z=-350,y=-20,x=200)

        show hound:
            xcenter 0.8 matrixtransform RotateMatrix(0,180,0)
            matrixcolor BrightnessMatrix(-1) blur 2
        with nwDissolve(0.5)

        Robyn "Look there!"
        play ambiance forest_ambianceb fadein 4.0 fadeout 4.0

        Narrator "You slow to a stop at the edge of the forest. You spot a lone hiker standing in the sunlight with their back towards you."

        Narrator "You frown. Where did August go? He ditched you?! No way!"
        python:
            adjustChar("Robyn",mouth=5,brow=0)
            houndyell= Character("Stranger", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "11C", who_color = "#ea3c53")
            houndyell2= Character("Hound", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "11C", who_color = "#ea3c53")

        show robyn at enterFromLeft (x=0.5,t=2.0)

        Robyn "Excuse me."

        $adjustChar("Robyn",mouth=0,eyes=3,brow=2)
        Robyn "Did a tall fuzzy guy pass through here?"
        show hound:
            xcenter 0.8
            matrixcolor BrightnessMatrix(-1) blur 2
            ease 0.4 matrixcolor BrightnessMatrix(0) blur 0 matrixtransform RotateMatrix(0,0,0)

        camera at camera_shake:
            camera_zoom(z=-350,y=-20,x=200)

        python:
            adjustChar("Robyn",mouth=5,eyes=0,brow=1)
            adjustChar("Hound",eyeFrame=0)
            musicPlayer.playSong(song="the_unwelcome_visitor")

        houndyell "{size=50}{b}GYAH!{/b}{/size}"

        $adjustChar("Robyn",mouth=1,eyes=3,brow=3)

        Narrator "OW! This freak's too loud! Are they shouting through a speaker?! You nearly had a heart attack!"
        python:
            stranger= Character("Stranger", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "1B", who_color = "#ea3c53")
            adjustChar("Robyn",mouth=5,eyes=1,brow=3)
            adjustChar("Hound",eyeFrame=1)
            musicPlayer.playSong(song="its_off")

        play music its_off_song
        show hound at startledSquish

        stranger "Oh. You're a human!"
        $adjustChar("Hound",eyes=4)

        stranger "Be on your way duckling. It's unwise to wander."
        $adjustChar("Robyn",mouth=4,eyes=2,brow=0)

        Robyn "What's with the out of season halloween costume?"
        $adjustChar("Hound",eyes=2)
        $adjustChar("Robyn",mouth=0,eyes=3,brow=0)

        stranger "My., {size=30}{b}uni.,form.{/b}{/size}"
        $adjustChar("Robyn",eyes=2)

        Robyn "A uniform huh? What do you do?"
        $adjustChar("Hound",eyes=1)

        stranger "Unspeakable things."
        $adjustChar("Hound",eyes=4)

        stranger "I'm under an NDA."

        python:
            adjustChar("Hound",eyes=1)
            adjustChar("Robyn",mouth=5,eyes=2)
        show hound at startledSquish

        stranger "Now, why are you speaking to me?"
        $adjustChar("Robyn",mouth=1,eyes=1,brow=0)

        Robyn "I was asking if you saw a tall fuzzy guy pass by!"

        show august at enterFromLeft (x=0.3,t=1.5) behind robyn
        python:
            adjustChar("August",mouth=5,brow=0)
            adjustChar("Hound",eyes=0)

        stranger "With an obnoxiously ugly red mustache?"

        $adjustChar("Robyn",mouth=1,eyes=2,brow=2)
        Robyn "Yes?"

        python:
            adjustChar("August",mouth=5,eyeFrame=2,eye=1,brow=2)

        camera:
            camera_zoom(z=-150,y=-30,x=100)
        play sfx blip_8a

        Narrator ""

        show hound at flipCharDelayed

        $adjustChar("Hound",eyes=2)
        stranger "Haven't seen him."
        show august:
            ease 0.9 xcenter 0.57
        show robyn at startledSquish:
            ease 0.9 xcenter 0.45
        python:
            adjustChar("August",mouth=2,brow=0,eyeFrame=3,eye=2)
            adjustChar("Robyn",mouth=5,eyes=0,brow=1)
            adjustChar("Hound",eyes=0)
        August "It's the {b}Hound{/b}! What an unpleasant surprise!"
        python:
            adjustChar("August",mouth=5,brow=2,eyeFrame=2,eye=3)
            adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        August "Don't you have a fiancé to crawl back to?"

        $adjustChar("August",mouth=0)
        show hound at unflipCharDelayed
        $adjustChar("Hound",eyes=4)

        Hound "Once I'm done here."

        $adjustChar("Hound",eyes=0)
        $adjustChar("August",brow=0,eyeFrame=2)

        Hound "See,, unlike you Summers,, most of us can hold down a healthy relationship."

        $adjustChar("August",eye=2,eyeFrame=3,mouth=6)

        August "You live in a cave."
        $adjustChar("August",eye=3,mouth=5)
        $adjustChar("Hound",eyes=1,eyeFrame=0)
        show hound:
            parallel:
                hoppies(xIntensity=2)
            parallel:
                startledSquish

        Hound "You prissy homeowners make me sick!"
        $adjustChar("Hound",eyes=0,eyeFrame=0)
        Hound "I'm lucky to own the teeth in my mouth and the scars on my chest!"

        Hound "I've never been happier! Happy, happy, happy!"

        show hound at vibratenum
        $adjustChar("August",eye=3,eyeFrame=2,mouth=1,brow=2)

        August "Are ya done throwing your little tantrum?"

        $adjustChar("August",eye=3,eyeFrame=2,mouth=5)
        $adjustChar("Hound",eyes=4,eyeFrame=1)
        Hound "Fight me city boy."

        $adjustChar("August",eye=2,mouth=6)
        August "Nope. I'm still not interested."

        $adjustChar("Hound",eyes=1)
        Hound "Spineless as usual I see."

        $adjustChar("Hound",eyes=0,eyeFrame=0)
        $adjustChar("August",eyeFrame=0,mouth=5,eye=1)
        Hound "Perhaps you'd feel differently under the light of a fullmoon."

        show hound at flipCharDelayed:
            xcenter 0.8
            ease 3 xcenter 1.5
        $adjustChar("Hound",eyes=0,eyeFrame=0)

        houndyell2 "{bt=3}{i}Bwuooohahaha!{/i}{/bt}"
        $adjustChar("August",eye=1,eyeFrame=2,mouth=6,brow=0)

        houndyell2 "{bt=5}A-AAAWOOOOOOO!{/bt}"

        $adjustChar("August",eye=0)
        August "Ugh."
        $adjustChar("August",eye=2,eyeFrame=2,brow=2)

        Robyn "... You got a lot of enemies huh?"
        scene BG Black
        camera:
            camera_default
        with Dissolve(0.75)
        stop sfx
        stop ambiance
        August "Worse. He's my future in-law."

    else:
        $ch1_alreadyMetHound = False
        Robyn "Look over here!"

        Narrator "A glimmer of metal catches your eye. There's an arrow plunged in an old oak."

        Narrator "Walking over, August rips the arrow out of the tree and examines the point. He flinches, the tip stings his fingers."

        August "A broadhead?"

        Narrator "August combs his fingers through his hair and pauses for a moment."

        Narrator "August perks right back up. He wraps the arrow up in the torn shirt and takes it with him."

        August "No use worrying about that. \n\nLet's head back."
        stop ambiance

    return


label Ch1_Gus_Hangout_Loop:
    menu:
        extend ""

        "Are there bears" if gus_questions[0]:
            python:
                gus_questions[0] = False

            python:
                adjustChar("Robyn",brow=0,eyes=2)
                adjustChar("August",mouth=5,eyeFrame=2,eye=3)

            Robyn "Are there bears?"

            $adjustChar("August",eye=3,mouth=1)
            show august:
                flipChar()

            August "Werebears."

            $adjustChar("August",eye=4,mouth=2,eyeFrame=0)
            August "Lake Teardrop's a popular summer fishing spot. Folks love playing chicken with our lake monster."

            $adjustChar("August",eyeFrame=2,brow=0,mouth=2,eye=1)
            August "See how far can you swim before Tessie gets ya."

            $adjustChar("Robyn",mouth=4,brow=2)
            Robyn "{i}That{/i} Tessie?"

            python:
                adjustChar("August",mouth=1,eyeFrame=1,eye=3,brow=2)
                adjustChar("Robyn",mouth=0,brow=2,eyes=3)
            August "The lake monster."
            python:
                adjustChar("Robyn",mouth=6,brow=3,eyes=3)
                adjustChar("August",mouth=5)

            Robyn "I knew it!"
            python:
                adjustChar("August",mouth=0,eye=3,brow=2)
                adjustChar("Robyn",mouth=4,brow=1,eyes=4)

            Robyn "She had this nautical energy about her."
            python:
                adjustChar("August",mouth=6,eyeFrame=2)
                adjustChar("Robyn",mouth=1,brow=0,eyes=2)

            August "You met her?"

            Robyn "Briefly."

            August "She's a sweetheart."
        "Tell me about Oz" if gus_questions[1]:
            python:
                gus_questions[1] = False
            $adjustChar("Robyn",mouth=4,brow=1,eyes=2)
            Robyn "Do you know what Oz's deal is? His mysterious ways allude me."
            python:
                adjustChar("August",eye=2,mouth=2)
                adjustChar("Robyn",mouth=0,eyes=2,brow=0)
            August "Heh! You and me both."

            $adjustChar("August",eye=3,mouth=1,brow=4)

            August "I've worked with Oz before, begrudgingly, and he knows his stuff. Probably the best medic in Elkhorn."

            August "I just wish he wasn't tied to that doctor."

            python:
                adjustChar("August",eye=0,mouth=5,brow=2)
                adjustChar("Robyn",mouth=5)
            Robyn "You mean Edith?.,\n\n But she seems so-{nw}"
            menu:
                extend ""
                "Cool.":
                    Robyn "Cool."
                    python:
                        adjustChar("August",mouth=6,eyeFrame=4,eye=2,brow=4)
                        adjustChar("Robyn",mouth=1,brow=0,eyes=2)

                    August "That's how she gets ya."
                    python:
                        adjustChar("August",mouth=3,eye=3,brow=1,eyeFrame=2)
                        adjustChar("Robyn",mouth=5,brow=1,eyes=1)

                    August "You lower your guard because she's smart, cute, and highly scoop-able."
                    python:
                        adjustChar("August",mouth=6,eye=0,brow=0,eyeFrame=3)
                        adjustChar("Robyn",mouth=1,brow=1,eyes=0)
                    August "Then she shoves pliers in your mouth!.,{nw}"
                    python:
                        adjustChar("August",mouth=4,eye=3,brow=1,eyeFrame=2)
                        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
                    extend "\n\nAnd I keep falling for it."
                    python:
                        adjustChar("August",mouth=5)
                        adjustChar("Robyn",mouth=4,brow=2,eyes=2)
                    Robyn "Sco.,op-able?"
                    python:
                        adjustChar("August",brow=2,eye=2,mouth=0)
                        adjustChar("Robyn",mouth=5,brow=0)
                    August "M'yeah, I'm bad with words."

                    pass
                "Peculiar.":
                    Robyn "Okay,, no, she is strange."
                    python:
                        adjustChar("August",eye=0,eyeFrame=0)
                        adjustChar("Robyn",mouth=1,brow=1,eyes=4)

                    Robyn "Is everyone in Longhope so peculiar?"
                    python:
                        adjustChar("August",mouth=0,eyeFrame=2,eye=2)
                        adjustChar("Robyn",mouth=0,brow=2,eyes=3)


                    August "Yup. \n\nAnd that includes you buster."

                    August "What's your deal anyway?"
                    python:
                        adjustChar("August",mouth=2,eye=3,brow=4)
                        adjustChar("Robyn",mouth=1,brow=0,eyes=2)

                    August "A lone stranger drifts into town, without a name or a story? That's pretty mysterious."
                    python:
                        adjustChar("August",mouth=5,eye=2,brow=2)
                        adjustChar("Robyn",mouth=4,brow=2,eyes=1)
                    Robyn "Well, prepare to be underwhelmed,, 'cause I'm not that interesting."
                    $adjustChar("Robyn",mouth=5,brow=0,eyes=4)
                    Robyn "It was an impulse decision. Longhope offered an escape and I took it."
                    $adjustChar("Robyn",mouth=7,brow=1,eyes=1)
                    extend "\n\nThat's all."
                    python:
                        adjustChar("August",eyeFrame=3,brow=4)
                        adjustChar("Robyn",mouth=1,brow=0,eye=4)
                    Narrator "August seems unconvinced, but he doesn't press you further."
                    pass
        "Quick! Werewolf question!":
            $gus_questions = [False,False]
            python:
                adjustChar("Robyn",brow=0,eyes=2)
                adjustChar("August",mouth=5,eyeFrame=2,eye=3)
            Robyn "How long have you been a werewolf?"

            $adjustChar("August",mouth=1,eye=2)

            August "Born with it. But it never reared its ugly head until high-school."

            $adjustChar("August",mouth=5)

            August "How long have you known Atlas?"
            python:
                adjustChar("August",eyeFrame=3)
                adjustChar("Robyn",mouth=6,eyes=3)

            Robyn "Since like forever. He smacked into my bedroom window one night and the rest is history."

            $adjustChar("Robyn",mouth=4,brow=1,eyes=2)

            Robyn "How long have you had a beard?"
            python:
                adjustChar("August",eyeFrame=0,mouth=2,eye=1)
                adjustChar("Robyn",mouth=5,brow=0)

            August "The beard's a recent development."
            $adjustChar("August",eyeFrame=2,mouth=1,eye=3)
            August "The moms at June's soccer practice seem to like it. Nobody else does."
            python:
                adjustChar("August",mouth=5)
                adjustChar("Robyn",mouth=1,eyes=4)
            Narrator "You glance at August's left hand. There's no ring."

            Robyn "Is it just you and June?"
            python:
                adjustChar("August",eye=2)
                adjustChar("Robyn",mouth=0,eyes=2)
            August "Yeah, but it ain't so bad. The folks here have been kind to us."
            $adjustChar("August",eyeFrame=0,mouth=2,eye=4)

            August "You moved to the right place."
            python:
                adjustChar("August",mouth=5,eye=2,brow=2,eyeFrame=2)
                adjustChar("Robyn",mouth=4,brow=2,eyes=1)
            Robyn "Y'think so? I'll admit, I've been feeling a bit out of place lately. I dunno how to shake it off."
            python:
                adjustChar("August",mouth=1,eye=0,eyeFrame=0)
                adjustChar("Robyn",mouth=1)
            August "Sounds like you got the new place blues. It'll go away with time."
            python:
                adjustChar("August",mouth=0,eye=2,brow=4)
                adjustChar("Robyn",mouth=5,brow=1,eyes=2)
            August "So, is it just you and... Your haunts?"

            Robyn "Yup."
            python:
                adjustChar("August",mouth=6,eye=0,brow=1,eyeFrame=3)
                adjustChar("Robyn",mouth=1,brow=0,eyes=1)

            August "Yeeesh, I wouldn't be able to sleep knowing a ghost's in the room. Like, don't they drain your life-force?"
            $adjustChar("Robyn",mouth=6,eyes=3,brow=2)
            Robyn "Psssh, nah! That's just a rumor."
            python:
                adjustChar("August",mouth=7,eye=2,brow=1,eyeFrame=2)

            August "I'm concerned for you."
            python:
                adjustChar("August",mouth=6)
                adjustChar("Robyn",mouth=5,eyes=1,brow=0)

            Robyn "Hey, it beats being bored and alone! I get weird and sad when I'm by myself for too long."
            python:
                adjustChar("August",mouth=5,eye=3,eyeFrame=3)
                adjustChar("Robyn",mouth=1,eyes=1)
            August "Concerned."
            $adjustChar("Robyn",mouth=1,eyes=0)

            Narrator "This guy has a lot of nerve. You'd be annoyed, but it sounds like he's coming from a genuine place."

    if True in gus_questions:
        jump Ch1_Gus_Hangout_Loop
