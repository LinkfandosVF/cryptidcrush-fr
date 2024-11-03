
#Kinesis
label FIGHT_06B_JAMIE_MM_0:
    camera at camera_default:
        camera_zoom(t=0.3)

    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name
        xDmg = -(renpy.random.randint(8,10) + playerUnits[0].cPower("occult"))

    Narrator "[pName] hits [eName] with psychic power!"

    show Jamie_Battle_MM_CG Attack at battle_jamie_mm_attack_pos
    show Jamie_Battle_CG Hurt at battle_jamie_hurt_pos
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_8

    $enemyUnits[targetChoice].modifyHP(xDmg,0.0,"brains")

    voice enemyUnits[targetChoice].getLine()
    Narrator "[eName] takes [sfxDmg] damage!"

    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $HighlightPlayerUnitBars([0])
        $playerUnits[0].modifyHP(int(xDmg/2),0.0,"brains")
        show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
        camera at camera_shake

        Narrator "[pName] takes [sfxDmg] recoil damage!"

        $playerUnits[0].modifyStatMod("guts",-2,-4,4)



    $playerUnits[0].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

#Noxious Fist
label FIGHT_06B_JAMIE_MM_1:
    camera at camera_default:
        camera_zoom(t=0.3)

    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name
        xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("brawn"))

    Narrator "[pName] punches [eName] with a noxious fist!"

    show Jamie_Battle_MM_CG Attack at battle_jamie_mm_attack_pos
    show Jamie_Battle_CG Hurt at battle_jamie_hurt_pos

    if not isRollSuccess:
        $xDmg = int(xDmg/2)

    $enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_9
    voice enemyUnits[targetChoice].getLine()

    Narrator "[eName] takes [sfxDmg] damage!"

    $enemyUnits[targetChoice].modifyStatMod("brains",-2,-4,4)


    $playerUnits[0].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

#Heckle
label FIGHT_06B_JAMIE_MM_2:
    camera at camera_default:
        camera_zoom(t=0.3)

    $xTxt = renpy.random.choice(["Bleeeh, you can't get me!","C'mon hot shot, can't punch a ghost?","You're just jealous of my dashing good looks!","Hey dry bones, why the long face?!","So what, are you like, a goat? A red goat?", "Look, up in the sky! Is that Atlas?! \n\nHaha, made ya look!"])

    Madhouse "[xTxt]"

    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name

    if isRollSuccess:
        Jamie "{sc}{b}!?{/b}{/sc}"

        python:
            enemyUnits[targetChoice].modifyStatMod("diff",2,-4,4)
            enemyUnits[targetChoice].ChangeMTA(1)

        Narrator "[eName]'s turn is delayed by +1."


    else:
        Jamie "Cowardice has no place here!"

        python:
            enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)
            enemyUnits[targetChoice].ChangeMTA(-999)

        Narrator "[eName] is spurred into action!"

    $playerUnits[0].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

#Not The Face
label FIGHT_06B_JAMIE_MM_3:
    camera at camera_default:
        camera_zoom(t=0.3)
    $eName = enemyUnits[targetChoice].name
    Madhouse "{bt=3}Bleeeeh, come and get me {b}Bonehead{/b}!{/bt}"

    python:
        if isRollSuccess:
            playerUnits[0].modifyStatMod("defense",2,-4,4)
            playerUnits[0].modifyStatMod("rollMod",2,-4,4)

        enemyUnits[targetChoice].ChangeMTA(-99)
    Narrator "[eName] takes the initiative!"

    jump expression currentLabelET


#JAMIE ---------------------------------------------------------------------------
default lxAtk = 4
label FIGHT_06B_JAMIE_JAMIE_ATTACK:
    camera at camera_default:
        camera_zoom(t=0.3)

    python:
        adjustChar("Jamie",eye=7,mouth=2,armR=2,fire=True,r3Fire=True)
        pName = playerUnits[0].name

        if enemyUnits[0].isBloodied():
            xAtk = renpy.random.choice([0,1,2,2,3,3])
        else:
            xAtk = renpy.random.choice([0,0,1,1,2,2,3])

        while lxAtk == xAtk:
            xAtk = renpy.random.choice([0,1,2,3])

        lxAtk = xAtk

    play sfx boss_target_sfx
    call expression "FIGHT_06B_JAMIE_JAMIE_" + str(xAtk) from _call_expression_41

    if enemyUnits[0].cHP <= 0:
        $jamieLives-=1
        if jamieLives < 1:
            jump FIGHT_06B_JAMIE_END
        $enemyUnits[0].modifyHP(10,0.0,"guts")
        Narrator "[eName] picks themselves back up back up. ([jamieLives] left)"

        if jamieLives > 1:
            Jamie "Good, lets go again."
        else:
            Jamie "Ngh, One more time..."

    if playerUnits[0].cHP <= 0:
        call dice_roll(playerUnits[0].cStats("guts"), 7, "Fright for your life!") from _call_dice_roll_82

        if not isRollSuccess:
            $mmLives = 0
            jump FIGHT_06_JAMIE_END

        $playerUnits[0].modifyHP(99,0.0,"guts")
        Narrator "[pName] falters but holds his ground."

        Madhouse "N-not yet."

    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_10
    jump expression currentLabelPT

label FIGHT_06B_JAMIE_JAMIE_0:
    Narrator "[eName] readies an attack."

    python:
        enemyUnits[0].modifyStatMod("occult",2,-4,4)
        enemyUnits[0].modifyStatMod("brawn",2,-4,4)


    return

#Skull Cracker
label FIGHT_06B_JAMIE_JAMIE_1:
    camera:
        xoffset 0

    show Jamie_Battle_CG Attack at battle_jamie_attack_pos
    show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos

    python:
        xDmg = -(renpy.random.randint(1,3) + enemyUnits[0].cPower("brawn"))
        enemyUnits[0].modifyHP(xDmg,1.0,"guts")
        playerUnits[0].modifyHP(xDmg,0.5,"guts")
        HighlightEnemyUnitBars([0,1,2,3])

    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_11
    Narrator "[eName] bashes their skull against [pName] with precision roughness! He takes [sfxDmg] damage!"
    return

#Iron Chokehold
label FIGHT_06B_JAMIE_JAMIE_2:
    show Jamie_Battle_CG Attack at battle_jamie_attack_pos

    show CGShade
    show GrabbingMadhouse at startledSquish

    play sfx mm_strangle
    Narrator "[eName] throws their claws around [pName] and squeezes him like a stress toy!"

    call dice_roll(playerUnits[0].cStats("brawn"), enemyUnits[0].cDifficulty("brawn"), "Silver Chokehold") from _call_dice_roll_83

    python:
        xDmg = limitValue( -(enemyUnits[0].cPower("brawn")-2) , -99, -1)
        playerUnits[0].modifyHP(xDmg,0.5,"guts")

    show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_12

    show GrabbingMadhouse at startledSquish:
        matrixcolor ColorizeMatrix("#6b192d","#f23a3a")*SaturationMatrix(0)
        ease 0.5 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)

    play sfx mm_strangle
    Narrator "[pName] takes [sfxDmg] radiant damage!"

    $xFails = 0
    while not isRollSuccess:

        show GrabbingMadhouse:
            matrixcolor ColorizeMatrix("#6b192d","#f23a3a")*SaturationMatrix(0)
            ease 0.5 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)


        python:
            xFails+=1
            xDmg = limitValue( -(renpy.random.randint(-1,1) + enemyUnits[0].cPower("brawn") + xFails) , -99 ,-1)
            playerUnits[0].modifyHP(xDmg,0.5,"guts")

        show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
        call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_13
        Narrator "[pName] takes [sfxDmg] radiant damage!"

        $playerUnits[0].modifyStatMod("guts",-1,-4,4)
        if playerUnits[0].isAlive:
            call dice_roll(playerUnits[0].cStats("brawn"), enemyUnits[0].cDifficulty("brawn")-xFails, "Silver Chokehold") from _call_dice_roll_85
        else:
            $isRollSuccess = True


    show GrabbingMadhouse:
        matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)
        yoffset 0
        ease 0.5 yoffset -700

    with None
    hide CGShade with nwDissolve(0.3)

    if playerUnits[0].isAlive:
        Narrator "[pName] breaks away!"
    else:
        Narrator "[eName] tosses [pName] to the ground in a slimy heap."

    hide GrabbingMadhouse
    return

#Spirit Blaze
label FIGHT_06B_JAMIE_JAMIE_3:
    show Jamie_Battle_CG Attack at battle_jamie_attack_pos
    Narrator "[eName] flings a blue fireball at [pName]!"

    call dice_roll(playerUnits[0].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Spirit Blaze") from _call_dice_roll_86

    if isRollSuccess:
        Narrator "[pName] barely peels out of the way!"
    else:
        python:
            xDmg = -(renpy.random.randint(7,9) + enemyUnits[0].cPower("occult"))
            playerUnits[0].modifyHP(xDmg,0.0,"brains")

        show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
        call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_14
        Narrator "[pName] erupts into a screeching flame taking [sfxDmg] radiant damage!"

    return
