# ------------------------------------------------------------------------ ROBYN
label FIGHT_00B_MADLAS_ROBYN_0:
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

label FIGHT_00B_MADLAS_ROBYN_1:

    python:
        eName = enemyUnits[0].name
        pName = playerUnits[0].name

    Robyn "Lets kick ass!"

    if targetChoice == -1:
        python:
            playerUnits[0].modifyStatMod("power",1,-4,4)
            playerUnits[1].modifyStatMod("power",1,-4,4)
            playerUnits[2].modifyStatMod("power",1,-4,4)
    else:

        python:
            #Raises Power by 1
            xHeal = renpy.random.randint(3,7)
            xName = playerUnits[targetChoice].name
            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

            HighlightPlayerUnitBars([targetChoice])


        Narrator "[pName] uses the power of determination to heal [xName]'s for [xHeal] [kwHealth]!"

        python:
            #Heals Target
            playerUnits[targetChoice].modifyStatMod("power",2,-4,4)


    if not isRollSuccess:
        Narrator "[eName] definitely took [PCname]'s words the wrong way but is somehow invigorated!"

        $enemyUnits[0].modifyStatMod("power",2,-4,4)


    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_00B_MADLAS_ROBYN_2:
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

# ------------------------------------------------------------------------ JAMIE
label FIGHT_00B_MADLAS_JAMIE_0:
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
        python:
            HighlightPlayerUnitBars([0,1,2])
            xDmg = int(-0.75*(renpy.random.randint(7,9) + playerUnits[1].cPower("occult")))

            if Taro_Stats.taroTuna: #Taro intervenes on a failure
                playerUnits[2].modifyHP(xDmg,0.0,"brains")
            else:
                xDmg = int(-0.75*(renpy.random.randint(7,9) + playerUnits[1].cPower("occult")))
                for x in range(len(playerUnits)):
                    playerUnits[x].modifyHP(xDmg,0.0,"brains")

            enemyUnits[0].modifyHP(xDmg,0.0,"brains")

        if Taro_Stats.taroTuna:
            $xStr = playerUnits[2].name
            Narrator "[xStr] shields the party from recoil!"
        else:
            Narrator "Everyone takes damage!"

    $playerUnits[1].DiminishModifiers([2,3,4,5])

    jump expression currentLabelET

label FIGHT_00B_MADLAS_JAMIE_1:
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

    Narrator "[eName] takes [eDmg] damage! [pName] takes [sfxDmg] recoil damage!"
    $ToggleBarState([1], 0)

    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $playerUnits[1].modifyStatMod("guts",-1,-4,4)

    $playerUnits[1].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00B_MADLAS_JAMIE_2:
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
        $playerUnits[2].modifyHP(xHeal,0.0,"guts")

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

# ------------------------------------------------------------------------- TARO
label FIGHT_00B_MADLAS_TARO_0:
    python:
        pName = playerUnits[2].name
        eName = enemyUnits[targetChoice].name
        #Damage Calclulation
        xDmg = -(renpy.random.randint(4,7) + playerUnits[2].cPower("brawn"))

        #Multiplies Base Damage if Taro is at low health
        xDmg = playerUnits[2].pounceMult(xDmg)

        #All Taro's Moves except tuna defender set the defending state off
        Taro_Stats.taroTuna = False

    if isRollSuccess:
        python:
            #damage
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")
            xStr = renpy.random.choice([pName + " rears back and pounces, scratching " + eName + " across the face, dealing",pName + " leaps up and scratches " + eName + " for"])

        Narrator "[xStr] [sfxDmg] damage!"
    else:
        python:
            #Halves Damage on Failure
            xDmg= int(0.5*xDmg)
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

        Narrator "[pName] goes for the throat! But her claws just barely swipe [eName] for [sfxDmg] damage!"

        Taro "I’ll turn you into kitty litter another day."

    $playerUnits[2].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_00B_MADLAS_TARO_1: ##Taro's Tuna Defender
    $pName = playerUnits[2].name
    #taroTuna is used to check if this move is active
    $Taro_Stats.taroTuna = True

    if isRollSuccess:
        Narrator "[pName] flops cutely, making her fur fluff up in defense!"

        Taro "This feline’s feeling fortified!"

        #Raises Taro's Defense on a success
        $playerUnits[2].modifyStatMod("defense",1,-4,4)
    else:
        #Lowers Taro's defense and raises her power on a failure
        Narrator "[pName] makes a show of her powerful paws!"

        Taro "My claws are getting sharper!"

        $playerUnits[2].modifyStatMod("power",2,-4,4)
        $playerUnits[2].modifyStatMod("defense",-1,-4,4)


    jump expression currentLabelET

label FIGHT_00B_MADLAS_TARO_2: ##Taro's Jeer
    #All Taro's Moves except tuna defender set the defending state off
    $eName = enemyUnits[0].name

    $Taro_Stats.taroTuna = False

    if isRollSuccess:
        #Sets Madhouse emote
        $xStr = renpy.random.choice(["Check this out. Hey ecto cooler! You look like an anthropomorphic string bean!","Your hat has more personality than you!","Your hand's too big for your face!","Reality check,, nobody listened to your show to begin with!","It's called the Phantom Frequency because nobody cares!","You sound like you eat glass on the reg!"])
        $yStr = renpy.random.choice(["Pssssht. Nice try, but I’m not that easy.","Hah! You think that’s gonna get me?","SHUT UP!", "LA LA LA,, I'm not {sc=4}LISTENING.{/sc}"])
        $zStr = renpy.random.choice(["A single tear rolls down "+enemyUnits[0].name+"’s cheek.","The demon stifles a feeble sob.",enemyUnits[0].name+" grimaces and curses under his breath."])

        Taro "[xStr]"

        Madlas "[yStr]"

        Narrator "[zStr]"

        #Modifies dem stats
        $enemyUnits[0].modifyStatMod("diff",-1,-4,4)
        $enemyUnits[0].modifyStatMod("power",-2,-4,4)
    else:

        Taro "You’re so… You! Uhm, gimme’ a minute to come up with something."

        Madlas "You’re wastin’ my time kitty cat."

        $enemyUnits[0].modifyStatMod("power",2,-4,4)

    $playerUnits[2].DiminishModifiers([2,3,5])
    jump expression currentLabelET


# ----------------------------------------------------------------------- MADLAS
label FIGHT_00B_MADLAS_MD_ATTACK:
    $bossName = enemyUnits[0].name
    $CheckForGameOvers()
    play sfx boss_target_sfx
    python:
        if currentCA == 1:
            xAtk = renpy.random.choice([2,3,3])
        if currentCA == 2:
            xAtk = renpy.random.choice([2,0,0])
        if currentCA == 3:
            xAtk = renpy.random.choice([0,1,1])

        if (currentCA != 1 or xAtk != 3):
            eTarget = renpy.random.randint(0,1)

            while not playerUnits[eTarget].isAlive:
                eTarget = renpy.random.randint(0,2)

            eTargetName = playerUnits[eTarget].name
            HighlightPlayerUnitBars([eTarget])

    call expression "FIGHT_00B_MADLAS_MD_" + str(xAtk) from _call_expression_35
    if not enemyUnits[0].isAlive:
        $mm_rank = calcRank(mD_turncount,30,25,20,15,13)

        Narrator "Turn Count: [mD_turncount] Rank: [mm_rank]"
        return

    jump expression currentLabelPT

label FIGHT_00B_MADLAS_MD_0:
    python: #Calculate Damage and Highlight Bar

        xDmg = -(renpy.random.randint(3,6) + enemyUnits[0].cPower("brawn"))

    Narrator "[bossName] looks to [eTargetName] and wildly slashes his claws through the air!"

    if Taro_Stats.taroTuna and eTarget != 2:#Switches Target and says a special line on Taro Defender
        $eTarget = 2
        $eTargetName = playerUnits[eTarget].name
        $HighlightPlayerUnitBars([eTarget])
        Narrator "[eTargetName] steps in the way of the attack!"

        Taro "No need to fear! Taro is here!"

    call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("hustle"), "Phantom Slash") from _call_dice_roll_19

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

    return

label FIGHT_00B_MADLAS_MD_1:
    $xDmg = -(renpy.random.randint(8,10))
    Narrator "[bossName] cackles as he chucks an oversized stereo speaker at [eTargetName]!"

    if Taro_Stats.taroTuna and eTarget != 2:#Switches Target and says a special line on Taro Defender
        $eTarget = 2
        $eTargetName = playerUnits[eTarget].name
        $HighlightPlayerUnitBars([eTarget])
        Narrator "[eTargetName] steps in the way of the attack!"

        Taro "No need to fear! Taro is here!"

    call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_20
    show MMFight_Chair at MMFight_LeftProp_Exit
    show MMFight_Speaker at MMFight_RightProp_Exit
    if isRollSuccess:
        if Taro_Stats.taroTuna:
            $HighlightEnemyUnitBars([0])
            $enemyUnits[0].modifyHP(xDmg,0.0,"guts")

            Narrator "[eTargetName] catches the speaker and throws it back at [bossName] who takes it in the face and takes [sfxDmg] damage!"
        else:
            $xStr = renpy.random.choice(["scrambles out of the way, ducking behind a desk.","shields their face from the sparks and broken parts, taking no damage.","gracefully slips out of the way.", "steps back as the hit completely whiffs, shattering against the ground, grimacing at the collateral damage."])
            Narrator "[eTargetName] [xStr]"
    else: #Damage on failure
        $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
        $xStr = renpy.random.choice(["takes a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])

        camera at camera_shake
        Narrator "[eTargetName] [xStr] [sfxDmg] damage!"


    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry

    return

label FIGHT_00B_MADLAS_MD_2:
    Narrator "[bossName] tries to bore [eTargetName] to death."

    if Taro_Stats.taroTuna and eTarget != 2:#Switches Target and says a special line on Taro Defender
        $eTarget = 2
        $eTargetName = playerUnits[eTarget].name
        $HighlightPlayerUnitBars([eTarget])
        Narrator "[eTargetName] steps in the way of the attack!"

        Taro "No need to fear! Taro is here!"

    call dice_roll(playerUnits[eTarget].cStats("brains"), enemyUnits[0].cDifficulty("brains"), "Lore Dump") from _call_dice_roll_46

    if isRollSuccess:
        Narrator "[eTargetName] holds their ground."
    else:
        if eTarget == 0:
            Robyn "I feel my brain shutting off"
        elif eTarget == 1:
            Jamie "Atlas,, no... not-., again."
        else:
            Taro "No more words… So tired."

        python:
            xDmg = -(renpy.random.randint(4,6) + enemyUnits[0].cPower("occult"))
            playerUnits[eTarget].modifyHP(xDmg,0.0,"brains")

        Narrator "[eTargetName] takes [sfxDmg] boredom damage!"

        if playerUnits[eTarget].Stamina != 0:
            $playerUnits[eTarget].Stamina = 0
            Narrator "[eTargetName]'s stamina is set to 0."
    return

label FIGHT_00B_MADLAS_MD_3:
    #pump up

    Atlas "{sc=3}CRUSH THEIR SKULLS, FRIEND! LET THEIR BLOOD FUEL YOUR POWER!{/sc}"

    Madhouse "NOW YOU'RE TALKING."

    python:
        enemyUnits[0].modifyStatMod("occult",2,-4,4)
        enemyUnits[0].modifyStatMod("brawn",2,-4,4)

    return
