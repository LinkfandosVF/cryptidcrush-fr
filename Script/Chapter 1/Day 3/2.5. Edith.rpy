image BG HospitalFuzzy:
    contains:
        "BG Hospital Room"
    contains:
        WaveImage("BG Hospital Room", amp = 5, strip_height = 2,melt=True,freq=30)
        alpha 1
        ease_bounce 15.0 alpha 0.5

label Ch1_AtlasDoctorVisit:

    scene BG HospitalFuzzy

    camera:
        camera_zoom(x=-130,y=200,z=-500)
        matrixcolor BrightnessMatrix(-1)*SaturationMatrix(0.5)*ColorizeMatrix("#7bff73","#0f4020")
        ease_bounce 5.0 matrixcolor BrightnessMatrix(-0.7)*SaturationMatrix(0.5)*ColorizeMatrix("#0f4020","#8ffc88")

    show edith:
        xcenter 0.5
        matrixtransform rotated(y=180)

    python:
        musicPlayer.playSong(fadeOut=1)
        timeText = "???"
        timeText = "11:10AM"

    with Dissolve(0.5)
    Narrator "Meanwhile."

    Edith "Your resting heart rate is well below average."

    show edith:
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated()

    Edith "You're freezing, your reaction time sucks—\n\nAnd you're spacing out again."

    camera:
        parallel:
            ease_bounce 0.5 matrixcolor BrightnessMatrix(0)*SaturationMatrix(1)*ColorizeMatrix("#000000","#ffe7ee")
            ease 0.2 matrixcolor TintMatrix("#ffe7ee")
        parallel:
            camera_zoom(x=130,y=80,z=-400,t=0.5)

    show edith:
        matrixtransform rotated()
        ease 0.5 matrixtransform rotated(y=180)
    with None

    show BG Hospital Room with nwDissolve(0.5):
        ease 0.5 matrixcolor BrightnessMatrix(0)

    show atlas at startledSquish:
        xcenter 0.75
        matrixtransform RotateMatrix(0,0,0)

    python:
        adjustChar("Atlas",eye=3,feelers=2)
        adjustChar("Edith",mouth=0,eye=1,brow=2)

        musicPlayer.playSong(song="thaumaturgy_thursdays_song",fadeOut=1,fadeIn=3)
        timeText = "11:15AM"

    Atlas "AH!"

    $adjustChar("Atlas",eye=14,feelers=0,eyeFrame=5)

    Atlas "What am I doing here?!"

    $adjustChar("Atlas",eye=10,feelers=2,eyeFrame=0)

    Atlas "{sc}HIC!{/sc}{nw}"

    python:
        adjustChar("Atlas",eye=8,feelers=0)
        adjustChar("Edith",mouth=3,eyeframe=1)

    show atlas at startledSquish:
        xcenter 0.75
        matrixtransform RotateMatrix(0,0,0)

    Atlas "URK!.,{nw}"

    show atlas:
        ease 0.3 matrixtransform RotateMatrix(0,0,-15) yoffset 20
        ease 0.3 matrixtransform RotateMatrix(0,0,0) yoffset 0

    $adjustChar("Atlas",eye=5,feelers=1)
    extend "\n\nBleugh."

    $adjustChar("Edith",mouth=5,eye=0,armR=1)
    Edith  "You checked yourself in."

    show atlas:
        matrixtransform RotateMatrix(0,0,0)
        yoffset 0

    $adjustChar("Atlas",eye=7,feelers=0)

    Atlas "{size=35}OH!{/size}\n\nThat makes sense."
    $adjustChar("Edith",mouth=0,eye=1,brow=2,eyeframe=0)

    Edith "You've got an phantom hitchhiker sabotaging your system."
    $adjustChar("Atlas",eye=13,feelers=0)

    show atlas at vibratenum
    Atlas "Ok, but it's giving me cool powers."

    $adjustChar("Atlas",eye=0,feelers=1)
    Atlas  "I'm still figuring out how it works."

    python:
        adjustChar("Edith",mouth=1,eyeframe=1,armR=0)

    Edith  "You like being a guinea pig huh?"

    python:
        adjustChar("Atlas",eye=6,feelers=0)
        adjustChar("Edith",brow=2,eyeframe=0)

    Atlas "As a pioneer of the supernatural, yes."

    python:
        adjustChar("Atlas",eye=0,feelers=0)
        adjustChar("Edith",mouth=1,eye=2)

    Edith "I admire that. Most aren’t willing to take such personal risks."

    $adjustChar("Atlas",eye=1)

    Atlas "Speaking from experience?"
    python:
        adjustChar("Atlas",eye=13)
        adjustChar("Edith",mouth=0,eye=0)

    Edith "Unfortunately."

    $adjustChar("Edith",eye=5)
    Edith "But I’m a softy. I can’t turn anyone away."

    $adjustChar("Atlas",eye=3)

    Atlas "How many experi—{nw}"
    show atlas at vibratenum:
        xcenter 0.75

    python:
        adjustChar("Atlas",eye=0,feelers=3)
        adjustChar("Edith",mouth=2,eye=1,brow=1)

    extend "{b}PATIENTS{/b} do you have?"

    Edith "A good handful, like your werewolf friend."

    python:
        adjustChar("Atlas",eye=13,feelers=0,eyeFrame=3)
        adjustChar("Edith",mouth=0,brow=2)

    Atlas  "Yeah, August mentioned you chased him with needles?"

    Edith "I still need a blood sample."

    $adjustChar("Edith",mouth=1,eye=2)

    Narrator "Edith lets out a dreamy sigh."

    $adjustChar("Edith",eye=0,armR=1)

    Edith "You think you could send him my way?"

    $adjustChar("Atlas",eye=0,feelers=1)

    Atlas "I don’t think that’s a good idea."

    $adjustChar("Edith",mouth=0,armR=0,eyeframe=1,eye=1)

    Edith "I'll give you free reign of the storefront for six minutes."

    show atlas at startledSquish:
        xcenter 0.75

    $adjustChar("Atlas",eye=4,feelers=0,eyeFrame=0)

    Narrator "A six minute magic shopping spree? What a steal!"

    Atlas "I'll consider it."

    python:
        adjustChar("Atlas",eye=13,feelers=1)
        adjustChar("Edith",mouth=1,eye=1,eyeframe=0)

    Edith "Now about your possession problem. I recommend cutting this pest off at the source. Is that okay with you?"

    $adjustChar("Edith",mouth=1,eye=1)

    Atlas "Sounds good Doc."

    $adjustChar("Edith",mouth=4,eye=1,armR=1)

    Edith  "Great. Wait right there and I’ll be back."

    show edith:
        matrixtransform rotated(y=180)
        parallel:
            ease 0.4 matrixtransform rotated()
        parallel:
            ease 1.0 xcenter -0.25


    Narrator "Edith leaves and {nw}"

    hide edith
    show atlas:
        yoffset 0
        ease 0.2 yoffset -40
        ease 0.15 yoffset 0

    camera:
        camera_shake_off(150)

    $adjustChar("Atlas",eye=3)
    play sfx audio.hurt_c

    extend "slams the door shut."

    hide edith

    $adjustChar("Atlas",eye=7)

    Edith "{size=45}OZZIE, BRING ME MY SPEC EXTRACTOR!{/size}"

    $adjustChar("Atlas",eye=19)

    Atlas "Is this a good idea? Without these powers I'm useless."

    $adjustChar("Atlas",eye=18)
    $adjustChar("Atlas",eye=19)

    Narrator "He eyes the window and notices the claw marks dug into the frame."

    show atlas:
        matrixtransform rotated()
        yoffset 0
        ease 0.25 matrixtransform rotated(y=180)
        ease 0.75 xcenter 0.9

    $adjustChar("Atlas",eye=1)

    Narrator "Atlas brushes his wing against the scratches. The lock looks busted, the window panel shoved off its casing."

    Narrator "Heavy footsteps march outside the door."

    Atlas "Nope."

    show atlas:
        matrixtransform rotated(y=180)
        xcenter 0.9
        parallel:
            ease 0.35 matrixtransform rotated(y=180,z=90)
        parallel:
            pause 0.1
            ease 0.3 xcenter 1.25
        parallel:
            ease 0.4 yoffset -100
    extend "\n\nNevermind."

    $adjustChar("OH",armR=2,armL=1)
    hide atlas
    show oswald:
        matrixtransform rotated(y=180)
        xcenter 0
        ease 1.0 xcenter 0.5

    Narrator "Oz walks into the empty room."
    voice oz_huh
    Oz "{sc}-?{/sc}"
    scene BG Black with Dissolve(0.5)
    play sfx steps_leaving

    Narrator "Oz whirls around and rushes out of the hospital room."

    jump Ch1_AtlasDoctorVisit_Escape

transform run_back_and_forth:
    xoffset -1280
    ease 5 xoffset 1280

label Ch1_AtlasDoctorVisit_Escape:
    scene BG DaytimeRoadside

    camera:
        camera_default
        shaded("#dbeaff")

    python:
        Ed = Character("???", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "7A", who_color = "#aad8dd")
        timeText = "11:30AM"
        musicPlayer.playSong(song="urgently_jammin_song",fadeIn=1,fadeOut=0.5)

        adjustChar("OH",eyeFrame=1,eyes=0,armR=0,armL=0,brow=0)

    camera:
        camera_zoom(z=-200,y=-15)

    with pixellate

    show oswald:
        xcenter 0.55
        block:
            flipped
            xoffset -1280
            ease 4.5 xoffset 1280
            unFlipped
            ease 4.5 xoffset -1280
            repeat

    show Thursday Default behind oswald:
        ycenter 0.22
        xcenter 0.49
        matrixtransform rotated(z=-25)

        block:
            parallel:
                unFlipped
                xcenter 0.49
                xoffset -1280
                ease 4.5 xoffset 1280
                flipped
                xcenter 0.61
                ease 4.5 xoffset -1280
                repeat
            parallel:
                easeout 0.15 yoffset -20
                easein 0.15 yoffset 0
                repeat

    Narrator "..."

    show oswald:
        parallel:
            ease 0.25 matrixtransform rotated(y=180)
            ease 1.0 xoffset 0

    show Thursday:
        ycenter 0.22
        parallel:
            ease 0.25 matrixtransform rotated()
            ease 1.0 xcenter 0.49 xoffset 0
        parallel:
            hoppies(5)

    show edith:
        enterFromRight(0.8,1.2)

    show edward:
        enterFromLeft(0.25,1.2)

    python:

        adjustChar("Edith",eye=1,eyeframe=1,brow=0,mouth=4,armR=0)
        adjustChar("Edward",mouth=3)

    Edith "How do you lose a giant bug!?"

    $adjustChar("Edith",eye=2,eyeframe=0,brow=0,mouth=2)
    Edith "Oz why didn't you grab him?"

    $adjustChar("OH",eyeFrame=1,eyes=5,brow=1)
    Oz "..."
    show Thursday Caw:
        ycenter 0.22
        xcenter 0.49
    Thursday "Chain the doors! Board up the windows! No soul escapes!"

    $adjustChar("Edith",mouth=5)
    Edith "We're running a clinic not a dungeon, dumbass!"

    show Thursday Angry:
        ycenter 0.22
        vibratenum()
    $adjustChar("Edith",mouth=0)

    Thursday "Then what do you suppose we do? {b}BEG?!{/b}"

    show Thursday Wings:
        ycenter 0.22
        hoppies(5)

    Thursday "Oh, don't forget to pay! Don't forget to pay!"

    python:
        adjustChar("Edward",eyes=2,mouth=0)
        adjustChar("Edith",eye=1,eyeframe=0,brow=2)
    Ed "You're delightfully myopic."

    show edward:
        startledSquish
        xcenter 0.25

    show oswald:
        unflipChar(tSpeed = 0.5)
        xcenter 0.55

    show Thursday Caw at hoppies(5):
        ycenter 0.22
        xcenter 0.49
        parallel:
            flipChar(tSpeed = 0.5)
        parallel:
            ease 0.5 xcenter 0.61

    $adjustChar("Edward",eyes=1)

    Ed "We're living in den of monsters. There are no riches to be made off this place."

    $adjustChar("Edward",eyes=4)
    Narrator "The monitor headed stranger's gaze drifts up and rests on Oz."

    python:
        adjustChar("Edward",eyes=2,mouth=2)
        adjustChar("OH",eyeFrame=0,eyes=1,brow=3)

    show oswald:
        ease 2.0 yoffset 60

    show Thursday Default:
        ycenter 0.22
        parallel:
            unflipChar(tSpeed = 0.5)

        parallel:
            ease 2.0 yoffset 30

    Ed "Maybe if you shake that {b}nasty reputation{/b} you'd stop bleeding customers."
    $adjustChar("OH",eyes=5)
    Oz "{sc}...{/sc}"

    show Thursday Caw:
        yoffset 30
        ycenter 0.22
        vibratenum()

    Thursday "How about I drop a wrench on your face and pour soda down your display ports?!"
    show edward at hoppies(xIntensity=2.5):
        xcenter 0.25

    $adjustChar("Edward",mouth=1,eyes=0)

    voice ed_laugha
    Narrator "The monitor laughs."
    show Thursday Look:
        yoffset 30
        ycenter 0.22
        vibratenum()

    $adjustChar("OH",eyeFrame=0,eyes=1,brow=3)
    $adjustChar("Edith",eye=2,eyeframe=1,mouth=0)
    Edith "Cool it Thursday! {color=#aad8dd}{b}Edward's{/b}{/color} right. You two are scaring clients."

    show edward:
        vibratenum()
        xcenter 0.25

    python:
        adjustChar("Edward",mouth=3)
        adjustChar("Edith",eyeframe=0)

    Narrator "The raven's feathers bristle."

    show Thursday Angry:
        yoffset 30
        ycenter 0.22
        vibratenum()

    $adjustChar("OH",eyes=6)

    voice thursday_facepalm

    Thursday "{b}WHATEVER!{/b}\n\n Just,, stop taking it out on Oz! Leave them alone!"

    $adjustChar("Edith",eyeframe=0,brow=0,mouth=2)

    Edith "Take a walk."

    Thursday "I've been working my feathers off and nobody in this godforsaken ghost town gives a shit!"

    show oswald:
        yoffset 60
        ease 0.2 yoffset -10
        ease 0.2 yoffset 0

    show Thursday Default:
        yoffset 30
        ycenter 0.22
        ease 0.3 yoffset -30

    $adjustChar("OH",eyes=0,brow=6,eyeFrame=1)

    Edith "Take a walk!"

    python:
        adjustChar("OH",eyeFrame=0,eyes=5,brow=3)
        adjustChar("Edward",mouth=0,eyes=3)
        adjustChar("Edith",eye=1,eyeframe=0,brow=2,mouth=0)
        musicPlayer.playSong(fadeOut=1.5)

    show oswald behind edward:
        ease 5 xcenter -1.5

    show Thursday Angry behind edward:
        ycenter 0.22
        yoffset -30
        ease 5  xcenter -1.5

    camera:
        camera_zoom(z=-425,x=200,t=1.2)

    show edward:
        xoffset 0
        ease 0.8 xcenter 0.55 matrixtransform rotated()

    Narrator "Oz, unflinching, follows orders and walks away."

    hide oswald
    hide Thursday

    python:
        adjustChar("Edward",eyes=1)
        adjustChar("Edith",eye=2)

    Edward "That muzzle's rather unnecessary don't you think? The fiend's made a full recovery."

    $adjustChar("Edward",eyes=4)
    Edward "Unless you're., starting to have doubts?"

    $adjustChar("Edith",eye=5,brow=3)
    Edith "It was Ozzie's decision. There's no shame in being cautious."

    $adjustChar("Edward",eyes=2)

    Edward "Aw, you worry too much lil' sis. I say let them loose."

    show edward:
        vibratenum()

    $adjustChar("Edward",mouth=1,eyes=0)
    Edward "I wanna watch!"
    python:
        musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=3)

    $adjustChar("Edward",eyes=3,mouth=2)
    Edward "Hm?"

    show edward:
        flipChar()

    python:
        adjustChar("Edward",eyes=1,mouth=0)
        adjustChar("Edith",eye=1)

    voice RobynSays("chapter 1","ohyeah")
    Robyn "Mike, now’s your chance to talk to Edith, she’s right there!"

    camera:
        camera_zoom(z=-480,x=-350,y=-35,t=3.0)

    show robyn:
        enterFromLeft(0.35,3)

    show madhouse:
        flipped
        enterFromLeft(0.1,3)
        idleFloat(2.2,10)

    python:
        adjustChar("Robyn",mouth=0,eyes=3)
        adjustChar("MM",mouth=1,eyes=1,armR=0,armL=0)

    voice mm_nob
    Madhouse "So she can laugh at me? Not a chance."

    show robyn:
        xcenter 0.35
        flipChar(0.3)

    Robyn "She’s not gonna laugh at you. C’mon, it’s worth a try."

    python:
        adjustChar("Robyn",mouth=6,eyes=2)
        adjustChar("MM",mouth=4,eyes=5,armR=2,armL=2)
        adjustChar("Edith",brow=2)

    Madhouse "Fine."

    camera:
        camera_zoom(z=-220,x=150,t=3.0)

    show edward behind edith:
        xcenter 0.55
        ease 1.5 xcenter 0.95

    show edith:
        xcenter 0.8
        ease 1.5 xcenter 0.75

    show robyn behind madhouse:
        flipped
        xcenter 0.35
        unflipChar(0.3)
        ease 1.0 xcenter 0.3

    show madhouse:
        xcenter 0.1
        ease 3.25 xcenter 0.5
        idleFloat(2.2,10)
    $adjustChar("MM",mouth=10,eyes=0)
    Narrator "Mike approaches the doctor."
    python:
        adjustChar("Robyn",eyes=1,mouth=1)
        adjustChar("MM",mouth=6,eyes=7)
        adjustChar("Edward",eyes=0)

    camera:
        camera_zoom(z=-400,x=150,t=0.5)

    voice mm_greet
    Madhouse "Oh my gosh, Edith heeey! Long time no see! \n\nHow’ve you been girl?"

    python:
        adjustChar("MM",mouth=6,eyes=7)
        adjustChar("Edith",eye=1,brow=1)

    voice edith_ugh
    Edith "Do I know you?"

    python:
        adjustChar("MM",mouth=11,eyes=0)
        adjustChar("Edith",eye=2,brow=1)

    Madhouse "It’s me, Madhouse Mike! Hold the applause."

    $adjustChar("Edith",eye=0,brow=2)
    $musicPlayer.playSong(song="not_so_spooky_song",fadeIn=0.5,fadeOut=0.5)

    Edith ".,Wait."

    python:
        adjustChar("MM",mouth=6)
        adjustChar("Edith",eye=2,brow=0,mouth=2)

    camera:
        camera_shake_off(150)

    show edith:
        xcenter 0.75
        block:
            yoffset 0
            ease 0.15 yoffset -20
            ease 0.15 yoffset 0
            repeat 2

    Edith "You’re that uppity prick who trash talked about me on air!"

    $adjustChar("Edith",eyeframe=1,brow=0,mouth=0,eye=1)

    Edith  "The Hocus Health Center’s ran by a bloodthirsty mad scientist? She chains weeping test subjects in the basement?"
    voice mm_screamc
    python:
        adjustChar("MM",mouth=1,eyes=7)
        adjustChar("Edith",eyeframe=0,brow=0,mouth=0,eye=2)

    show edith:
        yoffset 0
        xcenter 0.75
        ease 0.25 xcenter 0.7

    camera:
        camera_shake_off(150)

    show madhouse:
        xcenter 0.5
        pause 0.2
        ease 0.25 xcenter 0.45

    Edith "{size=40}I'LL KILL YOU!{/size}"

    Madhouse "Debbie was in charge of the ad copy! Are you accusing her of tampering with the script?"

    python:
        adjustChar("MM",mouth=3,eyes=-1)
        adjustChar("Edith",eyeframe=1,brow=0,mouth=2,eye=2)

    Edith "I don’t know who Debbie is!"

    python:
        adjustChar("Edward",eyes=1,mouth=2)
        adjustChar("Edith",eyeframe=0,brow=2,eye=0,mouth=3)
    show edward:
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated(y=180,z=-30)

    Edward "Is she your imaginary girlfriend?"

    python:
        adjustChar("Edward",eyes=0,mouth=0)
        adjustChar("Edith",brow=0,eye=2,mouth=0)
    show edith:
        flipChar(0.25)
        ease 0.2 xcenter 0.8
        ease 0.2 xcenter 0.7
        pause 0.2
        unflipChar(0.4)

    show edward:
        matrixtransform rotated(y=180,z=-30)
        pause 0.35
        ease 0.2 xcenter 1.0 matrixtransform rotated(y=180)

    Edith "Stay out of this Eddie!"

    python:
        adjustChar("MM",mouth=9,eyes=10,armR=0,armL=0)
        adjustChar("Edith",eyeframe=0,brow=2,mouth=2,eye=2)
        adjustChar("MM",mouth=11,eyes=0,armR=0,armL=0)
    show edward:
        xcenter 1.0
        matrixtransform rotated(y=180)
        ease 1.0 xcenter 0.9
    voice mm_laugha

    Madhouse "Folks love a good ghost story! It's great publicity!"

    voice edith_hmph
    Edith "No, it attracts annoying people. "

    python:
        adjustChar("MM",mouth=9,eyes=7,armR=1,armL=1)
        adjustChar("Edith",eyeframe=0,brow=2,mouth=0,eye=0)

    camera:
        camera_zoom(z=-450,x=100,y=-0,t=0.25)

    show edith:
        ease 0.2 xcenter 0.675

    show madhouse:
        ease 0.2 yoffset 15

    extend "Annoying people looking for monsters. "

    python:
        adjustChar("MM",mouth=0,eyes=8)
        adjustChar("Edith",brow=2,mouth=0,eye=2)

    camera:
        camera_zoom(z=-500,x=75,y=-10,t=0.25)

    show edith:
        ease 0.2 xcenter 0.65

    show madhouse:
        ease 0.2 yoffset 30

    extend "Annoying people looking for trouble. "

    python:
        adjustChar("MM",mouth=6,eyes=1)
        adjustChar("Edith",brow=0,mouth=4,eye=1)

    camera:
        camera_zoom(z=-550,x=50,y=-20,t=0.25)

    show edith:
        ease 0.2 xcenter 0.625

    show madhouse:
        ease 0.2 yoffset 45

    extend "Meddling freaks who lie through their teeth!"
    python:
        adjustChar("MM",mouth=9,eyes=10)
    voice mm_laughe
    Madhouse "You hear that Meatball? Edith’s calling you annoying."

    Robyn "{size=30}HEY!{/size}"

    python:
        adjustChar("MM",eyes=8,mouth=6)
        adjustChar("Edith",brow=2,mouth=0,eye=1)

    show robyn:
        xcenter 0.3
        unFlipped
        ease 0.2 matrixtransform rotated(z=15)

    camera:
        camera_zoom(z=-550,x=-50,y=-20,t=0.5)

    extend "\n\nIf it's any consolation, Mike recommended I come to you for help."

    Robyn "He called you a witch."
    python:
        adjustChar("MM",eyes=1)
    Madhouse "The baddest witch!"

    python:
        adjustChar("Edith",brow=0,eye=0,mouth=1)
    Edith "Tch,, whatever."
    $musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1,fadeOut=2)

    python:
        adjustChar("MM",mouth=3,eyes=4,armR=2,armL=2)
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        adjustChar("Edith",brow=2,eye=2,mouth=0,armR=1)
        adjustChar("Edward",eyes=1,mouth=0)
    show edith:
        flipChar(0.3)
        ease 1.3 xcenter 0.7

    show robyn:
        matrixtransform rotated(z=15)
        ease 0.35 matrixtransform rotated()

    camera:
        camera_zoom(z=-220,x=150,t=2)

    show madhouse:
        xcenter 0.45
        idleFloat(2.2,10)

    Edith "Do us all a favor Mike, and go home."

    python:
        adjustChar("Edward",eyes=5)
        adjustChar("Edith",brow=0,eye=0,mouth=0,armR=0)

    Edith "C'mon Ed."

    python:
        adjustChar("Edward",eyes=3)
        adjustChar("Edith",brow=0,eye=2,mouth=0)

    Edward "Sure."

    python:
        adjustChar("Edward",mouth=3,eyes=4)

    show edith:
        flipped
        ease 1.4 xcenter 1.25

    show edward:
        unflipChar(0.4)
        ease 2.5 xcenter 1.25

    show robyn:
        matrixtransform rotated()
        ease 0.5 xcenter 0.45

    show madhouse:
        ease 0.5 xcenter 0.63

    Edward "Sheesh, you got all worked up over some dead guy!"

    Robyn "Wow."

    python:
        adjustChar("Robyn",eyes=1,mouth=1)
        adjustChar("MM",mouth=1,eyes=5)

    voice mm_defeated
    Madhouse "I quit."

    jump Ch2_MadhouseConvoNight2

label Ch1_MadhouseChangesYourPhone:
    #show CGShade
    #camera:
    #    camera_zoom(z=-250,x=-90)

    #Madhouse "BOOM! At least I got your phone! That's somethin' right? You carry me around in your pocket!"

    #Madhouse "Check this out."

    Narrator "Your cell screen starts to bend, green slime oozing out the gaps in the metal, like it's about to burst."

    Narrator "The cellphone suddenly twists and a pair of horns pop out the top, the phone taking on a black and red theme, reflecting the ghost inhabiting it."
    voice mm_powerupb
    show CG MM_PhoneSide green:
        xpos -0.3
        ypos 0.25
        matrixtransform rotated(x=0)

        parallel:
            ease 0.6 xpos -0.01
        parallel:
            ease 0.4 matrixtransform rotated(z=20) ypos 0.35
            ease 0.2 matrixtransform rotated(z=0) ypos 0.25
    play music digihouse_mike_song
    python:
        songText= "Digihouse Mike"
        musicNote= 9

    show CG MM_PhoneSide smirk
    Madhouse "Ta-Dah!"

    show CG MM_PhoneSide
    voice mm_boopa
    Madhouse "It's me! Your cellphone!"

    show CG MM_PhoneSide calm
    Madhouse "It's like you're cradlin' me in the palm of your hand."

    show CG MM_PhoneSide smirk
    Madhouse "So don't drop me!"

    show CG MM_PhoneSide green

    Robyn "Did they even have cellphones back then?"

    show CG MM_PhoneSide smirk
    voice mm_greet
    Madhouse "Whu— How old do you think I am!?"

    show CG MM_PhoneSide green

    Robyn "Victorian Era?"

    show CG MM_PhoneSide calm
    voice mm_nob
    Madhouse "Now you're messing with me."

    Narrator "You stifle a laugh."
    show CG MM_PhoneSide smirk

    Madhouse "Have you ever met a ghost that old?"
    show CG MM_PhoneSide green
    Robyn "Me? Nah.\n\nMost sightings are either total bogus, or they're gone before I get there."

    Robyn "You're the first ghost I've spoke to."

    Robyn "If you don't count Taro."
    show CG MM_PhoneSide calm
    Madhouse "Aw, I'm special!"

    show CG MM_PhoneSide smirk
    Madhouse "Where is Taro anyway?"

    show CG MM_PhoneSide black:
        xpos 0.0
        ypos 0.25
        matrixtransform rotated(x=0)

        ease 0.6 matrixtransform rotated(z=90) ypos 0.35 xpos -0.3

    Robyn "She was sleeping last I saw her."
    hide CG
    hide CGShade with nwDissolve(0.5)

    return
