init python:
    def seenLabel(xlabel=""):
        return gameVersion == 3 or renpy.seen_label(xlabel)

label redo_identity_loop:
    menu:
        extend ""
        "Montre moi la {b}séléction de chapitre{/b}":
            jump chapter_select_label

        "Les combats!":
            jump battle_select_label

        "Je veux changer deux trois truc niveau gameplay.":
            voice atticus_mixingthingsup
            menu:
                extend ""
                "Changer le dé.":
                    voice atticus_dicechoice
                    Atticus "Très bien, on prend lequel?{nw}"
                    $displaymenu = True

                    call dice_choice_menu from _call_dice_choice_menu

                    python:
                        displaymenu = True
                        diceBot.setDieType(persistent.dieSettings)
                        pc_karma = diceBot.maxKarma
                    voice atticus_chuckle
                    Atticus "On essaie?{nw}"
                    menu:
                        extend ""

                        "Ouais!":
                            call dice_roll(rMod=0, rDiff=7, rDesc="Test Roll") from _call_dice_roll_1
                            $pc_karma = diceBot.maxKarma
                        "Non merci.":
                            pass


                    $Atticus_State["eye"] = 6
                    $displaymenu = True
                    voice atticus_anythingelsea
                    Atticus "Autre chose?{nw}"
                    jump redo_identity_loop
                "La difficulté.":
                    voice atticus_diffchoice
                    Atticus "Okay, quel genre de difficulté tu veux?"

                    call diff_choice_menu from _call_diff_choice_menu

                    voice atticus_anythingelsea
                    Atticus "Quelque chose d'autre? J'ai le temps.{nw}"
                    jump redo_identity_loop
                "Je veux changer mes stats!":
                    call stats_redo_questions from _call_stats_redo_questions
                    $displaymenu = True
                    $Atticus_State["eye"] = 6
                    voice atticus_anythingelsea
                    Atticus "Autre chose?{nw}"
                    jump redo_identity_loop

        "J'aimerais bidouiller quelque trucs a propos de moi.":
            voice atticus_mixingthingsup
            menu:
                extend ""
                "Je veux changer mon style.":
                    $Atticus_State["armR"] = 1
                    $Atticus_State["eye"] = 5
                    voice atticus_chuckle

                    Atticus "Pas d'mal dans changer de style!\n\n .,Que voudrais tu changer?{nw}"
                    $Atticus_State["armR"] = 1
                    $Atticus_State["eye"] = 0
                    show robyn:
                        matrixcolor TintMatrix("#b6f0fc")
                        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                        xcenter 1.3
                        ease 1.0 xcenter 0.85
                    show atticus:
                        ease 0.5 xcenter 0.2
                    call id_Loop from _call_id_Loop_1
                    show robyn:
                        ease 1.0 xcenter 1.5
                    show atticus:
                        ease 0.5 xcenter 0.5
                    $Atticus_State["armR"] = 0
                    voice atticus_anythingelsea
                    Atticus "T'a l'air cool comme ça. \n\n Besoin d'autre chose?"
                    jump redo_identity_loop
                "Je veux changer mon identitée.":
                    voice atticus_reminded
                    $Atticus_State["eye"] = 0
                    $displaymenu = False
                    python:
                        PCname = renpy.input("First Name",length=10)
                        persistent.RobynName[0] = PCname = PCname.strip()
                    play sfx select3
                    python:
                        PClastname = renpy.input("Last Name",length=10)
                        persistent.RobynName[1] = PClastname = PClastname.strip()
                    play sfx select3

                    python:
                        if not PCname:
                            persistent.RobynName[0] = PCname = "Robyn"
                        if not PClastname:
                            persistent.RobynName[1] = PClastname = "Hart"

                        save_name = "[PCname] [PClastname]"

                    Atticus "[PCname] [PClastname] huh? \n\n C'est fait.."

                    $displaymenu = True
                    Atticus "Et pour le genre?{nw}"
                    menu:
                        extend ""
                        "He/Him":
                            python:
                                persistent.RobynPronouns = 0
                                PCthey = "he"
                                PCthem = "him"
                                PCtheir = "his"
                                PCtheirs = "his"
                                PCThey = "He"
                                PCThem = "Him"
                                PCTheir = "His"
                                PCTheirs = "His"
                        "She/Her":
                            python:
                                persistent.RobynPronouns = 1
                                PCthey = "she"
                                PCthem = "her"
                                PCtheir = "her"
                                PCtheirs = "hers"
                                PCThey = "She"
                                PCThem = "Her"
                                PCTheir = "Her"
                                PCTheirs = "Hers"
                        "They/Them":
                            python:
                                persistent.RobynPronouns = 2
                                PCthey = "they"
                                PCthem = "them"
                                PCtheir = "their"
                                PCtheirs = "theirs"
                                PCThey = "They"
                                PCThem = "Them"
                                PCTheir = "Their"
                                PCTheirs = "Theirs"
                    Atticus "Je vais garder ça en tête."

                    $displaymenu = True
                    voice atticus_anythingelseb
                    Atticus "Autre chose?"
                    $Atticus_State["eye"] = 0
                    $Atticus_State["armR"] = 0
                    jump redo_identity_loop
                "Changer ma voix.":
                    Atticus "Cool. On prend quoi?{nw}"

                    menu:
                        extend ""

                        "Voice A":
                            $robynvoice = persistent.pcvoice = 1
                        "Voice B":
                            $robynvoice = persistent.pcvoice = 2

                    $Atticus_State["eye"] = 6
                    play voice2 [RobynSays("Generic","Excited"),audio.atticus_anythingelsea]
                    Atticus "Autre chose?{nw}"
                    jump redo_identity_loop

        "Je veux tester des trucs." if gameVersion == 1:
            jump test_zone_select_label

        "J'ai besoin de conseils patternels.":
            $displaymenu = False
            $Atticus_State["eye"] = 1

            $xStr = renpy.random.choice(["T'es serieux?","Oh tu rigole.","Rooh, okay.","T'es sur?","Um okay.","Tu doit vraiment te faire chier.","Tu te fout de moi, hein?","Gamin je suis pas ton... Rooh et puis zut.","Ne me regarde pas comme ca.","Je te comprend un peu. Mais juste un peu."])
            Atticus "[xStr]"

            $Atticus_State["eye"] = 6

            voice atticus_hmmb
            Atticus "{sc=6}...{/sc}"

            $Atticus_State["eye"] = 5
            show atticus:
                blur 0
                ease 0.2 yoffset -20
                ease 0.2 yoffset 0

            $xStr = renpy.random.choice(["Ne me demande pas des conseils d'amitiés. Si tu en à besoin c'est quelle ne durerons pas.",
                "Fait quand même un peu le con parfois.",
                "L'école c'est vraiment un endroit de con. Enfin c'est peut-être pas politiquement correct mais c'est mon avis.",
                "Tu t'est lavé les dents aujourd'hui?",
                "Si tu à mal a la tête quand tu te fait transporter par un mothman, regarde l'horizon. Ou mange des biscuits.",
                "Tu devrais boire un peu d'eau.",
                "Toujours se brosser les plummes avant d'aller dormir.",
                "Si une prophétie te fait mal, S'il te plaît... Laisse toi pleurer.",
                "Tu sais... J'ai entendu dire que si on frottait une citrouille-lanterne dans de la vaseline, ça durerait plus longtemps. C'est un peu dégeu si tu veux mon avis.",
                "Fermes les rideaux la nuit et allume des LEDs. Ca gardera les phalènes écartés. J'ai um... Confondu les lumières d'un porche et la lune une fois.",
                "Ne met pas tes antennes la ou elle ne doivent pas être.",
                "Bigfoot est un gros con, et tu peux me citer la dessus.",
                "N'embrasse jamais avec les proboscis.","T'a vu Atlas quelque part? ... Ils ne répond pas a mes appels.",
                "Comment tu t'en sort? Ca fait pas mal de temps que tu te ballade.","Quelqu'un m'a dit qu'une personne du nom de Linkfandos était super cool.",
                "Oublie pas d'étirer tes ailes et tes talons.","Tient c'est marrant j'ai eu une vision dans laquelle quelqu'un fesait une serie de vidéo avec des avocats et que j'était dedans.",
                "Mon nom c'est en réalité {glitch=100}Atticus.{/glitch} \n\nNon pas que ce soit important.",
                "Tu me fatigue un peu... J'ai pas déja assez parlé?",
                "J'aimerais bien manger un bloc de fromage.",
                "J'ai un sentiment que ont va se voir un de ces jours.",
                "Tu devrais essayer le thé. C'est moins callorique que le café.",
                "Ma boison préférée? Eh bien c'est la limonade à la pèche. De rien."])

            voice renpy.random.choice([audio.atticus_dadisma,audio.atticus_dadismb,audio.atticus_dadismc,audio.atticus_backinmydaya,audio.atticus_backinmydayb])
            Atticus "[xStr]"
            $Atticus_State["eye"] = 6

            voice atticus_anythingelsea
            Atticus "Quoi d'autre?{nw}"
            jump redo_identity_loop

    return

label diff_choice_menu:
    menu:
        extend ""

        "Humain (Facile)":
            Atticus "Ah facile. Ce mode réduit les dégâts que toi et tes amis subissez lors des combats et facilite légèrement les lancers de dé."
            $gameDiff = persistent.gD = 1

        "Cryptide (Par défaut)":
            Atticus "Je vois. Simpliste."
            $gameDiff = persistent.gD = 2

        "Ghoule (Dur dur)":
            Atticus "Ghoule augmente essentiellement les dégâts/soins que tout le monde subit. Il est plus explosif, mais conçu pour être plus rapide pour ceux qui recherchent un faible nombre de tours dans les combats."
            $gameDiff = persistent.gD = 3

        "Demon (Pour les gens un peu étrange)":
            Atticus "Oh je vois tu est un masochiste. Tout est super dur. En plus de rendre les lancers de dé super chiant."
            $gameDiff = persistent.gD = 4
    return

label dice_choice_menu:
    menu:
        extend ""

        "Bon vieux D6" if persistent.unlockedDice[0] or gameVersion >= 2:
            $persistent.dieSettings = 1
            $displaymenu = False
            Atticus "Ah, le bon vieux fiable. Même si c'est un peu basique, les matrices de base sont tout simplement fiables."
        "Puriste des enfers" if persistent.unlockedDice[1] or gameVersion >= 2:
            $persistent.dieSettings = 2
            $displaymenu = False
            Atticus "Bon choix. Die Hard Purist est le genre de dés que tu prend si tu renonce principalement au système de karma. Avec un seul karma, tu devras compter davantage sur la chance."

            Atticus "Au moins il a des chiffres plus haut."
        "Jus de citron" if persistent.unlockedDice[2] or gameVersion >= 2:
            $persistent.dieSettings = 3
            $displaymenu = False
            Atticus "Lemon Squeezy. Celui là est mieux si tu veux la jouer molo. Même si tu loupe ton lancer, tu regagne quand même du Karma."
        "Peur et faim" if persistent.unlockedDice[3] or gameVersion >= 2:
            $persistent.dieSettings = 4
            $displaymenu = False
            Atticus "Tu préfère le chaos, hein? Pas de nombre. Juste Oui ou Non. Un simple lancer de pile ou face."
        "Yeux de serpents" if persistent.unlockedDice[4] or gameVersion >= 2:
            $persistent.dieSettings = 5
            $displaymenu = False
            Atticus "SCelui la est un peu chelou. Le premier lancer rate toujors mais le deuxième fait toujours 8. T'a interet dans le karma."

        "Plus" if True in persistent.unlockedDice[5:] or gameVersion >= 2:
            $displaymenu = True
            menu:
                extend ""

                "Full Moon Duet" if persistent.unlockedDice[5] or gameVersion >= 2:
                    $persistent.dieSettings = 6
                    $displaymenu = False
                    Atticus "Full Moon Duet est sympa. C'est un 8 et un 4!"
                    Atticus "..."
                    Atticus "C'est surtout aesthetic ca donne juste un chiffre plus proche du millieu.."
                "Even Stevens" if persistent.unlockedDice[6] or gameVersion >= 2:
                    $persistent.dieSettings = 7
                "Prime Party" if persistent.unlockedDice[7] or gameVersion >= 2:
                    $persistent.dieSettings = 8
                "3 Lizards In a Trenchcoat" if persistent.unlockedDice[8] or gameVersion >= 2:
                    $persistent.dieSettings = 9
                "Mothman's Hoard" if persistent.unlockedDice[9] or gameVersion >= 2:
                    $persistent.dieSettings = 10
                "New Jersey Greataxe" if persistent.unlockedDice[10] or gameVersion >= 2:
                    $persistent.dieSettings = 11

    python:
        diceBot.setDieType(persistent.dieSettings)
        pc_karma = diceBot.maxKarma
    return

label dice_choice_menu_alt:
    menu:
        extend ""

        "Ol' Reliable" if persistent.unlockedDice[0] or gameVersion >= 2:
            $persistent.dieSettings = 1
            $displaymenu = False
            Narrator "Dés standart. 3 karma avec 2 dés 1-6."
        "Die Hard Purist" if persistent.unlockedDice[1] or gameVersion >= 2:
            $persistent.dieSettings = 2
            $displaymenu = False
            Narrator "Gros chiffre mais seulement 1 de karma. Tu garde toujours ton karma si tu reroll pas par contre."

        "Lemon Squeezy" if persistent.unlockedDice[2] or gameVersion >= 2:
            $persistent.dieSettings = 3
            $displaymenu = False
            Narrator "6 karma, plus gros chiffres, et la capacité de récuperer du karma sur des lancés loupés. C'est simplement le meilleur putain de dé dans tout le jeu. Bravo le game design."

        "Jackalope's Fate" if persistent.unlockedDice[3] or gameVersion >= 2:
            $persistent.dieSettings = 4
            $displaymenu = False
            Narrator "Jackalope's fate has 2 outcomes, complete success or complete failure. It's a split 50/50 set for those who like chaos, 2 max karma, and karma returned on failed rerolls."
        "Snake Eye Sam" if persistent.unlockedDice[4] or gameVersion >= 2:
            $persistent.dieSettings = 5
            $displaymenu = False
            Narrator "Snake Eye Sam always rolls snake eyes on the first roll, but on rerolls it never rolls below an 8. With a staggering 8 max karma, this set is focused on managing karma and failing tactically."

        "More" if True in persistent.unlockedDice[5:] or gameVersion >= 2:
            $displaymenu = True
            menu:
                extend ""

                "Full Moon Duet" if persistent.unlockedDice[5] or gameVersion >= 2:
                    $persistent.dieSettings = 6
                    $displaymenu = False
                    Atticus "Full Moon Duet is a fun one. Instead of 2d6, it's a d4 and a d8!"
                    Atticus "..."
                    Atticus "It's mostly aestetic difference. This set is just more likely to get something more towards the middle."
                "Even Stevens" if persistent.unlockedDice[6] or gameVersion >= 2:
                    $persistent.dieSettings = 7
                "Prime Party" if persistent.unlockedDice[7] or gameVersion >= 2:
                    $persistent.dieSettings = 8
                "3 Lizards In a Trenchcoat" if persistent.unlockedDice[8] or gameVersion >= 2:
                    $persistent.dieSettings = 9
                "Mothman's Hoard" if persistent.unlockedDice[9] or gameVersion >= 2:
                    $persistent.dieSettings = 10
                "New Jersey Greataxe" if persistent.unlockedDice[10] or gameVersion >= 2:
                    $persistent.dieSettings = 11

    python:
        diceBot.setDieType(persistent.dieSettings)
        pc_karma = diceBot.maxKarma
    return

label chapter_select_label:
    $displaymenu = True
    voice atticus_chselect
    Atticus "Tu vas ou?{nw}"

    menu:
        extend ""
        "Au TOUT début.":
            Atticus "Cool. Laisse moi juste anihiller toute information sur toi de mon cerveau..."
            call choose_identity from _call_choose_identity_1
            jump Ch0_Intro
        "Chapitre 0":
            jump Ch0_SectionSelect_Label

        "Chaptitre 1" if seenLabel("Ch1_Start"):
            jump Ch1_SectionSelect_Label

        "Chaptitre 2" if seenLabel("Ch2_DreamHouse_Intro"):
            jump Ch2_SectionSelect_Label

        "Ballades" if checkUnlock("MM",1) or gameVersion == 3:
            jump Hangouts_select_label


    return

#Chapter 0
label Ch0_SectionSelect_Label:
    menu:
        extend ""
        "Jouer normallement":
            jump Ch0_Intro
        "Elkhorn Radio" if seenLabel("atTheStation"):
            jump atTheStation
        "Elkhorn Radio (Inside the Station & Investigation)" if seenLabel("exploreStation"):
            jump exploreStation
        "Show de Madhouse" if seenLabel("RadioShow"):
            jump RadioShow
        "Tuto de Madlas" if seenLabel("fightbuildup"):
            python:
                displaymenu = False
                PC_Stats = RobynUnit()
                PC_Stats.updateStats()
                PC_Stats.resetSelf()

                PC_Stats.SetAttackMoves(['Bash', 'Cheer', 'Focus', 'Heart Out'], 'FIGHT_01_MM_ROBYN_')

                playerUnits = []
                playerUnits.append(PC_Stats)

            jump fightbuildup
        "Après la frappe de Madhouse & Ghost Zone" if seenLabel("MM_fightAftermath"):
            $displaymenu = False
            jump MM_fightAftermath
        "Après la Ghost Zone & rentrer à la maison" if seenLabel("leavingElkhornRadio_ch0"):
            $displaymenu = False
            jump leavingElkhornRadio_ch0


#Side Story / B Plot
label Hangouts_select_label:
    menu:
        extend ""
        "Madhouse #1" if checkUnlock("MM",1):
            jump MM_Hangout1

        "Madhouse #2" if checkUnlock("MM",2):
            jump Madhouse_Hangout2

        "August #1" if checkUnlock("Gus",1):
            jump August_Hangout1

#Test Zones
label test_zone_select_label:
    menu:
        extend ""
        "Jos' Test Zone":
            $displaymenu = False
            ##TESTING FOR JOS COMMENT IF NEEDED
            jump FIGHT_00_DUNGEON_MAESTRO
        "Dom's Test Zone":
            $displaymenu = False
            #In scripts\testingzone.rpy
            jump testZone
        "Zakirin's Test Zaone":
            $displaymenu = False
            #In scripts/biscuitTown.rpy
            jump biscuittown

#Battles
label battle_select_label:
    if gameVersion < 2:
        Atticus "Here you can fight optional or powered up versions of bosses throughout the game. On top of that, certain patrons can even fight Bosses that're still being developed!"

    voice atticus_diffchoiceb
    Atticus "So, which battle shall we try?{nw}"

    menu:
        extend ""
        "Madhouse" if seenLabel("FIGHT_01_MADHOUSE"):
            voice atticus_goodchoice
            call FIGHT_01_MADHOUSE from _call_FIGHT_01_MADHOUSE

        "Mr. Walker" if seenLabel("FIGHT_05_MISTWALKER"):
            voice atticus_goodchoice
            call FIGHT_05_MISTWALKER from _call_FIGHT_05_MISTWALKER_1

        "Jamie" if seenLabel("FIGHT_06_JAMIE"):
            voice atticus_goodchoice
            call FIGHT_06_JAMIE from _call_FIGHT_06_JAMIE

        "Dream Guard" if gameVersion >= 1:
            voice atticus_goodchoice
            call FIGHT_04_DREAMOZ from _call_FIGHT_04_DREAMOZ

        "Dream Eater" if gameVersion >= 1:
            voice atticus_goodchoice
            call FIGHT_02_LEX from _call_FIGHT_02_LEX

        "EX Battles" if seenLabel("FIGHT_01_MADHOUSE"):
            menu:
                extend ""

                "Gladhouse":
                    voice atticus_goodchoice
                    call FIGHT_01B_MADHOUSE from _call_FIGHT_01B_MADHOUSE

                "Madlas EX":
                    voice atticus_goodchoice
                    call FIGHT_00B_MADLAS from _call_FIGHT_00B_MADLAS

                "Book Babes" if gameVersion >= 1:
                    voice atticus_goodchoice
                    Atticus "This fight is going to be scrapped into an EX Battle and replaced with a new fight as an FYI but enjoy!"

                    call FIGHT_03_LIB from _call_FIGHT_03_LIB
                    
                "Mistwalker EX" if seenLabel("FIGHT_05_MISTWALKER"):
                    voice atticus_goodchoice
                    call FIGHT_05B_MISTWALKER from _call_FIGHT_05B_MISTWALKER

                "Jamie EX" if seenLabel("FIGHT_06_JAMIE"):
                    call FIGHT_06B_JAMIE from _call_FIGHT_06B_JAMIE

                "Robo-Atlas" if seenLabel("FIGHT_06_JAMIE"):
                    voice atticus_goodchoice
                    call FIGHT_03_RBA from _call_FIGHT_03_RBA


    $HideBars()
    jump start
