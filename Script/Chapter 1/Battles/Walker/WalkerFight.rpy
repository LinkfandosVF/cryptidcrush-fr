default mist_turncount = 0
default mist_phase2 = False

label FIGHT_05_MISTWALKER:
    $curBattleNum = 5
    call battleTransition from _call_battleTransition_6
    camera:
        camera_zoom()
    $mist_phase2 = False
    pause 0.1

    #Scene
    scene BG Graveyard Night:
        matrixcolor SaturationMatrix(0.3)*BrightnessMatrix(-0.05)*ColorizeMatrix("#000000","#ffffff")

        choice:
            pause 1.0
        choice:
            pause 3.0
        choice:
            ease 0.4 matrixcolor SaturationMatrix(0.3)*BrightnessMatrix(-0.05)*ColorizeMatrix("#18110a","#ffd028")
            ease 0.4 matrixcolor SaturationMatrix(0.3)*BrightnessMatrix(-0.05)*ColorizeMatrix("#000000","#ffffff")

        repeat

    show MrWalker base at WalkerEnter, WalkerPos
    show mw_lantern default

    #Music
    python:
        songText = "Old Gods"
        musicNote = 7
        enemiesActed = []
        timeText = "Save Mike"

    play music wrath_of_the_old_gods_song_bearsome

    #Mistwalker
    python:
        MW_Stats = Unit("{color=#f0bf6c}Mr. Walker{/color}",3,-2,1,-2,-1,2,16)
        MW_Stats.baseDiff = 6

        MW_Stats.SetMaxMTA(3)
        MW_Stats.SetNOCA(3)
        MW_Stats.SetEnemyAttackLabel("FIGHT_05_MW_MISTWALKER_ATTACK")
        MW_Stats.SetMTA(3)#3

        numWisp = 0

    #Lantern
    python:
        LA_Stats = Unit("{color=#8bf8ff}Lantern{/color}",-2,2,-2,3,-2,3,55)
        LA_Stats.baseDiff = 7

        LA_Stats.SetMaxMTA(5)
        LA_Stats.SetNOCA(3)
        LA_Stats.SetEnemyAttackLabel("FIGHT_05_MW_LANTERN_ATTACK")
        LA_Stats.SetMTA(1)#1

    # ------------------------------------------------------------- Player Setup

    python:
        #Robyn
        PC_Stats = RobynUnit()
        PC_Stats.updateStats()

        tPCAttacks = ["Bash", "Focus", "Sleight of Crowbar", "Flex", "Cheer", "Healing Sprite"]
        override = []
        PCAttacks = []

        for x in range(6):
            if pcBaseStats[x] > 0:
                PCAttacks.append(tPCAttacks[x])
                override.append(x)

                if len(override) >= 3:
                    break

        PCAttacks.append("Kazap")
        override.append(6)

        PC_Stats.SetAttackMoves(PCAttacks, "FIGHT_05_MW_ROBYN_", override)

        #Wolf Gus
        Gus_Stats = GusUnit()
        Gus_Stats.SetIcon("wolfGusIcon")
        Gus_Stats.SetAttackMoves(['Onslaught','Howl', 'Bite Back', 'Sniff'], 'FIGHT_05_MW_GUS_')

        #Oz
        Oz_Stats = OzUnit()
        Oz_Stats.SetAttackMoves(['Silver Stab', 'Glare', 'Gut Punch', 'Bandage Wounds'], 'FIGHT_05_MW_OZ_')

    #UnitSetup
    python:
        currentLabelPT = "FIGHT_05_MISTWALKER_PT"
        currentLabelET = "FIGHT_05_MISTWALKER_ET"


        playerUnitsInit("PC","Gus","Oz")
        enemyUnitsInit("MW","LA")

        InitializeCombatUI(playerUnits, enemyUnits)

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])
        resetUnitStates("mist_turncount")

    Narrator "[MW_Stats.name] appears!"

    call FIGHT_05_MISTWALKER_WOLF from _call_FIGHT_05_MISTWALKER_WOLF
    $HighlightEnemyUnitBars([])

    jump FIGHT_05_MISTWALKER_ET

label FIGHT_05_MISTWALKER_PT:
    camera at camera_default
    show MrWalker base at WalkerPos
    show mw_lantern default
    python:
        PlayerTurnStart()
        mist_turncount+=1
    python:
        #Random Idle Lines
        xStr = "The cryptids look to you for guidance."
        xIdle = []

        #Robyn
        if playerUnits[0].isAlive:
            xIdle.append("You brace yourself for the worst.")
            xIdle.append("Madhouse is in there somewhere. He's got to be.")
            for x in [1,2]:
                if playerUnits[x].isAlive:
                    xIdle.append("You look to " + playerUnits[x].name + " nervously.")
        #Gus
        if playerUnits[1].isAlive:
            xIdle.append("August wants to bite.")
            xIdle.append("August wants to scratch.")
            xIdle.append("August wants to tear Oz apart.")

            if playerUnits[2].isAlive:
                xIdle.append("August looks at OZ.")

        #Oz
        if playerUnits[2].isAlive:
            xIdle.append("Oz glances up at the moon.")

            if playerUnits[1].isAlive:
                xIdle.append("Oz looks at August.")
                xIdle.append("Oz wants to bite August.")

        xStr = renpy.random.choice(xIdle)
        xNum = CheckLowestHP(False)

        if playerUnits[xNum].cHP <= 5:
            xStr = playerUnits[xNum].name + " is hurting."


    Narrator "[xStr]"

    python:
        toggleQuickMenu()

    hide screen quicker_menu
    show screen turnCounter(mist_turncount)

    python:
        CombatUnitPick()
        ui.interact()

label FIGHT_05_MISTWALKER_ET:
    camera at camera_default

    if mist_phase2 == False and enemyUnits[1].isBloodied():
        call FIGHT_05_MISTWALKER_P2 from _call_FIGHT_05_MISTWALKER_P2

    python:
        EnemyTurnStart()

    if enemyUnits[1].cHP <= 0:
        python:

            mm_rank = calcRank(mist_turncount,50,35,25,15,10)

        Narrator "Turn Count: [mist_turncount] Rank: [mm_rank]"

        $persistent.unlockedDice[5] = True
        Narrator "You've unlocked the Full Moon Duet dice! You can equip them at any time through the quick menu."

        return

    jump FIGHT_05_MISTWALKER_PT

label FIGHT_05_MISTWALKER_WOLF:

    August "What is that thing?!"

    Walker "Why, you're rather rude. Not that it matters now."

    Walker "You'll all be gone by morning."

    Narrator "Oz hisses through clenched teeth."

    August "H-hey,, that lantern's givin' me the creeps. It reeks."

    $HighlightEnemyUnitBars([1])
    Narrator "Oz lunges, darting to the side before bashing the hilt of his dagger against the lantern."


    call dice_roll(playerUnits[2].cStats("brawn"), enemyUnits[1].cDifficulty("hustle"), "Silver Stab") from _call_dice_roll_54

    python:
        targetChoice = 1
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
        call FIGHT_05_MW_MISTWALKER_HURT(targetChoice) from _call_FIGHT_05_MW_MISTWALKER_HURT_6

        python:
            xDmg = -limitValue(int(round(renpy.random.randint(-3,-1) + playerUnits[2].cPower("brains") + enemyUnits[targetChoice].cStats("occult")*2)),1,100)
            enemyUnits[targetChoice].modifyHP(xDmg,xPierce,"guts")

        Narrator "[xVar]\n\n[pName] stabs [eName] for [sfxDmg] damage!\nAnd flicks shadowy threads off the tip of his blade."
    else:
        Narrator "Oz shakes his head, his attack barely left a scratch."

    $ToggleBarState([1,2,3,4], 0)
    Narrator "Oz looks to you for further instruction.{nw}"

    menu:
        extend ""

        "Hit him with a magic blast?":

            Narrator "Oz gestures to the lantern's HP block and its high [kwDefenseMod]."

            August "If we had something that'd lower their [kwGuts]..."

            Robyn "Then we lower [kwBrains] to make magic attacks more effective, right?"

            August "Jeez, you sound like Atlas."

        "Lower its defense!":
            Robyn "Lower [kwGuts] to lower physical defense, and lower [kwBrains] to lower supernatural defense.\n\n Go get 'em!"

    Walker "I'm in no rush..."

    Narrator "Madhouse is tethered to your phone right? What if you tried calling him back?"

    call dice_roll(playerUnits[0].cStats("occult"), 7, "Kazap") from _call_dice_roll_55

    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name

        xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("occult"))
        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")
        pcS = "s"
        if PCThey == "They":
            pcS = ""

    Narrator "[pName] angles [PCtheir] phone at the [eName] and a wild bolt of green lightning spikes through the air, dealing [sfxDmg] damage!"

    python:
        if isRollSuccess:
            enemyUnits[targetChoice].modifyStatMod("brawn",-2,-4,4)
            enemyUnits[targetChoice].modifyStatMod("brains",-2,-4,4)

    Robyn "{sc}Aaaie!{/sc}"

    Narrator "The shadow laughs and tips his hat."

    Walker "Rather impatient are we? I don't mind. \n\n{bt=2}Now,, why don't you go first?{/bt}"

    Narrator "It's time to put your new abilities to the test. \n\n{sc=2}You miss Taro.{/sc}"

    $HighlightEnemyUnitBars([0])
    return

label FIGHT_05_MISTWALKER_P2:
    $mist_phase2 = True

    call FIGHT_05_MW_SETWISPS(limitValue(numWisp-2,0,5)) from _call_FIGHT_05_MW_SETWISPS_5
    Narrator "The lantern begins to fracture, and [wowName]s seep through the cracks!"

    Walker "Oh dear, now this is rather irritating."

    python:
        enemyUnits[1].modifyStatMod("guts",-8,-4,4)
        enemyUnits[1].modifyStatMod("occult",-8,-4,4)
        enemyUnits[0].modifyStatMod("power",2,-4,4)

    call FIGHT_05_MW_DESPOOK(0) from _call_FIGHT_05_MW_DESPOOK_24
    call FIGHT_05_MW_DESPOOK(1) from _call_FIGHT_05_MW_DESPOOK_25
    call FIGHT_05_MW_DESPOOK(2) from _call_FIGHT_05_MW_DESPOOK_26
    return
