init offset = -1
default Atticus = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ED2A82")

default Atticus_State = { "eye": 0,
    "armR" : 0,
    "sleep": False}

default Atticus_Default = { "eye": 0,
    "armR" : 0,
    "sleep": False}

image atticusGlowA:
    alpha 1
    "images/Characters/Atticus Indrid/Atticus_Base_Dream_Glow.webp"
    choice:
        ease 3 alpha 0.5
    choice:
        ease 5 alpha 0.5
    pause 0.5
    choice:
        ease 3 alpha 1
    choice:
        ease 5 alpha 1
    pause 0.5
    repeat

image atticusGlowB:
    alpha 1
    "images/Characters/Atticus Indrid/Atticus_Base_Dream_GlowB.webp"
    choice:
        ease 2 alpha 0.5
    choice:
        ease 4 alpha 0.5
    choice:
        ease 6 alpha 0.5
    pause 0.5
    choice:
        ease 2 alpha 1
    choice:
        ease 4 alpha 1
    choice:
        ease 6 alpha 1
    pause 0.5
    repeat


layeredimage atticus:
    xanchor 0.5
    ycenter 0.7
    zoom 0.3

    always:
        "images/Characters/Atticus Indrid/Atticus_Base.webp"

    if Atticus_State["armR"] == 0:
        "images/Characters/Atticus Indrid/Atticus_ArmR1.webp"
    elif Atticus_State["armR"] == 1:
        "images/Characters/Atticus Indrid/Atticus_ArmR2.webp"

    if Atticus_State["eye"] == 1:
        "images/Characters/Atticus Indrid/Atticus_Eye1.webp"
    elif Atticus_State["eye"] == 2:
        "images/Characters/Atticus Indrid/Atticus_Eye2.webp"
    elif Atticus_State["eye"] == 3:
        "images/Characters/Atticus Indrid/Atticus_Eye3.webp"
    elif Atticus_State["eye"] == 4:
        "images/Characters/Atticus Indrid/Atticus_Eye4.webp"
    elif Atticus_State["eye"] == 5:
        "images/Characters/Atticus Indrid/Atticus_Eye5.webp"
    elif Atticus_State["eye"] == 6:
        "images/Characters/Atticus Indrid/Atticus_Eye6.webp"
    elif Atticus_State["eye"] == 7:
        "images/Characters/Atticus Indrid/Atticus_Eye7.webp"

    if Atticus_State["sleep"]:
        "images/Characters/Atticus Indrid/Atticus_Base_Sleep.webp"

    always:
        "atticusGlowA"
    always:
        "atticusGlowB"
