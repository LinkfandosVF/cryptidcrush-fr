define Oz = Character("Oz", image = "oswald", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#fffb42")
define NVL_Oz = Character("Oz", image = "oz", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#fffb42",kind=nvl)
#---------------------DREAM OZZIE
image side oz:
    matrixcolor ColorizeMatrix("#131c11","#ffd16a")
    zoom 0.12
    anchor (0.5,1.0)
    pos (0.77,1.0)
    "images/Characters/Minis/Mini_Oz.webp"
    block:
        yzoom 1
        pause 1
        yzoom 0.9
        pause 0.8
        repeat

default OH_State = { "eyes": 0,
    "eyeFrame": 0,
    "brow": 0,
    "armL": 0,
    "armR": 0,
    "mask": False,
    "breath": True,
    "drool": False}

default OH_Default = { "eyes": 0,
    "eyeFrame": 0,
    "brow": 0,
    "armL": 0,
    "armR": 0,
    "mask": False,
    "breath": True,
    "drool": False}

image Oz_ArmL4:
    "images/Characters/Oswald Howler/Oz_ArmL3.webp"
    pause 0.3
    "images/Characters/Oswald Howler/Oz_ArmL3B.webp"
    pause 0.4
    repeat

image Oz_ArmL5:
    "images/Characters/Oswald Howler/Oz_ArmL3.webp"
    pause 0.3
    "images/Characters/Oswald Howler/Oz_ArmL2.webp"
    pause 0.4
    "images/Characters/Oswald Howler/Oz_ArmL3.webp"
    pause 0.2
    "images/Characters/Oswald Howler/Oz_ArmL2.webp"
    pause 2.0
    repeat

layeredimage oswald:
    zoom 0.21
    ycenter 0.65
    xanchor 0.5

    #Right Arm
    if OH_State["armR"] == 1 or OH_State["armR"] == 0 and OH_State["armL"] > 0:
        "images/Characters/Oswald Howler/Oz_ArmR1.webp"

    #Body
    always:
        "images/Characters/Oswald Howler/Oz_Base.webp"

    always:
        "images/Characters/Oswald Howler/Oz_Base_Hair.webp"

    #Arms
    if OH_State["armL"] == 0 and OH_State["armR"] == 0:
        "images/Characters/Oswald Howler/Oz_ArmRL1.webp"
    elif OH_State["armL"] == -1 and OH_State["armR"] == -1:
        "images/Characters/Oswald Howler/Oz_ArmRL2.webp"
    elif OH_State["armR"] > 1:
        ConditionSwitch(
            "OH_State['armR'] == 2", "images/Characters/Oswald Howler/Oz_ArmR2.webp",
            "OH_State['armR'] == 3", "images/Characters/Oswald Howler/Oz_ArmR3.webp")



    #Drool
    if OH_State["drool"]:
        "images/Characters/Oswald Howler/Oz_EX_Drool.webp"

    #Mask
    if OH_State["mask"]:
        "images/Characters/Oswald Howler/Oz_EX_Mask.webp"

    if OH_State["armL"] > 0:
        ConditionSwitch(
            "OH_State['armL'] == 1", "images/Characters/Oswald Howler/Oz_ArmL1.webp",
            "OH_State['armL'] == 2", "images/Characters/Oswald Howler/Oz_ArmL2.webp",
            "OH_State['armL'] == 3", "images/Characters/Oswald Howler/Oz_ArmL3.webp",
            "OH_State['armL'] == 4", "Oz_ArmL4",
            "OH_State['armL'] == 5", "Oz_ArmL5",
            "OH_State['armL'] == 6", "images/Characters/Oswald Howler/Oz_ArmL4.webp",
            "OH_State['armL'] >= 7", "images/Characters/Oswald Howler/Oz_ArmL5.webp")

    elif OH_State["armR"] > 0:
        "images/Characters/Oswald Howler/Oz_ArmL1.webp"

    #Eyes
    if OH_State["eyeFrame"] == 1 or OH_State['eyes'] == 3:
        "images/Characters/Oswald Howler/Oz_EyeFrame1.webp"

    always:
        ConditionSwitch(
            "OH_State['eyes'] <= 0", "images/Characters/Oswald Howler/Oz_Eye1.webp",
            "OH_State['eyes'] == 1", "images/Characters/Oswald Howler/Oz_Eye2.webp",
            "OH_State['eyes'] == 2", "images/Characters/Oswald Howler/Oz_Eye3.webp",
            "OH_State['eyes'] == 3", "images/Characters/Oswald Howler/Oz_Eye4.webp",
            "OH_State['eyes'] == 4", "images/Characters/Oswald Howler/Oz_Eye5.webp",
            "OH_State['eyes'] == 5", "images/Characters/Oswald Howler/Oz_Eye6.webp",
            "OH_State['eyes'] >= 6", "images/Characters/Oswald Howler/Oz_Eye7.webp")

    if OH_State["eyeFrame"] == 0 and OH_State["eyes"] < 2:
        "oz_blink"


    #Breath
    if OH_State["breath"]:
        "oz_breath"

    #Eye Brows
    always:
        ConditionSwitch(
            "OH_State['brow'] <= 0 or OH_State['eyes'] == 2", "images/Characters/Oswald Howler/Oz_Brow1.webp",
            "OH_State['brow'] == 1", "images/Characters/Oswald Howler/Oz_Brow2.webp",
            "OH_State['brow'] == 2", "images/Characters/Oswald Howler/Oz_Brow3.webp",
            "OH_State['brow'] == 3", "images/Characters/Oswald Howler/Oz_Brow4.webp",
            "OH_State['brow'] >= 4", "images/Characters/Oswald Howler/Oz_Brow5.webp")

image oswald default = "oswald"

layeredimage oswald casual:
    zoom 0.21
    ycenter 0.65
    xanchor 0.5

    #Body
    always:
        "images/Characters/Oswald Howler/Oz_Casual_Base.webp"

    #Drool
    if OH_State["drool"]:
        "images/Characters/Oswald Howler/Oz_EX_Drool.webp"

    #Mask
    if OH_State["mask"]:
        "images/Characters/Oswald Howler/Oz_EX_Mask.webp"

    if OH_State["armL"] > 0:
        ConditionSwitch(
            "OH_State['armL'] == 1", "images/Characters/Oswald Howler/Oz_ArmL1.webp",
            "OH_State['armL'] == 2", "images/Characters/Oswald Howler/Oz_ArmL2.webp",
            "OH_State['armL'] == 3", "images/Characters/Oswald Howler/Oz_ArmL3.webp",
            "OH_State['armL'] == 4", "Oz_ArmL4",
            "OH_State['armL'] == 5", "Oz_ArmL5",
            "OH_State['armL'] >= 6", "images/Characters/Oswald Howler/Oz_ArmL4.webp")
    elif OH_State["armR"] > 0:
        "images/Characters/Oswald Howler/Oz_ArmL1.webp"

    #Eyes
    if OH_State["eyeFrame"] == 1 or OH_State['eyes'] == 3:
        "images/Characters/Oswald Howler/Oz_EyeFrame1.webp"

    always:
        ConditionSwitch(
            "OH_State['eyes'] <= 0", "images/Characters/Oswald Howler/Oz_Eye1.webp",
            "OH_State['eyes'] == 1", "images/Characters/Oswald Howler/Oz_Eye2.webp",
            "OH_State['eyes'] == 2", "images/Characters/Oswald Howler/Oz_Eye3.webp",
            "OH_State['eyes'] == 3", "images/Characters/Oswald Howler/Oz_Eye4.webp",
            "OH_State['eyes'] == 4", "images/Characters/Oswald Howler/Oz_Eye5.webp",
            "OH_State['eyes'] == 5", "images/Characters/Oswald Howler/Oz_Eye6.webp",
            "OH_State['eyes'] == 6", "images/Characters/Oswald Howler/Oz_Eye7.webp",
            "OH_State['eyes'] >= 7", "images/Characters/Oswald Howler/Oz_Eye_Blink.webp")

    if OH_State["eyeFrame"] == 0 and OH_State["eyes"] < 2:
        "oz_blink"

    #Breath
    if OH_State["breath"]:
        "oz_breath"

    always:
        "images/Characters/Oswald Howler/Oz_Casual_Base_Hair.webp"

    #Eye Brows
    always:
        ConditionSwitch(
            "OH_State['brow'] <= 0", "images/Characters/Oswald Howler/Oz_Brow1.webp",
            "OH_State['brow'] == 1", "images/Characters/Oswald Howler/Oz_Brow2.webp",
            "OH_State['brow'] == 2", "images/Characters/Oswald Howler/Oz_Brow3.webp",
            "OH_State['brow'] >= 3", "images/Characters/Oswald Howler/Oz_Brow4.webp")



image oz_blink:
    alpha 0

    choice:
        pause 15.0
    choice:
        pause 3
    choice:
        pause 9
    choice:
        pause 2.25

    alpha 1
    "images/Characters/Oswald Howler/Oz_Eye_Blink.webp"
    pause 0.5
    repeat

image oz_breath:
    zoom 1.0
    alpha 0
    blur 30
    choice:
        pause 5.0
    choice:
        pause 4.0
    choice:
        pause 3.0

    "images/Characters/Oswald Howler/Oz_EX_Breath.webp"
    ease 0.75 alpha 1 blur 0
    ease 1.5 alpha 0 blur 30 zoom 0.8
    repeat
