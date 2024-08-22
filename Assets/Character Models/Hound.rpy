# Hound WIP ---------------------------------------------------------------
define Hound = Character("Hound", image = "hound", callback = Bleep,ctc="end_of_msg", cb_id = "1B", who_color = "#ea3c53") #Hound

default Hound_State = {
    "eyes": 0,
    "eyeFrame": 0,
    "uniform": True}

layeredimage hound:
    xanchor 0.5
    ycenter 0.83
    zoom 0.35

    if Hound_State['uniform']:
        "images/Characters/Hound/Hound_Uniform.png"
    else:
        "images/Characters/Hound/Hound_NoUniform.png"

    always:
        ConditionSwitch(
            "Hound_State['eyeFrame'] <= 0","images/Characters/Hound/Hound_EyeRed.png",
            "Hound_State['eyeFrame'] >= 1", "images/Characters/Hound/Hound_EyeGreen.png")

    if Hound_State['eyes'] > 0:
        ConditionSwitch(
            "Hound_State['eyes'] == 1", "images/Characters/Hound/Hound_Eye1.png",
            "Hound_State['eyes'] == 2", "images/Characters/Hound/Hound_Eye2.png",
            "Hound_State['eyes'] == 3", "images/Characters/Hound/Hound_Eye3.png",
            "Hound_State['eyes'] >= 4", "images/Characters/Hound/Hound_Eye4.png")
