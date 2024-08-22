define Robert = Character("Robbie", callback = Bleep,ctc="end_of_msg", cb_id = "6A", who_color = "#ea3c53")

default Robbie_State = { "eye": 0,
    "armR" : 0,
    "mouth": 0}

default Robbie_Default = { "eye": 0,
    "armR" : 0,
    "mouth": 0}

#ROBBIE
layeredimage robbie:
    xanchor 0.5
    ycenter 0.74
    zoom 0.23

    #Base
    always:
        "images/Characters/Robbie/robbie_base.webp"

    #arm
    always:
        ConditionSwitch(
            "Robbie_State['armR'] <= 0", "images/Characters/Robbie/robbie_armr2.webp",
            "Robbie_State['armR'] >= 1", "images/Characters/Robbie/robbie_armr1.webp")
    #Eyes
    always:
        ConditionSwitch(
            "Robbie_State['eye'] <= 0", "images/Characters/Robbie/robbie_eye1.webp",
            "Robbie_State['eye'] == 1", "images/Characters/Robbie/robbie_eye2.webp",
            "Robbie_State['eye'] == 2", "images/Characters/Robbie/robbie_eye3.webp",
            "Robbie_State['eye'] == 3", "images/Characters/Robbie/robbie_eye4.webp",
            "Robbie_State['eye'] == 4", "images/Characters/Robbie/robbie_eye5.webp",
            "Robbie_State['eye'] == 5", "images/Characters/Robbie/robbie_eye6.webp",
            "Robbie_State['eye'] == 6", "images/Characters/Robbie/robbie_eye7.webp",
            "Robbie_State['eye'] == 7", "images/Characters/Robbie/robbie_eye8.webp",
            "Robbie_State['eye'] >= 8", "images/Characters/Robbie/robbie_eye9.webp")

    #Mouth
    if Robbie_State['mouth'] > 0:
        ConditionSwitch(
            "Robbie_State['mouth'] == 1", "images/Characters/Robbie/robbie_mouth1.webp",
            "Robbie_State['mouth'] == 2", "images/Characters/Robbie/robbie_mouth2.webp",
            "Robbie_State['mouth'] == 3", "images/Characters/Robbie/robbie_mouth3.webp",
            "Robbie_State['mouth'] == 4", "images/Characters/Robbie/robbie_mouth4.webp",
            "Robbie_State['mouth'] == 5", "images/Characters/Robbie/robbie_mouth5.webp",
            "Robbie_State['mouth'] == 6", "images/Characters/Robbie/robbie_mouth6.webp",
            "Robbie_State['mouth'] >= 7", "images/Characters/Robbie/robbie_mouth7.webp")
