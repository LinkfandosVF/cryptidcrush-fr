init offset = -1

# HAZEL
define Hazel = Character("Hazel", image = "hazel", callback = Bleep,ctc="end_of_msg", cb_id = "8C", who_color = "#ee6756")

default Hazel_State = {
    "mouth": 3,
    "eyes": 0,
    "eyeFrame": 0,
    "brow": 0,

    "collar": True,
    "hairpin": True,
    "base": 0}

default Hazel_Default = {
    "mouth": 3,
    "eyes": 0,
    "eyeFrame": 0,
    "brow": 0,

    "collar": True,
    "hairpin": True,
    "base": 0}

layeredimage hazel:
    xanchor 0.5
    zoom 0.22
    ycenter 0.78
    always:
        ConditionSwitch(
            "Hazel_State['base'] <= 0","images/Characters/Hazel/Hazel_Base.webp",
            "Hazel_State['base'] >= 1", "images/Characters/Hazel/Hazel_Base2.webp")


    if Hazel_State["mouth"] > 0:
        ConditionSwitch(
            "Hazel_State['mouth'] <= 1", "images/Characters/Hazel/Hazel_Mouth1.webp",
            "Hazel_State['mouth'] == 2", "images/Characters/Hazel/Hazel_Mouth2.webp",
            "Hazel_State['mouth'] == 3", "images/Characters/Hazel/Hazel_Mouth3.webp",
            "Hazel_State['mouth'] == 4", "images/Characters/Hazel/Hazel_Mouth4.webp",
            "Hazel_State['mouth'] == 5", "images/Characters/Hazel/Hazel_Mouth5.webp",
            "Hazel_State['mouth'] >= 6", "images/Characters/Hazel/Hazel_Mouth6.webp")

    always:
        ConditionSwitch(
            "Hazel_State['eyeFrame'] <= 1", "Hazel_EyeFrameA",
            "Hazel_State['eyeFrame'] >= 2", "images/Characters/Hazel/Hazel_EyeFrame2.webp")

    always:
        ConditionSwitch(
            "Hazel_State['brow'] <= 0", "images/Characters/Hazel/Hazel_Brow1.webp",
            "Hazel_State['brow'] == 1", "images/Characters/Hazel/Hazel_Brow2.webp",
            "Hazel_State['brow'] >= 2", "images/Characters/Hazel/Hazel_Brow3.webp")

    if Hazel_State["collar"]:
        "images/Characters/Hazel/Hazel_Base_Collar.webp"

    if Hazel_State["hairpin"]:
        "images/Characters/Hazel/Hazel_Base_Hairpin.webp"




layeredimage Hazel_EyeFrameA:
    if Hazel_State['eyeFrame'] == 1:
        "images/Characters/Hazel/Hazel_EyeFrame1.webp"

    always:
        ConditionSwitch(
            "Hazel_State['eyeFrame'] <= 0", "Hazel_Eye_Blink",
            "True", "Hazel_Eye")


image Hazel_Eye:
    ConditionSwitch(
        "Hazel_State['eyes'] <= -1", "images/Characters/Hazel/Hazel_Eye0.webp",
        "Hazel_State['eyes'] == 0", "images/Characters/Hazel/Hazel_Eye1.webp",
        "Hazel_State['eyes'] == 1", "images/Characters/Hazel/Hazel_Eye2.webp",
        "Hazel_State['eyes'] == 2", "images/Characters/Hazel/Hazel_Eye3.webp",
        "Hazel_State['eyes'] == 3", "images/Characters/Hazel/Hazel_Eye4.webp",
        "Hazel_State['eyes'] == 4", "images/Characters/Hazel/Hazel_Eye5.webp",
        "Hazel_State['eyes'] >= 5", "images/Characters/Hazel/Hazel_Eye6.webp")

image Hazel_Eye_Blink:
    ConditionSwitch(
        "Hazel_State['eyes'] <= -1", "images/Characters/Hazel/Hazel_Eye0.webp",
        "Hazel_State['eyes'] == 0", "images/Characters/Hazel/Hazel_Eye1.webp",
        "Hazel_State['eyes'] == 1", "images/Characters/Hazel/Hazel_Eye2.webp",
        "Hazel_State['eyes'] == 2", "images/Characters/Hazel/Hazel_Eye3.webp",
        "Hazel_State['eyes'] == 3", "images/Characters/Hazel/Hazel_Eye4.webp",
        "Hazel_State['eyes'] == 4", "images/Characters/Hazel/Hazel_Eye5.webp",
        "Hazel_State['eyes'] >= 5", "images/Characters/Hazel/Hazel_Eye6.webp")

    choice:
        pause 9.0
    choice:
        pause 3.0
    choice:
        pause 6.0
    choice:
        pause 1.0

    "images/Characters/Hazel/Hazel_EyeBlink.webp"
    pause 0.2
    repeat
