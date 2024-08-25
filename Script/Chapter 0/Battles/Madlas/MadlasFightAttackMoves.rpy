label FIGHT_00_MADLAS_ROBYN_0:
    $eName = enemyUnits[targetChoice].name
    $pName = playerUnits[0].name

    if isRollSuccess:
        Narrator "[pName] frappe [eName] avec un poing!"
        python:

            xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("brawn"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")



        Narrator "[eName] prend [sfxDmg] damage!"

        $enemyUnits[targetChoice].modifyStatMod("power",-1,-4,4)

    else:
        Narrator "[pName] Frappe${w=.5} et loupe lamentablement. Les yeux de [eName]sont rivés sur [pName] a présent."
        #Modify Mahouse Stat
        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

    $playerUnits[0].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_ROBYN_1:

    python:
        eName = enemyUnits[0].name
        pName = playerUnits[0].name
        if targetChoice != -1:
            xArray = ["Allez moi! Tu peux le faire!","Montre leur ce qui fait de toi un démon, Jamie!"]
            xStr = xArray[targetChoice]
        else:
            xStr = "C'est l'heure de lui défoncer le cul!"
    Robyn "[xStr]"

    if targetChoice == -1:
        $playerUnits[0].modifyStatMod("power",1,-4,4)
        $playerUnits[1].modifyStatMod("power",1,-4,4)
    else:

        python:
            #Raises Power by 1
            xName = playerUnits[targetChoice].name
            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

            HighlightPlayerUnitBars([targetChoice])


        Narrator "[pName] utilise le pouvoir de la determination pour soigner [xName] de [xHeal] [kwHealth]!"

        python:
            #Heals Target
            playerUnits[targetChoice].modifyStatMod("power",2,-4,4)
            xHeal = renpy.random.randint(3,7)

    if not isRollSuccess:
        Narrator "[eName] a définitivement pris les mots de [PCname] de la mauvaise manière, donc il est soigné aussi!"

        $enemyUnits[0].modifyStatMod("power",2,-4,4)


    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_ROBYN_2:
    $pName = playerUnits[0].name
    if isRollSuccess:
        #Raises Karma on success
        Narrator "[pName] réspire profondément,, et éssaie de regagner son {i}focus{/i}."

        Robyn "… Okay! C'est bon!"

        $pc_karma = limitValue(pc_karma+1, 0, diceBot.maxKarma)
        play sfx powerup_a
        Narrator "[kwKarma] increases by +2!"

    else:
        #Raises Jamie's Brain's and occult on a failure
        Narrator "[pName] réspire profondément,, mais tu te fait arrèter en plein milleu."

        Robyn "Je crois que j'ai cassé mon cerveau."

        Jamie "T'inquète je m'en occupe."

        python:
            xName = playerUnits[1].name
            Jamie_Stats.modifyStatMod("brawn",2,-4,4)
            Jamie_Stats.modifyStatMod("occult",2,-4,4)

    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_0:
    python:
        pName = playerUnits[1].name
        eName = enemyUnits[0].name

    #Calculates Damage
    $xDmg = -(renpy.random.randint(7,10) + playerUnits[1].cPower("occult"))
    $xStr = renpy.random.choice(["Reaching up, " +pName+ " cups the flame in their hands and whispers a spell, the small flame dancing forward before exploding into a wild burst of hellfire.", "Swiping their hand through the air, " +pName+ " unleashes a raging bolt of blue hellfire."])

    Narrator "[xStr]"

    if isRollSuccess:
        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")


        Narrator "[eName] se fait prendre dans une lumière bleue et prend [sfxDmg] dommages!"
        $MD_State["eyes"] = 6
        $MD_State["feelerL"] = 1
        $MD_State["feelerR"] = 1
        $MD_State["mouth"] = 0
        Madlas "{sc=4}GyaAAAH!{/sc}"
        $MD_State["eyes"] = 1
        $MD_State["feelerL"] = 0
        $MD_State["feelerR"] = 0
        $MD_State["mouth"] = 1

        if renpy.random.choice([True,False]):
            Narrator "[pName] jette un regard au monstre et se force de fermer les yeux."
            $MD_State["eyes"] = -1
            Jamie "J'suis désolé!"
    else:
        Narrator "Les braséros magiquent manquent de contrôle!"
        camera at camera_shake
        $HighlightPlayerUnitBars([0,1])
        $xDmg = int(-0.75*(renpy.random.randint(7,9) + playerUnits[1].cPower("occult")))

        $playerUnits[0].modifyHP(xDmg,0.0,"brains")
        $playerUnits[1].modifyHP(xDmg,0.0,"brains")

        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")

        Narrator "Everyone takes damage!"
        Robyn "JAMIE!"
        $ToggleBarState([0,1], 0)

    $playerUnits[1].DiminishModifiers([2,3,4,5])

    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_1:
    python:
        pName = playerUnits[1].name
        eName = enemyUnits[0].name

    $HighlightPlayerUnitBars([1])
    Narrator "[pName] se pète le crâne sur le corps de [eName] avec une précision déconcertante!"
    $targetName = enemyUnits[targetChoice].name

    $xDmg = -(renpy.random.randint(4,6) + playerUnits[1].cPower("brawn"))
    $enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")
    $eDmg = sfxDmg

    if isRollSuccess:
        $xDmg= int(0.5*xDmg)

    $playerUnits[1].modifyHP(xDmg,1.0,"guts")


    camera at camera_shake
    Narrator "[eName] prend [eDmg] dommages! [pName] prend aussi [sfxDmg] de recoil!"
    $ToggleBarState([1], 0)

    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $playerUnits[1].modifyStatMod("guts",-1,-4,4)

    $playerUnits[1].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_2:
    $pName = playerUnits[1].name
    if targetChoice != -1:
        $xHeal = renpy.random.randint(6,9) + playerUnits[1].cPower("occult")
        $xName = playerUnits[targetChoice].name
        $HighlightPlayerUnitBars([targetChoice])

        #Halve Healing on fail
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)
    else:
        $HighlightPlayerUnitBars([0,1,2,3])

    if targetChoice == -1:
        $xHeal = renpy.random.randint(2,4) + playerUnits[1].cPower("occult")
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)

        $playerUnits[0].modifyHP(xHeal,0.0,"guts")
        $playerUnits[1].modifyHP(xHeal,0.0,"guts")


        Narrator "[pName] ferme les yeux, et la lumière entre ses cornes émanne d'une lumière bleue rafraichissante. Iel panse ainsi quelques-unes des bléssures du groupe."
    else: #Single Target
        $playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        Narrator "[pName] ferme les yeux, et la lumière entre ses cornes émanne d'une lumière bleue rafraichissante, procurant un soin de [xHeal] [kwHealth]."

    if not isRollSuccess:
        $xStr = renpy.random.choice(["...Tu peux pas la fermer le gremlin?!","Raaah...","J'ESSAIE de lancer un sort.","Putain j'y arrive pas...","Putain de merde!"])

        Narrator "Iel grogne, incapable de plus se concentrer."

        Jamie "[xStr]"
    else:
        Jamie "J'éspère que ça va aider."

    $playerUnits[1].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_MD_ATTACK:
    $bossName = enemyUnits[0].name
    $CheckForGameOvers()
    play sfx boss_target_sfx
    python:
        xAtk = renpy.random.choice([0,1])

        eTarget = renpy.random.randint(0,1)

        while not playerUnits[eTarget].isAlive:
            eTarget = renpy.random.randint(0,1)

        eTargetName = playerUnits[eTarget].name
        HighlightPlayerUnitBars([eTarget])

    if xAtk == 0: #Phantom Slash
        python: #Calculate Damage and Highlight Bar

            xDmg = -(renpy.random.randint(3,6) + enemyUnits[0].cPower("brawn"))

        Narrator "[bossName] regarde [eTargetName] et griffe violament en sa direction!"

        call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("hustle"), "Phantom Slash") from _call_dice_roll_21

        camera at camera_shake
        if isRollSuccess: #Half Damage on success
            python:
                xDmg= int(0.5*xDmg)
                playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")


            Narrator "[eTargetName] en sort peu touché avec [sfxDmg] dommages!"
        else: #Damage bby
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
            $xStr = renpy.random.choice(["takes a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])


            Narrator "[eTargetName] [xStr] [sfxDmg] damage!"
    else:
        $xDmg = -(renpy.random.randint(5,7))
        Narrator "[bossName] expulse une enceinte sur-dimmensionnée dans la direction de [eTargetName]!"

        call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_22
        show MMFight_Chair at MMFight_LeftProp_Exit
        show MMFight_Speaker at MMFight_RightProp_Exit
        if isRollSuccess:
            $xStr = renpy.random.choice(["se dégage de la trajéctoire en se cachant derrière un bureau.","protège son visage dse morceaux, et ne prend aucun pas de dommages.","se bouge gracieusement du chemin.", "recule sur le coté, le projéctile touche le sol est se fragment."])
            Narrator "[eTargetName] [xStr]"
        else: #Damage on failure
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
            $xStr = renpy.random.choice(["prend un gros coup, résultant en", "crache sur un total de", "se fait éjécter prennant", "rammasse sa tête sur le sol et prend","se le BONK en pleine tête prennant"])

            camera at camera_shake
            Narrator "[eTargetName] [xStr] [sfxDmg] dommages!"


        show MMFight_Chair at MMFight_LeftProp_Entry
        show MMFight_Speaker at MMFight_RightProp_Entry
        $ToggleBarState([0,1], 0)

    jump expression currentLabelPT
