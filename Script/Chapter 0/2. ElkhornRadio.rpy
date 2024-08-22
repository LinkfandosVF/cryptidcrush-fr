#Taro Tutorial
label taro_dice_tutorial:
    python:
        tempDieType = diceBot.dieType
        diceBot.setDieType(1)
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 2

        Robyn_State["mouth"] = 3

    show taro:
        ease 1.0 xcenter 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn:
        ease 1.0 xcenter 0.2

    voice taro_laughc
    Taro "Tout cela demande à être fouillé!"

    Robyn "Où je pourrais juste lui envoyer un message."

    #Narrator "Tu explore la zone des yeux avec ta lampe, mais ne trouve rien en particulier."
    python:
        Taro_State["pawL"] = 0
        Taro_State["mouth"] = 1
        Taro_State["eye"] = 1

        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 1

    Taro "Nooon! Pas comme ça! Tu dois lancer un dé!"
    $Robyn_State["mouth"] = 4

    Robyn "Je les ai laissé à la maison."
    python:
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

        Taro_State["mouth"] = 4

    show screen Dice_Rolling_Menu
    python:
        xRerolls = 0
        pc_karma = 2
        rMod = dMenuMod = PC_Stats.cStats("brains")
        tempDif = rDiff = rrDif = dMenuDiff = 9
        rDesc = dMenuDesc = "Investigation"
        tempFailCheck = False
        DiceMenuResult = -1

    voice RobynSays("Generic","ConfusedA")
    Robyn "Ummm? C'est QUOI ça?"

    Taro "Certaines choses demande du skill et un peu de chance, donc pour déterminer ton avenir, tu dois lancer des dés!"

    Taro "T'auras parfois de la difficulté dépendant de ce que tu doit faire ou surpasser. Et l'univers rajoutera une alteration sur une de tes stats! ([kwBrains] dans ce cas)"

    $Robyn_State["mouth"] = 3

    Robyn "Ca ressemble à un genre de truc interdit."

    python:
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 2

    Taro "Oh mais c'est le cas! Maintenant lance un dé!"

    python:
        die1Result = 1
        die2Result = 1
        die3Result = 0
        dieTotal = die1Result + die2Result + die3Result
        DiceMenuResult = 0
        dieGlow = True

    with Dissolve(0.2)
    pause 2.0
    python:
        DiceMenuResult = 2

        Robyn_State["mouth"] = 7
        Robyn_State["brow"] = 2



    show failFlash
    play sfx dice_result_c

    Robyn "Um."
    hide failFlash
    python:
        Taro_State["pawR"] = 2
        Taro_State["mouth"] = 2
        Taro_State["eye"] = 2

    voice taro_smugb
    Taro "Wow, c'était vraiment nul."
    python:
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 5

    Taro "Mais t'inquète! Si tu te loupe, tu peux relancer et changer le destin en utilisant du [kwKarma]!"
    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

        Robyn_State["eyes"] = 4

    Robyn "Laisse moi juste appeler Atlas par pitié."

    Taro "C'est quoi le [kwKarma] tu dit? Et bien quand tu loupe un lancer, tu peux utiliser du [kwKarma] pour reroll!"

    Taro "Tant que tu à du [kwKarma] tu peux relancer. Même si tu a reussi. Donc soit intélligent et ne dépense pas tout!"

    Taro "Tu regagne seulement un point de [kwKarma] quand tu loupe, et quand tu décide de ne pas relancer. Comrpis?"
    $Robyn_State["eyes"] = 1

    Robyn "Je suis sur que quelqu'un ici comprend."
    python:
        tempFailCheck = True
        Taro_State["mouth"] = 4
        Taro_State["eye"] = 5
    Taro "Super! Maintenant appuie sur ce bouton et relance moi ces dés !"

    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3
    Taro "Le bouton juste en dessous!"

    Taro "..."

    Taro "Quand tu veux, meow~"

    Taro "..."

    Taro "Le dé avec la flèche rose."

    Taro "..."

    Taro "Ouais prend ton temps."

    Taro "..."

    Taro "Bon..."

    Taro "{sc=2}...{/sc}"

    $Taro_State["eye"] = 1
    Taro "Tu le fait meowxpères?"

    Taro "{sc=4}...{/sc}"

    Taro "Just clique sur ce foutu bouton."

    Taro "Nan j'rigole! Je m'en fout un peu de ce que tu fait."

    Taro "Je suis juste là pour le fun vraiment."

    Taro "Sinon, quoi d'neuf?"

    Taro "Tu dois vraiment aimer lire! J'admire ça!"

    Taro "Et si je spoilais la fin du chapitre?"

    Taro "A la fin..."

    Taro "Vous mourrez {sc=3}{b}TOUS!{/b}{/sc}"

    Taro "Nan je déconne."

    Taro "Bref appuie sur le bouton!"

    Taro "Je vais tomber a court de dialogues."

    Taro "Il fait si beau dehors..."

    Taro "Give me a drink bartender!"

    Taro "Bon serieux même Gaël a plus d'idées là!"

    Taro "Si Salomé tu voit ça, merci d'avoir éssayé le jeu!"

    Taro "..."

    Taro "Il est écrit..."

    Taro "Seul Link peut vaincre Ganon."

    Taro "Et toi tu peux commencer par appuyer sur ce fichu bouton!"

    Taro "Eh t'a vu! Super game design! Pleins de dialogues pour les gens qui refusent de continuer comme toi."

    Taro "C'est frustrant vraiment."

    Taro "..."  

    Taro "Fish."

    Taro "Whopper whopper whopper whopper! Junior double tripple whopper!"

    Taro "Est-ce que c'est ton adresse ip:       192.168.1.24\n Tu n'est pas en sécurité cette nuit~"

    Taro "Bon là j'ai plus d'idées."

    Taro "207 lines de code pour CA."

    Taro "Sinon ce serait bien si quelqu'un comme Farod fesait le jeu."

    Taro "..."

    Taro "It is hot as hell in this fucky hot ass room i'm in."

    Taro "Et là tu voit t'est censé dire:\n IS THAT THE GRIM REAPER??"

    Taro "..."

    Taro "Juste au cas où... Bonjour le chat!"

    Taro "...Bon c'est plus drôle là. Au fait l'adress IP était fausse. Tu est en sécurité chez toi."

    Taro "Enfin j'éspère. C'est les gens comme toi qui rendent le monde meilleur."

    Taro "Enfin tu POURRAIS si tu décidait d'appuyer sur ce FICHU BOUTON!"

    Taro "J'ai pas appris Ren'Py pour ça moi!"

    Taro "Bon désolé j'ai plus de ligne là, c'est un WHILE TRUE en ligne 230. Pardon. Y'a plus rien à voir. Et pour une fois je suis honnète. D'ailleurs ce que tu vient de voir c'est que dans le patch français. Nulle part ailleurs."
    while True:
        Taro "{sc=6}...{/sc}"



    return

# Script Start
label atTheStation:
    python:
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=8)
        timeText = "2:00AM"

    play ambiance forest_ambiancea fadeout 1.0 fadein 7.5

    scene BG Outside Radio Station Near
    #show BGCG Outside Radio Station Fence: DONT USE THIS IT LOOKS BAD
        #xcenter 0.5
        #yalign 1.0
        #yoffset 1
    with pixellate #----------------------------- Outside Radio Station

    Narrator "Arrivant dans le parking vide de la station, tu te gare à travers les lignes quasi éffacés. Taro sort et se jette dans tes bras, insistant pour être porté comme un bébé sur-dimensionné qu'elle est. Tu ouvre la porte et sort."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0

        Taro_State["eye"] = 1
        Taro_State["pawR"] = 2

    show robyn:
        matrixcolor TintMatrix("#d1ffe1")
        xcenter -0.3
        ease 2.0 xcenter 0.3

    show taro:
        parallel:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter -0.25
            ease 2.0 xcenter 0.45
        parallel:
            ease 1.3 yoffset 10
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10

        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat


    Narrator "Tu sent les moustaches de Taro sur tes joues, d'une manière ou d'une autre elle aime bien te voir flipper."
    camera:
        ease 3.0 zoom 1.5 ycenter 0.7

    show robyn:
        xcenter 0.3

    show taro:
        xcenter 0.45
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

    voice RobynSays("Generic","Concern")
    Robyn "Oooké! Tout vas bien aller. C'est juste une station abandonnée. Rien d'autre."

    Narrator "Tu clique sur le bouton de ta très chère lampe de poche.."

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 2

    Narrator "Tu pointe la fainte lumière vers la station. Incluant la barrière grillé en métal qui la protège. Merde. T'a encore oublié la pince."

    $Robyn_State["brow"] = 2

    Narrator  "Tu tourne plûtot ton attention vers un large morceau de bois sur lequel a sauvagement été écrit à la bombe avec des lettres rouges majuscules accroché sur le grillage. Tu le lit a voix haute."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 4

    Robyn "Dégagez! Les trepasseurs seront {sc=2}{b}{color=#EC2A2A}éxecutés!{/color}{/b}{/sc}."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 6

    Robyn "Ah,, cool."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1

    #Narrator "Taro se jette de tes bras et fini sur le sol."
    camera:
        ease 1.0 zoom 2.0 ycenter 0.8 xcenter 0.7

    python:
        Taro_State["pawL"] = 1
        Taro_State["mouth"] = 2
        Taro_State["eye"] = 2

        Robyn_State["eyes"] = 1

    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        parallel:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10

        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    voice taro_laughc
    Taro "J'ai entendu que cet endroit brillait en rouge les nuits de vendredi, et que le panneau ON AIR ne s'éteint jamais. Juste des petites rummeurs débiles si tu veux mon avis."

    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    pause 0.5

    python:
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0
        Taro_State["mouth"] = 1
        Taro_State["eye"] = 1

    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    Taro "Où sont les autres?"
    camera:
        ease 3.0 zoom 1.0 ycenter 0.5 xcenter 0.5

    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 2.3 xcenter 0.6
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 2.3 xcenter 0.45
        linear 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        repeat

    #Narrator  "Bougeant sa queue, elle tourne autour dans le parking."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 4
        Robyn_State["armR"] = 1

    Robyn "Il est déja 2 Heures du ma't! Ils sont censé être là!"

    Narrator "Tu regarde l'heure, et remet ton téléphone portable dans ta poche puis scanne les environs avec ta lampe."

    call taro_dice_tutorial from _call_taro_dice_tutorial

    python:
        diceBot.setDieType(tempDieType)
        pc_karma = diceBot.maxKarma
        musicNote = 8

    if isRollSuccess:
        show robyn:
            ease 0.5 xcenter 0.25

        show taro:
            ease 0.75 xcenter 0.7 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        Narrator "L'éclairage parcours la zone, puis éclaire une vitre cassée avec des mauvaise-herbes ayant trop poussés. Soudainement, une paire de yeux rouge dans l'obscurité des arbes te fait passer un bâtement, de la lumière émanne des yeux non-clignant."

        python:
            Robyn_State["eyes"] = 3
            Robyn_State["mouth"] = 2
            Robyn_State["brow"] = 2

            Taro_State["mouth"] = 3

            Atlas_State["eye"] = 8

        show robyn:
            matrixtransform RotateMatrix(0.0, 0.0, -6.0)
            xcenter 0.25
            ease 0.05 xoffset -5
            ease 0.1 xoffset 5
            ease 0.1 xoffset -5
            ease 0.1 xoffset 5
            ease 0.05 xoffset 0

        show taro:
            xcenter 0.7
            matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        voice RobynSays("Generic","SurpriseC")
        Robyn "{sc=5}AH! WHAT THE FUCK!?{/sc}"

        $musicPlayer.playSong(fadeOut=5)
        Narrator "Tu crie de surprise et fait tomber ta lampe."

        show atlas fall:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter 0.5

        Narrator "En un flash, la créature saute des branches et écarte ses ailes, puis arrive sur le sol. Dramatiquement, les yeux te regardent, la douce lueur de la lune éclairant le visage plummé de la créature."
        python:
            Atlas_State["eye"] = 2
    else:
        show robyn:
            ease 0.75 xcenter 0.25

        show taro:
            ease 0.75 xcenter 0.7 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        Narrator "Tu cherche dans le parking avec ta lampe, rien n'attire particulièrement ton attention."

        $musicPlayer.playSong()
        stop ambiance
        $Atlas_State["eye"] = 7

        show robyn:
            xcenter 0.25

        show taro:
            xcenter 0.7 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        show atlas:
            matrixcolor TintMatrix("#d1ffe1")
            xcenter 0.5

        play sfx blip_2b
        pause

        python:
            Atlas_State["eye"] = 0

            Taro_State["mouth"] = 3

        play sfx blip_2b
        pause
        show taro:
            xcenter 0.7 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        python:
            Atlas_State["eye"] = 2

            Robyn_State["brow"] = 0
            Robyn_State["eyes"] = 2
            Robyn_State["mouth"] = 4
            Robyn_State["armR"] = 1

        play sfx blip_2b
        pause
        python:
            Robyn_State["eyes"] = 3
            Robyn_State["mouth"] = 2
            Robyn_State["brow"] = 2

        show robyn:
            matrixtransform RotateMatrix(0.0, 0.0, -6.0)
            ease 0.05 xoffset -5
            ease 0.1 xoffset 5
            ease 0.1 xoffset -5
            ease 0.1 xoffset 5
            ease 0.05 xoffset 0

        voice RobynSays("Generic","SurpriseC")
        Robyn "{sc=5}AH! WHAT THE FUCK!?{/sc}"

        $Robyn_State["armR"] = 0
        #Narrator "Tu fait tomber ta lampe sur le sol."
        play ambiance forest_ambiancea fadein 7.5

    show robyn:
        ease 0.75 xcenter 0.2 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 2
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=8,fadeOut=5)

    Robyn "Attend. {color=#ED2A82}{b}ATLAS{/b}{/color}?"
    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["sparkle"] = 1

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.75 xcenter 0.2

    show atlas reset:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.625 matrixtransform RotateMatrix(0.0, 360.0, 0.0)

    hide taro
    show taro:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor TintMatrix("#d1ffe1")
        xcenter 0.7
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    voice atlas_oneandonly
    Atlas "{bt=3}Le seul et l'unique{/bt}! J'ai pensé que j'allais observer les environs avant d'y aller directement."

    python:
        Atlas_State["sparkle"] = 0

        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.075 matrixtransform RotateMatrix(0.0, 30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, -30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, 30.0, 0.0)
        linear 0.15 matrixtransform RotateMatrix(0.0, -30.0, 0.0)
        linear 0.075 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show robyn:
        xcenter 0.2


    Narrator "Après son entrée dramatique, Atlas secoue ses plumes salles d'écorce et bas ses larges ailes."
    python:
        Taro_State["mouth"] = 3
        Taro_State["eye"] = 2

        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1
        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 2


    show atlas:
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 1.0 xcenter 0.545
    Narrator  "Ses antennes bougent, alors qu'il se tient sur un pied, il touche Taro de l'autre."
    python:
        Atlas_State["eye"] = 7
        Atlas_State["armL"] = 2

        Robyn_State["eyes"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.545

    voice atlas_spiritumentioned
    Atlas "{b}SO{/b},.,., C'est ça l'ésprit qui te hante? Huh. J'aurais espéré quelque chose de plus...{w=0.3} Impressionant."
    python:
        Taro_State["mouth"] = 1
        Taro_State["pawL"] = 1

    show taro:
        yoffset 0
        pause 1.0
        ease 0.25 xcenter 0.71
        pause 0.5
        ease 0.25 xcenter 0.72
        pause 0.6
        ease 0.25 xcenter 0.73

    show atlas:
        ease 3.0 xcenter 0.6

    Narrator "Taro crache, ses poils s'érissent."
    python:
        Taro_State["mouth"] = 1
        Taro_State["pawR"] = 1
        Taro_State["pawL"] = 0

    voice taro_iamagreatandpowerfulcosmicguardian
    Taro "{sc=2}Je suis un grand et puissant gardien cosmique{/sc}!"
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 4
        Atlas_State["armL"] = 1

        Robyn_State["brow"] = 0

    play sfx emote_frustration
    Narrator "Elle mort le talon de la phalène humanoide."

    Taro "Mrrrff! Grrh!"
    python:
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0

    Atlas "Wow. J'ai mal."

    show atlas:
        ease 0.5 xcenter 0.5
    Narrator "Atlas la dégage, et se défait de l'emprise de Taro."
    python:
        Atlas_State["eye"] = 0
        Atlas_State["eyeFrame"] = 4
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

        Robyn_State["brow"] = 3

    show atlas:
        xcenter 0.5
    Atlas "C'est pas trop tard pour se faire hanter par un truc plus cool, hein?"

    python:
        Robyn_State["eyes"] = 2
        Atlas_State["eyeFrame"] = 3
        Robyn_State["mouth"] = 4

        Taro_State["eye"] = 3
        Taro_State["mouth"] = 4
        Taro_State["pawL"] = 0
        Taro_State["pawR"] = 0

        Atlas_State["feelers"] = 1

    show robyn:
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        pause 0.05
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0

    Robyn "Elle fait de son mieux!.. Je crois."

    $Robyn_State["mouth"] = 5

    #Narrator "Tu lance un regard moqueur au mothman."

    $Atlas_State["eye"] = 2

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.75 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Robyn "T'es juste jaloux de pas avoir un famillier qui te suit partout."

    voice atlas_nervouslaugh

    Atlas "Raah, si je pouvait prendre je choisirais un corbeau!"

    python:
        Atlas_State["eye"] = 7
        Atlas_State["eyeFrame"] = 0

        Taro_State["eye"] = 1
        Taro_State["pawR"] = 2

    Atlas "Dommage qu'ils me détestent."

    python:
        Atlas_State["eye"] = 7

        Taro_State["eye"] = 1

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.75 yoffset 200 matrixtransform RotateMatrix(0.0, 0.0, -20.0)
        pause 0.5
        ease 0.75 yoffset 0  matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 1.5 xcenter 0.4

    show taro:
        pause 2.0
        ease 1.5 xcenter 0.6

    Narrator "Atlas se baisse et ramasse la lampe sur le sol."
    python:
        Atlas_State["eye"] = 1
        Atlas_State["eyeFrame"] = 3

        Taro_State["eye"] = 1

        Robyn_State["brow"] = 2
        Robyn_State["mouth"] = 3


    show taro:
        xcenter 0.6

    show atlas:
        xcenter 0.4
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        yoffset 0

    Atlas "Tient, désolé de t'avoir fait peur, je voulais pas."

    Narrator "Se démarquant dans la végétation, une petite flamme bleue émanne d'une légère lumière au dessus d'une large silhouette démonique. Debout dans l'ouverture, une paire de pinces lourdes."
    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 1
        Atlas_State["feelers"] = 0

        Taro_State["eye"] = 4

        Robyn_State["brow"] = 1

        Jamie_State["eye"] = 3
        Jamie_State["armR"] = 1

    show robyn:
        ease 0.5  xcenter 0.13

    show atlas:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0) xcenter 0.33

    show taro:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        linear 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.55

    show jamie:
        matrixcolor TintMatrix("#d1ffe1")
        xcenter 1.2
        ease 1.0 xcenter 0.85


    voice jamie_greet
    Jamie "Ah. On dirais que tout le monde est là."

    Jamie "Je suppose qu'Atlas a parlé de moi?"

    #Narrator "The tall devil stares down, as if evaluating the small human and [PCtheir] spectral cat."
    python:
        Taro_State["eye"] = 1
        Taro_State["mouth"] = 3

        Robyn_State["mouth"] = 4

    Robyn "Comment t'es arrive si vite?!"
    python:
        Atlas_State["eye"] = 7

        Jamie_State["eye"] = 1
        Jamie_State["sweat"] = 1
        Jamie_State["armR"] = 2
        Jamie_State["brow"] = 3

        Robyn_State["mouth"] = 3

    Jamie "Jambes?"

    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["sparkle"] = 1

    Atlas "Voici Jamie! Le plus dûr-a-cuire des démons. Iel écoute bien, collectionne des Os, combat au poings, et déssine! \n\n Jamie,, tu devrais montrer à [PCname] quelques dessins un de ces jours!"

    python:
        Jamie_State["sweat"] = 0
        Jamie_State["eye"] = 7
        Jamie_State["mouth"] = 4
        Jamie_State["armR"] = 0
    voice jamie_growld
    Jamie "No."

    python:
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 1
    voice atlas_frustration
    Atlas "Mais tu déssines tellement bien!"

    Robyn "Compréhensible."

    python:
        Atlas_State["eye"] = 7

        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 0
        Jamie_State["brow"] = 5
        Jamie_State["mouth"] = 0

    voice taro_dismissive
    Taro "Bon je suppose que je vais partir un peu, vu que t'a l'air d'être entre de si bonnes mains."
    python:
        Jamie_State["sweat"] = 0
        Jamie_State["brow"] = 1

    show taro:
        ease 3.0 yoffset 500

    Narrator "Le félin disparais dans les feuillages."
    python:
        Jamie_State["brow"] = 0
        Jamie_State["eye"] = 3

    voice jamie_scoffb
    Jamie "On devrais y aller nous aussi."

    Narrator "Jamie prend la chaine qui retient les grillages, et le séctionne en 2. Elle coupe le cadena et fait un petit pouce en l'air."
    python:
        Jamie_State["r3Fire"] = 1
        Jamie_State["armR"] = 2
        Jamie_State["mouth"] = 2
        Jamie_State["eye"] = 6
        Jamie_State["steam"] = 1



    voice jamie_crimes
    Jamie "{bt=4}Let the crimes commence.{/bt}"
    #show BGCG Outside Radio Station Fence: die fence
        #ease 2.0 yoffset 700

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 0

        Jamie_State["r3Fire"] = 0
        Jamie_State["armR"] = 0

    show jamie:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        parallel:
            ease 1.25 xcenter 1.3
        parallel:
            ease 0.7 matrixtransform RotateMatrix(0.0,-180.0,0.0)

    show robyn:
        ease 1.0 xcenter 0.35

    show atlas:
        ease 1.0 xcenter 0.5
    Robyn "C'est une idée horrible. Et si quelqu'un se blesse?"

    Narrator "Tu hésite et t'arrètes juste avant la clôture."
    python:
        Atlas_State["eye"] = 0
        Atlas_State["feelers"] = 0

    show robyn:
        xcenter 0.35
    $Atlas_State["eye"] = 16

    #Narrator "Atlas nudges you and smiles with his eyes, his antennae flicking forward as he tilts his head to one side."

    Atlas "Psh,, les fantômes sont pratiquement innofensifs. Je suis sur ce mec c'est genre une voie distordue ou un micro possèdé."
    python:
        Atlas_State["eye"] = 6
        Atlas_State["armL"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["sparkle"] = 1
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 3
        Robyn_State["brow"] = 1
    Atlas "Et puis, je suis là pour te protèger!"
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 0
    $Robyn_State["mouth"] = 5
    $Atlas_State["eye"] = 0
    $Atlas_State["sparkle"] = 0
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    Robyn "Mmmh,, nan c'est plûtot l'inverse."
    $Atlas_State["eye"] = 1
    $Robyn_State["eyes"] = 0
    $Robyn_State["brow"] = 1
    Jamie "Dépèchez vous!"
    show atlas:
        ease 2.5 xcenter 1.5

    show robyn:
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        pause 0.2
        ease 1.0 xcenter 0.55
        pause 0.2
        ease 0.4 matrixtransform RotateMatrix(0.0,180.0,0.0)
        pause 0.6
        ease 0.4 matrixtransform RotateMatrix(0.0,360.0,0.0)
        pause 0.2
        linear 0.1 yoffset -20
        linear 0.1 yoffset 0
        ease 0.7 xcenter 1.5
    #Narrator "Reluctantly, you follow suit, trailing after Atlas as you three approach the abandoned station."
    $Robyn_State["eyes"] = 2
    $Robyn_State["brow"] = 0
    play sfx rustyDoor
    Narrator "L'éxterieur de la station est taggé avec des vieux graffitis et recouvert de posters de condamnation déchirés. Jamie tourne la poignée de la porte et l'ouvre facilement."

    Atlas "Creepy!"
    jump exploreStation

label exploreStation:
    scene BG Hallway Radio Station with Fade(0.75, 0.25, 0.75, color="#000")
    stop ambiance fadeout 1.0
    Narrator "En regardant dans le couloir, l'interieur de l'endroit a l'air impossiblement propre par rapport à l'exterieur. La salle d'attente à l'air suspendu dans le temps, seulement salie par des moits de négligence... peut-être même des années."
    python:
        Atlas_State["eye"] = 1

    show robyn:
        matrixcolor TintMatrix("#fccaca")
        xcenter -0.5
        ease 2.0 xcenter 0.3

    show jamie:
        matrixcolor TintMatrix("#fccaca")
        xcenter -0.5
        pause 1.0
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        ease 2.0 xcenter 0.8
        ease 0.3 matrixtransform RotateMatrix(0.0,0.0,0.0)

    show atlas:
        matrixcolor TintMatrix("#fccaca")
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter -0.5
        ease 2.0 xcenter 0.5


    Narrator "Tu avance en ligne derrière Jamie alors que tu examine l'acceuil. Après un moment, Tu réalise que tu est la seule personne avec une lampe."

    show robyn:
        xcenter 0.3

    Robyn "Vous pouvez tous voir dans le noir?"


    python:
        Jamie_State["armR"] = 2
        Jamie_State["eye"] = 1
        Jamie_State["steam"] = 0
        Jamie_State["mouth"] = 0

    Jamie "En effet, mes yeux percent l'obscurité."
    show jamie:
        xcenter 0.8
        matrixtransform RotateMatrix(0.0,0.0,0.0)

    python:
        Jamie_State["armR"] = 0
        Jamie_State["eye"] = 3

        Atlas_State["armL"] = 1
        Atlas_State["eye"] = 6
    show atlas:
        xcenter 0.5
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 7.0) yoffset 30
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 0.0) yoffset 0
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 7.0) yoffset 30
        ease 0.15 matrixtransform RotateMatrix(0.0, 180.0, 0.0) yoffset 0

    Atlas "En fait moi c'est avec mes antennes, et ces bon vieux gros yeux ma vision est super sensible à la lumière."

    python:
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 0

        Robyn_State["mouth"] = 3
    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Atlas "Okay, c'est plus sentir que voir."

    python:
        Atlas_State["eye"] = 1

    python:
        Jamie_State["eye"] = 4

    show jamie:
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.805
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.805
        linear 0.05 xcenter 0.795
        linear 0.05 xcenter 0.8

    voice jamie_annoyedb
    Jamie "Atlas, tu peux passer un jour sans mentionner tes parties d'insecte?"


    python:
        Jamie_State["eye"] = 1

    python:
        Robyn_State["mouth"] = 4
    show jamie:
        xcenter 0.8

    Robyn "Ca me dérange pas honnètement."

    python:
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 1

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.8 matrixtransform RotateMatrix(0.0, 360.0, 0.0)

    Narrator  "Tu fait tourner la lampe dans tes mains, la fesant presque chuter dans le processus."

    python:
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 1.5 xcenter 0.2

    show jamie:
        ease 1.5 xcenter 0.45

    show atlas:
        ease 1.5 xcenter 0.8

    Narrator "En se balladant, Atlas essaie la porte la plus proche. Après l'avoir trouvé fermée, il tourne son regard vers la fenètre du studio d'enregistrement."

    Narrator "Jamie donne un coup dans une des poubelles et la renverse. Une douzaine de cannettes vertes tombent sur le sol, s'étallant un peu partout."

    python:
        Jamie_State["eye"] = 8
        Jamie_State["brow"] = 2

    show jamie:
        xcenter 0.45

    show atlas:
        xcenter 0.8

    Jamie "Pour une maison hanté pas vérouillée, c'est plûtot en bon état. Je me sens presque mal à salir l'endroit."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 0

    Robyn "Où est-ce que tu crois qu'on trouvera le spectre?"

    python:
        Atlas_State["eye"] = 17
        Atlas_State["armL"] = 1
        Atlas_State["armR"] = 1
        Jamie_State["eye"] = 0
        Robyn_State["mouth"] = 5

    Atlas "T'a mit la fréquence fantôme,, n'est-ce pas?"

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
    #Narrator "Atlas perks up, his feelers twitching, as he stands back and turns around."

    Robyn "..."

    show atlas:
        matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 360.0, -7.0) yoffset 30
        ease 0.3 matrixtransform RotateMatrix(0.0, 360.0, 0.0) yoffset 0

    python:
        Atlas_State["eye"] = 16
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0

    Narrator "Atlas te hôche la tête d'une manière rassurante."

    $Atlas_State["eye"] = 0


    voice atlas_dismissive
    Atlas "C'est pas grave si tu l'a pas fait."

    $Atlas_State["eye"] = 1
    $Atlas_State["eyeFrame"] = 6
    camera:
        ease 8.0 zoom 2.3 xcenter 1.05 ycenter 0.8

    Atlas "Je vais te mettre à jour. En gros, le show c'était ce mec, Madhouse Mike, il lisait des histoires de cryptides et des légendes urbaines comme script. C'était super cool et j'ai vraiment aimé."
    camera:
        zoom 2.3 xcenter 1.05 ycenter 0.8
        ease 0.3 xoffset -1500

    $displaymenu = True
    Robyn "Je vois vraiment pas comment-.{nw}"
    $displaymenu = False
    camera:
        ease 0.3 xoffset 0

    $Atlas_State["eyeFrame"] = 2
    $Atlas_State["eye"] = 0

    Atlas "Bref, c'est le fantôme qu'on cherche. Madhouse était un {color=#3bec27}{b}EXPERT{/b}{/color} sur le super-naturel, donc je suis quasi sûr qu'il sait un truc sur ta malédiction."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 1

    Jamie "Mike joue un personnage, Atlas. Qui sait qui ce type est vraiment en dehors du stage."
    show jamie:
        ease 3.0 xcenter -0.5
    show robyn:
        ease 1.0 xcenter 0.5
    Narrator "Jamie écrase une des cannettes par accident et la remet dans la poubelle."

    python:
        Atlas_State["eyeFrame"] = 3
        Atlas_State["eye"] = 2
        Atlas_State["feelers"] = 1

    camera:
        ease 4.0 zoom 1.6 xcenter 0.8 ycenter 0.7

    show robyn:
        xcenter 0.5

    #Narrator "Atlas’ antennae droop and he looks away."

    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Robyn "Les fantômes sont pas censé être créée avec des tragédies? Il a l'air plûtot normal selon moi."

    python:
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["eyeFrame"] = 0
        Atlas_State["feelers"] = 0
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 2
    show atlas:
        matrixtransform RotateMatrix(0.0, 360.0, 0.0)
        ease 0.2 yoffset -30
        ease 0.2 yoffset 0
    Narrator "Atlas gasps."

    python:
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 1
        Atlas_State["eye"] = 6
    camera:
        ease 0.5  zoom 3.5 xcenter 1.15 ycenter 0.85

    voice atlas_gotastory
    Atlas "{bt=5}Oh! C'était super tragique!{/bt}"

    Atlas "Madhouse est mort pendant qu'il fesait la promotion d'une marque de boison energisante super sketchy! Il a cru que boire la boite entière d'échantillions serait une bonne idée."

    Atlas "Ca a marché pendant genre... Deux secondes."

    python:
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 8
        Atlas_State["feelers"] = 1
        Atlas_State["sparkle"] = 0

    Atlas "J'veux dire,, Vraiment. Qui peut avoir confiance en une companie du nom de Toxic Waste Energy?"
    camera:
        ease 0.5 xoffset -1400 yoffset -100
    $displaymenu = True
    Robyn "That’s terrible—{nw}"
    $displaymenu = False
    camera:
        ease 0.5 xoffset 0 yoffset 0

    python:
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["feelers"] = 3
        Atlas_State["eye"] = 9
    show atlas:
        yoffset 0
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Atlas "{sc=1}Il en à bu tellement que sa peau s'est mise a briller d'une couleur {color=#3bec27}vert fluo{/color}{/sc} et il est mort instant de toute la radiation! \n\nLe studio a du fermer, et personne de vivant a été sur l'air depuis!"

    camera:
        ease 0.5 xoffset -1400 yoffset -100

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Jamie "Tu t'entend parler, serieux?"

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 2
    Atlas "C'est exactement le genre de truc qu'il aurait voulu! Gérer une station radio pour le reste de l'éternité? Ca a l'air trop cool!"
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    python:
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 3

    voice jamie_annoyedb
    Jamie "Se transformer en fantôme sociopathe coincé dans un endroit pareil est problablement le pire scenario du monde."

    python:
        Jamie_State["eye"] = 1
        Jamie_State["brow"] = 3
        Atlas_State["armR"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2
    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 3.0 xcenter 0.3

    camera:
        parallel:
            ease 4.0 zoom 1.0 xcenter 0.5 ycenter 0.5
        parallel:
            ease 3.0  xoffset 0 yoffset 0
    Atlas "C'est marrant, je l'écoutait beaucoup quand j'était encore sur mon ancien job a l'époque. Tu sais, avant que je me fasse virer pour avoir été cambriolé 2 fois et avoir commencé un feu éléctrique. Le type c'était une légende pour nous."

    #Jamie Expression needed
    python:
        Atlas_State["eye"] = 7
        Jamie_State["armR"] = 3
    Jamie "T'a vraiment pas de chance mon pauvre."

    #Atlas expression needed
    python:
        Atlas_State["eye"] = 18
        Atlas_State["feelers"] = 0
    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Atlas "T'es littéralement un démon!"
    Robyn "Doooonc, c'est juste une rumeur."
    python:
        Jamie_State["eye"] = 4

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 360.0, 0.0)
    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["brow"] = 0

    Jamie "Les rumeurs vont pas nous aider,, on doit chercher l'endroit pour trouver plus d'infos."

    python:
        Atlas_State["eyeFrame"] = 0
        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 0
    show robyn:
        matrixtransform RotateMatrix(0, 360, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
        ease 0.5 xcenter 0.2
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
    show jamie:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 xcenter 0.4

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    $Atlas_State["eye"] = 19

    Atlas "Et risquer énerver le type a qui on est sur le point de rentrer en plein dans son émition radio? Hors de question!"

    Jamie "Enerver?"

    python:
        Jamie_State["armR"] = 2
        Jamie_State["mouth"] = 2
        Jamie_State["eye"] = 6
        Jamie_State["steam"] = 1
        Jamie_State["brow"] = 1
        Atlas_State["eye"] = 7
        Atlas_State["feelers"] = 1
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 0
        Robyn_State["brow"] = 1

    voice jamie_annoyeda
    Jamie "Atlas on est des trépasseurs!"
    $Atlas_State["eye"] = 19
    Atlas "T'en pense quoi, {i}TOI{/i}, [PCname]?"

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 18
    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0) xcenter 0.45
    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Narrator "Jamie et Atlas se tournent vers toi, éspérant que tu trouve un terme aux arguments."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 0
        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["steam"] = 0
        Jamie_State["eye"] = 1

    Robyn "Jamie à raison. On dois éssayer de trouver un truc utile, genre un coffre fantôme ou un espèce de portail vers une autre dimmension."

    show robyn:
        ease 1.0 xcenter 0.55

    show jamie:
        ease 1.0 xcenter 0.3
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    python:
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 1

    Robyn "Atlas, pense a tout le merch exclusif—! Tu pourrais même demander pour un autographe."
    $Atlas_State["eye"] = 4
    $Atlas_State["feelers"] = 0

    Atlas "Tu croit? En fait, verifions la salle des enregistrements, doit y a voir des vinyls collector ou des cassettes exclusives quelque part."

    Narrator "Les yeux du mothman s'illuminent."

    python:
        Atlas_State["eye"] = 9
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 0
        Jamie_State["armR"] = 0

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 3.0 xcenter 1.5
    Atlas "T'sais, pour la recherche."

    show jamie:
        ease 2.0 xcenter 0.75
    Narrator "Jamie passe a coté de toi et ouvre la porte, pour te laisser entrer en premier."

    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 1

    voice jamie_scoffa
    Jamie "Puis zut,, j'ai envie de voir ce {i}type cinglé{/i} après tout."

    $Robyn_State["eyes"] = 4
    #Narrator "En évitant les yeux bleus illuminés de Jamie, ton coeur manque un battement à ses mots. Même si iel à accepté de se joindre à toi, t'a quand même l'impression qu'iel est en train de te brûler un trou dans le torse."

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

    show robyn:
        ease 0.3 xcenter 0.5
    Robyn "Hey,, Je me demandais, pourquoi t'a voulu venir avec nous?"

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 0

    #Narrator "Jamie thinks a moment before answering flatly."

    Jamie "Je voulais te rencontrer."

    python:
        Robyn_State["eyes"] = 0

    Jamie "Un humain normal qui arrive a Longhope c'est pas tout les jours."

    python:
        Robyn_State["mouth"] = 4
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 0

    Robyn "Qu'est-ce qui te fait dire ça?"

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 1

    Jamie "Les gens par içi on tendence à être,, mort, volant ou aquatique. \n\nCe que au dernières nouvelles tu n'est pas."

    $Robyn_State["eyes"] = 2
    $Robyn_State["mouth"] = 5

    voice RobynSays("Generic","ConfusedA")
    Robyn "Ouais."

    Jamie "Alors un truc t'a ammené içi."

    Narrator "Son expression s'assombre, son regard descent avant de se poser sur toi. Ta gorge sent sèche tandis que tu éssaie de sortir une réponse."

    Robyn "Eh ben... Je connais Atlas depuis genre,, toujours! Il m'a aidé a déballer!"

    Jamie "Non. \n\nY'a autre chose."

    $Robyn_State["mouth"] = 5
    $Robyn_State["eyes"] = 3
    $Robyn_State["brow"] = 2

    Robyn "Jamie, tu est horriblement cryptique."

    #Narrator "You hardly manage to squeak out your words, ready to buckle under Jamie’s suffocating aura."

    Jamie "J'ai l'habitude."

    voice RobynSays("Generic","HmphB")
    Robyn "Um, D'accord."

    Jamie "Mais ne sautons pas au conclusions."

    Narrator "Tu te dit que Jamie te déteste définitivement maintenant. Tu dois essayer de sauver ça."

    Robyn "{bt=4}Doooonc{/bt}, tu seras là pour la soirée film de vendrendi soir, pas vrai?"

    $Robyn_State["eyes"] = 0
    $Jamie_State["armR"] = 1
    $Jamie_State["eye"] = 2
    $Robyn_State["mouth"] = 1

    show jamie:
        matrixtransform RotateMatrix(0, 180, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 0, 0)

    Narrator "Les yeux de Jamie s'allument, la flamme au dessus de sa tête brille d'une manière plus vaste."

    Jamie "Ammener des patates douces farcies, des brochettes de poulet et une trempette aux jalapeños."

    Narrator "Tu imagine Jamie vétu d'un tablier à carreaux vichy et des gants de cuisine tout en portant un plateau de snickerdoodles fraîchement sortis du four."

    $Robyn_State["mouth"] = 4
    $Robyn_State["brow"] = 2

    Robyn "Tu cuisine?"

    $Jamie_State["eye"] = 6
    $Jamie_State["armR"] = 2
    $Robyn_State["eyes"] = 2

    voice jamie_happya
    Jamie "{sc=1}{color=#ff0f4f}Mi-temps.{/color}{/sc}"

    $Robyn_State["mouth"] = 0

    Robyn "J'ai {sc=1}teeeellement{/sc} de questions."

    $Jamie_State["eye"] = 7
    $Jamie_State["mouth"] = 1

    Jamie "Ils me surnomment le {bt=4}Maître du gril{/bt}."
    $Jamie_State["mouth"] = 0
    Robyn "Jamie, j'ai besoin de réponses."

    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 0
    $Robyn_State["mouth"] = 3
    $Robyn_State["eyes"] = 1
    $Robyn_State["brow"] = 2

    show jamie:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 180, 0)
    Jamie "Et moi j'ai besoin que tu continue de marcher."

    show jamie:
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.75 xcenter 1.5

    show robyn:
        ease 1.75 xcenter 1.3

    $Jamie_State["eyes"] = 4

    Robyn "Ca marche, {bt=4}Maître du gril!{/bt}"

    voice jamie_angry
    Jamie "Ne m'appèle pas comme ça, s'il te plaît."

    Robyn "Pardon."

    scene black with dissolve
    play sfx rustyDoor
    Narrator "Avec un grognement, tu parvient a ouvrir la porte, fesant tomber un tiroir qui bloquait la porte dans la salle."

    Narrator "Tu marche par dessus et regarde le bureau."
    scene  BG Office Dark Spooky
    python:
        Atlas_State["eye"] = 3
        Atlas_State["eyeFrame"] = 3
        Atlas_State["tears"] = 1

    show atlas:
        matrixcolor TintMatrix("#d1ffe1")
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        xcenter 0.85
        yoffset 75

    with Fade(0.25, 0.5, 0.75, color="#000")
    Narrator "Tout est défoncé. Des papiers déchirés sont étalés sur le tapis, un liquide gluant vert est répendu sur les murs, et une étagère autrefois remplie d'enregistrements et de vinyls se voit explosé sur le sol en morceaux."

    python:
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0

        Jamie_State["eye"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["brow"] = 0

    show robyn:
        xcenter 0.55
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor BrightnessMatrix(-1)*TintMatrix("#d1ffe1")
        blur 20
        alpha 0
        ease 0.5 blur 0 alpha 1
        ease 0.25 matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        ease 0.7 xcenter 0.3
        ease 0.3 matrixtransform RotateMatrix(0, 0, 0)

    Robyn "Oh wow."

    #Narrator "Atlas hatèle et se rue sur la pile d'enregistrements détruits sur le sol."
    show robyn:
        xcenter 0.3
        alpha 1
        matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        blur 0
        matrixtransform RotateMatrix(0, 0, 0)


    voice atlas_frustration
    Atlas "{sc=3}Nooon{/sc}! Quel genre de monstre à bien pu faire ça!"


    Narrator  "Le mothman fouille dans les enregistrements tous écrasés, laissant passer des fragments tomber de ses mains."

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0) yoffset 75
    Atlas "{sc=1}C'était des copies originales{/sc}!"

    python:
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.5
        ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    Robyn "Tu pouvais pas juste télécharger l'album digital?"

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show jamie:
        alpha 0
        xcenter 0.62
        matrixcolor BrightnessMatrix(-1)*TintMatrix("#d1ffe1")
        blur 20
        ease 0.5 alpha 1.0 blur 0
        ease 0.25 matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        yoffset 75

        parallel:
            ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        parallel:
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85
            ease 0.1 xcenter 0.87
            ease 0.1 xcenter 0.85

    $Atlas_State["eye"] = 12
    $Atlas_State["eyeFrame"] = 1
    $Atlas_State["tears"] = 0
    $Atlas_State["feelers"] = 1

    Atlas "{sc=3}Non!{/sc} Tout est dans le riche, son omni-dimensionel!"

    python:
        Jamie_State["eye"] = 3
        Jamie_State["mouth"] = 0
        Jamie_State["brow"] = 1
        Jamie_State["armR"] = 2

    show jamie:
        alpha 1
        matrixcolor BrightnessMatrix(0)*TintMatrix("#d1ffe1")
        blur 0
        ease 1.5 xcenter 0.3

    show robyn:
        ease 1.5 xcenter 0.5

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 5.0)
    Narrator "En ignorant les blablatages d'Atlas, Jamie passe ses mains sur les murs, lisant les mots écrit dans le slime vert."

    python:
        Robyn_State["eyes"] = 2
        Jamie_State["eye"] = 0
        Jamie_State["brow"] = 4
        Jamie_State["mouth"] = 4
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 1
    show robyn:
        xcenter 0.5

    show jamie:
        xcenter 0.3


    Jamie "‘Daily ghost watch point net'... C'est quoi ce charabia?"
    $Jamie_State["mouth"] = 0
    $Jamie_State["armR"] = 0
    $Robyn_State["mouth"] = 5
    $Robyn_State["eye"] = 1
    show jamie:
        ease 0.3 xcenter 0.33
    #Narrator "Jamie recule, lisant les mots sur le mur."

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    voice RobynSays("Generic","Thinking")
    Robyn "On dirait un site web."

    python:
        Atlas_State["tears"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["eyeFrame"] = 0
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 5.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 5.0)

    Narrator "Atlas se lève du tas de ce qui reste des vinyls, et éssuie les larmes sur ses yeux."

    show robyn:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

    show jamie:
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.4 matrixtransform RotateMatrix(0, 180, 0) xcenter 0.25

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 5.0)

    $Atlas_State["eye"] = 0
    $Atlas_State["eyeFrame"] = 5

    Atlas "Pff, c'est juste un blog qui parle de paranormal."

    $Jamie_State["eye"] = 3
    $Robyn_State["eyes"] = 4

    Jamie "Logique."

    $Atlas_State["eye"] = 14
    $Atlas_State["feelers"] = 0
    $Atlas_State["eyeFrame"] = 0
    $Jamie_State["brow"] = 0

    Atlas "J'était dessus pendant genre un mois en fait."
    $Jamie_State["mouth"] = 1
    $Jamie_State["eye"] = 1
    $Atlas_State["eye"] = 13
    Jamie "Ew."

    $Jamie_State["mouth"] = 0
    $Jamie_State["eye"] = 0
    $Robyn_State["brow"] = 3
    $Robyn_State["eyes"] = 2

    show robyn:
        ease 0.2 yoffset -20
        ease 0.2 yoffset 0


    Robyn "C'est important la modération!"
    $Jamie_State["eye"] = 2
    $Atlas_State["eye"] = 18
    $Robyn_State["brow"] = 0
    $Robyn_State["mouth"] = 1

    Jamie "Ouaaais,, vous feriez mieux de vous dépècher les nerds."

    $Robyn_State["mouth"] = 3

    show robyn:
        yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.3 yoffset 20 matrixtransform RotateMatrix(0.0, 0.0, 5.0)
        ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    Robyn "Je vais essayer."

    $Atlas_State["eye"] = 1
    $Jamie_State["eye"] = 1
    $startInvest = True


    jump investigation_loop

label investigation_loop:
    show jamie:
        ease 0.4 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.7 xcenter 0.2

    show robyn:
        ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.6 xcenter 0.5

    show atlas:
        ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.85

    $displaymenu = True

    if startInvest:
        python:
            inv1 = True
            inv2 = True
            inv3 = True
            inv4 = True
            inv5 = True
            inv6 = True
            inv7 = True

            numInvest = 0
            startInvest = False
            mCaseInvest = False
        Robyn "Où-est-ce que je commence?{nw}"
    else:
        Robyn "Voyons voir...{nw}"

    menu:
        extend ""

        "L'ordinateur" if inv1:
            python:
                displaymenu = False
                inv1 = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 5
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.2

            show jamie:
                ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.7 xcenter 0.5

            show atlas:
                ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.8 xcenter 0.85

            Narrator "Tu arrive devant le bureau dans le coin de la salle."

            Narrator "Un viel ordinateur a peine vivant reste sur le bureau, un unique post-it collé sur l'écran. Il lit, Mot de passe: 'deathproof' en mal écrit."

            $Robyn_State["mouth"] = 1
            $Robyn_State["brow"] = 1

            Narrator "Tu clique sur le bouton de l'écran, qui finit par s'allumer montrant une photo de groupe de ce qui semble être les membres du studio avant l'incident."

            Narrator "Tu clique sur une icone dans la barre des tâches, une page web minimisée apparait et te voilà acceuili par le forum du nom de ghost hunting problems."

            Narrator "Quelqu'un a déscendu la page, laissant des commentaires en se disputant avec des utilisateurs sous le nom de {i}RadioGhost1.{/i}"

            Narrator "Un des commentaires dit, Ce mec est trop cool! Je me demande ce qu'il était dans la vraie vie. Une réponse en dessous du poste cite, Super post! Le paradis ne sait pas ce qu'il manque, LOL."

            python:
                Robyn_State["eyes"] = 4

            Narrator "Tu scroll et voit que, RadioGhost1' a été banni pour self advertising."

            python:
                Robyn_State["eyes"] = 0
                Robyn_State["mouth"] = 4
                Robyn_State["brow"] = 1

            show robyn:
                ease 0.2 yoffset -50
                ease 0.2 yoffset 0

            Narrator "Tu était sur le point de regarder les autres onglets du navigateur, mais un touché froid te coupe par derrière."

            python:
                Robyn_State["mouth"] = 1
            show Debbie Prop:
                alpha 0
                ease 0.5 alpha 1.0
            Narrator "Tu te retourne rapidement, et remarque une figure humanoide fait de cannettes de Toxic Waste qui s'assoit sur la chaise du bureau."

            Narrator "La création a un sourire déssiné au marqeur, sa tête est faite d'un barril d'eau en plastique a moitié écrasé et de trombones qui ressemble a des cheveux. Une étiquette sur son front lit Debbie."
            show Debbie Prop Leave:
                alpha 1
                pause 0.5
                ease 0.5 alpha 0
            Robyn "C'est serieusement creepy."
            hide Debbie Prop

        "Boohou Answers" if inv6 and not inv1:
            python:
                inv6 = False
                displaymenu = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 5
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.2

            show jamie:
                ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.7 xcenter 0.5

            show atlas:
                ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.8 xcenter 0.85
            $Atlas_State["eye"] = 2
            $Atlas_State["phone"] = 1
            $Jamie_State["eye"] = 3
            $Robyn_State["eye"] = 0

            Narrator "Tu retourne vers l'ordi et continue de chercher dedans. Un autre onglet liste un site appelé BooHoo Answers."
            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "{i}Question: Comment bannir un fantôme?{/i}"

            Computer "Salut, j'ai un fantôme qui vit chez moi et ce depuis 6 ans. J'ai tout éssayé— Psychés, Prètres, investigations et plus encore! IL VEUT PAS PARTIR! HELP. (10 Answers)"

            $Computer = Character("L0GIC", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "3A", who_color = "#f0bf6c")
            Computer "Demande lui de payer un loyer, mais monte le tous les mois. (Top Reply)"

            $Computer = Character("Para_Mama", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "#e96cf0")
            Computer "Attend un peu chéri, si il te faut un medium j'accepte les sessions virtuelles. Je te donne mon site web si il te faut d'autres ressources. Bonne chance! :)"

            $Computer = Character("(Deleted)", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "7B", who_color = "#ff3232")
            Computer "Meeeec pareil! J'ai un spectre de sang dans le mirroir de ma salle de bain et elle veut pas arrèter de taper sur la vitre!. Elle veut quoi? \n\n(Dernièrement en ligne il y a 725 jours)"

            $Computer = Character("FaeBae", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "10A", who_color = "#7b78ff")
            Computer "Tu prend un feutre rouge, tu déssine deux cercles qui se touchent suivit par une longue ovale qui connecte les deux formes, de préférence sur le mur. C'est comme des protections qui banissent les ésprits!"

            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "Pas marché, et aussi, va te faire foutre!"

            $Computer = Character("Dan105.1", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "10C", who_color = "#6cbcf0")
            Computer "Tu veux mon secret? Pain à l'ail. Je mange genre 6 morceaux par jour et j'ai jamais vu un fantôme."

            $Computer = Character("RadioGhost2", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#79f06c")
            Computer "Vous croyez vraiment que je suis là pour rien?! Si c'était si simple je vous parlerais même pas! Vous êtes tous des putains de fraudes!!"

            Narrator "L'utilisateur a été banni a vie."

        "Voix éttoufés" if inv7 and numInvest >= 2:
            python:
                inv7 = False
                displaymenu = False
                renpy.block_rollback()
                Voice = Character("???", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27")

            Narrator "Tu entend des petites voies derrière la porte et porte ton oreille dessus pour écouter."

            Voice "Debbie arrète de mettre de la merde avec les lettres de fan!\n\n{sc=2} J'ai pas envie de lire plus{b}D'ARNAQUES!{/b}{/sc}"

            Narrator "Il y a une longue pause avant que les voies ne reprennent."

            Voice "Ecoute je me demandais... à propos de mes horaires. Tu vois, normallement je suis plus précis q'une morsure de loup! Mais là, la dernière décénnie à été plûtot chiante..."

            Voice "Je me disais, je pourrais faire une pose! J'ai envie de reconnecter avec cette partie vivante de moi."

            Narrator "Il y a un silence avant qu'un bruit de métal qui touche le sol ne puisse être entendu, suivi d'un son de prise de quelqu'un sur une cannette. "

        "Bulletins" if inv2:
            python:
                inv2 = False
                displaymenu = False
                renpy.block_rollback()

                Atlas_State["tears"] = 0
                Atlas_State["eye"] = 2
                Atlas_State["eyeFrame"] = 0

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 1.0 xcenter 0.4

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 1.0 xcenter 0.2

            Narrator "Tu regarde le panneau sur le mur, prenant note des nombreuses pages attachés dessus."

            Narrator "Des moustaches au marqeur sont mises sur une photo de groupe, un homme portant une veste rouge complètement rayé."

            Narrator "Un calendrier est aussi attaché au mur, la date du 21 Aout entouré et noté, “Médecin.” Il y a même un coupon pour une canette gratuite de Toxic Waste Energy glissé sur le coté."

            show robyn:
                ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
                ease 0.8 xcenter 0.6
            Narrator "Tu arrache le coupon, et l'apporte à Atlas ésperant un peu d'information."

            Robyn "C'est quoi?"

            show atlas:
                matrixtransform RotateMatrix(0, 180, 0)
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                pause 0.6
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)

            voice atlas_thinking
            $Atlas_State["eye"] = 3
            Atlas "Hm? Oh, c'est la boisson qui a tué Madhouse Mike! Il est connu pour avoir une quantitée atroce de cafféine."
            $Atlas_State["eye"] = 13

            Narrator "Tu regrette imédiatement avoir demandé, mais décide de garder le coupon quand même... au cas où?"

        "Papiers sur le sol" if mCaseInvest and inv3:
            python:
                inv3 = False
                displaymenu = False
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2

            show robyn:
                ease 1.0 xcenter 0.45

            Narrator "Tu recule d'un pas, et sent quelque chose sur ta chaussure. Tu baisse les yeux, et réalise que tu à marché sur des factures impayés adressés à la station d'Elkhorn."

            show robyn:
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
                ease 0.7 yoffset 150 matrixtransform RotateMatrix(0.0, 180.0, -10.0)
                ease 0.7 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

            Narrator  "Tu t'accroupis, et prend un journal froissé sur le sol accusant Elkhorn Radio de conditions de travail négligés et de longues heures de travail. L'Auteur a l'air d'avoir mit beaucoup de coeur dans cet article. Tu lit la dernière phrase a voix haute."

            voice RobynSays("Generic","HmphB")
            Robyn "{i}J'éspère que le gérant de la station face la justice...{/i}"

        "Dead Carnations" if numInvest >= 2 and inv4:
            python:
                inv4 = False
                displaymenu = False
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2

            show atlas:
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.5

            show robyn:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.8


            play sfx emote_realization_sfx
            Narrator "Dans la poubelle se trouve un vase rempli d'œillets roses et blancs. Une petite carte est glissée sur le coté. Tu la ramasse en fronssant les sourcils, elle lit {i}Voilà cinq ans chez Elkhorn Radio et bien plus encore !{/i}"

            Narrator "Regardant la carte, Atlas juge."

            Atlas "Oof, pas cool."

        "Etagère a trophées" if inv5:
            python:
                inv5 = False
                displaymenu = False
                mCaseInvest = True
                renpy.block_rollback()

            show jamie:
                ease 0.4 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.2
            show atlas:
                ease 0.3 matrixtransform RotateMatrix(0, 0, 0)
                ease 1.0 xcenter 0.6
                ease 0.3 matrixtransform RotateMatrix(0, 180, 0)
            show robyn:
                ease 1.0 xcenter 0.8
            Narrator "En suivant la trace des papiers, tu t'arrête devant la boîte à trophées cassée avec les mots \"Pue plus que Momo\" spray-painted en rouge par dessus tout le truc." #, stepping over the glass shattered against the floor.

            Narrator "Ont dirait qu'il y ait eu diverses commémorations et récompenses célébrant les divertissements radiophoniques diffusés par la station..."

            Narrator "Tu regarde la déstruction, seulement pour trouver les restes d'Awards pour des gens comme Shark Infinity, Tiny Red Panda, et DJ Bean Angel. Rien sur Madhouse, cependant."

            Robyn "Ont dirait que Mike avait beaucoup de... Personalité."

            #voice atlas_booyah
            Atlas "Meec! Shark Infinity a enregistré ici—!"


    $numInvest +=1
    if numInvest == 2:  #2 Things have been investigated
        show jamie:
            ease 0.4 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.7 xcenter 0.2

        show robyn:
            ease 0.3 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.6 xcenter 0.85

        show atlas:
            ease 0.2 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            ease 0.8 xcenter 0.5
        $Atlas_State["phone"] = 1
        Narrator "Atlas est collé au mur près de la porte, a scroller sur son portable."
        $Atlas_State["eye"] = 1
        play sfx emote_realization_sfx
        Atlas "Apparament, le Daily Ghost à écrit un article sur Elkhorn Station."

        Narrator "Le mothman écume sur le post."
        $Atlas_State["eye"] = 3
        $Jamie_State["eye"] = 1
        $Robyn_State["eyes"] = 2

        Atlas "Wow. Ca les dérange pas de citer Mike par son nom."
        show jamie:
            ease 0.4 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        voice jamie_scoffa
        Jamie "C'est important?"

        Atlas "Mike c'est juste un poltergeist sans visage pour ces gens. Tu vois? Litteralement pas de visage."

        Narrator "Atlas te montre son portable, affichant une masse verte floue qui porte une casquette et une veste, c'est un peu dure a voir."

        Jamie "C'est pas justement comment ça marche?"

        Atlas "Je suppose que t'a raison."

        Narrator "Jamie lève les épaules et écarte son regard d'Atlas, sa queue renversant une petite poubelle, délâchant son contenu sur le sol."

        Jamie "Oops."

    if numInvest >= 7:
        jump endInvestigation


    call dice_roll(rMod=PC_Stats.cStats("brains"), rDiff=3+numInvest, rDesc="Investigation") from _call_dice_roll
    if isRollSuccess:# True:#
        jump investigation_loop #Loop Back
    else:
        jump endInvestigation #End

label endInvestigation:
    Jamie "Bon on doit y aller."
    $Atlas_State["phone"] = 0


    Narrator "Jamie pointe la porte, sa queue bouge d'impatience."

    #voice atlas_defeated
    Atlas "Pff... oké. Y'a pas moyen que je sauve ça de toute façon."

    Narrator "Il dit avant de laisser les restes de vinyls sur le sol."

    scene BG Hallway Radio Station with Fade(0.75, 0.25, 0.75, color="#000")

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 16
        Atlas_State["sparkle"] = 1

    show atlas:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.5 xcenter 0.8

    Narrator "Atlas avance dans le couloir."

    show atlas:
        xcenter 0.8

    Jamie "\n\n{size=-5}Tu marche comme un pigeon.{/size}"

    show robyn:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 0, 0)
        ease 1.0 xcenter 0.35

    show jamie:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0, 180, 0)
        ease 1.0 xcenter 0.1

    Narrator "Suivant la voix d'Atlas, toi et Jamie tournez le coin et vous arrêtez brusquement. Il joue avec la poignée de porte."

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1


    Atlas "C'est complètement bloqué—"
    $musicPlayer.playSong()
    $musicNote = 12
    python:
        Atlas_State["eye"] = 3
    show atlas:
        ease 0.3 xcenter 2.0


    play sfx dramatic_boom_b
    Narrator "Atlas est interrompu lorsqu'une main jaillit de la porte, saisissant les plummes de son cou. Il s'arrête, confus, et se faufile derrière la porte."
    show atlas:
        xcenter 1.4
        matrixtransform RotateMatrix(0, 0, 0)
        ease 0.5 xcenter 0.8

    python:
        Atlas_State["eyeFrame"] = 5
        Atlas_State["eye"] = 0
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 0

    Atlas "Je suppose que je leur ai fait peur?"

    #show atlas:
        #ease 0.35 xcenter 1.4 matrixtransform RotateMatrix(0.0, 0.0, 90.0) yoffset 700

    show atlas:
        matrixtransform RotateMatrix(0, 0, 0)
        parallel:
            pause 0.1
            ease 0.5 yoffset 700
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0, 0, 180)
        parallel:
            ease 0.5 xcenter 1.2

    Narrator "La porte disparaît soudainement, laissant Atlas dégringoler dans la salle du Studio."


    $musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_wellwellwella
    Madhouse "{bt=3}Bien bien bien~{/bt}"

    voice mm_whattookyousolong
    Madhouse "Qu'est-ce qui vous a prit autant de temps? Vous trois m'avez complètement laisser raccroché’!"

    voice mm_deadairisacareerkiller
    Madhouse "Le Dead Air c'est un tueur de carrière dans ce domaine de travail. T'aurais au moins pu reprogrammer avec le producteur !"

    if not inv1:
        #voice PC_Thinking
        Robyn "Tu veut dire l'abomination en plastique sur la chaise du bureau?"

        Madhouse "Ah, donc vous avez vu Debbie!"

        Madhouse "Y' Parle pas beaucoup."

        voice mm_laugha
        Narrator "Le spectre rit a sa propre blague."

    #Madhouse "Bon, z'êtes qui et vous voulez quoi?"

    hide robyn
    hide jamie
    hide atlas
    show MM_Appears CG
    with { "master" : Dissolve(0.5) }


    Narrator "Il apparait soudainement dans ton champ de vision en toute sa splandeur."

    #voice PC_Confused
    Robyn "Donc tu EXISTE!"

    #voice MM_Listening1
    Madhouse "{sc=2}Evidement que je suis réel{/sc}! Tu crois j'hoste un show de radio pour de l'air? J'attendais un invité spécial depuis des lustres!"

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7
        Atlas_State["sparkle"] = 0

    show atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter -0.5
        yoffset -40
        matrixcolor TintMatrix("#ebabab")
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 35.0) xcenter -0.02
    Atlas "{bt=3}OHMONDIEU!{/bt} Mike Madhouse!"

    show atlas:
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        linear 0.05 xoffset 5
        linear 0.05 xoffset -5
        pause 1.0
        repeat

    Narrator "Atlas réspire fort, complètement époustouflé à la vue de son héros— une vraie légende urbaine."

    show atlas:
        xoffset 0
        xcenter -0.01
        on replaced:
            xcenter -0.05
            matrixtransform RotateMatrix(0.0, 180.0, 35.0)
            ease 0.5 xcenter -0.2 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show jamie:
        xcenter -0.5

    python:
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1

    voice atlas_hugefan
    Atlas "Oh boy— Je suis un éeeeenoooorme fan!"

    hide MM_Appears
    show atlas:
        xcenter 0.3
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        pause 0.65
        ease 0.7 yoffset 0

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 0
        MM_State["mouth"] = 0
        Jamie_State["mouth"] = 1
        Jamie_State["eye"] = 6
        Jamie_State["brow"] = 1
        Jamie_State["armR"] = 0

    show madhouse:
        matrixcolor TintMatrix("#ebabab")
        matrixtransform RotateMatrix(0.0, 0, 0.0)
        xcenter 1.5
        ease 0.5 xcenter 0.85

    show jamie behind atlas:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        matrixcolor TintMatrix("#ebabab")
        ease 1.5 xcenter 0.095
        linear 0.05 xcenter 0.105
        linear 0.05 xcenter 0.095
        linear 0.05 xcenter 0.105
        linear 0.05 xcenter 0.095
        repeat

    show robyn behind atlas:
        matrixcolor TintMatrix("#ebabab")
        xcenter -0.5
        matrixtransform RotateMatrix(0.0, 0, 0.0)
        ease 1.0 xcenter 0.45

    voice jamie_growld
    Jamie "{sc=3}Grrrr...{/sc}"

    Narrator "Atlas lève les yeux vers Jamie, actuellement possèdé d'un regard violent."

    python:
        Atlas_State["eyeframe"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1
        Robyn_State["mouth"] = 7
        Robyn_State["eyes"] = 4
        Robyn_State["brow"] = 2

    Atlas "Jamie... Non."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 6
        Jamie_State["armR"] = 3
        Atlas_State["eye"] = 1
        Robyn_State["mouth"] = 6
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 2

    show jamie:
        xcenter 0.1
    #Narrator "He turns back towards the phantom and squeaks."


    Atlas "On aimerais te rejoindre pour le show de ce soir!"

    Robyn "Et poser quelques questions."

    python:
        MM_State["armR"] = 2
        MM_State["armL"] = 2
        MM_State["eyes"] = 0
        MM_State["mouth"] = 3
        Atlas_State["eye"] = 7
        Atlas_State["feelers"] = 3
        Robyn_State["mouth"] = 1
        Robyn_State["eyes"] = 3
        Robyn_State["brow"] = 2

    $musicPlayer.playSong()
    Madhouse "Je sais pas si c'est une bonne idée-"

    Narrator "Madhouse s'arrète."

    python:
        MM_State["armR"] = 0
        MM_State["armL"] = 0
        MM_State["eyes"] = 1
        MM_State["mouth"] = 5
        MM_State["blush"] = 1
        Atlas_State["feelers"] = 0
        Atlas_State["eye"] = 2
        Atlas_State["eyeFrame"] = 5
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 6

        musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_laughb
    Madhouse "{bt=3}De renvoyer de si grand fans! Hah!{/bt}"

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 5
        MM_State["mouth"] = 1
        MM_State["blush"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 0
        Jamie_State["armR"] = 0
        Jamie_State["alFace"] = 1
        Atlas_State["eye"] = 3
        Robyn_State["mouth"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["brow"] = 2

    Madhouse "Sauf toi avec les cornes. Je gère pas les démons."

    $Jamie_State["mouth"] = 3
    $Jamie_State["eye"] = 7
    $Jamie_State["armR"] = 0
    $Jamie_State["alFace"] = 0


    Jamie "Mots gras pour un homme mort."

    python:
        MM_State["armR"] = 1
        MM_State["armL"] = 1
        MM_State["eyes"] = 5
        MM_State["mouth"] = 4
        Atlas_State["eye"] = 0


    Madhouse "... T'es un incendit ambulant."

    $Robyn_State["mouth"] = 7
    $Robyn_State["eyes"] = 4
    $Robyn_State["brow"] = 2

    Robyn "Désolé Jamie."

    python:
        Jamie_State["mouth"] = 0
        Jamie_State["eye"] = 1
        Jamie_State["armR"] = 1
        Jamie_State["brow"] = 0
        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 5
        Atlas_State["feelers"] = 1
        MM_State["mouth"] = 2
        MM_State["armR"] = 2
        MM_State["armL"] = 2
        MM_State["eyes"] = 0


    Jamie "Je comprends. Les ésprits faible on tendence à s'évanouir devant moi."

    python:
        Atlas_State["eye"] = 4
        Atlas_State["sparkle"] = 1
        Atlas_State["feelers"] = 0
        MM_State["mouth"] = 9
        MM_State["armR"] = 1
        Robyn_State["mouth"] = 0
        Robyn_State["eyes"] = 2
        Robyn_State["brow"] = 1

    show jamie:
        ease 0.4 matrixtransform RotateMatrix(0.0, 0, 0.0)
        ease 1.0 xcenter -0.3
    Narrator "Atlas se fait un check a lui même avant d'avancer."

    voice atlas_booyah
    Atlas "Cool! Je ah— ouais, c'est du business."

    python:
        Atlas_State["eye"] = 6
        Atlas_State["sparkle"] = 0
        Atlas_State["feelers"] = 1
        Atlas_State["armR"] = 1
        Atlas_State["armL"] = 2

    Atlas "Je suis quelqu'un qui est très serieux niveau Business!"

    Narrator "Vous vous avancez dans le studio."

    jump RadioShow
