define Edith = Character("Edith", callback = Bleep,ctc="end_of_msg", cb_id = "7B", who_color = "#aad8dd")

default Edith_State = { "eye": 0,
    "eyeframe": 0,
    "brow": 0,
    "mouth" : 0,
    "hat": False,
    "socks": True,
    "armR": 0,
    "armL":0}

default Edith_Default = { "eye": 0,
    "eyeframe": 0,
    "brow": 0,
    "mouth" : 0,
    "hat": False,
    "socks": True,
    "armR": 0,
    "armL":0}

image edithblink:
    "images/Characters/Edith/Edith_Eye_Blink.webp"
    alpha 0
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    alpha 1
    pause 0.5
    repeat

layeredimage edith:
    xanchor 0.5
    ycenter 0.825
    zoom 0.185
    always:
        ConditionSwitch(
            "Edith_State['armR'] <=0", "images/Characters/Edith/Edith_ArmR1.webp",
            "Edith_State['armR'] >= 1", "images/Characters/Edith/Edith_ArmR2.webp")

    always:
        "images/Characters/Edith/Edith_Base.webp"

    if Edith_State['socks']:
        "images/Characters/Edith/Edith_EX_Socks.webp"

    if Edith_State['eyeframe'] > 0:
        ConditionSwitch(
            "Edith_State['eyeframe'] == 1", "images/Characters/Edith/Edith_EyeFrame1.webp",
            "Edith_State['eyeframe'] == 2", "images/Characters/Edith/Edith_EyeFrame2.webp",
            "Edith_State['eyeframe'] >= 3", "images/Characters/Edith/Edith_EyeFrame_Glasses.webp")

    if Edith_State['eyeframe'] < 3:
        ConditionSwitch(
            "Edith_State['eye'] <= 0", "images/Characters/Edith/Edith_Eye1.webp",
            "Edith_State['eye'] == 1", "images/Characters/Edith/Edith_Eye2.webp",
            "Edith_State['eye'] == 2", "images/Characters/Edith/Edith_Eye3.webp",
            "Edith_State['eye'] >= 3", "images/Characters/Edith/Edith_Eye4.webp")

    elif Edith_State['eyeframe'] == 4:
        "images/Characters/Edith/Edith_Eye_Glasses.webp"

    if Edith_State['eyeframe'] < 3:
        "edithblink"

    if Edith_State['eyeframe'] == 0:
        ConditionSwitch(
            "Edith_State['brow'] <= 0", "images/Characters/Edith/Edith_Brow1.webp",
            "Edith_State['brow'] == 1", "images/Characters/Edith/Edith_Brow2.webp",
            "Edith_State['brow'] == 2", "images/Characters/Edith/Edith_Brow3.webp",
            "Edith_State['brow'] >= 3", "images/Characters/Edith/Edith_Brow4.webp")

    if Edith_State['mouth'] > 0:
        ConditionSwitch(
            "Edith_State['mouth'] == 1", "images/Characters/Edith/Edith_Mouth1.webp",
            "Edith_State['mouth'] == 2", "images/Characters/Edith/Edith_Mouth2.webp",
            "Edith_State['mouth'] == 3", "images/Characters/Edith/Edith_Mouth3.webp",
            "Edith_State['mouth'] == 4", "images/Characters/Edith/Edith_Mouth4.webp",
            "Edith_State['mouth'] == 5", "images/Characters/Edith/Edith_Mouth5.webp",
            "Edith_State['mouth'] >= 6", "images/Characters/Edith/Edith_Mouth6.webp")

    if Edith_State['hat']:
        "images/Characters/Edith/Edith_EX_Hat.webp"



    always:
        ConditionSwitch(
            "Edith_State['armL'] <=0", "images/Characters/Edith/Edith_ArmL1.webp",
            "Edith_State['armL'] >= 1", "images/Characters/Edith/Edith_ArmL1.webp")
