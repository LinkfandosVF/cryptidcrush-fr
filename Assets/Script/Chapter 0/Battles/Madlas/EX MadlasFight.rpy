default mD_turncount = 0

label FIGHT_00B_MADLAS:
    call battleTransition from _call_battleTransition_5

    play music urgently_jammin_sir_meow_remix_intro
    queue music urgently_jammin_sir_meow_remix_loop

    scene BG Studio Room Spookier2:
        matrixcolor HueMatrix(190)*SaturationMatrix(1.3)*BrightnessMatrix(-0.3)

    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    show madlas:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.545 xcenter 0.5 matrixtransform RotateMatrix(0,0,0)
        block:
            yoffset -10
            parallel:
                ease 0.2725 yoffset 0
                pause 0.2725
                yoffset -10
                ease 0.2725 yoffset 0
                pause 0.2725
            parallel:
                pause 0.545
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,360,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,180,0)
                choice:
                    ease 0.545 matrixtransform RotateMatrix(0,0,0)

            repeat

    python:
        musicNote = 7
        songText = "Urgently Jammin (Sir Meow Remix)"

        MM_Stats = Unit("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}",1,1,2,0,1,1,40)
        MM_Stats.baseDiff = 7
        MM_Stats.SetIcon("dIcon1")
        MM_Stats.SetMaxMTA(3) ##This is previously known as eDelay
        MM_Stats.SetNOCA(3) ##Enemy Unit attacks 2 times when its their turn.
        MM_Stats.SetEnemyAttackLabel("FIGHT_00B_MADLAS_MD_ATTACK")
        MM_Stats.SetMTA(1)

        PC_Stats.updateStats()
        PC_Stats.SetAttackMoves(["Bash", "Cheer", "Focus"], "FIGHT_00B_MADLAS_ROBYN_")

        Jamie_Stats = JamieUnit()
        Jamie_Stats.SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave'], 'FIGHT_00B_MADLAS_JAMIE_')

        Taro_Stats = TaroUnit()
        Taro_Stats.SetAttackMoves(['Pounce', 'Tuna Defender', 'Jeer'], 'FIGHT_00B_MADLAS_TARO_')


        playerUnitsInit("PC","Jamie","Taro")
        enemyUnitsInit("MM")
        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "FIGHT_00B_MADLAS_PT"
        currentLabelET = "FIGHT_00B_MADLAS_ET"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])

        resetUnitStates("mD_turncount")



    Narrator "{glitch=20}Madlas{/glitch} freaks out!"

    $HighlightEnemyUnitBars([])
    jump FIGHT_00B_MADLAS_ET

label FIGHT_00B_MADLAS_ET:
    camera at camera_default

    $EnemyTurnStart()

    if not enemyUnits[0].isAlive:
        $mm_rank = calcRank(mD_turncount,30,25,20,15,13)

        Narrator "Turn Count: [mD_turncount] Rank: [mm_rank]"
        return

    jump FIGHT_00B_MADLAS_PT

label FIGHT_00B_MADLAS_PT:
    camera at camera_default

    python:
        PlayerTurnStart()
        mD_turncount+=1

        MD_State["mouth"] = 3
        MD_State["eyes"] = -1
    Narrator "It's time to fight. [mD_turncount]"

    $toggleQuickMenu()

    hide screen quicker_menu
    show screen turnCounter(mD_turncount)
    python:
        CombatUnitPick()
        ui.interact()

    return
