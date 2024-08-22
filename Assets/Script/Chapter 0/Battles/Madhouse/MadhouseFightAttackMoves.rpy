#Robyn's Moves -----------------------------------------------------------------
label FIGHT_01_MM_ROBYN_0: ##Robyn's Bash. -- NEEDS TEXT
    $eName = enemyUnits[targetChoice].name
    $pName = playerUnits[0].name

    if isRollSuccess:
        python:
            #Update Demon Madhouse Expression
            MMD_State["hurt"] = True
            MMD_State["glitch"] = 1

            #Enemy Damage
            xDmg = -(renpy.random.randint(4,6) + playerUnits[0].cPower("brawn"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

        show demon_madhouse at MMD_Damaged_Pos

        Narrator "[pName] successfully bash [eName] with a thwack, dealing [sfxDmg] damage!"

        #Modify Mahouse Stat
        $enemyUnits[targetChoice].modifyStatMod("power",-1,-4,4)
    else:
        Narrator "Swing{w=.5} And a miss! [eName]’s eyes are on [pName] now."

        #Modify Mahouse Stat
        $enemyUnits[targetChoice].modifyStatMod("diff",-2,-4,4)

    $playerUnits[0].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_ROBYN_1: ##Robyn's Cheer.

    python:
        playerUnits[0].DiminishModifiers([2,3,5])

        eName = enemyUnits[0].name
        pName = playerUnits[0].name

        if targetChoice != -1:
            xArray = ["C’mon, me, you’ve got this!", "You’ve got so much junk food to live for, Atlas!", "Show ‘em what Jersey’s made of, Jamie!", "Taro, Taro, you’re so great! Scratch that guy right in the face!"]
            xStr = xArray[targetChoice]
        else:
            xStr = "We’ve got this, everyone!"

    Robyn "[xStr]"

    if targetChoice == -1: #Multi-Target
        #Increases everyone's power by +1
        python:
            for x in range(len(playerUnits)):
                playerUnits[x].modifyStatMod("power",1,-4,4)

    else: #Single Target
        python:
            #Heals Target
            xName = playerUnits[targetChoice].name
            HighlightPlayerUnitBars([targetChoice])
            xHeal = renpy.random.randint(3,7)

            if xHeal <= 0:
                xHeal = 1

            playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        Narrator "[pName] uses the power of positivity to heal [xName]'s for [xHeal] [kwHealth]!"

        $playerUnits[targetChoice].modifyStatMod("power",2,-4,4)

    if not isRollSuccess:
        Narrator "[eName] takes [pName]'s words the wrong way and is also invigorated!!"

        $enemyUnits[0].modifyStatMod("power",2,-4,4)



    jump expression currentLabelET

label FIGHT_01_MM_ROBYN_2: ##Robyn's Focus. -- NEEDS TEXT
    $pName = playerUnits[0].name
    if isRollSuccess:
        #Raises Karma on success
        Narrator "[pName] thinks REAL hard to collect [PCtheir] thoughts about what to do next."

        Robyn "Think, think, think… I’ve got it!"

        $addBattleKarma(2)

    else:
        #Raises Jamie's Brain's and occult on a failure
        Narrator "As [pName] tries to think as hard as [PCthey] can, [pName] is worn out in the process."

        Robyn "Can’t. Focus. Brain. Foggy."

        Jamie "Don’t strain yourself, boss, I’ll take it from here."

        python:
            xName = playerUnits[2].name
            Jamie_Stats.modifyStatMod("brawn",2,-4,4)
            Jamie_Stats.modifyStatMod("occult",2,-4,4)

    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_01_MM_ROBYN_3: ##Robyn's Heart Out.
    python:
        pName = playerUnits[0].name
        eName = enemyUnits[0].name

    if isRollSuccess:
        $xStr = renpy.random.choice(["You’re completely unstable! I don’t know how much more your soul can take!","Are you even listening to me?!","Mike, you’re going to get hurt!","Mike, I lied! I’ve literally never heard of you or your show! I was just trying to make you and Atlas happy!"])
        Robyn "[xStr]"

        $xStr = renpy.random.choice([eName + " tenses up, hesitating a moment as he feels a twinge of guilt.","The demon reels back, bringing a hand to his face with a pained growl.","The demon’s chest aches, hearing these words make his head spin and his blood boil. A small part of " + eName + " wants to cry."])
        Narrator "[xStr]"

        Madhouse "I can’t give up."

        python:
            #Fucks with Madhouse on a success
            enemyUnits[0].ChangeMTA(1)
            enemyUnits[0].modifyStatMod("diff",-2,-4,4)
            enemyUnits[targetChoice].modifyStatMod("brawn",-2,-4,4)

        Narrator "[eName]'s turn is delayed by +1."
    else:
        $xStr = renpy.random.choice(["Mike roars, drowning out " + pName + "'s words.","The demon growls, refusing to listen."])
        Narrator "[xStr]"

        python:
            enemyUnits[0].modifyStatMod("diff",2,-4,4)
            enemyUnits[0].ChangeMTA(-1)

        Narrator "[eName]'s turn is hastened by +1."

    $playerUnits[0].DiminishModifiers([2,3,5])
    jump expression currentLabelET

#Taro's Moves ------------------------------------------------------------------
label FIGHT_01_MM_TARO_0: ##Taro's Pounce -- NEEDS TEXT
    python:
        pName = playerUnits[3].name
        eName = enemyUnits[targetChoice].name
        #Damage Calclulation
        xDmg = -(renpy.random.randint(4,7) + playerUnits[3].cPower("brawn"))

        #Multiplies Base Damage if Taro is at low health
        xDmg = playerUnits[3].pounceMult(xDmg)


        #Sets Madhouse emote
        MMD_State["hurt"] = True
        MMD_State["glitch"] = 1

        #All Taro's Moves except tuna defender set the defending state off
        Taro_Stats.taroTuna = False

    if isRollSuccess:
        python:
            #damage
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")
            xStr = renpy.random.choice([pName + " rears back and pounces, scratching " + eName + " across the face, dealing",pName + " leaps up and scratches " + eName + " for"])

        show demon_madhouse at MMD_Damaged_Pos
        Narrator "[xStr] [sfxDmg] damage!"
    else:
        python:
            #Halves Damage on Failure
            xDmg= int(0.5*xDmg)
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")

        Narrator "[pName] goes for the throat! But her claws just barely swipe [eName] for [sfxDmg] damage!"

        Taro "I’ll turn you into kitty litter another day."

    $playerUnits[3].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_TARO_1: ##Taro's Tuna Defender
    $pName = playerUnits[3].name
    #taroTuna is used to check if this move is active
    $Taro_Stats.taroTuna = True

    if isRollSuccess:
        Narrator "[pName] flops cutely, making her fur fluff up in defense!"

        Taro "This feline’s feeling fortified!"

        #Raises Taro's Defense on a success
        $playerUnits[3].modifyStatMod("defense",1,-4,4)
    else:
        #Lowers Taro's defense and raises her power on a failure
        Narrator "[pName] makes a show of her powerful paws!"

        Taro "My claws are getting sharper!"

        $playerUnits[3].modifyStatMod("power",2,-4,4)
        $playerUnits[3].modifyStatMod("defense",-1,-4,4)


    jump expression currentLabelET

label FIGHT_01_MM_TARO_2: ##Taro's Jeer
    #All Taro's Moves except tuna defender set the defending state off
    $eName = enemyUnits[0].name

    $Taro_Stats.taroTuna = False

    if isRollSuccess:
        #Sets Madhouse emote
        $MMD_State["hurt"] = True
        $MMD_State["glitch"] = 1
        $xStr = renpy.random.choice(["Check this out. Hey ecto cooler! You look like an anthropomorphic string bean!","Mike Madhouse? More like Mike needs a Bathhouse, cause you stink!","Your hat has more personality than you!","Your hand's too big for your face!","Reality check,, nobody listened to your show to begin with!","It's called the Phantom Frequency because nobody cares!","You sound like you eat glass on the reg!"])
        $yStr = renpy.random.choice(["Pssssht. Nice try, but I’m not that easy.","Hah! You think that’s gonna get me?","SHUT UP!", "LA LA LA,, I'm not {sc=4}LISTENING.{/sc}"])
        $zStr = renpy.random.choice(["A single tear rolls down " + eName + "’s cheek.","The demon stifles a feeble sob.", eName + " grimaces and curses under his breath."])



        Taro "[xStr]"

        Madhouse "[yStr]"

        Narrator "[zStr]"

        #Modifies dem stats
        $enemyUnits[0].modifyStatMod("diff",-1,-4,4)
        $enemyUnits[0].modifyStatMod("power",-2,-4,4)
    else:

        Taro "You’re so… You! Uhm, gimme’ a minute to come up with something."

        Madhouse "You’re wastin’ my time kitty cat."

        $enemyUnits[0].modifyStatMod("power",2,-4,4)

    $playerUnits[3].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_01_MM_TARO_3: ##Taro's HexFlare -- NEEDS TEXT
    python:
        pName = playerUnits[3].name
        eName = enemyUnits[0].name

        #Sets Madhouse emote
        MMD_State["hurt"] = True
        MMD_State["glitch"] = 1

        #All Taro's Moves except tuna defender set the defending state off
        Taro_Stats.taroTuna = False

        #Damage!!!
        xDmg = -(renpy.random.randint(2,5) + playerUnits[3].cPower("occult"))
        enemyUnits[targetChoice].modifyHP(xDmg,0.0,"brains")

    show demon_madhouse at MMD_Damaged_Pos
    Narrator "HexFlare is performed! [eName] takes [sfxDmg] damage!"

    python:
        #Stat Modifications
        playerUnits[3].modifyStatMod("brawn",2,-4,4)

        if not isRollSuccess:
            playerUnits[3].modifyStatMod("guts",-2,-4,4)
            playerUnits[3].modifyStatMod("brains",-2,-4,4)

        playerUnits[3].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET


#Jamie's Moves -----------------------------------------------------------------
label FIGHT_01_MM_JAMIE_0: ##Jamie's Spirit Blaze. -- NEEDS TEXT
    python:
        HighlightPlayerUnitBars([2])
        pName = playerUnits[2].name
        eName = enemyUnits[0].name
        Jamie_Stats.iconState = 3

    #Calculates Damage
    $xDmg = -(renpy.random.randint(7,10) + playerUnits[2].cPower("occult"))
    $xStr = renpy.random.choice(["Reaching up, " +pName+ " cups the flame in their hands and whispers a spell, the small flame dancing forward before exploding into a wild burst of hellfire.", "Swiping their hand through the air, " +pName+ " unleashes a raging bolt of blue hellfire."])

    Narrator "[xStr]"

    #Sets Madhouse emote
    $MMD_State["hurt"] = True
    $MMD_State["glitch"] = 1

    if isRollSuccess:
        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")

        show demon_madhouse at MMD_Damaged_Pos
        Narrator "[eName] is engulfed in a pale blue light and takes a hefty [sfxDmg] damage!"

        if renpy.random.choice([True,False]):
            Narrator "[pName] whispers to the flame resting in their hands. It flickers before exploding in a ray of hellfire."

            Jamie "Thanks little friend."
    else:
        Narrator "The flames roar out of control!"
        camera at camera_shake
        $HighlightPlayerUnitBars([0,1,2,3])
        #Halves Damage on a failure
        if Taro_Stats.taroTuna: #Taro intervenes on a failure
            $playerUnits[3].modifyHP(xDmg,0.0,"brains")
        else:
            python:
                xDmg = int(-0.75*(renpy.random.randint(7,9) + playerUnits[2].cPower("occult")))
                for x in range(len(playerUnits)):
                    playerUnits[x].modifyHP(xDmg,0.0,"brains")


        $enemyUnits[0].modifyHP(xDmg,0.0,"brains")

        show demon_madhouse at MMD_Damaged_Pos
        if Taro_Stats.taroTuna:
            $xStr = playerUnits[3].name
            Narrator "[xStr] shields the party from recoil!"
        else:
            Narrator "Everyone takes damage!"

    $playerUnits[2].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_JAMIE_1: ##Jamie's Skull Cracker. -- NEEDS TEXT
    #Damage!!!
    python:
        pName = playerUnits[2].name
        eName = enemyUnits[0].name
    $HighlightPlayerUnitBars([2])
    Narrator "[pName] bashes their skull into [eName]’s head with precision roughness!"

    $xDmg = -(renpy.random.randint(4,6) + playerUnits[2].cPower("brawn"))
    $enemyUnits[targetChoice].modifyHP(xDmg,1.0,"guts")
    $eDmg = sfxDmg

    if isRollSuccess:
        $xDmg= int(0.5*xDmg)

    $playerUnits[2].modifyHP(xDmg,1.0,"guts")


    #Sets Madhouse emote
    $MMD_State["hurt"] = True
    $MMD_State["glitch"] = 1
    camera at camera_shake
    show demon_madhouse at MMD_Damaged_Pos
    Narrator "[eName] takes [eDmg] damage! [pName] takes [sfxDmg] recoil damage!"

    #Modify Defense
    $enemyUnits[targetChoice].modifyStatMod("guts",-2,-4,4)

    if not isRollSuccess:
        $playerUnits[2].modifyStatMod("guts",-1,-4,4)

    $playerUnits[2].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_JAMIE_3: ##Jamie's Iron Tether.
    #Sets Madhouse emote
    $MMD_State["hurt"] = True
    $MMD_State["glitch"] = 1
    $eName = "ERROR"

    #Damage Calculation
    $xDmg = -(renpy.random.randint(2,5) + playerUnits[2].cPower("brawn"))

    show demon_madhouse at MMD_Damaged_Pos
    if isRollSuccess: #DO be damaging
        $enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")


        Narrator "Iron Tether is performed! [eName] takes [sfxDmg] damage!"

        $enemyUnits[0].modifyStatMod("occult",-2,-4,4)

        python:
            xDmg = -(renpy.random.randint(2,4) + playerUnits[2].cPower("occult"))
            enemyUnits[targetChoice].modifyHP(xDmg,0.5,"brains")


        Narrator "The second hit does [sfxDmg] damage!"
    else: #Half Damage on Failure
        python:
            xDmg= int(0.5*xDmg)
            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")


        Narrator "Iron Tether has failed. [eName] takes [sfxDmg] damage!"

        python:
            xDmg = -(renpy.random.randint(0,3) + playerUnits[2].cPower("occult"))
            xDmg= int(0.5*xDmg)
            enemyUnits[targetChoice].modifyHP(xDmg,0.5,"brains")


        Narrator "The second hit does [sfxDmg] damage!"

    $playerUnits[2].DiminishModifiers([1,2,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_JAMIE_2: ##Jamie's Healing Wave.
    $pName = playerUnits[2].name
    #Calculate Healing for single target
    if targetChoice != -1:
        $xHeal = renpy.random.randint(6,9) + playerUnits[2].cPower("occult")
        $xName = playerUnits[targetChoice].name
        $HighlightPlayerUnitBars([targetChoice])

        #Halve Healing on fail
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)
    else:
        $HighlightPlayerUnitBars([0,1,2,3])

    if targetChoice == -1: #Multi Target
        $xHeal = renpy.random.randint(2,4) + playerUnits[2].cPower("occult")
        if not isRollSuccess:
            $xHeal= int(0.5*xHeal)

        $playerUnits[0].modifyHP(xHeal,0.0,"guts")
        $playerUnits[1].modifyHP(xHeal,0.0,"guts")
        $playerUnits[2].modifyHP(xHeal,0.0,"guts")
        $playerUnits[3].modifyHP(xHeal,0.0,"guts")


        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over their allies, mending some of their wounds."
    else: #Single Target
        $playerUnits[targetChoice].modifyHP(xHeal,0.0,"guts")

        Narrator "[pName] closes their eyes, and the flame between their horns casts a cool light over [xName], healing them for [xHeal] [kwHealth]."

    if not isRollSuccess:
        $xStr = renpy.random.choice(["...Can you all shut up?!","Mmmrgh...","I am TRYING to cast a spell.","I… can’t do this.","Goddammit!"])

        Narrator "They growl, unable to focus any further."

        Jamie "[xStr]"
    else:
        Jamie "I hope this helps."

    $playerUnits[2].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

#Atlas' Moves ------------------------------------------------------------------
label FIGHT_01_MM_ATLAS_0: ##Atlas' Lore Dump.
    #Delay

    $pName = playerUnits[1].name
    $eName = enemyUnits[0].name
    $xStr = renpy.random.choice(["Guys, I'm pretty sure my dad is an intergalactic fugitive,, he's never actually talked to me about it but I've got this hunch-","What does it all mean? Personally, I find comfort in the people I surround myself with-","Jamie I stress ate your winter jacket and I've been too nervous to tell you I-","In episode 301 of Slagnar the Werewolf Lover Barbarian, it’s revealed that Slagnar’s mom is ACTUALLY-"])
    $xDmg = -(renpy.random.randint(1,3) + playerUnits[1].cPower("brains"))

    if isRollSuccess:
        Narrator "[pName] begins his rambling, making [eName] get sleepy."

        Atlas "[xStr]"

        Madhouse "No, dude, stop. It’s too dorky-., Getting… Sleepy. Zzzz..."
    else:
        Narrator "[pName] rambles begins putting everyone to sleep."

        Atlas "[xStr]"
        $xNum = renpy.random.choice([True,False])
        $yNum = renpy.random.choice([True,False])

        if xNum:
            Robyn "I feel my brain shutting off"
        else:
            Taro "No more words… So tired."

        if yNum:
            Jamie "Atlas,, no... not-., again."
        else:
            Madhouse "What a... dork."

        #KILL STAMINA
        $HighlightPlayerUnitBars([0,2,3])
        $playerUnits[0].Stamina = 0
        $playerUnits[2].Stamina = 0
        $playerUnits[3].Stamina = 0
        Narrator "Everyone but [pName]'s stamina is set to 0."


        Atlas "Wait, guys! I wasn’t done!"

    $enemyUnits[targetChoice].modifyHP(xDmg,1.0,"brains")
    Narrator "[eName] takes [sfxDmg] boredom damage!"

    $enemyUnits[0].ChangeMTA(3)
    Narrator "[eName]'s turn is delayed by +3 turns."

    $playerUnits[1].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_01_MM_ATLAS_1: ##Atlas' Kinesis. -- NEEDS TEXT
    python:

        pName = playerUnits[1].name
        eName = enemyUnits[0].name
    $Atlas_Stats.iconState = 3

    #Calculate damage and Hurt Enemy
    $xDmg = -(renpy.random.randint(10,12) + playerUnits[1].cPower("occult"))
    $HighlightPlayerUnitBars([1])

    if usedKinesis:
        Narrator "Lunging at the mothman, [eName] is struck with a crushing supernatural force. [eName] grasps his chest and wheezes."
    else:
        python:
            isRollSuccess = True
            usedKinesis = True
            Atlas_Stats.SetAttackMoves(['Lore Dump', 'Kinesis', 'Pump Up'], 'FIGHT_01_MM_ATLAS_')

        Narrator "[pName] jerks to one side and his red eyes flicker to a hazy green. \n\n He reaches towards the demon and speaks."

        Atlas "Maddie I'm hurt you'd turn on us like that! I know you're struggling but, we're like your {i}biggest fans!{/i} Can't we talk about this over some drinks? Let's kiss an make up! \n\n You can autograph my shirt!"
        Madhouse "I {b}don't{/b} know you."

        Narrator "Lunging at the mothman, [eName] is struck down by a crushing supernatural force. \n\n [eName] grasps his chest and wheezes."

        Madhouse "What the hell?!"

        Narrator "Atlas staggers back and shakes his head."

        Atlas "Huh?"


    #Sets Madhouse emote
    $MMD_State["hurt"] = True
    $MMD_State["glitch"] = 1

    $enemyUnits[targetChoice].modifyHP(xDmg,0.0,"brains")
    camera at camera_shake
    if isRollSuccess: #Halve Recoil on success
        $eDmg = sfxDmg
        $xDmg= int(0.3*xDmg)
        $playerUnits[1].modifyHP(xDmg,1.0,"brains")

        show demon_madhouse at MMD_Damaged_Pos
        Narrator "[eName] takes [eDmg] damage, and [pName] coughs up ectoplasm taking [sfxDmg] recoil damage!"
    else:
        $eDmg = sfxDmg
        $xDmg= int(0.6*xDmg)
        $playerUnits[1].modifyHP(xDmg,1.0,"brains")

        Narrator "[eName] takes [eDmg] damage, and [pName] coughs up ectoplasm taking [sfxDmg] recoil damage!"

        #Muder Atlas' Brains on failure
        $playerUnits[1].modifyStatMod("brains",-2,-4,4)

    #Stat Change
    $enemyUnits[targetChoice].modifyStatMod("brains",-2,-4,4)
    $ToggleBarState([2], 0)
    $playerUnits[1].DiminishModifiers([2,3,4,5])
    jump expression currentLabelET

label FIGHT_01_MM_ATLAS_2: ##Atlas' Pump Up. -- NEEDS TEXT
    $pName = playerUnits[1].name
    $xName = playerUnits[2].name


    if isRollSuccess:
        Narrator "[pName] knows exactly what to say to get [xName] excited!"

        Atlas "{sc=3}CRUSH THEIR SKULLS, FRIEND! LET THEIR BLOOD FUEL YOUR POWER!{/sc}"

        Jamie "Hell yes, let’s do this."

        python:
            #Pump up jamie's stats more on a success!
            playerUnits[2].modifyStatMod("occult",2,-4,4)
            playerUnits[2].modifyStatMod("brawn",2,-4,4)
            playerUnits[2].modifyStamina(1)
        Narrator "[xName] regains +1 Stamina"
    else:
        Narrator "[pName] thinks of ways to get [xName] excited but can't come up with anything good."

        Atlas "Go beat them up or whatever you do!"

        Jamie "Eh, the effort is there. Thank you, friend."

        python:
            #Pump Up Jamie's Stats
            playerUnits[2].modifyStatMod("occult",1,-4,4)
            playerUnits[2].modifyStatMod("brawn",1,-4,4)

    $playerUnits[1].DiminishModifiers([2,3,5])
    jump expression currentLabelET

label FIGHT_01_MM_ATLAS_3: ##Atlas' Cryptic Collection.
    python:
        #Randomize Line
        xStr = renpy.random.choice(["plucks","pulls","yoinks"])
        yStr = renpy.random.choice(["a vial of oil","a stick of iron","a piece of chalk","a salt shaker","a lanyard with his house keys"])
        zStr = renpy.random.choice(["Eat this!","Never meet your heroes!","You. Made. Jamie. CRY!","Guess this’ll work."])

        #Sets Madhouse emote
        MMD_State["hurt"] = True
        MMD_State["glitch"] = 1

    Narrator "Reaching into his neck fluff, Atlas digs a claw around and [xStr] out [yStr]. He then balls up his feathery fist and flings the object at the phantom."

    Atlas "[zStr]"

    if isRollSuccess:
        python:
            #Calculate and Do damage
            xDmg = -(renpy.random.randint(6,9))

            enemyUnits[targetChoice].modifyHP(xDmg,0.0,"guts")


        show demon_madhouse at MMD_Damaged_Pos
        Narrator "The item soars through the air and perfectly falls into Mike’s open mouth. The phantom gags and coughs hard, taking [sfxDmg] damage!"

        Narrator "Atlas gives himself a high five."


        $enemyUnits[targetChoice].modifyStatMod("brawn",1,-4,4)

        $enemyUnits[targetChoice].modifyStatMod("brains",-1,-4,4)
    else: #Nothing happens on a failure
        $zStr = renpy.random.choice(["Nooo! That cost me like fifteen bucks!","Curse these wing hands!","I’m totally off my game."])


        Narrator "It goes wide, clattering somewhere amongst the rubble."

        Atlas "[zStr]"

    $playerUnits[1].DiminishModifiers([1,3,4,5])
    jump expression currentLabelET

#Madhouse's Moves --------------------------------------------------------------
label FIGHT_01_MM_MM_ATTACK:
    $CheckForGameOvers()
    show demon_madhouse at MMD_Attack_Pos
    play sfx boss_target_sfx
    python:
        #Madhouse Attack Emote

        MMD_State["glitch"] = 1
        MMD_State["eye"] = 1
        MMD_State["mouth"] = 1

        #Attack Choice
        xAtk = renpy.random.choice([0,0,0,0,1,1,1,2,2,3])

        #Target Choice
        eTarget = [playerUnits[0].calcAggro(),playerUnits[1].calcAggro(),playerUnits[2].calcAggro(),playerUnits[3].calcAggro()]
        eTarget = AIChooseTarget(eTarget)

        while not playerUnits[eTarget].isAlive:
            eTarget = renpy.random.randint(0,3)

        if eTarget == 1 and xAtk == 2:
            xAtk = 0

        eTargetName = playerUnits[eTarget].name

    if xAtk == 0: #Phantom Slash
        call FIGHT_01_MM_MM_ATTACK_1 from _call_FIGHT_01_MM_MM_ATTACK_1

    elif xAtk == 1: #Noxious Blast
        call FIGHT_01_MM_MM_ATTACK_2 from _call_FIGHT_01_MM_MM_ATTACK_2

    elif xAtk == 2: #Psycho Toss
        call FIGHT_01_MM_MM_ATTACK_3 from _call_FIGHT_01_MM_MM_ATTACK_3

    else: #Psycho Spin Needs Text
        $eName = enemyUnits[0].name
        Narrator "[eName] cackles!"
        $enemyUnits[0].modifyStatMod("diff",1,-4,4)

        #call FIGHT_01_MM_MM_ATTACK_4 from _call_FIGHT_01_MM_MM_ATTACK_4


    #$MMD_State["frenzy"] = False
    $MMD_State["eye"] = 0
    $MMD_State["mouth"] = 0
    jump expression currentLabelPT

label FIGHT_01_MM_MM_ATTACK_1:
    python: #Calculate Damage and Highlight Bar
        HighlightPlayerUnitBars([eTarget])
        xDmg = -(renpy.random.randint(4,7) + enemyUnits[0].cPower("brawn"))

    Narrator "[eName] looks to [eTargetName] and slashes his claw through the air!"
    if Taro_Stats.taroTuna and eTarget != 3:#Switches Target and says a special line on Taro Defender
        $eTarget = 3
        $eTargetName = playerUnits[eTarget].name
        $HighlightPlayerUnitBars([eTarget])
        Narrator "[eTargetName] steps in the way of the attack!"

        Taro "No need to fear! Taro is here!"
    else:
        Madhouse "This is for the fans!"

    #Dice Roll
    call dice_roll(playerUnits[eTarget].cStats("hustle"), enemyUnits[0].cDifficulty("hustle"), "Phantom Slash") from _call_dice_roll_9

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

label FIGHT_01_MM_MM_ATTACK_2:
    $HighlightPlayerUnitBars([0,1,2,3])
    Narrator "The demon gargles, craning his head back before exhaling a cloud of noxious waste."

    if Taro_Stats.taroTuna: #Taro protects everyone
        $HighlightPlayerUnitBars([3])
        Narrator "Taro steps in to protect everyone!"
        #Calculate Damage & Highlight Taro

        $xDmg = -(renpy.random.randint(6,9) + enemyUnits[0].cPower("occult"))

        #Roll
        call dice_roll(playerUnits[3].cStats("guts"), enemyUnits[0].cDifficulty("occult"), "Noxious Blast") from _call_dice_roll_10

        if isRollSuccess: #Half Damage on success
            $xDmg= int(0.5*xDmg)
            $playerUnits[3].modifyHP(xDmg,0.0,"brains")
        else: #Damage bby
            $playerUnits[3].modifyHP(xDmg,0.0,"brains")


        camera at camera_shake
        Narrator "A toxic haze falls over the party, but Taro takes the brunt of the poison. She's hit with [sfxDmg] damage!"

    else: #Everyone is fucked
        python: #Calculate xMod
            xGuts = 0
            xAlive = 0

            for x in range(len(playerUnits)):
                if playerUnits[x].isAlive:
                    xGuts+=playerUnits[x].cStats("guts")
                    xAlive+=1

            xGuts = int(xGuts/xAlive)

        #Roll
        call dice_roll(xGuts, enemyUnits[0].cDifficulty("occult"), "Noxious Blast") from _call_dice_roll_11

        #Take Damage
        $xDmg = -(renpy.random.randint(5,8) + enemyUnits[0].cPower("occult"))

        #Third Damage on success
        if isRollSuccess:
            $xDmg= int(0.33*xDmg)

        if playerUnits[0].isAlive:
            $playerUnits[0].modifyHP(xDmg,0.0,"brains")

        if playerUnits[1].isAlive:
            $playerUnits[1].modifyHP(xDmg,0.0,"brains")

        if playerUnits[2].isAlive:
            $playerUnits[2].modifyHP(xDmg,0.0,"brains")

        if playerUnits[3].isAlive:
            $playerUnits[3].modifyHP(xDmg,0.0,"brains")


        camera at camera_shake
        Narrator "A toxic haze falls over the party, coughing and sputtering as they take damage."
    return

label FIGHT_01_MM_MM_ATTACK_3:
    python: #Calculate Damage
        xDmg = -(renpy.random.randint(6,10))
        atlasHelp = False

        HighlightPlayerUnitBars([eTarget])
        xStr = renpy.random.choice(["Gritting his teeth, Mike jerks to one side and lifts a loud speaker with his mind.","Balling up his fists, Mike slams his fist down and the speaker follows, smashing into the floor with a shower of splintered parts.","Raking his claws through the air, Mike tears the giant analog mixing board out of the wall and flings it at the party. It crunches against the floor, buttons and wires splintering.","Mike scoops up a hefty effects rack off the floor and slams it against the wall, sparks showering from the electrical carnage."])

    Madhouse "Eat this [eTargetName]!"

    Narrator "[xStr]"
    if Taro_Stats.taroTuna: #Switches Target to Taro if she's taro defender
        if eTarget != 3:
            $eTarget = 3
            $eTargetName = playerUnits[eTarget].name
            $HighlightPlayerUnitBars([eTarget])
            Narrator "Taro steps in the way of the attack!"

    elif (playerUnits[1].isAlive and not playerUnits[1].exhausted) and usedKinesis and eTarget !=1:
        $HighlightPlayerUnitBars([eTarget,1])
        $displaymenu = True
        Atlas "No, don't hurt [eTargetName]!"

        Narrator "Atlas wants to stop the attack. Do you let him?{nw}"

        menu: #Menu to decide if Atlas Should help
            extend ""

            "Yes":
                $atlasHelp = True
            "No":
                $atlasHelp = False

        $displaymenu = False

    if Taro_Stats.taroTuna: #Taro defender Needs Text
        call dice_roll(playerUnits[3].cStats("brawn"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_27
        show MMFight_Chair at MMFight_LeftProp_Exit
        show MMFight_Speaker at MMFight_RightProp_Exit
        if isRollSuccess:
            #Sets Madhouse emote
            $MMD_State["hurt"] = True
            $MMD_State["glitch"] = 1

            #Damage
            $HighlightEnemyUnitBars([0])
            $enemyUnits[0].modifyHP(xDmg,0.0,"guts")


            show demon_madhouse at MMD_Damaged_Pos
            Narrator "[eTargetName] catches the speaker and throws it back at [eName] who takes it in the face and takes [sfxDmg] damage!"

            if enemyUnits[0].cHP <= 0:
                jump Fight_01_MADHOUSE_END
        else:
            #Damage
            $playerUnits[3].modifyHP(xDmg,0.0,"guts")


            camera at camera_shake
            Narrator "[eTargetName] faces the hit head on, taking [sfxDmg] damage!"

    elif atlasHelp: #Atlas Help Needs Text
        #Roll and Highlight
        $HighlightPlayerUnitBars([1,eTarget])
        $Atlas_Stats.iconState = 3
        call dice_roll(playerUnits[1].cStats("occult"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_28
        show MMFight_Chair at MMFight_LeftProp_Exit
        show MMFight_Speaker at MMFight_RightProp_Exit
        if isRollSuccess:
            #Atlas Recoil
            $playerUnits[1].modifyHP(-renpy.random.randint(3,5),1.0,"brains")
            $Atlas_Stats.iconState = 3

            camera at camera_shake
            Narrator "Atlas takes [sfxDmg] necrotic damage, but he successfully tosses the possessed equipment aside!"
        else:
            #Atlas Recoil
            $playerUnits[1].modifyHP(-renpy.random.randint(3,5),1.0,"brains")
            $tempVar = sfxDmg
            $Atlas_Stats.iconState = 3
            $xStr = renpy.random.choice(["tanks a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])

            #Damage
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")


            camera at camera_shake
            Narrator "Atlas is overwhelmed with an undead power tanking [tempVar] damage. \n\n [eTargetName] [xStr] [sfxDmg] damage!"

    else: #No Atlas Help
        #Roll
        call dice_roll(playerUnits[eTarget].cStats("guts"), enemyUnits[0].cDifficulty("occult"), "Psycho Toss") from _call_dice_roll_29
        show MMFight_Chair at MMFight_LeftProp_Exit
        show MMFight_Speaker at MMFight_RightProp_Exit
        if isRollSuccess:
            $xStr = renpy.random.choice(["scrambles out of the way, ducking behind a desk.","shields their face from the sparks and broken parts, taking no damage.","gracefully slips out of the way.", "steps back as the hit completely whiffs, shattering against the ground, grimacing at the collateral damage."])
            Narrator "[eTargetName] [xStr]"
        else: #Damage on failure
            $playerUnits[eTarget].modifyHP(xDmg,0.0,"guts")
            $xStr = renpy.random.choice(["tanks a heavy hit, taking", "winces as they take", "gets knocked back, taking", "faces the hit head on, taking","is bonked over the head, taking"])

            camera at camera_shake
            Narrator "[eTargetName] [xStr] [sfxDmg] damage!"

    show MMFight_Chair at MMFight_LeftProp_Entry
    show MMFight_Speaker at MMFight_RightProp_Entry
    return

label FIGHT_01_MM_MM_ATTACK_4:
    $HighlightPlayerUnitBars([eTarget])
    Narrator "[eName] spins [eTargetName] around with psychic power!"

    call dice_roll(playerUnits[eTarget].cStats("guts"), enemyUnits[0].cDifficulty("occult"), "Psycho Spin") from _call_dice_roll_30


    camera at camera_dizzy

    Narrator "[eTargetName] feels sick to their stomach."
    if isRollSuccess:


        #Modify Guts
        $playerUnits[eTarget].modifyStatMod("guts",-1,-4,4)
    else:

        #Modify more stats on a failure
        $playerUnits[eTarget].modifyStatMod("guts",-1,-4,4)
        $playerUnits[eTarget].modifyStatMod("brains",-1,-4,4)
        $playerUnits[eTarget].modifyStatMod("hustle",-1,-4,4)
    return
