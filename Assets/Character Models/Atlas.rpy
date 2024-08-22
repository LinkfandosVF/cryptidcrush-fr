init offset = -1

define Atlas = Character("Atlas", callback = Bleep,ctc="end_of_msg", cb_id = "2B", who_color = "#ED2A82") # ATLAS

define P_Atlas = Character("Atlas?", callback = Bleep,ctc="end_of_msg", cb_id = "2B", who_color = "#3bec27")

define NVL_Atlas = Character("Atlas", image = "matlas", callback = Bleep,ctc="end_of_msg", cb_id = "2B", who_color = "#ED2A82",kind=nvl)

define NVL_DreamAtlas = Character("Atlas", image = "datlas", callback = Bleep,ctc="end_of_msg", cb_id = "2B", who_color = "#ED2A82",kind=nvl)

define NVL_Birdlas = Character("Atlas", image = "birdlas", callback = Bleep,ctc="end_of_msg", cb_id = "2B", who_color = "#ED2A82",kind=nvl)
#----------------- NVL
image side birdlas:
    #matrixcolor ColorizeMatrix("#1c1f4d","#ED2A82")
    zoom 0.2
    yalign 1.0
    xalign 0.8f
    "images/Characters/Minis/Dreamy_Birdlas.webp"
    block:
        yzoom 1.0
        pause 0.7
        yzoom 0.96
        pause 0.7
        repeat

image side datlas:
    matrixcolor ColorizeMatrix("#1c1f4d","#ED2A82")
    zoom 0.2
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_KidAtlas.webp"
    block:
        rotate 7
        pause 0.7
        rotate -7
        pause 0.7
        repeat

image side matlas:
    matrixcolor ColorizeMatrix("#1c1f4d","#ED2A82")
    zoom 0.12
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_Atlas.webp"

    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat

default Atlas_State = { "eye": 0,
    "eyeFrame" : 0,
    "armL": 0,
    "armR" : 0,
    "shirt": True,
    "tears": False,
    "sparkle": False,
    "phone": False,
    "feelers": 0,
    "blush": False}

default Atlas_Default = { "eye": 0,
    "eyeFrame" : 0,
    "armL": 0,
    "armR" : 0,
    "shirt": True,
    "tears": False,
    "sparkle": False,
    "phone": False,
    "feelers": 0,
    "blush": False}

#------------------------------------------------------------------ Model Emotes
layeredimage atlas:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    if (Atlas_State["eye"] > 4 and Atlas_State["eye"] < 8) or (Atlas_State['eye'] > 15):
        "images/Characters/Atlas/Atlas_Face_Cover.webp"
    elif (Atlas_State["eye"] > 7 and Atlas_State["eye"] < 12) or Atlas_State['eye'] == 15:
        "images/Characters/Atlas/Atlas_EyeShadow2.webp"

    always:
        ConditionSwitch(
            "Atlas_State['eye'] <= 0", "images/Characters/Atlas/Atlas_Eye1.webp",
            "Atlas_State['eye'] == 1", "images/Characters/Atlas/Atlas_Eye2.webp",
            "Atlas_State['eye'] == 2", "images/Characters/Atlas/Atlas_Eye3.webp",
            "Atlas_State['eye'] == 3", "images/Characters/Atlas/Atlas_Eye_Shocked.webp",
            "Atlas_State['eye'] == 4", "images/Characters/Atlas/Atlas_EyeSparkle.webp",
            "Atlas_State['eye'] == 5", "images/Characters/Atlas/Atlas_Eye4.webp",
            "Atlas_State['eye'] == 6", "images/Characters/Atlas/Atlas_Eye5.webp",
            "Atlas_State['eye'] == 7", "images/Characters/Atlas/Atlas_Eye6.webp",
            "Atlas_State['eye'] == 8", "images/Characters/Atlas/Atlas_Eye7.webp",
            "Atlas_State['eye'] == 9", "images/Characters/Atlas/Atlas_Eye8.webp",
            "Atlas_State['eye'] == 10", "images/Characters/Atlas/Atlas_Eye9.webp",
            "Atlas_State['eye'] == 11", "images/Characters/Atlas/Atlas_Eye10.webp",
            "Atlas_State['eye'] == 12", "images/Characters/Atlas/Atlas_Eye11.webp",
            "Atlas_State['eye'] == 13", "images/Characters/Atlas/Atlas_Eye12.webp",
            "Atlas_State['eye'] == 14","atlasflickeringeyes",
            "Atlas_State['eye'] == 15", "images/Characters/Atlas/Atlas_Eye13.webp",
            "Atlas_State['eye'] == 16", "images/Characters/Atlas/Atlas_Eye14.webp",
            "Atlas_State['eye'] == 17", "images/Characters/Atlas/Atlas_Eye15.webp",
            "Atlas_State['eye'] == 18", "images/Characters/Atlas/Atlas_Eye16.webp",
            "Atlas_State['eye'] == 19", "images/Characters/Atlas/Atlas_Eye17.webp",
            "Atlas_State['eye'] == 20", "images/Characters/Atlas/Atlas_EyeShadow2.webp",
            "Atlas_State['eye'] > 20", "images/Characters/Atlas/Atlas_Eye18.webp")

    #if (Atlas_State["eye"] > 9 and Atlas_State["eye"] < 12) or Atlas_State['eye'] == 15:
    #    "images/Characters/Atlas/Atlas_EX_Slime.webp"

    #Eye Frame
    if Atlas_State["eyeFrame"] >= 1:
        ConditionSwitch(
            "Atlas_State['eyeFrame'] == 1", "images/Characters/Atlas/Atlas_EyeShadow.webp",
            "Atlas_State['eyeFrame'] == 2", "images/Characters/Atlas/Atlas_Eye_Frame1.webp",
            "Atlas_State['eyeFrame'] == 3", "images/Characters/Atlas/Atlas_Eye_Frame2.webp",
            "Atlas_State['eyeFrame'] == 4", "images/Characters/Atlas/Atlas_Eye_Shocked.webp",
            "Atlas_State['eyeFrame'] >= 4", "images/Characters/Atlas/Atlas_Eye_Frame3.webp")

    #Tears
    if Atlas_State["tears"]:
        "images/Characters/Atlas/Atlas_Tears.webp"

    #Sparkle
    if Atlas_State["sparkle"]:
        "images/Characters/Atlas/Atlas_Sparkle.webp"

    always:
        "atlas_foreground"

image atlas default = "atlas"

# Basic Emotes
# Neutral   | Happy
# Annoyed   | Angry
# Sad       | Fear
# Surprised | Smug
# Thinking  | Sigh

layeredimage atlas neutral:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79

    always:
        "atlas_background"

    always:
        "images/Characters/Atlas/Atlas_Eye12.webp"

    always:
        "atlas_foreground"

layeredimage atlas neutral_b:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79

    always:
        "atlas_background"

    always:
        "images/Characters/Atlas/Atlas_Eye1.webp"

    always:
        "atlas_foreground"

layeredimage atlas happy:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye14.webp"

    #Sparkle
    if Atlas_State["sparkle"]:
        "images/Characters/Atlas/Atlas_Sparkle.webp"

    always:
        "atlas_foreground"

layeredimage atlas annoyed:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye16.webp"

    always:
        "atlas_foreground"

layeredimage atlas annoyed_b:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye17.webp"

    always:
        "atlas_foreground"

layeredimage atlas angry:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    always:
        "images/Characters/Atlas/Atlas_Eye12.webp"

    #Eye Frame
    always:
        "images/Characters/Atlas/Atlas_Eye_Frame1.webp"

    always:
        "atlas_foreground"


layeredimage atlas sad:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    always:
        "images/Characters/Atlas/Atlas_Eye1.webp"

    #Eye Frame
    always:
        "images/Characters/Atlas/Atlas_Eye_Frame2.webp"

    #Tears
    if Atlas_State["tears"]:
        "images/Characters/Atlas/Atlas_Tears.webp"

    always:
        "atlas_foreground"

layeredimage atlas fear:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    always:
        "images/Characters/Atlas/Atlas_Eye_Shocked.webp"

    #Eye Frame
    always:
        "images/Characters/Atlas/Atlas_EyeShadow.webp"

    always:
        "atlas_foreground"

layeredimage atlas surprised:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye6.webp"

    always:
        "atlas_foreground"

layeredimage atlas thinking:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye15.webp"

    always:
        "atlas_foreground"

layeredimage atlas smug:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_EyeShadow2.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye8.webp"

    #Sparkle
    if Atlas_State["sparkle"]:
        "images/Characters/Atlas/Atlas_Sparkle.webp"

    always:
        "atlas_foreground"

layeredimage atlas sigh:
    xanchor 0.5
    zoom 0.23
    ycenter 0.79
    always:
        "atlas_background"

    #Eyes
    always:
        "images/Characters/Atlas/Atlas_Face_Cover.webp"

    always:
        "images/Characters/Atlas/Atlas_Eye4.webp"

    always:
        "atlas_foreground"

#------------------------------------------------------------------ Model Pieces
layeredimage atlas_background:
    #Base
    always:
        "images/Characters/Atlas/Atlas_Base.webp"

    #Feelers
    always:
        ConditionSwitch(
            "Atlas_State['feelers'] <= 0", "images/Characters/Atlas/Atlas_Feelers1.webp",
            "Atlas_State['feelers'] == 1", "images/Characters/Atlas/Atlas_Feelers2.webp",
            "Atlas_State['feelers'] >= 2", "images/Characters/Atlas/Atlas_Feelers3.webp")

    #Left Arms
    if Atlas_State["armL"] < 2:
        ConditionSwitch(
            "Atlas_State['armL'] <= 0", "images/Characters/Atlas/Atlas_armL1.webp",
            "Atlas_State['armL'] >= 1", "images/Characters/Atlas/Atlas_armL2.webp")

    #Shirt
    if Atlas_State["shirt"]:
        "images/Characters/Atlas/Atlas_Shirt.webp"

    #Right Arms
    always:
        ConditionSwitch(
            "Atlas_State['armR'] <= 0", "images/Characters/Atlas/Atlas_armR1.webp",
            "Atlas_State['armR'] >= 1", "images/Characters/Atlas/Atlas_armR2.webp")

    #Sleeve
    if Atlas_State["shirt"]:
        "images/Characters/Atlas/Atlas_Sleeve.webp"

layeredimage atlas_foreground:
    #Phone
    if Atlas_State["phone"]:
        "images/Characters/Atlas/Atlas_Base_Phone.webp"

    #Thinky Arm
    if Atlas_State["armL"] >= 2:
        "images/Characters/Atlas/Atlas_armL3.webp"

    if Atlas_State["blush"]:
        "images/Characters/Atlas/Atlas_EX_Blush.webp"

image atlasflickeringeyes:
    "images/Characters/Atlas/Atlas_Eye1.webp"
    pause 0.2
    "images/Characters/Atlas/Atlas_Eye12.webp"
    pause 0.2
    repeat
image atlasArmR2 = "images/Characters/Atlas/Atlas_armR2.webp"
image atlasfallcg:
    zoom 0.19
    ycenter 0.755
    "images/Characters/Atlas/Atlas_Fall_CG.webp"

image atlas reset = "atlas"

image atlas fall:
    xanchor 0.5
    ycenter -0.5
    matrixtransform RotateMatrix(0.0, 0.0, -20.0)
    matrixcolor BrightnessMatrix(-1)
    blur 10

    "atlasfallcg"
    ease 0.5 ycenter 1.5 matrixtransform RotateMatrix(0.0, 0.0, -20.0)
    pause 0.2
    blur 0 matrixcolor BrightnessMatrix(0) matrixtransform RotateMatrix(0.0, 0.0, -40.0)
    "atlas"
    ease 0.6 ycenter 0.79 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
