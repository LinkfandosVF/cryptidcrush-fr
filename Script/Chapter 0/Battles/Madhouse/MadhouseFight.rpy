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
        PC_Stats.SetAttackMoves(['Frapper', 'Encourager', 'Focus', 'Coeur ouvert'], 'FIGHT_01_MM_ROBYN_')

        #Jamie Setup
        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Esprit brasier', 'Pète crâne', 'Vague Dia'], 'FIGHT_01_MM_JAMIE_')

        #Taro Setup
        Taro_Stats = TaroUnit()
        Taro_Stats.SetAttackMoves(['Bourrer', 'Défense Tuna', 'Rayer'], 'FIGHT_01_MM_TARO_')

        usedKinesis = False
        Atlas_Stats = AtlasUnit()
        Atlas_Stats.SetAttackMoves(['Étalage de lore', 'Kinesis α', 'Bon Mindset'], 'FIGHT_01_MM_ATLAS_')

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
        xStr = "C'est l'heure d'attaquer."
        xIdle = []

        #Robyn
        if playerUnits[0].isAlive:
            xIdle.append("Tu te prépare au pire.")
            xIdle.append("Tu éssaie de suivre le moment. Ca fait beaucoup à encasser d'un coup.")

        #Atlas
        if playerUnits[1].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("Tu regarde Atlas nerveusement.")

            xIdle.append("Atlas regarde dans le vide.")
            xIdle.append("Atlas Crache plus d'éctoplasme.")
            xIdle.append("Atlas pense à avoir un familier corbeau.")

        #Jamie
        if playerUnits[2].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("Tu regarde Jamie nerveusement.")

            if playerUnits[1].isAlive:
                xIdle.append("Jamie ajuste sa posture, sa queue bouge sur le sol.")
                xIdle.append("Jamie éssaie de se retenir pour Atlas.")
            else:
                xIdle.append("Jamie en à plus qu'assez de bidouiller.")

        #Taro
        if playerUnits[3].isAlive:
            if playerUnits[0].isAlive:
                xIdle.append("Tu regarde Taro nerveusement.")

            xIdle.append("Taro baille et lèche ses pattes.")
            xIdle.append("Taro est prète à déchiqueter Madhouse.")

        xStr = renpy.random.choice(xIdle)
        if playerUnits[CheckLowestHP(False)].cHP <= 5:
            xStr = playerUnits[CheckLowestHP(False)].name + " pourrait avoir un peu d'aide."


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

    Atlas "Je pensais que tu aimait travailler içi, mais c'est complètement faux! Tu déteste ton travail!"

    Madhouse "Sort de ton monde des bisounours. \n\n{size=30}TU NE ME CONNAIS PAS!{/size}"

    Atlas "Je sais que tu est sur la route de l'{i}éradication!{/i}"

    Narrator "Un sourire triste se penche du coté de Madhouse alors qu'il se dit a lui même."

    Madhouse "T'avais vu mon avenir là bas, n'est-ce pas?"

    Atlas "H-hein? Nan! Je peux pas!"

    Madhouse "{size=30}T'es vraiment qu'un putain de mauvais menteur!{/size}"

    Atlas "Si tu continue tu vas mourir! Genre {i}Crèver{/i}, crèver!"

    Madhouse "{size=35}TOUT LE MONDE S'EN FOUT!{/size}"
    jump FIGHT_01_MADHOUSE_ET2

label Fight_01_MADHOUSE_END:
    $mm_rank = calcRank(mm_turncount,50,35,25,15,10)

    Narrator "Turn Count: [mm_turncount] Rank: [mm_rank]"

    if False in persistent.unlockedDice[3:5]:
        $persistent.unlockedDice[2] = True
        $persistent.unlockedDice[3] = True
        $persistent.unlockedDice[4] = True

    Narrator "T'a choppé un nouveau dé. Tu peux le changer dans le menu. (le = sur la gauche) quand tu veux! Juste pas quand tu joue un dé."

    Narrator "Va voir le Mothman pour des explications détaillées de leurs effets."
    

    return
