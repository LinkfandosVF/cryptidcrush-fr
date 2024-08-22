init -3 python:
    PCname = "Robyn"
    PClastname = "Hart"
    PCthey = "they"
    PCthem = "them"
    PCtheir = "their"
    PCtheirs = "theirs"

    # if persistent.RobynCreated and False in persistent.unlockedDice[3:5]:
    #     persistent.unlockedDice[3] = True
    #     persistent.unlockedDice[4] = True

init offset = -1

# Set/Change Identity ----------------------------------------------------------
image BG Dream Zone Blur:
    contains:
        "BG atTheTableFright"
    contains:
        alpha 0.5
        zoom 1.05
        xcenter 0.5
        ycenter 0.5
        WaveImage("BG atTheTableFright", amp = 10, strip_height = 5,melt=True,freq=35)
        block:
            ease 5.0 alpha 0.2
            ease 5.0 alpha 0.5
            repeat
    contains:
        alpha 0.2
        zoom 1.05
        xcenter 0.5
        ycenter 0.5
        WaveImage("BG atTheTableFright", amp = 10,horizontal=False, strip_height = 5,melt=True,freq=35)
        block:
            ease 5.5 alpha 0.5
            ease 5.5 alpha 0.2
            repeat

label choose_identity:
    #scene BG Dream Zone
    python:
        musicNote = 0
        songText = "Reflet Astral"
        timeText = "Inconnu"
        timeSlot = 0

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
    voice atticus_hellocanyouhearme
    Atticus "{glitch=80}Hello?{/glitch} {glitch=40}Tu peux m'entendre?{/glitch}"
    $Atticus_State["eye"] = 0
    $Atticus_State["armR"] = 0

    show atticus:
        matrixcolor TintMatrix("#b6f0fc")
        xcenter 0.5
        blur 5

    with { "master" : Dissolve(0.5) }
    voice atticus_gladigotaholdofyou
    Atticus "{glitch=20}Ravis{/glitch} d'avoir pu te rattraper {glitch=10}à{/glitch} temps!"
    $Atticus_State["eye"] = 7

    show atticus:
        ease 2.0 blur 3
    voice atticus_fabricofreality
    Atticus "Tu n'est pas du tout prêt a rentrer dans ce {glitch=20}monde{/glitch}, et je préfererais ne pas voir un {glitch=35}humain{/glitch} se faire déchiqueter par les {glitch=10}fabriques de la réalitée.{/glitch}"
    python:
        Atticus_State["eye"] = 6
        displaymenu = True

    show atticus:
        ease 3.0 blur 0

    voice atticus_youcanspeakog
    Atticus "Tu {i}peux{/i} parler, n'est-ce pas?{nw}"

    menu:
        extend ""

        "Naturellement":
            $Atticus_State["eye"] = 0
            show atticus:
                blur 0
                ease 0.2 yoffset -20
                ease 0.2 yoffset 0
            Atticus "Parfait!"
            pass
        "Nope.":
            pass
            voice atticus_funnyone
            Atticus "Oh,., t'es un petit {i}rigolo{/i} a ce que je vois."
            $Atticus_State["eye"] = 6
    python:

        displaymenu = False
    voice atticus_whatsyournamefirst
    Atticus "Dans tout les cas, je me permet de demander—{nw}"

    $Atticus_State["eye"] = 7

    extend "\n\nComment t'appelles tu?"

    python:
        PCname = renpy.input("Prénom",length=10)
        persistent.RobynName[0] = PCname = PCname.strip()
    play sfx select3
    python:
        PClastname = renpy.input("Nom de famille",length=10)
        persistent.RobynName[1] = PClastname = PClastname.strip()
    play sfx select3

    # while "deez" in [PCname.lower(), PClastname.lower()]:
    #     Atticus "No. Try again."
    #
    #     python:
    #         PCname = renpy.input("First Name",length=10)
    #         PCname = PCname.strip()
    #     play sfx select3
    #     python:
    #         PClastname = renpy.input("Last Name",length=10)
    #         PClastname = PClastname.strip()
    #     play sfx select3

    python:
        if not PCname:
            persistent.RobynName[0] = PCname = "Robyn"
        if not PClastname:
            persistent.RobynName[1] = PClastname = "Hart"

        save_name = "[PCname] [PClastname]"




    Atticus "Très bien, [PCname] [PClastname]. Je vais garder ça en tête."
    voice atticus_whoami
    Atticus "C'est quoi ça? Qui suis-je?"
    $Atticus_State["armR"] = 1
    $Atticus_State["eye"] = 5
    show atticus at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1
    voice atticus_notthemothman
    Atticus "{bt=3}Définitivement pas le Mothman!~{/bt}"
    $Atticus = Character("{glitch=40}{color=#ED2A82}Mothman{/color}{/glitch}", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ED2A82")
    $displaymenu = True
    show atticus:
        yoffset 0

    $Atticus_State["eye"] = 7
    voice atticus_howwouldyouliketobeaddressed
    Atticus "Maintenant, quels sont tes pronoms?{nw}"

    menu:
        extend ""
        "Il/Lui":
            python:
                persistent.RobynPronouns = 0
                PCthey = "Il"
                PCthem = "Lui"
                PCtheir = "Son"
                PCtheirs = "Ses"
                PCThey = "Ils"
                PCThem = "Eux"
                PCTheir = "Leur"
                PCTheirs = "Eux"
        "Elle/Elle":
            python:
                persistent.RobynPronouns = 1
                PCthey = "Elle"
                PCthem = "Elle"
                PCtheir = "Sa"
                PCtheirs = "Ses"
                PCThey = "Elles"
                PCThem = "Elles"
                PCTheir = "Leur"
                PCTheirs = "Leurs"
        "Iel/Iel":
            python:
                persistent.RobynPronouns = 2
                PCthey = "Iel"
                PCthem = "Eux"
                PCtheir = "Ses"
                PCtheirs = "Ses"
                PCThey = "Iels"
                PCThem = "Iels"
                PCTheir = "Leur"
                PCTheirs = "Leurs"
    python:
        displaymenu = False
        Atticus_State["eye"] = 0
        Atticus_State["armR"] = 0

    menu:
        Atticus "Et la voix?"

        "Voice A":
            $robynvoice = persistent.pcvoice = 1
        "Voice B":
            $robynvoice = persistent.pcvoice = 2

    play voice2 RobynSays("Generic","Excited")
    voice atticus_goodchoice
    Atticus "Bon choix."

    voice atticus_diffchoice
    Atticus "Aussi pour la difficultée, qu'est-ce qui te conviendrais?{nw}"
    call diff_choice_menu from _call_diff_choice_menu_1


    $Atticus_State["eye"] = 2
    voice atticus_randomquestions
    Atticus "Quoi d'neuf avec les questions? Et bien—"
    $Atticus_State["eye"] = 6
    $displaymenu = True
    voice atticus_lackasenseofselfog
    Atticus "Ceux qui ne sont pas qui ils sont eux-mêmes ont tendance à se {glitch=100}se désintégrer{/glitch} dès leur entrée dans ce domaine de l'existence. Je suis juste là pour t'aider à rafraîchir ta mémoire.{nw}"

    menu:
        extend ""
        "Oh, ouais c'est pas une mauvaise idée!":
            $displaymenu = False
            call playerStatQuestions from _call_playerStatQuestions

        "Je crois savoir a peu près qui je suis. (Prédefini)":
            $displaymenu = False

            $Atticus_State["eye"] = 7

            $displaymenu = True
            voice atticus_whatkindofperson
            Atticus "Je vois,, quel genre de personne est-tu ?{nw}"


            menu:
                extend ""

                "Je suis plûtot sportif avec une grosse personalitée. (Attaque & Vitesse)":
                    #Mountain
                    python:
                        Robyn_State["hair"] = persistent.RobynSettings[0] = 1
                        Robyn_State["fPomf"] = persistent.RobynSettings[1] = 1
                        Robyn_State["fHair"] = persistent.RobynSettings[2] = 1
                        Robyn_State["glasses"] = persistent.RobynSettings[3] = 0
                        xNum = persistent.RobynSettings[4] = 0
                        Robyn_State["hairpin"] = persistent.RobynSettings[6] = 0
                        Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                        Robyn_State["necklace"] = (xNum == 2)
                        Robyn_State["beanie"] = persistent.RobynSettings[5] = 0
                        Robyn_State["shirt"] = persistent.RobynSettings[7] = 3
                        robCoat = persistent.RobynSettings[8] = 2
                        PCnameColor = PCnameColors[robCoat]
                        Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                        NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                        NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

                        persistent.RobynStats = pcBaseStats = [3,-1,2,0,1,-2,11]
                    #Brawn: +3
                    #Brains: -1
                    #Hustle: +2
                    #Guts: +0
                    #Charm: +1
                    #Occult: -2
                "Rat de biblio. (QI & Agilité)":
                    #UFO
                    python:
                        Robyn_State["hair"] = persistent.RobynSettings[0] = 0
                        Robyn_State["fPomf"] = persistent.RobynSettings[1] = 0
                        Robyn_State["fHair"] = persistent.RobynSettings[2] = 0
                        Robyn_State["glasses"] = persistent.RobynSettings[3] = 1
                        xNum = persistent.RobynSettings[4] = 0
                        Robyn_State["hairpin"] = persistent.RobynSettings[6] = 1
                        Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                        Robyn_State["necklace"] = (xNum == 2)
                        Robyn_State["beanie"] = persistent.RobynSettings[5] = 0
                        Robyn_State["shirt"] = persistent.RobynSettings[7] = 0
                        robCoat = persistent.RobynSettings[8] = 0
                        PCnameColor = PCnameColors[robCoat]
                        Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                        NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                        NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

                        persistent.RobynStats = pcBaseStats = [-1,3,2,-1,-1,1,11]
                    #Brawn: -1
                    #Brains: +3
                    #Hustle: +2
                    #Guts: -1
                    #Charm: -1
                    #Occult: +1
                "Monsieur tout le monde en gros. (Charme & Occult)":
                    #Madhouse
                    python:
                        Robyn_State["hair"] = persistent.RobynSettings[0] = 1
                        Robyn_State["fPomf"] = persistent.RobynSettings[1] = 0
                        Robyn_State["fHair"] = persistent.RobynSettings[2] = 0
                        Robyn_State["glasses"] = persistent.RobynSettings[3] = 0
                        xNum = persistent.RobynSettings[4] = 1
                        Robyn_State["hairpin"] = persistent.RobynSettings[6] = 0
                        Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                        Robyn_State["necklace"] = (xNum == 2)
                        Robyn_State["beanie"] = persistent.RobynSettings[5] = 1
                        Robyn_State["shirt"] = persistent.RobynSettings[7] = 1
                        robCoat = persistent.RobynSettings[8] = 3
                        PCnameColor = PCnameColors[robCoat]
                        Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                        NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                        NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

                        persistent.RobynStats = pcBaseStats = [-1,1,-2,0,3,2,11]
                    #Brawn: -1
                    #Brains: +1
                    #Hustle: -2
                    #Guts: +0
                    #Charm: +3
                    #Occult: +2
                "J'ai des gros bras et un cerveau formaté jusqu'a la racine! (Courage & Attaque)":
                    #Robbie
                    python:
                        Robyn_State["hair"] = persistent.RobynSettings[0] = 0
                        Robyn_State["fPomf"] = persistent.RobynSettings[1] = 1
                        Robyn_State["fHair"] = persistent.RobynSettings[2] = 1
                        Robyn_State["glasses"] = persistent.RobynSettings[3] = 1
                        xNum = persistent.RobynSettings[4] = 2
                        Robyn_State["hairpin"] = persistent.RobynSettings[6] = 0
                        Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                        Robyn_State["necklace"] = (xNum == 2)
                        Robyn_State["beanie"] = persistent.RobynSettings[5] = 1
                        Robyn_State["shirt"] = persistent.RobynSettings[7] = 2
                        robCoat = persistent.RobynSettings[8] = 1
                        PCnameColor = PCnameColors[robCoat]
                        Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                        NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                        NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

                        persistent.RobynStats = pcBaseStats = [2,-2,-1,3,0,1,11]
                    #Brawn: +2
                    #Brains: -2
                    #Hustle: -1
                    #Guts: +3
                    #Charm: +0
                    #Occult: +1

            python:
                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 2
            show robyn:
                matrixcolor TintMatrix("#b6f0fc")
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                xcenter 1.3
                ease 1.0 xcenter 0.7
            show atticus:
                ease 0.5 xcenter 0.3
            $displaymenu = False
            $Atticus_State["eye"] = 0
            voice atticus_sureofyourself
            Atticus "Très bien, tu a l'air plûtot sur de toi."

        "On s'en fout. (J'ai de la chance)":
            $displaymenu = False
            python:

                Robyn_State["hair"] = persistent.RobynSettings[0] = random.randint(0,1)
                Robyn_State["fPomf"] = persistent.RobynSettings[1] = random.randint(0,1)
                Robyn_State["fHair"] = persistent.RobynSettings[2] = random.randint(0,1)
                Robyn_State["glasses"] = persistent.RobynSettings[3] = random.randint(0,1)
                xNum = persistent.RobynSettings[4] = random.randint(0,2)
                Robyn_State["hairpin"] = persistent.RobynSettings[6] = 0
                Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                Robyn_State["necklace"] = (xNum == 2)
                Robyn_State["beanie"] = persistent.RobynSettings[5] = random.randint(0,1)
                Robyn_State["shirt"] = persistent.RobynSettings[7] = random.randint(0,3)
                robCoat = persistent.RobynSettings[8] = random.randint(0,3)
                PCnameColor = PCnameColors[robCoat]
                Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

                Robyn_State["mouth"] = 5
                Robyn_State["eyes"] = 2

                pcBaseStats = [3,2,1,0,-1,-2]
                random.shuffle(pcBaseStats)
                pcBaseStats.append(11)
                persistent.RobynStats = pcBaseStats


            show robyn:
                matrixcolor TintMatrix("#b6f0fc")
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                xcenter 1.3
                ease 1.0 xcenter 0.7
            show atticus:
                ease 0.75 xcenter 0.3

            $Atticus_State["eye"] = 7
            voice atticus_ifyousayso
            Atticus "Si tu le dit." #Note: You should probably have something that shows your stats

    $Atticus_State["eye"] = 0
    voice atticus_timeup
    Atticus "Je suis a court de temps on dirait,, bonne chance pour la suite.—{nw}"

    $Atticus_State["eye"] = 0
    extend "\n\nJe te supporte a 100 pourcent !"
    $PC_Stats.updateStats()
    stop music
    $persistent.firstGame = False
    $renpy.block_rollback()
    hide Overlay Dreamy
    $pBar1_Name = "{color=1AE65A}"+PCname
    $isPlaytesting = False
    return

label playerStatQuestions:
    $pcBaseStats = [0,0,0,0,0,0,11]

    $displaymenu = True

    $Atticus_State["eye"] = 7

    voice atticus_zoomthroughthesequestions
    Atticus "Bien,, essayons avec ces questions;.,.,\n\n{nw}"

    voice atticus_preferredbeverage
    extend "Donc dit moi en plus: Quel est ton genre de boisson ?{nw}"

    menu:
        extend ""

        "Eau gazeuse! C'est de l'eau mais qui se défend!" if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 2 #Brawn
        "H20, mais c'est pas ce qui fait de moi un nerd." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 2 #Brains
        "Une concoction de soda que je surnomme {i}Fizzy Killer{/i}~" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 2 #Hustle
        "Juste du thé herbalisé." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 2 #Guts
        "C'est moins au niveau de la boisson et plûtot la présentation." if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 2 #Charm
        "Je suis composé a 70 pourcent de café froid..." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 2 #Occult

            $Atticus_State["eye"] = 1

    voice atticus_greatestweakness
    Atticus "Un de tes défauts?.{nw}"
    menu:
        extend ""

        "J'ai des bras en spaghetti..." if pcBaseStats[0] == 0:
            $pcBaseStats[0] = -2 #Brawn
        "Je suis un peu con." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = -2 #Brains
        "Je bug quand je dois agir vite." if pcBaseStats[2] == 0:
            $pcBaseStats[2] = -2 #Hustle
        "J'ai mal au dos!" if pcBaseStats[3] == 0:
            $pcBaseStats[3] = -2 #Guts
        "Je croyait pas à la malchance." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = -2 #Occult
        "Un peu de tout?" if pcBaseStats[4] == 0:
            $pcBaseStats[4] = -2 #Charm

            $Atticus_State["eye"] = 6

    voice atticus_ignoringrightnow
    Atticus "Un truc que tu ignore la toute suite?{nw}"
    menu:
        extend ""

        "Mon sport." if pcBaseStats[0] == 0:
            $pcBaseStats[0] = -1 #Brawn
        "Hein quoi? Pardon j'était dans la lune." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = -1 #Brains
        "Je n'ai rien en tête, vraiment.." if pcBaseStats[2] == 0:
            $pcBaseStats[2] = -1 #Hustle
        "Juste a quel point j'ai faim." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = -1 #Guts
        "Du coup c'est qui le moth-boy?" if pcBaseStats[4] == 0:
            $pcBaseStats[4] = -1 #Charm
        "Prendre les précautions néccésaire pour empêcher que mon doppleganger ne me remplace en pleine nuit." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = -1 #Occult

            $Atticus_State["eye"] = 0

    voice atticus_strongestquality
    Atticus "Et t'a plus grande qualité?{nw}"
    menu:
        extend ""

        "Je garde une routine stricte et organisée!" if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 3 #Brawn
        "J'ai jamais peur de demander quoi que ce soit." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 3 #Brains
        "Je travaille vite et me focalise sur ma tâche!" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 3 #Hustle
        "J'éssaie de me pardonner moi même." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 3 #Guts
        "J'admet quand j'ai tort. " if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 3 #Charm
        "J'éxiste. C'est déja pas mal non?" if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 3 #Occult

            $Atticus_State["eye"] = 7

    voice atticus_entiredaytoyourself
    Atticus "Si tu avait une journée de libre, t'en ferais quoi?{nw}"
    menu:
        extend ""

        "Randonnée avec un pote et un sac." if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 1 #Brawn
        "M'organiser. C'est dur le travail!" if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 1 #Brains
        "Me ballader en ville!" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 1 #Hustle
        "Je ferais du pain. BEAUCOUP de pain." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 1 #Guts
        "Recharger mes batteries sociales en jouant a un jeu vidéo en solo." if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 1 #Charm
        "Le temps c'est pas vraiment une monnaie alors je le dépense pas." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 1 #Occult

            $Atticus_State["eye"] = 1

    $persistent.RobynStats = pcBaseStats
    $PC_Stats.name = "{color=1AE65A}"+PCname+"{/color}"
    $PC_Stats.ChangeStats(hp=pcBaseStats[6],brawn=pcBaseStats[0],brains=pcBaseStats[1],hustle=pcBaseStats[2],guts=pcBaseStats[3],charm=pcBaseStats[4],occult=pcBaseStats[5])

    voice atticus_ifyouwereacryptid
    Atticus "Si tu était un Cryptide, tu serait quoi?{nw}"
    menu:
        extend ""

        "Lochness.":
            $Robyn_State["shirt"] = 2 #Robbie
        "Alien de l'espace!!":
            $Robyn_State["shirt"] = 0 #UFO
        "Loup-garou s'il vous plaît.":
            $Robyn_State["shirt"] = 3 #Mountain
        "Peut être un fantôme un jour.":
            $Robyn_State["shirt"] = 1 #Madhouse
        "J'sais pas! N'importe le quel, vraiment.":
            $Robyn_State["shirt"] = random.randint(0,3) #Random

    python:
        Robyn_State["mouth"] = 5
        Robyn_State["eyes"] = 2

    show robyn:
        matrixcolor TintMatrix("#b6f0fc")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 1.3
        ease 1.0 xcenter 0.85
    show atticus:
        ease 0.5 xcenter 0.2

    $Atticus_State["eye"] = 0

    voice atticus_howdoyouenvision
    Atticus "Cool, cool... Um maintenant comment tu te voit?{nw}"
    $xNum = 0
    call id_Loop from _call_id_Loop
    python:
        persistent.RobynSettings[0] = Robyn_State["hair"]
        persistent.RobynSettings[1] = Robyn_State["fPomf"]
        persistent.RobynSettings[2] = Robyn_State["fHair"]
        persistent.RobynSettings[3] = Robyn_State["glasses"]
        persistent.RobynSettings[4] = xNum
        persistent.RobynSettings[6] = Robyn_State["hairpin"]
        Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
        Robyn_State["necklace"] = (xNum == 2)
        persistent.RobynSettings[5] = Robyn_State["beanie"]
        persistent.RobynSettings[7] = Robyn_State["shirt"]
        persistent.RobynSettings[8] = robCoat
    $displaymenu = False

    return

label id_Loop:
    menu:
        extend ""

        "Cheveux":
            python:
                if not Robyn_State["hair"]:
                    Robyn_State["hair"] = 1
                else:
                    Robyn_State["hair"] = 0
            jump id_Loop
        "Touffe de cheveux":
            $Robyn_State["fPomf"] = not Robyn_State["fPomf"]
            jump id_Loop
        "Pilosité":
            $Robyn_State["fHair"] = not Robyn_State["fHair"]
            jump id_Loop
        "Lunettes":
            $Robyn_State["glasses"] = not Robyn_State["glasses"]
            jump id_Loop

        "Veste":
            $robCoat = persistent.RobynSettings[8] = loopInt(robCoat+1,8)
            $PCnameColor = PCnameColors[persistent.RobynSettings[8]]
            jump id_Loop

        "Plus":
            jump id_Loop2
        "C'est fini.":
            python:
                persistent.RobynSettings[0] = Robyn_State["hair"]
                persistent.RobynSettings[1] = Robyn_State["fPomf"]
                persistent.RobynSettings[2] = Robyn_State["fHair"]
                persistent.RobynSettings[3] = Robyn_State["glasses"]
                persistent.RobynSettings[4] = xNum
                persistent.RobynSettings[6] = Robyn_State["hairpin"]
                Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                Robyn_State["necklace"] = (xNum == 2)
                persistent.RobynSettings[5] = Robyn_State["beanie"]
                persistent.RobynSettings[7] = Robyn_State["shirt"]
                persistent.RobynSettings[8] = robCoat
                PCnameColor = PCnameColors[robCoat]
                Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

    return

label id_Loop2:
    menu:
        extend ""
        "Barette" if not Robyn_State["beanie"]:
            $Robyn_State["hairpin"] = not Robyn_State["hairpin"]
            jump id_Loop2

        "Bonnet" if not Robyn_State["hairpin"]:
            $Robyn_State["beanie"] = not Robyn_State["beanie"]
            jump id_Loop2

        "Mettre Eyeliner/Colier/Choker":
            python:
                xNum+=1
                if xNum > 2:
                    xNum = 0
                Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                Robyn_State["necklace"] = (xNum == 2)
            jump id_Loop2

        "Attend...":
            jump id_Loop
        "C'est fini.":
            python:
                persistent.RobynSettings[0] = Robyn_State["hair"]
                persistent.RobynSettings[1] = Robyn_State["fPomf"]
                persistent.RobynSettings[2] = Robyn_State["fHair"]
                persistent.RobynSettings[3] = Robyn_State["glasses"]
                persistent.RobynSettings[4] = xNum
                persistent.RobynSettings[6] = Robyn_State["hairpin"]
                Robyn_State["eyeliner"] = Robyn_State["choker"] = (xNum == 1)
                Robyn_State["necklace"] = (xNum == 2)
                persistent.RobynSettings[5] = Robyn_State["beanie"]
                persistent.RobynSettings[7] = Robyn_State["shirt"]
                persistent.RobynSettings[8] = robCoat
                PCnameColor = PCnameColors[robCoat]
                Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)
                NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
                NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)

    return
    #xNum = random.randint(0,2)
    #robCoat = random.randint(0,3)

label redo_identity:
    python:
        Atticus = Character("{glitch=40}{color=#ED2A82}Mothman{/color}{/glitch}", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ED2A82")
        musicNote = 0
        songText = "Astral Reflection"
        timeText = "Unknown"
        timeSlot = 0

    scene BG Dream Zone Blur:
        xzoom -1
        matrixcolor HueMatrix(0)
        ease 6.0 matrixcolor HueMatrix(90)
        ease 10.0 matrixcolor HueMatrix(-60)
        block:
            ease 10.0 matrixcolor HueMatrix(90)
            ease 10.0 matrixcolor HueMatrix(-60)
            repeat

    with Dissolve(0.7)
    play music astral_dissociation_song fadein 3.0

    $adjustChar("Atticus",eye=7,armR=0)

    show atticus:
        matrixcolor TintMatrix("#b6f0fc")
        xcenter 0.5

    with { "master" : Dissolve(0.5) }

    voice renpy.random.choice([audio.atticus_restingmyeyesa,audio.atticus_restingmyeyesb])
    Atticus "Hrmgh, Je... reposais juste mes yeux."
    show atticus at startledSquish: #.Startled Squish
        matrixtransform rotated()
        zoom 1
        alpha 1


    $displaymenu = True
    $adjustChar("Atticus",eye=6)
    voice atticus_youseemlost
    Atticus "Tu m'a l'air un peu paumé, je peux t'aider pour quoi que se soit?{nw}"
    jump redo_identity_loop

label stats_redo_questions:
    python:
        pcBaseStats = [0,0,0,0,0,0,11]
        displaymenu = True

        adjustChar("Atticus",eye=6)

    voice atticus_zoomthroughthesequestions
    Atticus "Bon alors voyons voir;.,\n\n{nw}"

    voice atticus_preferredbeverage
    extend "Quel genre de boisson préfère tu?{nw}"
    menu:
        extend ""

        "Eau gazeuse! C'est de l'eau mais qui se défend!" if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 2 #Brawn
        "H20, mais c'est pas ce qui fait de moi un nerd." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 2 #Brains
        "Une concoction de soda que je surnomme {i}Fizzy Killer{/i}~" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 2 #Hustle
        "Juste du thé herbalisé." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 2 #Guts
        "C'est moins au niveau de la boisson et plûtot la présentation." if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 2 #Charm
        "Je suis composé a 70 pourcent de café froid..." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 2 #Occult
    $Atticus_State["eye"] = 1

    voice atticus_greatestweakness
    Atticus "Dit moi un de tes plus gros point faibles?{nw}"
    menu:
        extend ""

        "J'ai des bras en spaghetti..." if pcBaseStats[0] == 0:
            $pcBaseStats[0] = -2 #Brawn
        "Je suis un peu con." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = -2 #Brains
        "Je bug quand je dois agir vite." if pcBaseStats[2] == 0:
            $pcBaseStats[2] = -2 #Hustle
        "J'ai mal au dos!" if pcBaseStats[3] == 0:
            $pcBaseStats[3] = -2 #Guts
        "Je croyait pas à la malchance." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = -2 #Occult
        "Un peu de tout?" if pcBaseStats[4] == 0:
            $pcBaseStats[4] = -2 #Charm

    $Atticus_State["eye"] = 6
    voice atticus_ignoringrightnow
    Atticus "Un truc que t'ignore là toute suite?{nw}"
    menu:
        extend ""

        "Mon sport." if pcBaseStats[0] == 0:
            $pcBaseStats[0] = -1 #Brawn
        "Hein quoi? Pardon j'était dans la lune." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = -1 #Brains
        "Je n'ai rien en tête, vraiment.." if pcBaseStats[2] == 0:
            $pcBaseStats[2] = -1 #Hustle
        "Juste a quel point j'ai faim." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = -1 #Guts
        "Du coup c'est qui le moth-boy?" if pcBaseStats[4] == 0:
            $pcBaseStats[4] = -1 #Charm
        "Prendre les précautions nécéssaire pour empêcher que mon doppleganger ne me remplace cette nuit." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = -1 #Occult

    $Atticus_State["eye"] = 7
    voice atticus_strongestquality
    Atticus "Et ce que tu considère être un point fort?{nw}"
    menu:
        extend ""

        "Je garde une routine stricte et organisée!" if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 3 #Brawn
        "J'ai jamais peur de demander quoi que ce soit." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 3 #Brains
        "Je travaille vite et me focalise sur ma tâche!" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 3 #Hustle
        "J'éssaie de me pardonner moi même." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 3 #Guts
        "J'admet quand j'ai tort. " if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 3 #Charm
        "J'éxiste. C'est déja pas mal non?" if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 3 #Occult

    voice atticus_entiredaytoyourself
    Atticus "Si tu avait un jour entier libre?{nw}"
    menu:
        extend ""

        "Randonnée avec un pote et un sac!" if pcBaseStats[0] == 0:
            $pcBaseStats[0] = 1 #Brawn
        "Je dois vérifier mon emplois tu temps, le travaille c'est dur." if pcBaseStats[1] == 0:
            $pcBaseStats[1] = 1 #Brains
        "Me ballader en ville!" if pcBaseStats[2] == 0:
            $pcBaseStats[2] = 1 #Hustle
        "Je ferais du pain. BEAUCOUP DE PAIN." if pcBaseStats[3] == 0:
            $pcBaseStats[3] = 1 #Guts
        "Recharger mes batteries sociale en jouant à un jeu en solo." if pcBaseStats[4] == 0:
            $pcBaseStats[4] = 1 #Charm
        "Je vois pas le temps comme de l'argent donc je ne le dépense pas." if pcBaseStats[5] == 0:
            $pcBaseStats[5] = 1 #Occult

    $Atticus_State["eye"] = 1

    $persistent.RobynStats = pcBaseStats
    $PC_Stats.name = "{color=1AE65A}"+PCname+"{/color}"
    $PC_Stats.ChangeStats(hp=pcBaseStats[6],brawn=pcBaseStats[0],brains=pcBaseStats[1],hustle=pcBaseStats[2],guts=pcBaseStats[3],charm=pcBaseStats[4],occult=pcBaseStats[5])
    $Atticus_State["eye"] = 2

    voice atticus_ifyouwereacryptid
    Atticus "Et si tu était un cryptide?{nw}"
    menu:
        extend ""

        "Lochness!":
            $persistent.RobynSettings[7] = Robyn_State["shirt"] = 2 #Robbie
        "Alien!":
            $persistent.RobynSettings[7] = Robyn_State["shirt"] = 0 #UFO
        "Loup-Garou":
            $persistent.RobynSettings[7] = Robyn_State["shirt"] = 3 #Mountain
        "Fantôme!":
            $persistent.RobynSettings[7] = Robyn_State["shirt"] = 1 #Madhouse
        "On s'en fout!":
            $persistent.RobynSettings[7] = Robyn_State["shirt"] = random.randint(0,3) #Random

    $Atticus_State["eye"] = 0
    Atticus "Problème réglé! Voilà c'était pas trop dur, hein? \n\n{size=-5}{i}Ne le refaisons pas.{/i}{/size}"

    return
