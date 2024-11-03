
label FIGHT_05B_MISTWALKER:
    $curBattleNum = 5
    call battleTransition from _call_battleTransition_7
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
        MW_Stats = Unit("{color=#f0bf6c}Mr. Walker{/color}",4,-2,2,-2,-1,3,20)
        MW_Stats.baseDiff = 6

        MW_Stats.SetMaxMTA(3)
        MW_Stats.SetNOCA(3)
        MW_Stats.SetEnemyAttackLabel("FIGHT_05B_MW_MISTWALKER_ATTACK")
        MW_Stats.SetMTA(3)#3

        numWisp = 0

    #Lantern
    python:
        LA_Stats = Unit("{color=#8bf8ff}Lantern{/color}",-1,2,-1,3,-2,4,80)
        LA_Stats.baseDiff = 8

        LA_Stats.SetMaxMTA(3)
        LA_Stats.SetNOCA(3)
        LA_Stats.SetEnemyAttackLabel("FIGHT_05B_MW_LANTERN_ATTACK")
        LA_Stats.SetMTA(2)#1

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

        PC_Stats.SetAttackMoves(PCAttacks, "FIGHT_05B_MW_ROBYN_", override)

        #Wolf Gus
        Gus_Stats = GusUnit()
        Gus_Stats.SetIcon("wolfGusIcon")
        Gus_Stats.SetAttackMoves(['Onslaught','Howl', 'Bite Back', 'Sniff'], 'FIGHT_05B_MW_GUS_')

        #Oz
        Oz_Stats = OzUnit()
        Oz_Stats.SetAttackMoves(['Silver Stab', 'Glare', 'Gut Punch', 'Bandage Wounds'], 'FIGHT_05B_MW_OZ_')

        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave','ChainFlare'], 'FIGHT_05B_MW_JAMIE_')

    #UnitSetup
    python:
        currentLabelPT = "FIGHT_05B_MISTWALKER_PT"
        currentLabelET = "FIGHT_05B_MISTWALKER_ET"


        playerUnitsInit("PC","Gus","Oz","Jamie")
        enemyUnitsInit("MW","LA")

        InitializeCombatUI(playerUnits, enemyUnits)

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])
        resetUnitStates("mist_turncount")

    Narrator "[MW_Stats.name] wants a rematch!"

    $HighlightEnemyUnitBars([])

    jump FIGHT_05B_MISTWALKER_ET

label FIGHT_05B_MISTWALKER_PT:
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

label FIGHT_05B_MISTWALKER_ET:
    camera at camera_default

    if mist_phase2 == False and enemyUnits[1].isBloodied():
        call FIGHT_05B_MISTWALKER_P2 from _call_FIGHT_05B_MISTWALKER_P2

    python:
        EnemyTurnStart()

    if enemyUnits[1].cHP <= 0:
        python:
            mm_rank = calcRank(mist_turncount,40,30,25,20,15)

        Narrator "Turn Count: [mist_turncount] Rank: [mm_rank]"
        return

    jump FIGHT_05B_MISTWALKER_PT


label FIGHT_05B_MISTWALKER_P2:
    $mist_phase2 = True

    call FIGHT_05B_MW_SETWISPS(limitValue(numWisp-2,0,5)) from _call_FIGHT_05B_MW_SETWISPS
    Narrator "The lantern begins to fracture, and [wowName]s seep through the cracks!"

    Walker "Oh dear, now this is rather irritating."

    python:
        enemyUnits[1].modifyStatMod("guts",-8,-4,4)
        enemyUnits[1].modifyStatMod("occult",-8,-4,4)
        enemyUnits[0].modifyStatMod("power",2,-4,4)

    call FIGHT_05B_MW_DESPOOK(0) from _call_FIGHT_05B_MW_DESPOOK
    call FIGHT_05B_MW_DESPOOK(1) from _call_FIGHT_05B_MW_DESPOOK_1
    call FIGHT_05B_MW_DESPOOK(2) from _call_FIGHT_05B_MW_DESPOOK_2
    return
