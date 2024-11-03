default Thu_Stats = Unit("{color=#d5a0cb}Thursday{/color}",-2,-1,2,-2,2,6,5)

label Ch1_AtlasDoctorVisit_Confrontation:
    python:
        timeText = "12:00PM"
        musicPlayer.playSong(song = "urgently_jammin_song")
        Thu_Stats = Unit("{color=#d5a0cb}Thursday{/color}",-2,-1,2,-2,2,6,5)

    scene BG Sky Gray

    camera at camera_default

    with zoomfade(0.9)

    narrator "Elsewhere."
    Narrator "Atlas glides through the air, circling high above the main street below."

    show Thursday Look:
        matrixtransform rotated(z=15)
        xcenter 1.2
        yoffset -230
        ease 0.7 xcenter 0.6

    show oswald:
        xcenter 1.2
        ease 0.7 xcenter 0.5

    $adjustChar("OH",eyeFrame=0,eyes=1,brow=1,armR=3,armL=1,breath=True,)
    Narrator "He spots Oz combing the area, kicking through bushes, shaking trees and peeking behind dumpsters. He's looking for something."

    show Thursday Caw:
        xcenter 0.6
        yoffset -230
        easein 0.15 yoffset -260
        easeout 0.15 yoffset -230
        easein 0.15 yoffset -260
        easeout 0.15 yoffset -230

    show oswald:
        xcenter 0.5

    voice thursday_surprisea
    Thursday "Give it up Oswald! This another one of Edith's dead-end errands."


    show oswald:
        xcenter 0.5

        easein 0.3 xcenter 0.7 matrixtransform rotated(y=180)

    show Thursday Angry:
        yoffset -230
        xcenter 0.6
        matrixtransform rotated(z=15)
        ease 0.35 matrixtransform rotated(y=180,z=-20) xcenter 0.6

    $adjustChar("OH",eyes=5)

    voice thursday_angryc
    Thursday "And get away from that dumpster! We're looking for a moth not a cockroach!"

    voice oz_growlc
    Oz "{sc}...{/sc}"

    show atlasfallcg:
        xcenter 0.35
        xanchor 0.5
        ycenter -0.5
        matrixtransform RotateMatrix(0.0, 0.0, -20.0)
        matrixcolor BrightnessMatrix(-1)
        blur 10
        ease 0.5 ycenter 1.5 matrixtransform RotateMatrix(0.0, 0.0, -20.0)

    Narrator "Atlas drops from the sky and lands behind the howler."

    hide atlasfallcg
    show atlas:
        xcenter 0.35
        yoffset 700
        matrixtransform rotated()

        ease 0.4 yoffset 0
        ease 0.3 matrixtransform rotated(y=180)

    python:
        adjustChar("OH",eyes=0,brow=0)
        adjustChar("Atlas",eye=21,eyeFrame=0,armL=1,armR=1,feelers=1,phone=0)

    Atlas "HEY!"

    show oswald:
        matrixtransform rotated(y=180)
        xcenter 0.7

        easein 0.15 yoffset -30
        easeout 0.15 yoffset 0

        easein 0.3  matrixtransform rotated(0)

    show Thursday Default:
        matrixtransform rotated(y=180,z=-20)
        xcenter 0.6

        yoffset -230
        easein 0.15 yoffset -290
        easeout 0.15 yoffset -230

        ease 0.3 matrixtransform rotated(z=15) xcenter 0.8

    voice oz_huh
    $adjustChar("OH",eyes=0,eyeFrame=1,brow=0)
    Narrator "Oz jumps and whips around."

    show atlas:
        xcenter 0.35
        yoffset 0
        matrixtransform rotated(y=180)

        ease 0.6 matrixtransform rotated(y=-180,z=-15)

    python:
        adjustChar("OH",eyes=5,armL=2,brow=1)
        adjustChar("Atlas",eye=5,eyeFrame=0,tears=True,sparkle=True)

    Atlas "Oh nooo, you caught me!"

    $adjustChar("Atlas",eye=0,eyeFrame=3,tears=True,sparkle=True)

    show atlas:
        matrixtransform rotated(y=-180,z=-15)
        ease 0.6 matrixtransform rotated(y=360,z=15)

    Atlas "You win!"

    show atlas:
        matrixtransform rotated(y=360,z=15)
        ease 0.4 matrixtransform rotated(y=180)

    python:
        adjustChar("Atlas",eye=18,eyeFrame=0,tears=False,sparkle=False)
        adjustChar("OH",eyes=6,eyeFrame=0,armL=0,armR=0)

    Atlas "You guys can stop looking now."

    show Thursday Angry:
        matrixtransform rotated(z=15)
        xcenter 0.8

        yoffset -230
        block:
            easein 0.15 yoffset -250
            easeout 0.15 yoffset -230
            repeat 3

    voice thursday_listenb
    Thursday "Ya caught me in a bad mood twerp. Pay up!"

    show atlas:
        matrixtransform rotated(y=180,z=15)
        ease 0.4 matrixtransform rotated(z=15)

    $adjustChar("Atlas",eye=19)
    Atlas "Woah, what's with the hostility!? I'm doing you guys a favor!"

    $adjustChar("OH",eyeFrame=0,brow=0,eyes=0)
    Atlas "Can you tell Edith I changed my mind? The Spec Extractor sounds really scary."

    call battleTransition from _call_battleTransition_9

    camera:
        camera_zoom(z=-200)

    scene BG Sky Gray

    python:
        Atlas_Stats = AtlasUnit()
        Atlas_Stats.SetAttackMoves(['Kinesis'], 'Ch1_AtlasDoctorVisit_Confrontation_Cont_')
        musicPlayer.playSong(song = "supernatural_foe_intro_song")

    python:
        Oz_Stats = Unit("{color=#fffb42}Oz{/color}",2,2,-2,1,1,-1,12)
        Oz_Stats.baseDiff = 8
        Oz_Stats.SetIcon("dIcon1")
        Oz_Stats.SetMaxMTA(3)
        Oz_Stats.SetNOCA(2)
        Oz_Stats.SetMTA(3)
        Oz_Stats.SetEnemyAttackLabel("FIGHT_03_DREAMOZ_OZ_ATTACK")
        Oz_Stats.canTarget = False

        Thu_Stats = Unit("{color=#d5a0cb}Thursday{/color}",-2,-1,2,-2,2,6,5)
        Thu_Stats.baseDiff = 7
        Thu_Stats.SetIcon("dIcon2")
        Thu_Stats.SetMaxMTA(2)
        Thu_Stats.SetNOCA(2)
        Thu_Stats.SetMTA(2)
        Thu_Stats.SetEnemyAttackLabel("FIGHT_03_DREAMOZ_OZ_ATTACK")

    python:
        playerUnitsInit("Atlas")
        enemyUnitsInit("Oz","Thu")

        InitializeCombatUI(playerUnits, enemyUnits)

        HighlightEnemyUnitBars([0,1])
        HighlightPlayerUnitBars([0])

    with Dissolve(0.5)

    show oswald:
        xpos 1.3
        matrixtransform rotated()
        yoffset 100
        ease 0.6 xpos 1.0 matrixtransform rotated(z=-50)

    show Thursday Wings:
        yoffset -700
        xcenter 0.55

        ease 0.5 yoffset 0
        idleFloat(2.0,50)

    Thursday "You'll pay for this!"

    play sfx boss_target_sfx
    show Thursday Wings:
        ease 0.1 xoffset 10
        ease 0.1 xoffset -10
        ease 0.1 xoffset 10
        ease 0.1 xoffset -10
        ease 0.05 xoffset 0
        idleFloat(2.0,50)

    $Atlas_Stats.modifyHP(-3,1)

    voice thursday_howdareyoua
    Narrator "The raven attacks! He furiously bites and scratches the mothman, and Atlas takes [sfxDmg] piercing damage!"

    camera:
        camera_zoom(z=-200)

    $playerUnits[0].iconState = 0
    Atlas "It was a free consultation!"


    $Atlas_Stats.modifyHP(-3,1)
    voice thursday_angrya

    Narrator "Thursday goes for Atlas' fluffy antennae, and Atlas takes another [sfxDmg] piercing damage!"


    Atlas "{sc=3}Gya-ah!{/sc}"

    $playerUnits[0].modifyStatMod("rollMod",5,-5,5)

    $toggleQuickMenu()
    hide screen quicker_menu
    show screen turnCounter(1)

    python:
        CombatUnitPick()
        ui.interact()

label Ch1_AtlasDoctorVisit_Confrontation_Cont_0:
    play sfx boss_target_sfx
    Narrator "Thursday attacks again!"
    python:
        musicPlayer.playSong(song="the_unwelcome_visitor")
        #Atlas_Stats.iconState = 3
        playerBarNames[0] = "{glitch=30}{color=#3bec27}Atlas{/color}{/glitch}"
        Atlas_Stats.iconState = 3

    camera:
        matrixcolor TintMatrix("#c0fac8")
    camera screens:
        matrixcolor TintMatrix("#3bec27")*SaturationMatrix(0)
        ease 0.5 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(1)

    extend " But a {color=#3bec27}crushing force{/color} stops the creature. He squawks, {b}squeezed{/b} like an icecream cone."

    P_Atlas "{bt=3}{color=#3bec27}Hey, hey Thursday!{/color}{/bt}\n\nWhat do they call a raven caught between home and first base?"
    voice dmm_laughc
    P_Atlas "{color=#3bec27}A fowl ball!{/color}"

    python:
        Atlas_Stats.iconState = 3
        Thu_Stats.modifyHP(-100,1.0)

    camera at camera_shake

    show Thursday Wings:
        matrixtransform rotated()

        parallel:
            ease 0.6 yoffset -700

        parallel:
            yzoom 1.0 xzoom 1.0
            ease 0.1 yzoom 4.0 xzoom 0.5
            ease 0.2 yzoom 1.0 xzoom 1.0

    $adjustChar("OH",eyes=0,brow=4,eyeFrame=1,armR=0,armL=0)

    Narrator "The raven's shot through the air like a bullet, and disappears through the clouds."

    show Thursday Wings behind oswald:
        yoffset -700
        matrixtransform rotated()
        yzoom 1.0
        xzoom 1.0
        zoom 0.5
        ease 3.0 matrixtransform rotated(z=720) yoffset 100 zoom 0

    voice oz_hurtf
    Narrator "Oz freezes."

    show oswald:
        xpos 1.0
        matrixtransform rotated(z=-50)

        ease 0.5  xpos 1.2 yoffset 0 matrixtransform rotated()
        easein 1.1 xpos -0.25

    python:
        HighlightEnemyUnitBars([])
        musicPlayer.playSong()



    camera:
        parallel:
            camera_zoom(z=-200,x=150,t=0.75)
        parallel:
            ease 0.5 matrixcolor TintMatrix("#ffe7ee")


    extend "\n\nAnd sprints off to find his little buddy."

    pause 0.5

    python:
        musicPlayer.playSong(song="urgent_slower")
    Narrator "Atlas' phone rings. \n\n It rings and rings."

    Narrator "And rings."

    P_Atlas "{color=#3bec27}...?{/color}"

    stop music
    play sfx select_hover

    camera:
        camera_zoom(z=-250,y=20,x=-170,t=2.5)

    python:
        Atlas_Stats.iconState = 1
        playerBarNames[0] = "{color=#ED2A82}Atlas{/color}"

    Narrator "Atlas answers the call."

    python:
        HighlightPlayerUnitBars([])
        musicPlayer.playSong(song="supernatural_serenade_song",fadeOut=2,fadeIn=1)

    show atlas at climbfromhole:
        xcenter 0.5

    $adjustChar("Atlas",eyeFrame=3,eye=2,phone=2,feelers=3)

    August "{sc=3}{b}Atlas!{/b}{/sc} You okay? My whiskers were tingling! Where are you?"

    Atlas "Bleugh."

    $adjustChar("Atlas",eyeFrame=0,eye=5,feelers=0)

    extend "\n\nDon't use your wolfy sense on me man."

    $adjustChar("Atlas",eye=18,feelers=1)

    Atlas "I'll be home soon."

    August "You'd better!"

    jump Ch1_JamieFightBuildup
