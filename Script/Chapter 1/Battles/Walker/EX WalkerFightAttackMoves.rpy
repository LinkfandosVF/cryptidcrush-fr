# ---------------------------------------------------------------------(0) ROBYN
#BASH
label FIGHT_05B_MW_ROBYN_0:
    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name
        HighlightPlayerUnitBars([0])

    if isRollSuccess:
        Narrator "[pName] kicks [eName] and throws a wobbly punch!"
        call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT
        python:
            xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("brawn"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

            #,modifyHP(mod=xDmg)


        Narrator "[eName] takes [sfxDmg] damage!"

        $enemyUnits[targetChoice].modifyStatMod("power",-1,-4,4)
    else:
        Narrator "Punch{w=.5} And a miss! [eName] snickers at [pName] condescendingly."

        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

    $playerUnits[0].DiminishModifiers([1,3,4,5])
    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_3
    jump expression currentLabelET

#FOCUS
label FIGHT_05B_MW_ROBYN_1:
    $pName = playerUnits[0].name

    if isRollSuccess:
        #Raises Karma on success

        Narrator "[pName] takes a moment to collect [PCtheir] thoughts."

        Robyn "I… I think I've got it!"

        $addBattleKarma(2)
    else:
        Narrator "As [pName] tries to think [PCtheir] thoughts get away from [PCthem]. [pName] is overwhelmed."

        Robyn "I-I dunno if I can do this. It's all too much."

        Oz "..."

        python:
            playerUnits[2].modifyStatMod("brawn",2,-4,4)
            playerUnits[2].modifyStatMod("brains",2,-4,4)

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_4
    jump expression currentLabelET

#SLEIGHT OF CROWBAR
label FIGHT_05B_MW_ROBYN_2:
    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name

    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_1
    if isRollSuccess:
        python:
            xDmg = -(renpy.random.randint(3,5) + playerUnits[0].cPower("hustle"))
            enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")

        Narrator "THWACK! [pName] successfully feints [eName] with a crowbar, taking [sfxDmg] damage!"
    else:
        python:
            xDmg = -(4+playerUnits[0].cPower("hustle"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

        Narrator "CLUNK. [eName] sees [pName] coming and only takes [sfxDmg] damage!"

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_5
    jump expression currentLabelET

#FLEX
label FIGHT_05B_MW_ROBYN_3:
    $pName = playerUnits[0].name
    Narrator "[pName] strikes a pose!"

    python:
        for x in ["brawn","brains","hustle","guts","charm","occult"]:
            playerUnits[0].modifyStatMod(x,3,-4,4)

    if not isRollSuccess:
        Narrator "Unfortunately, the enemy catches on and strikes a cooler pose."
        python:
            for x in range(len(enemyUnits)):
                if enemyUnits[x].isAlive:
                    enemyUnits[x].modifyStatMod("diff",2,-4,4)

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_6
    jump expression currentLabelET

#CHEER
label FIGHT_05B_MW_ROBYN_4:

    python:
        pName = playerUnits[0].name

        #Random Text
        if targetChoice != -1:
            xArray = ["I um, I feel like a third wheel here!", "Oz, you're frightening, but in a cool way!","Go get 'em tiger!", "Let's go Jamie!"]
            xStr = xArray[targetChoice]
        else:
            xStr = "Hang in there guys!"

    Narrator "[xStr]"

    if targetChoice == -1: #Multi-Target
        python:
            HighlightPlayerUnitBars([0,1,2,3])

            #Increases everyone's power by +1
            for x in range(len(playerUnits)):
                playerUnits[x].modifyStatMod("power",1,-4,4)

    else: #Single Target
        python: #Healing
            xName = playerUnits[targetChoice].name
            HighlightPlayerUnitBars([targetChoice])
            xHeal = renpy.random.randint(3,7)
            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        #Update HP
        Narrator "[pName] uses the power of will to heal [xName]'s for [xHeal] [kwHealth]!"

        #Stat Change
        $playerUnits[targetChoice].modifyStatMod("power",2,-4,4)

    if not isRollSuccess:
        Narrator "The shadows take [pName]'s words to heart and feel empowered!"

        python:
            for x in range(len(enemyUnits)):
                if enemyUnits[x].isAlive:
                    enemyUnits[x].modifyStatMod("power",1,-4,4)

            HighlightEnemyUnitBars([0,1,2,3])



    $playerUnits[0].DiminishModifiers([2,3,5])
    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_7
    jump expression currentLabelET

#Healing Spirit
label FIGHT_05B_MW_ROBYN_5:
    python:
        pName = playerUnits[0].name
        xHeal = renpy.random.randint(3,5) + playerUnits[0].cPower("occult")

        for x in range(len(playerUnits)):
            playerUnits[x].modifyHP(xHeal,0.0,"guts")

    Narrator "The party is healed in a moment of relief."

    python:
        xNum = -1
        if not isRollSuccess:
            xNum = -2

        playerUnits[0].modifyStatMod("brains",xNum,-4,4)
        playerUnits[0].modifyStatMod("guts",xNum,-4,4)

        playerUnits[0].DiminishModifiers([2,3,4,5])

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_8
    jump expression currentLabelET

#Kazap
label FIGHT_05B_MW_ROBYN_6:
    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_2
    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name

        xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("occult"))
        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

    Narrator "[pName] aims their phone at [eName] and shoots out a burst of electricity dealing [sfxDmg] damage!"

    python:
        if isRollSuccess:
            enemyUnits[targetChoice].modifyStatMod("brawn",-2,-4,4)
            enemyUnits[targetChoice].modifyStatMod("brains",-2,-4,4)

        playerUnits[0].DiminishModifiers([2,3,4,5])

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_9
    jump expression currentLabelET
# -----------------------------------------------------------------------(1) GUS
#Onslaught
label FIGHT_05B_MW_GUS_0:
    python:
        playerUnits[1].counterPow = 0
        pName = playerUnits[1].name
        eName = enemyUnits[targetChoice].name
        hitAcc = [True,isRollSuccess]



    Narrator "[pName] goes wild!"


    call FIGHT_05B_MW_GUS_0_SLASH(-1) from _call_FIGHT_05B_MW_GUS_0_SLASH

    if renpy.random.choice(hitAcc) and enemyUnits[targetChoice].isAlive:
        call FIGHT_05B_MW_GUS_0_SLASH(1) from _call_FIGHT_05B_MW_GUS_0_SLASH_1

    $hitAcc.append(False)
    if renpy.random.choice(hitAcc) and enemyUnits[targetChoice].isAlive:
        call FIGHT_05B_MW_GUS_0_SLASH(3) from _call_FIGHT_05B_MW_GUS_0_SLASH_2

    call FIGHT_05B_MW_GUS_REGEN from _call_FIGHT_05B_MW_GUS_REGEN
    $playerUnits[1].DiminishModifiers([1,3,4,5])
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_10
    jump expression currentLabelET

label FIGHT_05B_MW_GUS_0_SLASH(xMod=0):
    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_3
    python:
        #Enemy Damage
        xDmg = -limitValue((1+xMod + playerUnits[1].cPower("brawn")),1,100)
        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

    Narrator "[eName] takes [sfxDmg] damage!"
    return

#HOWL
label FIGHT_05B_MW_GUS_1:
    python:
        playerUnits[1].DiminishModifiers([2,3,5])
        playerUnits[1].counterPow = 0
        eName = enemyUnits[targetChoice].name
        playerUnits[1].DiminishModifiers([2,3,4,5])

    Narrator "August rears back and howls at the moon."

    $playerUnits[1].modifyStatMod("brawn",2,-4,5)

    if isRollSuccess:
        $enemyUnits[targetChoice].ChangeMTA(1)
        Narrator "[eName]'s [kwMTA] increases +1."
    else:
        $enemyUnits[targetChoice].ChangeMTA(-1)
        Narrator "[eName]'s [kwMTA] decreases -1."

    call FIGHT_05B_MW_GUS_REGEN from _call_FIGHT_05B_MW_GUS_REGEN_1
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_11
    jump expression currentLabelET

#Bite Back
# Counter
label FIGHT_05B_MW_GUS_2:
    python:
        if isRollSuccess:
            playerUnits[1].modifyStatMod("guts",2,-4,4)
        else:
            playerUnits[1].modifyStatMod("guts",-2,-4,4)

        pName = playerUnits[1].name
        playerUnits[1].counterPow=limitValue(playerUnits[1].counterPow+1,0,3)

    if playerUnits[1].counterPow == 3:
        Narrator "[pName] is at max counter power!"
    else:
        Narrator "[pName] is ready to bite back."

    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_12
    jump expression currentLabelET

#Sniff (Sniff it Out)
# Lowers Target Difficulty Mod
label FIGHT_05B_MW_GUS_3:
    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[1].name

    if isRollSuccess:
        Narrator "[pName] gets a read on [eName]!"
        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)
    else:
        Narrator "August can't catch a clue and sneezes."

    $playerUnits[1].DiminishModifiers([2,3,5])
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_13
    jump expression currentLabelET

label FIGHT_05B_MW_GUS_REGEN:
    $playerUnits[1].modifyHP(2,1.0,"guts")
    Narrator "Blessed by the moon's silvery light, August recovers 2 [kwHealth]!"
    return

label FIGHT_05B_MW_GUS_COUNTER(eDex=0):
    if not playerUnits[1].isAlive:
        $playerUnits[1].counterPow =0

    if playerUnits[1].counterPow > 0:
        python:
            eName = enemyUnits[eDex].name
            pName = playerUnits[1].name
            xDmgMod = int(playerUnits[1].counterPow*1.5)
            xDmg = -(xDmgMod + renpy.random.randint(0,1) + playerUnits[1].cPower("brawn"))
            enemyUnits[eDex].modifyHP(xDmg,0.0,"guts")
            playerUnits[1].counterPow = 0

        Narrator "{b}{sc}WHAM!{/sc}{/b} [pName] intercepts [eName] dealing [sfxDmg] damage!"
    return
# ------------------------------------------------------------------(2) OZ
#Silver Stab
label FIGHT_05B_MW_OZ_0:
    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[2].name

        xVar = dieTotal + playerUnits[2].cStats("brains")
        xPierce = 0
        if (xVar >= critNum):
            playerUnits[2].iconState = 3
            xPierce = 2
            xVar = "{sc}{b}SHINK!{/b}{/sc}"
            voice(playerUnits[playerChoice].getLine("crit"))
        else:
            xVar = "{sc}{b}SHUNK!{/b}{/sc}"

    if (isRollSuccess):
        call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_4

        python:
            xDmg = -limitValue(int(round(renpy.random.randint(-3,-1) + playerUnits[2].cPower("brains") + enemyUnits[targetChoice].cStats("occult")*2)),1,100)
            enemyUnits[targetChoice].modifyHP(xDmg,xPierce,"guts")

        Narrator "[xVar]\n\n[pName] stabs [eName] for [sfxDmg] damage!\nAnd flicks shadowy threads off the tip of his blade."

    else:
        Narrator "[pName] misses his mark. He's expressionless."

    $playerUnits[2].DiminishModifiers([2,3,4,5])
    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_14
    jump expression currentLabelET

#Glare
label FIGHT_05B_MW_OZ_1:
    python:
        xVar = dieTotal + playerUnits[2].cStats("brains")

        eName = enemyUnits[targetChoice].name
        pName = playerUnits[2].name
        if (xVar >= critNum):
            playerUnits[2].iconState = 3
            voice(playerUnits[playerChoice].getLine("crit"))

    if (isRollSuccess):
        python:
            enemyUnits[targetChoice].modifyStatMod("power",-1,-4,4)
            xDmg = -(renpy.random.randint(1,3) + playerUnits[2].cPower("charm"))
            enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")

        Narrator "[eName] is startled, feeling queasy for [sfxDmg] damage!"
    else:
        Narrator "[eName] wasn't looking."

    $xVar = dieTotal + playerUnits[2].cStats("charm")
    if (xVar >= critNum):
        $enemyUnits[targetChoice].ChangeMTA(2)
        Narrator "[eName]'s [kwMTA] increases +2."

    $playerUnits[2].DiminishModifiers([2,3,4,5])
    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_15
    jump expression currentLabelET

#Gut Punch
label FIGHT_05B_MW_OZ_2:
    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_5
    python:
        xVar = dieTotal + playerUnits[2].cStats("brawn")

        if (xVar >= critNum):
            playerUnits[2].iconState = 3
            voice(playerUnits[playerChoice].getLine("crit"))

        eName = enemyUnits[targetChoice].name
        pName = playerUnits[2].name

        xDmg = -(renpy.random.randint(4,5) + playerUnits[2].cPower("brawn"))
        if not isRollSuccess:
            xDmg = int(xDmg*0.5)

        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

    Narrator "[pName] buries his fist into [eName]'s gut and tears a meaty chunk out 'em for [sfxDmg]!"

    python:
        xVar = dieTotal + playerUnits[2].cStats("brawn")

        if (xVar >= critNum):
            enemyUnits[targetChoice].modifyStatMod("guts",-4,-4,4)
        else:
            enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

        playerUnits[2].DiminishModifiers([1,3,4,5])

    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_16
    jump expression currentLabelET

#Bandage Wounds
label FIGHT_05B_MW_OZ_3:
    python:
        p2Name = playerUnits[targetChoice].name
        pName  = playerUnits[2].name

    if pc_karma > 0:
        python:
            xHeal = renpy.random.randint(8,10)
            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")
            pc_karma-=1

        Narrator "[pName] hastily bandages [p2Name]'s wounds, replenishing [xHeal] [kwHealth]. He pats them on the back."

        $playerUnits[targetChoice].modifyStatMod("rollMod",3,-4,4)
    else:
        $addBattleKarma(2)

    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_17
    jump expression currentLabelET

# ------------------------------------------------------------------s(3) Jamie
label FIGHT_05B_MW_JAMIE_0: ##Jamie's Spirit Blaze
    python:
        HighlightPlayerUnitBars([3])
        pName = playerUnits[3].name
        Jamie_Stats.iconState = 3

        #Calculates Damage
        xDmg = -(renpy.random.randint(7,9) + playerUnits[3].cPower("occult"))
        xStr = renpy.random.choice(["Reaching up, " +pName+ " cups the flame in their hands and whispers a spell, the small flame dancing forward before exploding into a wild burst of hellfire.", "Swiping their hand through the air, " +pName+ " unleashes a raging bolt of blue hellfire."])

    Narrator "[xStr]"

    if isRollSuccess:
        call FIGHT_05B_MW_MISTWALKER_HURT(-1) from _call_FIGHT_05B_MW_MISTWALKER_HURT_6
        python:
            for x in range(len(enemyUnits)):
                enemyUnits[x].modifyHP(xDmg,0.0,"brains")
        Narrator "The enemy party is engulfed in a pale blue pyre!"

        if renpy.random.choice([True,False]):
            Narrator "[pName] whispers to the flame resting in their hands. It flickers before exploding in a ray of hellfire."

            Jamie "Thanks little friend."
    else:
        Narrator "The flames roar out of control!"
        camera at camera_shake
        $HighlightPlayerUnitBars([0,1,2,3])
        call FIGHT_05B_MW_MISTWALKER_HURT(-1) from _call_FIGHT_05B_MW_MISTWALKER_HURT_7
        python:
            xDmg = int(0.75*xDmg)
            for x in range(len(playerUnits)):
                playerUnits[x].modifyHP(xDmg,0.0,"brains")

            for x in range(len(enemyUnits)):
                enemyUnits[x].modifyHP(xDmg,0.0,"brains")

        Narrator "Everyone takes damage!"


    $playerUnits[3].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_05B_MW_JAMIE_1: ##Jamie's Skull Cracker.
    #Damage!!!
    python:
        pName = playerUnits[3].name
        eName = enemyUnits[targetChoice].name
    $HighlightPlayerUnitBars([3])
    Narrator "[pName] bashes their skull into [eName]’s head with precision roughness!"

    $xDmg = -(renpy.random.randint(4,6) + playerUnits[3].cPower("brawn"))
    $enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")
    $eDmg = sfxDmg

    if isRollSuccess:
        $xDmg= int(0.5*xDmg)

    $playerUnits[3].modifyHP(xDmg,1.0,"guts")


    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_8
    camera at camera_shake
    Narrator "[eName] takes [eDmg] damage! [pName] takes [sfxDmg] recoil damage!"

    #Modify Defense
    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $playerUnits[3].modifyStatMod("guts",-1,-4,4)

    $playerUnits[3].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_05B_MW_JAMIE_2: ##Jamie's Healing Wave.
    $pName = playerUnits[3].name
    #Calculate Healing for single target
    if targetChoice != -1:
        $xHeal = renpy.random.randint(6,9) + playerUnits[3].cPower("occult")
        $xName = playerUnits[targetChoice].name
        $HighlightPlayerUnitBars([targetChoice])

        #Halve Healing on fail
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)
    else:
        $HighlightPlayerUnitBars([0,1,2,3])

    if targetChoice == -1: #Multi Target
        $xHeal = renpy.random.randint(2,4) + playerUnits[3].cPower("occult")
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)

        python:
            for x in range(len(playerUnits)):
                playerUnits[x].modifyHP(xHeal,0.0,"brains")


        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over their allies, mending some of their wounds."
    else: #Single Target
        $playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over [xName], healing them for [xHeal] [kwHealth]."

    if not isRollSuccess:
        $xStr = renpy.random.choice(["...Can you all shut up?!","Mmmrgh...","I am TRYING to cast a spell.","I… can’t do this.","Goddammit!"])

        Narrator "They growl, unable to focus any further."

        Jamie "[xStr]"
    else:
        Jamie "I hope this helps."

    $playerUnits[3].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_05B_MW_JAMIE_3: ##Jamie's Chain Flare.
    #Sets Madhouse emote
    call FIGHT_05B_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05B_MW_MISTWALKER_HURT_9

    #Damage Calculation
    python:
        pName = playerUnits[3].name
        eName = enemyUnits[targetChoice].name

        xDmg = -(renpy.random.randint(4,6) + playerUnits[2].cPower("brawn"))
        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")


    Narrator "[pName] whips an iron chainwhip around [eName] and slams them into the ground for [sfxDmg] damage!"

    if isRollSuccess:
        python:


            xDmg = -(renpy.random.randint(-1,1) + playerUnits[3].cPower("occult"))
            if xDmg >=0:
                xDmg = -1
            enemyUnits[targetChoice].modifyHP(xDmg,1.0,"brains")


        Narrator "The whip catches fire and explodes for another [sfxDmg] damage!"

        $enemyUnits[targetChoice].modifyStatMod("hustle",-2,-4,4)

    $playerUnits[2].DiminishModifiers([1,2,3,4,5])
    jump expression currentLabelET

# ---------------------------------------------------------------------- ENEMIES
# ---------------------------------------------------------------------- ENEMIES
# ---------------------------------------------------------------------- ENEMIES
label FIGHT_05B_MW_MISTWALKER_HURT(eMan=0):
    if eMan in [-1,0]:
        show MrWalker hurt at WalkerPos
    if eMan in [-1,1]:
        show mw_lantern hurt
    return

#currentCA
# ----------------------------------------------------------------(0) MISTWALKER
label FIGHT_05B_MW_MISTWALKER_ATTACK:
    if currentCA == 1:
        call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_18
        call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_19
        call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_20
    elif currentCA == 3:
        call FIGHT_05B_MW_MISTWALKER_BUFFLANTERN from _call_FIGHT_05B_MW_MISTWALKER_BUFFLANTERN

    show MrWalker attack at WalkerPos
    python:
        CheckForGameOvers()
        HighlightEnemyUnitBars([0])

        eTarget = -1
        HighlightPlayerUnitBars([0,1,2,3])
        if numWisp >= 4:
            xAtk = 3
        elif numWisp  <= 1:
            xAtk = renpy.random.randint(1,2)
        else:
            xAtk = renpy.random.randint(0,3)


        if xAtk != 0 and xAtk != 3:
            eTarget = [playerUnits[0].calcAggro(),playerUnits[1].calcAggro(),playerUnits[2].calcAggro(),playerUnits[3].calcAggro()]
            eTarget = AIChooseTarget(eTarget)
            HighlightPlayerUnitBars([eTarget])


    play sfx boss_target_sfx
    call expression "FIGHT_05B_MW_MISTWALKER_" + str(xAtk) from _call_expression_36
    call FIGHT_05B_MW_GUS_COUNTER(0) from _call_FIGHT_05B_MW_GUS_COUNTER
    jump expression currentLabelPT

label FIGHT_05B_MW_MISTWALKER_BUFFLANTERN:
    python:
        eName = enemyUnits[0].name
        e2Name = enemyUnits[1].name
        enemyUnits[1].ChangeMTA(-1)

    Narrator "[eName] fuels the [e2Name] so that it can act sooner."
    return

#Shrill wind- AoE low damage. Spooks party on failure. Resisted by Brains
label FIGHT_05B_MW_MISTWALKER_0:
    #NOTE: THIS IS CURRENTLY BEING UNUSED DW ABOUT THIS MOVE

    Narrator "A bone-chilling wind breezes through the graveyard."

    call dice_roll(avgUnitStat(playerUnits,"brains"), enemyUnits[0].cDifficulty("occult"), "Shrill Wind") from _call_dice_roll_61

    if isRollSuccess:
        Narrator "You hide behind the behemoth that is Oz. He shivers but is unmoved. August gives you the side-eye."
        python:
            for x in range(len(playerUnits)):
                if playerUnits[x].isAlive:
                    playerUnits[x].modifyStatMod("guts",1,-4,4)
    else:
        python:
            xDmg = -(renpy.random.randint(2,4) + enemyUnits[0].cPower("occult") + int(numWisp*.5))
            for x in range(len(playerUnits)):
                playerUnits[x].modifyHP(xDmg,0.0,"brains")

        Narrator "The party is struck with a devestating gale that rocks them to their core!"
        python:
            ToggleBarState([1,2,3,4], 0)
            for x in range(len(playerUnits)):
                if playerUnits[x].isAlive:
                    playerUnits[x].InflictStatus(4)
    return

#Mysterious Claw: Physical Damage that lowers Guts + Brawn on Failure
label FIGHT_05B_MW_MISTWALKER_1:
    python:
        eName = enemyUnits[0].name
        pName = playerUnits[eTarget].name

    Narrator "[eName] slashes at [pName]!"

    call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("brawn"), "Mysterious Claw") from _call_dice_roll_62

    if isRollSuccess:
        Narrator "[pName] ducks out of the way!"
    else:
        python:
            xDmg = -(renpy.random.randint(2,4) + enemyUnits[0].cPower("brawn"))
            playerUnits[eTarget].modifyHP(xDmg,0.5,"guts")

        Narrator "[pName] is sliced with a flurry of shadowy claws for [sfxDmg] piercing damage!"

        python:
            playerUnits[eTarget].modifyStatMod("guts",-1,-4,4)
            playerUnits[eTarget].modifyStatMod("brains",-1,-4,4)
        # Narrator "[pName] is horrified!"
        # $playerUnits[eTarget].InflictStatus(4)
    return

#Clinging fog: lowers hustle, low damage (Guts roll, avoid hustle debuff). Spooks target on failure
label FIGHT_05B_MW_MISTWALKER_2:
    python:
        eName = enemyUnits[0].name
        pName = playerUnits[eTarget].name

        xDmg = -(renpy.random.randint(-1,1) + enemyUnits[0].cPower("occult") + numWisp)
        xDmg = limitValue(xDmg,-100,-1)
        playerUnits[eTarget].modifyHP(xDmg,0,"brains")

    Narrator "[pName] is frozen for [sfxDmg] damage!"
    $ToggleBarState([1,2,3,4], 0)

    call dice_roll(playerUnits[eTarget].cStats("guts"), enemyUnits[0].cDifficulty("occult"), "Clinging Fog") from _call_dice_roll_63

    if not isRollSuccess:
        if playerUnits[eTarget].status == 4:
            python:
                xDmg*=3
                playerUnits[eTarget].modifyHP(xDmg,0,"brains")

            Narrator "[pName] takes [sfxDmg] damage from amplified fear!"
        else:
            Narrator "[pName] is horrified!"
            $playerUnits[eTarget].InflictStatus(4)
    else:
        Narrator "[pName] remains grounded."
        call FIGHT_05B_MW_DESPOOK(eTarget) from _call_FIGHT_05B_MW_DESPOOK_21

    return

#Lights Out- Mistwalker does an an AoE that power is determined by number of Will-o-Wisps. Expends will o wisps
label FIGHT_05B_MW_MISTWALKER_3:
    python:
        xNum = avgUnitStat(playerUnits,"brains")
    show Flickering Black
    camera screens:
        matrixcolor SaturationMatrix(1)
        pause 0.6
        matrixcolor SaturationMatrix(0)
    Narrator "[eName] cuts the lights!"

    call dice_roll(xNum, enemyUnits[0].cDifficulty("occult"), "Lights Out") from _call_dice_roll_64

    python:
        eName = enemyUnits[0].name
        pName = playerUnits[eTarget].name
        xDmg = -int(enemyUnits[0].cPower("occult") + int(numWisp*2.25))

    if isRollSuccess:
        $xDmg = int(xDmg*0.5)
        camera screens:
            matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(0)
            ease 0.1 matrixcolor ColorizeMatrix("#300606","#ff1c1c")*SaturationMatrix(0)
            ease 0.3 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(0)
    else:
        camera screens:
            matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(0)
            ease 0.1 matrixcolor ColorizeMatrix("#300606","#ff1c1c")*SaturationMatrix(0)
            pause 0.5
            ease 0.3 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(0)

    python:
        for x in range(len(playerUnits)):
            playerUnits[x].modifyHP(xDmg,0.0,"brains")

    Narrator "Spectral hands shove painful memories to the forefront of your mind!"

    Narrator "With a sharp breath, Oz wipes his eyes."

    $ToggleBarState([1,2,3,4], 0)
    camera screens:
        matrixcolor SaturationMatrix(1)
    hide Flickering Black
    call FIGHT_05B_MW_SETWISPS(0) from _call_FIGHT_05B_MW_SETWISPS_1
    with { "master" : Dissolve(0.5) }
    Narrator "The wisps fade."
    return

label FIGHT_05B_MW_SETWISPS(xWisps=0):
    if numWisp < xWisps:
        show mw_lantern glow
        python:
            for x in range(xWisps):
                if numWisp <= x:
                    renpy.show(name="willowisp"+str(x+1),at_list=[wispPos(x+1,xWisps),WispEnter])
                elif numWisp > x:
                    renpy.show(name="willowisp"+str(x+1),at_list=[wispPosEase(x+1,xWisps)])

    elif numWisp > xWisps:
        python:
            for x in reversed(range(5)):
                if x+1 > xWisps:
                    renpy.hide("willowisp" + str(x+1))
                else:
                    break

    $numWisp = xWisps
    return

#Cures Spooked Status
label FIGHT_05B_MW_DESPOOK(pDex=0):
    if playerUnits[pDex].status == 4:
        python:
            pName = playerUnits[pDex].name
            playerUnits[pDex].CureStatus(True)
        Narrator "[pName] finds their courage."
    return

# -------------------------------------------------------------------(0) LANTERN
label FIGHT_05B_MW_LANTERN_ATTACK:

    python:
        CheckForGameOvers()
        HighlightEnemyUnitBars([1])

    play sfx boss_target_sfx

    #Summons a will-o-wisp. If has 3+, uses CA2 to heal. If at Max, boosts MW difficulty. Auto heals mistwalker as a bonus on CA1

    if currentCA == 1 and numWisp < 5:
        call FIGHT_05B_MW_LANTERN_0 from _call_FIGHT_05B_MW_LANTERN_0
    elif numWisp == 5:
        if not enemyUnits[0].isAlive:
            call FIGHT_05B_MW_LANTERN_2 from _call_FIGHT_05B_MW_LANTERN_2
        elif enemyUnits[1].isBloodied() and enemyUnits[1].stats["gutsMod"] > -4:
            call FIGHT_05B_MW_LANTERN_1 from _call_FIGHT_05B_MW_LANTERN_1
        if renpy.random.choice([True,False]):
            call FIGHT_05B_MW_LANTERN_3 from _call_FIGHT_05B_MW_LANTERN_3
        else:
            call FIGHT_05B_MW_LANTERN_2B from _call_FIGHT_05B_MW_LANTERN_2B

    else:
        if not enemyUnits[0].isAlive:
            call FIGHT_05B_MW_LANTERN_2 from _call_FIGHT_05B_MW_LANTERN_2_1
        elif enemyUnits[1].isBloodied() and enemyUnits[1].stats["gutsMod"] > -4:
            call FIGHT_05B_MW_LANTERN_1 from _call_FIGHT_05B_MW_LANTERN_1_1
        else:
            call FIGHT_05B_MW_LANTERN_0 from _call_FIGHT_05B_MW_LANTERN_0_1

    jump expression currentLabelPT

#Summon Will-o-wisp (Max: 5)
label FIGHT_05B_MW_LANTERN_0:
    python:
        eName = enemyUnits[1].name

    call FIGHT_05B_MW_SETWISPS(limitValue(numWisp+1,0,5)) from _call_FIGHT_05B_MW_SETWISPS_2
    Narrator "[eName] summons a [wowName]."

    return

#Unstable
label FIGHT_05B_MW_LANTERN_1:
    call FIGHT_05B_MW_SETWISPS(limitValue(numWisp-1,0,5)) from _call_FIGHT_05B_MW_SETWISPS_3
    Narrator "[eName]'s light seeps through the cracks!"
    python:
        enemyUnits[1].modifyStatMod("guts",-2,-4,4)
        enemyUnits[1].modifyStatMod("occult",-2,-4,4)
        enemyUnits[0].modifyStatMod("power",2,-4,4)

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_22
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_23
    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_24
    return

#Heal Mistwalker
label FIGHT_05B_MW_LANTERN_2:

    if numWisp > 0:
        python:
            HighlightEnemyUnitBars([0,1])
            xHeal = (numWisp*5)
            enemyUnits[0].modifyHP(xHeal+renpy.random.randint(0,3),0.0,"guts")
            eName = enemyUnits[1].name
            e2Name = enemyUnits[0].name

    call FIGHT_05B_MW_SETWISPS(limitValue(numWisp-3,0,5)) from _call_FIGHT_05B_MW_SETWISPS_4
    Narrator "[eName] uses the [wowName]s to heal [e2Name] for [xHeal] [kwHealth]!"

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK_25
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_26
    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_27
    return

#Heal Mistwalker
label FIGHT_05B_MW_LANTERN_2B:
    if numWisp > 0:
        python:
            HighlightEnemyUnitBars([0,1])
            xHeal = (numWisp*2)
            enemyUnits[0].modifyHP(xHeal+renpy.random.randint(0,3),0.0,"guts")
            eName = enemyUnits[1].name
            e2Name = enemyUnits[0].name


    Narrator "[eName] uses the [wowName]s to heal [e2Name] for [xHeal] [kwHealth]!"
    return

#Boost Mistwalker Diff
label FIGHT_05B_MW_LANTERN_3:
    python:
        eName = enemyUnits[1].name
        e2Name = enemyUnits[0].name

    call FIGHT_05B_MW_SETWISPS(limitValue(numWisp-1,0,5)) from _call_FIGHT_05B_MW_SETWISPS_5
    Narrator "[eName] glows, casting an eerie light over [e2Name]."

    $enemyUnits[0].modifyStatMod("diff",3,-4,4)
    return
