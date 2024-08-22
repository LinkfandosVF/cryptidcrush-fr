define Edward = Character("Edward", callback = Bleep,ctc="end_of_msg", cb_id = "7A", who_color = "#aad8dd")

default Edward_State = {
    "mouth" : 0,
    "eyes" : 0}


layeredimage edward:
    xanchor 0.5
    ycenter 0.76
    zoom 0.29

    always:
        "images/Characters/Edward/Ed_Base.webp"


    if Edward_State["eyes"] > 0:
        ConditionSwitch("Edward_State['eyes'] == 1", "images/Characters/Edward/Ed_Eye1.webp",
            "Edward_State['eyes'] == 2", "images/Characters/Edward/Ed_Eye2.webp",
            "Edward_State['eyes'] == 3", "images/Characters/Edward/Ed_Eye3.webp",
            "Edward_State['eyes'] >= 4", "images/Characters/Edward/Ed_Eye4.webp")

    if Edward_State["mouth"] > 0:
        ConditionSwitch("Edward_State['mouth'] == 1", "images/Characters/Edward/Ed_Mouth1.webp",
            "Edward_State['mouth'] == 2", "images/Characters/Edward/Ed_Mouth2.webp",
            "Edward_State['mouth'] == 3", "images/Characters/Edward/Ed_Mouth3.webp")
