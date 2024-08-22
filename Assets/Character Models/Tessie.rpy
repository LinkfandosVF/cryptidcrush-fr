define Tessie = Character("Tessie", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "#57fcd0")

image tessie_eye_blink:
    "tessie_eye"
    choice:
        pause 10.0
    choice:
        pause 5.0
    "images/Characters/Tessie/Tessie_Eye_Blink.webp"
    pause 0.15
    repeat

layeredimage tessie_eye:
    always:
        ConditionSwitch(
            "Tessie_State['eye'] <= 0", "images/Characters/Tessie/Tessie_Eye1.webp",
            "Tessie_State['eye'] == 1", "images/Characters/Tessie/Tessie_Eye2.webp",
            "Tessie_State['eye'] == 2", "images/Characters/Tessie/Tessie_Eye3.webp",
            "Tessie_State['eye'] >= 3", "images/Characters/Tessie/Tessie_Eye4.webp")

    if Tessie_State['eyeFrame'] > 0:
        ConditionSwitch(
            "Tessie_State['eyeFrame'] == 1", "images/Characters/Tessie/Tessie_EyeFrame1.webp",
            "Tessie_State['eyeFrame'] >= 2", "images/Characters/Tessie/Tessie_EyeFrame2.webp")

default Tessie_State = { "eye": 0,
    "brow" : 0,
    "eyeFrame": 0,
    "mouth": 0}

default Tessie_Default = { "eye": 0,
    "brow" : 0,
    "eyeFrame": 0,
    "mouth": 0}

layeredimage tessie:
    xanchor 0.5
    zoom 0.165
    ycenter 0.7

    #Base
    always:
        "images/Characters/Tessie/Tessie_Base.webp"

    #Mouths
    always:
        ConditionSwitch(
            "Tessie_State['mouth'] <= 0", "images/Characters/Tessie/Tessie_Mouth4.webp",
            "Tessie_State['mouth'] == 1", "images/Characters/Tessie/Tessie_Mouth2.webp",
            "Tessie_State['mouth'] == 2", "images/Characters/Tessie/Tessie_Mouth3.webp",
            "Tessie_State['mouth'] == 3", "images/Characters/Tessie/Tessie_Mouth1.webp",
            "Tessie_State['mouth'] == 4", "images/Characters/Tessie/Tessie_Mouth5.webp",
            "Tessie_State['mouth'] == 5", "images/Characters/Tessie/Tessie_Mouth6.webp",
            "Tessie_State['mouth'] >= 6", "images/Characters/Tessie/Tessie_Mouth7.webp")

    #Eyes
    always:
        "tessie_eye_blink"

    #Eyebrows
    always:
        ConditionSwitch(
            "Tessie_State['brow'] <= 0", "images/Characters/Tessie/Tessie_Brow1.webp",
            "Tessie_State['brow'] == 1", "images/Characters/Tessie/Tessie_Brow2.webp",
            "Tessie_State['brow'] >= 2", "images/Characters/Tessie/Tessie_Brow3.webp")
