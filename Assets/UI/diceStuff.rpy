init offset = -4
default persistent.dieSettings = 1


init offset = -1
default isRollSuccess = False
#Number of rerolls done used to plug into the dice bot
default xRerolls = 0

#Dice Results
default die1Result = 1
default die2Result = 1
default die3Result = 0
default dieTotal = 2

#enables Reroll button if true
default tempFailCheck = False

#Reroll Click is set true when pressing the reroll button so that tempDif is used instead of the default difficulty when the die_roll is called again
default rerollClick = False
default tempDif = 0

#Variables for the dice menu
define DiceMenuResult = 0
default dieGlow = False
default dMenuMod = -1
default dMenuDiff = 9
default dMenuDesc = "Placeholder"

default persistent.unlockedDice = [True,True,False,False,False,False,False,False,False,False,False] #11
#Dice Bot
init -3 python:

    try:
        while len(persistent.unlockedDice) < 11: persistent.unlockedDice.append(False)
    except:
        persistent.unlockedDice = [True,True,False,False,False,False,False,False,False,False,False]


    def numUnlockedDice():
        global gameVersion
        y = 0
        for x in persistent.unlockedDice:
            if x or gameVersion:
                y+=1
        return y
    #Gets the Average of an array
    def getAvg(xArray):
        avgNum = 0

        for x in xArray:
            avgNum+= x

        return int(avgNum/len(xArray))

    #Change Name to Limit Value
    def limitValue(xValue = 0, xMin = 0, xMax = 100):
        if xValue < xMin:
            return xMin
        elif xValue > xMax:
            return xMax
        else:
            return xValue

    class dice_bot:
        def __init__(self, **kwargs):
            self.cur_dice = 0
            self.diceNum = [[1,2,3,4,5,6,1,2,3,4],[1,2,3,4,5,6,1,2,3,4],[0,0,0,0,0,0,0,0,0,0]]
            self.dicePool = [1,2,3,3,4,4,5,6]
            self.dicePoolB = [1,2,3,3,4,4,5,6]
            self.dicePoolC = [0]
            self.dieFace = [6,6,0]
            self.dieType = 1
            self.maxKarma = 3
            self.superKarma = False

            self.numDice = 2
            self.dieMin = 2
            self.dieMax = 12

            self.lastDice = [1,1,0]

            self.dieName = "Ol' Reliable"

            self.dieNames = ["Ol' Reliable","Die Hard Purist","Lemon Squeezy","Jackalope's Fate","Snake Eye Sam","Full Moon Duet","Even Stevens","Prime Party","Lizards³","Mothman's Hoard","NJ Greataxe"]

        def setDieType(self, xType):
            self.dieType = xType


            self.dieName = "Ol' Reliable" # Avg 7
            self.dicePool = [1,2,3,3,4,4,5,6]
            self.dicePoolB = [1,2,3,3,4,4,5,6]
            self.dicePoolC = [0]
            self.dieFace = [6,6,0]
            self.maxKarma = 3
            self.superKarma = False
            self.numDice = 2
            self.dieMin = 2
            self.dieMax = 12

            if xType == 1:
                pass
            elif xType == 2:
                self.dieName = "Die Hard Purist" # Avg 8
                self.dicePool = [1,2,3,4,4,5,6,6,6]
                self.dicePoolB = [1,2,3,4,4,5,6,6,6]
                self.maxKarma = 1
                self.superKarma = True

            elif xType == 3:
                self.dieName = "Lemon Squeezy" # Avg 8.4
                self.dicePool = [1,2,3,4,4,5,5,6,6,6]
                self.dicePoolB = [1,2,3,4,4,5,5,6,6,6]
                self.maxKarma = 6
                self.superKarma = True
            elif xType == 4:
                self.dieName = "Jackalope's Fate" #50% Success Rate
                self.dicePool = [1,15]
                self.dicePoolB = [0]
                self.maxKarma = 2
                self.superKarma = True
                self.numDice = 1
                self.dieMin = 1
                self.dieMax = 15
                self.dieFace = [2,0,0]
            elif xType == 5:
                self.dieName = "Snake Eye Sam" # Avg  10
                self.dicePool = [1]
                self.dicePoolB = [1]
                self.maxKarma = 8
                self.superKarma = False
            elif xType == 6:
                self.dieName = "Full Moon Duet" # Avg  7
                self.dicePool = [1,2,3,4]
                self.dicePoolB = [1,2,3,4,5,6,7,8]
                self.maxKarma = 3
                self.superKarma = False
                self.dieFace = [4,8,0]
            elif xType == 7:
                self.dieName = "Even Stevens" # Avg 8
                self.dicePool = [2,4,6]
                self.dicePoolB = [2,4,6]
                self.maxKarma = 2
                self.superKarma = False
                self.dieMin = 4
            elif xType == 8:
                self.dieName = "Prime Party" # Avg 7.6
                self.dicePool = [2,2,3,3,7]
                self.dicePoolB = [2,2,5,5,7]
                self.maxKarma = 2
                self.superKarma = False
                self.dieMin = 4
                self.dieMax = 14
                self.dieFace = [8,8,0]
            elif xType == 9:
                self.dieName = "Lizards³" # Avg  7.6
                self.dicePool = [1,2,3,4,4]
                self.dicePoolB = [1,2,3,3,4]
                self.dicePoolC = [1,1,2,2,3,4]
                self.maxKarma = 2
                self.superKarma = False
                self.numDice = 3
                self.dieMin = 3
                self.dieFace = [4,4,4]
            elif xType == 10:
                self.dieName = "Mothman's Hoard" # Avg  7.5
                self.dicePool = [1,2,3,4]
                self.dicePoolB = [1,2]
                self.dicePoolC = [1,2,3,4,5,6]

                self.maxKarma = 2
                self.superKarma = False
                self.numDice = 3
                self.dieMin = 3
                self.dieFace = [4,2,6]
            elif xType == 11:
                self.dieName = "NJ Greataxe" # Avg  7
                self.dicePool = [1,2,3,4,5,6,7,8,9,10,11,12,13]
                self.dicePoolB = [0]
                self.maxKarma = 3
                self.superKarma = False
                self.numDice = 1
                self.dieMin = 1
                self.dieMax = 13
                self.dieFace = [12,0,0]

            self.setRolls()

        def setRolls(self):
            self.cur_dice = 0
            for x in range(10):
                if (x > 1):
                    self.diceNum[0][x] = renpy.random.choice(self.dicePool)
                    self.diceNum[1][x] = renpy.random.choice(self.dicePoolB)
                    self.diceNum[2][x] = renpy.random.choice(self.dicePoolC)

                    dt = self.diceNum[1][x] + self.diceNum[0][x] + self.diceNum[2][x]
                    ldt = self.diceNum[1][x-1] + self.diceNum[0][x-1] + self.diceNum[2][x-1]

                    if ((ldt <= 4 and dt <= 4 ) or (dt > 10 and ldt > 10)) and (self.dieType < 4 and self.dieType > 5):
                        self.diceNum[0][x] = renpy.random.choice(self.dicePool)
                        self.diceNum[1][x] = renpy.random.choice(self.dicePoolB)
                        self.diceNum[2][x] = renpy.random.choice(self.dicePoolC)
                else:
                    self.diceNum[0][x] = renpy.random.choice(self.dicePool)
                    self.diceNum[1][x] = renpy.random.choice(self.dicePoolB)
                    self.diceNum[2][x] = renpy.random.choice(self.dicePoolC)

        def reroll(self, rNum = 1):

            if self.dieType == 5:
                self.diceNum[0][self.cur_dice] = renpy.random.randint(4,6)
                self.diceNum[1][self.cur_dice] = renpy.random.randint(4,6)
            elif self.dieType == 4:
                self.diceNum[0][self.cur_dice] = renpy.random.choice(self.dicePool)
                self.diceNum[1][self.cur_dice] = renpy.random.choice(self.dicePoolB)
            else:
                maxPool = len(self.dicePool)-1
                dieA = renpy.random.randint(limitValue(rNum*2, 1, maxPool ), maxPool)
                maxPool = len(self.dicePoolB)-1
                dieB = renpy.random.randint(limitValue(rNum*2, 1, maxPool ), maxPool)
                maxPool = len(self.dicePoolC)-1
                dieC = renpy.random.randint(limitValue(rNum*2, 0, maxPool ), maxPool)

                self.diceNum[0][self.cur_dice] = self.dicePool[dieA]
                self.diceNum[1][self.cur_dice] = self.dicePoolB[dieB]
                self.diceNum[2][self.cur_dice] = self.dicePoolC[dieC]

        def get_cur_total(self):
            return self.diceNum[0][self.cur_dice]+self.diceNum[1][self.cur_dice]+self.diceNum[2][self.cur_dice]

        def get_last_total(self):
            return get_last_dice[0] + get_last_dice[1] + get_last_dice[2]

        def is_roll_match(self):
            if (self.diceNum[2][self.cur_dice] !=0):
                return self.diceNum[0][self.cur_dice] == self.diceNum[1][self.cur_dice] and self.diceNum[1][self.cur_dice] == self.diceNum[2][self.cur_dice]
            elif (self.diceNum[1][self.cur_dice] !=0):
                return self.diceNum[0][self.cur_dice] == self.diceNum[1][self.cur_dice]
            return True

        @property
        def get_last_dice(self):
            return self.lastDice

        @property
        def get_cur_dice(self):
            return [self.diceNum[0][self.cur_dice],self.diceNum[1][self.cur_dice],self.diceNum[2][self.cur_dice]]

        def increment_dice(self):
            self.lastDice = self.get_cur_dice
            self.cur_dice+= 1
            if (self.cur_dice > 9):
                self.setRolls()

        def get_num_dice(self):
            return self.numDice

    diceBot = dice_bot()
    diceBot.setDieType(persistent.dieSettings)
    diceBot.setRolls()

# -------------------------------------- Dice Labels
default rollCamOverwrite = False
label dice_roll(rMod=0, rDiff=7, rDesc="Basic Roll",rCO = False):
    $canChangeDice = False
    $rollCamOverwrite = rCO
    if gameDiff < 2:
        $rDiff-=1


    if rDiff < 0:
        $isRollSuccess = True
        return
    elif gameDiff > 3:
        $rDiff+=1

    show screen Dice_Rolling_Menu
    python:
        xRerolls = 0
        dMenuMod = rMod
        dMenuDiff = rDiff
        dMenuDesc = rDesc
        tempFailCheck = False
        DiceMenuResult = -1

        renpy.pause(0.5,hard=True)

        #Sets Dice Results to temporary variables for usage in text and outside the roll itself
        tempDif = rDiff
        die1Result = diceBot.get_cur_dice[0]
        die2Result = diceBot.get_cur_dice[1]
        die3Result = diceBot.get_cur_dice[2]
        dieTotal = die1Result + die2Result + die3Result
        DiceMenuResult = 0
        dieGlow = True

    if (rDiff-rMod > 2) and (rDiff-rMod <13):
        with Dissolve(0.2)
        pause 1.5

    #Shows Result
    if dieTotal + rMod >= 2+rDiff:
        play sfx dice_result_a
    elif dieTotal + rMod >= rDiff-1:
        play sfx dice_result_b
    else:
        play sfx dice_result_c

    if pc_karma > 0:
        $tempFailCheck = True

    #Sets the modifier text
    if rMod < 0:
        $rsMod = str(rMod)
    elif rMod == 0:
        $rsMod = ""
    else:
        $rsMod = "+" + str(rMod)

    show screen KarmaBar
    #$renpy.block_rollback()
    if dieTotal + rMod >=rDiff:
        $DiceMenuResult = 1
        show successFlash
        if not rollCamOverwrite:
            camera:
                resultFlash(True)

        Narrator "{color=#f25ebd}Difficulty: [rDiff]\n{/color}{color=#83ed6e}Result: [dieTotal][rsMod]\n\n{/color}{color=#83ed6e}Success!{/color}{fast}"
        hide successFlash
    else:
        $DiceMenuResult = 2
        show failFlash
        if not rollCamOverwrite:
            camera:
                resultFlash(False)
        Narrator "{color=#f25ebd}Difficulty: [rDiff]\n{/color}{color=#83ed6e}Result: [dieTotal][rsMod]\n\n{/color}{color=#f25ebd}Failure.{/color}{fast}"

        $pc_karma = limitValue(pc_karma+1, 0, diceBot.maxKarma)
        hide failFlash

    #Resets Resettable Variables
    python:
        diceBot.increment_dice()

    hide screen KarmaBar
    hide screen Dice_Rolling_Menu
    with None
    hide Die onlayer screens
    hide Die2 onlayer screens
    hide Die3 onlayer screens
    with Dissolve(0.1)

    python:
        dieGlow = False
        isRollSuccess = (dieTotal + rMod >=rDiff)
        renpy.sound.stop("sfx", 0.1)

    if not rollCamOverwrite:
        camera:
            matrixcolor SaturationMatrix(1)

        pause 0.01

    $canChangeDice = True
    return

label dice_reroll:
    hide screen KarmaBar
    python:
        renpy.block_rollback()
        tempFailCheck = False
        xRerolls+=1
        diceBot.reroll(xRerolls)
        pc_karma-=1
        rrDif = tempDif

        die1Result = diceBot.get_cur_dice[0]
        die2Result = diceBot.get_cur_dice[1]
        die3Result = diceBot.get_cur_dice[2]
        dieTotal = die1Result + die2Result + die3Result
        DiceMenuResult = 0

    if (rDiff-rMod > 2) and (rDiff-rMod <13):
        with Dissolve(0.2)
        pause 2.0


    #Shows Result
    if dieTotal + rMod >= 2+rrDif:
        play sfx dice_result_a
    elif dieTotal + rMod >= rrDif-1:
        play sfx dice_result_b
    else:
        play sfx dice_result_c

    if pc_karma > 0:
        $tempFailCheck = True

    #Sets the modifier text
    if rMod < 0:
        $rsMod = str(rMod)
    elif rMod == 0:
        $rsMod = ""
    else:
        $rsMod = "+" + str(rMod)

    #Shows Text Result
    $renpy.block_rollback()

    show screen KarmaBar
    if dieTotal + rMod >=rrDif:
        $DiceMenuResult = 1
        show successFlash
        if not rollCamOverwrite:
            camera:
                resultFlash(True)

        Narrator "{color=#f25ebd}Difficulty: [rDiff]\n{/color}{color=#83ed6e}Result: [dieTotal][rsMod]\n\n{/color}{color=#83ed6e}Success!{/color}{fast}"
        hide successFlash
    else:
        $DiceMenuResult = 2
        show failFlash
        if not rollCamOverwrite:
            camera:
                resultFlash(False)

        Narrator "{color=#f25ebd}Difficulty: [rDiff]\n{/color}{color=#83ed6e}Result: [dieTotal][rsMod]\n\n{/color}{color=#f25ebd}Failure.{/color}{fast}"
        hide failFlash


    #Resets Resettable Variables
    python:
        diceBot.increment_dice()

    hide screen KarmaBar
    hide screen Dice_Rolling_Menu
    with None
    hide Die onlayer screens
    hide Die2 onlayer screens
    hide Die3 onlayer screens
    with Dissolve(0.1)

    python:
        dieGlow = False
        isRollSuccess = (dieTotal + rMod >=rDiff)
        if (not isRollSuccess) and diceBot.superKarma:
            pc_karma = limitValue(pc_karma+1, 0, diceBot.maxKarma)

        renpy.sound.stop("sfx", 0.1)

    if not rollCamOverwrite:
        camera:
            matrixcolor SaturationMatrix(1)
        pause 0.01

    $canChangeDice = True
    return

# -------------------------------------- Dice Screen
screen Dice_Rolling_Menu:
    zorder 3
    #Reroll Button
    imagebutton:
        at rerollButton_anim
        focus_mask "gui/DiceMenu/Reroll_Button_Idle.webp"
        idle "gui/DiceMenu/Reroll_Button_Idle.webp"
        insensitive "gui/DiceMenu/Reroll_Button_Insensitive.webp"
        hover "gui/DiceMenu/Reroll_Button_Hover.webp"
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        action [SensitiveIf(tempFailCheck),Jump('dice_reroll')]

    #Added Visual Effects
    if dieGlow:
        add "DiceMenuGlowL"  at dice_menu_extras, dice_menu_rollingGlow
        add "DiceMenuGlowR"  at dice_menu_extras, dice_menu_rollingGlow2

    if DiceMenuResult >= 1:
        add "DiceMenuEyes" at dice_menu_extras, dice_menu_successGlow
    if DiceMenuResult == 2:
        add "DiceMenuEyes" at dice_menu_extras, dice_menu_failGlow

    add "DiceMenu" at dice_menu_location

    if DiceMenuResult == 2:
        add "DiceMenuFailFrame" at dice_menu_extras

    #Roll Description
    text dMenuDesc at dice_menu_textTransform:
        xanchor 0.0
        yanchor 0.0
        xpos 850
        ypos 3
        size 30 - len(dMenuDesc)*0.15
        xmaximum 270
        text_align 0.5
        minwidth 270
        font "fonts/typwrng.ttf"

    #Move Modifier
    if dMenuMod >= 0:
        text "+" + str(dMenuMod) at dice_menu_textTransform:
            color "#83ed6e"
            xanchor 0.5
            yanchor 0.0
            xpos 0.705
            ypos 0.2
            size 25
            font "fonts/typwrng.ttf"
    else:
        text str(dMenuMod) at dice_menu_textTransform:
            color "#83ed6e"
            xanchor 0.5
            yanchor 0.0
            xpos 0.705
            ypos 0.2
            size 25
            font "fonts/typwrng.ttf"

    #Difficulty
    text str(dMenuDiff) at dice_menu_textTransform:
        color "#f25ebd"
        xanchor 0.5
        yanchor 0.0
        xpos 0.88
        ypos 0.17
        size 25
        font "fonts/typwrng.ttf"

    #Dice
    $tDieIndex = ["A","B","C"]
    if DiceMenuResult >= 0:
        if diceBot.numDice == 1:
            showif DiceMenuResult == 0:
                if diceBot.dieFace[0] == 2:
                    image "d2_rollA" at dicePos
                elif diceBot.dieFace[0] < 8:
                    image "dSquare_rand" + str(diceBot.dieFace[0]) at dRollAnim(0), dicePos
                else:
                    image "dHex_rand" + str(diceBot.dieFace[0]) at dRollAnim(0), dicePos
            else:
                if diceBot.dieFace[0] == 2:
                    image "d2A" at resultSpinCoin, dicePos

                elif diceBot.dieFace[0] < 8:
                    image "dSquareA" at resultSpin, dicePos

                else:
                    image "dHexA" at resultSpin, dicePos

        elif diceBot.numDice == 2:
            for x in range(2):
                showif DiceMenuResult == 0:
                    if diceBot.dieFace[x] == 2:
                        image "d2_roll" + tDieIndex[x] at dicePosDuo(x)

                    elif diceBot.dieFace[x] < 8:
                        image "dSquare_rand" + str(diceBot.dieFace[0]) at dRollAnim(x), dicePosDuo(x)
                    else:
                        image "dHex_rand" + str(diceBot.dieFace[0]) at dRollAnim(x), dicePosDuo(x)
                else:
                    if diceBot.dieFace[x] == 2:
                        image "d2" + tDieIndex[x] at resultSpinCoin, dicePosDuo(x)

                    elif diceBot.dieFace[x] < 8:
                        image "dSquare" + tDieIndex[x] at resultSpin, dicePosDuo(x)
                    else:
                        image "dHex" + tDieIndex[x] at resultSpin, dicePosDuo(x)

        elif diceBot.numDice == 3:
            for x in range(3):
                showif DiceMenuResult == 0:
                    if diceBot.dieFace[x] == 2:
                        image "d2_roll" + tDieIndex[x] at dicePosTrio(x)

                    elif diceBot.dieFace[x] < 8:
                        image "dSquare_rand" + str(diceBot.dieFace[0]) at dRollAnim(x), dicePosTrio(x)
                    else:
                        image "dHex_rand" + str(diceBot.dieFace[0]) at dRollAnim(x), dicePosTrio(x)
                else:
                    if diceBot.dieFace[x] == 2:
                        image "d2" + tDieIndex[x] at resultSpinCoin, dicePosTrio(x)

                    elif diceBot.dieFace[x] < 8:
                        image "dSquare" + tDieIndex[x] at resultSpin, dicePosTrio(x)
                    else:
                        image "dHex" + tDieIndex[x] at resultSpin, dicePosTrio(x)


transform karmabar_tf:
    on show:
        yoffset -275
        ease 0.5 yoffset 0

    on hide:
        yoffset 0
        ease 0.5 yoffset -275


default karmaRainbow = ["#fff069","#ff8941","#ff5342","#ED2A82","#b480ff","#a1fffc","#a7ff78"]
init python:
    def loopInt(xNum=0,xMax=1,reset=False):
        if xNum >= xMax:
            if reset: return 0

            return loopInt(xNum-xMax,xMax)
        return xNum

screen KarmaBar:
    if pc_karma > 0:
        frame at karmabar_tf:
            background None


            add "songtext_bg":
                xanchor 0.5
                ycenter 0.0
                xpos 350
                xysize (pc_karma*70+20,170)

            for x in range(pc_karma):
                add "gui/text_icons/KARMA_StatIcon.webp":
                    xanchor 0
                    ypos -5
                    xpos 350 - pc_karma*35 + x*70
                    xysize (70,70)
                    matrixcolor ColorizeMatrix("#000000",karmaRainbow[loopInt(x,7)])



transform dicePos:
    ycenter 0.4
    xcenter 0.8
    zoom 0.7

transform dicePosDuo(xNum=0):
    ycenter 0.4
    xcenter 0.86
    zoom 0.64
    xoffset -160*xNum

transform dicePosTrio(xNum=0):
    ycenter 0.42
    xcenter 0.875
    zoom 0.45
    xoffset -100*xNum
    yoffset -60*(xNum%2)
# --------------------------------------------------------------------------- d2

image d2A:
    ConditionSwitch(
        "die1Result == 1", "d2_tails",
        "True", "d2_heads"
        )

image d2B:
    ConditionSwitch(
        "die2Result == 1", "d2_tails",
        "True", "d2_heads"
        )

image d2C:
    ConditionSwitch(
        "die3Result == 1", "d2_tails",
        "True", "d2_heads"
        )

image d2_rollA:
    perspective True

    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    "d2_heads"
    linear 0.2 matrixtransform RotateMatrix(0, 90, 0)
    "d2_tails"
    linear 0.4 matrixtransform RotateMatrix(0, 270, 0)
    "d2_heads"
    linear 0.2 matrixtransform RotateMatrix(0, 360, 0)

    repeat

image d2_rollB:
    perspective True

    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    "d2_heads"
    linear 0.2 matrixtransform RotateMatrix(0, -90, 0)
    "d2_tails"
    linear 0.4 matrixtransform RotateMatrix(0, -270, 0)
    "d2_heads"
    linear 0.2 matrixtransform RotateMatrix(0, -360, 0)

    repeat


image d2_rollC = "d2_rollA"

image d2_heads:
    matrixcolor ColorizeMatrix("#733f29", "#fad874")
    "images/Props/Dice/d2/d2_heads.png"

image d2_tails:
    matrixcolor ColorizeMatrix("#2e2033", "#8b85f5")
    "images/Props/Dice/d2/d2_tails.png"

# ------------------------------------------------- Square Dice
layeredimage dSquare_1:
    matrixcolor ColorizeMatrix("#000000", "#BC6BFF")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_1" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_2:
    matrixcolor ColorizeMatrix("#000000", "#446eec")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_2" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_3:
    matrixcolor ColorizeMatrix("#000000", "#77ee79")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_3" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_4:
    matrixcolor ColorizeMatrix("#000000", "#6bb4ff")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_4" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_5:
    matrixcolor ColorizeMatrix("#000000", "#9bf5ba")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_5" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_6:
    matrixcolor ColorizeMatrix("#000000", "#fad874")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_6" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_7:
    matrixcolor ColorizeMatrix("#000000", "#f25b9f")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_7" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_8:
    matrixcolor ColorizeMatrix("#000000", "#9265fe")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_8" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_9:
    matrixcolor ColorizeMatrix("#000000", "#fa9a74")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_9" + renpy.random.choice([".webp","b.webp"])

layeredimage dSquare_10:
    matrixcolor ColorizeMatrix("#000000", "#ff6b78")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_10.webp"

layeredimage dSquare_11:
    matrixcolor ColorizeMatrix("#000000", "#62f24c")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_11.webp"

layeredimage dSquare_12:
    matrixcolor ColorizeMatrix("#000000", "#fad874")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_12.webp"

layeredimage dSquare_13:
    matrixcolor ColorizeMatrix("#000000", "#698eff")
    always:
        "images/Props/Dice/diebg1.webp"
    always:
        "images/Props/Dice/dnum_13.webp"

image dSquare_rand4:
    choice:
        "dSquare_1"
    choice:
        "dSquare_3"

    pause 0.21

    choice:
        "dSquare_2"
    choice:
        "dSquare_4"

    pause 0.21
    repeat

image dSquareA:
    ConditionSwitch(
        "die1Result == 1", "dSquare_1",
        "die1Result == 2", "dSquare_2",
        "die1Result == 3", "dSquare_3",
        "die1Result == 4", "dSquare_4",
        "die1Result == 5", "dSquare_5",
        "die1Result == 6", "dSquare_6",
        "die1Result == 7", "dSquare_7",
        "die1Result == 8", "dSquare_8",
        "die1Result == 9", "dSquare_9",
        "die1Result == 10", "dSquare_10",
        "die1Result == 11", "dSquare_11",
        "die1Result == 12", "dSquare_12",
        "die1Result == 13", "dSquare_13"
        )

image dSquareB:
    ConditionSwitch(
        "die2Result == 1", "dSquare_1",
        "die2Result == 2", "dSquare_2",
        "die2Result == 3", "dSquare_3",
        "die2Result == 4", "dSquare_4",
        "die2Result == 5", "dSquare_5",
        "die2Result == 6", "dSquare_6",
        "die2Result == 7", "dSquare_7",
        "die2Result == 8", "dSquare_8",
        "die2Result == 9", "dSquare_9",
        "die2Result == 10", "dSquare_10",
        "die2Result == 11", "dSquare_11",
        "die2Result == 12", "dSquare_12",
        "die2Result == 13", "dSquare_13"
        )

image dSquareC:
    ConditionSwitch(
        "die3Result == 1", "dSquare_1",
        "die3Result == 2", "dSquare_2",
        "die3Result == 3", "dSquare_3",
        "die3Result == 4", "dSquare_4",
        "die3Result == 5", "dSquare_5",
        "die3Result == 6", "dSquare_6",
        "die3Result == 7", "dSquare_7",
        "die3Result == 8", "dSquare_8",
        "die3Result == 9", "dSquare_9",
        "die3Result == 10", "dSquare_10",
        "die3Result == 11", "dSquare_11",
        "die3Result == 12", "dSquare_12",
        "die3Result == 13", "dSquare_13"
        )

image dSquare_rand6:
    choice:
        "dSquare_1"
    choice:
        "dSquare_4"

    pause 0.21

    choice:
        "dSquare_2"
    choice:
        "dSquare_5"

    pause 0.21

    choice:
        "dSquare_3"
    choice:
        "dSquare_6"

    pause 0.21
    repeat

image dSquare_rand8:
    choice:
        "dSquare_1"
    choice:
        "dSquare_5"

    pause 0.21

    choice:
        "dSquare_2"
    choice:
        "dSquare_6"

    pause 0.21

    choice:
        "dSquare_3"
    choice:
        "dSquare_7"

    pause 0.21

    choice:
        "dSquare_4"
    choice:
        "dSquare_8"

    pause 0.21
    repeat

image dSquare_rand10:
    choice:
        "dSquare_1"
    choice:
        "dSquare_6"

    pause 0.21

    choice:
        "dSquare_2"
    choice:
        "dSquare_7"

    pause 0.21

    choice:
        "dSquare_3"
    choice:
        "dSquare_8"

    pause 0.21

    choice:
        "dSquare_4"
    choice:
        "dSquare_9"

    pause 0.21

    choice:
        "dSquare_5"
    choice:
        "dSquare_10"

    pause 0.21
    repeat

image dSquare_rand12:
    choice:
        "dSquare_1"
    choice:
        "dSquare_7"

    pause 0.21

    choice:
        "dSquare_2"
    choice:
        "dSquare_8"

    pause 0.21

    choice:
        "dSquare_3"
    choice:
        "dSquare_9"

    pause 0.21

    choice:
        "dSquare_4"
    choice:
        "dSquare_10"

    pause 0.21

    choice:
        "dSquare_5"
    choice:
        "dSquare_11"

    pause 0.21

    choice:
        "dSquare_5"
    choice:
        "dSquare_12"

    pause 0.21
    repeat

# ------------------------------------------------- Hex Dice
layeredimage dHex_1:
    matrixcolor ColorizeMatrix("#000000", "#BC6BFF")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_1" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_2:
    matrixcolor ColorizeMatrix("#000000", "#446eec")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_2" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_3:
    matrixcolor ColorizeMatrix("#000000", "#77ee79")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_3" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_4:
    matrixcolor ColorizeMatrix("#000000", "#6bb4ff")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_4" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_5:
    matrixcolor ColorizeMatrix("#000000", "#9bf5ba")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_5" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_6:
    matrixcolor ColorizeMatrix("#000000", "#fad874")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_6" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_7:
    matrixcolor ColorizeMatrix("#000000", "#f25b9f")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_7" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_8:
    matrixcolor ColorizeMatrix("#000000", "#9265fe")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_8" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_9:
    matrixcolor ColorizeMatrix("#000000", "#fa9a74")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_9" + renpy.random.choice([".webp","b.webp"])

layeredimage dHex_10:
    matrixcolor ColorizeMatrix("#000000", "#ff6b78")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_10.webp"

layeredimage dHex_11:
    matrixcolor ColorizeMatrix("#000000", "#62f24c")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_11.webp"

layeredimage dHex_12:
    matrixcolor ColorizeMatrix("#000000", "#fad874")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_12.webp"

layeredimage dHex_13:
    matrixcolor ColorizeMatrix("#000000", "#698eff")
    always:
        "images/Props/Dice/diebg2.webp"
    always:
        "images/Props/Dice/dnum_13.webp"

image dHexA:
    ConditionSwitch(
        "die1Result == 1", "dHex_1",
        "die1Result == 2", "dHex_2",
        "die1Result == 3", "dHex_3",
        "die1Result == 4", "dHex_4",
        "die1Result == 5", "dHex_5",
        "die1Result == 6", "dHex_6",
        "die1Result == 7", "dHex_7",
        "die1Result == 8", "dHex_8",
        "die1Result == 9", "dHex_9",
        "die1Result == 10", "dHex_10",
        "die1Result == 11", "dHex_11",
        "die1Result == 12", "dHex_12",
        "die1Result == 13", "dHex_13"
        )

image dHexB:
    ConditionSwitch(
        "die2Result == 1", "dHex_1",
        "die2Result == 2", "dHex_2",
        "die2Result == 3", "dHex_3",
        "die2Result == 4", "dHex_4",
        "die2Result == 5", "dHex_5",
        "die2Result == 6", "dHex_6",
        "die2Result == 7", "dHex_7",
        "die2Result == 8", "dHex_8",
        "die2Result == 9", "dHex_9",
        "die2Result == 10", "dHex_10",
        "die2Result == 11", "dHex_11",
        "die2Result == 12", "dHex_12",
        "die2Result == 13", "dHex_13"
        )

image dHexC:
    ConditionSwitch(
        "die3Result == 1", "dHex_1",
        "die3Result == 2", "dHex_2",
        "die3Result == 3", "dHex_3",
        "die3Result == 4", "dHex_4",
        "die3Result == 5", "dHex_5",
        "die3Result == 6", "dHex_6",
        "die3Result == 7", "dHex_7",
        "die3Result == 8", "dHex_8",
        "die3Result == 9", "dHex_9",
        "die3Result == 10", "dHex_10",
        "die3Result == 11", "dHex_11",
        "die3Result == 12", "dHex_12",
        "die3Result == 13", "dHex_13"
        )


image dHex_rand4:
    choice:
        "dHex_1"
    choice:
        "dHex_3"

    pause 0.21

    choice:
        "dHex_2"
    choice:
        "dHex_4"

    pause 0.21
    repeat

image dHex_rand6:
    choice:
        "dHex_1"
    choice:
        "dHex_4"

    pause 0.21

    choice:
        "dHex_2"
    choice:
        "dHex_5"

    pause 0.21

    choice:
        "dHex_3"
    choice:
        "dHex_6"

    pause 0.21
    repeat

image dHex_rand8:
    choice:
        "dHex_1"
    choice:
        "dHex_5"

    pause 0.21

    choice:
        "dHex_2"
    choice:
        "dHex_6"

    pause 0.21

    choice:
        "dHex_3"
    choice:
        "dHex_7"

    pause 0.21

    choice:
        "dHex_4"
    choice:
        "dHex_8"

    pause 0.21
    repeat

image dHex_rand10:
    choice:
        "dHex_1"
    choice:
        "dHex_6"

    pause 0.21

    choice:
        "dHex_2"
    choice:
        "dHex_7"

    pause 0.21

    choice:
        "dHex_3"
    choice:
        "dHex_8"

    pause 0.21

    choice:
        "dHex_4"
    choice:
        "dHex_9"

    pause 0.21

    choice:
        "dHex_5"
    choice:
        "dHex_10"

    pause 0.21
    repeat

image dHex_rand12:
    choice:
        "dHex_1"
    choice:
        "dHex_7"

    pause 0.21

    choice:
        "dHex_2"
    choice:
        "dHex_8"

    pause 0.21

    choice:
        "dHex_3"
    choice:
        "dHex_9"

    pause 0.21

    choice:
        "dHex_4"
    choice:
        "dHex_10"

    pause 0.21

    choice:
        "dHex_5"
    choice:
        "dHex_11"

    pause 0.21

    choice:
        "dHex_5"
    choice:
        "dHex_12"

    pause 0.21
    repeat

transform dRollAnim(xNum=0):
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    linear 1 matrixtransform RotateMatrix(0.0, 0.0, -360.0*pow(-1,xNum))
    repeat

transform rollA:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    linear 1 matrixtransform RotateMatrix(0.0, 0.0, -360.0)
    repeat

transform rollB:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    linear 1 matrixtransform RotateMatrix(0.0, 0.0, -360.0)
    repeat

transform rollC:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    linear 1 matrixtransform RotateMatrix(0.0, 0.0, -360.0)
    repeat

init -1 python:
    def changeDice(dieNum=1):
        global diceBot, pc_karma
        persistent.dieSettings = dieNum
        diceBot.setDieType(dieNum)
        pc_karma = limitValue(pc_karma,0,diceBot.maxKarma)

image Dice_Change_Menu:
    zoom 0.5
    "gui/DiceMenu/Dice_Change_Menu.webp"

image Dice_Change_Button:
    xanchor 0.5
    zoom 0.525
    matrixcolor ColorizeMatrix("#424242","#424242")
    "gui/DiceMenu/Dice_Change_Tag.webp"

image Dice_Change_Button_Hover:
    xanchor 0.5
    zoom 0.525
    matrixcolor ColorizeMatrix("#1f1f1f","#1f1f1f")
    "gui/DiceMenu/Dice_Change_Tag.webp"

transform dieMenuShow(t=0.5):
    ease t yoffset 325

transform dieMenuHide(t=0.5):
    ease t yoffset 0

transform slideInOut(t=0.5):
    on show:
        yoffset -400
        ease t yoffset 0
    on hide:
        yoffset 0
        ease t yoffset -600

default menuShowing = False
default canChangeDice = True

image ShowDiceMenu_Open:
    crop (940,800,200,200)
    zoom 0.5
    "gui/DiceMenu/Dice Eyes 1.png"
    pause 0.2
    "gui/DiceMenu/Dice Eyes 2.png"
    pause 0.2
    "gui/DiceMenu/Dice Eyes 3.png"
    pause 0.2
    "gui/DiceMenu/Dice Eyes 4.png"
    pause 0.2
    repeat

image ShowDiceMenu_Closed:
    crop (940,800,200,200)
    zoom 0.5
    "gui/DiceMenu/Dice Eyes RESTING.png"

screen diceChangingMenu():
    default dieIndex = 0
    python:
        diceInList = 0
        curIndex = 0

    frame at slideInOut(0.5):
        background None

        frame:
            background None

            xpos 50
            ypos -400

            if menuShowing:
                at dieMenuShow(0.5)
            else:
                at dieMenuHide(0.5)

            add "Dice_Change_Menu"

            vbox:
                xanchor 0.5
                xpos 165
                ypos 150
                spacing 15
                python:
                    curIndex = dieIndex
                    diceInList = 0

                for x in range(5):
                    python:
                        while curIndex < 11 and not ((persistent.unlockedDice[ curIndex ] or gameVersion >= 3) and ( curIndex +1 != persistent.dieSettings)):
                            curIndex = loopInt(curIndex+1,11)

                    if curIndex < 11:
                        button:
                            xminimum 120
                            xmaximum 120
                            yminimum 25
                            ymaximum 25


                            action [Hide('quicker_menu_hide'), Confirm("Change dice to " + diceBot.dieNames[ curIndex ] + "?", [Function(changeDice, curIndex + 1 ),Show('quicker_menu_hide')] , Show('quicker_menu_hide'), False)]
                            sensitive canChangeDice

                            idle_background "Dice_Change_Button"
                            hover_background "Dice_Change_Button_Hover"
                            insensitive_background "Dice_Change_Button_Hover"

                            text diceBot.dieNames[ curIndex ]:
                                xanchor 0.5
                                text_align 0.5
                                size 15
                                kerning -1
                                xmaximum 100


                                hover_color karmaRainbow[loopInt(x,7)]
                                idle_color "#ffffff"
                                insensitive_color "#828288"

                    $curIndex += 1

                if numUnlockedDice() > 5:
                    button:
                        xminimum 120
                        xmaximum 120
                        yminimum 25
                        ymaximum 25


                        action SetLocalVariable("dieIndex",loopInt(dieIndex+5,11,True))
                        sensitive canChangeDice

                        idle_background "Dice_Change_Button"
                        hover_background "Dice_Change_Button_Hover"
                        insensitive_background "Dice_Change_Button_Hover"

                        text "More Dice":
                            xanchor 0.5
                            text_align 0.5
                            size 15
                            kerning -1
                            xmaximum 100


                            hover_color karmaRainbow[loopInt(x,7)]
                            idle_color "#ffffff"
                            insensitive_color "#828288"

            imagebutton:
                pos (58,392)
                hover "ShowDiceMenu_Open"
                idle "ShowDiceMenu_Closed"

                action [Hide('quicker_menu_hide'), ToggleVariable("menuShowing"), Show('quicker_menu_hide')]
                #text_size 15
                #text_hover_color karmaRainbow[loopInt(numUnlockedDice()-1,7)]
                #text_idle_color "#ffffff"
