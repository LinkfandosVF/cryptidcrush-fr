define Goatmaam = Character("Goatma'am", callback = Bleep,ctc="end_of_msg", cb_id = "2C", who_color = "#bc8bff")

default GM_State = { "eyes": 3,
    "mouth": 0,
    "scarf": False,
    "armL": 0,
    "armR": 0,
    "ears": 0}

default GM_Default = { "eyes": 3,
    "mouth": 0,
    "scarf": False,
    "armL": 0,
    "armR": 0,
    "ears": 0}

layeredimage goatmaam:
    zoom 0.2
    ycenter 0.78
    xanchor 0.5

    #Arm1
    if GM_State['armR'] == 1:
        "images/Characters/Goatmaam/GM_ArmR1.webp"

    #Tail
    always:
        "images/Characters/Goatmaam/GM_Tail.webp"

    #Base
    always:
        "images/Characters/Goatmaam/GM_Base.webp"

    #Ears
    always:
        ConditionSwitch(
            "GM_State['ears'] <= 0", "images/Characters/Goatmaam/GM_Base_Ears.webp",
            "GM_State['ears'] == 1", "images/Characters/Goatmaam/GM_Base_Ears2.webp",
            "GM_State['ears'] >= 2", "gm_earsflutter")


    #ArmR
    if GM_State['armR'] > 1:
        ConditionSwitch(
            "GM_State['armR'] >= 2", "images/Characters/Goatmaam/GM_ArmR2.webp")

    #ArmL
    if GM_State['armL'] > 0:
        ConditionSwitch(
            "GM_State['armL'] == 1", "images/Characters/Goatmaam/GM_ArmL1.webp",
            "GM_State['armL'] >= 2", "images/Characters/Goatmaam/GM_ArmL2.webp")

    #Mouth
    always:
        ConditionSwitch(
            "GM_State['eyes'] <= 0", "images/Characters/Goatmaam/GM_Eye1.webp",
            "GM_State['eyes'] == 1", "images/Characters/Goatmaam/GM_Eye2.webp",
            "GM_State['eyes'] == 2", "images/Characters/Goatmaam/GM_Eye3.webp",
            "GM_State['eyes'] == 3", "images/Characters/Goatmaam/GM_Eye4.webp",
            "GM_State['eyes'] == 4", "images/Characters/Goatmaam/GM_Eye5.webp",
            "GM_State['eyes'] == 5", "images/Characters/Goatmaam/GM_Eye6.webp",
            "GM_State['eyes'] >= 6", "images/Characters/Goatmaam/GM_Eye7.webp")

    #Mouth
    always:
        ConditionSwitch(
            "GM_State['mouth'] <= 0", "images/Characters/Goatmaam/GM_Mouth1.webp",
            "GM_State['mouth'] == 1", "images/Characters/Goatmaam/GM_Mouth2.webp",
            "GM_State['mouth'] == 2", "images/Characters/Goatmaam/GM_Mouth3.webp",
            "GM_State['mouth'] == 3", "images/Characters/Goatmaam/GM_Mouth4.webp",
            "GM_State['mouth'] == 4", "images/Characters/Goatmaam/GM_Mouth5.webp",
            "GM_State['mouth'] == 5", "images/Characters/Goatmaam/GM_Mouth6.webp",
            "GM_State['mouth'] >= 6", "images/Characters/Goatmaam/GM_Mouth7.webp",
            "GM_State['mouth'] >= 6", "images/Characters/Goatmaam/GM_Mouth8.webp")

    #Scarf
    if GM_State['scarf']:
        "images/Characters/Goatmaam/GM_Base_ScarfUp.webp"

image gm_earsflutter:
    "images/Characters/Goatmaam/GM_Base_Ears.webp"
    pause 0.25
    "images/Characters/Goatmaam/GM_Base_Ears2.webp"
    pause 0.25
    repeat

image nekonomicon:
    zoom 0.2
    ycenter 0.6
    xanchor 0.5
    "images/Characters/Dungeon Maestro/Nekonomicon/Neko_Default.webp"
