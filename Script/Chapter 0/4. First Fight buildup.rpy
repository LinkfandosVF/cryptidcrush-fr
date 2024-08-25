label fightbuildup:
    $musicPlayer.playSong(song="the_visitor_radio_song",fadeOut=1,fadeIn=5)
    pause 0.01
    scene BG Black
    python:
        timeText = "2:30AM"

        MM_Stats = Unit("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}",1,1,2,0,1,1,25)
        MM_Stats.baseDiff = 5
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(1) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01_MM_MM_ATTACK")
        MM_Stats.SetMTA(3)

        enemyUnits = []
        enemyUnits.append(MM_Stats)

        attackDescA = "Tu veux vraiment que je frappe ce type?!"
        attackDescB = "Ouaaais, je dit pas non à un peu de support émotionel."
        attackDescC = "J'ai l'impression que tu éssaie de me dire un truc..."
        attackDescD = "Hum. Ce nom est un choix original."

        playerUnits[0].attacks = [
                    AttackMove("Frapper",attackDescA, 0, "madlas_tutorial2", "brawn", "hustle", 0, False, [],0),
                    AttackMove("Encourager",attackDescB, 0, "madlas_tutorial2", "charm", "fixed", 1, True, [],7),
                    AttackMove("Focus",attackDescC, 0, "madlas_tutorial2", "brains", "fixed", 2, True, [],8)
                    ]


        playerUnits[0].recoveryRate = 2



        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0])

    camera:
        zoom 2.3
        xcenter 0.65
        ycenter 0.5

    python:
        MD_State["feelerL"] = 1
        MD_State["feelerR"] = 1

        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 2

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter 0.3

    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter 0.7

    with Fade(0.1, 0.2, 2.0, color="#3bec27")

    play voice2 dmm_angryb
    Madlas "Tu ne sais pas qui je suis?!"
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        matrixtransform RotateMatrix(0.0,180.0,180.0)
        pause 0.1
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.1
        matrixtransform RotateMatrix(0.0,0.0,0.0)

    show BG Studio Room Spooky

    show robyn:
        matrixcolor TintMatrix("#95ffba")

    show madlas:
        matrixcolor TintMatrix("#95ffba")

    play voice2 mm_imagoddamnurbanlegend
    Madlas "Je suis une putain de légende urbaine, et je pert mon temps dans ce trou à rats!"
    python:
        MD_State["eyes"] = 2

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,360.0,0.0)

    show BG Studio Room Spooky
    play voice2 mm_dontideservetobefree
    Madlas "Je mérite pas d'être libre!?"
    python:
        MD_State["eyes"] = 3
        MD_State["mouth"] = 4

        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 1

    show BG Studio Room Spooky
    show madlas:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 xcenter 0.4

    play voice2 mm_evenindeath
    Madlas "Putain de merde, même après être mort, je travaille TOUJOURS! Tous les jours, toutes les nuits, tout le temps, pour toujours. POUR TOUJOURS."
    python:
        MD_State["eyes"] = -1
        MD_State["mouth"] = 3


        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2

    show BG Studio Room Spooky
    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 xcenter 0.45
    show robyn:
        pause 0.15
        ease 0.3 xcenter 0.75

    play voice2 mm_wellimdone
    Madlas "J'en ai plus qu'assez de ces menteurs, faux fans, et encore plus de ces putains de chasseur de fantômes! Aucun d'eux n'en avais ne serais-ce que quelque chose à foutre du VRAI MOI!"

    show madlas:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0,0.0,0.0)

    show BG Studio Room Spookier
    play voice2 mm_iquitloud
    Madlas "J'ARRÈTE!"
    python:
        MD_State["mouth"] = 2
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    play voice2 mm_nomore
    Madlas "Plus d'horaires horrible, plus de management, et plus de faux fans!"
    python:
        MD_State["mouth"] = 1
    Narrator "Ses yeux posent leur regard sur ses mains, il bouge chaque doigts un par un."
    python:
        MD_State["mouth"] = 4
        MD_State["eyes"] = 3
    play voice2 mm_whathappenstofakefans
    Madlas "Et tu sais ce que je leur fait aux faux fans?"

    show madlas:
        ease 0.3 xcenter 0.4
    Narrator "Le cryptide rigole, et prend un grand pas en avant."
    python:
        MD_State["mouth"] = 2

        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 2
    show madlas:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0,180.0*3,0.0)

    play voice2 mm_igettheirsouls
    Madlas "JE BOUFFE LEURS ÂMES!"

    $MD_State["eyes"] = -1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1

    show BG Studio Room Spooky
    $Robyn_State["eyes"] = 2

    show madlas:
        pause 0.1
        matrixtransform RotateMatrix(0.0,180.0,0.0)

        parallel:
            ease 0.5 xcenter 0.9 matrixtransform RotateMatrix(0.0,180.0,45.0)
        parallel:
            ease 0.1 yoffset -30
            ease 0.4 yoffset 600
        pause 0.5
        ease 0.5 xcenter 0.75 matrixtransform RotateMatrix(0.0,0.0,0.0) yoffset 0

    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.5 xcenter 0.25 matrixtransform RotateMatrix(0.0,360.0,0.0)

    Narrator "Atlas s'élance en avant, et donne un coup du talon dans le vide te loupant de peu."

    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.1
        ease 0.3 xcenter 0.1

    Narrator "Tu roulle sur le sol depuis ta chaise, et sans le réaliser tu te met à courir vers la porte avec la seule intention de rester en vie."

    $Robyn_State["mouth"] = 4
    show robyn:
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,0.0,0.0)

    Robyn "Atlas, et notre soirée film de vendredi?!"

    Madlas "Atlas ne t'entends paaas!"

    Robyn "On allait faire la version longue de cette triologie fantasie., avec les commentaires du directeur!"

    Narrator "Le mothman s'arrète net, ses antennes pointée dans ta direction."
    python:
        MD_State["eyes"] = 0
        MD_State["mouth"] = 4
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    Atlas "Avec les sous-titres?"

    $Robyn_State["mouth"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)

    Narrator "Tu détruit presque la poignée en éssayant de l'ouvrir."

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 xcenter 0.6 matrixtransform RotateMatrix(0,0,-20) yoffset 100
        ease 0.3 xcenter 0.65 matrixtransform RotateMatrix(0,0,0) yoffset 0

    Narrator "La jampe gauche d'Atlas bouge d'un coté, il tombe presque sur le sol."
    $MD_State["eyes"] = -1
    show madlas:
        yoffset 0
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    play voice2 madlas_stopit
    Madlas "Arrète!"

    show madlas:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.4 xcenter 0.7 matrixtransform RotateMatrix(0,180,90) yoffset 500

    Narrator "Il fait un autre pas en avant, mais tombe miséablement sur le sol comme deux conducteurs qui se battent pour le volant."

    show madlas:
        matrixtransform RotateMatrix(0,180,90)
        ease 0.6 xcenter 0.6 matrixtransform RotateMatrix(0,0,0) yoffset 0
        pause 0.2
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.2 xcenter 0.8
        pause 0.3
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.3 matrixtransform RotateMatrix(0,360,0)
    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    Madlas "T'es cinglé?! On peut pas juster combiner {glitch=40}{i}deux cryptides!{/i}{/glitch} \nLe Radio Man Moth sonne {glitch=60}putain{/glitch} de {glitch=2}stupide!{/glitch}"
    $MD_State["eyes"] = -1
    $Robyn_State['eyes'] = 3
    $Robyn_State['mouth'] = 4
    $MD_State["mouth"] = 0
    Robyn "{size=45}JAMIE À L'AIDE!{/size}"

    python:
        Jamie_Stats = Unit("{color=3AE9F6}Jamie{/color}",1,2,-1,0,-2,3,13)
        Jamie_Stats.Color = "#3AE9F6"
        Jamie_Stats.SetIcon("jamieIcon")

        attackDescA = "Cool! Cool?"
        attackDescB = "Tout est mieux que rien."
        attackDescC = "Un truc cool pourrais arriver... peut-être"
        attackDescD = "Ouais, laisse le DPS faire du soin tant que t'y est. Super game design."

        JamieAttacks = [
                    AttackMove("Pète crâne",attackDescA, 0, "madlas_tutorial2", "guts", "guts", 0, False, [],0),
                    AttackMove("Esprit Brasier",attackDescC, 0, "madlas_tutorial2", "occult", "fixed", 2, False, [],11),
                    AttackMove("Vague Dia",attackDescD, 0, "madlas_tutorial2", "occult", "fixed", 1, True, [],10)
                    ]

        Jamie_Stats.SetAttackMoves(JamieAttacks)
        playerUnits.append(Jamie_Stats)


        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0,1])

        playerUnits[1].recoveryRate = 2

        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 0
        Jamie_State["sweat"] = 1
        Jamie_State["wispEyes"] = 2
        Jamie_State["armR"] = 0
        Jamie_State["mouth"] = 4
        Robyn_State['eyes'] = 0
        Robyn_State['mouth'] = 5

    show robyn:
        pause 0.4
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.7 matrixtransform RotateMatrix(0.0,180*4,0.0) xcenter 0.12

    show jamie:
        matrixcolor TintMatrix("#95ffba")
        xcenter -0.5
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.6 xcenter 0.35

    Narrator "Le démon rentre dans la salle, visiblement confus."

    show jamie:
        ease 0.5 xcenter 0.45
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,360.0,0.0)
        pause 0.5
        ease 0.3 matrixtransform RotateMatrix(0.0,180.0,0.0)

    Narrator "Iel regarde autours, et observe Atlas en train de s'arracher ses propres plumes de colère."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["alFace"] = 1
        Jamie_State["wispEyes"] = 3
        MD_State["mouth"] = 0

    voice jamie_surpriseb
    Jamie "...Atlas est devenu plus grand?"

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 3
        Robyn_State["mouth"] = 4

    Robyn "C'est le premier truc que t'a remarqué?!"

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["alFace"] = 0

        Jamie_State["eye"] = 7
        Jamie_State["fire"] = 0
        Jamie_State["armR"] = 2
        Jamie_State["r3Fire"] = 1
        Jamie_State["sweat"] = 0
        Jamie_State["wispEyes"] = 1

    Jamie "C'est impardonable."

    voice dmm_laughb
    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish

    python:
        Robyn_State["eyes"] = -1
        Robyn_State["mouth"] = 3
        MD_State["mouth"] = 1
        MD_State["eyes"] = 0
        MD_State["feelerL"] = 0
        MD_State["feelerR"] = 0

    Madlas "Awwww,, t'a pas l'habitude d'être {glitch=8}le nain{/glitch} que tout le monde utilise comme accoudoir?"
    show madlas:
        xcenter 0.8
    python:
        Jamie_State["eye"] = 6
        Jamie_State["mouth"] = 2
        Jamie_State["steam"] = 1

        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 4

        MD_State["mouth"] = 0
        MD_State["eyes"] = -1

    Robyn "C'est pas un concours!"

    Jamie "T'a raison,., et les antennes ne comptent pas."

    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 0
    $Jamie_State["steam"] = 0

    Jamie "Je crois là c'est le moment où on se bat."

    python:
        Robyn_State["mouth"] = 5
        Robyn_State["brow"] = 2

        MD_State["mouth"] = 1

    Robyn "Mais ça va le blesser!"

    $MD_State["mouth"] = 2

    voice dmm_yawn
    Madlas "On donc maintenant tu t'en préocupe! Genre,., [PCname] je pensais que t'était censé me {glitch=8}protéger.{/glitch}"
    $Robyn_State["mouth"] = 4
    Robyn "H-hein?"

    Jamie "On va le faire vite."

    python:
        songText = "The Visitor"
        timeText = "2:30AM?"

    show BG Studio Room Spooky
    camera:
        zoom 1.0 xcenter 0.5 ycenter 0.5
        matrixtransform RotateMatrix(0,0,180)
        pause 0.2
        matrixtransform RotateMatrix(0,180,0)
        matrixcolor HueMatrix(180)

    call makeCheckpoint from _call_makeCheckpoint_1
    show Flickering Black
    pause 0.65
    play music elkhorn_radio_intro_song noloop
    pause (4.3)

label madlas_tutorial:

    play music urgently_jammin_sir_meow_remix_intro
    $musicPlayer.playSong(song="urgently_jammin_sir_meow_remix_loop",queueSong=True)

    scene BG Studio Room Spookier:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)

    camera at camera_default
    camera:
        matrixcolor HueMatrix(0)
        matrixtransform RotateMatrix(0,0,0)

    $MD_State["mouth"] = 2

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        yoffset 700
        xcenter 0.5
        ycenter 0.6

        ease 1.09 yoffset 0
        block:
            yoffset -10
            parallel:
                ease 0.2725 yoffset 0
                pause 0.2725
                yoffset -10
                ease 0.2725 yoffset 0
                pause 0.2725
            parallel:
                pause 0.545
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,360,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,180,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,0,0)

            repeat

    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    Narrator "{glitch=30}Madlas{/glitch} te rit au visage!"

    $MD_State["eyes"] = 2
    Narrator "{glitch=20}Madlas{/glitch} t'envoie une enceinte sur-dimensionnée au visage par une force surdimentionelle!"

    call dice_roll(playerUnits[1].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Psycho lance") from _call_dice_roll_13

    $xDmg = -(renpy.random.randint(6,10))
    show MMFight_Chair at MMFight_LeftProp_Exit
    show MMFight_Speaker at MMFight_RightProp_Exit

    if isRollSuccess:
        Narrator "Jamie se met hors du chemin!"
    else:
        $playerUnits[1].modifyHP(xDmg,0.0,"guts")
        $RefreshBarHP()
        Narrator "Jamie se la prend en pleine poire, et prend [sfxDmg] dommages!"

    play voice2 dmm_laughc
    $ToggleBarState([1], 0)
    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry
    Madlas "Bwahaha, imbéciles! Est-ce que vous ne-serais-ce qu'essayez?"
    show MMFight_Chair at MMFight_LeftProp_Exit
    show MMFight_Speaker at MMFight_RightProp_Exit

    Narrator "{glitch=20}Madlas{/glitch} lance un coup de griffes au démon qui ésquive rapidement l'attaque."
    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    Jamie "{b}{sc=2}[PCname], J'AI BESOIN D'ORDRES.{/sc}{/b}"

    Robyn "M-mais qu'est-ce que je suis censé faire?!"

    Jamie "Choisis une attaque dans le coin supérieur gauche!"

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

    jump madlas_tutorial

label madlas_tutorial2:
    show robyn:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)
        xcenter 1.3
        yoffset 50
        matrixtransform RotateMatrix(0,0,0)

        ease 1.0 xcenter 1.0 matrixtransform RotateMatrix(0,0,-45)

    voice RobynSays("Generic","ConfusedA")
    if isRollSuccess:
        Robyn "Ooookay c'est reussi, et maintenant?"
    else:
        Robyn "Ooouuais, j'ai loupé? Maintenant quoi?"

    show MMFight_Chair:
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0*3)
        parallel:
            ease 0.75 yoffset -800

    show MMFight_Speaker:
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0*3)
        parallel:
            ease 0.75 yoffset -800

    show madlas:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.5
        yoffset 0
        ease 0.545 xcenter 0.2 matrixtransform RotateMatrix(0,180,0)
        block:
            yoffset -10
            ease 0.2725 yoffset 0
            pause 0.2725
            repeat

    show jamie:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)
        xcenter 1.3
        matrixtransform RotateMatrix(0,0,0)

        ease 1.0 xcenter 1.1 matrixtransform RotateMatrix(0,0,-45)
    $Jamie_State ["fire"] = 0
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 1

    Jamie "COOL. Laisse moi éxpliquer les bases. \n\n{size=-10}          Merde. Par quoi je commence? {/size}\n\nTu um."
    hide MMFight_Speaker
    hide MMFight_Chair
    $MD_State["eyes"] = 6

    python:
        displaymenu = True
        preferences.text_cps = 30

    Jamie "Tu vois.{nw}"
    $preferences.text_cps = 32
    $Jamie_State ["eye"] = 3

    Jamie "Damage. Base Damage.{nw}"
    $preferences.text_cps = 33

    Jamie "{nw}"
    $preferences.text_cps = 34
    $Jamie_State ["eye"] = 0
    $Jamie_State ["mouth"] = 1
    $Jamie_State ["brow"] = 1

    Jamie "Et après tu simule l'action et-{nw}"
    $preferences.text_cps = 36
    $Jamie_State ["mouth"] = 2
    $Jamie_State ["brow"] = 3

    Jamie "Les modificateurs- rajoutent des chiffres-{nw}"
    $preferences.text_cps = 37

    $Jamie_State ["mouth"] = 0

    Jamie "Stamina, fatigue, Infos..,{nw}"
    $preferences.text_cps = 41

    Jamie "Ma tête fait mal-.,{nw}"
    $preferences.text_cps = 42

    Robyn "H-hey tout vas bien, prend ton temps.,-{nw}"
    $preferences.text_cps = 60

    Jamie "Les modifications physique-{nw}"
    $preferences.text_cps = 50


    $Jamie_State ["hurt"] = 1
    $Jamie_State ["eye"] = 4


    Jamie "J'suis en train de saigner du nez là?{nw}"
    $preferences.text_cps = 46

    Robyn "Réspire-.,{nw}"
    $preferences.text_cps = 30

    Jamie "Je peux pas faire ça.,-{nw}"
    $preferences.text_cps = 48

    $Jamie_State ["steam"] = 1
    $Jamie_State ["eye"] = 6
    $Jamie_State ["brow"] = 0


    Jamie "Si je blesse Atlas., je me le pardonnerais jamais., roh putain, je suis vraiment le diable.,!{nw}"
    $preferences.text_cps = 60

    $Jamie_State ["armR"] = 3
    $Jamie_State ["hurt"] = 0
    $Jamie_State ["fire"] = 0
    $Jamie_State ["wispEyes"] = 4
    $Jamie_State ["steam"] = 0

    python:
        displaymenu = False
        preferences.text_cps = 30
    $Robyn_State["mouth"] = 4
    $Robyn_State["eyes"] = 0
    Robyn "{b}{sc=2}ATLAS À L'AIDE!{/sc}{/b}"

    $MD_State["mouth"] = 1
    $MD_State["eyes"] = 6
    $displaymenu = True

    Madlas "Pas mon problème."

    $MD_State["eyes"] = 0
    show madlas:
        linear 0.05 xcenter 0.200
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        pause 0.2
        repeat
    Madlas ".,.,{nw}"
    $MD_State["eyes"] = 6
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1
    $MD_State["mouth"] = 0
    show madlas:
        block:
            yoffset -10
            ease 0.2725 yoffset 0
            pause 0.2725
            repeat
    Madlas "{size=40}NON!{/size} \n\nJ'EXPLIQUERAIS PAS CETTE MERDE!"
    $MD_State["mouth"] = 3
    $MD_State["eyes"] = -1
    Madlas "{sc=1}Ferme là et bats toi!{/sc}"
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 4
    $Robyn_State["brow"] = 2
    Robyn "{bt=4}Steuplaaaait?{/bt}"

    Madlas ".,.,{nw}"
    $MD_State["mouth"] = 4
    $MD_State["eyes"] = 0

    show madlas:
        linear 0.05 xcenter 0.200
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.206
        linear 0.05 xcenter 0.2
        pause 0.2
        repeat
    Atlas "{size=40}Okay! Si tu veux!{/size}"

    Narrator "On dirait que le l'envie d'aider ses amis a l'interieur d'Atlas est plus forte que la haine de Madhouse."
    show madlas
    $MD_State["eyes"] = 4
    $MD_State["feelerL"] = 0
    $MD_State["feelerR"] = 0
    $firstLoop = True
    jump madlas_tutorialQuestions

default tQcanAsk = [True,True,True,True]
label madlas_tutorialQuestions:
    $displaymenu = True
    show madlas at startledSquish #.Startled Squish

    if firstLoop:
        Atlas "Donc, qu'est-ce que tu veux savoir?{nw}"
        $firstLoop = False
        $tQcanAsk = [True,True,True,True]
    elif True in tQcanAsk:
        Atlas "Autre chose?{nw}"

    menu:
        extend ""

        "Les stats" if tQcanAsk[0]:
            $displaymenu = False
            $tQcanAsk[0] = False
            $MD_State["eyes"] = 5
            Atlas "Bon y'a 6 stats: [kwBrawn], [kwBrains], [kwGuts], [kwHustle], [kwCharm], et [kwOccult]!"

            Atlas "[kwBrawn] C'est t'a force physique. C'est un modificateur pour les attaques physiques, typiquement."

            Atlas "[kwBrains] c'est la somme de tes capacités mentales. C'est un peu tout ce qu'il est utilisé pour les recherches en dehors des combats et ta résistance contre les attaques PSI."

            Atlas "[kwGuts] c'est ta constitution physique et forme générale. C'est genre la défense, pour résister aux poisons, affectations de status, et aussi ta résistance contre tout le reste en fait."

            Atlas "[kwHustle] c'est genre ta vision et réaction. C'est un peu la vitesse de chaque trucs que tu fait."

            Atlas "[kwCharm] c'est le charisme. C'est plûtot en dehors des combats pour convaincre les gens, ce genre de truc."

            Atlas "[kwOccult] c'est ton affinitée au supernaturel. Toutes les actions en dehors de la catégorie du physique c'est de l'occulte."

            Atlas "Toute ces stats modifient les lancés, et aussi les réductions/augmentations de dégats pour ce que tu éssaie de faire. Y'a aussi des stats que dans les combats, comme [kwPowerMod], [kwPDefense], et [kwSDefense]."

            Atlas "[kwPowerMod] c'est un bonus additionel pour l'attaque. A partir du [kwPowerMod] c'est un bonus pour les lancés sur l'attaque."

            Atlas "[kwPDefense]/[kwSDefense] c'est la même chose, mais pour la défense contre certaines attaques."

            Atlas "Les dommages sont coupés en 2 parties, physique et supernaturel, Les attaques physiques sont bloqués par [kwGuts] et les super naturelles sont atténués par [kwOccult]."

            $MD_State["eyes"] = 0
            jump madlas_tutorialQuestions

        "Les actions et leur effets" if tQcanAsk[1]:
            $displaymenu = False
            $tQcanAsk[1] = False
            Atlas "Oh c'est simple!"

            Atlas "En gros ça fonctionne comme ça:"
            $MD_State["eyes"] = 0
            Atlas "{size=-5}Tu verras [kwSuccess] si sa reussi.\n\n Tu verras[kwFailure] si tu loupe.\n\nEn gros c'est {color=#83ed6e}(Ton modificateur){/color} vs {color=#7aff44}(Le modificateur adverse ou La difficultée (X)){/color}\nCoûte: X Stamina{/size}"

            Atlas "Si une attaque fait des dégats, pour savoir si c'est [kwPDefense] ou [kwSDefense] qui joue sur la défense, juste pense à ce que la skill fait."
            $MD_State["eyes"] = 5
            Atlas "Si tu frappe, c'est [kwPDefense], mais si c'est une boule de feu par éxemple, c'est [kwSDefense] qui compte."
            jump madlas_tutorialQuestions

        "Stamina, Fatigue & Récupération" if tQcanAsk[2]:
            $displaymenu = False
            $tQcanAsk[2] = False
            Atlas "Tout les Skills requirent un nombre de stamina de 0 à 5, et tout les membres de l'équipe ont une stamina de 0-4."

            Atlas "Si tu loupe ton tour, tu pert la stamina montrée, mais tout les membres de l'équipe non affectés gagnent +1 de stamina. Plusieurs Skills utilisent plusieurs alliés pour se lancer, alors garde ça en tête."

            Atlas "Si tu utilise une Skil alors que la demande de stamina est plus grande que ton énergie actuelle tu va dans le négatif, mais si cela arrive, tu deviens fatigué. Tu pourras pas attaquer tant que tu auras pas récupéré."
            jump madlas_tutorialQuestions

        "Enemy Attaques, MTA, & Difficultée" if tQcanAsk[3]:
            $displaymenu = False
            $tQcanAsk[3] = False
            $MD_State["eyes"] = 5
            Madlas "[kwMTA] {size=-9}(Moves Until Attack){/size} c'est simple! C'est le nombre de tours que tu dois attendre avant que la cible en question ne puisse agir."

            Atlas "C'est un petit décompte sympa avant que ont puisse te faire bobo!"

            Atlas "Certains ennemis peuvent attaquer plusieurs fois quand le compteur est à 0, Donc les ennemis qui s'attaquent ou aggissent entre eux attaquent forcément plusieurs fois."

            Atlas "Et aussi, les alliés KO. Si un ami est KOed, n'importe quel soin peut le rammener au dessus de 0 health. Il n'y a pas de résuréction après tout!"

            Atlas "Pour équilibrer, quand le tour d'un ennemi fini et que un allié est KO, sont délai MTA est déscendu de 1 point par alliés KO."

            Madlas "Par éxemple, si tu à une équipe de 4 et que 2 de tes alliés sont KO, L'ennemy devrait avoir un nombre de tour max de 5. Son délair seras mis à 3, parce que 2 membres de ton équipe étant KO rend le procéssus plus rapide!"
            $MD_State["eyes"] = 0
            jump madlas_tutorialQuestions

        "J'ai compris!" if True in tQcanAsk:
            Atlas "Cool!"
            pass
            $MD_State["eyes"] = 4
            $MD_State["mouth"] = 4
    $MD_State["eyes"] = 4
    Atlas "Je crois que c'est tout!"
    $MD_State["eyes"] = 1

    Atlas "Hey,, Jamie? Tout vas bien."

    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1
    voice dmm_laughb
    Madlas "Explose moi son cul."

    show jamie:
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        ease 0.06 yoffset 2
        ease 0.06 yoffset -2
        pause 0.3
        repeat

    voice jamie_growlb
    Jamie "..."
    show jamie:
        ease 0.08 yoffset 5
        ease 0.08 yoffset -5
        ease 0.08 yoffset 5
        ease 0.08 yoffset -5
        ease 0.04 yoffset 0
        pause 0.2
        repeat

    $Jamie_State["eye"] = 7
    $Jamie_State["fire"] = 1
    $Jamie_State["armR"] = 2
    $Jamie_State["r3Fire"] = 1
    $Jamie_State["wispEyes"] = 1
    $Jamie_State["mouth"] = 1

    Narrator "Jamie est complètement enragé, une lueure de détermination brille dans ses yeux. Ca t'inspire aussi,, peut être que tu peux y arriver. Peut être que tu peux faire ça."

    show robyn:
        ease 0.5 xcenter 1.5
    show jamie:
        ease 0.6 xcenter 1.5
    $Jamie_State["r3Fire"] = 0
    Robyn "Sauvons Atlas!"

    $MD_State["eyes"] = 2
    $MD_State["mouth"] = 2
    $MD_State["feelerL"] = 0
    $MD_State["feelerR"] = 0
    if gameVersion == 3:
        $displaymenu = True
        Narrator "Passer le combat?{nw}"
        menu:
            extend ""
            "Yes":
                $displaymenu = False
                jump buildup_to_MM_Fight
            "No":
                $displaymenu = False
    call FIGHT_00_MADLAS from _call_FIGHT_00_MADLAS

    jump buildup_to_MM_Fight

label buildup_to_MM_Fight:
    show madlas:
        ease 0.545 xcenter 0.5 matrixtransform RotateMatrix(0,0,0)
    $MD_State["mouth"] = 0
    $MD_State["eyes"] = -1
    voice dmm_angryb
    Madlas "Vous avez vraiment cru que vous pouviez me battre? \n\n{sc=3}QUELLE BLAGUE!{/sc}"
    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish
    $MD_State["mouth"] = 1
    $MD_State["eyes"] = 0
    $MD_State["feelerR"] = 1
    $MD_State["feelerL"] = 1
    Madlas "Tu à les yeux devant le prochain Mothamn, baby! Ouais nan! Pas {b}UN{/b} mothman,, mais \n{b}LE MOTHMAN{/b}!"
    show madlas:
        parallel:
            hoppies_flipped(xIntensity=2)
        parallel:
            startledSquish
    Madlas "Plus d'ignorance ou de dégout, \n\nJuste de la pure, {glitch=30}TERREUR CRYSTALINE!{/glitch}"

    show madlas:
        parallel:
            hoppies(xIntensity=2)
        parallel:
            startledSquish
    Madlas "J'suis une légende!"
    show madlas:
        ease 0.15 yoffset -30
        ease 0.15 yoffset 0

    Madlas "J'suis un démon!"

    $MD_State["mouth"] = 5
    $MD_State["eyes"] = 2
    show madlas:
        linear 0.05 xcenter 0.500
        linear 0.05 xcenter 0.506
        linear 0.05 xcenter 0.5
        linear 0.05 xcenter 0.504
        linear 0.05 xcenter 0.502
        linear 0.05 xcenter 0.5
        pause 0.2
        repeat
    $MD_State["eyes"] = 0
    $MD_State["mouth"] = 1
    $MD_State["feelerL"] = 1
    $MD_State["feelerR"] = 1

    Madlas "{sc=6}Je suis—{/sc}"
    python:
        musicNote = 3
        songText = "Awkward Silence"
    play sfx emote_frustration
    $musicPlayer.playSong()
    show madlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(1.0, 0.0, 2.0)
        zoom 1
        alpha 1
    narrator "{nw}"
    hide madlas

    $Atlas_State["eye"] = 7
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Atlas_State["feelers"] = 1
    show atlas:
        xcenter 0.5

    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(1.0, 0.0, 2.0)
        zoom 1
        alpha 1

    Narrator "Poof."

    show atlas:
        linear 0.05 xcenter 0.500
        linear 0.05 xcenter 0.504
        linear 0.05 xcenter 0.5
        linear 0.05 xcenter 0.503
        linear 0.05 xcenter 0.502
        linear 0.05 xcenter 0.5

    $Atlas_State["eye"] = 5
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    $Atlas_State["feelers"] = 0

    Atlas "Je suis un peu léger de la tête."
    $Atlas_State["eye"] = 13

    voice taro_angryb
    Taro "{sc=1}SAIS OU TU DOIS ÊTRE!{/sc}"
    $BTaro_State['mouth'] = 2
    $BTaro_State['eye'] = 1
    camera:
        pause 0.23
        xoffset -15
        ease 0.06 xoffset 15
        ease 0.06 xoffset -13
        ease 0.06 xoffset 11
        ease 0.06 xoffset -9
        ease 0.06 xoffset 7
        ease 0.06 xoffset -5
        ease 0.06 xoffset 3

        ease 0.03 xoffset 0

    python:
        Taro_Stats = Unit("{color=#C064FF}Taro{/color}",2,-1,1,2,0,-1,14)
        Taro_Stats.Color = "#C064FF"
        Taro_Stats.SetIcon("taroIcon")

        attackDescA = "[kwSuccess] Dommages mediums à une cible. Quand Taro est à moins de [kwHealth], fait des dommages lourds.\n\n[kwFailure] Moins de résultats\n\nUtilise[kwBrawn] vs [kwHustleD]\nCoût: 2 Stamina"

        attackDescB = "[kwSuccess] Taro intércepte toute attaque, et augmente légèrement sa [kwDefenseMod]. Elle garde la stat ansi jusqu'a l'utilisation d'une autre Skill.\n\n[kwFailure] Fonctionne, mais diminue légèrement la [kwDefenseMod] de Taro. Augmente aussi son [kwPowerMod].\n\nStats: [kwGutsD] vs Fixé(7)"

        attackDescD = "[kwSuccess] Baisse le [kwPowerMod] de la cible, et monte légèrement son [kwDifficultyModD].\n\n[kwFailure] Monte le [kwPowerMod] de la cible.\n\nStats: [kwCharm] vs [kwBrainsD]\nCoût: 3 Stamina"

        TaroAttacks = [
                    AttackMove("Pounce",attackDescA, -2, "FIGHT_01_MM_TARO_0", "brawn", "hustle", 0, False, [],0),
                    AttackMove("Tuna Defender",attackDescB, 0, "FIGHT_01_MM_TARO_1", "guts", "fixed", 2, True, [],7),
                    AttackMove("Jeer",attackDescD, -3, "FIGHT_01_MM_TARO_3", "charm", "brains", 0, False, [],10)
                    ]
        Taro_Stats.SetAttackMoves(TaroAttacks)
        playerUnits.append(Taro_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0,1,2])

    $audio.delayedThunk = ["<silence .23>", "audio/SFX Battle/Hurt_D.ogg"]
    show tarobig:
        xcenter -0.5
        ease 0.3 xcenter 0.5
    $Atlas_State["eye"] = 3
    show atlas:
        pause 0.23
        matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 1.0 xcenter 1.5
        parallel:
            ease 0.4 yoffset -300
            ease 0.4 yoffset 600
        parallel:
            ease 1.3 matrixtransform RotateMatrix(0,0,360*3)

    play sfx delayedThunk

    Narrator "La porte se fait éxploser contre le mur, elle souvre en deux alors qu'une version monstrueuse de Taro apparait dans la salle. Avec un miaulement victorieux elle éjecte Atlas au sol."
    hide atlas
    $BTaro_State['mouth'] = 1
    $BTaro_State['eye'] = 2
    show tarobig:
        ease 10 xcenter -0.5
    Narrator "Balancé sur le sol, Atlas laisse éxtraire une quantitée atroce de Toxic Waste depuis son horifice bucal. Il vomis,, en gros."

    Robyn "{sc=2}Taro c'est quoi ton {b}problème{/b}!{/sc}., Atlas tout vas bien?!"

    Narrator "Atlas te donne un petit pouce en l'air."

    python:
        Atlas_Stats = Unit("{color=#ED2A82}Atlas{/color}",-1,2,2,-1,1,0,13)
        Atlas_Stats.Color = "#ED2A82"
        Atlas_Stats.SetIcon("atlasIcon")

        attackDescA = "[kwSuccess] Délai le tour ennemis.\n\n[kwFailure] Fonctionne mais la stamina de tout le monde est réduite à 0. (sauf Atlas).\n\nStats: [kwBrainsD] vs Fixé(10)\nCoût: 3 Stamina"

        attackDescB = "[kwSuccess] Gros dommages, et baisse le [kwBrainsD] de la cible. Atlas prend 30% de contre.\n\n[kwFailure] Fonctionne mais le [kwBrainsD] d'Atlas est baissé, il prend aussi 60% de contre.\n\nStats: [kwOccultD] vs [kwBrainsD]\nCoût: 4 Stamina"

        attackDescC = "[kwSuccess] Jamie regagne +1 stamina, et son [kwOccultD] ainsi que son [kwBrawn] sont augmentés. \n\n[kwFailure] Les stats [kwOccultD] et [kwBrawn] de Jamie montent un petit peu.\n\nStats: [kwCharm] vs Fixé(10)\nCoût: 1 Stamina"


        AtlasAttacks = [
                    AttackMove("Étalage de lore",attackDescA, -3, "FIGHT_01_MM_ATLAS_0", "brains", "fixed", 2, False, [],10),
                    AttackMove("Kinésis α",attackDescB, -4, "FIGHT_01_MM_ATLAS_1", "occult", "brains", 0, False, [],7),
                    AttackMove("Bon Mindset",attackDescC, -2, "FIGHT_01_MM_ATLAS_2", "charm", "fixed", 2, True, [],10)
                    ]

        Atlas_Stats.SetAttackMoves(AtlasAttacks)
        Atlas_Stats.cHP = 3
        playerUnits.append(Atlas_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0,1,2,3])

    Atlas "Je vais bien."
    Atlas "Désolé de t'avoir fait peur."
    Narrator "Tu aide Atlas a se relever, et garde ton bras autours de lui avant de regarder autours nerveusement. Où est Madhouse?"

    hide tarobig

    Jamie "Mike espèce de connard!"

    Narrator "Regardant dans les airs, le démon crache une bouffée de feu bleu alors qu'iel lance des poings dans le vide qu'est le corps de Mike."

    Taro "Prrrh, tu crois vraiment que ça va marcher?"
    $musicPlayer.playSong(song="not_so_spooky_song",fadeIn=1)

    Narrator "Lanceant un autre coup, Jamie grince alors qu'il touche en fait la main ouverte de Madhouse."
    voice mm_booa
    Madhouse "Connard?"
    voice mm_laughe
    Narrator "Le fantôme résume un sourire narquois en arrètant le poing de Jamie."

    voice jamie_surpriseb
    Jamie "-!{nw}"

    Madhouse "Je te l'ai déja dit, je—"

    Narrator "Rien à foutre. Elle donne un gros coup de tête sur le spectre le laissant bouche-bé."

    Madhouse "Je travaille pas avec les—"

    Narrator "Iel lance un autre coup, Jamie frappe une nouvelle fois le torse de Madhouse."

    Madhouse "{sc=1}Laisse moi finir!{/sc}"

    Narrator "Ils sont tout les deux bloqués. Jamie ne peux pas bouger ses bras."

    Narrator "Iel mors et se débat,, d'une manière très violente malgré l'efficacitée de l'acte proche du zéro absolu."
    voice mm_laughawkward
    Madhouse "Arrète de ruiner l'instant, tête d'os."

    Narrator "Madhouse serre plus fort sur son emprise."

    Jamie "., Tu n'hoserais pas."

    $musicPlayer.playSong(song="drink_it_song",fadeOut=1,fadeIn=3)
    voice mm_laugha
    Madhouse "Quoiii? J'ai jamais possedé un démon avant!"

    Jamie "Ton âme se ferait {i}carboniser!{/i}"

    voice mm_yawn
    Madhouse "Et alors?"

    Madhouse "J'men fout,, {bt=2}dans les deux cas c'est gagnant-gagnant!{/bt}"


    camera:
        pause 0.4
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.1 xoffset 7
        ease 0.1 xoffset -7
        ease 0.05 xoffset 0


    show demon_madhouse at MMD_Entry_Pos

    Narrator "La mâchoire de Madhouse se déchaîne soudainement, une corne recourbée dépassant du côté de sa tête. Il met une main sur son visage et étouffe un cri, sa forme horrible vacillant dans les lumières irisées"

    Jamie "Je t'ai dit que ça marcherais pas!"

    Narrator "Jamie se dégage enfin de l'emprise de Madhouse, iel secoue ses main maintenant pleine d'éctoplasme."
    if gameVersion == 3:
        $displaymenu = True
        Narrator "Skip Fight?{nw}"
        menu:
            extend ""
            "Yes":
                $displaymenu = False
                jump MM_fightAftermath
            "No":
                $displaymenu = False

    call FIGHT_01_MADHOUSE from _call_FIGHT_01_MADHOUSE_1
    jump MM_fightAftermath




#GO TO MMFight.RPY #1 FOR THE FIGHT