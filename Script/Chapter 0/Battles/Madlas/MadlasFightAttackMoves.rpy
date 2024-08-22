label FIGHT_00_MADLAS_ROBYN_0:
    $eName = enemyUnits[targetChoice].name
    $pName = playerUnits[0].name

    if isRollSuccess:
        Narrator "[pName] successfully bash [eName] with a thwack!"
        python:

            xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("brawn"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")



        Narrator "[eName] takes [sfxDmg] damage!"

        $enemyUnits[targetChoice].modifyStatMod("power",-1,-4,4)

    else:
        Narrator "Swing{w=.5} And a miss! [eName]’s eyes are on [pName] now."
        #Modify Mahouse Stat
        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

    $playerUnits[0].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_ROBYN_1:

    python:
        eName = enemyUnits[0].name
        pName = playerUnits[0].name
        if targetChoice != -1:
            xArray = ["C’mon, me, you’ve got this!","Show ‘em what Jersey’s made of, Jamie!"]
            xStr = xArray[targetChoice]
        else:
            xStr = "Lets kick ass!"
    Robyn "[xStr]"

    if targetChoice == -1:
        $playerUnits[0].modifyStatMod("power",1,-4,4)
        $playerUnits[1].modifyStatMod("power",1,-4,4)
    else:

        python:
            #Raises Power by 1
            xName = playerUnits[targetChoice].name
            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

            HighlightPlayerUnitBars([targetChoice])


        Narrator "[pName] uses the power of determination to heal [xName]'s for [xHeal] [kwHealth]!"

        python:
            #Heals Target
            playerUnits[targetChoice].modifyStatMod("power",2,-4,4)
            xHeal = renpy.random.randint(3,7)

    if not isRollSuccess:
        Narrator "[eName] definitely took [PCname]'s words the wrong way but is somehow invigorated!"

        $enemyUnits[0].modifyStatMod("power",2,-4,4)


    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_ROBYN_2:
    $pName = playerUnits[0].name
    if isRollSuccess:
        #Raises Karma on success
        Narrator "With a deep breath [pName] takes a moment to gather [PCtheir] thoughts."

        Robyn "… I’ve got it!"

        $pc_karma = limitValue(pc_karma+1, 0, diceBot.maxKarma)
        play sfx powerup_a
        Narrator "[kwKarma] increases by +2!"

    else:
        #Raises Jamie's Brain's and occult on a failure
        Narrator "[pName] tries to think as hard as [PCthey] can, but is worn out in the process."

        Robyn "I think I broke my brain."

        Jamie "Don't worry, I can take things from here."

        python:
            xName = playerUnits[1].name
            Jamie_Stats.modifyStatMod("brawn",2,-4,4)
            Jamie_Stats.modifyStatMod("occult",2,-4,4)

    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_0:
    python:
        pName = playerUnits[1].name
        eName = enemyUnits[0].name

    #Calculates Damage
    $xDmg = -(renpy.random.randint(7,10) + playerUnits[1].cPower("occult"))
    $xStr = renpy.random.choice(["Reaching up, " +pName+ " cups the flame in their hands and whispers a spell, the small flame dancing forward before exploding into a wild burst of hellfire.", "Swiping their hand through the air, " +pName+ " unleashes a raging bolt of blue hellfire."])

    Narrator "[xStr]"

    if isRollSuccess:
        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")


        Narrator "[eName] is engulfed in a pale blue light and takes [sfxDmg] damage!"
        $MD_State["eyes"] = 6
        $MD_State["feelerL"] = 1
        $MD_State["feelerR"] = 1
        $MD_State["mouth"] = 0
        Madlas "{sc=4}GyaAAAH!{/sc}"
        $MD_State["eyes"] = 1
        $MD_State["feelerL"] = 0
        $MD_State["feelerR"] = 0
        $MD_State["mouth"] = 1

        if renpy.random.choice([True,False]):
            Narrator "[pName] winces at the monster's scream and squeezes their eyes shut."
            $MD_State["eyes"] = -1
            Jamie "I'm sorry!"
    else:
        Narrator "The magical flame blazes out of control!"
        camera at camera_shake
        $HighlightPlayerUnitBars([0,1])
        $xDmg = int(-0.75*(renpy.random.randint(7,9) + playerUnits[1].cPower("occult")))

        $playerUnits[0].modifyHP(xDmg,0.0,"brains")
        $playerUnits[1].modifyHP(xDmg,0.0,"brains")

        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")

        Narrator "Everyone takes damage!"
        Robyn "JAMIE!"
        $ToggleBarState([0,1], 0)

    $playerUnits[1].DiminishModifiers([2,3,4,5])

    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_1:
    python:
        pName = playerUnits[1].name
        eName = enemyUnits[0].name

    $HighlightPlayerUnitBars([1])
    Narrator "[pName] headbutts [eName]’s with precision roughness!"
    $targetName = enemyUnits[targetChoice].name

    $xDmg = -(renpy.random.randint(4,6) + playerUnits[1].cPower("brawn"))
    $enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")
    $eDmg = sfxDmg

    if isRollSuccess:
        $xDmg= int(0.5*xDmg)

    $playerUnits[1].modifyHP(xDmg,1.0,"guts")


    camera at camera_shake
    Narrator "[eName] takes [eDmg] damage! [pName] takes [sfxDmg] recoil damage!"
    $ToggleBarState([1], 0)

    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $playerUnits[1].modifyStatMod("guts",-1,-4,4)

    $playerUnits[1].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_JAMIE_2:
    $pName = playerUnits[1].name
    if targetChoice != -1:
        $xHeal = renpy.random.randint(6,9) + playerUnits[1].cPower("occult")
        $xName = playerUnits[targetChoice].name
        $HighlightPlayerUnitBars([targetChoice])

        #Halve Healing on fail
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)
    else:
        $HighlightPlayerUnitBars([0,1,2,3])

    if targetChoice == -1:
        $xHeal = renpy.random.randint(2,4) + playerUnits[1].cPower("occult")
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)

        $playerUnits[0].modifyHP(xHeal,0.0,"guts")
        $playerUnits[1].modifyHP(xHeal,0.0,"guts")


        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over their allies, mending some of their wounds."
    else: #Single Target
        $playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over [xName], healing them for [xHeal] [kwHealth]."

    if not isRollSuccess:
        $xStr = renpy.random.choice(["...Can you all shut up?!","Mmmrgh...","I am TRYING to cast a spell.","I… can’t do this.","Goddammit!"])

        Narrator "They growl, unable to focus any further."

        Jamie "[xStr]"
    else:
        Jamie "This had better help."

    $playerUnits[1].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_00_MADLAS_MD_ATTACK:
    $bossName = enemyUnits[0].name
    $CheckForGameOvers()
    play sfx boss_target_sfx
    python:
        xAtk = renpy.random.choice([0,1])

        eTarget = renpy.random.randint(0,1)

        while not playerUnits[eTarget].isAlive:
            eTarget = renpy.random.randint(0,1)

        eTargetName = playerUnits[eTarget].name
        HighlightPlayerUnitBars([eTarget])

    if xAtk == 0: #Phantom Slash
        python: #Calculate Damage and Highlight Bar

            xDmg = -(renpy.random.randint(3,6) + enemyUnits[0].cPower("brawn"))

        Narrator "[bossName] looks to [eTargetName] and wildly slashes his claws through the air!"

        call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("hustle"), "Phantom Slash") from _call_dice_roll_21

        camera at camera_shake
        if isRollSuccess: #Half Damage on success
            python:
                xDmg= int(0.5*xDmg)
                playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")


            Narrator "[eTargetName] comes out mostly unscathed taking [sfxDmg] damage!"
        else: #Damage bby
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
            $xStr = renpy.random.choice(["takes a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])


            Narrator "[eTargetName] [xStr] [sfxDmg] damage!"
    else:
        $xDmg = -(renpy.random.randint(5,7))
        Narrator "[bossName] cackles as he chucks an oversized stereo speaker at [eTargetName]!"

        call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_22
        show MMFight_Chair at MMFight_LeftProp_Exit
        show MMFight_Speaker at MMFight_RightProp_Exit
        if isRollSuccess:
            $xStr = renpy.random.choice(["scrambles out of the way, ducking behind a desk.","shields their face from the sparks and broken parts, taking no damage.","gracefully slips out of the way.", "steps back as the hit completely whiffs, shattering against the ground, grimacing at the collateral damage."])
            Narrator "[eTargetName] [xStr]"
        else: #Damage on failure
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
            $xStr = renpy.random.choice(["takes a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])

            camera at camera_shake
            Narrator "[eTargetName] [xStr] [sfxDmg] damage!"


        show MMFight_Chair at MMFight_LeftProp_Entry
        show MMFight_Speaker at MMFight_RightProp_Entry
        $ToggleBarState([0,1], 0)

    jump expression currentLabelPT
