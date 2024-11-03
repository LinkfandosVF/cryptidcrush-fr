
# ------------------------------------------------------------------(0) MADHOUSE

#Kinesis
label FIGHT_06_JAMIE_MM_0:
    camera at camera_default:
        camera_zoom(t=0.3)

    python:
        eName = enemyUnits[targetChoice].name
        pName = playerUnits[0].name
        xDmg = -(renpy.random.randint(8,10) + playerUnits[0].cPower("occult"))

    Narrator "[pName] hits [eName] with psychic power!"

    show Jamie_Battle_MM_CG Attack at battle_jamie_mm_attack_pos
    show Jamie_Battle_CG Hurt at battle_jamie_hurt_pos
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER
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
label FIGHT_06_JAMIE_MM_1:
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
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_1
    voice enemyUnits[targetChoice].getLine()

    Narrator "[eName] takes [sfxDmg] damage!"

    $enemyUnits[targetChoice].modifyStatMod("brains",-2,-4,4)


    $playerUnits[0].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

#Heckle
label FIGHT_06_JAMIE_MM_2:
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
label FIGHT_06_JAMIE_MM_3:
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

# ---------------------------------------------------------------------(1) ROBYN

#Cheer madhouse
label FIGHT_06_JAMIE_ROBYN_0:
    camera at camera_default:
        camera_zoom(t=0.3)
    $playerUnits[1].DiminishModifiers([2,3,4,5])
    python:
        pName = playerUnits[1].name

        xStr = renpy.random.choice(["I believe in you!", "Hold on Mike!", "Remember your theme song!", "Show 'em what you got big shot!"])

    Narrator "[xStr]"

    python: #Healing
        xName = playerUnits[0].name
        HighlightPlayerUnitBars([targetChoice])
        xHeal = renpy.random.randint(3,7)
        playerUnits[0].modifyHP(xHeal,0.0,"guts")

    #Update HP
    Narrator "[pName] uses the power of will to heal [xName]'s for [xHeal] [kwHealth]!"

    #Stat Change
    $playerUnits[0].modifyStatMod("power",2,-4,4)

    if not isRollSuccess:
        $enemyUnits[0].modifyStatMod("power",2,-4,4)

    jump expression currentLabelET

#Idle
label FIGHT_06_JAMIE_ROBYN_1:
    camera at camera_default:
        camera_zoom(t=0.3)
    python:
        if pc_karma > 1:
            pc_karma-=1
            hadKarma = True
        else:
            hadKarma = False

    #Robyn "Hey Granny, did you know ghosts adopt lasting attributes after they possess a creature? Like Kirby!"
    Narrator "You strike up the most pleasant conversation with Goatma'am."

    Goatmaam "Oh, that reminds me!"

    if hadKarma:
        Jamie "{sc}Hrmgh.{/sc}"

        $enemyUnits[targetChoice].ChangeMTA(2)
        Narrator "[eName] takes a pause to listen to what Goatma'am has to say, delaying their turn."

        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

    else:
        $addBattleKarma(1)

    jump expression currentLabelET

#Cheer Jamie
label FIGHT_06_JAMIE_ROBYN_2:
    camera at camera_default:
        camera_zoom(t=0.3)
    $pName = playerUnits[1].name

    $xTxt = renpy.random.choice(["Knock 'em dead Jamie!", "Consume, corrupt, destroy!!", "Show us what Jersey's got Jamie!", "Knock 'em dead!"])
    Robyn "[xTxt]"

    Robbie "{b}{sc}RIBBIT!{/sc}"

    python: #Healing
        xName = enemyUnits[0].name
        HighlightPlayerUnitBars([0])
        xHeal = renpy.random.randint(3,7)
        enemyUnits[0].modifyHP(xHeal,0.0,"guts")

    #Update HP
    Narrator "[pName]'s words heal [xName]'s for [xHeal] [kwHealth]!"

    python:
        if isRollSuccess:
            #Stat Change
            enemyUnits[targetChoice].modifyStatMod("power",-2,-4,4)
            enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

        playerUnits[0].DiminishModifiers([2,3,4,5])

    jump expression currentLabelET

label FIGHT_06_JAMIE_ROBYN_3:
    camera at camera_default:
        camera_zoom(t=0.3)
    if renpy.random.choice([True,False]):
        Narrator "You look at your phone and when you look back, Madhouse is biting Jamie like a feral cat. Jamie yowls."

        show Jamie_Battle_MM_CG Attack at battle_jamie_mm_attack_pos
        show Jamie_Battle_CG Hurt at battle_jamie_hurt_pos

        python:
            HighlightEnemyUnitBars([0])
            xDmg = -(renpy.random.randint(6,8) + playerUnits[0].cPower("brawn"))
            enemyUnits[0].modifyHP(xDmg,0.0,"guts")

        call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_2
        Narrator "[eName] takes [sfxDmg] damage!"
    else:
        Narrator "You look at your phone, and when you look back Jamie is twisting Madhouse like a string of taffy. Great day for no bones!"
        $HighlightPlayerUnitBars([0])
        call FIGHT_06_JAMIE_JAMIE_2 from _call_FIGHT_06_JAMIE_JAMIE_2


    $playerUnits[0].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET
# ---------------------------------------------------------------------- ENEMIES
# ---------------------------------------------------------------------- ENEMIES
# ---------------------------------------------------------------------- ENEMIES

#currentCA
# ---------------------------------------------------------------------(0) JAMIE

label FIGHT_06_JAMIE_JAMIE_ATTACK:
    camera at camera_default:
        camera_zoom(t=0.3)

    python:
        adjustChar("Jamie",eye=7,mouth=2,armR=2,fire=True,r3Fire=True)
        pName = playerUnits[0].name

        if jamieLives <=1:
            if enemyUnits[0].isBloodied():
                xAtk = renpy.random.choice([2,3,3,4,4])
            else:
                xAtk = renpy.random.choice([2,2,3,3,3])
        else:
            if currentCA == 1:
                xAtk = renpy.random.randint(0,1)
            else:
                if enemyUnits[0].isBloodied():
                    xAtk = renpy.random.choice([2,3,4,4,4])
                else:
                    xAtk = renpy.random.choice([1,1,2,2,2])

    play sfx boss_target_sfx
    call expression "FIGHT_06_JAMIE_JAMIE_" + str(xAtk) from _call_expression_37

    if enemyUnits[0].cHP <= 0:
        $jamieLives-=1
        if jamieLives < 1:
            jump FIGHT_06_JAMIE_END
        $enemyUnits[0].modifyHP(10,0.0,"guts")
        Narrator "[eName] picks themselves back up back up. ([jamieLives] left)"

        if jamieLives > 1:
            Jamie "Good, lets go again."
        else:
            Jamie "Ngh, One more time..."

    if playerUnits[0].cHP <= 0:
        call dice_roll(playerUnits[0].cStats("guts"), 10, "Fright for your life!") from _call_dice_roll_74

        if not isRollSuccess:
            $mmLives = 0
            jump FIGHT_06_JAMIE_END

        $playerUnits[0].modifyHP(1,0.0,"guts")
        Narrator "[pName] falters but holds his ground."

        Madhouse "N-not yet."

    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_3
    jump expression currentLabelPT

label FIGHT_06_JAMIE_JAMIE_0:
    Narrator "[eName] readies an attack."

    python:
        enemyUnits[0].modifyStatMod("occult",1,-4,4)
        enemyUnits[0].modifyStatMod("brawn",2,-4,4)


    return

#Skull Cracker
label FIGHT_06_JAMIE_JAMIE_1:
    camera:
        xoffset 0

    show Jamie_Battle_CG Attack at battle_jamie_attack_pos
    show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos

    python:
        xDmg = -(renpy.random.randint(1,3) + enemyUnits[0].cPower("brawn"))
        enemyUnits[0].modifyHP(xDmg,1.0,"guts")
        playerUnits[0].modifyHP(xDmg,0.5,"guts")
        HighlightEnemyUnitBars([0,1,2,3])

    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_4
    Narrator "[eName] bashes their skull against [pName] with precision roughness! He takes [sfxDmg] damage!"
    return

#Iron Chokehold
label FIGHT_06_JAMIE_JAMIE_2:
    show Jamie_Battle_CG Attack at battle_jamie_attack_pos

    show CGShade
    show GrabbingMadhouse at startledSquish

    play sfx mm_strangle
    Narrator "[eName] throws their claws around [pName] and squeezes him like a stress toy!"

    #Madhouse "Th-that's gotta be against the rules!"

    #Goatmaam "What rules? You're already dead!"

    call dice_roll(playerUnits[0].cStats("brawn"), enemyUnits[0].cDifficulty("brawn"), "Silver Chokehold") from _call_dice_roll_65

    python:
        xDmg = limitValue( -(enemyUnits[0].cPower("brawn")-2) , -99, -1)
        playerUnits[0].modifyHP(xDmg,0.5,"guts")

    show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
    call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_5

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
        call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_6
        Narrator "[pName] takes [sfxDmg] radiant damage!"

        $playerUnits[0].modifyStatMod("guts",-1,-4,4)
        if playerUnits[0].isAlive:
            call dice_roll(playerUnits[0].cStats("brawn"), enemyUnits[0].cDifficulty("brawn")-xFails, "Silver Chokehold") from _call_dice_roll_66
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
label FIGHT_06_JAMIE_JAMIE_3:
    show Jamie_Battle_CG Attack at battle_jamie_attack_pos
    Narrator "[eName] flings a blue fireball at [pName]!"

    call dice_roll(playerUnits[0].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Spirit Blaze") from _call_dice_roll_67

    if isRollSuccess:
        Narrator "[pName] barely peels out of the way!"
    else:
        python:
            xDmg = -(renpy.random.randint(7,9) + enemyUnits[0].cPower("occult"))
            playerUnits[0].modifyHP(xDmg,0.0,"brains")

        show Jamie_Battle_MM_CG Hurt at battle_jamie_mm_hurt_pos
        call FIGHT_06_JAMIE_CROWDCHEER from _call_FIGHT_06_JAMIE_CROWDCHEER_7
        Narrator "[pName] erupts into a screeching flame taking [sfxDmg] radiant damage!"
    return


#Healing wave
label FIGHT_06_JAMIE_JAMIE_4:

    Narrator "[eName] focuses on self healing."

    $xTxt = renpy.random.choice(["What're you doing?! Cut that out!","'Ey referee that shit's a yellow card!","Rulebreaker! Rulebreaker!","Cheater cheater, pumpkin eater!"])
    Madhouse "{sc=3}{b}NO!{/b}{/sc}\n\n[xTxt]"

    call dice_roll(playerUnits[0].cStats("charm"), enemyUnits[0].cDifficulty("brains"), "Annoy Jamie") from _call_dice_roll_68
    $HighlightEnemyUnitBars([0,1,2,3])
    if isRollSuccess:
        show Jamie_Battle_MM_CG Attack at battle_jamie_mm_attack_pos
        voice enemyUnits[targetChoice].getLine("fail")
        python:
            xHeal = renpy.random.randint(1,3)
            enemyUnits[0].modifyHP(xHeal,0.0,"guts")

            xStr = renpy.random.choice(["...Can you all shut up?!","Mmmrgh...","Dammit.","{sc}Aargh!{/sc}","Goddammit!"])

        Narrator "[eName]'s focus breaks and they heal for [xHeal] [kwHealth]."

        Jamie "[xStr]"
        $enemyUnits[0].modifyStatMod("brains",-1,-4,4)
    else:
        voice enemyUnits[targetChoice].getLine("success")
        python:
            xHeal = renpy.random.randint(6,9) + enemyUnits[0].cPower("occult")
            enemyUnits[0].modifyHP(xHeal,0.0,"guts")

        Narrator "[eName] remains stoic, and their wounds mend for [xHeal] [kwHealth]."


    return
