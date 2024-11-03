# Hangout 1
label Ch2_AtlasInvestigation:

    scene  BG Atlas Room Day
    with Dissolve(0.5)

    $musicPlayer.playSong(song="atlas_theme_loop",fadeIn=1,fadeOut=1)

    Narrator "Atlas' room is surprisingly organized. Seems he quickly tidied up the place before you came upstairs."

    Narrator "You look over the fairy lights and string of photographs decorating the overhead wood beams. Ugh, he's got a cuter room that you! \n\nAnd a beanbag?!"

    Narrator "Your apartment's great, but your room's drafty and the pipes creak. Not to mention, you haven't met the landlord."

    Robyn "Atlas you in here?"

    Narrator "No answer. Where'd he go?"

    pause 1.5

    python:
        atInv = [True,True,True,True,True]
        atDiff = 5
        atLaptop = False

    Narrator "That's enough waiting. Let's see what he's got going on.{nw}"

    label AtlasHangout1_Investigation:

        menu:
            extend ""

            "Alien Photo" if atInv[0]:
                show CGShade
                show CG Atlas Alien Pic
                Narrator "Aww, you remember this! It was when you two took a roadtrip to Ohio and ran into a real life alien! You named them Cheese."

                Narrator "But, in a strange twist, Cheese wasn't from space at all! They were a spray-painted homunculus born from a sleazy tourist trap."

                Narrator "You helped the little dude escape into the night."

                Narrator "You hope they're doing well."
                hide CGShade
                hide CG Atlas Alien Pic
                $atInv[0] = False

            "Vacation Photo" if atInv[1]:
                show CGShade
                show CG Atlas Vacation

                Narrator "You find a postcard that was never mailed. It's a photo of Atlas and who you assume is August relaxing at the beach."

                Narrator "Since when did Atlas visit Malibu? That can't possibly be safe for a cryptid! He'd get the feds on his feather ass!"

                Narrator "Atlas is dressed like a grandma in this photo."

                Narrator "Gosh, you love that wide-eyed twenty mile stare."

                hide CG Atlas Vacation
                hide CGShade
                $atInv[1] = False

            "Laptop" if atInv[2]:
                Narrator "You peek at the laptop sitting on the moth's bed. A word document detailing some personal writing is pulled up. \n\nOkay, maybe one glance. You can check for typos!"
                nvl show dissolve

                NVL_Text "\"Don't be silly.\""

                NVL_Text"The Mantis snickers with a slow shake of his head."

                NVL_Text "\"We're from different worlds darling.\""

                NVL_Text "The mutant takes your hand in his bulky paw and his glossy, compound eyes sparkle."

                NVL_Text "\"We can never be together.\""

                NVL_Text "The truth in his words sting."

                menu(nvl=True):
                    extend ""

                    "Stop":
                        pass

                    "Keep reading":

                        NVL_Text "\"Why? It's not fair.\""

                        NVL_Text "You gaze up at the cyborg warrior, pressing his hand to your chest. He gently brushes your cheek with the back of his hooked raptorial claw, and smiles weakly."

                        NVL_Text "\"The galactic syndicate would never allow it.\" He shakes his head."

                        menu(nvl=True):
                            extend ""

                            "That's enough":
                                pass

                            "I'm invested":
                                python:
                                    atLaptop = True
                                    atDiff = atDiff+4

                                NVL_Text "\"I don't care what the syndicate wants! Lady luck is on our side Blue. We can escape this planet together!\""

                                NVL_Text "You beg, gripping the lapel of the insectoid's leather uniform. Blue's expression darkens as he considers your words."

                                NVL_Text "\"You would risk banishment on my behalf?\""

                                NVL_Text "Blue murmurs, combing his fingers through your wild hair."

                                NVL_Text "\"I've never feared exile. Not with you by my side.\" You smile."

                                NVL_Text "\"Kiss me you {i}(sexy placeholder){/i}.\" He growls."

                                NVL_Text "Blue squishes your face in his hands and kisses you passionately. He kisses you, bites you or Whatever WIP FINISH THIS LATER!!!"

                                NVL_Narrator "Is that one of Atlas' original characters? If they are, he's never told you about them. Aaaaw man, now you feel kinda bad."
                                nvl clear
                $atInv[2] = False

            "Notebook" if atInv[3]:

                Narrator "You sit on the edge of Atlas' bed and scoop up his notebook. There's an impressive amount of doodles in this thing."

                Narrator "{i}Do I walk like a pigeon? Investigate. \n\nWash dishes. Werewolf plan failed. Thoughts like that.{/i}"
                show CGShade
                show CG Atlas Notebook
                Narrator "You flip to the newest page."

                Narrator "{i}Venus 452b. Signal DX Station. Braxton crash site communicator. Crush the killer robot.{/i}"

                Narrator "This is nonsense. What are you even looking at?"

                Narrator "You flip to a blank page and scribble down a nerdy stick figure rudely gesturing towards the reader. Then finish it off with plenty of hearts and your worst signature."
                hide CGShade
                hide CG Atlas Notebook
                $atInv[3] = False

            #"Window" if atInv[4]:
                #Narrator "The window's unlocked. Maybe Atlas went on a night flight around town?"

            "I'm good!" if not False in atInv:
                $atInv = [False,False,False,False,False]

            "Wait patiently" if False in atInv:
                $atInv = [False,False,False,False,False]

        if True in atInv:
            call dice_roll(PC_Stats.cStats("hustle") , atDiff, "Quickly now!") from _call_dice_roll_75

            if isRollSuccess:
                python:
                    atLaptop = False
                    atDiff = atDiff+2

                Narrator "Okay, what's next?"
                jump AtlasHangout1_Investigation

    Narrator "With a sigh you flop onto Atlas' bed and roll onto your back. The mattress is too soft for your liking, but you'll survive."

    Narrator "It's no problem! You'll just lay here and chillax until Atlas gets back."
    $musicPlayer.playSong(fadeOut=3.0)

    Narrator "You rest your head on the moth's pillow and hear a papery crunch. Did you squash something?"

    Narrator "You lift the pillow and see an old, crumbled photograph hidden underneath. Oops."

    play music astral_rejection_song
    scene  BG Atlas Room Day:
        matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")
    with nwDissolve(0.5)

    show CGShade
    show CG Atlas Portrait

    Narrator "It's a portrait of two parents gingerly cradling a pearlescent sphere."

    Narrator "The photo's torn and battered, but it's holding on."

    Narrator "Is that another moth?"

    Narrator "It has to be."
    stop music
    scene  BG Atlas Room Day:
        matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")
    with Dissolve(0.5)
    hide CGShade
    hide CG Atlas Portrait
    Narrator "You place the photo back where you found it."

    #cut to atlas
    scene BG Black
    with Dissolve(0.5)
    Narrator "Then with a sigh, you crash on the bed and wait until Atlas comes back."

    Narrator "Where'd he go anyway?"
    jump Ch2_AtlasAndTessieConvo

label Ch2_AtlasAndTessieConvo:
    scene BG Black
    camera:
        camera_default

    scene BG Lake Night
    play ambiance forest_ambianceb fadein 5.0 fadeout 4.0
    python:
        musicPlayer.playSong(song="boots_on_the_shore_bearsome")
        timeText = "7:00PM"
        shaded("#ebc0f8")

    with Dissolve(2.0)

    Narrator "The mothman glides above Lake Teardrop, watching the water below."

    camera:
        camera_zoom(x=200,y=-10,z=-350,t=0.9)

    show atlasfallcg:
        xcenter 0.35
        xanchor 0.5
        ycenter -0.5
        matrixtransform RotateMatrix(0.0, 0.0, -20.0)
        matrixcolor BrightnessMatrix(-1)
        blur 10
        ease 0.8 ycenter 1.5 matrixtransform RotateMatrix(0.0, 0.0, -20.0)

    Narrator "He swoops down and dantily perches atop his island. His thinking island... It's a sad patch of dirt poking out of the water."
    $adjustChar("Atlas",eye=1,armL=0,phone=0)

    hide atlasfallcg

    show atlas:
        xcenter 0.5
        yoffset 700
        matrixtransform rotated()
        shaded("#ebc0f8")

        ease 0.4 yoffset 0
        ease 0.3 matrixtransform rotated(y=180)

    Narrator "Atlas takes a seat on his rock and thinks."
    $adjustChar("Atlas",eye=0)

    Narrator "After a while, the moth plucks a feather from his wing and gently places it on the water's surface."

    $adjustChar("Atlas",eye=5,feelers=3)
    Atlas "Oh Lady of the Lake, I seek your guidance."

    show atlas at startledSquish

    $adjustChar("Atlas",eye=17,feelers=0)
    Atlas "Or I'm going to explode."

    pause 0.5

    $adjustChar("Atlas",eye=7,feelers=1)
    Atlas "Hello?"

    camera:
        camera_zoom(x=180,y=-10,z=-250,t=0.9)
    $adjustChar("Atlas",eye=2,feelers=0)

    show TessieTailCG_R at flipped:
        pos (0.5,1.0)
        shaded("#ebc0f8")

        yoffset 500
        easein 1 yoffset -30

        block:
            ease 3.0 yoffset 30
            ease 3.0 yoffset -30
            repeat

    show TessieTailCG_L:
        pos (0.9,1.0)
        shaded("#ebc0f8")

        matrixtransform rotated(z=45)
        yoffset 500
        easein 1 yoffset 0 matrixtransform rotated(z=5)

        block:
            ease 3.0 matrixtransform rotated(z=-5) xoffset -30
            ease 3.0 matrixtransform rotated(z=5)  xoffset  30
            repeat


    Tessie "It's the little man! What's the occasion?"

    Tessie "Brought any offerings?"

    $adjustChar("Atlas",eye=1)
    Atlas "Sorry Tess, not this time."

    Tessie "Aw man."
    $adjustChar("Atlas",eye=13,feelers=1)

    Atlas "Can I ask you for some advice?"
    $adjustChar("Atlas",eye=0)
    Tessie "Advice without an offering? You're on thin ice."

    Tessie "But go on, shoot."

    $adjustChar("Atlas",eye=21,feelers=3)

    Atlas "What do you do if your friends are hanging around a murderous jerk who tried to kill you?"

    Tessie ".,Well, If I had that problem,, I bite them really hard and drag them to the bottom of the lake."

    $adjustChar("Atlas",eye=13,feelers=1)

    Atlas "What if I can't swim?"

    Tessie "Then I guess you gotta talk to your friends."

    $adjustChar("Atlas",eye=0,eyeFrame=3,feelers=0)

    Atlas "What do I even say?"

    $adjustChar("Atlas",eye=13,eyeFrame=3,feelers=2)

    Tessie "I'm a dragon! I don't deal with interpersonal issues."

    Tessie "What would the {i}{b}great mothman{/b}{/i} do?"

    $adjustChar("Atlas",eye=5,eyeFrame=0,feelers=3)

    $musicPlayer.playSong(fadeOut=3)
    Atlas "He'd run away. That's what we always do."

    Tessie "..."

    hide TessieTailCG_L
    hide TessieTailCG_R
    scene CG Tessie Peek2
    camera:
        camera_default

    with Dissolve(0.75)

    Narrator "The lake monster rises out of the waves and rests her chin on her webbed paw."

    Tessie "Do you want to run away?"

    Narrator "She smiles slightly."

    Atlas "Sometimes."

    Tessie "Atlas. You're a smart guy."

    Tessie "You gotta fight for what's yours."

    Atlas "But I'm not brave or wise like you."

    Tessie "You don't need to be."

    Tessie "I know it's frightening, but you deserve to be heard. Your friends will understand."

    Tessie "You don't need to act now,, but act when you're ready."

    Atlas "Thanks Tessie."

    Atlas "Are you sure you don't deal with interpersonal drama?"

    Tessie "Mmh,, no, not anymore."

    Tessie "You mammals are exhausting."

    scene BG Black
    camera:
        camera_default
    with Dissolve(0.75)

    Tessie "Now get outta here."

    Narrator "Waving goodbye to Tessie, Atlas heads home."
    stop ambiance

    #atlas madhouse argue, robyn smoochie gus idk

    scene BG Black with Dissolve(0.5)
    window hide

    scene BG Cabin Night
    camera:
        camera_default
        camera_zoom(z=-220,y=80,x=150)
        matrixcolor TintMatrix("#ffffff")
        camera_zoom(z=-270,y=-80,x=-150,t=4.0)

    with Dissolve(0.5)

    pause 3.0
    scene BG Atlas Room Day
    with Dissolve(0.5)

    Narrator "Ugh, this is taking too long. If you lay here any longer you're gonna fall asleep. You roll off the bed and stand up with a good stretch. Atlas is probably busy."

    scene BG Black
    with Dissolve(0.9)
    Narrator "With a sigh, you leave the room."
    camera:
        camera_default
    jump Ch2_GusConvoKiss

    jump Ch2_MadhouseAndAtlas_Night
