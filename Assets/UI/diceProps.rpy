
# Dice Menu Animations
transform rerollButton_anim:
    xanchor 0.0
    yanchor 0.0
    xpos 0.76
    ypos 353
    zoom 0.32

    on show:
        xzoom 1.2
        yzoom 0
        pause 1.0
        parallel:
            ease 0.25 ypos 353
        parallel:
            ease 0.25 yzoom 1.3 xzoom 0.8
            ease 0.125 yzoom 0.8 xzoom 1.3
            ease 0.125 yzoom 1 xzoom 1

    on hide:
        ypos 353
        ease 0.2 ypos 430 xzoom 0.7 yzoom 0

transform dice_menu_location:
    xcenter 0.77

    on show:
        xcenter 0.77
        ypos -500
        ease 0.5 ypos 0 xzoom 0.8 yzoom 1.3
        ease 0.125 xzoom 1.2 yzoom 0.9
        ease 0.125 xzoom 0.95 yzoom 1.1
        ease 0.125 xzoom 1.05 yzoom 0.975
        ease 0.125 xzoom 1.0 yzoom 1.0

    on hide:
        ease 0.2 yzoom 1.2 xzoom 0.8
        ease 0.35 ypos -600 xzoom 0.5 yzoom 1.3

transform dice_menu_extras:
    xcenter 0.77

    on show:
        xcenter 0.77
        ypos 0
        alpha 0
        ease 0.4 alpha 1.0

    on hide:
        ease 0.2 yzoom 1.2 xzoom 0.8
        ease 0.35 ypos -600 xzoom 0.5 yzoom 1.3

transform dice_menu_rollingGlow:
    matrixcolor ColorizeMatrix("#006a0e", "#52e965")
    block:
        choice:
            ease 1.5 matrixcolor ColorizeMatrix("#156751", "#10FCBB")
        choice:
            ease 2.0 matrixcolor ColorizeMatrix("#3e2254", "#bb67ff")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#00376a", "#52e5e9")
        choice:
            ease 2.0 matrixcolor ColorizeMatrix("#4f0b42", "#ff93dd")
        choice:
            ease 1.5 matrixcolor ColorizeMatrix("#006a0e", "#52e965")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#543122", "#ff8941")
        repeat

transform dice_menu_rollingGlow2:
    matrixcolor ColorizeMatrix("#006a0e", "#52e965")
    block:
        choice:
            ease 2.0 matrixcolor ColorizeMatrix("#156751", "#10FCBB")
        choice:
            ease 1.5 matrixcolor ColorizeMatrix("#3e2254", "#bb67ff")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#00376a", "#52e5e9")
        choice:
            ease 2.0 matrixcolor ColorizeMatrix("#4f0b42", "#ff93dd")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#006a0e", "#52e965")
        choice:
            ease 1.5 matrixcolor ColorizeMatrix("#543122", "#ff8941")
        repeat

transform dice_menu_successGlow:
    matrixcolor ColorizeMatrix("#006a0e", "#52e965")
    block:
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#156751", "#10FCBB")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#00376a", "#52e5e9")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#006a0e", "#52e965")
        repeat

transform dice_menu_failGlow:
    ease 2.0 matrixcolor ColorizeMatrix("#4f0b42", "#ff93dd")
    block:
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#3e2254", "#bb67ff")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#4f0b42", "#ff93dd")
        choice:
            ease 1.75 matrixcolor ColorizeMatrix("#543122", "#ff8941")
        repeat

transform dice_menu_textTransform:
    on show:
        yzoom 1.0
        alpha 0
        pause 0.6
        ease 0.4 alpha 1.0
    on hide:
        ease 0.1 yoffset 20 yzoom 0

transform resultSpin:
    on show:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        choice:
            ease 0.6 matrixtransform RotateMatrix(0.0, 0.0, -360.0*2)
        choice:
            ease 0.6 matrixtransform RotateMatrix(0.0, 0.0, 360.0*2)

transform resultSpinCoin:
    perspective True
    on show:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        choice:
            ease 0.8 matrixtransform RotateMatrix(0.0, -360.0*2, 0)
        choice:
            ease 0.8 matrixtransform RotateMatrix(0.0, 360.0*2, 0)

image DiceMenu:
    zoom 0.5
    "gui/DiceMenu/diceBox_Base.webp"

layeredimage dBEyeBase:
    always:
        "gui/DiceMenu/diceBox_EyeBack.webp"

    always:
        "gui/DiceMenu/diceBox_Eyes.webp"

image DiceMenuEyes:
    zoom 0.5
    "dBEyeBase"

image DiceMenuGlowL:
    zoom 0.5
    "gui/DiceMenu/diceBox_GlowL.webp"

image DiceMenuGlowR:
    zoom 0.5
    "gui/DiceMenu/diceBox_GlowR.webp"

image DiceMenuFailFrame:
    zoom 0.5
    "gui/DiceMenu/diceBox_FailFrame.webp"

#--------------------------------------- Result Effects

image successFlash:
    alpha 0.0
    "images/Props/effects/successflash.webp"
    linear 0.05 alpha 0.5
    pause 0.1
    ease 0.75 alpha 0.0

image failFlash:
    alpha 0.0
    "images/Props/effects/failflash.webp"
    linear 0.05 alpha 1.0
    pause 0.1
    ease 0.75 alpha 0.0

define rFlash = {True:ColorizeMatrix("#063023","#8efb9d"),False:ColorizeMatrix("#300606","#fc5c91")}
transform resultFlash(success=True):
    matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)
    ease 0.1 matrixcolor rFlash[success]*SaturationMatrix(0.5)
    pause 0.1
    ease 0.4 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)
