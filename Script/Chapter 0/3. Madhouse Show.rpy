transform radio_camera:
    ease 5.0 ycenter 0.82 xcenter 0.73 zoom 1.49

transform quick_radio_camera:
    ease 1.0 ycenter 0.82 xcenter 0.73 zoom 1.49

transform radio_atlas_cameraA:
    ease 0.5 zoom 2.3 ycenter 0.97 xcenter 0.75

transform radio_madhouse_cameraA:
    ease 0.5 xcenter 0.95 zoom 2.1 ycenter 0.95

label RadioShow:
    show Flickering Black
    pause 0.65
    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    pause (4.3)
    scene black
    $musicPlayer.playSong(song="elkhorn_radio_song",fadeIn=1)

    python:
        Robyn_State["brow"] = 0
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 9
        MM_State["armR"] = 0
        MM_State["armL"] = 0
        MM_State["hair"] = 0
        MM_State["outfit"] = 0

        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 0

        Taro_State["mouth"] = 0
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0

        Jamie_State["eye"] = 0
        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["armL"] = 0
        Jamie_State["armR"] = 0
        Jamie_State["pants"] = True
        Jamie_State["rings"] = True,
        Jamie_State["alFace"] = False
        Jamie_State["blush"] = False
        Jamie_State["sweat"] = False
        Jamie_State["fire"] = False
        Jamie_State["r3Fire"] = False
        Jamie_State["steam"] = False
        Jamie_State["hurt"] = False
        Jamie_State["wispEyes"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 7
        MM_State["armR"] = 0
        MM_State["armL"] = 0

        Atlas_State["armL"] = 1


    Madhouse "Bonsoir, fantômes et ghoules! On est de retour en live à Elkhorn Radio, juste a coté de la Route 101 pour ceux qui passent pas loin. Je suis votre hôte préféré, Madhouse Mike, et bienvenu sur l'heure fantôme!"

    show madhouse:
        xcenter 0.8
        yoffset 140
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Madhouse "Et ce soir est plûtot spécial! On à des invités spécial du royaume des vivants! Pourquoi ne pas vous présenter?"

    python:
        MM_State["eyes"] = 4
        MM_State["mouth"] = 0

    show madhouse:
        matrixcolor BrightnessMatrix(0)

    Narrator "Mike acquiesce de la tête, vous fesant signe d'avancer."
    python:
        Atlas_State["feelers"] = 1
        Atlas_State["eye"] = 9
        Atlas_State["eyeFrame"] = 0

    show atlas:
        xcenter 0.5
        yoffset 130
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Atlas "Lex si tu entend, tu me dois 20 balles."
    show atlas:
        matrixcolor BrightnessMatrix(0)
    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

        Robyn_State["brow"] = 3
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 1

    show robyn behind atlas:
        xcenter 0.35
        yoffset 110
        matrixcolor BrightnessMatrix(-1)
        ease 0.25 matrixcolor BrightnessMatrix(0)

    Robyn "{size=-6}C'est pas le moment.{/size}"
    scene BG Studio Room Dark
    $Robyn_State["mouth"] = 1

    show madhouse:
        xcenter 0.8
        yoffset 140

    show atlas:
        xcenter 0.5
        yoffset 130
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn behind atlas:
        xcenter 0.35
        yoffset 110


    camera at radio_camera
    Narrator "Tu chuchote au mothman, un regard un peu déconcertant."
    python:
        Robyn_State["mouth"] = 0
        Robyn_State["brow"] = 0
    show BG Studio Room

    Robyn "Je suis [PCname] et voici Atlas. On est tout les deux de grands fans!"

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 9

    voice mm_woah
    Madhouse "Wow, tu dois avoir des boules pour avoir enménagé dans une ville pleine de cryptides."
    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 4
        Atlas_State["eye"] = 0

    Robyn "Je suppose?"

    $Atlas_State["eye"] = 13
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5

    Madhouse "Ca fesait peur?"

    $Robyn_State["mouth"] = 5
    $Atlas_State["eye"] = 0

    Robyn "Un peu,, Mais je sais que j'irais bien avec mon gardien cosmique autour."

    $Robyn_State["mouth"] = 0
    $Robyn_State["eyes"] = 2
    $MM_State["mouth"] = 10
    Madhouse "Ton quoi?"
    $Robyn_State["brow"] = 2
    Robyn "Mon chat fantôme Taro! Elle est censé me protéger, mais heu... Elle a tendance à en faire un peu qu'a sa tête."

    $Atlas_State["eye"] = 0
    $Atlas_State["eyeFrame"] = 5
    $Atlas_State["armL"] = 2
    $MM_State["mouth"] = 0

    Atlas "Même, où est-ce qu'elle est?"

    $MM_State["mouth"] = 9

    Madhouse "On dirait que t'a vraiment une affinitée pour les esprits."

    $Robyn_State["eyes"] = 4
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["armL"] = 0
    $Atlas_State["eye"] = 1

    Atlas "Et un aimant pour les problèmes."

    $Robyn_State["mouth"] = 6
    $Robyn_State["brow"] = 1
    $Robyn_State["eyes"] = 3
    $Atlas_State["eye"] = 16

    Narrator "Toi et Atlas vous échangez des sourires narquois."


    python:
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

        MM_State["eyes"] = 5
        MM_State["mouth"] = 0

        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0

    Madhouse "Eh bien je suppose que on va avoir des {b}problèmes{/b}, puisque voici le seul et unique Mothman. Prophète du pont d'argent, créateur de désastres! Donc c'est comment d'être la loie de Murphy incarnée?"
    camera at radio_atlas_cameraA

    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 5
        Atlas_State["feelers"] = 0

    Atlas "Nan, ce serait plûtot... mon père. Je suis juste {i}UN{/i} mothman, pas {i}LE{/i} Mothman. Je peux pas vraiment contrôler mes visions non plus."

    python:
        Atlas_State["eye"] = 6
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 1

    Atlas "J'éssaie juste d'aider un pote maudit."
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

    Robyn "Tu peux voir le futur?!"
    $Atlas_State["eye"] = 0

    camera at radio_madhouse_cameraA

    $MM_State["mouth"] = 7
    $MM_State["eyes"] = 0


    Madhouse "Oh ouais! Fait nous une prédiction, mothman!"

    $Atlas_State["eye"] = 14
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0

    Narrator "Atlas a l'air un peu phasé sur le moment. Presque paniqué."
    $Atlas_State["eye"] = 12
    $Atlas_State["eyeFrame"] = 1

    Atlas "Genre là toute suite?\n\nJ-je voulais parler de la {i}malédiction{/i} de [PCname] !"

    Robyn "{size=-6}C'est pas grave juste suit le rythme.{/size}"

    $MM_State["mouth"] = 11
    $Robyn_State["brow"] = 2
    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 0
    $MM_State["armR"] = 1
    $MM_State["armL"] = 1

    Madhouse "Y'a quoi dans mon futur?"

    camera at radio_atlas_cameraA

    Atlas "Okay, ouais! Bien sûr, haha, {i}ouais{/i} je... Je peux essayer."

    $Atlas_State["eye"] = 20
    $Atlas_State["feelers"] = 1
    $Robyn_State["mouth"] = 1
    $Robyn_State["eyes"] = 0

    Narrator "Il ferme les yeux et pench sa tête sur le coté, comme si il essayait d'écouter un truc."

    Atlas "...{nw}"
    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        zoom 1
        alpha 1
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

        musicPlayer.playSong()


    Atlas "{size=35}NOPE, OUBLIE!{/size} \n\n Je peux pas faire ça."

    Madhouse "Pourquoi pas?"

    $Atlas_State["feelers"] = 1
    $Atlas_State["eye"] = 16
    voice atlas_nervouslaugh

    Atlas "Je suppose que l'avenir des fantômes est trop dûr a prédire. Pardon pardon."

    $Atlas_State["eye"] = 7
    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 2
    $MM_State["mouth"] = 0

    $musicPlayer.playSong(song="elkhorn_radio_song",fadeIn=1)

    Atlas "On peut changer de sujet?"

    camera at radio_madhouse_cameraA
    voice mm_yawn
    Madhouse "Serieux?"

    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 5
        Atlas_State["feelers"] = 0
        MM_State["mouth"] = 2
    Atlas "Sorry man."
    $MM_State["mouth"] = 3
    Madhouse "Eh, ça vallait la peine d'essayer."

    camera at radio_atlas_cameraA

    Narrator "Tu te sent un peu oublié."

    $Robyn_State["mouth"] = 6
    $Robyn_State["brow"] = 1
    $Robyn_State["eyes"] = 3

    Robyn "Et moi?"

    $Atlas_State["eye"] = 0

    pause 0.4
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 16
    $Atlas_State["feelers"] = 1
    Atlas "[PCname], tu v'as trop dormir et te réveiller avec un mal de tête."

    $Robyn_State["eyes"] = 1
    $Robyn_State["mouth"] = 3
    $Robyn_State["brow"] = 2
    voice RobynSays("Generic","HmphB")
    Robyn "Aw man."

    Narrator "T'es définitivement oublié."

    Madhouse "Des idées pour faire que ça arrive?"

    $Atlas_State["eye"] = 18
    $MM_State["mouth"] = 0
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0

    Atlas "Comment je suis censé savoir? \n\nL'avenir est stupide et en fait qu'a sa tête."

    Madhouse "Wow,, vraiment inspirant p'tit gars."

    camera at quick_radio_camera
    Madhouse "Mike lance sa main, et secoue sa tête avec un sourire."

    $MM_State["eyes"] = 0
    Madhouse "Bref changeons de sujet à présent!"

    $MM_State["mouth"] = 9

    Madhouse "Et si on fesait un p'tit quiz? Ca devrait être super simple pour de si {b}GRAND FANS{/b}!"
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 4

        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 5

    Robyn "Yep! J'suis un super fan."

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 0

    Narrator "Tu n'a absolument aucune idée de ce que tu est en train de faire."

    Madhouse "Episode vingt, quelle abomination à-ton interviewé sur le plateau?"
    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0

        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["eyeFrame"] = 0

    voice RobynSays("Generic","ConfusedA")
    Robyn "Ah..."
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5

    $displaymenu = True
    Narrator "Tu reste ici silencieusement, assis sur t'a chaise, perpexle sur quoi dire.{nw}"

    menu:
        extend ""

        "Un chat fantôme":
            pass
        "Un genre de spaghétti chelou.":
            pass
        "Ma mère?":
            pass
    python:
        displaymenu = False

        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0

        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1

    show atlas:
        yoffset 130
        ease 0.15 yoffset 90
        ease 0.15 yoffset 130
        pause 0.1
        ease 0.15 yoffset 90
        ease 0.15 yoffset 130

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 8

    Atlas "Bloody Bones!"

    Narrator "Il se jette en l'air, en criant presque sa réponse."
    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1

        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 6
        Atlas_State["sparkle"] = 0

    show robyn:
        ease 3.0 yoffset 140

    camera at radio_atlas_cameraA
    Narrator "Tu croises les bras, et t'enfonce dans ta chaise."

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 7

    Madhouse "Parfait!"

    #Narrator "Mike moves things right along."

    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 9

    Madhouse "Celle là est un peu {bt=3}épicée{/bt}. épisode 26, qui était l'amoureux secret de Bigfoot?"
    python:
        Atlas_State["eye"] = 3
        Atlas_State["feelers"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["eyeFrame"] = 1

    show atlas:
        xcenter 0.5
        linear 0.1 xcenter 0.49
        linear 0.1 xcenter 0.5
        repeat

    #Narrator "Atlas a l'air d'être sur le point d'éxploser."
    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4

    $displaymenu = True
    Robyn "Je l'ai sur le bout de la langue!{nw}"

    menu:
        extend ""

        "Un frogman?":
            pass
        "Ummm... le Squonk.":
            pass
        "Bigfoot numéro 2.":
            pass

    python:
        displaymenu = False
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0

        Atlas_State["eye"] = 6
        Atlas_State["eyeFrame"] = 0
        Atlas_State["sparkle"] = 0

    show atlas:
        xcenter 0.5

    #voice atlas_booyah
    Atlas "L'homme chèvre!"

    $MM_State["eyes"] = 2
    $MM_State["mouth"] = 9

    Madhouse "Pas mal! Par contre tu devrais peut-être laisser une chance à ton pote."

    Narrator "Mike ricane."
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2

    Robyn "Je suis un peu pas préparé du tout là."
    python:
        Atlas_State["eye"] = 1
        Atlas_State["sparkle"] = 0
        Atlas_State["eyeFrame"] = 3
        Atlas_State["feelers"] = 1

    Atlas "Ouais. Rooh je peux pas m'empècher de parler."

    python:
        displaymenu = True

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0

    Madhouse "A la fin de la saison 1, quelles étaient les breaking news?{nw}"

    menu:
        extend ""

        "J'ai déménagé a longhope!":
            pass
        "Bigfoot et l'homme chèvre se sont marriés?":
            pass
        "J'suis plûtot sur que t'es mort.":
            pass

    python:
        displaymenu = False

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

    Narrator "Atlas te touche gentillement la jambe avec la sienne et te chuchote dans l'oreille."
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0


    Atlas "\n{size=-5}Alien abduction.{/size}\n"

    python:
        Robyn_State["mouth"] = 6
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0

    Robyn "Y'avais des aliens!"

    camera at radio_madhouse_cameraA
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 4
    Madhouse "Oh ouais? Et y'avais combien d'épisodes sur la radio au total?"

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0

        Atlas_State["feelers"] = 1

    camera at radio_atlas_cameraA
    Narrator "Atlas t'annonce discrètement la réponse a nouveau."

    Atlas "\n{size=-5}Trente-deux.{/size}\n"

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0

    Robyn "T-Trente deux!"

    camera at radio_madhouse_cameraA
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 3
    Madhouse "Correct."

    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 1
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 16
        MM_State["mouth"] = 1

    Narrator "Madhouse lance un sourire hésitant."

    python:
        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 0

        MM_State["eyes"] = 4
        MM_State["mouth"] = 5
        MM_State["armL"] = 1
        MM_State["armR"] = 1

    Madhouse "Prochaine question; qu'est-ce que je mange le matin?"


    camera at quick_radio_camera
    Narrator "Tu regarde Atlas en éspérant une réponse."

    Atlas "Je...{nw}"

    python:
        Atlas_State["feelers"] = 1
        Atlas_State["eyeFrame"] = 3
        Atlas_State["eye"] = 2
    extend "\n\nJe sais pas..."

    show BG Studio Room2
    show atlas:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    show robyn:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    show madhouse:
        matrixcolor TintMatrix("#ffffff")
        ease_bounce 10.0 matrixcolor TintMatrix("#c0fac8")

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 6

    Narrator "Le fantôme lance un faux regard déçu à Atlas."

    voice mm_laugha
    Madhouse "N'importe quel {i}vrai{/i} fan saurait que je passe le p'tit déj!"
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 3

    Robyn "C'est pas juste!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    $Robyn_State["mouth"] = 5
    Madhouse "Oh ouais? Hey, Atlas, qui a sponsorisé l'épisode récap de la saison 2?"

    Narrator "Atlas hôche les épaules."

    Atlas "Je passe les pauses pubs."

    python:
        displaymenu = True

        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "Comment tu peux passer les pubs sur la radio-?{nw}"

    python:
        displaymenu = False

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

    $MM_State["eyes"] = 10
    $MM_State["mouth"] = 1
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    show madhouse at hoppies:
        yoffset 140
    Madhouse "{size=45}TOXIC WASTE ENERGY!{/size} \nC'ETAIT TOXIC WASTE EN—"

    $MM_State["armL"] = 2
    $MM_State["armR"] = 2
    $MM_State["eyes"] = 1
    $MM_State["mouth"] = 5

    show madhouse:
        yoffset 140
        parallel:
            flipCharDelayed(0.7,0.5)
    Madhouse "{sc=2}Mais bien éssayé!{/sc}"

    $MM_State["armR"] = 1
    $MM_State["armL"] = 1
    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 0

    Madhouse "On fait pause pub."

    $musicPlayer.playSong()
    play music elkhorn_radio_outro_song noloop

    $Atlas_State["eye"] = 1
    $MM_State["mouth"] = 1

    #Narrator "Mike’s smile falters as he flicks off the microphones and whirls around."

    #Robyn "I-I thought we were having a good time!"

    $Atlas_State["eye"] = 3

    $MM_State["eyes"] = 0
    $MM_State["armL"] = 3
    $MM_State["armR"] = 1
    $MM_State["mouth"] = 9

    show madhouse:
        yoffset 140
        parallel:
            unflipCharDelayed(0.7,0.5)

    Narrator "Il pointe Atlas du doigt."

    camera at radio_madhouse_cameraA
    Madhouse "{sc=5}{b}TOI.{/b}{/sc}"

    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

        Atlas_State["feelers"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 16

    Atlas "Moi?"

    Madhouse "Tu vas m'aider."

    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    $musicPlayer.playSong(song="elkhorn_radio_song",queueSong=True)

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 5
    $MM_State["armL"] = 1

    #Narrator "The ghost growls and clicks on the microphones, snapping back into his chipper host persona."

    python:
        MM_Stats = Unit("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}",1,1,2,0,1,1,40)
        MM_Stats.baseDiff = 6
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(2) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01_MM_MM_ATTACK")
        MM_Stats.SetMTA(3)

        enemyUnits = []
        enemyUnits.append(MM_Stats)

        Atlas_Stats = Unit("{color=#ED2A82}Atlas{/color}",-1,2,2,-1,1,0,13)
        Atlas_Stats.Color = "#ED2A82"
        Atlas_Stats.SetIcon("atlasIcon")

        #Puts the party into the Bar
        playerUnits = []
        playerUnits.append(Atlas_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0])

    python:
        Atlas_State["eye"] = 4
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 1


    Atlas "Wow, okay!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 7

    Madhouse "Vous savez tous que j'aime personellement le Toxic waste. En fait, j'en ai bu tellement que m'a peau est devenue {color=#3bec27}VERTE{/color}, HAH!"


    Madhouse "Mais je reconnaît mes propres préjugés, alors ne me croyez pas sur parole! Atlas, l'ami, pourquoi n'éssaie tu pas le nouveau goût, Beyond The Grave?"
    camera at radio_atlas_cameraA
    $musicPlayer.playSong(song="drink_it_song",fadeOut=1,fadeIn=3)
    $Atlas_State["armR"] = 1
    show atlas:
        xcenter 0.5
        yoffset 130
    show ToxicWasteCG:
        xcenter 0.51
        yoffset 340
        matrixcolor TintMatrix("#c0fac8")
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    show atlasArmR2:
        ycenter 0.79
        zoom 0.23
        xcenter 0.5
        yoffset 130
        matrixcolor TintMatrix("#c0fac8")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Narrator "Une canette de Toxic Waste apparait soudainement dans les mains du Mothman comme s'il l'avait toujours eu dans les mains."

    Narrator "Atlas ouvre la canette en tirant sur l'ouverture, laissant échaper une fummée {color=#3bec27}verte{/color} qui fini par couler sur ses mains."

    python:
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 7
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 0

    voice atlas_nervouslaugh
    Atlas "Ouais, d'accord, mais c'est pas genre le truc qui t'a tué?"

    $Atlas_State["eye"] = 1
    Atlas "... Tu me donneras un autographe, hein?"

    python:
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1

    Madhouse "{sc=5}{b}JUSTEBOISLEPUTAINDEMERDE.{/b}{/sc}"

    play sfx blip_2b
    pause 0.6

    camera at radio_atlas_cameraA
    Narrator "Il prend une petite gorgée."

    python:
        displaymenu = True
        preferences.text_cps = 60

        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 1

    Atlas "GWUAH—{nw}"
    python:
        playerUnits[0].modifyHP(-100,1.0,"guts")
        preferences.text_cps = 30
        displaymenu = False
    hide atlasArmR2
    show atlas:
        ease 0.4 yoffset 700

    show ToxicWasteCG:
        yoffset 340
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            ease 0.4 yoffset 0
            ease 0.7 yoffset 700
        parallel:
            ease 1.2 matrixtransform RotateMatrix(0.0, 0.0, 360.0*2)
    camera at quick_radio_camera
    $RefreshBarHP()
    Narrator "Il tombe au sol comme une pierre."
    python:
        MM_State["eyes"] = 6
        MM_State["mouth"] = 9

        Atlas_Stats.iconState = 0

    camera at quick_radio_camera


    Madhouse "Bon? T'en pense quoi? On {i}MEURT{/i} de savoir ce que tu en pense."
    hide ToxicWasteCG

    python:
        Atlas_State["eye"] = 10
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Atlas_State["sparkles"] = 0
        Atlas_State["armR"] = 0

        playerUnits[0].cHP = -13
        playerBarNames[0] = "{color=#3bec27}Atlas?"
        Atlas_Stats.iconState = 3

    play sfx ko_reverse

    show atlas:
        yoffset 1000
        matrixtransform RotateMatrix(0.0, 180.0, 25.0)
        ease 2.0 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    $RefreshBarHP()
    Narrator "Atlas se relève soudainement le liquide vert coulant de ses lèvres. "

    $Atlas_State["eye"] = 11

    P_Atlas "Wowzers! J'ai l'impression que mon squelette pourais sortir de mon corps et danser la polka! Serieux, Beyond The Grave déchire trop!"
    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

        HighlightPlayerUnitBars([])

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            ease 0.3 yoffset 0
        parallel:
            linear 0.15 matrixtransform RotateMatrix(0.0, 0.0, 10.0)
            linear 0.15 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "Tu saute de ta chaise."
    $HideBars()

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        yoffset 0

    Robyn "Attend— Il se passe quoi là? Qu'est-ce que t'a fait à Atlas!?"

    voice mm_laughf

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    Madhouse "Chillax, c'est juste temporaire. En partant du principe que tu va survivre au prochain ségment. C'est l'heure de mon jeu préféré, Fake or Folklore!"

    python:
        Atlas_State["eye"] = 10
        Atlas_State["sparkle"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1

        preferences.text_cps = 60
        displaymenu = True
        pauseEnable = False

    P_Atlas "Je peux juste le dire! J'apprécie vraiment notre temps passé ensemble, Maddie ! Si je peux me permettre, la direction devrait tout de suite se défaire. Sérieusement, qu'est-ce que ces connards savent !? Bien sûr, vous êtes en train de pourrir dans un bâtiment abandonné, mais bon, au moins les opossums sont sympas.{nw}"

    python:
        displaymenu = False
        pauseEnable = True
        preferences.text_cps = 30

    voice mm_confused
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 10
    voice mm_yawn
    Madhouse "Bref."

    python:
        Atlas_State["eye"] = 11
        Atlas_State["sparkle"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0

        MM_State["eyes"] = 0
        MM_State["mouth"] = 0
    Madhouse "Pourquoi tu n'éxplique pas les règles, l'insecte?"
    python:
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

        Atlas_State["eye"] = 11
        Atlas_State["sparkle"] = 0
        Atlas_State["armL"] = 2
        Atlas_State["feelers"] = 1

    show atlas: ##possessed think: TODO
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        linear 0.15 xoffset -10
        linear 0.05 xoffset 0
        pause 0.1
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        linear 0.05 xoffset -10
        linear 0.1 xoffset 0
        pause 0.05
        linear 0.15 xoffset -10
        linear 0.05 xoffset 0
        pause 1.0
        repeat

    Narrator "Atlas rigole d'une manière très peu naturelle. Ses antennes bougent en même temps."

    P_Atlas "Bien sûr! Les règles sont simples: Mike va décrire un cryptide et tu dois deviner lequel c'est! Si tu loupe, tu souffre d'une {i}PETITE{/i} pénalitée. Si t'est vivant à la fin, tu gagne!"
    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "Pénalité? Je suppose que tu va me buter si je refuse de jouer."
    python:
        Atlas_State["eye"] = 10
        Atlas_State["sparkle"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0

    show atlas:
        xoffset 0


    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9

    Madhouse "Pas du tout! Je garderais juste Atlas comme associé, donc en gros, tu laisse ton p'tit copain l'insecte ici! J'dis pas non à une co-hôte."
    python:
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3


    show robyn:
        xanchor 0.5
        yanchor 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    call makeCheckpoint from _call_makeCheckpoint
    Robyn "Rooh! Okay! Je vais jouer a ton stupide jeu."
    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.6 matrixtransform RotateMatrix(0.0, 0.0, 10.0) yoffset 110
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    Narrator "Tu te rassois dans le siège et croises les bras."
    jump RadioQuiz

default radioDamagedHP = 0
label RadioDamaged(lastQ=False):
    $playerUnits[0].modifyHP(-(3+numWrong*2),1.0,"guts")
    $radioDamagedHP = playerUnits[0].maxHP - playerUnits[0].cHP
    $RefreshBarHP()

    if numWrong < 1 and playerUnits[0].isAlive:
        Narrator "Tu sent une soudaine sensation de douleur dans ton corps, comme un crispement."

        $pcSelected = 0
        $Robyn_State["mouth"] = 1
        $Robyn_State["eyes"] = 1
        $Robyn_State["brow"] = 2
        Robyn "Ah! Ouch-"
        $PC_Stats.iconState = 0

        if not lastQ:
            $MM_State["eyes"] = 6
            $MM_State["mouth"] = 5
            Madhouse "Ca va juste devenir plus dûr. En fait, à chauque questions que tu loupe, je vais bouffer un peu plus de ton énergie. Sorry, not sorry, les règles c'est les règles."

            $Robyn_State["mouth"] = 1
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 3
            Robyn "Tu vient de les inventer!"

            Madhouse "Quelqu'un doit bien les faires!"
    elif numWrong < 2 and playerUnits[0].isAlive:
        show robyn:
            ease 0.15 yoffset 90
            ease 0.15 yoffset 110
        $Robyn_State["mouth"] = 7
        $Robyn_State["eyes"] = 3
        $Robyn_State["brow"] = 3
        Narrator "Soudainement tu te fait frapper dans le ventre cette fois, une force invisible te poignarde comme l'estomac."
        $pcSelected = 0
        $PC_Stats.iconState = 0
        $Robyn_State["mouth"] = 4
        $Robyn_State["eyes"] = 0
        $Robyn_State["brow"] = 3
        Robyn "Gah! P-putain mec, le jeu est censé être fun!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 5

        Madhouse "C'est fun pour moi!"
    elif numWrong < 3 or not playerUnits[0].isAlive:
        show robyn:
            ease 1.0 yoffset 700

        python:
            Robyn_State["mouth"] = 1
            Robyn_State["eyes"] = 3
            Robyn_State["brow"] = 2

        Narrator "Tu te sent horriblement mal. La douleur dans ton estomac est si intense que tu tombe au sol."

        python:
            PC_Stats.iconState = -1
            Robyn_State["mouth"] = 2
            Robyn_State["eyes"] = 0
            Robyn_State["brow"] = 2

            MM_State["eyes"] = 0
            MM_State["mouth"] = 9

            Atlas_State["eye"] = 5
            Atlas_State["eyeFrame"] = 2
            Atlas_State["feelers"] = 1
            Atlas_State["armL"] = 1
            Atlas_State["armR"] = 1
        Madhouse "Gyehahahaa! On dirait que ton âme est à moi! Oh beh! Je peux enfin me casser de ce trou à rat!"

        pause 0.01
        scene black
        with Dissolve(1.0)

        $Atlas_State["eye"] = 11
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0


        P_Atlas "Tu devrais faire un podcast!"
        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 5

        Madhouse "Mouais j'ai le temps."


    $numWrong+=1
    $PC_Stats.iconState = 0
    return

label RadioQuiz:
    python:
        PC_Stats.updateStats()

        playerUnits = []
        playerUnits.append(PC_Stats)

        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightPlayerUnitBars([0])

        Atlas_State["eye"] = 11
        Atlas_State["armR"] = 1

    show atlas: #TODO possessed snarky hand:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.75 matrixtransform RotateMatrix(0.0, 180.0*4, 0.0)


    $musicPlayer.playSong(song="urgently_jammin_song",fadeOut=5,fadeIn=5)

    P_Atlas "C'est t'a chance de faire briller tes connaissances!"
    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Madhouse "J'aurais pas pu mieux le dire, vermine. Maintenant commençons avec un peu de FAKE., or., FOLKLORE!"

    hide atlasIcon onlayer screens

    python:
        Atlas_State["eye"] = 10
        Atlas_State["armR"] = 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0


    Madhouse "Question 1!{nw}"

    extend "\n\nEn 1971, le monstre du Missouri, Momo, est connu pour éloigner ses attaquant avec quoi?"

    python:
        displaymenu = True
        isRight = False
        numWrong = 0

    menu:
        extend ""

        "En leur jetant des grosses pierres.":
            python:
                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 4
                Robyn_State["brow"] = 1

            ##TODO voice PC_Thinking
            Robyn "En... Lançant des grosses pierres? Ce genre de truc?"
        "Il pue.":
            python:
                isRight = True

                Robyn_State["mouth"] = 7
                Robyn_State["eyes"] = 0
                Robyn_State["brow"] = 2

            ##TODO voice PC_Thinking
            Robyn "Il pue beaucoup, non? Je crois qu'il éloignent les gens avec son odeur."
        "Une lettre très mal écrite.":
            python:
                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 4
                Robyn_State["brow"] = 1

            ##TODO voice PC_Confused
            Robyn "En envoyant une lettre de menace?"

            Narrator "Là c'est sur tu va clamser."

    $displaymenu = False
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 6

    Madhouse "C'est vraiment une sacré réponse!"
    python:
        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    play sfx drumroll

    $renpy.block_rollback()

    if isRight:
        play sfx emote_realization_sfx
        python:
            Atlas_State["eye"] = 11
            Atlas_State["feelers"] = 0
            Atlas_State["armL"] = 2

        P_Atlas "Serieux, tu t'entends? Est-ce que t'éssaie au moins?"

        Madhouse "T'a raison, J'suis devenu plus mou qu'un marshmallow."
    else:
        play sfx sadTrumpet
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 2
        P_Atlas "BZZT! Wrong. La bonne réponse c'était son odeur!"

        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 0
        P_Atlas "Aw, dommage. On dirait que je vais devoir te prendre un peu de vie~"

        call RadioDamaged(False) from _call_RadioDamaged
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 1
    $Atlas_State["armL"] = 0

    Madhouse "Question 2!{nw}"

    extend "\n\nOld Ephraim, un cryptide qui térrorisait les gens du Logan Canyon en 1923, c'était quel genre de créatures?"
    python:
        displaymenu = True
        isRight = False

    menu:
        extend ""

        "Un {sc=5}{b}{color=#ff4545}TRES GROS{/color}{/b}{/sc} ours":
            $isRight = True
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 2

            Robyn "C'était pas genre un gros ours?"

            Narrator "T'es juste en train de deviner à ce point."
        "Un Bigfoot":

            $Robyn_State["mouth"] = 6
            $Robyn_State["eyes"] = 1
            $Robyn_State["brow"] = 2
            Robyn "C'était pas bigfoot justement?"

        "Un Gris perdu.":
            $Robyn_State["mouth"] = 3
            $Robyn_State["eyes"] = 1
            $Robyn_State["brow"] = 2

            Robyn "Un uh... Gris perdu."

            Narrator "Tu crois avoir lu un truc la dessus."

    $displaymenu = False

    show atlas:
        linear 0.1 xoffset -10
        linear 0.1 xoffset 10
        repeat

    $Atlas_State["eye"] = 11
    $Atlas_State["feelers"] = 1
    $Atlas_State["armL"] = 2
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 6
    Madhouse "How daring!"

    play sfx drumroll
    show madhouse:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.25 matrixtransform RotateMatrix(0.0, 0.0, -7.0) yoffset 170
        ease 0.25 matrixtransform RotateMatrix(0.0, 0.0, 0.0) yoffset 140

    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 0
    $Atlas_State["armL"] = 0
    Narrator "Madhouse pointe vers Atlas qui vibre comme un ragdoll."

    $renpy.block_rollback()
    show atlas:
        xoffset 0

    if isRight:
        play sfx emote_realization_sfx
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 2
        P_Atlas "Correct!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 10
        Madhouse "Huh, je m'y attendais pas. Bravo sur celui-là."

        $Robyn_State["mouth"] = 4
        $Robyn_State["eyes"] = 0
        $Robyn_State["brow"] = 1
        Robyn "Oh— um, merci?"
    else:
        play sfx sadTrumpet
        $Atlas_State["eye"] = 11
        $Atlas_State["feelers"] = 1
        $Atlas_State["armL"] = 2

        $Robyn_State["mouth"] = 2
        $Robyn_State["eyes"] = 2
        $Robyn_State["brow"] = 1

        P_Atlas "BZZT! Faux. La bonne réponse c'était un gros ours."

        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        #P_Atlas "Oof and that’s a hit! Sorry pal."

        call RadioDamaged(False) from _call_RadioDamaged_1
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    P_Atlas "Prochaine question?"

    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 9
    ##TODO voice MM_Laugh4
    Madhouse "{bt=3}Oh, celle là est pas mal.{/bt}"

    #QUESTION: 3
    $Atlas_State["eye"] = 10
    $Atlas_State["feelers"] = 0
    $Atlas_State["armL"] = 0
    Madhouse "Question 3!{nw}"

    extend "\n\nLe géant du Rochester, appercu en 1965, a écrasé le toit de quelle voiture?"
    python:
        displaymenu = True
        isRight = False

    menu:
        extend ""

        "George... Washington.":
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 1
            ##TODO voice PC_Confused
            Robyn "George... Washington."
        "Harold":
            $Robyn_State["mouth"] = 2
            $Robyn_State["eyes"] = 0
            $Robyn_State["brow"] = 2
            ##TODO voice PC_Thinking
            Robyn "Harold sounds about right. C'est genre un nom normal...\n Tu est dans la merde."
        "Comment je suis censé savoir ça???":
            $ isRight = True
            $Robyn_State["mouth"] = 4
            $Robyn_State["eyes"] = 4
            $Robyn_State["brow"] = 3
            ##TODO voice PC_Frustrated
            Robyn "Je sais même pas ce qu'est Rochester. T'es juste en train d'inventer des trucs!"
    python:
        displaymenu = False
        renpy.block_rollback()

    if isRight:
        voice atlas_possessed_betrayed
        $Atlas_State["eye"] = 10
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 1
        $Atlas_State["armR"] = 1
        P_Atlas  "Heeeey, pas cool Maddie! Les questions piège sont contre les règles!"

        $Atlas_State["eye"] = 7
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0
        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 1
        Madhouse  "Comment est-ce que tu peux être aussi {sc=3}ODIEUX{/sc}?! T'es censé être sous mon contrôle total!"
        $Atlas_State["eye"] = 10
    else:
        play sfx sadTrumpet

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 7
        Madhouse "Gyeheheh! T'es tombé dans le panneau! Le géant de Rochester n'éxiste pas!"

        $Atlas_State["eye"] = 10
        $Atlas_State["eyeFrame"] = 0
        $Atlas_State["feelers"] = 0
        $Atlas_State["armL"] = 0
        $Atlas_State["armR"] = 0
        P_Atlas "BZZT! Faux, mais Maddie, t'a complètement triché!"

        $MM_State["eyes"] = 0
        $MM_State["mouth"] = 3
        Madhouse "Et?"

        call RadioDamaged(True) from _call_RadioDamaged_2
        if not playerUnits[0].isAlive:
            jump gameOverScreen

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $RefreshBarHP()
    Madhouse "Je crois ont à le temps pour une dernière question."

    $Robyn_State["mouth"] = 3
    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1

    Narrator "Mike se penche dans son micro. Il baisse sa voix comme un grognement."

    python:
        Atlas_State["eye"] = 10
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

        Robyn_State["mouth"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    Madhouse "Tu sais ce qu'on fait au tricheur?"

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 9

    #Narrator "Ajustant sa casquette légèrement, Le regard vide de Mike te fixe de ses yeux blancs."
    play sfx drumroll
    $displaymenu = True
    menu:
        extend ""

        "T'a jamais fait une règle.":
            Narrator "Un mauvais présentiment te parcours le dos quand tu réponds."
            play sfx sadTrumpet
            Madhouse "Donc tu l'admet."
        "Je perd?":
            play sfx sadTrumpet
            Madhouse "{sc=5}EVIDEMENT QUE TU PERD.{/sc}"
        "On est libre de partir.":
            play sfx sadTrumpet
            Madhouse "Bien sur! Dégage de là, et pourquoi je te donne pas mon porte-feuille tant que t'y est!"
    $displaymenu = False
    $MM_State["eyes"] = 6
    $MM_State["mouth"] = 7
    Madhouse "{sc=5}JE fait les règles!{/sc} C'est MON show, MES règles, MON jeu!"

    show madhouse:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.25 yoffset -100 xzoom 0 blur 30
        pause 0.3
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.4
        ease 0.25 yoffset 0 xzoom 1 blur 0
    Narrator "Le fantôme se retrouve derrière Atlas."

    voice mm_yourejustanotherfakefan
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    Madhouse "T'es juste même pas un vrai fan."

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9

    show madhouse: ##TODO creepy grin:
        ease 0.65 xcenter 0.5 zoom 0.75 alpha 0 blur 30

    show atlas:
        linear 0.075 xoffset -3
        linear 0.075 xoffset 3
        repeat

    $Atlas_State["feelers"] = 1

    show  Overlay Green Flashing
    Narrator "IEn un éclair, Mike fusionne avec Atlas avant de former une créature beaucoup plus grande et creepy."

    $tRobynHP = playerUnits[0].cHP
    jump fightbuildup
default tRobynHP = PC_Stats.maxHP



#Go to 3.5
