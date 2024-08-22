init python:
    def avgUnitStat(xUnits=[],xStat=""):
        if len(xUnits) < 1:
            return 0

        xArr = []
        for x in xUnits:
            xArr.append(x.cStats(xStat))

        return getAvg(xArr)
    def addBattleKarma(xKarma=0):
        global pc_karma, kwKarma, diceBot
        pc_karma = limitValue(pc_karma+xKarma, 0, diceBot.maxKarma)

        temp = [audio.powerup_a,audio.powerup_a2,audio.powerup_a3]
        renpy.sound.play(temp[limitValue(xKarma,1,3)-1],"sfx")

        if pc_karma >= diceBot.maxKarma:
            renpy.say(Narrator,"Your " + kwKarma + " is maxed out!")
        else:
            renpy.say(Narrator,"Your " + kwKarma + " increases by +" + str(xKarma) + "!")

    def calcRank(turnCount, cRank=40,bRank=30,aRank=25,sRank=20,xRank=15):
        rank_dict = {
            xRank : "X",
            sRank : "S",
            aRank : "A (" + str(sRank) + " for S)",
            bRank : "B (" + str(aRank) + " for A)",
            cRank : "C (" + str(bRank) + " for B)",
        }
        rank_list = [xRank, sRank, aRank, bRank, cRank]
        for rank in rank_list:
            if turnCount <= rank:
                return rank_dict[rank]
        return "D (" + str(cRank) + " for C)"

    def playerUnitsInit(*argv):
        global playerUnits
        playerUnits = []
        xNum = 0

        for x in argv:
            xNum+=1

            if xNum > 4:
                return

            newChar = globals()[x + '_Stats']
            playerUnits.append(newChar)

    def enemyUnitsInit(*argv):
        global enemyUnits
        enemyUnits = []
        xNum = 0

        for x in argv:
            xNum+=1

            if xNum > 4:
                return

            newChar = globals()[x + '_Stats']
            enemyUnits.append(newChar)


    def battlePredict(*argv):
        global predictArray
        predictArray = argv
        renpy.start_predict("images/Props/Dice/*",*argv)
        renpy.start_predict_screen("Dice_Rolling_Menu")
        config.conditionswitch_predict_all = True


    def endBattlePredict():
        global predictArray
        renpy.stop_predict("images/Props/Dice/*",*predictArray)
        renpy.stop_predict_screen("Dice_Rolling_Menu")
        config.conditionswitch_predict_all = False


default predictArray = []

label battleTransition:
    show Flickering Black
    pause 0.65

    play music elkhorn_radio_intro_song noloop
    call makeCheckpoint from _call_makeCheckpoint_2
    pause (4.3)

    return

# -------------------------------------------------------------- Icon Animations
init python:
    def backdropHue(xUnit=Unit()):
        return HueMatrix(-210*(1-float(xUnit.cHP*1.2)/xUnit.maxHP))*BrightnessMatrix(-0.15*(1-float(xUnit.cHP)/xUnit.maxHP))

    def exBackdrop():
        return HueMatrix(150)*BrightnessMatrix(-0.4)*SaturationMatrix(1.05)

    def exIconHue(xUnit=Unit()):
        return BrightnessMatrix(xUnit.Stamina*0.05)*SaturationMatrix((4+xUnit.Stamina)*0.15)

    def koIconHue():
        return SaturationMatrix(0)*BrightnessMatrix(-0.1)

transform backdropDamaged(tImage="images/Characters/Atlas/Battle/Atlas"):
    tImage + "_Backdrop_Damage.webp"
    pause 0.1
    xanchor 0.5
    pause 0.1
    xanchor 0.4
    tImage + "_Backdrop_Default.webp"
    pause 0.1
    tImage + "_Backdrop_Selected.webp"
    xanchor 0.5

transform fightIconPos(tZoom=1.0,xAnchor=0.5,yAnchor=0.5):
    zoom tZoom
    xanchor xAnchor
    yanchor yAnchor

transform fightIconHurt:
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1

# ------------------------------------------------------------- Enemy Animations
transform Boss_AttackPos:
    xcenter 0.5
    ycenter 0.6
    yoffset 0
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.05 xoffset 0

# ------------------------------------------------------------ Camera Animations
transform camera_shake:
    xoffset -15
    ease 0.06 xoffset 15
    ease 0.06 xoffset -13
    ease 0.06 xoffset 11
    ease 0.06 xoffset -9
    ease 0.06 xoffset 7
    ease 0.06 xoffset -5
    ease 0.06 xoffset 3

    ease 0.03 xoffset 0

transform camera_shake_off(x=0):
    xoffset -15 + x
    ease 0.06 xoffset 15 + x
    ease 0.06 xoffset -13 + x
    ease 0.06 xoffset 11 + x
    ease 0.06 xoffset -9 + x
    ease 0.06 xoffset 7 + x
    ease 0.06 xoffset -5 + x
    ease 0.06 xoffset 3 + x

    ease 0.03 xoffset x

transform camera_spin:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    ease 1.75 matrixtransform RotateMatrix(0.0, 0.0, 360.0*2)
    pause 1.0

transform camera_dizzy:
    matrixcolor HueMatrix(0.0)
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    parallel:
        ease 1.4 matrixcolor HueMatrix(360.0)
    parallel:
        blur 0
        ease 0.7 blur 25
        ease 0.7 blur 0

transform camera_default:
    matrixcolor HueMatrix(0.0)
    blur 0
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    xoffset 0
    yoffset 0
    zoom 1.0
    xcenter 0.5
    ycenter 0.5
    zpos 0
    perspective True

# --------------------------------------------------------------- Battle Effects
image powerup:
    matrixcolor ColorizeMatrix("#ffffff","#71db6b")
    alpha 0.8
    yzoom 3
    xcenter 0.5
    yanchor 0
    ypos 1.0
    "images/props/effects/PUp.webp"

transform powup_trans(num=1):
    block:
        ypos 1.0
        yzoom 3

        parallel:
            ease 0.37-num*0.05 ypos -0.1
        parallel:
            ease 0.47-num*0.05 yzoom 0
        repeat num

image powerup 1:
    "powerup"
    powup_trans(1)

image powerup 2:
    "powerup"
    powup_trans(2)

image powerup 3:
    "powerup"
    powup_trans(3)

image powerdown:
    matrixcolor ColorizeMatrix("#ffffff","#e769a2")
    alpha 0.8
    yzoom 3
    xcenter 0.5
    yanchor 1.0
    ypos 0.0
    "images/props/effects/PDown.webp"

transform powdown_trans(num=1):
    block:
        ypos 0.0
        yzoom 3

        parallel:
            ease 0.37-num*0.05 ypos 1.1
        parallel:
            ease 0.47-num*0.05 yzoom 0

        repeat num

image powerdown 1:
    "powerdown"
    powdown_trans(1)

image powerdown 2:
    "powerdown"
    powdown_trans(2)

image powerdown 3:
    "powerdown"
    powdown_trans(3)

image sqer:
    "images/Props/Battles/Square.webp"
    xcenter 0.5
    ycenter 0.5
    zoom 0
    matrixtransform RotateMatrix(0,0,0)
    alpha 1

    parallel:
        pause 0.3
        ease 0.3 alpha 0
    parallel:
        linear 0.6 zoom 0.5 matrixtransform RotateMatrix(0,0,360*1.4)

transform sq_pulseOut(xC=0.5,yC=0.5,xTint="#ffffff"):

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        "sqer"
    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        pause 0.3
        "sqer"

image sqr:
    "images/Props/Battles/Square.webp"

    zoom 0.5
    matrixtransform RotateMatrix(0,0,0)
    alpha 0

    parallel:
        ease 0.2 alpha 1
        pause 0.2
        ease 0.2 alpha 0
    parallel:
        linear 0.6 zoom 0 matrixtransform RotateMatrix(0,0,360*1.4)

transform sq_pulseIn(xC=0.5,yC=0.5,xTint="#ffffff"):

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        "sqr"

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        pause 0.3
        "sqr"

transform circ(tZoom):
    "images/Props/Battles/Circle.webp"
    zoom 0
    alpha 1

    parallel:
        pause 0.2
        ease 0.3 alpha 0
    parallel:
        linear 0.5 zoom tZoom

transform c_trailUp(xC=0.5,yC=0.5,xTint="#ffffff"):

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        circ(0.3)

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        pause 0.125
        yoffset -75
        circ(0.25)

    contains:
        matrixcolor TintMatrix(xTint)
        xcenter xC
        ycenter yC
        pause 0.25
        yoffset -150
        circ(0.2)

image circTrans:
    zoom 0.3
    "images/Props/Battles/Circle.webp"
    xcenter 0.7
    ycenter 0.5
    block:
        parallel:
            ease 0.5 xcenter 0.3
            ease 0.5 xcenter 0.7
        parallel:
            easein 0.25 ycenter 0.7
            ease 0.5 ycenter 0.3
            easeout 0.25 ycenter 0.5
        repeat
