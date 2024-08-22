default mmb_turncount = 0
#A Rank: 25
#B Rank: 35
#C Rank: 50
#D Rank: 51+

label FIGHT_01B_MADHOUSE:
    call battleTransition from _call_battleTransition_4

    play music urgently_jammin_sir_meow_remix_intro
    queue music urgently_jammin_sir_meow_remix_loop

    scene BG Studio Room Spookier2:
        matrixcolor HueMatrix(190)*SaturationMatrix(1.3)*BrightnessMatrix(-0.3)

    python:
        musicNote = 7
        songText = "Urgently Jammin (Sir Meow Remix)"

        #Enemy Setup
        MM_Stats = Unit("{color=#ed58ff}Gladhouse{/color}",2,-1,1,0,1,2,99)
        MM_Stats.baseDiff = 6
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(4) ##This is previously known as eDelay
        MM_Stats.SetNOCA(3) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01B_MM_MM_ATTACK")
        MM_Stats.SetMTA(2)

        enemyUnits = []
        enemyUnits.append(MM_Stats)

        #Robyn Setup
        PC_Stats.updateStats()
        PC_Stats.SetAttackMoves(['Bash', 'Cheer', 'Focus', 'Heart Out'], 'FIGHT_01B_MM_ROBYN_')

        #Jamie Setup
        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave'], 'FIGHT_01B_MM_JAMIE_')

        Taro_Stats = TaroUnit()
        Taro_Stats.SetAttackMoves(['Pounce', 'Tuna Defender', 'Jeer'], 'FIGHT_01B_MM_TARO_')

        Atlas_Stats = AtlasUnit()
        Atlas_Stats.SetAttackMoves(['Lore Dump', 'Kinesis', 'Pump Up'], 'FIGHT_01B_MM_ATLAS_')

        #Puts the party into the Bar
        playerUnitsInit("PC","Atlas","Jamie","Taro")
        enemyUnitsInit("MM")
        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "FIGHT_01B_MADHOUSE_PT"
        currentLabelET = "FIGHT_01B_MADHOUSE_ET"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])
        eName = enemyUnits[0].name

        resetUnitStates("mmb_turncount")

    show demon_madhouse at MMD_Entry_Pos:
        matrixcolor HueMatrix(180)
    show MMFight_Chair at MMFight_LeftProp_Entry:
        matrixcolor HueMatrix(180)
    show MMFight_Speaker at MMFight_RightProp_Entry:
        matrixcolor HueMatrix(180)

    with Dissolve(0.5)

    Narrator "[eName] gets {i}another{/i} encore!"

    show demon_madhouse at MMD_Default_Pos
    show MMFight_Chair at MMFight_LeftProp_Pos
    show MMFight_Speaker at MMFight_RightProp_Pos

    $HighlightEnemyUnitBars([])
    jump FIGHT_01B_MADHOUSE_ET

label FIGHT_01B_MADHOUSE_PT:
    camera at camera_default

    python:
        PlayerTurnStart()
        mmb_turncount+=1

        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 0

        #Random Idle Lines
        xStr = "The party is ready to fight."
        xIdle = []

        #Robyn
        if playerUnits[0].isAlive:
            xIdle.append("You try getting a grip on the situation. It’s a lot to process.")
            xIdle.append("You brace yourself for the worst.")
            xIdle.append("You try getting a grip on the situation. It’s a lot to process.")

        #Atlas
        if playerUnits[1].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Atlas nervously.")

            xIdle.append("Atlas stares off into space.")
            xIdle.append("Atlas coughs up more ectoplasm.")
            xIdle.append("Atlas daydreams about having a raven familiar.")
            xIdle.append("Atlas REALLY wants to steal Mike’s hat.")

        #Jamie
        if playerUnits[2].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Jamie nervously.")

            if playerUnits[1].isAlive:
                xIdle.append("Jamie reaches up and pats the wisp atop their head.")
                xIdle.append("Jamie shifts their weight, their tail swishing in time.")
                xIdle.append("Jamie’s trying to hold back for Atlas’ sake.")
            else:
                xIdle.append("Jamie is done messing around.")
                xIdle.append("Jamie exhales a gout of steam.")

        #Taro
        if playerUnits[3].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Taro nervously.")

            xIdle.append("Taro slams her belly.")
            xIdle.append("Taro daydreams about ghost sushi.")
            xIdle.append("Taro is ready and raring to get this over with.")
            xIdle.append("Taro demands attention. Stat.")

        xStr = renpy.random.choice(xIdle)
        if playerUnits[CheckLowestHP(False)].cHP <= 5:
            xStr = playerUnits[CheckLowestHP(False)].name + " could use some help."

    Narrator "[xStr]"

    $toggleQuickMenu()
    hide screen quicker_menu

    show screen turnCounter(mmb_turncount)
    python:
        CombatUnitPick()
        ui.interact()


    return

label FIGHT_01B_MADHOUSE_ET:
    camera at camera_default
    python:
        EnemyTurnStart()

        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 0


    if enemyUnits[0].cHP <= 40:
        jump FIGHT_01B_MADHOUSE_P2START

    jump FIGHT_01B_MADHOUSE_PT

label FIGHT_01B_MADHOUSE_ET2:
    camera at camera_default
    python:
        EnemyTurnStart()

        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 2
        MMD_State["frenzy"] = True

    if enemyUnits[0].cHP <= 0:
        jump Fight_01B_MADHOUSE_END

    jump FIGHT_01B_MADHOUSE_PT

label FIGHT_01B_MADHOUSE_P2START:
    camera at camera_default
    python:
        ToggleBarState([1,2,3,4], 0)
        currentLabelET = "FIGHT_01B_MADHOUSE_ET2"
        enemyUnits[0].SetMaxMTA(3)
        enemyUnits[0].baseDiff = 7

        if not enemyUnits[0].isAlive:
            enemyUnits[0].modifyHP(1,1.0,"guts")

    Narrator "Madhouse decides to kick it up a notch!"

    jump FIGHT_01B_MADHOUSE_ET2

label Fight_01B_MADHOUSE_END:
    $mm_rank = calcRank(mmb_turncount,40,30,25,20,15)

    Narrator "Turn Count: [mmb_turncount] Rank: [mm_rank]"
    return
