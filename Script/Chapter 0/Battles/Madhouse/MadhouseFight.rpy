default mm_turncount = 0
#S Rank: 20
#A Rank: 25
#B Rank: 30
#C Rank: 35
#D Rank: 40+

label FIGHT_01_MADHOUSE:
    $curBattleNum = 1
    call battleTransition from _call_battleTransition_3

    play music supernatural_foe_intro_song
    queue music supernatural_foe_loop_song

    scene BG Studio Room Spookier2:
        matrixcolor TintMatrix("#adffcc")*SaturationMatrix(1.1)*BrightnessMatrix(-0.1)

    python:
        enemiesActed = []

        musicNote = 7
        songText = "Supernatural Foe"

        #Enemy Setup
        MM_Stats = Unit("{color=#3bec27}Madhouse{/color}",2,0,1,0,1,2,60)
        MM_Stats.baseDiff = 6
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(2) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_01_MM_MM_ATTACK")
        MM_Stats.SetMTA(3)

        #Robyn Setup
        PC_Stats = RobynUnit()
        PC_Stats.SetAttackMoves(['Bash', 'Cheer', 'Focus', 'Heart Out'], 'FIGHT_01_MM_ROBYN_')

        #Jamie Setup
        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave'], 'FIGHT_01_MM_JAMIE_')

        #Taro Setup
        Taro_Stats = TaroUnit()
        Taro_Stats.SetAttackMoves(['Pounce', 'Tuna Defender', 'Jeer'], 'FIGHT_01_MM_TARO_')

        usedKinesis = False
        Atlas_Stats = AtlasUnit()
        Atlas_Stats.SetAttackMoves(['Lore Dump', 'Kinesis', 'Pump Up'], 'FIGHT_01_MM_ATLAS_')

    python:
        #Puts the party into the Bar
        playerUnitsInit("PC","Atlas","Jamie","Taro")
        enemyUnitsInit("MM")
        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "FIGHT_01_MADHOUSE_PT"
        currentLabelET = "FIGHT_01_MADHOUSE_ET"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])
        eName = enemyUnits[0].name

        resetUnitStates("mm_turncount")

    show demon_madhouse at MMD_Entry_Pos
    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    with Dissolve(0.5)
    Narrator "[eName] gets an encore!"

    show demon_madhouse at MMD_Default_Pos
    show MMFight_Chair at MMFight_LeftProp_Pos
    show MMFight_Speaker at MMFight_RightProp_Pos

    $HighlightEnemyUnitBars([])
    jump FIGHT_01_MADHOUSE_ET

label FIGHT_01_MADHOUSE_PT:
    camera at camera_default

    python:
        PlayerTurnStart()
        mm_turncount+=1



    python:
        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 0

    #Random Lines
    python:
        #Random Idle Lines
        xStr = "The party is ready to fight."
        xIdle = []

        #Robyn
        if playerUnits[0].isAlive:
            xIdle.append("You brace yourself for the worst.")
            xIdle.append("You try getting a grip on the situation. It’s a lot to process.")

        #Atlas
        if playerUnits[1].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Atlas nervously.")

            xIdle.append("Atlas stares off into space.")
            xIdle.append("Atlas coughs up more ectoplasm.")
            xIdle.append("Atlas daydreams about having a raven familiar.")

        #Jamie
        if playerUnits[2].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Jamie nervously.")

            if playerUnits[1].isAlive:
                xIdle.append("Jamie shifts their weight, their tail swishing in time.")
                xIdle.append("Jamie’s trying to hold back for Atlas’ sake.")
            else:
                xIdle.append("Jamie is done messing around.")

        #Taro
        if playerUnits[3].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("You look to Taro nervously.")

            xIdle.append("Taro yawns and combs her whiskers.")
            xIdle.append("Taro is ready and raring to tear into this dude.")

        xStr = renpy.random.choice(xIdle)
        if playerUnits[CheckLowestHP(False)].cHP <= 5:
            xStr = playerUnits[CheckLowestHP(False)].name + " could use some help."


    Narrator "[xStr]"

    $toggleQuickMenu()
    hide screen quicker_menu

    show screen turnCounter(mm_turncount)

    python:
        CombatUnitPick()
        ui.interact()


    return

label FIGHT_01_MADHOUSE_ET:
    camera at camera_default

    python:
        EnemyTurnStart()

        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 0

    if enemyUnits[0].cHP <= 35:
        jump FIGHT_01_MADEHOUSE_P2START

    jump FIGHT_01_MADHOUSE_PT

label FIGHT_01_MADHOUSE_ET2:
    camera at camera_default
    python:
        EnemyTurnStart()

        #Reset Demon Madhouse Expression
        MMD_State["hurt"] = False
        MMD_State["glitch"] = 2
        MMD_State["frenzy"] = True

    if enemyUnits[0].cHP <= 0:
        jump Fight_01_MADHOUSE_END

    jump FIGHT_01_MADHOUSE_PT

label FIGHT_01_MADEHOUSE_P2START:
    camera at camera_default
    python:
        ToggleBarState([1,2,3,4], 0)

        currentLabelET = "FIGHT_01_MADHOUSE_ET2"

        enemyUnits[0].SetMTA(1)
        enemyUnits[0].baseDiff = 7

        if not enemyUnits[0].isAlive:
            enemyUnits[0].modifyHP(1,1.0,"guts")

    Atlas "I wanted to believe you loved it here, working your dream job, but now I know that was a total lie!"

    Madhouse "Get over yourself. \n\n{size=30}You don't know me!{/size}"

    Atlas "I know you're on the road to {i}eradication!{/i}"

    Narrator "A crooked grin peels across the demon’s face as he giggles to himself."

    Madhouse "You saw my future back there, didn't you?"

    Atlas "H-huh? No- I can't! I didn't!"

    Madhouse "{size=30}You're one shitty liar!{/size}"

    Atlas "If you keep this up, you’re going to die, like {i}die{/i}, die!"

    Madhouse "{size=35}No one cares!!{/size}"
    jump FIGHT_01_MADHOUSE_ET2

label Fight_01_MADHOUSE_END:
    $mm_rank = calcRank(mm_turncount,50,35,25,15,10)

    Narrator "Turn Count: [mm_turncount] Rank: [mm_rank]"

    if False in persistent.unlockedDice[3:5]:
        $persistent.unlockedDice[2] = True
        $persistent.unlockedDice[3] = True
        $persistent.unlockedDice[4] = True

    Narrator "You've unlocked some new dice! You can equip them through the quick menu (the = on the left) at any time! Just not while rolling."

    Narrator "Future updates will include more in depth explanations on the differences between dice sets, but the main thing you'll want to keep in mind is that dice sets change how much karma you have to work with, and the numbers you typically roll."
    

    return
