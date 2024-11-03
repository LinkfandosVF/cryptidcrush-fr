label FIGHT_06B_JAMIE:
    $curBattleNum = 6
    call battleTransition from _call_battleTransition_11

    scene BG Empty Street Day

    show CG_RobbieRobynDuo:
        xcenter 0.25
        yoffset 700
        ease 1.0 yoffset 0
        block:
            ease 2.2 yoffset 0
            ease 1.8 yoffset -20
            repeat

    show CG Crowd:
        xcenter 0.3
        pause 0.5
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    show CG2 Crowd:
        xcenter 0.7
        block:
            ease 1.8 yoffset 17
            ease 2.2 yoffset 0
            repeat

    show Jamie_Battle_CG Default at battle_jamie_pos
    show Jamie_Battle_MM_CG Default at battle_jamie_mm_pos
    camera at camera_default

    python:
        adjustChar("Jamie",eye=6,mouth=1,armR=0,fire=True)
        Jamie_Stats = Unit("{color=3AE9F6}Jamie{/color}",1,2,-1,0,-2,3,60)
        Jamie_Stats.battleLines = JamieUnit().battleLines
        Jamie_Stats.baseDiff = 6
        Jamie_Stats.SetIcon("dIcon1")
        Jamie_Stats.SetMaxMTA(2) ##This is previously known as eDelay
        Jamie_Stats.SetNOCA(3) ##Enemy Unit attacks 2 times when its their turn.
        Jamie_Stats.SetEnemyAttackLabel("FIGHT_06B_JAMIE_JAMIE_ATTACK")
        Jamie_Stats.SetMTA(4)

        MM_Stats = MMUnit()
        MM_Stats.SetAttackMoves(['Kinesis', 'Noxious Fist', 'Heckle', 'Not The Face'], 'FIGHT_06_JAMIE_MM_')


        playerUnitsInit("MM")
        enemyUnitsInit("Jamie")

        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "FIGHT_06B_JAMIE_PT"
        currentLabelET = "FIGHT_06B_JAMIE_ET"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])

        eName = enemyUnits[0].name
        pName = playerUnits[0].name

        mmLives = 1
        jamieLives = 3
        resetUnitStates("jamie_turncount")


    with Dissolve(0.5)
    $musicPlayer.playSong("ghastly_resurgence")

    Jamie "I will give you a head start, but just know that I won't hold back."

    $HighlightEnemyUnitBars([])

    jump FIGHT_06_JAMIE_ET

label FIGHT_06B_JAMIE_PT:
    show Jamie_Battle_CG Default at battle_jamie_pos
    show Jamie_Battle_MM_CG Default at battle_jamie_mm_pos

    camera at camera_default:
        camera_zoom(z=-350,x=-230,y=-50,t=0.5)
        block:
            choice:
                parallel:
                    choice:
                        ease 2.5 yoffset -10 - 50
                    choice:
                        ease 2.5 yoffset 10 - 50
                    choice:
                        ease 2.5 yoffset -5 - 50
                    choice:
                        ease 2.5 yoffset 5 - 50
                    choice:
                        ease 2.5 yoffset 0 - 50

                parallel:
                    choice:
                        ease 2.5 xoffset -10 -230
                    choice:
                        ease 2.5 xoffset 10 -230
                    choice:
                        ease 2.5 xoffset -5 -230
                    choice:
                        ease 2.5 xoffset 5 -230
                    choice:
                        ease 2.5 xoffset 0 -230

                repeat 3

            choice:

                parallel:
                    choice:
                        ease 2.5 yoffset -120
                    choice:
                        ease 2.5 yoffset -115
                    choice:
                        ease 2.5 yoffset -110
                parallel:
                    choice:
                        ease 2.5 xoffset 240
                    choice:
                        ease 2.5 xoffset 250
                    choice:
                        ease 2.5 xoffset 260

                repeat 2

            choice:

                parallel:
                    choice:
                        ease 2.5 yoffset -80
                    choice:
                        ease 2.5 yoffset -75
                    choice:
                        ease 2.5 yoffset -70
                parallel:
                    choice:
                        ease 2.5 xoffset -10
                    choice:
                        ease 2.5 xoffset 0
                    choice:
                        ease 2.5 xoffset 10

                repeat 2

            repeat

    python:
        adjustChar("Jamie",eye=6,mouth=1,armR=0,fire=True,r3Fire=False)
        PlayerTurnStart()
        jamie_turncount+=1

    python:
        #Random Idle Lines
        xStr = "Madhouse is ready to fight."
        xIdle = ["Madhouse sneers.","Madhouse stands his ground.","Madhouse shivers.","Madhouse snarls.","Madhouse growls.","Madhouse curses under his breath.","Madhouse keeps this PG-13."]

        xStr = renpy.random.choice(xIdle)
        if playerUnits[CheckLowestHP(False)].cHP <= 5:
            xStr = playerUnits[CheckLowestHP(False)].name + " could use a hand."

    Narrator "[xStr]"

    $toggleQuickMenu()
    hide screen quicker_menu
    show screen turnCounter(jamie_turncount)
    python:
        CombatUnitPick()
        ui.interact()

    return

label FIGHT_06B_JAMIE_ET:
    show Jamie_Battle_CG Default at battle_jamie_pos
    show Jamie_Battle_MM_CG Default at battle_jamie_mm_pos

    camera at camera_default

    if enemyUnits[0].cHP <= 0:
        jump FIGHT_06B_JAMIE_END

    if playerUnits[0].cHP <= 0:
        call dice_roll(playerUnits[0].cStats("guts"), 7, "Fright for your life!") from _call_dice_roll_81

        if not isRollSuccess:
            $mmLives = 0
            jump FIGHT_06_JAMIE_END

        $playerUnits[0].modifyHP(99,0.0,"guts")
        Narrator "[pName] stays in the game."

        Madhouse "Sorry pal, I ain't so easy."


    python:
        EnemyTurnStart()

    jump FIGHT_06_JAMIE_PT

label FIGHT_06B_JAMIE_END:
    $mm_rank = calcRank(jamie_turncount,45,35,25,20,17)

    if mmLives:
        Narrator "Turn Count: [jamie_turncount] Rank: [mm_rank]"
    else:
        Narrator "Jamie Turn Count: [jamie_turncount] Rank: [mm_rank]"


    return
