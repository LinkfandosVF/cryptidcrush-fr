
label FIGHT_00_MADLAS:
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
    call makeCheckpoint from _call_makeCheckpoint_6

    python:
        playerUnits[0].SetAttackMoves(["Bash", "Cheer", "Focus"], "FIGHT_00_MADLAS_ROBYN_")
        xHP = playerUnits[1].cHP


        playerUnits[1] = Jamie_Stats = JamieUnit()
        playerUnits[1].SetAttackMoves(['Spirit Blaze', 'Skull Cracker', 'Healing Wave'], 'FIGHT_00_MADLAS_JAMIE_')
        playerUnits[1].cHP = xHP
        playerUnits[1].recoveryRate = 2

        enemyUnits[0].SetEnemyAttackLabel("FIGHT_00_MADLAS_MD_ATTACK")

        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0,1])
        currentLabelPT= "FIGHT_00_MADLAS_PT"
        currentLabelET = "FIGHT_00_MADLAS_ET"


    Narrator "{glitch=20}Madlas{/glitch} freaks out!"

    Jamie "I need a breather."
    python:
        xHeal = playerUnits[1].cPower("occult") + 3
        playerUnits[0].modifyHP(xHeal,0.0,"guts")
        playerUnits[1].modifyHP(xHeal,0.0,"guts")

    Narrator "Jamie closes their eyes, and the flame between their horns casts a cool light over their allies, mending some of their wounds."
    $HighlightEnemyUnitBars([])
    jump FIGHT_00_MADLAS_ET

label FIGHT_00_MADLAS_ET:
    camera at camera_default

    $EnemyTurnStart()

    if not enemyUnits[0].isAlive:
        return
    jump FIGHT_00_MADLAS_PT

label FIGHT_00_MADLAS_PT:
    camera at camera_default

    python:
        PlayerTurnStart()

        MD_State["mouth"] = 3
        MD_State["eyes"] = -1
    Narrator "It's time to fight."

    $toggleQuickMenu()

    hide screen quicker_menu

    python:
        CombatUnitPick()
        ui.interact()

    return
