init offset = -1
define Taro = Character("Taro", image = "taro", callback = Bleep,ctc="end_of_msg", cb_id = "4C", who_color = "#C064FF") #TARO (2D or 4C)
image side taro:
    xzoom 0.2
    yzoom 0.2

default Taro_State = { "eye": 0,
    "mouth" : 0,
    "pawL": 0,
    "pawR" : 0}

default BTaro_State = { "eye": 0,
    "mouth" : 0}

default Taro_Default = { "eye": 0,
    "mouth" : 0,
    "pawL": 0,
    "pawR" : 0}

default BTaro_Default = { "eye": 0,
    "mouth" : 0}

image taro_eyes1:
    "images/Characters/Taro/Taro_eye_Closed.webp"
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
    pause 0.15
    repeat

image taro_eyes2:
    "images/Characters/Taro/Taro_eye2.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/Taro_eye_Closed.webp"
    pause 0.15
    repeat

image taro_eyes3:
    "images/Characters/Taro/Taro_eye3.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/Taro_eye_Closed.webp"
    pause 0.15
    repeat

image taro_eyes4:
    "images/Characters/Taro/Taro_eye4.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/Taro_eye_Closed.webp"
    pause 0.15
    repeat

image taro_eyes5:
    "images/Characters/Taro/Taro_eye5.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/Taro_eye_Closed.webp"
    pause 0.15
    repeat

image taro:
    xanchor 0.5
    zoom 0.18
    ycenter 0.59

    
    Flatten("taro_model")
    ghostShader_trans(0.5)

layeredimage taro_model:
    
    #Base
    always:
        "images/Characters/Taro/Taro_Base.webp"

    #Right Paws
    if Taro_State["pawR"] == 0:
        "images/Characters/Taro/Taro_pawR1.webp"
    elif Taro_State["pawR"] == 1:
        "images/Characters/Taro/Taro_pawR2.webp"

    #Left Paws
    if Taro_State["pawL"] == 1:
        "images/Characters/Taro/Taro_pawL1.webp"

    #Mouth
    if Taro_State["mouth"] == 0:
        "images/Characters/Taro/Taro_mouth1.webp"
    elif Taro_State["mouth"] == 1:
        "images/Characters/Taro/Taro_mouth2.webp"
    elif Taro_State["mouth"] == 2:
        "images/Characters/Taro/Taro_mouth3.webp"
    elif Taro_State["mouth"] == 3:
        "images/Characters/Taro/Taro_mouth4.webp"
    elif Taro_State["mouth"] == 4:
        "images/Characters/Taro/Taro_mouth5.webp"

    if Taro_State["eye"] == 2:
        "images/Characters/Taro/Taro_eyeFrame.webp"
    #Eyes
    if Taro_State["eye"] == 0:
        "taro_eyes1"
    elif Taro_State["eye"] == 1:
        "taro_eyes2"
    elif Taro_State["eye"] == 2:
        "taro_eyes3"
    elif Taro_State["eye"] == 3:
        "taro_eyes4"
    elif Taro_State["eye"] == 4:
        "taro_eyes5"
    elif Taro_State["eye"] == 5:
        "images/Characters/Taro/Taro_eye_Closed.webp"

    #Ex Right Paw
    if Taro_State["pawR"] == 2:
        "images/Characters/Taro/Taro_pawR3.webp"

image btaro eye1:
    "images/Characters/Taro/BTaro_Eye1.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/BTaro_Eye_Closed.webp"
    pause 0.15
    repeat

image btaro eye2:
    "images/Characters/Taro/BTaro_Eye2.webp"
    choice:
        pause 4.0
    choice:
        pause 2.0
    choice:
        pause 3.0
    choice:
        pause 1.0

    "images/Characters/Taro/BTaro_Eye_Closed.webp"
    pause 0.15
    repeat

layeredimage tarobig:
    xanchor 0.5
    zoom 0.28
    ycenter 0.69
    #Base
    always:
        "images/Characters/Taro/BTaro_Base.webp"

    #Eyes
    if BTaro_State["eye"] == 0:
        "btaro eye1"
    elif BTaro_State["eye"] == 1:
        "btaro eye2"
    elif BTaro_State["eye"] == 2:
        "images/Characters/Taro/BTaro_Eye_Closed.webp"

    #Mouth
    if BTaro_State["mouth"] == 1:
        "images/Characters/Taro/BTaro_Mouth1.webp"
    elif BTaro_State["mouth"] == 2:
        "images/Characters/Taro/BTaro_Mouth2.webp"
