label Ch1_CafeIntro:
    scene BG Cafe:
        matrixcolor ColorizeMatrix("#1c1c1c","#93ccea")

    camera:
        camera_zoom(z=-280,x=-190)

    python:
        musicPlayer.playSong(fadeOut=1)

        timeText = "2:00PM"

        adjustChar("Robyn",eye=4,brow=2,mouth=3,armR=0)
        adjustChar("Robbie",armR=1,eye=2)

    show robyn neutral:
        xcenter -0.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.0 xcenter 0.2

    show robbie behind robyn:
        xcenter 0.5

    show jamie cafe:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.8

    with Dissolve(1.0)
    python:
        musicPlayer.playSong(song="stygian_scuffle_song",fadeIn=2,fadeOut=1)
        songText = "(REDACTED)"

    Narrator "En entrant dans le café, tu est immédiatement acceuilli par un air de café en poudre et de musique chorale funky qui ne se tient pas du tout à l'athmosphère."

    Narrator "Non pas que tu sois là pour juger, tout le monde à des goûts musicaux étranges. \n\n Tu est juste ici pour une chaise et un truc à manger."

    show robyn happy:
        xcenter 0.2
    $Robbie_State["eye"] = 3
    Robyn "Tu fait la queue?"

    $Robbie_State["eye"] = 1
    Narrator "Debout devant le contoir se tient un cryptide penché devant un petit goblet, habillé de multiples couches de vêtements et un chapeau poilu pour accompagner."

    Narrator "La musique change soudainement vers une playlist enjouée, altèrant complètement l'ambiance."

    $musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=1,fadeOut=1)

    python:
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "6A", who_color = "ea3c53")
        adjustChar("Robbie",eye=0,mouth=1)

    show robbie:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    voice robbie_hopingtochangeorder
    Someone "J'aurais espéré pouvoir changer ma commande."
    voice robbie_longhopescoffee
    $adjustChar("Robbie",eye=7,mouth=3)

    Someone "Mais,, je crois que le café de Longhope., il est juste., {b}mauvais.{/b} Regarde ce truc. C'est juste de l'eau marron."

    python:
        musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=1,fadeOut=1)
        adjustChar("Robyn",eyes=2,brow=1,mouth=3)

        Jamie_State["eye"] = 2
        Robbie_State["eye"] = 0

    camera:
        camera_zoom(x=100,y=-30,z=-150,t=2)

    show robyn:
        xcenter 0.2
        ease 2.0 xcenter 0.5

    show robbie:
        flipCharDelayed(0.8,0.5)
        xcenter 0.5
        ease 3.0 xcenter -0.5

    show jamie cafe:
        unflipCharDelayed(0.8,0.5)

    Narrator "Tu t'écartes alors que le cryptide quitte le magasin."
    camera:
        camera_zoom(x=100,y=-30,z=-150)

    hide robbie

    show robyn default:
        xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)

    voice jamie_abyssalcoldbrewishalfoff
    Jamie "Bienvenue! Qu'est-ce que vous voulez commander? Les infusions abyssales froides sont à moité prix."

    $adjustChar("Robyn",eyes=0,mouth=4)
    Robyn "Jamie?"

    show jamie at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1

    $adjustChar("Jamie",alFace=0,eye=4,sweat=0,blush=1)
    Narrator "L'immense démon se bloque sur place et son visage se mettent à briller d'un lèger bleu clair."

    voice jamie_lookaway
    Jamie "Non,., s'il te plait,., ne me regarde pas-..."

    Robyn "Oh—"

    $adjustChar("Jamie",mouth=1,eye=6,blush=0,wispEyes=3)
    voice jamie_begonehuman
    Jamie "{sc=2}Vas-t'en humain!{/sc}"

    $adjustChar("Jamie",eye=7,mouth=2)
    Jamie "Ne pose pas les yeux sur cette forme affaiblie."

    python:
        adjustChar("Robyn",eyes=2,mouth=2)
        Jamie_State["blush"] = 0

    Robyn "Tu veux dire., ton uniforme de travail?"

    python:
        adjustChar("Jamie",eye=1,mouth=0,wispEyes=4)
        Robyn_State["mouth"] = 5

    Jamie "Précisément,, mais je suis vraiment un rat sous cette forme."

    Robyn "Hey, si c'est trop génant, je peux revenir quand c'est ta pause."

    $Jamie_State["eye"] = 4

    Jamie "Non, je dois rester fort."

    python:
        adjustChar("Jamie",eye=3,blush=0,wispEyes=0)
        adjustChar("Robyn",eyes=3,mouth=0,brow=2)

    Robyn "Je vais prendre un chai et un croissant."

    show robyn:
        matrixtransform RotateMatrix(0,0,0)

    $adjustChar("Jamie",mouth=1,eye=6,wispEyes=1)
    Jamie "Tu économiserait 2 dollars si tu prenait une infusion."

    Robyn "Okau, si tu le recommande!"

    python:
        adjustChar("Robyn",eyes=0,mouth=3)
        adjustChar("Jamie",eye=1,wispEyes=1,mouth=2)

    Jamie "Non, c'est plûtot mauvais."

    $adjustChar("Robyn",eyes=3,mouth=0,brow=0)
    Robyn "Et du thé vert glacé?"

    $adjustChar("Jamie",mouth=0,eye=2)
    Jamie "Super choix."

    python:
        adjustChar("Jamie",eye=2,mouth=0)
        Robyn_State["eyes"] = 2

    show robyn:
        ease 0.75 xcenter 0.6
        pause 0.5
        ease 0.75 xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.75 matrixtransform RotateMatrix(0,0,-10) yoffset 40
        pause 0.5
        ease 0.75 matrixtransform RotateMatrix(0,0,0) yoffset 0

    Narrator "Tu prends ton croissant et ton thé, impatient d'en prendre une gorgé. Avec beaucoup d'anticipation, tu le porte à tes lèvres- "

    $adjustChar("Robyn",mouth=4,brow=3,eyes=3)

    show robyn:
        xcenter 0.5

    show jamie:
        matrixtransform RotateMatrix(0,0,0)
        yoffset 0

    extend "\net merde! C'est immonde! Ça à le goût d'un aspirateur fermenté avec des tentacules de l'éspace."

    $adjustChar("Robyn",mouth=4,brow=1,eyes=0)
    Robyn "C'est... pas ce que j'ai commandé-"

    Jamie "Je pensais que tu voulais un thé vert abyssal?"

    Robyn "N-non. Je- {sc=3}{i}Attends.{/i}{/sc} Abyssal?"

    python:
        adjustChar("Jamie",eye=0,brow=3,mouth=4)
        Robyn_State["mouth"] = 5

    Jamie "C'est de là que on prends nos ingrédients."

    python:
        adjustChar("Robyn",eyes=1,mouth=3,brow=2)
        Jamie_State["mouth"] = 0

    Robyn "Bleugh."

    $adjustChar("Jamie",wispEyes=0,eye=2)
    Jamie "Et si je fesais quelque chose qui n'est pas sur la carte? {i}En dehors du menu{/i}? {nw}"

    $adjustChar("Jamie",wispEyes=1,eye=1,brow=0)
    extend "\n\n J'insiste."

    $Robyn_State["eyes"] = 2
    Robyn "Okay,, juste,, ne t'attire pas de problèmes."

    python:
        adjustChar("Robyn",eyes=1,mouth=5)
        adjustChar("Jamie",eye=1,wispEyes=0,brow=0)


    Jamie "Ça fait parti du fun."
    show jamie cafe:
        xcenter 0.8
        ease 2.0 xcenter 1.3

    Narrator "Tu mets ta boisson de coté alors que Jamie retourne derrière le contoir."

    camera:
        camera_zoom(z=-500,x=-30,t=0.4)
    hide jamie

    $BM_State['face'] = 1

    show blobhouse:
        zoom 0
        matrixtransform RotateMatrix(0,0,5)
        xcenter 0.4
        parallel:
            ease 0.6 xcenter 0.39
        parallel:
            ease 0.2 zoom 1.0
        parallel:
            ease 0.3 yoffset -200
            ease 0.3 yoffset 0
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0,180,360*2)

        idleFloat(2,10)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.45 matrixtransform RotateMatrix(0,180,0)

    $musicPlayer.playSong(song="not_so_spooky_song")

    voice mm_laughd
    Madhouse "{sc=3}{b}DES BATTERIES DE VOITURES!{/b}{/sc}"

    $adjustChar("Robyn",eyes=0,brow=1,mouth=4)
    Robyn "Pardon?"

    python:
        adjustChar("Robyn",eyes=2,mouth=5)
        BM_State['face'] = 2

    voice mm_laughawkward
    Madhouse "Si tu prennait des câbles et les branches sur moi et une batterie de voiture,, ca serait juste le coup de {b}jus{/b} dont j'ai besoin pour récupérer mes pouvoirs!"

    $adjustChar("Robyn",eyes=1,mouth=4,brow=2)
    Robyn "T'essaie de me tuer?"

    $BM_State['face'] = 4
    Madhouse "Non? Pourquoi je ferais ça?"

    python:
        adjustChar("Robyn",eyes=4,mouth=5,brow=3)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.45 matrixtransform RotateMatrix(0,0,0)

    Robyn "Qui sais."

    $BM_State['face'] = 14
    voice mm_dismissive

    Madhouse "Alleeeeez, jamais je te blesserais!"

    python:
        adjustChar("Robyn",eyes=2,mouth=4)
        BM_State['face'] = 4

    Robyn "Va dire ça à ton {i}unique fanboy.{/i}"

    python:
        BM_State['face'] = 5
        adjustChar("Robyn",mouth=5,eyes=1)

    show blobhouse at startledSquish:
        idleFloat(2,10)

    Madhouse "{sc=2}{b}Ye-{/b}{/sc}{sc=4}{b}OWCH!{/b}{/sc} \n\nPutain, t'es brûtal. J'étais juste honnète tu sais."

    show robyn:
        matrixtransform RotateMatrix(0,0,0) 
        ease 0.45 matrixtransform RotateMatrix(0,180,0)

    Robyn "Je veux pas que tu pense être permis de tout ici, {color=#3bec27}Slimeball.{/color}"

    $BM_State['face'] = 2

    show blobhouse at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        idleFloat(2,10)

    voice mm_yohoholaugh
    Madhouse "Et un surnom mignon? \n\nEst-ce que ca veut dire que je dois t'appeller., {sc=2}{b}{color=#EC2A2A}Meatball{/color}{/b}{/sc}?"

    $adjustChar("Robyn",eyes=2,mouth=4,brow=2)
    Robyn "Non, serieux, t'as beaucoup de travail à faire."

    python:
        BM_State['face'] = 4
        Robyn_State["mouth"] = 5

    Madhouse "Qu—{nw}"

    $BM_State['face'] = 13

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2,10)

    extend "\n\nOn s'en fout."

    python:
        adjustChar("Robyn",eyes=1,mouth=5,brow=1)
        musicPlayer.playSong(song="cryptidcrush_cafe2",fadeIn=0.2,fadeOut=0.2)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.45 matrixtransform RotateMatrix(0,0,0)

    show blobhouse:
        ease 0.3 xzoom 0 yoffset -100 alpha 0 blur 30

    Narrator "Wow, sans déconner, c'est quoi son problème? On dirait qu'il cherche constament les conflits."
    scene BG Black
    camera:
        camera_zoom()
    show CG WIP Cafe Jamie

    with BGDissolve(name="Trans_BM.png")

    Narrator "De retour dans la cuisine, le démon se met à concocter un truc vraiment étrange..."
    python:
        displaymenu = True
        drinkChoice = 0
        drinkDifficulty = 7

    Narrator "Iel cherche dans son coeur et la recette parfaite vient à l'ésprit-{nw}"

    menu:
        extend ""

        "Boisson de Dagon Primordiale":
            python:
                displaymenu = False
                drinkChoice = 1
                drinkDifficulty = 8
        "Tincture des véritiés divines":
            python:
                displaymenu = False
                drinkChoice = 2
                drinkDifficulty = 10
        "Thé prismatique des inductions inconnues":
            python:
                displaymenu = False
                drinkChoice = 3
                drinkDifficulty = 12

    call dice_roll(rMod=Jamie_Stats.cStats("occult"), rDiff= drinkDifficulty, rDesc="Drinkomancy") from _call_dice_roll_12

    jump Ch1_CafeResult

label Ch1_CafeResult:

    $dNoun = ["sucrée","serrée","indescriptible"][drinkChoice-1]

    Narrator "Avec une idée en place iel se met au travail. Ses mains bougent avec adresse et se composent à la concoction de la boisson [dNoun] , en faisant attention à la faire aux goûts du mortel."
    python:
        adjustChar("Jamie",eye=2,mouth=2,wispEyes=3,brow=3)
        adjustChar("Robyn",eyes=2,brow=1,mouth=0)

    scene BG Cafe

    camera:
        camera_zoom(x=100,y=-30,z=-150)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.5

    show jamie cafe:
        xcenter 1.1
        matrixtransform RotateMatrix(0,0,0)
        easein 1.2 xcenter 0.8

    with Pixellate(0.75,7)

    Jamie "Voilà."

    if not isRollSuccess:
        python:
            adjustChar("Jamie",eye=1,mouth=2,sweat=1)
            adjustChar("Robyn",brow=2)
        Narrator "Jamie fait glisser la boisson sur la table, mais pas sans louper de la faire tomber avant."
    else:
        Narrator "Jamie dépose la boisson sur la table."

    Jamie "J'éspère que t'aimeras."

    show CGShade
    show CG Cafe Drink

    if drinkChoice == 1:
        Narrator "It’s a murky drink, that with the bluish twinge make it feel like the inky abyss of the ocean had been washed out by coffee beans."
    elif drinkChoice == 2:
        Narrator "It’s a bright peach-ish beverage, that would look tasty, but the fact that it’s slightly glowing a divine radiance is mildly unsettling."
    elif drinkChoice == 3:
        Narrator "The drink looks more like a cosmic sludge that feels a bit too alive and bouncy. It refracts various bright colors as light glints off the surface, it doesn’t feel like a drink that should exist, let alone be consumed by people."

    $adjustChar("Robyn",brow=2)
    Narrator "You look up at Jamie, who stares back at you expectantly. \n\nSurely, if they're confident in it, you should be too!"

    hide CGShade

    hide CG Cafe Drink

    show SmallCafeDrink:
        yoffset 700
        xcenter 0.6
        ease 1.0 yoffset 20

    with nwDissolve(0.5)


    Narrator "…"

    if isRollSuccess:

        if drinkChoice == 1:
            $adjustChar("Robyn",eyes=0,mouth=4,brow=1)
            Narrator "It’s a little salty, but that just makes it all the sweeter when it combines with the bitter iced coffee base. There's a slight hint of caramel."

            $adjustChar("Robyn",mouth=6)
            Robyn "Delicious!"
        elif drinkChoice == 2:
            $adjustChar("Robyn",eyes=0,mouth=4,brow=1)
            Narrator "It’s rich. Almost like a hot cider, with apple and lemon. It fills you with a mellow warmth like any good tea should."

            $adjustChar("Robyn",mouth=6)
            Robyn "Yum!"
        elif drinkChoice == 3:
            $adjustChar("Robyn",eyes=0,mouth=3)
            Narrator "What flavor is this? It's sweet? No, it's savory? Each sip brings out a different flavor. It's overwhelming yet enlightening."

            $adjustChar("Robyn",mouth=6)
            Robyn "I have no idea what I'm drinking, but I think I like it?"

            $adjustChar("Jamie",eye=1,sweat=1)
            Jamie "I'm glad it didn't melt your brain."


    else:
        camera at camera_shake_off(x=100)
        python:
            adjustChar("Jamie",eye=4,mouth=1)
            adjustChar("Robyn",eyes=0,mouth=3)

        Jamie "{b}{sc=3}WAIT!{/sc}{/b}"

        $adjustChar("Robyn",mouth=4)
        show jamie cafe:
            matrixtransform rotated() xoffset 0 yoffset 0
            ease 0.3 matrixtransform rotated(z=-30) xoffset -160 yoffset 30
            ease 0.25 matrixtransform rotated(z=10) xoffset 20 yoffset 0
            ease 0.175 matrixtransform rotated() xoffset 0

        show SmallCafeDrink:
            xcenter 0.6
            pause 0.35
            matrixtransform rotated()
            parallel:
                easein 0.6 xcenter 1.3 matrixtransform rotated(z=360*3)
            parallel:
                easein 0.3 yoffset -300
                ease 0.3 yoffset 0


        Narrator "Jamie lunges, swatting your hand away before snatching up the cup of tea,, a wild look in their eyesockets."

        $adjustChar("Jamie",mouth=2)
        Jamie "I screwed something up! I can {b}feel it.{b} \n\nYou can't drink this."

        Robyn "It can't be that bad!"

        $adjustChar("Jamie",eye=1,mouth=0)
        Jamie "You're getting a tropical mix juice box instead."

        Robyn "{sc=3}H-huh?{/sc}"

        Jamie "Here's an apologetic grilled veggie panini on the side."

        $adjustChar("Robyn",eyes=1,mouth=5)
        Robyn "Okay fine."
        scene BG Black
        with nwDissolve(0.5)

        Narrator "Temporarily pacified by the delicious sandwich and the not so fancy juice box,, you take a deep breath, stretch and collect your thoughts."


    scene BG Black
    camera at camera_default:
        camera_zoom()

    with nwDissolve(0.5)

    python:
        PC_Stats.updateStats()
        bookNames = {
            "brawn": kwBrawn,
            "brains": kwBrains,
            "hustle": kwHustle,
            "guts": kwGuts,
            "charm": kwCharm,
            "occult": kwOccult }

        xBooks = []
        for x in ["brawn","brains","hustle","guts","charm","occult"]:
            if PC_Stats.cStats(x) > 0:
                xBooks.append(bookNames[x])

        xBookA = xBooks[0]
        xBookB = xBooks[1]
        xBookC = xBooks[2]



    Narrator "You give Jamie your thanks and leave the cafe. You head outside and find the perfect bench to rest upon."

    Narrator "With sustenance in hand, you decide to crack open the trove of pamphlets you were given. Each of them seem to be about... self-defense?"

    Narrator "Kind of strange that the Goatma'am's first thought would be on how to use your [xBookA], [xBookB], and [xBookC] to kick ass, but to each their own."

    Narrator "Maybe you could use these if anything like that Madhouse debacle happens again."

    Narrator "You could take a nap right about now. Maybe ghosts do leech on life force. \n\nIt'd explain why those {i}two{/i} are so clingy."

    Narrator "Leaning back, you fold your arms and bow your head, letting your eyes flutter closed. \n\nIt's nice feeling needed,, even if it's for cat food."

    show CG Taro wip
    camera at camera_shake

    Taro "{sc=3}{b}THERE YOU ARE!{/b}{/sc}"

    Narrator "Speak of the devil herself."

    Robyn "Taro!"

    Taro "You left me to {b}ROT{/b}! That googly eyed goat wouldn't stop asking me questions!"

    Taro "{bt=3}Oooh a three eyed cat?\n\nI've never heard of a {b}guardian nyangel{/b}! \n\nMay I hold your little paws?{/bt}"

    Taro "Not with those creepy mage hands!"

    Robyn "Aw nooo,, I'm sorry for wandering off without you Taro. I figured you wanted to go off and do your own thing."

    Taro "Typically yes,, but on my own terms."

    Taro "Now carry me."

    hide CG Taro wip
    with nwDissolve(0.5)

    #Narrator "After waving goodbye to Jamie,, you head outside and continue on your trek, exploring the town."

    Narrator "You scoop up Taro and give Atlas a call. He's always been your go-to guy for., anything really."

    jump Ch1_RobbieIntro
