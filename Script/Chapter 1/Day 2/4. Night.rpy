label Ch1_Day2Night:
    $ch1_midnight2 = False

    Narrator "The drive home is rather cramped."
    camera at camera_default
    scene BG Black
    camera default
    window hide
    scene BG Road Side with pixellate #----------------------------------------- Road side
    window show
    python:
        musicPlayer.playSong(song="undead_icebreakers_song",fadeIn=1,fadeOut=2)
        timeText = "7:00PM"

    play ambiance car_ambiance fadein 2.0
    pause 0.6


    show CGShade
    show CG AugustCar:
        xcenter -0.5
        ease 1.5 xcenter 0.5
    Robyn "Auguuuust! You were so brave out there. I never knew you were a fighter!"

    August "Yeah, no, my caveman brain took over at the first sign of trouble."

    August "But you were weirdly calm the whole time. What gives?"

    Robyn "Eh, you get used to it. Atlas and I got into to a lot of trouble back in the day."

    August "{i}Back in the day.{/i} \n\nKid, you're in your twenties."

    Robyn "And I haven't achieved anything!"

    Narrator "Mike snores, sleeping in the back seat."

    Robyn "Dude, how are you so put together?"

    August "Hm?"

    Robyn "Like how do you have a house and a family already?"

    August "Good or bad luck I guess? I had to grow up fast."

    August "Family wanted me married and out of the house."

    August "The marriage bit didn't work out. \n\nAaand now I'm here."

    August "But I'm flattered you think I'm put together."

    August "I wouldn't worry about all that achievement stuff. Life's about having good times with good folks."

    August "Which I'd say you're on the right track."

    stop ambiance
    camera:
        camera_default
        camera_zoom(z=-350,y=-55,x=-130,t=0.3)
        shaded("#ffe7ee")

    python:
        timeText = "10:00PM"
        musicPlayer.playSong(fadeOut=5.0)
        musicPlayer.playSong(song="magic_birdbrain_song",fadeOut=1,fadeIn=3)

    scene BG Black
    with Dissolve(0.75)
    Narrator "The side door of Edith's shop creaks open, the lumbering howler ducking inside, rubbing his sore arm."

    play sfx steps_approaching
    voice edith_hmph
    Edith "You're late."
    scene BG OutsideHospital:
        matrixcolor ColorizeMatrix("#1c1c1c","#77f6bd")

    show edith:
        xcenter 0.3
        matrixtransform rotated(y=180)
    show oswald:
        xcenter 0.5

    python:
        adjustChar("Edith",mouth=0,eye=1,brow=1,armR=1)
        adjustChar("OH",eyes=0,brow=4,eyeFrame=1)

    play sfx light_switch
    Narrator "Edith flicks on the light."
    $adjustChar("Edith",mouth=2,eye=0,brow=0,armR=1)

    voice edith_sigh
    Edith "And you're empty handed."
    python:
        adjustChar("Edith",mouth=0,eye=2,brow=0,armR=0)
        adjustChar("OH",brow=3,eyes=1,eyeFrame=0,armR=0,armL=0)

    voice oz_bleuhgh
    Oz "..."
    python:
        adjustChar("Edith",mouth=1,eye=2,brow=2)
        adjustChar("OH",eyes=5)

    Edith "Oh relax,, it's no wonder you're going gray."
    python:
        adjustChar("Edith",mouth=0,eye=1,brow=2)
        adjustChar("OH",brow=1,eyeFrame=1)

    voice oz_hurta
    Oz "{sc}-!{/sc}"
    python:
        adjustChar("Edith",mouth=2,eye=0,brow=0,armR=1)
        adjustChar("OH",brow=1,eyeFrame=1,armR=0,armL=0)

    Edith "I was talking about your {i}hair,{/i} Ozzie."
    python:
        adjustChar("Edith",mouth=0,eye=2,brow=2,armR=1)
        adjustChar("OH",eyes=0,brow=0)

    Edith "There's a mess downstairs, I need you to clean it up."
    python:
        adjustChar("Edith",mouth=0,eye=1,brow=2,armR=1)
        adjustChar("OH",eyes=5)

    Edith "I'm going to bed."
    python:
        adjustChar("Edith",mouth=1,eye=2,brow=2,armR=0)
        adjustChar("OH",brow=0,eyeFrame=0,eyes=5)

    extend "\n\nHelp yourself to the cheesecake in the fridge when you're finished."
    scene BG Black
    camera:
        camera_default
        shaded("#ffe7ee")

    python:
        timeText = "10:30PM"
        musicPlayer.playSong(fadeOut=5.0)

    with Dissolve(0.75)
    Narrator "After wishing everyone goodnight and a quick shower, you collapse into bed."

    Narrator "..."

    scene BG Apartment Bedroom with Dissolve(0.75)
    Narrator "Atlas shoots you a text."

    Atlas "Wanna call before bed?{nw}"
    menu:
        extend ""

        "Maybe for a bit.":
            Robyn "What's up?"
            scene BG Atlas Spooky with Dissolve(0.75)
            $musicPlayer.playSong(song="ghost_space",fadeIn=1)

            Atlas "Heard you and Auggie lurked around the graveyard. How'd it go?"

            Robyn "We found a hat and punched a lamp. It was good."

            Atlas "Y'sure? You don't sound too good."

            Robyn "... I dunno,, I'm starting to feel out of place."

            Atlas "How so?"

            Robyn "Take a wild guess."

            Atlas "Hey, nobody thinks of you that way. Cryptid or not you've got a place here. \n\nAnd you've got me!"

            Atlas "Besides, you could always ask August to bite ya."

            Robyn "That sounds painful, so no."

            Atlas "Good, 'cause he got all upset when I asked."

            extend "\n\nSomething about responsibility, family tradition or whatever."

            Atlas "I was like, \"So you're saying I'm not part of the family?\" Then he was all like, \"No you would probably die\"."

            Robyn "What a killjoy."

            Narrator "You stifle a yawn."

            Atlas "Well, I'm gonna head to bed. Sweet dreams!"

            Robyn "Goodnight Atlas."

            Narrator "You set your phone aside and close your eyes."

        "Nah, it's sleep time.":
            Narrator "You roll over and go right to sleep."

    scene BG Black
    python:
        musicNote = 6
        songText = "Ghost Space"
        timeSlot = 3


    with Dissolve(0.5)

    play music ghost_space
    Narrator "Resting on your nightstand..."

    Narrator "Madhouse yawns, throwing his arms above his head for a big stretch. He leans to one side, then to the other, and slides off his office chair. It's getting late."

    show CG MM shoes

    Narrator "He walks through the messy office and looks down at his feet. He's missing a shoe."

    Narrator "What's this feeling? There's a drumming in his ears, and a dull ache in his back. His chest rises and falls in this mechanical rhythm."

    Narrator "Breathing? Yeah, that's what they call it."

    show CG MM hands
    Narrator "Breathing."

    hide CG MM hands
    Narrator "Madhouse staggers to the bathroom. He shoves the door open, slaps his hand to the wall and feels around for the light switch."

    stop music fadeout 0.5

    play ambiance light_switch noloop
    #play music chapter_0_reverse noloop
    scene CG MikeInTheMirror 1
    # camera:
    #   camera_zoom(z=-500,x=-220,y=180)
    #   camera_zoom(z=0,x=0,y=0,t=2.0)
    with Fade(0.25, 0.5, 0.75)
    Narrator "There's a stranger in the mirror. A ghastly, hideous creature made of meat, hair and bone."

    extend "\n\nIt follows his every move and thinks his every thought."

    camera at camera_shake:
        camera_zoom(z=0,x=0,y=0)

    scene CG MikeInTheMirror 2

    #play sfx dice_result_c
    Narrator "A shriek escapes the young man's throat,, terror twisting his stomach to knots."

    show CG MikeInTheMirror 2:
        yoffset 0 matrixtransform rotated()
        easeout 0.4 yoffset 1200 matrixtransform rotated(z=150)

    Narrator "He staggers back, clutching his head in his hands,, and collapses."

    jump Ch1_Dream3

label Ch1_Dream3:
    scene BG Dream Meadow
    nvl clear

    python:
        timeText = "Dreamtime"
        musicPlayer.playSong(song="dreamlike_state_song",fadeIn=5,fadeOut=1)


    nvl show Dissolve(1)
    with Dissolve(.5)

    NVL_Narrator "You're lying in a field of wild grass, gazing at a sky sprinkled with clouds. \n\nWith luck, it'll rain, so you can run out in your boots and raincoat, even if Atlas hates wet feathers. \n\nYou could lend him your umbrella!"

    NVL_DRobyn "Wanna look for frogs tomorrow?"

    NVL_Atlas "I'd love to."

    NVL_Narrator "Atlas stands over you dressed in cut jeans and a torn flannel. He's older. Far too old for rain boots and frog hunting."

    NVL_Atlas "May I sit with you?"

    NVL_DRobyn "Oh! Uh, yeah."

    NVL_Narrator "The moth folds his wings and flops onto his back, gazing up at the clouds."

    NVL_Atlas "I'm sorry for frightening you like that."

    NVL_DRobyn "Like in general?"

    NVL_Atlas "{sc=2}No, ah, n-nevermind.{/sc}"

    #NVL_Narrator "A blue butterfly flutters past and gently lands on Atlas' antennae. He doesn't mind."

    NVL_Atlas "Feels real doesn't it?"

    NVL_DRobyn "Hm?"

    NVL_Atlas "This place, a meadow sculpted from a memory. Perfected down to the rocks in the soil."

    NVL_DRobyn "My teachers always said I had a vibrant imagination."

    NVL_Atlas "I envy that."

    NVL_Narrator "The moth sits up."

    NVL_Atlas "My memories of the surface are fading."

    extend "\n\nBut you, {glitch=30}{color=#70fffb}Daydreamer{/color}{/glitch} have stirred my heart."

    $musicPlayer.playSong(fadeOut=3.0)

    NVL_DRobyn "Atlas, is this a bit? Don't screw with me man."

    NVL_Latlas "Ah, the mothman!"

    NVL_Narrator "{glitch=30}Atlas{/glitch} helps you to your feet and gives your hands a reassuring squeeze."

    NVL_Latlas "Please, take this. My time runs short."

    NVL_Latlas "You've got company."

    NVL_Narrator "A crumpled twenty dollar bill appears in your hand. You glance down at the money., and when you look up, Atlas is gone."

    nvl clear

    NVL_DRobyn "{sc}-?.,{/sc}{nw}"


    voice mm_screama
    NVL_Narrator "A scream rattles the landscape.,.{nw}"

    show CG MikeInTheMirror 2 onlayer screens zorder 10000:
        yoffset -700 matrixtransform rotated(z=150) zoom 0.75
        xcenter 0.5
        easeout 0.7 yoffset 1200 matrixtransform rotated(z=360)

    camera:
        pause 0.7
        camera_shake

    play sfx ["<silence .7>", audio.hurt_b]
    play voice2 ["<silence .7>", audio.mm_damagedd]
    stop voice fadeout 0.7

    extend "\n\nA figure plummets from the clouds and hits the ground. He sits up with a start, a waterfall of red spilling from his crown. You scream."

    hide CG MikeInTheMirror 2 onlayer screens
    voice mm_surprise
    python:
        musicPlayer.playSong(song="not_so_spooky_song",fadeIn=1)
    NVL_Mike "What?! Where?! What's this flowery shit?"

    NVL_Narrator "Smearing blood off his face, the man struggles to his feet and starts wobbling towards you like a newborn fawn."

    voice mm_laughk
    menu(nvl=True):
        extend ""

        "Run away":

            NVL_Narrator "You stagger back."

            NVL_DRobyn "Stay away from me!"

            NVL_Narrator "You run far, far away, leaving the figure in the dust."
            pass

        "Help":
            NVL_Mike "Is that a cap and nightgown? {sc=3}{b}HILARIOUS!{/b}{/sc}"

            NVL_Narrator "He notes your worried expression."

            NVL_Mike "What's with the weird look?"

            NVL_DRobyn "{size=35}Mike? What happened to you?!{/size}"

            voice mm_yohoholaugh
            NVL_Mike "Oh! Yeah, I cracked my head on the toilet bowl. Are you an angel? \n\n\Is this heaven?"

            NVL_Narrator "You rush to the man's side, and catch him as he teeters over. He's hurt."

            NVL_DRobyn "No! No, this is bad. You need to wake up!"

            NVL_Narrator "Mike rests his head on your shoulder."

            NVL_Mike "I'll be fine."

            NVL_Mike "So y'sure you're not an angel?"

            NVL_DRobyn "You wanna see the pearly gates that badly? There's no going back from that!"

            NVL_Mike "Who cares! The world's frickin' moved on without me."

            NVL_DRobyn "I know how that feels. \n\nBut you gotta keep trying! Tomorrow's a new day!"

            NVL_Mike "Fine,, but I'm not gonna be happy about it."

    #NVL_DRobyn "Hey at least I'm trying!"

    #NVL_Narrator "Mike's expression softens and he gives you a faint smile."

    #NVL_Mike "A lot easier said than done."

    stop music fadeout 0.7
    nvl clear
    nvl hide Dissolve(0.5)
    scene BG Black  with Dissolve(0.5)

    Narrator "The dream fades as you stir awake, sunlight pouring through your bedroom window."

    Narrator "Elsewhere."

    jump Ch1_AtlasMorningConvo

label Non_Dev_Cutoff:
    python:
        musicNote = 0
        songText = "Astral Reflection"
        timeText = "ENDZONE"

    scene BG Dream Zone Blur:
        xzoom -1
        matrixcolor HueMatrix(0)
        ease 6.0 matrixcolor HueMatrix(90)
        ease 10.0 matrixcolor HueMatrix(-60)
        block:
            ease 10.0 matrixcolor HueMatrix(90)
            ease 10.0 matrixcolor HueMatrix(-60)
            repeat
    with Dissolve(1.0)
    play music astral_dissociation_song fadein 5.0

    $adjustChar("Atticus",eye=0,armR=0)
    show atticus:
        matrixcolor TintMatrix("#b6f0fc")
        xcenter 0.5

    with { "master" : Dissolve(0.5) }
    #Narrator "To be continued in {color=#ED2A82}{b}Part Two{/b}{/color}."

    $adjustChar("Atticus",eye=1,armR=0)

    Atticus "Seems we've hit the end of this update. \n\nYeesh, I need a nap."
    $adjustChar("Atticus",eye=0,armR=1)
    voice atticus_chuckle

    $adjustChar("Atticus",eye=6,armR=0)
    show atticus:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0, -10.0) yoffset 3
    Atticus "I hate stepping in like this but, y'know how it is."

    if gameVersion < 1:
        Atticus "The full work-in-progress build over on {a=https://www.patreon.com/DrowsyDrake}patreon{/a}."

    $adjustChar("Atticus",eye=7)
    voice atticus_hmmd
    Atticus "{sc}...{/sc}"

    show atticus:
        matrixtransform RotateMatrix(0.0, 0.0, -10.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0, 0.0) yoffset 30

    $adjustChar("Atticus",eye=8)
    voice atticus_youtakecare
    Atticus "Now you take care, alright?"

    jump credits_roll

#dom signal
label credits_roll:
    scene BG Black
    with Dissolve(0.5)
    camera:
        camera_zoom()
    window hide
    $musicPlayer.playSong("ghastly_resurgence")
    show credits_image:
        xpos 0.01
        yanchor 0.0
        ypos 1.0
        easein 70.0 ypos 0.0 yanchor 1.0 yoffset 150

    pause
    show credits_image:
        ypos 0 yanchor 1.0 yoffset 150
    pause
    return

image credits_image:
    Text(aboutTxt,xmaximum=700)

default aboutTxt = gui.about
