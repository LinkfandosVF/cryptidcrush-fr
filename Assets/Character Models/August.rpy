init offset = -1
define August = Character("August", image = "august", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c") #AUGUSTUS
define AugustWolf = Character("August", image = "august", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c")

define NVL_August = Character("August", image = "mgus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c",kind=nvl)
define NVL_WolfAugust = Character("August", image = "wgus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c",kind=nvl)
define NVL_WolfAugust2 = Character("August", image = "hwgus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c",kind=nvl)

define NVL_DreamGus = Character("August", image = "dgus", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e8850c",kind=nvl)

image side dgus:
    zoom 0.2
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Dreamy_August.webp"
    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat

#NVL_NOT DOODLE
image side mgus:
    matrixcolor ColorizeMatrix("#1c1f4d","#f5824b")
    zoom 0.2
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_August.webp"
    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat
#NVL_WOLF GUS
image side wgus:
    matrixcolor ColorizeMatrix("#1c1f4d","#f5824b")
    zoom 0.17
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/wolfgus_mini.webp"
    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat
#happy wolf gus
image side hwgus:
    matrixcolor ColorizeMatrix("#1c1f4d","#f5824b")
    zoom 0.17
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/wolfgus_minihappy.webp"
    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat
# Human ------------------------------------------------------------------------
default August_State = { "eye": 3,
    "hair": 1,
    "eyeFrame": 0,
    "brow" : 0,
    "mouth": 5,
    "armL": 0,
    "armR" : 0,
    "sweater": False,
    "coat": False,
    "blush": False,
    "wolfEars": False,
    "hurt": False}

default August_Default = { "eye": 3,
    "hair": 1,
    "eyeFrame": 0,
    "brow" : 0,
    "mouth": 5,
    "armL": 0,
    "armR" : 0,
    "sweater": False,
    "coat": False,
    "blush": False,
    "wolfEars": False,
    "hurt": False}

transform presetgusblink(xStr="robyn"):
    xStr
    choice:
        pause 10.0
    choice:
        pause 2.0
    choice:
        pause 6.0
    choice:
        pause 0.5

    "images/Characters/August/August_EyesBlink.webp"
    pause 0.23
    repeat

#------------------------------------------------------------------ Model Emotes
layeredimage august:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        ConditionSwitch(
            "August_State['mouth'] <= 0", "images/Characters/August/August_Mouth1.webp",
            "August_State['mouth'] == 1", "images/Characters/August/August_Mouth2.webp",
            "August_State['mouth'] == 2", "images/Characters/August/August_Mouth3.webp",
            "August_State['mouth'] == 3", "images/Characters/August/August_Mouth4.webp",
            "August_State['mouth'] == 4", "images/Characters/August/August_Mouth5.webp",
            "August_State['mouth'] == 5", "images/Characters/August/August_Mouth6.webp",
            "August_State['mouth'] == 6", "images/Characters/August/August_Mouth7.webp",
            "August_State['mouth'] == 7", "images/Characters/August/August_Mouth8.webp",
            "August_State['mouth'] >= 8", "images/Characters/August/August_Mouth9.webp")

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        "augusteyes"

    #Brows
    always:
        ConditionSwitch(
            "August_State['brow'] <= 0", "images/Characters/August/August_Brows1.webp",
            "August_State['brow'] == 1", "images/Characters/August/August_Brows2.webp",
            "August_State['brow'] == 2", "images/Characters/August/August_Brows3.webp",
            "August_State['brow'] == 3", "images/Characters/August/August_Brows4.webp",
            "August_State['brow'] >= 4", "images/Characters/August/August_Brows5.webp")

    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"



image august default = "august"
# Basic Emotes
# Neutral   | Happy
# Annoyed   | Angry
# Sad       | Fear
# Surprised | Smug
# Thinking  | Sigh

layeredimage august neutral:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth6.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("images/Characters/August/August_Eyes4.webp")

    #Brows
    always:
        "images/Characters/August/August_Brows3.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"



layeredimage august happy:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth9.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("images/Characters/August/August_Eyes4.webp")

    #Brows
    always:
        "images/Characters/August/August_Brows1.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"

layeredimage august annoyed:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth6.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustannoyedeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows1.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"


layeredimage augustannoyedeyes:
    always:
        "images/Characters/August/August_Eyes1.webp"

    always:
        "images/Characters/August/August_EyesFrame1.webp"

layeredimage august angry:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth7.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustangryeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows1.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"


layeredimage augustangryeyes:
    always:
        "images/Characters/August/August_Eyes3.webp"

    always:
        "images/Characters/August/August_EyesFrame2.webp"

layeredimage august sad:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth5.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustsadeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows2.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"


layeredimage augustsadeyes:
    always:
        "images/Characters/August/August_Eyes3.webp"

    always:
        "images/Characters/August/August_EyesFrame2.webp"

layeredimage august fear:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth7.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustfeareyes")

    #Brows
    always:
        "images/Characters/August/August_Brows4.webp"

    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"

layeredimage augustfeareyes:
    always:
        "images/Characters/August/August_Eyes2.webp"

    always:
        "images/Characters/August/August_EyesFrame3.webp"

layeredimage august surprised:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth8.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("images/Characters/August/August_Eyes2.webp")

    #Brows
    always:
        "images/Characters/August/August_Brows3.webp"


    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"


layeredimage august smug:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth3.webp"


    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustsmugeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows1.webp"

    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"


layeredimage augustsmugeyes:
    always:
        "images/Characters/August/August_Eyes4.webp"

    always:
        "images/Characters/August/August_EyesFrame2.webp"

layeredimage august thinking:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth8.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustthinkingeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows4.webp"

    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"

layeredimage augustthinkingeyes:
    always:
        "images/Characters/August/August_Eyes1.webp"

    always:
        "images/Characters/August/August_EyesFrame1.webp"

layeredimage august sigh:
    xanchor 0.5
    zoom 0.175
    ycenter 0.8

    always:
        "august_background"

    #Mouth
    always:
        "images/Characters/August/August_Mouth1.webp"

    #Ears
    if August_State["wolfEars"]:
        "images/Characters/August/August_Base_Ears.webp"

    #Eyes
    always:
        presetgusblink("augustangryeyes")

    #Brows
    always:
        "images/Characters/August/August_Brows5.webp"

    #Blush
    if August_State["blush"]:
        "images/Characters/August/August_Base_Blush.webp"

#------------------------------------------------------------------ Model Pieces
layeredimage august_background:

    if August_State['armR'] <= 0:
        "images/Characters/August/August_ArmR1.webp"

    #Base
    always:
        "images/Characters/August/August_Base.webp"

    #Arm R1
    if August_State['armR'] >= 1:
        "images/Characters/August/August_ArmR2.webp"

    #Base
    always:
        "images/Characters/August/August_Base_ShirtLogo.webp"

    #Coat
    if August_State["coat"]:
        "images/Characters/August/August_Base_Coat.webp"

    #Arm L
    always:
        ConditionSwitch(
            "August_State['armL'] <= 1 or August_State['sweater'] or August_State['coat']", "images/Characters/August/August_ArmL2.webp",
            "August_State['armL'] >= 2", "images/Characters/August/August_ArmL3.webp")

    #Sweater
    if August_State["sweater"]:
        "images/Characters/August/August_Base_Sweater.webp"

    if August_State["coat"] or August_State["hair"] > 0:
        ConditionSwitch(
            "August_State['coat'] or August_State['hair'] == 1","images/Characters/August/August_Hair1.webp",
            "August_State['hair'] >= 2","images/Characters/August/August_Hair2.webp")


layeredimage guseyeswitch:
    always:
        ConditionSwitch(
            "August_State['eye'] <= 0", "images/Characters/August/August_Eyes1.webp",
            "August_State['eye'] == 1", "images/Characters/August/August_Eyes2.webp",
            "August_State['eye'] == 2", "images/Characters/August/August_Eyes3.webp",
            "August_State['eye'] == 3", "images/Characters/August/August_Eyes4.webp",
            "August_State['eye'] >= 4", "images/Characters/August/August_EyesBlink.webp")

    if August_State["eyeFrame"] > 0 and not August_State["hurt"]:
        ConditionSwitch(
            "August_State['eyeFrame'] == 1", "images/Characters/August/August_EyesFrame1.webp",
            "August_State['eyeFrame'] == 2", "images/Characters/August/August_EyesFrame2.webp",
            "August_State['eyeFrame'] == 3", "images/Characters/August/August_EyesFrame3.webp",
            "August_State['eyeFrame'] == 4", "images/Characters/August/August_EyesFrame4.webp",
            "August_State['eyeFrame'] >= 5", "images/Characters/August/August_EyesFrame5.webp")

image augusteyes:
    "guseyeswitch"
    choice:
        pause 10.0
    choice:
        pause 2.0
    choice:
        pause 6.0
    choice:
        pause 0.5

    ConditionSwitch(
        "August_State['eyeFrame'] != 5 or August_State['hurt']", "images/Characters/August/August_EyesBlink.webp",
        "True", "guseyeswitch")

    pause 0.23
    repeat


# Half -------------------------------------------------------------------------
default HalfAugust_State = { "eye": 0,
    "eyeFrame": 0,
    "brow": 0,
    "mouth": 0,
    "ear": 0,
    "blush": False,
    "sparkle": False,
    "shirt": 1,
    "pants": True }

#IDK WHAT IM DOING HERE GIRL
default HalfAugust_Default = { "eye": 0,
    "eyeFrame": 0,
    "brow": 0,
    "mouth": 0,
    "ear": 0,
    "blush": 0,
    "sparkle": 0,
    "shirt": 1,
    "pants": True }

image halfaugust_eyeblink:
    "halfaugust_eye"
    choice:
        pause 10.0
    choice:
        pause 2.0
    choice:
        pause 6.0
    choice:
        pause 0.5

    "halfaugust_blink"
    pause 0.23
    repeat

layeredimage halfaugust_eye:
    always:
        ConditionSwitch(
            "HalfAugust_State['eye'] <= 0" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Eye1.png",
            "HalfAugust_State['eye'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Eye2.png",
            "HalfAugust_State['eye'] == 2" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Eye3.png",
            "HalfAugust_State['eye'] >= 3" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Eye4.png")

    if HalfAugust_State['eyeFrame'] > 0:
        ConditionSwitch(
            "HalfAugust_State['eyeFrame'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_EyeFrame.png",
            "HalfAugust_State['eyeFrame'] == 2" , "images/Characters/August/Halfwolf/HG_2023/HGus2_EyeFrame2.png",
            "HalfAugust_State['eyeFrame'] >= 3" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Blink.png")

layeredimage halfaugust_blink:
    #Brow
    if HalfAugust_State['eyeFrame'] <= 1:
        "images/Characters/August/Halfwolf/HG_2023/HGus2_Blink.png"
    else:
        "halfaugust_eye"

layeredimage halfaugust:
    xanchor 0.5
    zoom 0.213
    ycenter 0.675

    #Base
    always:
        "images/Characters/August/Halfwolf/HG_2023/HGus2_Base.png"

    #ears
    always:
        ConditionSwitch(
            "HalfAugust_State['ear'] <= 0" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Ears1.png",
            "HalfAugust_State['ear'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Ears2.png",
            "HalfAugust_State['ear'] >= 2" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Ears3.png")

    #Eye
    always:
        "halfaugust_eyeblink"

    always:
        ConditionSwitch(
            "HalfAugust_State['brow'] <= 0" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Brow0.png",
            "HalfAugust_State['brow'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Brow1.png",
            "HalfAugust_State['brow'] >= 2" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Brow2.png")

    #Mouth
    always:
        ConditionSwitch(
            "HalfAugust_State['mouth'] <= 0" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth1.png",
            "HalfAugust_State['mouth'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth2.png",
            "HalfAugust_State['mouth'] == 2" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth3.png",
            "HalfAugust_State['mouth'] == 3" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth4.png",
            "HalfAugust_State['mouth'] == 4" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth5.png",
            "HalfAugust_State['mouth'] == 5" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth6.png",
            "HalfAugust_State['mouth'] >= 6" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Mouth7.png")

    if HalfAugust_State['pants']:
        "images/Characters/August/Halfwolf/HG_2023/HGus2_Pants.png"

    if HalfAugust_State['shirt'] > 0:
        ConditionSwitch(
            "HalfAugust_State['shirt'] == 1" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Shirt.png",
            "True" , "images/Characters/August/Halfwolf/HG_2023/HGus2_Gown.png")

    if HalfAugust_State['blush']:
        "images/Characters/August/Halfwolf/HG_2023/HGus2_Blush.png"

    if HalfAugust_State['sparkle']:
        "images/Characters/August/Halfwolf/HG_2023/HGus2_Sparkle.png"

# Wolf -------------------------------------------------------------------------
default WolfAugust_State = { "head": 3,
    "eyes" : 2,
    "eyeFrame" : 0,
    "brow": 1,
    "pants": False,
    "shirt": True,
    "undies": True,
    "hurt": True}

default WolfAugust_Default = { "head": 3,
    "eyes" : 2,
    "eyeFrame" : 0,
    "brow": 1,
    "pants": False,
    "shirt": True,
    "undies": True,
    "hurt": True}

image WGusEyeglow:
    matrixcolor SaturationMatrix(2.0)
    "images/Characters/August/Werewolf/WGus_EyeGlow.webp"

layeredimage wolfaugust:
    xanchor 0.5
    zoom 0.18
    ycenter 0.66
    #Base
    always:
        "images/Characters/August/Werewolf/WGus_Base.webp"

    #Head
    always:
        ConditionSwitch(
            "WolfAugust_State['head'] >=5","waugust_talkies",
            "WolfAugust_State['head'] == 4","images/Characters/August/Werewolf/WGus_Head3.webp",
            "WolfAugust_State['head'] > 1", "images/Characters/August/Werewolf/WGus_Head2A.webp",
            "WolfAugust_State['head'] <= 1", "images/Characters/August/Werewolf/WGus_Head1A.webp")

    if WolfAugust_State['head'] == 1:
        "images/Characters/August/Werewolf/WGus_Head1B.webp"
    elif WolfAugust_State['head'] == 3:
        "images/Characters/August/Werewolf/WGus_Head2B.webp"

    #Eyes
    if WolfAugust_State['eyeFrame'] != 2:
        ConditionSwitch(
            "WolfAugust_State['eyes'] <= 0", "images/Characters/August/Werewolf/WGus_Eye1.webp",
            "WolfAugust_State['eyes'] == 1", "images/Characters/August/Werewolf/WGus_Eye2.webp",
            "WolfAugust_State['eyes'] >= 2", "waugust_franticeyes")


    if WolfAugust_State['eyeFrame'] > 0 and WolfAugust_State['eyeFrame'] <= 2:
        ConditionSwitch(
            "WolfAugust_State['eyeFrame'] == 1", "images/Characters/August/Werewolf/WGus_EyeFrame1.webp",
            "WolfAugust_State['eyeFrame'] == 2","images/Characters/August/Werewolf/WGus_EyeFrame2.webp")

    if WolfAugust_State['eyeFrame'] != 2:
        "waugust_blink"

    #Brow
    if WolfAugust_State['eyeFrame'] != 2:
        ConditionSwitch(
            "WolfAugust_State['brow'] == 0", "images/Characters/August/Werewolf/WGus_Brow1.webp",
            "WolfAugust_State['brow'] == 1", "images/Characters/August/Werewolf/WGus_Brow2.webp",
            "WolfAugust_State['brow'] == 2", "images/Characters/August/Werewolf/WGus_Brow3.webp")

    #Clothes
    if WolfAugust_State['pants']:
        "images/Characters/August/Werewolf/WGus_EX_Sweatpants.webp"

    if WolfAugust_State['shirt']:
        "images/Characters/August/Werewolf/WGus_EX_Shirt.webp"

    if WolfAugust_State['undies']:
        "images/Characters/August/Werewolf/WGus_EX_Meundies.webp"

    #Bloodied
    if WolfAugust_State['hurt']:
        "images/Characters/August/Werewolf/WGus_EX_Hurt.webp"

image waugust_talkies:
    "images/Characters/August/Werewolf/WGus_Head2A.webp"
    pause 0.2
    "images/Characters/August/Werewolf/WGus_Head1A.webp"
    pause 0.2
    repeat

image waugust_franticeyes:
    "images/Characters/August/Werewolf/WGus_Eye1.webp"
    choice:
        pause 1
    choice:
        pause 0.5
    "images/Characters/August/Werewolf/WGus_Eye2.webp"
    choice:
        pause 1
    choice:
        pause 0.5
    repeat

image waugust_blink:
    "images/Characters/August/Werewolf/WGus_Eye_Blink.webp"
    alpha 0
    choice:
        pause 2.5
    choice:
        pause 1
    choice:
        pause 2
    alpha 1

    choice:
        # ConditionSwitch(
        #     "August_State['hurt'] == True", "images/Characters/August/Gus_Eye_Blink_Hurt.webp",
        #     "True", "images/Characters/August/Gus_Eye_Blink.webp")
        pause 0.15
    choice:
        # ConditionSwitch(
        #     "August_State['hurt'] == True", "images/Characters/August/Gus_Eye_Blink_Hurt.webp",
        #     "True", "images/Characters/August/Gus_Eye_Blink.webp")
        pause 0.1
        alpha 0
        pause 0.1
        alpha 1
        pause 0.15
    repeat
