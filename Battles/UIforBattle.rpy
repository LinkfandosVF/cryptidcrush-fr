init offset = -1

################################################################################
## Battle Screen
################################################################################

init python:
    def GetHPTimer(x = 0, y = 10):
        z = .45-.08*limitValue(abs(x-y), 0, 10)

        return limitValue(z, 0.075, 0.4)

    def GetUnitMoves(unit):
        global unitAttacks
        unitAttacks = unit.attacks
        hoveredAttackOption = -1

    def InitializeCombatUI(pUs, eUs, **kwargs): ##Call this before initiating combat, input playerUnits using an array of Units (defined in BattleUnits.rpy)
        global pShowBars
        global playerBarCHP
        global playerBarMHP
        global playerBarDHP
        global playerBarNames
        global eShowBars
        global eBar_cHP
        global eBar_dHP
        global eBar_mHP
        global eNames
        global eBarNum
        global playerUnits
        global enemyUnits
        global eBarHidden
        global barHidden

        pShowBars = []
        playerBarCHP = []
        playerBarMHP = []
        playerBarDHP = []
        playerBarNames=[]
        eShowBars = []
        eBar_cHP = []
        eBar_dHP = []
        eBar_mHP = []
        eNames = []
        eBarNum = 0

        barHidden = [True, True, True, True]
        eBarHidden = [True, True, True, True]
        for x in pUs:
            pShowBars.append(False)
            playerBarMHP.append(x.maxHP)
            playerBarCHP.append(x.cHP)
            playerBarDHP.append(x.cHP)
            playerBarNames.append(x.name)

        playerUnits = pUs

        for x in eUs:
            eShowBars.append(False)
            eBar_cHP.append(x.cHP)
            eBar_dHP.append(x.cHP)
            eBar_mHP.append(x.maxHP)
            eNames.append(x.name)
            eBarNum +=1


        enemyUnits = eUs
        playerUnits = pUs

    # Adjusts the displayed HP for a Unit
    # Used in conjunction with a timer in the battleStats screen to roll the number down
    def AdjustUnitCHP(index, isPlayer):
        global playerBarCHP, playerBarDHP, eBar_cHP, eBar_dHP
        if isPlayer:
            if playerBarCHP[index] > playerBarDHP[index]:
                playerBarCHP[index] -= 1
            else:
                playerBarCHP[index] += 1
        else:
            if eBar_cHP[index] > eBar_dHP[index]:
                eBar_cHP[index] -= 1
            else:
                eBar_cHP[index] += 1
    # This handles the rolling text count down
    class RollingStatDisplay(renpy.Displayable):
        # index: Array index we'll use to get our health values
        # isPlayer: Whether we should be checking the player character health arrays or the enemy
        def __init__(self, index, isPlayer=True, **kwargs):
            global playerBarCHP, playerBarMHP, eBar_cHP, eBar_mHP
            super(RollingStatDisplay, self).__init__(**kwargs)
            self.index = index
            self.isPlayer = isPlayer
            # Setup current and max values
            
            if not isPlayer:
                self.curr_value = eBar_cHP[index]
            else:
                self.curr_value = playerBarCHP[index]

            
            if not isPlayer:
                self.max_value = eBar_mHP[index]
            else:
                self.max_value = playerBarMHP[index]

            self.lowHP = int(self.max_value*0.5)
            # Setup our child
            self.child = Text("{size=30}" + str(self.curr_value)+ "/" + str(self.max_value) + "{/size}{image=Health_StatIconL}")

        def render(self, width, height, st, at):
            global playerBarCHP, eBar_cHP, playerUnits
            # Get the value we'll compare against

            if self.isPlayer and len(playerUnits) > self.index and playerUnits[self.index].status == 3:
                self.child = Text("{bt=2}{size=27}{color=#ff88ec}Relaxing~{/color}{/size}{/bt}")
            elif self.curr_value <= 0: ##When character is defeated, change color.
                self.child = Text("{size=33}{color=#F52500}" + str(self.curr_value) +"{/color}/" + str(self.max_value) + "{/size} {image=Health_StatIconL}")
            elif self.curr_value <= self.lowHP: ##When character is low HP, change color.
                self.child = Text("{size=33}{color=#ffc634}" + str(self.curr_value) +"{/color}/" + str(self.max_value) + "{/size} {image=Health_StatIconL}")
            else: # Idk what this is here for but I'll include it.
                self.child = Text("{size=33}" + str(self.curr_value)+ "/" + str(self.max_value) + "{/size} {image=Health_StatIconL}")

            # Standard renpy render output stuff
            child_render = renpy.render(self.child, width, height, st, at)
            renpy.redraw(self, 0.05)
            return child_render

## PBar = images of the characters, PBar1 is for Odd Character buttons, Pbar2 is for even, Pbar 3 is for when they are damaged.
#### PLAYER SECTION ####
image playerBarOdd:
    ease 0.1 xanchor 0
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/bar_1.png"

image playerBarEven:
    ease 0.1 xanchor 0
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/bar_2.png"

image playerBarDamaged:
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/damaged_bar.png"
    ease 0.2 xanchor 0.05
    ease 0.2 xanchor -0.05
    ease 0.2 xanchor 0.05
    ease 0.2 xanchor -0.05
    ease 0.2 xanchor 0.05
    ease 0.2 xanchor -0.05
    ease 0.2 xanchor 0.05
    ease 0.2 xanchor -0.05
    ease 0.2 xanchor 0.05
    ease 0.2 xanchor -0.05
    ease 0.1 xanchor 0

##Coordinates for character battle bars, show moves bars inside screen, hide places them behind left side, barGone probably useless? (R is mirrored)

transform showBar:
    ease 0.5 xpos 0.0525 alpha 1
    on hide:
        ease 0.5 xpos -.3

transform hideBar:
    ease 0.5 xpos -.3 alpha 1

transform barGone:
    xanchor 0
    alpha 0

transform barShow:
    ease 0.5 alpha 1

transform showBarR:
    xanchor 0
    xpos 1.15
    ease 0.5 xpos 0.8 alpha 1

transform hideBarR:
    xanchor 0
    xpos 0.8
    ease 0.5 xpos 1.15 alpha 1

# Create images for the battle stats button's different states
transform playerBattleStatsBarIdle(index):
    size (253, 111)
    contains: # Background
        "gui/Party_Bar/bar_1.png"
        zoom .33
    contains: # Unit Icon
        playerUnits[index].icon
        pos (30,52)
    contains: # Unit Name
        Text(playerBarNames[index])
        xanchor 1.0 pos (200, 22)
    contains: # Unit Health
        RollingStatDisplay(index)
        xanchor 1.0 pos (230, 48)

transform playerBattleStatsBarHover(index):
    size (253, 111)
    contains: # Background
        "gui/Party_Bar/bar_2.png"
        zoom .33
    contains: # Unit Icon
        playerUnits[index].icon
        pos (30,52)
    contains: # Unit Name
        Text(playerBarNames[index])
        xanchor 1.0 pos (200, 22)
    contains: # Unit Health
        RollingStatDisplay(index)
        xanchor 1.0 pos (230, 48)

#Images for the stamina dots
image grayStam:
    matrixcolor ColorizeMatrix("#172625","#16fd6e")*BrightnessMatrix(-0.2)
    zoom 0.4
    "gui/Party_Bar/Stamina_dot.png"
image greenStam:
    zoom 0.4
    matrixcolor ColorizeMatrix("#172625","#16fd6e")*BrightnessMatrix(0.8)
    "gui/Party_Bar/Stamina_dot.png"


# Controls the movement of the battleStats button as it's manipulated
transform pBattleStatsButton(index):
    ycenter 0.10+(index*0.16)
    on idle:
        ease 0.1 xoffset 0
    on hover:
        ease 0.1 xoffset 10

# Controls the movement of the stat bar as the script shows and hides it
transform pBarAnim(index):
    on appear, show:
        xpos -0.3
        ease 0.5 xpos 0.0525
    on hide:
        xpos 0.0525
        ease 0.5 xpos -.3 alpha 1

image playerBarChoice:
    ease 0.1 xanchor 1
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/bar_1.png"

image playerBarHover:
    ease 0.1 xanchor -0.1
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/bar_2.png"

image playerBarSelected:
    ease 0.1 xanchor 1
    xzoom 0.33
    yzoom 0.33
    "gui/Party_Bar/bar_1.png"

default tempNo = 0 ##Temporary Number

default pShowBars = [False, False, False, False]

default barHidden = [True, True, True, True]

default playerBarCHP = [1,1,1,1]
default playerBarMHP = [1,1,1,1]
default playerBarDHP = [1,1,1,1] ##DisplayedHP
default playerBarNames = ["peepee","poopoo","bruh", "big gay"]
default playerChoice = False
image bS_TooltipBG:
    zoom 0.83
    "gui/Party_Bar/Battle Menu/eSide_Box.png"

transform bS_TooltipBGPos:
    xpos 1.1
    xanchor 1.0
    yanchor 0.0
    ypos 0.1
    zoom 1.0
    block:
        xzoom 0
        ease 0.3 xzoom 1.3 xpos 0.92
        ease 0.12 xzoom 1.0

define hoveredBar = -1

transform karma_bar_anim:
    yalign 2.0
    ease 0.3 yalign 1.0

    on show:
        yalign 2.0
        ease 0.3 yalign 1.0

    on hide:
        yalign 1.0
        ease 0.3 yalign 2.0

screen battleStats: ##Screen allows UI to be placed on screen. Screens are also interactable.
    tag battleStats

    # Create each stat display
    for x in range(len(pShowBars)):
        # Hide the display if don't want it shown
        showif not barHidden[x]:
            # Fixed handles the appear, show and hide from the showif
            fixed at pBarAnim(x):
                # Button has it's own transform to handle idle and hover state

                button at pBattleStatsButton(x):
                    # This is probably going to break but wanted some way to combat offset not being reset after the button interaction
                    if not isinstance(playerChoice, bool) and playerChoice == x:
                        xoffset -10



                    hovered [Function(ToggleBarState, [x], 1),SetVariable('hoveredBar',x)]
                    unhovered [Function(ToggleBarState, [] , 0),SetVariable('hoveredBar',-1)]
                    idle_child playerBattleStatsBarIdle(x)
                    hover_child playerBattleStatsBarHover(x)
                    insensitive_child playerBattleStatsBarIdle(x)

                    hover_sound audio.selecthover
                    activate_sound renpy.random.choice(selectList)
                    selected False

                    action [SetVariable('playerChoice', x),SetVariable('hoveredBar',-1), Return(0)]
                    sensitive (playerChoice+1) and not continueToPlayerPhase

                #small stamina Idea
                for y in range(4):
                    if not (hoveredBar == x):
                        if playerUnits[x].Stamina > y:
                            text "{color=#55ff96}.":
                                ypos 98+x*115
                                xoffset 125+y*25
                                size 80
                                yoffset -50
                        else:
                            text "{color=#266a40}.":
                                ypos 98+x*115
                                xoffset 125+y*25
                                size 80
                                yoffset -50
                    else:
                        if playerUnits[x].Stamina > y:
                            text "{color=#55ff96}.":
                                ypos 98+x*115
                                xoffset 125+y*25+10
                                size 80
                                yoffset -50
                        else:
                            text "{color=#266a40}.":
                                ypos 98+x*115
                                xoffset 125+y*25+10
                                #text_color "#266a40"
                                size 80
                                yoffset -50

    if renpy.get_screen("say") == None:
        add "gui/Party_Bar/Karma_Backdrop.png" at karma_bar_anim:
            xalign 1.0
            xsize 100*pc_karma + 120
            ysize 120
            yoffset 20
            xoffset 120
        hbox:
            at karma_bar_anim
            xalign 1.0

            for x in range(pc_karma):
                add "gui/text_icons/KARMA_StatIcon.webp":
                    zoom 0.3
                    matrixcolor ColorizeMatrix("#000000", "#fff069")




    # Timers to update health stats
    for x in range(len(pShowBars)):
        if playerBarCHP[x] != playerBarDHP[x]:
            timer GetHPTimer(playerBarCHP[x], playerBarDHP[x]) action Function(AdjustUnitCHP, x, True) repeat playerBarCHP[x] != playerBarDHP[x]

transform eIconPosition: ## eIconPos is for enemies, you can tell because *Markiplier voice*: E
    ypos 0.04 + (tempNo*0.16)
    xpos 1.1
    ease 0.5 xpos 0.9
    on hide:
        ease 0.5 xpos 1.1


#### ENEMY SECTION ####

image eDemon: ##Shows difficulty of the boss.
    "gui/Party_Bar/Edemon.webp"
    yzoom 0.28
    xzoom 0.28

image miDemon:
    "gui/Party_Bar/Midemon.webp"
    yzoom 0.23
    xzoom 0.23

image harDemon:
    "gui/Party_Bar/Hardemon.webp"
    yzoom 0.21
    xzoom 0.21
    yoffset -15

##Layered images are objects on screen, cannot use ATL, Animation transformation language.


image dIcon1: ##Checks difficulty of monster and shows different icons depending on it
    "harDemon"
    # if eBar_Diff[0] > 7:
    #     "harDemon"
    # elif eBar_Diff[0] > 5:
    #     "miDemon"
    # else:
    #     "eDemon"

image dIcon2:
    "miDemon"
    # if eBar_Diff[1] > 7:
    #     "harDemon"
    # elif eBar_Diff[1] > 5:
    #     "miDemon"
    # else:
    #     "eDemon"

image dIcon3:
    "eDemon"
    # if eBar_Diff[2] > 7:
    #     "harDemon"
    # elif eBar_Diff[2] > 5:
    #     "miDemon"
    # else:
    #     "eDemon"

image dIcon4:
    "eDemon"
    # if eBar_Diff[3] > 7:
    #     "harDemon"
    # elif eBar_Diff[3] > 5:
    #     "miDemon"
    # else:
    #     "eDemon"

init python:
    def GetEnemyStatsIcon(st, at, index):
        global eBar_Diff
        if eBar_Diff[index] > 6:
            img = "harDemon"
        elif eBar_Diff[index] > 5:
            img = "miDemon"
        else:
            img = "eDemon"
        return img, None
# Create images for the battle stats button's different states
init python:

    def eBar_MTA(x):
        global enemyUnits
        c = enemyUnits[x].Color
        return str(enemyUnits[x].MTA)

transform enemyBattleStatsBarIdle(index):
    size (253, 111)
    contains: # Background
        "gui/Party_Bar/bar_1.png"
        zoom .33
    contains: # Unit Health
        RollingStatDisplay(index, False)
        pos (20, 52)
    contains: # Unit Icon
        DynamicDisplayable(GetEnemyStatsIcon, index)
        pos (140,12)
    contains: # Unit Name
        Text(eNames[index], False)
        pos (20, 22)
    contains: #MTA INDICATOR
        "gui/Party_Bar/Stamina_dot.png"
        pos (133,75)
        zoom 1.1
        matrixcolor BrightnessMatrix(-0.2)
    contains: #MTA INDICATOR
        Text(eBar_MTA(index), size=40,color=enemyUnits[index].Color)
        pos (140,75)

transform enemyBattleStatsBarHover(index):
    size (253, 111)
    contains: # Background
        "gui/Party_Bar/bar_2.png"
        zoom .33
    contains: # Unit Health
        RollingStatDisplay(index, False)
        pos (20, 52)
    contains: # Unit Icon
        DynamicDisplayable(GetEnemyStatsIcon, index)
        pos (140,12)
    contains: # Unit Name
        Text(eNames[index], False)
        pos (20, 22)
    contains: #MTA INDICATOR
        "gui/Party_Bar/Stamina_dot.png"
        pos (133,75)
        zoom 1.1
        matrixcolor BrightnessMatrix(-0.2)
    contains: #MTA INDICATOR
        Text(eBar_MTA(index), size=40,color=enemyUnits[index].Color)
        pos (140,75)

# Controls the movement of the battleStats button as it's manipulated
transform eBattleStatsButton(index):
    ycenter 0.10+(index*0.16)

# Controls the movement of the stat bar as the script shows and hides it
transform eBarAnim(index):
    on appear, show:
        xpos 2.0
        ease 0.5 xpos 0.8
    on hide:
        ease 0.5 xpos 2.0 alpha 1

default eBarHidden = [True, True, True, True]
default eNames = ["Name1", "Name2", "Name3", "Name4"]
default eShowBars = [False, False, False, False]
default eBar_cHP = [1,1,1,1]
default eBar_dHP = [1,1,1,1]
default eBar_mHP = [1,1,1,1]
default eBar_Diff = [1,1,1,1]
default eYCenterValues = [0.07, 0.23, 0.39, 0.55] ##If using more than 4 make sure you add here for defaults.
default temp1 = 0

default eBarNum = 1 ##ebarnum checks amount of enemies you are fighting.

screen eBattleStats:
    zorder 2
    tag eBattleStats
    # Create each stat display
    for x in range(len(eShowBars)):
        # Hide the display if don't want it shown
        showif not eBarHidden[x]:
            # Fixed handles the appear, show and hide from the showif
            fixed at eBarAnim(x):
                # Button has it's own transform to handle idle and hover state
                button at eBattleStatsButton(x):
                    # This is probably going to break but wanted some way to combat offset not being reset after the button interaction
                    # if not isinstance(playerChoice, bool) and playerChoice == x:
                    #     xoffset -10
                    idle_child enemyBattleStatsBarIdle(x)
                    hover_child enemyBattleStatsBarHover(x)
                    insensitive_child enemyBattleStatsBarIdle(x)

                    #hover_sound audio.selecthover
                    tooltip enemyUnits[x].getcStats(True)
                    action NullAction()

    #Tooltips
    if GetTooltip('eBattleStats'):
        frame:
            at bS_TooltipBGPos
            background 'bS_TooltipBG'
            xmaximum 230
            xminimum 230
            text GetTooltip('eBattleStats') size 30 line_spacing 2:
                xoffset 35
                yoffset 45


    for x in range(len(eShowBars)):
        if eBar_cHP[x] != eBar_dHP[x]:
            timer GetHPTimer(eBar_cHP[x],eBar_dHP[x]) action Function(AdjustUnitCHP, x, False) repeat eBar_cHP[x] != eBar_dHP[x]


define unitAttacks =[] ##Array of attacks the unit uses.
define isAttackSelectable = [] ##list of booleans that set wether the button is pressable
define hoveredAttackOption = -1 ##BiListX checks which option of the skills is hovered
define attackOptionSelected = -1 ##This holds the attack chosen, it uses an integer
define attackChoiceJump = "CallDiceRollForMove" ##For labels regarding moves
define tempAttackTooltip = ""

default LS_Frame = 8 ##Current frame of animation
default LS_Color = renpy.random.choice(["#00d000","#FF53F0","#1e85e4"]) ##Color selected button.

#This is a test description so that ya'll can see what I mean when I'm talking about the descriptions of this thing. Wow this purple box looks weird juxtposed on this screen doesn't it?

transform listPos: ##Position of attack menu
    xcenter 0.53

    on show:
        ypos -0.3
        xzoom 2
        yzoom 0
        ease 0.5 xzoom 0.35 yzoom 1.6 ypos -0.05
        ease 0.275 xzoom 1 yzoom 1

    on hide:
        ease 0.2 xzoom 0.35 yzoom 1.6
        ease 0.4 ypos -0.3 yzoom 0 xzoom 2

transform listPos2: ## Stat list next to attack menu.
    xpos 0.775

    on show:
        ypos 0.13
        xzoom 0
        pause 0.7
        ease 0.1 xzoom 1 yzoom 1

    on hide:
        ease 0.2 xzoom 0 xpos 0.6

image AttackMenuBG: ##Ace's lovely menu assets into play
    "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - BOX.png"
    xzoom 0.73
    yzoom 0.73
    xcenter 0.5

image LS_Mouth_textbox:
    xzoom 0.73
    yzoom 0.73
    xcenter 0.33
    "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - TEXT BOX.png"

layeredimage LS_Mouth:
    xzoom 0.73
    yzoom 0.73
    xcenter 0.33
    always:
        ConditionSwitch(
            "LS_Frame < 8", "LS_MouthBG",
            "LS_Frame == 8", "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - MAW.png")
    always:
        ConditionSwitch(
            "LS_Frame < 8", "LS_MouthFG",
            "LS_Frame == 8", "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - EYES.png")

image LS_MouthBG:
    "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - MAW.png"
    pause 0.07
    "gui/Party_Bar/Battle Menu/F2(Open Mouth Solid Teeth)/F2_Maw.png"
    pause 0.06
    "gui/Party_Bar/Battle Menu/F3(Half Closed Inbetween Down Movement)/F3_Maw.png"
    pause 0.05
    "gui/Party_Bar/Battle Menu/F4(Half Closed Down Movement)/F4_Maw.png"
    pause 0.04
    "gui/Party_Bar/Battle Menu/F5(Closed Mouth)/F5_Maw.png"
    pause 0.11
    "gui/Party_Bar/Battle Menu/F6(Half Closed Up Movement)/F6_Maw.png"
    pause 0.03
    "gui/Party_Bar/Battle Menu/F7(Half Closed Inbetween Up Movement)/F7_Maw.png"

image LS_MouthFG:
    "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - EYES.png"
    pause 0.07
    "gui/Party_Bar/Battle Menu/F1(Open Mouth Resting)/MENU Frame 1 - (Open Mouth Resting) - EYES.png"
    pause 0.06
    "gui/Party_Bar/Battle Menu/F3(Half Closed Inbetween Down Movement)/F3_Eyes.png"
    pause 0.05
    "gui/Party_Bar/Battle Menu/F4(Half Closed Down Movement)/F4_Eyes.png"
    pause 0.04
    "gui/Party_Bar/Battle Menu/F5(Closed Mouth)/F5_Eyes.png"
    pause 0.11
    "gui/Party_Bar/Battle Menu/F6(Half Closed Up Movement)/F6_Eyes.png"
    pause 0.03
    "gui/Party_Bar/Battle Menu/F7(Half Closed Inbetween Up Movement)/F7_Eyes.png"

image SS_SideBox:
    zoom 0.8
    "gui/Party_Bar/Battle Menu/Side_Box.png"
transform SS_SideBoxPos:
    xalign -0.03
    yanchor 0.0
    ypos 0.08
    zoom 1.0
    block:
        xzoom 0
        ease 0.4 xzoom 1.3
        ease 0.2 xzoom 1.0

    on hide:
        ease 0.5 xzoom 0.0

screen StatScreen: ##stat screen
    zorder 1
    tag StatScreen
    frame: ##Frame for attack menu
        xmaximum 600
        xminimum 600
        yminimum 330
        ymaximum 330

        at listPos
        background 'AttackMenuBG'
        vbox:
            hbox:
                vbox:
                    ypos 0.54
                    xpos -5
                    xmaximum 130
                    xminimum 130
                    yminimum 300
                    ymaximum 300
                    for xList in range(len(unitAttacks)): ##Checks the attacks of the user and places them on the menu, gets refreshed every moment of the game
                        if unitAttacks[xList].isSupport:
                            $unhoverTextColor = "#cdecc0"
                        else:
                            $unhoverTextColor = "#ecc0d6"

                        textbutton unitAttacks[xList].name: # + " :: " + str(0-unitAttacks[xList].staminaUsed)
                            text_color unhoverTextColor
                            text_hover_color playerUnits[playerChoice].Color
                            text_insensitive_color "#797979"

                            hover_sound audio.selecthover
                            activate_sound renpy.random.choice(selectList)
                            text_size 20

                            tooltip unitAttacks[xList].desc #Description for set move
                            hovered SetVariable('LS_Frame', 1)
                            action [SensitiveIf(isAttackSelectable[xList] == True),SetVariable('continueToPlayerPhase',True), SetVariable('attackOptionSelected',xList),Hide('StatScreen'),Jump(attackChoiceJump)] ##If able to be selected, then on action, BLY is set to BLX

                    textbutton "Go Back":
                        text_color "#c0e9ec"
                        text_hover_color playerUnits[playerChoice].Color
                        text_insensitive_color "#797979"

                        hover_sound audio.selecthover
                        activate_sound renpy.random.choice(selectList)
                        text_size 20

                        tooltip "Pick a different character to attack with."
                        hovered SetVariable('LS_Frame', 1)
                        action [Hide('StatScreen'), SetVariable('attackOptionSelected',-2),Jump(attackChoiceJump)] ##If able to be selected, then on action, BLY is set to BLX

                    $tooltip = GetTooltip('StatScreen') #Gets the tooltip for the textbutton

                #Sets off the tooltip animation
                if tooltip:
                    $tempAttackTooltip = GetTooltip('StatScreen')

                if tempAttackTooltip != hoveredAttackOption:
                    timer 0.23 action SetVariable('hoveredAttackOption', tempAttackTooltip) repeat False

                frame:
                    background 'LS_Mouth_textbox'

                    foreground 'LS_Mouth'

                    vbox:
                        xmaximum 420
                        xminimum 420
                        ypos 235
                        xpos 225
                        xalign 0.5

                        if hoveredAttackOption != -1: ##Show description of skill if hovered
                            text hoveredAttackOption:
                                color "#202020"
                                size 19.7
                                line_spacing -1
                                text_align 0.5

            if LS_Frame < 8: ## Animation for bite motion.
                timer 0.42 action SetVariable('LS_Frame', 8) repeat LS_Frame !=8

            #textbutton "Go Back":
            #    hover_sound "audio/SFX/OOC/Select_2.ogg"
            #    activate_sound renpy.random.choice(["audio/SFX/OOC/Select_6.wav","audio/SFX/OOC/Select_7.wav","audio/SFX/OOC/Select_8.wav","audio/SFX/OOC/Select_8_2.wav","audio/SFX/OOC/Select_9.wav"])
            #
            #    ypos 20
            #    text_color "#58744d"
            #    text_hover_color "#f675e8"
            #    text_size 24
            #    action Rollback()

    frame: #Character Stats
        background "SS_SideBox"
        at SS_SideBoxPos
        text playerUnits[playerChoice].getcStats() size 30 line_spacing 3:
            xoffset 125
            yoffset 35


    frame: #Stamina Bar
        background None
        at staminaBarPos
        bar:
            value playerUnits[playerChoice].Stamina
            range 4

            left_bar "stam_LBar"
            right_bar "stam_RBar"


            xysize(350,50)

        #Shows the Outside of the Stamina bar
        add "stam_Frame"


screen BarPlayerSelect(pUs):
    for x in range(len(pUs)):

        vbox:
            xcenter 0.2
            ycenter 0.2 +(x*0.16)
            xsize 0.43
            ysize 0.43


            python:
                global tempNo
                tempNo = x
                renpy.show(pUs[x].icon ,at_list = [pIconPosition()], layer='screens')
            imagebutton:

                idle ["playerBarChoice", SetVariable('currentSelect', -1), Call('UpdateHover')]
                hover "playerBarHover"
                selected ["playerBarSelected", SetVariable('currentSelect', x), Call('UpdateHover')]

                hover_sound audio.selecthover
                activate_sound renpy.random.choice(selectList)

                action [SetVariable('gayVariable',True), SetVariable('currentSelect', -1), Call('UpdateHover')]

transform turnCounter_tf:
    on show:
        xcenter -0.5
        ycenter 0.4

    on hide:
        ease 0.45 xcenter 0.5
        pause 0.75
        ease 0.5 xcenter 1.5

image tc_bg:
    "gui/notify2.png"
    xzoom 0.5
    yzoom 0.75

screen turnCounter(turnNum=1):
    frame at turnCounter_tf:
        background "tc_bg" #Solid("#000")
        xmaximum 100
        xminimum 100
        ymaximum 40
        yminimum 40
        xfill True
        yfill True
        label "Turn:" + str(turnNum):
            xcenter 0.5
            ycenter 0.5
            text_size 25
            text_text_align 0.5
            text_color karmaRainbow[renpy.random.randint(0,6)]

    timer 0.01 action Hide() repeat False
