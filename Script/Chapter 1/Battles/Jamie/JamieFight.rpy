default jamie_turncount = 0
default mmLives = 1
default jamieLives = 3

label FIGHT_06_JAMIE:
    $curBattleNum = 6
    call battleTransition from _call_battleTransition_8


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
        Jamie_Stats = Unit("{color=3AE9F6}Jamie{/color}",1,2,-1,0,-2,3,13)
        Jamie_Stats.battleLines = JamieUnit().battleLines
        Jamie_Stats.baseDiff = 5
        Jamie_Stats.SetIcon("dIcon1")
        Jamie_Stats.SetMaxMTA(2) ##This is previously known as eDelay
        Jamie_Stats.SetNOCA(2) ##Enemy Unit attacks 2 times when its their turn.
        Jamie_Stats.SetEnemyAttackLabel("FIGHT_06_JAMIE_JAMIE_ATTACK")
        Jamie_Stats.SetMTA(3)

        MM_Stats = MMUnit()
        MM_Stats.SetAttackMoves(['Kinesis', 'Noxious Fist', 'Heckle', 'Not The Face'], 'FIGHT_06_JAMIE_MM_')
        #Kinesis
        #Noxious Mist
        #So Silly "I'm jus a silly little guy!" . Raises MTA by 1 as well as stamina but on a failure jamie punches Madhouse

        PC_Stats = RobynUnit()
        PC_Stats.SetAttackMoves(['Cheer','Idle'], 'FIGHT_06_JAMIE_ROBYN_')
        PC_Stats.attacks[0].name = "Cheer Madhouse"
        PC_Stats.attacks[0].targetsAll = 2
        PC_Stats.attacks.append(PC_Stats.attacks[1])
        PC_Stats.attacks[1] = AttackMove("Cheer Jamie","[kwSuccess] Slightly lowers both Target(s)' [kwPowerMod] and [kwDifficultyModD], and restores [kwHealth].\n\n[kwFailure] Move works, only restores health.\n\nChecks [kwCharm] vs Fixed(8)\nCost: 2 Stamina", -2, "FIGHT_06_JAMIE_ROBYN_2", "charm","fixed",    2, True,  [],8)

        PC_Stats.attacks.append(AttackMove("Look at Phone","Either Jamie or Madhouse get a free attack on the other.", 0, "FIGHT_06_JAMIE_ROBYN_3", "charm","fixed",    2, True,  [],-1))


        playerUnitsInit("MM","PC")
        enemyUnitsInit("Jamie")
        InitializeCombatUI(playerUnits, enemyUnits)

        currentLabelPT= "FIGHT_06_JAMIE_PT"
        currentLabelET = "FIGHT_06_JAMIE_ET"

        HighlightEnemyUnitBars([0,1,2,3])
        HighlightPlayerUnitBars([0,1,2,3])

        eName = enemyUnits[0].name
        pName = playerUnits[0].name

        mmLives = 1
        jamieLives = 3
        resetUnitStates("jamie_turncount")


    with Dissolve(0.5)
    $musicPlayer.playSong(song="wrath_of_the_recolors")

    Madhouse "I-I'm g-gonna wipe the floor with this clown!"
    #Narrator "Jamie punches the ghost, leaving a fist shaped scrunch where a nose would be."

    #Narrator "Madhouse squeezes his eyes shut and his face pops back into place."

    #Madhouse "I wasn't ready!"

    #Jamie "Too slow!"

    $HighlightEnemyUnitBars([])
    jump FIGHT_06_JAMIE_ET

label FIGHT_06_JAMIE_PT:
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

label FIGHT_06_JAMIE_ET:
    show Jamie_Battle_CG Default at battle_jamie_pos
    show Jamie_Battle_MM_CG Default at battle_jamie_mm_pos

    camera at camera_default

    if enemyUnits[0].cHP <= 0:
        $jamieLives-=1
        if jamieLives < 1:
            jump FIGHT_06_JAMIE_END
        $enemyUnits[0].modifyHP(10,0.0,"guts")
        $Jamie_Stats.SetMTA(0)
        Narrator "With a snarl [eName] leaps up off the ground and spits a gout of fire. ([jamieLives] left)"

        if jamieLives > 1:
            Jamie " {sc=2}{b}{color=#EC2A2A}AGAIN!{/color}{/b}{/sc}"
        else:
            Jamie "{sc=3}Nnngh, y-you can't defeat me.{/sc}"

    if playerUnits[0].cHP <= 0:
        call dice_roll(playerUnits[0].cStats("guts"), 10, "Fright for your life!") from _call_dice_roll_73

        if not isRollSuccess:
            $mmLives = 0
            jump FIGHT_06_JAMIE_END

        $playerUnits[0].modifyHP(1,0.0,"guts")
        Narrator "[pName] stays in the game."

        Madhouse "Sorry pal, I ain't so easy."


    python:
        EnemyTurnStart()

    jump FIGHT_06_JAMIE_PT

label FIGHT_06_JAMIE_END:
    $mm_rank = calcRank(jamie_turncount,40,30,25,20,15)

    if mmLives:
        Narrator "Turn Count: [jamie_turncount] Rank: [mm_rank]"
    else:
        Narrator "Jamie Turn Count: [jamie_turncount] Rank: [mm_rank]"


    return

label FIGHT_06_JAMIE_CROWDCHEER:

    show CG_RobbieRobynDuo:
        yoffset 0
        parallel:
            ease 1.0 yoffset 700
            ease 0.5 yoffset -60
            ease 0.2 yoffset 0

        parallel:
            pause 1.0
            choice:
                matrixtransform rotated()
                xcenter 0.25
            choice:
                matrixtransform rotated(y=180)
                xcenter 0.85
            choice:
                pause 0.1
        block:
            ease 2.2 yoffset 0
            ease 1.8 yoffset -20
            repeat

    show CG Crowd:
        xcenter 0.3
        pause 0.2
        ease 0.2 yoffset 30
        ease 0.15 yoffset 0
        ease 0.15 yoffset 30
        pause 0.1
        ease 0.15 yoffset 0
        ease 0.15 yoffset 30
        pause 0.2
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    show CG2 Crowd:
        xcenter 0.7
        ease 0.2 yoffset 30
        ease 0.15 yoffset 0
        ease 0.15 yoffset 30
        ease 0.15 yoffset 0
        ease 0.15 yoffset 30
        block:
            ease 2.2 yoffset 17
            ease 1.8 yoffset 0
            repeat

    return
