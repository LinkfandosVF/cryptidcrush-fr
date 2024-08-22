label InitializeBattleVariables:

    define playerUnits = []
    define enemyUnits = []
    define currentEnemyTurn = [] ##If enemy's turn is up, then itll be 0, 1,2... depending on enemyUnits list.
    define currentLabelPT = "" ##Label for the current fight's player turn
    define currentLabelET = "" ##Label for the enemy turn
    define enemyAttackUpNext =[] ##List of enemies attacking next turn.
    define playerChoice = 0
    define continueToPlayerPhase = True
    define targetChoice = 0 ## 0-10 for slots on enemy or player, -1 for everyone in either team, -2
    define isSupportMove = False
    define CallDiceRollForMove = "CallDiceRollForMove"
    define enemiesActed = [] ##Passes information which enemies acted on the same turn
    define tempVar = 0 ##Useful temporary variable that is always initialized
    define currentCA = 0 ##Says how many consecutive enemy attacks have happened.




    return

label CallDiceRollForMove: ##Calls dice roll then calls the label the move is addressed as:
    $HighlightEnemyUnitBars([])
    if(attackOptionSelected==-2):
        $CombatUnitPick()

        window hide
        $HighlightEnemyUnitBars([0,1,2,3])
        $ui.interact()
        return

    python:
        currentAttack = playerUnits[playerChoice].attacks[attackOptionSelected]
        CheckMoveTargets(currentAttack)


    if (targetChoice == -2):
        python:
            SetUpCombatMenuUI(playerUnits[playerChoice])
            toggleQuickMenu()
            HighlightEnemyUnitBars([0,1,2,3])
        window hide
        $ui.interact()
        return

    python:
        updateBarsForMove()
        TakeAwayStaminaForMove(currentAttack)


    if (targetChoice == -1 or isSupportMove or currentAttack.enemyMod == "fixed"):
        call dice_roll(playerUnits[playerChoice].cStats(currentAttack.unitMod), currentAttack.MTD, currentAttack.name) from _call_dice_roll_43
    else:
        call dice_roll(playerUnits[playerChoice].cStats(currentAttack.unitMod), enemyUnits[targetChoice].cDifficulty(currentAttack.enemyMod), currentAttack.name) from _call_dice_roll_44


    python:
        rollVoiceLine()
        renpy.jump(currentAttack.attackLabel)

    return

#label StartOfTurn: ##Shows at start of turn
default sfxDmg = 0
label playHurtSFX: #Obsolete
    return

init python:
    def resetUnitStates(turnCounter = "mm_turncount"):
        global playerUnits
        global enemyUnits

        for x in playerUnits:
            x.resetSelf()
        for x in enemyUnits:
            x.resetSelf()

        globals()[turnCounter] = 0

    def updateBarsForMove():
        global isSupportMove, targetChoice, playerChoice, enemyUnits, playerUnits

        RefreshBarHP()
        if not isSupportMove:
            if (targetChoice == -1):
                xVar = []
                for x in range(len(enemyUnits)):
                    xVar.append(x)
            else:
                xVar = [targetChoice]

            HighlightEnemyUnitBars(xVar)
            HighlightPlayerUnitBars([playerChoice])

        else:
            HighlightEnemyUnitBars([])

            if (targetChoice == -1):
                xVar = []
                for x in range(len(playerUnits)):
                    xVar.append(x)
            else:
                xVar = [targetChoice]

            xVar.append(playerChoice)
            HighlightPlayerUnitBars(xVar)

    def rollVoiceLine():
        global playerChoice
        global playerUnits
        global isRollSuccess

        if renpy.random.choice([True,True,False]):
            if isRollSuccess:
                voice(playerUnits[playerChoice].getLine("success"))
            else:
                voice(playerUnits[playerChoice].getLine("fail"))

    #-------------Setting up battle functions
    def RefreshBarHP():
        global playerUnits
        global enemyUnits
        global playerBarDHP
        global eBar_dHP

        for x in range(len(playerUnits)):
            playerBarDHP[x] = playerUnits[x].cHP

        for x in range(len(enemyUnits)):
            eBar_dHP[x] = enemyUnits[x].cHP

        return

    def PlayerTurnStart():
        HighlightEnemyUnitBars([])
        renpy.block_rollback()


        renpy.hide("powerup")
        renpy.hide("powerdown")

        ToggleBarState([1,2,3,4], 0)

        AtStartOfTurn()
        CheckForGameOvers()
        WarnPlayerOfAttacks()

    def EnemyTurnStart():
        HighlightEnemyUnitBars([])
        renpy.block_rollback() ##Prevents people from cheesing rolls..... mmmmm...... cheese.
        #At the start of turn....

        ToggleBarState([1,2,3,4], 0)
        renpy.hide("powerup")
        renpy.hide("powerdown")

        RefreshEnemyDifficulty()
        CheckForGameOvers()
        CheckEnemyQueue()

    def RefreshEnemyDifficulty(): #Refreshes the visual difficulty of the enemy(the icon)
        global enemyUnits
        global eBar_Diff
        for x in range(len(enemyUnits)):
            eBar_Diff[x] = enemyUnits[x].cDifficulty()


    def HighlightPlayerUnitBars(slots): ##Shows player Bars with icons
        global playerUnits
        global battleStats
        global barHidden
        RefreshBarHP()


        if len(slots) > 0 and renpy.get_screen("battleStats") == None:
            renpy.start_predict_screen("battleStats")
            renpy.show_screen("battleStats")
        elif len(slots) == 0 and renpy.get_screen("battleStats") != None:
            for x in range(len(barHidden)):
                barHidden[x] = True
            #renpy.hide_screen("battleStats")
            #renpy.stop_predict_screen("battleStats")
            #renpy.free_memory()


        for x in range(len(playerUnits)):
            if x in slots:
                barHidden[x] = False
                # SetPlayerBarsPosition(x, True)
            else:
                barHidden[x] = True
                # SetPlayerBarsPosition(x, False)

    def HideBars():
        global playerUnits
        global battleStats
        global barHidden
        global enemyUnits
        global eBattleStats
        global eBarHidden

        for x in range(len(barHidden)):
            barHidden[x] = True

        for x in range(len(eBarHidden)):
            eBarHidden[x] = True

        renpy.hide_screen("battleStats")
        renpy.stop_predict_screen("battleStats")

        renpy.hide_screen("eBattleStats")
        renpy.stop_predict_screen("eBattleStats")

        #renpy.free_memory()

    def PlayerChoicePick(): ##Shows player Bars with icons
        global playerUnits
        global barHidden
        global playerChoice
        global continueToPlayerPhase
        continueToPlayerPhase = False
        availableMoves = False ##Checks that not everyone is exhausted.
        if renpy.get_screen("battleStats") == None:
            renpy.show_screen("battleStats")

        playerChoice = True
        for x in range(len(playerUnits)):
            barHidden[x] = False
            if(playerUnits[x].canAct()):
                availableMoves = True

        if(availableMoves == False): ##If no one can act, then continue to enemy turn.
            continueToPlayerPhase = True
            playerChoice = -1
        _window_hide(False)
        # Hold the player here until they select a character
        ui.interact()

            # SetPlayerBarsPosition(x, True)

    def CheckWhichAttacksAreUsable(unit):
        global isAttackSelectable
        #for x in range(len(unit.attacks))


    def SetUpCombatMenuUI(unit):
        global SS_stat_text
        global enemyUnits
        global LS_statText

        LS_statText = { ##Makes text of the list select.
            "1    brawn": unit.cStats("brawn"),
            "2    brains": unit.cStats("brains"),
            "3    hustle": unit.cStats("hustle"),
            "4    guts": unit.cStats("guts"),
            "5    charm": unit.cStats("charm"),
            "6    occult": unit.cStats("occult"),
            "9    stamina": unit.Stamina,
            "8    defense": unit.cDefense(),
            "7    atk Mod": unit.powerMod
        }
        #renpy.hide_screen("battleStats")
        HighlightPlayerUnitBars([])
        HighlightEnemyUnitBars([0,1,2,3])
        CheckMoveSelectable(unit) ##Tells the UI that the move is selectable.
        renpy.show_screen("StatScreen")


    def CheckMoveTargets(attackMove): ##Will check what targets the move uses, and decides if it targets only one person or multiple or its self heal.
        global targetChoice
        global playerUnits
        global enemyUnits
        global isSupportMove
        global quick_menu

        quick_menu = True
        _window_show(False)

        if (len(attackMove.comboUnit)>0):
            for x in attackMove.comboUnit:
                if (not playerUnits[x].canAct()):
                    targetChoice = -2
                    renpy.say(Narrator, str(playerUnits[x].name) + " cannot act!")
                    return

        ##Target measuring if theres only one target left which is alive.
        if not attackMove.isSupport:
            EnemiesAlive = 0
            EnemyAlive = 0
            isSupportMove = False
            for x in range(len(enemyUnits)):
                if (enemyUnits[x].isAlive and enemyUnits[x].canTarget):
                    EnemiesAlive +=1
                    EnemyAlive = x

            if(EnemiesAlive ==1):
                targetChoice = EnemyAlive
                return

            if (EnemiesAlive == 0):
                targetChoice = -2

                renpy.say(Narrator, str(playerUnits[x].name) + " can't use that move on anyone!")
                return

        if(attackMove.targetsAll!=2): ##If it doesnt always target everyone
            isSupportMove = attackMove.isSupport
            targets = []
            xDisplay = []

            if (attackMove.isSupport):
                HighlightEnemyUnitBars([])
                renpy.say(Narrator, "Who should be the target of this move?{nw}")
                for x in range(len(playerUnits)):
                    xDisplay.append(x)
                    targets.append((playerUnits[x].name, x))

                if(attackMove.targetsAll == 1):
                    targets.append(("Everyone", -1))

                HighlightPlayerUnitBars(xDisplay)

                renpy.say(Narrator, "Who should be the target of this move?{fast}",interact=False)


            else:

                renpy.say(Narrator, "Who should be the target of this attack?{nw}")
                for x in range(len(enemyUnits)):
                    xDisplay.append(x)
                    if enemyUnits[x].isAlive and enemyUnits[x].canTarget:
                        targets.append((enemyUnits[x].name, x))

                if(attackMove.targetsAll == 1):
                    targets.append(("Every enemy", -1))

                HighlightEnemyUnitBars(xDisplay)

                renpy.say(Narrator, "Who should be the target of this attack?{fast}",interact=False)



            targets.append(("Go Back", -2))

            targetChoice = renpy.display_menu(targets)

        else: ##If it DOES target everyone
            targetChoice = -1

    def TakeAwayStaminaForMove(attackMove):

        global playerUnits
        global playerChoice

        playerUnits[playerChoice].modifyStamina(attackMove.staminaUsed)
        if (len(attackMove.comboUnit)>0):
            for x in attackMove.comboUnit:
                playerUnits[x].modifyStamina(attackMove.staminaUsed)
        #renpy.block_rollback()

    def CheckMoveSelectable(unit): ##Tells the UI that the move is selectable once a unit is chosen, this check happens due to some moves requiring other units.
        global isAttackSelectable
        global playerUnits
        global unitAttacks

        GetUnitMoves(unit)
        isAttackSelectable = []
        for x in range(len(unit.attacks)): ##For each move in the unit
            if(len(unit.attacks[x].comboUnit) == 0): ##Check if the move requires any partners
                isAttackSelectable.append(True)
            else:
                CanMoveWork = True
                for y in range(len(unit.attacks[x].comboUnit)): ##If it does, check for each player unit if they are not exhausted.
                    if not playerUnits[y].canAct:
                        CanMoveWork = False
                isAttackSelectable.append(CanMoveWork)
            if (unit.status == 4):
                isAttackSelectable[x] = unit.attacks[x].isSupport
                renpy.notify(str(unit.attacks[x].isSupport))


    def DifficultyStringForDescription(move, unit): ##Calculates move difficulty using stats from unit that is using the move vs all current enemies, used for player UI difficulty calculation(for now)
        global enemyUnits
        difficultyString = ""
        cDiff = ""
        for x in range(len(enemyUnits)):
            cDiff = enemyUnits[x].cDifficulty(move.enemyMod)
            difficultyString += ("\n\n" + enemyUnits[x].name + "'s Diff: " + str(cDiff))

        return difficultyString ##Returns difficulty String used on move's descriptions.




    def CombatUnitPick():
        global playerUnits
        global playerChoice

        countExhaust = 0 ##Make it so that it skips playerphase if everyone is exhaused or dead
        for x in range(len(playerUnits)):
            if (not playerUnits[x].canAct()):
                countExhaust+=1
        if(countExhaust == len(playerUnits)):
            renpy.say(Narrator, "No one can act this turn!")
            renpy.jump(currentLabelET)
            return


        PlayerChoicePick()
        if(playerChoice == -1):
            renpy.say(Narrator, "Cannot act!")
            renpy.jump(currentLabelET)

        else:
            while (not playerUnits[playerChoice].canAct()):
                renpy.say(Narrator, str(playerUnits[playerChoice].name) + " cannot act! You have to pick someone else.") #TODO Have Quick Menu Show back up during this
                PlayerChoicePick()
            SetUpCombatMenuUI(playerUnits[playerChoice])




    def SetPlayerBarsPosition(val, bool): ##Shows player bars only
        pShowBars[val] = bool

    def HighlightEnemyUnitBars(slots): ##Shows player Bars with icons
        global enemyUnits
        global eBattleStats
        global eBarHidden
        RefreshBarHP()
        RefreshEnemyDifficulty()
        if len(slots) > 0 and renpy.get_screen("eBattleStats") == None:
            renpy.start_predict_screen("eBattleStats")
            renpy.show_screen("eBattleStats")
        elif len(slots) == 0 and renpy.get_screen("eBattleStats") != None:
            for x in range(len(eBarHidden)):
                eBarHidden[x] = True
            #renpy.hide_screen("eBattleStats")
            #renpy.stop_predict_screen("eBattleStats")

        for x in range(len(enemyUnits)):
            if x in slots:
                eBarHidden[x] = False
                SetEnemyBarsPosition(x, True)
            else:
                eBarHidden[x] = True
                SetEnemyBarsPosition(x, False)

    def SetEnemyBarsPosition(val, bool): ##Shows player bars only
        eShowBars[val] = bool



    def ToggleBarState(passUnits, val): ##units is a list [] of ORDERED values, val is to which value to set it to
        global playerUnits
        units = passUnits

        for x in range(len(playerUnits)):
            if(len(units)>0):
                if(x == units[0]):
                    playerUnits[x].iconState = val
                    units.pop(0)
                else:
                    playerUnits[x].iconState = 0
            else:
                playerUnits[x].iconState = 0


        #-------------------------------------------------------------Battle functions



    def CheckForGameOvers(inBattle=True):
        global playerUnits,curInBattle
        val = True
        for x in range(len(playerUnits)):
            if (playerUnits[x].isAlive):
                val = False
        if val:
            curInBattle=inBattle
            renpy.jump("gameOverScreen")


    def CheckEnemyQueue(): ##Checks whose enemies have to act
        global enemyUnits
        global currentEnemyTurn
        for x in range(len(enemyUnits)):
            if enemyUnits[x].isAlive:
                enemyUnits[x].ChangeMTA(-1) ##Per turn, their MTA decreases by one (Moves til attack)
            else:
                enemyUnits[x].ResetMTA()

        currentEnemyTurn = []
        for x in range(len(enemyUnits)): ##If any enemy unit's mta is less than 0, then they are added to the attack queue.
            if (enemyUnits[x].MTA <= 0 and enemyUnits[x].canAct()):
                enemyUnits[x].ResetNOCA()
                currentEnemyTurn.append(x)



    # def UnqueueAndResetEnemyMTA(): ##Unqueues enemy from enemy queue and resets their MTA.
    #     global enemyUnits
    #     val = currentEnemyTurn.pop(0)
    #     renpy.say(Narrator, currentEnemyTurn[0])
    #     enemyUnits[val].ResetMTA()

    def TurnStartStamRec(): ##Recovers party stamina except for the unit who last attacked (defined in slot)
        global playerUnits
        global playerChoice
        for x in range(len(playerUnits)):

            if( x == playerChoice):
                pass
            elif not (playerUnits[x].exhausted):
                playerUnits[x].modifyStamina(playerUnits[x].recoveryRate) ##Recover by natural recovery
            elif playerUnits[x].exhausted:
                playerUnits[x].modifyStamina(playerUnits[x].recoveryStamina) ##Recover by exhaustion recovery rate.
                if not (playerUnits[x].exhausted):
                    renpy.say(Narrator, playerUnits[x].name + " catches their breath.")


    # def AtStartOfTurnDMFight(): ##Used at the start at the turn to check if enemy is about to move, DMFight only.
    #     global playerUnits
    #     global xNum
    #     global enemyUnits
    #     global xStr
    #     global currentEnemyTurn
    #     global currentLabelPT
    #     CheckEnemyQueue()
    #
    #     while (len(currentEnemyTurn) >0):
    #         for x in range(len(currentEnemyTurn)):
    #             while (enemyUnits[currentEnemyTurn[x]].CALeft >0):
    #                 renpy.call(enemyUnits[currentEnemyTurn[x]].enemyAttackLabel)
    #                 enemyUnits[currentEnemyTurn[x]].ChangeCALeft(-1)
    #
    #             enemyUnits[currentEnemyTurn[x]].resetCA()
    #             enemyUnits[currentEnemyTurn[x]].DiminishModifiers([1,2,3,4,5,6])
    #             xNum = renpy.random.randint(1,5)
    #             if xNum == 1: ##Numbers representing rolls.
    #                 enemyUnits[currentEnemyTurn[x]].SetMTA(6)
    #                 xStr = "nat 1..."
    #             elif xNum < 5:
    #                 enemyUnits[currentEnemyTurn[x]].SetMTA(4)
    #                 xStr = "pretty average number."
    #             else:
    #                 enemyUnits[currentEnemyTurn[x]].SetMTA(2)
    #                 xStr = "nat 20!"
    #             for y in playerUnits:
    #                 if not (playerUnits[y].isAlive and enemyUnits[currentEnemyTurn[x]].MTA > 1):
    #                     enemyUnits[currentEnemyTurn[x]].ChangeMTA(-1)
    #             renpy.say(Narrator, enemyUnits[currentEnemyTurn[x]].name + " rolls for initiative, They rolled a [xStr]")
    #
    #
    #         UnqueueAndResetEnemyMTA()
    #
    #     TurnStartStamRec()
    #     renpy.call(currentLabelPT)

    def AtStartOfTurn(): ##Used at the start of each turn ##TODO wtf what why is this code like this
        global playerUnits
        global enemyUnits
        global currentEnemyTurn
        global enemiesActed
        global currentCA

        ToggleBarState([],0)

        if(len(currentEnemyTurn) > 0):

            if(enemyUnits[currentEnemyTurn[0]].CALeft >0):
                enemyUnits[currentEnemyTurn[0]].ChangeCALeft(-1)
                val=currentEnemyTurn[0]
                eAlive = enemyUnits[currentEnemyTurn[0]].isAlive

                currentCA = enemyUnits[currentEnemyTurn[0]].NOCA - enemyUnits[currentEnemyTurn[0]].CALeft

                if(enemyUnits[currentEnemyTurn[0]].CALeft <=0):
                    enemiesActed.append(currentEnemyTurn[0])
                    currentEnemyTurn.pop(0)

                if eAlive:
                    renpy.jump(enemyUnits[val].enemyAttackLabel)


        if(len(enemiesActed)>0):
            for x in range(len(enemiesActed)):
                enemyUnits[enemiesActed[x]].DiminishModifiers([1,2,3,4,5,6])
                enemyUnits[enemiesActed[x]].ResetMTA()

                #Lowers Enemy MTA if party members are dead
                for y in range(len(playerUnits)):
                    if (not playerUnits[y].isAlive) and enemyUnits[enemiesActed[x]].MTA > 1:
                        enemyUnits[enemiesActed[x]].ChangeMTA(-1)

        enemiesActed = []

        currentEnemyTurn = []
        TurnStartStamRec()


    def CureUnitOfStatus(x, number):
        global playerUnits

        if (playerUnits[x].status == number):
            playerUnits[x].CureStatus(1)
            renpy.sound.play("healing_b","sfx")
            Pixellate(0.2,4)
            renpy.say(Narrator, playerUnits[x].name+" returns to normal.")



    def CheckForNaturalCure(number): ##Cures ailments
        global playerUnits
        for x in range(len(playerUnits)):
            if(number == 1):
                if(playerUnits[x].exhausted == False):
                    CureUnitOfStatus(x, number)

    def WarnPlayerOfAttacks():
        global enemyAttackUpNext
        global enemyUnits
        enemyAttackUpNext = []
        for x in range(len(enemyUnits)):
            if (enemyUnits[x].MTA ==1):
                enemyAttackUpNext.append(x)

        if (len(enemyAttackUpNext) > 2):
            renpy.say(Narrator, "Several Enemies are preparing to act.")
        elif (len(enemyAttackUpNext) == 2):
            renpy.say(Narrator, enemyUnits[enemyAttackUpNext[0]].name+", and "+enemyUnits[enemyAttackUpNext[1]].name + " are preparing to attack.")
        elif (len(enemyAttackUpNext) ==1):
            renpy.say(Narrator, enemyUnits[enemyAttackUpNext[0]].name + " is preparing to attack.")

        #renpy.block_rollback()

    ## AI functions
    def AIChooseTarget(targetArray = [1,1,1,1]): #Chooses a Target randomly based on the priority they're given
        tempArray = []
        xOption = 0

        for x in range(len(targetArray)):
            for y in range(targetArray[x]):
                tempArray.append(x)

        xOption = renpy.random.choice(tempArray)

        return xOption

    def CheckLowestHP(isEnemy,needAlive=False): ##if you want to check between the enemies (and return an index from their own party, for things like healing spells), use this.
        ##Returns index on either playerunits or enemy units
        global playerUnits
        global enemyUnits

        HPtoCheck = []
        if not isEnemy:
            for x in range(len(playerUnits)):
                if ((not needAlive) or playerUnits[x].isAlive):
                    HPtoCheck.append(playerUnits[x].cHP)
                else:
                    HPtoCheck.append(999)

        else:
            for x in range(len(enemyUnits)):
                if ((not needAlive) or enemyUnits[x].isAlive):
                    HPtoCheck.append(enemyUnits[x].cHP)
                else:
                    HPtoCheck.append(999)

        minval = min(HPtoCheck)
        return HPtoCheck.index(minval) ##returns lowest index of the lowest value, this means the tie breaker is the order in which enemyunits is appended.

    def CheckHighestHP(isEnemy=False,needAlive=False): ##if you want to check between the enemies (and return an index from their own party, for things like healing spells), use this.
        ##Returns index on either playerunits or enemy units
        global playerUnits
        global enemyUnits

        HPtoCheck = []
        if not isEnemy:
            for x in range(len(playerUnits)):
                if ((not needAlive) or playerUnits[x].isAlive):
                    HPtoCheck.append(playerUnits[x].cHP)
                else:
                    HPtoCheck.append(-999)
        else:
            for x in range(len(enemyUnits)):
                if ((not needAlive) or enemyUnits[x].isAlive):
                    HPtoCheck.append(enemyUnits[x].cHP)
                else:
                    HPtoCheck.append(-999)

        maxval = max(HPtoCheck)
        return HPtoCheck.index(maxval) ##returns lowest index of the lowest value, this means the tie breaker is the order in which enemyunits is appended.

    def CheckLowestDefense(isEnemy=False, stat="guts",needAlive=False): ##if you want to check between the enemies (and return an index from their own party, for things like healing spells), use this.
        ##Returns index on either playerunits or enemy units
        global playerUnits
        global enemyUnits

        DeftoCheck = []
        if not isEnemy:
            for x in range(len(playerUnits)):
                if ((not needAlive) or playerUnits[x].isAlive):
                    DeftoCheck.append(playerUnits[x].cDefense(stat))
                else:
                    DeftoCheck.append(99)

        else:
            for x in range(len(enemyUnits)):
                if ((not needAlive) or enemyUnits[x].isAlive):
                    DeftoCheck.append(enemyUnits[x].cDefense(stat))
                else:
                    DeftoCheck.append(99)

        minval = min(DeftoCheck)
        return DeftoCheck.index(minval)

    def CheckLowestStat(isEnemy=False, stat="guts",needAlive=False): ##if you want to check between the enemies (and return an index from their own party, for things like healing spells), use this.
        ##Returns index on either playerunits or enemy units
        global playerUnits
        global enemyUnits

        StattoCheck = []
        if not isEnemy:
            for x in range(len(playerUnits)):
                if ((not needAlive) or playerUnits[x].isAlive):
                    StattoCheck.append(playerUnits[x].cStats(stat))
                else:
                    StattoCheck.append(99)

        else:
            for x in range(len(enemyUnits)):
                if ((not needAlive) or enemyUnits[x].isAlive):
                    StattoCheck.append(enemyUnits[x].cStats(stat))
                else:
                    StattoCheck.append(99)

        minval = min(StattoCheck)
        return StattoCheck.index(minval)

    def CheckHighestStat(isEnemy=False, stat="guts",needAlive=False): ##if you want to check between the enemies (and return an index from their own party, for things like healing spells), use this.
        ##Returns index on either playerunits or enemy units
        global playerUnits
        global enemyUnits

        StattoCheck = []
        if not isEnemy:
            for x in range(len(playerUnits)):
                if ((not needAlive) or playerUnits[x].isAlive):
                    StattoCheck.append(playerUnits[x].cStats(stat))
                else:
                    StattoCheck.append(-99)

        else:
            for x in range(len(enemyUnits)):
                if ((not needAlive) or enemyUnits[x].isAlive):
                    StattoCheck.append(enemyUnits[x].cStats(stat))
                else:
                    StattoCheck.append(-99)

        maxval = max(StattoCheck)
        return StattoCheck.index(maxval)
