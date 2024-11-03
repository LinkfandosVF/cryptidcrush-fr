label Ch1_Start:
    #jump Ch1_SundayNightmare
    scene BG Black
    stop ambiance
    play sfx carCrash
    python:
        musicPlayer.playSong()
        WolfAugust_State["hurt"] = 1

        ResetChar("Jamie")
        ResetChar("Robyn")
        ResetChar("Atlas")
        ResetChar("MM")
        ResetChar("Taro")

    Narrator "CRUNCH."

    Narrator "..."
    camera:
        matrixcolor TintMatrix("#ffffff")

    scene BG RoadSideBlur:
        matrixcolor TintMatrix("#ba7dff")#*BrightnessMatrix(-0.05)
        xzoom 1.6
        yzoom 1.6
        xcenter 0.5
        ycenter 0.5
        ease 4.0 rotate -7 xcenter 0.4 xzoom 1.5 yzoom 1.5
        ease 8.0 rotate 7 xcenter 0.6 xzoom 1.4 yzoom 1.4
        ease 4.0 rotate 0 xcenter 0.5 xzoom 1.35 yzoom 1.35
        ease 2.0 xzoom 1.0 yzoom 1.0

    with { "master" : Dissolve(1.0) }

    Narrator "Le brusque freinage t'éxplose le crâne. Tes senses commencent à revenir en même temps."
    play ambiance forest_ambianceb fadein 30.0

    Narrator "Avec chaque sensation retrouvée tu te sent de plus en plus mal. Tu suppose sentir l'odeur de la fumée de la voiture, un airbag au visage, ou juste le goût du sang dans ta bouche…"

    $musicPlayer.playSong(song = "midway_to_nowhere_song",fadeIn=20)

    Narrator "Heureusement rien de tout ça."

    Narrator "La voiture, et ses passagers, en reste pour la plus grande partie sans bléssures.{size=-10}\n\nTon mal de crâne est vraiment pas agréable par contre.{/size}"

    Narrator "Atlas et Jamie éssaient de s'en remettre tandis que le regard que te jète Taro te fait penser qu'elle a probablement 8 vies maintenant."

    Narrator "Tu observe à travers le pare-brise. Ton véhicule s'est arrèté net, et devant toi se trouve un-"

    Taro "Très! Gros! Chien!"

    Narrator "Taro s'enfonce dans le siège de la voiture tétanisée."

    #voice atlas_surprised
    Atlas "Oh putain oh merde—"

    python:
        Atlas_State["eyeFrame"] = 1
        Atlas_State["eye"] = 3
        Atlas_State["feelers"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1

    show BG RoadSideBlurAfter:
        ease 0.8 xzoom 1.0 yzoom 1.0 rotate 0 xcenter 0.5

    show atlas:
        xcenter -0.3
        matrixtransform RotateMatrix(0,180,0)
        matrixcolor TintMatrix("#ddbfff")
        ease 0.8 xcenter 0.25

    show CG August Dead zorder 10:
        xcenter 0.65
        yoffset 700
        matrixcolor TintMatrix("#ddbfff")
        ease 0.5 yoffset 0

    show AugustTail zorder 10:
        xcenter 0.85
        yoffset 700
        matrixcolor TintMatrix("#ddbfff")
        ease 0.5 yoffset 0

    Narrator "Atlas se détache, puis sort de la voiture. La manière avec laquelle il marche les pieds pas vraiment toujours au sol serait hillarante si tu vennait pas d'éxploser ta voiture il y à 10 secondes."
    python:
        Robyn_State["brow"] = 2
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 2


    show atlas:
        xcenter 0.25

    show robyn:
        xcenter 0.5
        yoffset 500
        matrixtransform RotateMatrix(0.0, 180.0, -60.0)
        matrixcolor TintMatrix("#ddbfff")

        ease 0.9 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Robyn "Tout le monde vas bien?"
    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

    show blobhouse:
        yoffset 500
        xcenter 0.5
        matrixcolor TintMatrix("#ddbfff")
        ease 1.0 yoffset 0
        idleFloat(2.3, 15)

    show robyn:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.7 xcenter 0.7

    Madhouse "Je crois."

    show robyn:
        xcenter 0.7

    $Atlas_State["eye"] = 18
    $Atlas_State["eyeFrame"] = 0
    Atlas "Pas toi!"

    show blobhouse:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.48
        easein 2.5 matrixtransform RotateMatrix(0.0, 360.0*3, 180.0) xcenter 0.7
        idleFloat(2.3, 15)

    show atlas:
        ease 0.5 xcenter 0.45

    show robyn:
        ease 1.0 xcenter 0.85
    Narrator "Atlas dégage Mike comme un moustique, mais sa main, aussi poilue qu'elle soit, passe juste à travers."

    show atlas:
        xcenter 0.45

    show robyn:
        xcenter 0.85

    show blobhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 180.0)
        xcenter 0.7
        ease 0.6 matrixtransform RotateMatrix(0.0, 180.0, 360.0)
        idleFloat(2.3, 15)


    Madhouse "Ouch."


    Robyn "Au moins tout le monde vas bien."

    python:
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 3
        Jamie_State["armR"] = 1
    $Jamie_State["brow"] = 0

    show jamie:
        xcenter -0.5
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor TintMatrix("#c9abeb")
        ease 0.95 xcenter 0.15
    Narrator "Le démon sort de la voiture est observe le nuisible vert. Uniquement pour laisser passer un soupir un peu inatendu."
    $Jamie_State["mouth"] = 4
    #voice jamie_annoyedb
    Jamie "On devras se taper dessus plus tard."

    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.7
        idleFloat(2.3, 15)

    $BM_State["face"] = 8
    Madhouse "Ouais,, Et je suis vraiment., très impatient."

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["feelers"] = 0
        BM_State["face"] = 8
    show blobhouse:
        ease 0.3 xzoom 0 yoffset -100 alpha 0 blur 30
    Narrator "Mike retourne dans ton téléphone."
    $Jamie_State["mouth"] = 0
    hide blobhouse

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.25

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.25 matrixtransform RotateMatrix(0.0, 360.0, 0.0) xcenter 0.55
    Taro "S'il te plaaaait- garde cet horrible monstre loin de moi."
    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 5
        Atlas_State["armL"] = 2

        Jamie_State["eye"] = 0

        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 3

    Atlas "C'est pas grave! On va juste s'éxcuser, offrir au big guy de le rammener chez lui et puis voilà!"
    python:
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 2
        Robyn_State["mouth"] = 2

        Jamie_State["eye"] = 1
    Taro "Où on se tire!"
    show robyn:
        ease 0.15 yoffset -30
        ease 0.15 yoffset 0

    Robyn "Pas moyen!"

    python:
        Atlas_State["eye"] = 0
        Atlas_State["feelers"] = 1

        Jamie_State["armR"] = 3

        Robyn_State["eyes"] = 2

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Atlas "PSSSHT, {bt=3}Tout le monde{/bt} sait que ont peut pas échapper à un loup garou."

    $Robyn_State["mouth"] = 1

    Robyn "C'est pas ce qui me fesais peur."
    python:
        Atlas_State["armR"]= 1
        Atlas_State["armL"]= 0
        Atlas_State["eye"] = 6
        Atlas_State["eyeFrame"] = 0


    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.8 yoffset 400 matrixtransform RotateMatrix(0.0, 180.0, 10)
        pause 0.4
        ease 0.75 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show bigAssStick:
        matrixcolor TintMatrix("#c9abeb")
        yoffset 700
        xcenter 0.56
        matrixtransform RotateMatrix(0.0, 0.0, 8.0)
        pause 1.2
        ease 0.75 yoffset 200 matrixtransform RotateMatrix(0.0, 0.0, 4.0)

    show atlasArmR2:
        xcenter 0.55
        ycenter 0.79
        zoom 0.23
        matrixcolor TintMatrix("#ddbfff")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        ease 0.8 yoffset 400 matrixtransform RotateMatrix(0.0, 180.0, 10)
        pause 0.4
        ease 0.75 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "Le mothman ramasse le plus gros bâton qu'il peut trouver."
    python:
        Jamie_State["armR"] = 2
        Jamie_State["sweat"] = 1
    show jamie:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0) xcenter 0.25

    show bigAssStick:
        matrixtransform RotateMatrix(0, 0, 4)
        ease 0.3 yoffset 200 matrixtransform RotateMatrix(0, 180, 4)

    show atlas:
        matrixtransform RotateMatrix(0, 180, 0) yoffset 0
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)

    show atlasArmR2:
        matrixtransform RotateMatrix(0, 180, 0) yoffset 0
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
    Jamie "Do you have a death wish?"

    Robyn "{size=1}Il réspire?{/size}"

    Atlas "T'inquète, j'ai les réflexe d'une mouche de maison."
    python:
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 0

    voice jamie_annoyeda
    Jamie "Okay, le MOTHman."

    show bigAssStick:
        matrixtransform RotateMatrix(0, 180, 4)
        ease 0.3 matrixtransform RotateMatrix(0, 360, 4)
        parallel:
            ease 0.6 matrixtransform RotateMatrix(0, 0, 510)
        parallel:
            ease 0.3 yoffset -400
            ease 0.75 yoffset 250
        block:
            ease 0.14 yoffset 350 xcenter 0.58
            ease 0.14 yoffset 250 xcenter 0.56
            pause 0.2
            ease 0.125 yoffset 350 xcenter 0.58
            ease 0.125 yoffset 250 xcenter 0.56
            pause 0.7
            repeat

    show atlasArmR2:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
        pause 0.3
        ease 0.6 matrixtransform RotateMatrix(0, 180, 7) yoffset 50

    show atlas:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
        pause 0.3
        ease 0.6 matrixtransform RotateMatrix(0, 180, 7) yoffset 50
    show robyn:
        pause 0.35
        ease 6.0 xcenter 1.2

    show CG August Dead zorder 10:
        pause 1.35
        block:
            pause 0.14
            parallel:
                ease 0.115 yoffset 10
                ease 0.115 yoffset 0
            parallel:
                ease 0.1 xoffset 7
                ease 0.1 xoffset -7
                ease 0.03 xoffset 0
            pause 0.235
            parallel:
                ease 0.115 yoffset 10
                ease 0.115 yoffset 0
            parallel:
                ease 0.1 xoffset 10
                ease 0.1 xoffset -10
                ease 0.03 xoffset 0
            pause 0.595
            repeat

    show AugustTail zorder 10:
        pause 1.35
        block:
            pause 0.14
            ease 0.13 xoffset 10
            ease 0.13 xoffset -10
            ease 0.08 xoffset 0
            pause 0.125
            ease 0.13 xoffset 10
            ease 0.13 xoffset -10
            ease 0.08 xoffset 0
            pause 0.485
            repeat
    Narrator "Atlas se retourne et se met immédiatement a toucher le tas de poil avec la branche."

    camera:
        ease 6.0 zoom 2.2 xcenter 0.96 ycenter 0.83
    Atlas "Heyyyy? Copain? T'es vivant la dessous?"

    Robyn "Je vais juste. Réster très loin de (qu'importe) ce que tu est en train de faire."
    $WolfAugust_State["head"] = 2

    camera:
        zoom 2.2 xcenter 0.96 ycenter 0.83

    show CG August Dead zorder 10:
        ease 0.7 yoffset 700
    show AugustTail zorder 10:
        ease 0.7 yoffset 700


    show wolfaugust:
        matrixcolor TintMatrix("#ddbfff")
        xcenter 0.83
        yoffset 700
        matrixtransform RotateMatrix(0, 180, -90)
        pause 0.75
        parallel:
            ease 1.2 matrixtransform RotateMatrix(0, 180, 0)
        parallel:
            ease 1.0 yoffset -30
            ease 0.2 yoffset 0

    show atlas:
        matrixtransform RotateMatrix(0, 180, 7)
        ease 0.5  matrixtransform RotateMatrix(0, 180, -7)

    show bigAssStick:
        matrixtransform RotateMatrix(0, 0, 150)
        pause 0.2
        ease 0.5 matrixtransform RotateMatrix(0, 0, 0) yoffset 220 xcenter 0.54

    show atlasArmR2:
        matrixtransform RotateMatrix(0, 180, 7)
        ease 0.5  matrixtransform RotateMatrix(0, 180, -7)
    $qShake = { "master" : Move((10, 0), (-10, 0), .075, bounce=True, repeat=True, delay=.207) }
    $August = Character("Gros chien?", image = "augustus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c")
    Narrator "La lumière de la lune brille entre les branches, la douce lueur se pose sur le personnage dans la terre. Alors qu'Atlas poke la béstiolle, il s'étire, ses grosses griffes poussant contre la terre, et éssuie la saletée sur ses muscles tendus."

    hide CG August Dead
    hide AugustTail
    hide jamie
    hide robyn
    camera:
        ease 1.0 yoffset -200
    August "Tu..."
    camera at camera_default
    show WereGusWakes1
    hide atlasArmR2
    hide atlas
    hide bigAssStick
    hide wolfaugust
    hide WGusEyeglow
    with { "master" : Dissolve(0.5) }
    $displaymenu = True
    August "L'animal se lève du sol, et arrache la branche des mains d'Atlas avant de{nw}"
    $displaymenu = False
    camera at camera_shake

    extend " l'éxploser en deux."

    hide WereGusWakes1
    show WereGusWakes2
    $displaymenu = True
    Atlas "Attend—{nw}"
    $displaymenu = False

    voice august_hitwithyourcar
    August "Tu m'a rentré dedans... {sc=3}{b}avec ta VOITURE!!{/b}{/sc}"

    Narrator "Il grogne, sa voix est comme un bruit animal avec le dessous d'une teinte d'homme."

    jump Ch1_WolfbiteFever

label Ch1_WolfbiteFever:
    show Flickering Black
    stop ambiance fadeout 1.0
    pause 0.65
    play music elkhorn_radio_intro_song noloop
    pause (4.3)
    scene BG Road Side

    python:
        #Enemy Setup
        Gus_Stats = Unit("{color=#e8850c}Gros chien???",3,0,2,-1,1,-2,20)
        Gus_Stats.cHP = 1
        Gus_Stats.baseDiff = 8
        Gus_Stats.SetIcon("dIcon1")
        Gus_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        Gus_Stats.SetNOCA(2) ##Enemy Unit attacks 2 times when its their turn.
        Gus_Stats.SetEnemyAttackLabel("Ch1_WolfbiteFeverCont")
        Gus_Stats.SetMTA(3)

        enemyUnits = []
        enemyUnits.append(Gus_Stats)

        #Robyn Setup
        PC_Stats.updateStats()
        PC_Stats.SetAttackMoves(['Bash', 'Cheer', 'Focus', 'Heart Out'], 'Ch1_WolfbiteFeverCont_')

        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave'], 'Ch1_WolfbiteFeverCont_')

        Atlas_Stats = AtlasUnit()
        Atlas_Stats.SetAttackMoves(['Lore Dump', 'Kinesis', 'Pump Up'], 'Ch1_WolfbiteFeverCont_')

        #Puts the party into the Bar
        playerUnitsInit("PC","Atlas","Jamie")
        enemyUnitsInit("Gus")

        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "Ch1_WolfbiteFeverCont_0"
        currentLabelET = "Ch1_WolfbiteFeverCont_0"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])

    $WolfAugust_State["head"] = 0

    show wolfaugust:
        xcenter 0.5
        yoffset 700
        ease 1.0 yoffset 0

    python:
        musicPlayer.playSong(song = "supernatural_foe_intro_song",notif=False)
        musicPlayer.playSong(song = "supernatural_foe_loop_song",queueSong=True)

    $RefreshBarHP()
    Narrator "C'est peut-être pas le meilleur moment pour lire ça."
    $enemyUnits[0].modifyHP(12,1.0,"guts")
    $RefreshBarHP()
    $WolfAugust_State['head'] = 2
    Narrator "Il fait un truc très chelou avec la lune est récupère 12HP alors que ses os se retrouvent d'une manière très peu naturelle à leur endroit d'origine."

    python:
        #This hides the floating Quick Menu
        quick_menu = False
        quicker_menu_show = False

        #Thinking Music
        #renpy.music.set_volume(0.0, delay=0.5, channel=u'music')
        #renpy.music.set_volume(1.0, delay=0.5, channel=u'music2')

    hide screen quicker_menu

    python:
        CombatUnitPick()
        ui.interact()

label Ch1_WolfbiteFeverCont_0:
label Ch1_WolfbiteFeverCont_1:
label Ch1_WolfbiteFeverCont_2:
label Ch1_WolfbiteFeverCont_3:
    voice august_howl
    Narrator "Tu te fait couper instantanément par le loup-garou."

    $HighlightPlayerUnitBars([1])
    $ToggleBarState([0,1,2], 0)
    Atlas "I-It's not a full moon!"

    Narrator "Atlas saute, ses plummes toutes renversées."

    August "{sc=3}{b}TU ETAIT CENSE BABYSITTER JUNE.{/b}{/sc}"

    Narrator "L'homme-chien grogne, ses yeux sont virés sur le petit Mothman."

    August "{sc=3}{b}{color=#cf0000}TU TE SOUVIENT?{/color}{/b}{/sc}"

    Atlas "Attend, {color=#e8850c}AUGUST{/color}?!"

    $eNames[0] = "{color=#e8850c}August"
    $August = Character("August", image = "augustus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c")

    voice august_igethomejunesfastasleep
    August "Je suis rentré à la maison, June était endormie sur le canapé, et tu était impossible à trouver!"
    python:
        WolfAugust_State['head'] = 3
        WolfAugust_State['eyes'] = 0

    show wolfaugust:
        linear 0.6 xcenter 0.65
        block:
            matrixtransform RotateMatrix(0,0,0)
            ease 0.3 matrixtransform RotateMatrix(0,180,0)
            linear 1.2 xcenter 0.35
            ease 0.3 matrixtransform RotateMatrix(0,0,0)
            linear 1.2 xcenter 0.65
            repeat

    Narrator "August avance et recule comme près à frapper."

    voice august_yetwhenifollowmynose
    August "Par contre, et je découvre que tu est en train de faire la fête avec tes amis!"

    python:
        WolfAugust_State['eyes'] = 0
        WolfAugust_State['head'] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 2
        Robyn_State["brow"] = 3

        HighlightPlayerUnitBars([0,1])
    show robyn:
        xcenter 0.35
        yoffset 700
        ease 0.5 yoffset 100

    show wolfaugust:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.6 xcenter 0.8 matrixtransform RotateMatrix(0,180,0)

    $WolfAugust_State['eyes'] = 1
    Robyn "Tu le connais!?"

    show robyn:
        yoffset 100

    show atlas:
        matrixtransform RotateMatrix(0,180,90)
        xcenter 0.5
        yoffset 700
        ease 0.75 matrixtransform RotateMatrix(0,180,0) yoffset 100

    Atlas "Ouais! Voici August, mon coloc préféré est meilleur ami... \n\n{size=-10}qui ne me morderais jamais pour une erreur de calendrier.{/size}\n\n{bt=3}Heiiiin?{/bt}"

    $Atlas_State["eye"] = 7
    August "Coloc!? Tu est une PESTE."
    python:
        Jamie_State["sweat"] = 0
        Jamie_State["eye"] = 6
        Jamie_State["armR"] = 0
        Jamie_State["fire"] = 0
        Jamie_State["steam"] = 1
        Jamie_State["mouth"] = 1

        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 3

        HighlightPlayerUnitBars([0,1,2])


    show jamie:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.45

    show atlas:
        matrixtransform RotateMatrix(0,180,0)
        yoffset 100
        ease 0.5 xcenter 0.2
    show robyn:
        ease 0.5 xcenter 0.1

    $WolfAugust_State['brow'] = 2

    Jamie "HEY."with hpunch

    python:
        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

        Robyn_State["mouth"] = 1
    Atlas "Je sais que tu le pensais pas..."
    $WolfAugust_State['head'] = 0
    $WolfAugust_State['brow'] = 0

    $WolfAugust_State['brow'] = 1
    voice august_growle
    August "GWARRRGH!"

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Jamie_State["steam"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 1

    Robyn "H-hey c'est bon calmez vous."


    $WolfAugust_State['head'] = 3

    August "Pas comme toi quand tu m'a renversé avec TA VOITURE."
    $playerUnits[0].modifyHP(mod=-100,pierce=1.0,spareUnit=True)
    $playerUnits[0].modifyStamina(-8)
    show robyn:
        matrixcolor SaturationMatrix(1.0)
        ease 0.5 matrixcolor SaturationMatrix(0.0)

    Narrator "[PCname] prend [sfxDmg] de dommages émotionels!"
    $ToggleBarState([0], 0)
    $Atlas_State["eye"] = 1
    Atlas "Eh arrète d'engeuler [PCname], tu était celui au milleu de la route!"
    $WolfAugust_State['head'] = 0
    camera at camera_shake
    August "{sc=3}RAAAAH!{/sc}"
    $Atlas_State["eye"] = 5
    $Atlas_State["eyeFrame"] = 0
    $WolfAugust_State['head'] = 1
    show atlas:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)

    Atlas "Tu vois? C'est un vrai problème, J'éssaie d'avoir une conversation honnète avec toi et tu me crie dessus!"

    $WolfAugust_State['head'] = 2

    August "Tu est un emmerdeur! Tu fait jamais ce que je te dis, et je te demande UNE FOIS de poser ton cul sur le canap' et de pas bouger, tu te TIRE!"

    show atlas:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.2 matrixtransform RotateMatrix(0,180,0)
    Atlas "Uh ouais, quand Hazel est rentré du travail!"

    Narrator "August a l'air d'être sur le point d'éxploser."

    Atlas "En plus j'ai fait les pâtes comme tu m'a demandé!"
    $WolfAugust_State['head'] = 3
    $WolfAugust_State['brow'] = 0
    August "T'a éteint le four?"

    python:
        Atlas_State["eye"] = 7
        Atlas_State["feelers"] = 0
        Atlas_State["armR"] = 0
    Atlas "Um."

    $WolfAugust_State['head'] = 0
    $WolfAugust_State['brow'] = 1
    $Atlas_State["eye"] = 8
    $Atlas_State["feelers"] = 1

    voice august_growla
    August "{sc=3}AAAAAWWRRRGH!!{/sc}"

    python:
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 3
        Jamie_State["armR"] = 1
        Jamie_State["mouth"] = 0

    Jamie "Ca ne vas nul-part."
    $HighlightPlayerUnitBars([0,2])
    show atlas:
        ease 1.0 xcenter -0.3
    Narrator "Jamie néttoie sa gorge et se met devant Atlas."
    python:
        WolfAugust_State["head"] = 2

        Jamie_State["eye"] = 0
        Jamie_State["armR"] = 2
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 3
    $HighlightPlayerUnitBars([2])
    $playerUnits[0].modifyStamina(8)
    hide atlas
    show wolfaugust:
        pause 0.6
        ease 0.7 xcenter 0.7

    show robyn:
        ease 0.5 yoffset 700

    show jamie:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.5 matrixtransform RotateMatrix(0,360,0)
        ease 0.3 xcenter 0.3
        ease 0.5 matrixtransform RotateMatrix(0,360+180,0)

    Jamie "Ce qu'Atlas éssaie de dire, c'est qu'il est vraiment désolé."

    hide robyn

    $WolfAugust_State["head"] = 1

    August "Et je vais lui arracher les plumes!"

    $Jamie_State["eye"] = 2
    $WolfAugust_State["head"] = 2

    Jamie "Je sais que c'est souvent un trou du cul."

    Atlas "Hey!"

    $WolfAugust_State['brow'] = 0

    Jamie "Mais merci de lui donner un endroit pour vivre."

    $Jamie_State["armR"] = 8
    show jamie:
        ease 0.5 xcenter 0.4
    Narrator "Jamie pose sa main sur l'épaule d'August."
    python:
        WolfAugust_State["head"] = 0

        Jamie_State["eye"] = 4

    show jamie:
        matrixtransform RotateMatrix(0,180,-10)
        parallel:
            ease 0.25 xcenter 0.25
        parallel:
            ease 0.1 yoffset -20
            ease 0.1 yoffset 0
            pause 0.1
            ease 0.15 matrixtransform RotateMatrix(0,180,0)

    show wolfaugust:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.45 matrixtransform RotateMatrix(0,-180,0)

    $WolfAugust_State["brow"] = 1
    Narrator "Par réflexe, August dégage la main de Jamie, et manque de la mordre avant qu'iel ne la retire."
    # Weird Section
    show jamie:
        matrixtransform RotateMatrix(0,180,0)

    Jamie "NEMEMORTPASSILTEPLAIT."
    $WolfAugust_State['head'] = 3

    August "Si tu est si proche, pourquoi il ne dors pas chez toi!?"
    $Jamie_State['eye'] = 2

    Jamie "Je um,, vit dans un mauvais endroit de la ville."

    August "Genre les mines abandonnées?"

    Jamie "Les catacombes en fait."
    $WolfAugust_State["head"] = 2
    $WolfAugust_State["brow"] = 0

    August "Ooof,, c'est comment le loyer?"
    $Jamie_State['eye'] = 1
    $Jamie_State['mouth'] = 2
    $Jamie_State['armR'] = 0
    $Jamie_State['sweat'] = 1

    Jamie "Horrible,, Bludughadda n'accepte que les chèques par mail."
    $Jamie_State['eye'] = 0
    $Jamie_State['mouth'] = 0
    $WolfAugust_State["eyes"] = 0
    $HighlightPlayerUnitBars([0,2])

    Robyn "IL SE PASSE QUOI."

    show jamie:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        ease 1.0 xcenter -0.5

    $HighlightPlayerUnitBars([0,1])
    Atlas "Je fesais pas la fète, Gus,, on cherchait des indices sur la malédiction de [PCname]."

    hide jamie
    $WolfAugust_State['brow'] = 2

    August "Qui?"

    Narrator "Il parle plûtot calmement cette fois, ses yeux se posent sur toi. Il te regarde à présent."

    August "T'a pas l'air maudit."
    $HighlightPlayerUnitBars([0])

    Robyn "C'est un peu comme un sentiment horrible... Genre un truc térrible est sur le point d'arriver et je peux rien faire pour l'arrèter. Je sais même pas ce que c'est."
    $WolfAugust_State['brow'] = 0

    August "Bienvenu dans le club."

    Narrator "Tu regarde le sol, patogant tes chaussures dans la terre."

    Robyn "Nan, C'est pas aussi cool que toi."

    August "Cool?"
    $WolfAugust_State['head'] = 3
    $WolfAugust_State['eyes'] = 1

    August "Se transformer en bête sauvage un peu tout le temps est pas vraiment ce que je pourrais qualifier de {b}cool{/b}. C'est tragique,, et dangereux."

    Robyn "Je suppose."
    $HighlightPlayerUnitBars([1])

    Atlas "MENTEUR!"

    Atlas "Les loup-garou sont trop cool!"
    $WolfAugust_State['head'] = 3
    $WolfAugust_State['brow'] = 1
    $WolfAugust_State['eyes'] = 0

    August "{b}Vraiment?{/b}"

    Atlas "Faire peur a des randonneurs? Hurler à la lune? Et puis t'a arrèté une voiture avec ta tête!"
    $WolfAugust_State['head'] = 3
    $WolfAugust_State['brow'] = 0
    $WolfAugust_State['eyes'] = 1
    $musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=7.5,fadeOut=2.3)

    Narrator "August soupire et secoue sa tête."
    $WolfAugust_State['head'] = 1
    $WolfAugust_State['eyeFrame'] = 0
    $WolfAugust_State['brow'] = 0
    $WolfAugust_State['eyes'] = 0

    voice august_youcouldvejustapologized
    August "T'aurais juste du t'éxcuser."

    $Atlas_State["eye"] = 1
    $Atlas_State['eyeFrame'] = 3
    $Atlas_State["feelers"] = 1

    jump Ch1_WolfbiteAftermath

label Ch1_WolfbiteAftermath:
    scene BG Road Side
    python:
        HideBars()

        WolfAugust_State['head'] = 2
        WolfAugust_State['eyeFrame'] = 0
        WolfAugust_State['eyes'] = 1

        Robyn_State["mouth"] = 0
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2


    show wolfaugust:
        xcenter 0.8
        matrixtransform RotateMatrix(0, 180, 0)

    show jamie:
        xcenter 0.15
        matrixtransform RotateMatrix(0, 180, 0)

    show atlas:
        xcenter 0.25
        matrixtransform RotateMatrix(0, 180, 0)

    show robyn:
        xcenter 0.45
    with Fade(0.1, 0.2, 2.0, color="#FFF")

    #voice august_chuckle
    #August "Well, it's a pleasure to meet you [PCname]."
    # show jamiearm:
    #     ycenter 0.65
    #     zoom 0.23
    #     xcenter 0.15
    #     matrixtransform RotateMatrix(0, 180, 0)
    # show atlas:
    #     xcenter 0.05
    #     yoffset -50
    #     matrixtransform RotateMatrix(0, 180, 70)

    #$Robyn_State["mouth"] = 4
    #Robyn "Yeah, you seem,, nice."

    $Atlas_State["eye"] = 0

    #Atlas "Mhmm."

    $Robyn_State["mouth"] = 2

    Robyn "Je peux t'ammener à l'hopital?"
    $WolfAugust_State['head'] = 3
    $WolfAugust_State['brow'] = 2
    $Atlas_State["eye"] = 1
    $Atlas_State["feelers"] = 0

    voice august_ifyoucanfindavet
    August "Si tu trouve un putain de vétérinaire à cet heure-! GAHAHA… ACK."

    $WolfAugust_State['head'] = 2
    $WolfAugust_State['eyeFrame'] = 2
    $Atlas_State["eye"] = 0
    $Robyn_State["mouth"] = 1

    Narrator "Il se tort de douleur presque tombant sur le sol."

    $Atlas_State["eye"] = 3
    $Atlas_State["tears"] = 1

    Atlas "AUGUST MEURT PAS! Je suis désolé,, tu comptait sur moi! J'aurais du être résponsable!"

    $WolfAugust_State['head'] = 1
    $WolfAugust_State['brow'] = 0
    $WolfAugust_State['eyeFrame'] = 0

    August "JE VAIS PAS MOURIR,, c'est juste cette putain de malédiction!"

    $Atlas_State["eye"] = 18
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["tears"] = 0
    Atlas "Oh."

    $Atlas_State["eye"] = 5
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["feelers"] = 1

    August "On est dans quel phase de la Lune?!"

    $Jamie_State['eye'] = 2
    $Jamie_State['mouth'] = 4

    Jamie "Premier quart."
    $WolfAugust_State['head'] = 2
    $WolfAugust_State['brow'] = 0
    $WolfAugust_State['eyeFrame'] = 0
    $Jamie_State['mouth'] = 0

    voice august_nowthatexplainsit
    August "Ah, bon bah ca éxplique tout."
    $Jamie_State["sweat"] = 0
    $Jamie_State["eye"] = 3
    Robyn "Explique quoi?"

    show wolfaugust:
        xcenter 0.8
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.5 xcenter 0.75
        pause 0.5
        ease 0.5 xcenter 0.7
        pause 0.5
        ease 0.5 xcenter 0.65
        pause 0.5

    Narrator "La forme monstrueuse d'August disparais, le laissant sur le sol à terre."

    $audio.delayedThunk = ["<silence .4>", "audio/SFX Battle/Hurt_B.ogg"]

    camera:
        pause 0.4
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.05 xoffset 0

    show wolfaugust:
        xcenter 0.65
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.5 yoffset 700 matrixtransform RotateMatrix(0, 180, 180) xcenter 0.75

    play sfx delayedThunk
    $Jamie_State["eye"] = 4
    Narrator "Il éxpire un coup ennuyé, avant de s'évanouir complètement inconscient."

    show jamie:
        ease 0.5 xcenter 0.45

    show atlas:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.5 xcenter 0.8
        ease 0.4 matrixtransform RotateMatrix(0,0,0)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.8 matrixtransform RotateMatrix(0,360*2,0) xcenter 0.2
    $Jamie_State["armR"] = 3
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 0
    $Atlas_State["eye"] = 14
    $BM_State["face"] = 9


    Narrator "Tu sais absolument rien sur les cryptides, et tu n'est pas sur de savoir comment aider."

    $Atlas_State["eye"] = 3
    $Atlas_State["feelers"] = 0

    Narrator "{i}On devrait l'emmener à l'hopital? Est-ce que Longhope à un hopital? Ils ont des stations services alors, ils ont des hopitaux… hein?{/i}"

    $Atlas_State["eye"] = 2
    Narrator "Tu veux juste tomber au sol et ne plus jamais en parler."

    #TODO FLIP BLOBHOUSE SO HE FACES JAMIE
    $Atlas_State["eye"] = 3
    show blobhouse:
        yoffset -100
        alpha 0
        blur 30
        xcenter 0.05
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 yoffset 0 alpha 1 blur 0
        idleFloat(2.3, 15)

    python:
        musicPlayer.playSong(song="not_so_spooky_song")
        timeText = "Tired."

        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1
        Robyn_State["mouth"] = 1

        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 5

    voice mm_wellwellwella
    Madhouse "Eh bien pendant que vous fesiez les cons… J'ai appelés les urgences! Des débiles de Hocus Health Center & Potions devraient être là dans une minute."

    Narrator "Je suppose que sa répond à ta question."

    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1
    $Robyn_State["mouth"] = 4

    Robyn "Vraiment?"
    $BM_State["face"] = 1
    $BM_State["arms"] = 1
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 2
    $Robyn_State["mouth"] = 3
    $Atlas_State["eye"] = 0

    Madhouse "Eh quelqu'un doit bien être résponsable par ici."

    $Atlas_State["eye"] = 18
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["feelers"] = 1

    Atlas "Merci., {sc=1}Mike.{/sc}"
    $BM_State["face"] = 4
    $BM_State["arms"] = 0
    $Atlas_State["eye"] = 19
    $Atlas_State["phone"] = 2
    Madhouse "Yeah,, {bt=3} on s'en fout.{/bt}"

    show jamie:
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 360, 0)
    $BM_State["face"] = 3
    $Jamie_State["mouth"] = 2
    $Jamie_State["eye"] = 3
    $Jamie_State["armR"] = 4
    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1
    $Robyn_State["mouth"] = 1

    Narrator "Jamie regarde le spectre et sourit nerveusement. Madhouse ricanne en réponse."
    $Jamie_State["mouth"] = 4
    Jamie "T'es vraiment un super ennemi, Madhouse Mike. J'aurais pas du t'attaquer dans ton état actuel, étant donné la... différence d'avantages."
    $BM_State["face"] = 1
    voice mm_laughawkward
    Madhouse "Aww crâne d'os, p'tit démon."
    $BM_State["face"] = 7
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 0
    $Robyn_State["mouth"] = 7

    Madhouse "{sc=2}Juste attend qu'ont sois en dehors d'un véhicule la prochaine fois.,.{/sc} \n\nJuste comme ça!"

    $BM_State["face"] = 1
    $BM_State["arms"] = 0
    $Jamie_State["eye"] = 2
    $Jamie_State["sweat"] = 1

    Jamie "Haha."

    $Jamie_State["mouth"] = 0
    $Jamie_State["eye"] = 1
    $Atlas_State["eye"] = 2
    $Atlas_State["eyeFrame"] = 3
    $BM_State["face"] = 1

    Jamie "[PCname] laisse moi régler ça."

    Robyn "Et bien., on s'en occuperas demain."

    Taro "Est-ce que le gros chien est mort?"

    $Atlas_State["phone"] = 0
    $Atlas_State["eye"] = 5
    $Atlas_State["eyeFrame"] = 0
    $Robyn_State["eyes"] = 2
    Jamie "Non il réspire. Il s'est juste évanouit."

    Taro "Oh."

    Narrator "Freinant non loin de la route, un SUV noir avec des décorations blanches s'arrète près du groupe, des lumières rouge clignotent au dessus du véhicule."
    $BM_State["face"] = 4
    $Atlas_State["eye"] = 18

    voice atlas_heya
    Atlas "Tu était censé appeler une ambulance, pas un coach funéraire."

    $BM_State["face"] = 1
    Madhouse "Très drôle!"
    python:
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#d5a0cb")

        musicPlayer.playSong(song="magic_birdbrain_song",fadeIn=1,fadeOut=1)

        timeText = "Trop. Fatigué."


    Someone "Ecartez le chemin!"
    show jamie:
        matrixtransform RotateMatrix(0, 0, 0)

        ease 0.75 xcenter 0.15
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

    show atlas:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.75 xcenter 0.4
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

    show robyn behind atlas:
        ease 0.75 xcenter 0.25

    show Thursday Default:
        matrixtransform RotateMatrix(0, 0, 0)
        xcenter 1.5
        yoffset -260
        pause 0.5
        ease 0.75 xcenter 0.83

    show oswald:
        xcenter 1.5
        pause 0.5
        ease 0.75 xcenter 0.805

    $Jamie_State["eye"] = 2
    $Jamie_State["mouth"] = 2
    $Jamie_State["sweat"] = 1
    $BM_State["face"] = 3

    Narrator "La porte du conducteur souvre et un corbeau blanc un peu étrange en sort, un énorme cryptide en combinaison grise ferme la porte en sortant derrière."

    voice thursday_cawc
    show oswald:
        xcenter 0.805

    show Thursday Caw:
        yoffset -260
        xcenter 0.83
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260
    Someone "Aller, mettez le dans la cabine."
    show Thursday Smile
    $Atlas_State["eye"] = 1
    $Robyn_State["eyes"] = 0
    $Robyn_State["mouth"] = 4
    $Robyn_State["brow"] = 1
    $BM_State["face"] = 4

    Robyn "L'oiseau conduisait?"

    voice thursday_cawi
    show Thursday Wings:
        yoffset -260
        xcenter 0.83
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260
    Someone "On est à court de personel."

    Robyn "Ah."

    $OH_State["armL"] = 1
    $OH_State["armR"] = 2
    $OH_State["eyes"] = 1
    $Atlas_State["eye"] = 1
    $Atlas_State["eyeFrame"] = 5
    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 5
    $Robyn_State["brow"] = 2
    $Jamie_State["eye"] = 1
    $BM_State["face"] = 1
    $Jamie_State["mouth"] = 0

    show blobhouse:
        yoffset 0
        alpha 1
        blur 0
        xcenter 0.05
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 yoffset -100 alpha 0 blur 30

    show Thursday Default
    Narrator "Le large cryptide en combinaisont sort un stylo et un presse-papier."

    show Thursday Caw:
        yoffset -260
        xcenter 0.83
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    Someone "On dirait que quelqu'un est tombé de fatigue. Bah, les chiens-chiens et leur complexe d'invincibilité."
    show Thursday Smile
    Someone "On vas vous le réparer."

    $Robyn_State["eyes"] = 0
    $Robyn_State["mouth"] = 2
    $Robyn_State["brow"] = 1

    Robyn "Et à propos de la police? Les cryptides ont des assurances? A qui est-ce que je parle de ça?!"
    show Thursday Smirk:
        yoffset -260
        xcenter 0.84
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260
    voice thursday_laugh
    Someone "HAHA! Les humains."

    $OH_State["eyes"] = 0
    $OH_State["brow"] = 1
    $Robyn_State["eyes"] = 2
    $Robyn_State["mouth"] = 5
    $Robyn_State["brow"] = 0
    Narrator "Froncant les sourcils, le plus grand humanoide lève sa main et donne une pichenète à l'oiseau."

    show Thursday Caw:
        yoffset -260
        xcenter 0.84
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    Someone "Gwah! I-Il iras bien! Après le coma. Peut-être."
    $OH_State["eyes"] = 2
    $OH_State["brow"] = 0
    $OH_State["eyeFrame"] = 1
    $OH_State["armR"] = 1
    $OH_State["armL"] = 1
    $Atlas_State["eye"] = 3
    $Robyn_State["eyes"] = 0
    $Robyn_State["mouth"] = 1
    $Robyn_State["brow"] = 1


    Narrator "Expirant de la fumée, le cryptide lance un regard tueur à l'oiseau."

    Robyn "Coma?!"

    show Thursday Look

    Someone "J-je rigole! T'inquète pas à propos de ça! {nw}"

    $Atlas_State["eye"] = 1
    $Robyn_State["eyes"] = 3
    $Robyn_State["mouth"] = 3
    $Robyn_State["brow"] = 4
    show Thursday Smile
    extend "\n\Les loup-garou sont éxtrèmement résistants."

    $OH_State["eyes"] = 5
    $OH_State["brow"] = 1
    $OH_State["armL"] = 1
    $OH_State["armR"] = 2
    $Robyn_State["eyes"] = 0
    $Robyn_State["mouth"] = 3
    $Robyn_State["brow"] = 1
    $Atlas_State["eye"] = 0
    show Thursday Default:
        matrixtransform RotateMatrix(0, 0, 0)
        xcenter 0.84
        yoffset -260

        ease 0.75 xcenter 0.73
    show oswald:
        xcenter 0.805

        ease 0.75 xcenter 0.69

    Narrator "Avec un léger grognement, l'humanoide te tend les documents,, il a l'air de vouloir que tu signe. C'est un peu comme un genre de comis, en fait,, un fait fait spéciallement pour les loup-garou?"

    $Robyn_State["eyes"] = 2
    $Robyn_State["mouth"] = 4
    $Robyn_State["brow"] = 0
    Robyn "C'est quoi?"

    $OH_State["eyeFrame"] = 0
    $OH_State["eyes"] = 0
    voice thursday_cawh
    show Thursday Caw:
        yoffset -260
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    Someone "Un report d'attaque,, Oz garde une trace de tout ce qu'il se passe."

    $Atlas_State["eye"] = 18
    $Atlas_State["eyeFrame"] = 0
    $Robyn_State["eyes"] = 2
    $Robyn_State["mouth"] = 5
    $Robyn_State["brow"] = 2
    $OH_State["eyes"] = 0
    Robyn "Mwouais, j'sais pas."

    Atlas "[PCname] va rien signer."
    show Thursday Default

    $OH_State["eyeFrame"] = 1
    $OH_State["brow"] = 0
    $OH_State["armR"] = 1
    $OH_State["eyes"] = 5
    Narrator "Atlas soupire, et rend le papier au Cryptide, qui regarde désépérement le Mothman."

    show Thursday Angry:
        yoffset -260
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    Someone "Tu signe vraimen rien?"
    $Robyn_State["mouth"] = 4
    $OH_State["eyes"] = 0

    Robyn "Hors de question. Pardon."
    $OH_State["eyes"] = 1
    $OH_State["eyeFrame"] = 0
    $OH_State["brow"] = 1
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 5
    voice atlas_distracted
    Atlas "Blah blah blah, okay vous pouvez y aller!"

    voice thursday_listenb
    show Thursday Angry:
        yoffset -260
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    Someone "Hey mec,, ont fait juste notre boulot!"
    show Thursday Caw:
        yoffset -260
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260
    $OH_State["eyes"] = 1

    Someone "Bon allez Oz."

    show Thursday Wings:
        yoffset -260
        ease 0.5 yoffset -700


    Narrator "Avec un coup d'aile, le corbeau retourne dans le van."
    hide Thursday

    $OH_State["eyes"] = 5
    $OH_State["eyeFrame"] = 1
    $OH_State["brow"] = 0
    $OH_State["armL"] = 2
    $OH_State["armR"] = 0
    $Robyn_State["eyes"] = 0
    $Robyn_State["mouth"] = 1
    $Robyn_State["brow"] = 1

    voice oz_growlc
    Oz "..."
    show oswald:
        ease 3.0 xcenter 1.5

    $OH_State["eyeFrame"] = 0
    $OH_State["brow"] = 1
    $OH_State["armL"] = 2
    $OH_State["armR"] = 0
    Narrator "En soulevant le corps inanimé d'August, Oz le porte au van avant de le fermer."

    Atlas "Peeeut être que l'un de nous devrait réster avec lui?"

    Narrator "Atlas regarde le SUV démarrer et repartir."

    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 5
    $Atlas_State["eye"] = 0

    Atlas "Tu peux conduire?"

    $Robyn_State["eyes"] = 3
    $Robyn_State["mouth"] = 6

    Robyn "Aaaabsolument, laisse moi juste… me lever."

    Jamie "On devrait s'en occuper."
    $musicPlayer.playSong(fadeOut=5)
    scene BG Black with Dissolve(1.0)

    Narrator "En un clain d'oeuil, tu te fait soulever et emmener sur les sièges arrière de ta voiture. Avec un autre, tu sent la voiture rouler avec Atlas qui pose sa tête contre ton épaule."

    Narrator  "Tu te réveille un tout petit peu, et porte Taro dans tes bras alors que le mouvement de la voiture qui s'arrète dans un parking te réveille un peu plus."

    Narrator "Tu baille un gros coup et porte ton chat, avant d'ammener les 3 cryptides dans ton appartement."

    Narrator "Avant de succomber au sommeil, tu regarde le coté de ton lit. Atlas est couché sur un matelas a coté de ton lit avec une couverture jetée sur lui. La fatigue t'empèche de le réaliser mais c'est un peu mignon."

    Narrator "Les lumières s'éteignent alors que tu observe Jamie fermer la porte de ta chambre."

    jump Ch1_SundayNightmare

label Ch1_SundayNightmare:
    #Dreaming of Biscuits

    scene BG DreamBedroom
    python:
        timeText = "L'heure du dodo"

        musicPlayer.playSong(song = "dreamlike_state_song",fadeIn=5)
        musicPlayer.playSong(song = "dreamlike_state_song_distorted",music2=True,notif=False)
        renpy.music.set_volume(0.0, delay=0, channel=u'music2')

    with Dissolve(.5)
    nvl show Dissolve(1)
    $displaymenu = True
    NVL_Narrator "Tu est couché sur ton lit d'enfance, tu serre la caméra polaroid dans tes mains. Ce soir, tu vas enfin prendre une photo de ce monstre."

    NVL_Narrator "Tu regarde a travers la vitre, et angule ta lampe dans l'ouverture. Le jardin est vide, pas même le chat de ton voisin est à être appercu."

    NVL_Narrator "Avec un soupir, tu ferme les yeux et baisse ton appareil."

    NVL_DRobyn "C'était peut-être juste un rève après tout."

    NVL_Narrator "..."
    #play sfx donk

    NVL_Narrator "Tu te fait réveiller instantanément par quelqu'un qui gratte contre la vitre."

    NVL_DRobyn "OHMONDIEU!"

    #play sfx donk
    NVL_Narrator "Toc toc"

    NVL_Narrator "Tu porte la caméra a tes yeux, une paire d'énormes yeux te fixent."

    NVL_Narrator "Tu n'as jamais vu un truc du genre avant, C'est ta chance!{nw}"
    menu(nvl=True):
        extend ""
        "Oui.":
            pass
        "Absolument!":
            pass
        "Prendre cette oportunité de vie.":
            pass

    NVL_Narrator "FLASH!"

    NVL_Narrator "Tu prend la photo, la créature frissone derrière la fenètre, aveuglée par le flash."

    NVL_Narrator "Succès! Tu lève ton poing en l'air victorieusement, en essayant de savoir ou est-ce que la créature est allée."

    NVL_Narrator "La fenètre souvre lentement, tu entend une petite voix timide derrière les buissons."

    voice owlet_atlas_pain
    NVL_DreamAtlas "Owww... Pourquoi est-ce que t'a fait ça?"

    NVL_DRobyn "Tu peux parler!?"

    NVL_DreamAtlas "Ouais, Je peux parler. Je suis pas un genre d'alien!"

    NVL_DRobyn "Pourquoi tu regardait par ma fenètre?"

    NVL_DreamAtlas "T'a laissé les lumières allumés!"

    NVL_DreamAtlas "T'a peur du noir?"

    NVL_DRobyn "Même pas vrai!"

    NVL_Narrator "L'étrange créature étire ses ailes et se pose sur le rebords de ta fenètre, posant son dos contre le mur."

    NVL_DreamAtlas "Tu devrais faire plus attention."

    NVL_Narrator "La créature est toute poilue, avec des antennes. Elle porte un T-shirt trop grand et des lunettes, une de ses jambes est pleine de bandages."

    NVL_DRobyn "Qu'est-ce que t'est?"

    voice owlet_atlas_imatlas
    NVL_DreamAtlas "J'suis Atlas!"

    NVL_DRobyn "C'est marrant comme nom."

    NVL_DreamAtlas "Oh ouais? C'est quoi TON nom?"

    NVL_DRobyn "[PCname]."

    NVL_DreamAtlas "Eh bien, [PCname]. T'es chelou."

    NVL_DRobyn "T'est un insecte qui parle!"

    NVL_DreamAtlas "Au cas ou tu n'a pas remarqué. Je suis une Phalène, pas un insecte."

    NVL_DRobyn "C'est pour ça que tu tapais contre la vitre?"

    NVL_DreamAtlas "Ouais... Désolé à propos de ça. Garde les lumières éteintes la prochaine fois."

    NVL_DreamAtlas "Tu sais pas ce que ça peut attirer."

    NVL_DRobyn "Genre quoi?"

    NVL_DreamAtlas "Des cryptides comme moi-"

    NVL_DRobyn "Ca me dérange pas."

    NVL_Narrator "Click."

    $renpy.music.set_volume(1.0, delay=20, channel=u'music2')
    show BG DreamBedroom 2 with { "master" : Dissolve(5.0) }:
        pause 10
        block:
            matrixcolor HueMatrix(0)
            linear 30.0 matrixcolor HueMatrix(360)
            repeat
    NVL_Narrator "Atlas ouvre grand les yeux et réagis au son."

    NVL_DreamAtlas "J-Je dois y aller!."

    NVL_Narrator "Tu entend des bruits de pas et regarde en direction de la porte."

    NVL_DRobyn "Atlas?"

    NVL_Narrator "Il est parti."

    NVL_Narrator "La porte s'ouvre... mais?"

    NVL_DRobyn "Hein?"

    NVL_Narrator "C'est la silouhette de ta mère, mais au lieu d'allumer les lumières et de t'engeuler comme d'habitude, des mots échappent ce que tu crois être sa bouche."

    $Mom = Character("{glitch=30}{color=#70fffb}Mamam?{/color}{/glitch}", image = "mom", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#70fffb",kind=nvl)

    Mom "{glitch=30}Lumières{/glitch}… {glitch=30}Eteintes{/glitch}."

    NVL_DRobyn "Maman?"

    NVL_Narrator "Tu pointe ton polaroid en direction du monstre."

    NVL_Narrator "L'ombre prend une forme différente, comme dans un cauchemard, des dizaines de yeux bleus brilliant sortent de la chair. Elle grogne, elle sort des mots que tu ne peux même pas comprendre."

    $renpy.music.set_volume(0.0, delay=10, channel=u'music')
    NVL_Narrator "T'a jamais vu un truc comme ça avant, c'est ta chance!{nw}"

    menu(nvl=True):
        extend ""

        "Oui?":
            NVL_DRobyn "Mom?"

            NVL_Narrator "Tu pointe la caméra vers elle."

            NVL_DRobyn "Laisse moi tranquile!"

            NVL_Narrator "Tu ferme très fort tes yeux, tu sent le flash sur tes paupières, la créature recule face à la lumière."

            NVL_Narrator "Etrangement, le flash ne se dissipe pas, il envloppe plûtot la salle entière et te couvre les yeux."
        "Je veux pas...":
            NVL_DRobyn "Maman?"

            NVL_Narrator "Tu pointe la caméra, mais..."

            NVL_Narrator "Tu ne peux pas prendre la photo. Ton ésprit est figé. Tu ne peux pas penser ou agir. Avec un dernier souffle tu te pousse sur le coté et ta vision se fade au noir."
        "J'ai peur...":
            NVL_DRobyn "Maman?"

            NVL_Narrator "Tu pointe la caméra, mais..."

            NVL_Narrator "Tu ne peux pas prendre la photo. Ton ésprit est figé. Tu ne peux pas penser ou agir. Avec un dernier souffle tu te pousse sur le coté et ta vision se fade au noir."

            nvl clear

    python:
        songText = "{glitch=50}Leviathan Waltz{/glitch}"
        timeText = "ZZZ"
        musicNote = 4

        renpy.music.set_volume(0.05, delay=10.0, channel=u'music')
        musicPlayer.playSong(song="radioStatic",fadeIn=5,fadeOut=1,music2=True)
        Mom = Character("{glitch=80}{color=#70fffb}Uhtxella'alu{/color}{/glitch}", image = "mom", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#70fffb",kind=nvl)

    play music the_leviathan_waltz_song_tofro fadeout 3.0 fadein 10.0

    scene BG Black with Dissolve(2.0)

    Mom "Je suis désolé…"

    $renpy.music.set_volume(0.0, delay=10.0, channel=u'music2')
    window hide
    scene BG Black with Dissolve(1.0)
    jump Ch1_MondayMorning
