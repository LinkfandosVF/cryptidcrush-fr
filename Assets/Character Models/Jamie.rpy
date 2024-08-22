init offset = -1

define Jamie = Character("Jamie", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#3AE9F6") #JAMIE
define NVL_Jamie = Character("Jamie", image = "jamie", callback = Bleep,ctc="end_of_msg", cb_id = "11A", who_color = "#3AE9F6",kind=nvl)

image side jamie:
    matrixcolor ColorizeMatrix("#0f2a18","#3AE9F6")
    zoom 0.28
    anchor (0.5,1.0)
    pos (0.77,1.0)
    "images/Characters/Minis/Mini_Jamie.webp"
    block:
        yzoom 1
        pause 1
        yzoom 0.9
        pause 0.8
        repeat

default Jamie_State = { "eye": 0,
    "brow": 0,
    "mouth" : 0,
    "armL": 0,
    "armR" : 0,
    "pants": True,
    "rings": True,
    "alFace" : False,
    "blush": False,
    "sweat": False,
    "fire": False,
    "r3Fire": False,
    "steam": False,
    "hurt": False,
    "wispEyes": 0}

default Jamie_Default = { "eye": 0,
    "brow": 0,
    "mouth" : 0,
    "armL": 0,
    "armR" : 0,
    "pants": True,
    "rings": True,
    "alFace" : False,
    "blush": False,
    "sweat": False,
    "fire": False,
    "r3Fire": False,
    "steam": False,
    "hurt": False,
    "wispEyes": 0}

#------------------------------------------------------------------ Model Emotes
image jamie default = "jamie"
layeredimage jamie:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        ConditionSwitch(
            "Jamie_State['eye'] <= 0", "images/Characters/Jamie/Jamie_Eye1.webp",
            "Jamie_State['eye'] == 1", "images/Characters/Jamie/Jamie_Eye2.webp",
            "Jamie_State['eye'] == 2", "images/Characters/Jamie/Jamie_Eye3.webp",
            "Jamie_State['eye'] == 3", "images/Characters/Jamie/Jamie_Eye4.webp",
            "Jamie_State['eye'] == 4", "images/Characters/Jamie/Jamie_Eye5.webp",
            "Jamie_State['eye'] == 5", "images/Characters/Jamie/Jamie_Eye6.webp",
            "Jamie_State['eye'] == 6", "images/Characters/Jamie/Jamie_Eye7.webp",
            "Jamie_State['eye'] == 7", "images/Characters/Jamie/Jamie_Eye8.webp",
            "Jamie_State['eye'] >= 8", "images/Characters/Jamie/Jamie_Eye9.webp")

    #Brow
    if Jamie_State["eye"] !=4:
        ConditionSwitch(
            "Jamie_State['brow'] == 0", "images/Characters/Jamie/Jamie_Brow1.webp",
            "Jamie_State['brow'] == 1", "images/Characters/Jamie/Jamie_Brow2.webp",
            "Jamie_State['brow'] == 2", "images/Characters/Jamie/Jamie_Brow3.webp",
            "Jamie_State['brow'] >= 3", "images/Characters/Jamie/Jamie_Brow4.webp")

    #EyeGlow
    if Jamie_State["eye"] == 5:
        "jamieGlow eyes2"

    #mouth
    if Jamie_State["mouth"] >= 1:
        ConditionSwitch(
            "Jamie_State['mouth'] == 1", "images/Characters/Jamie/Jamie_Mouth1.webp",
            "Jamie_State['mouth'] == 2", "images/Characters/Jamie/Jamie_Mouth2.webp",
            "Jamie_State['mouth'] == 3", "images/Characters/Jamie/Jamie_Mouth3.webp",
            "Jamie_State['mouth'] >= 4", "images/Characters/Jamie/Jamie_Mouth4.webp")

    always:
        "jamie_arms"

    if Jamie_State['mouth'] == 3:
        "images/Characters/Jamie/Jamie_Mouth3.webp"
    elif Jamie_State['mouth'] == 1:
        "images/Characters/Jamie/Jamie_Mouth1.webp"

    always:
        "jamie_arms2"

    if Jamie_State["alFace"]:
        "images/Characters/Jamie/Jamie_EXFace1.webp"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    if Jamie_State["sweat"]:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    always:
        "jamie_foreground"

# Basic Emotes
# Neutral   | Happy
# Annoyed   | Angry
# Sad       | Fear
# Surprised | Smug
# Thinking  | Sigh

layeredimage jamie neutral:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye4.webp"


    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow1.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

layeredimage jamie happy:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye3.webp"


    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow3.webp"


    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth2.webp"


    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    always:
        "jamie_foreground"

layeredimage jamie annoyed:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow1.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    always:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    always:
        "jamie_foreground"

layeredimage jamie angry:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye8.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth1.webp"

    always:
        "jamie_arms"

    always:
        "images/Characters/Jamie/Jamie_Mouth1.webp"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

layeredimage jamie sad:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye1.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow4.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

layeredimage jamie fear:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye5.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    #Sweat
    always:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    always:
        "jamie_foreground"

layeredimage jamie surprised:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    always:
        "images/Characters/Jamie/Jamie_EXFace1.webp"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    if Jamie_State["sweat"]:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    always:
        "jamie_foreground"

layeredimage jamie smug:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye3.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth3.webp"

    always:
        "jamie_arms"

    always:
        "images/Characters/Jamie/Jamie_Mouth3.webp"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

layeredimage jamie thinking:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow3.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

layeredimage jamie sigh:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23

    always:
        "jamie_background"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow4.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    always:
        "jamie_arms"

    always:
        "jamie_arms2"

    always:
        "jamie_foreground"

# -------------------------------------------------- CAFE
layeredimage jamie cafe:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"


    #Eyes
    always:
        ConditionSwitch(
            "Jamie_State['eye'] <= 0", "images/Characters/Jamie/Jamie_Eye1.webp",
            "Jamie_State['eye'] == 1", "images/Characters/Jamie/Jamie_Eye2.webp",
            "Jamie_State['eye'] == 2", "images/Characters/Jamie/Jamie_Eye3.webp",
            "Jamie_State['eye'] == 3", "images/Characters/Jamie/Jamie_Eye4.webp",
            "Jamie_State['eye'] == 4", "images/Characters/Jamie/Jamie_Eye5.webp",
            "Jamie_State['eye'] == 5", "images/Characters/Jamie/Jamie_Eye6.webp",
            "Jamie_State['eye'] == 6", "images/Characters/Jamie/Jamie_Eye7.webp",
            "Jamie_State['eye'] == 7", "images/Characters/Jamie/Jamie_Eye8.webp",
            "Jamie_State['eye'] >= 8", "images/Characters/Jamie/Jamie_Eye9.webp")

    #Brow
    if Jamie_State["eye"] !=4:
        ConditionSwitch(
            "Jamie_State['brow'] == 0", "images/Characters/Jamie/Jamie_Brow1.webp",
            "Jamie_State['brow'] == 1", "images/Characters/Jamie/Jamie_Brow2.webp",
            "Jamie_State['brow'] == 2", "images/Characters/Jamie/Jamie_Brow3.webp",
            "Jamie_State['brow'] >= 3", "images/Characters/Jamie/Jamie_Brow4.webp")


    #EyeGlow
    if Jamie_State["eye"] == 5:
        "jamieGlow eyes2"

    #mouth
    if Jamie_State["mouth"] >= 1:
        ConditionSwitch(
            "Jamie_State['mouth'] == 1", "images/Characters/Jamie/Jamie_Mouth1.webp",
            "Jamie_State['mouth'] == 2", "images/Characters/Jamie/Jamie_Mouth2.webp",
            "Jamie_State['mouth'] == 3", "images/Characters/Jamie/Jamie_Mouth3.webp",
            "Jamie_State['mouth'] >= 4", "images/Characters/Jamie/Jamie_Mouth4.webp")

    if Jamie_State["alFace"]:
        "images/Characters/Jamie/Jamie_EXFace1.webp"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    if Jamie_State["sweat"]:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

image jamie cafe default = "jamie cafe"

layeredimage jamie cafe neutral:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye4.webp"


    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow1.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe happy:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye3.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow3.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth2.webp"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe annoyed:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"


    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow1.webp"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    always:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe angry:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye8.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth1.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe sad:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye1.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow4.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe fear:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye5.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    #Sweat
    always:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe surprised:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    always:
        "images/Characters/Jamie/Jamie_EXFace1.webp"

    #Steam
    if Jamie_State["steam"]:
        "images/Characters/Jamie/Jamie_Base_Steam.webp"

    #Sweat
    if Jamie_State["sweat"]:
        "images/Characters/Jamie/Jamie_Base_Sweat.webp"

    #Blush
    if Jamie_State["blush"]:
        "images/Characters/Jamie/Jamie_Base_Blush.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe smug:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye3.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth3.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe thinking:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow3.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

layeredimage jamie cafe sigh:
    xanchor 0.5
    ycenter 0.65
    zoom 0.23
    always:
        "images/Characters/Jamie/Jamie_Base_Cafe.webp"

    #Eyes
    always:
        "images/Characters/Jamie/Jamie_Eye2.webp"

    #Brow
    always:
        "images/Characters/Jamie/Jamie_Brow4.webp"

    #mouth
    always:
        "images/Characters/Jamie/Jamie_Mouth4.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

#------------------------------------------------------------------ Model Pieces
image jamieGlow horn:
    alpha 1.0
    "images/Characters/Jamie/Jamie_Horns_Glow.webp"
    ease 2.0 alpha 0.8
    ease 2.0 alpha 1.0
    repeat

image jamieGlow wisp:
    alpha 1.0
    "images/Characters/Jamie/Jamie_Wisp_Base_Glow.webp"
    ease 2.0 alpha 0.2
    ease 2.0 alpha 1.0
    repeat

image jamieGlow eyes:
    "images/Characters/Jamie/Jamie_Eye_Glow.webp"
    choice:
        ease 3.0 alpha 0.4
        pause 3.0
        ease 3.0 alpha 0.9
    choice:
        ease 4.0 alpha 0.4
        pause 4.0
        ease 4.0 alpha 0.9
    choice:
        ease 5.0 alpha 0.4
        pause 5.0
        ease 5.0 alpha 0.9

    pause 2.0
    repeat

image jamieGlow eyes2:
    "images/Characters/Jamie/Jamie_Eye_Glow.webp"
    choice:
        ease 3.0 alpha 0.6
        pause 3.0
        ease 3.0 alpha 1.0
    choice:
        ease 4.0 alpha 0.6
        pause 4.0
        ease 4.0 alpha 1.0
    choice:
        ease 5.0 alpha 0.6
        pause 5.0
        ease 5.0 alpha 1.0

    pause 2.0
    repeat

layeredimage wispbase:
    always:
        "images/Characters/Jamie/Jamie_Wisp_Base.webp"

    always:
        "jamieGlow wisp"
    always:
        "jamieGlow wisp"

    always:
        ConditionSwitch(
            "Jamie_State['wispEyes'] <= 0", "images/Characters/Jamie/Jamie_Wisp_Eye1.webp",
            "Jamie_State['wispEyes'] == 1", "images/Characters/Jamie/Jamie_Wisp_Eye1_Closed.webp",
            "Jamie_State['wispEyes'] == 2", "images/Characters/Jamie/Jamie_Wisp_Eye2.webp",
            "Jamie_State['wispEyes'] >= 3", "images/Characters/Jamie/Jamie_Wisp_Eye2_Closed.webp")

image jamieWisp:
    "wispbase"
    block:
        choice:
            ease 2.5 yoffset -25
            ease 2.5 yoffset 0
        choice:
            ease 2.0 yoffset -25
            ease 2.0 yoffset 0
        choice:
            ease 1.5 yoffset -25
            ease 1.5 yoffset 0
        repeat

image jamieTail:
    yoffset -180
    xoffset 10
    zoom 1.0
    "images/Characters/Jamie/Jamie_Base_Tail.webp"

image jamiearm = "images/Characters/Jamie/Jamie_ArmR5.webp"

layeredimage jamie_background:
    #Base
    always:
        "jamieTail"

    always:
        "images/Characters/Jamie/Jamie_Base.webp"

    #Pants
    if Jamie_State["pants"]:
        "images/Characters/Jamie/Jamie_Pants1.webp"

layeredimage jamie_arms:
    #Left Arm
    always:
        "images/Characters/Jamie/Jamie_ArmL1.webp"

    #Right Arms
    if Jamie_State['armR'] < 4:
        ConditionSwitch("Jamie_State['armR'] <= 0", "images/Characters/Jamie/Jamie_ArmR1.webp",
        "Jamie_State['armR'] == 1", "images/Characters/Jamie/Jamie_ArmR2.webp",
        "Jamie_State['armR'] == 2", "images/Characters/Jamie/Jamie_ArmR3.webp",
        "Jamie_State['armR'] == 3", "images/Characters/Jamie/Jamie_ArmR4.webp")

    #Chain
    always:
        "images/Characters/Jamie/Jamie_EX_Chain.webp"

    #Jacket
    if Jamie_State["armR"] == 3:
        "images/Characters/Jamie/Jamie_Jacket1_ArmR4.webp"
    elif Jamie_State["armR"] == 1:
        "images/Characters/Jamie/Jamie_Jacket1_ArmR2.webp"
    else:
        "images/Characters/Jamie/Jamie_Jacket1.webp"

layeredimage jamie_arms2:
    if Jamie_State['armR'] >= 4:
        "images/Characters/Jamie/Jamie_ArmR5.webp"

    #Arm fire
    if Jamie_State["fire"]:
        "images/Characters/Jamie/Jamie_Base_Fire.webp"

    if Jamie_State["r3Fire"]:
        "images/Characters/Jamie/Jamie_ArmR3_Fire.webp"

    #Al face (Note: You'll want to turn off eyebrows for this. set it to like -1 or something)

layeredimage jamie_foreground:
    #Rings
    if Jamie_State["rings"]:
        "images/Characters/Jamie/Jamie_Base_Rings.webp"

    #Rings
    if Jamie_State["hurt"]:
        "images/Characters/Jamie/Jamie_EX_NoseBleed.webp"

    #Hornglow
    always:
        "jamieGlow horn"

    #Wisp
    always:
        "jamieWisp"

image jamieplaceholder:
    matrixcolor ColorizeMatrix("#000000","#ffffff")
    "images/Characters/Jamie/Jamie_Placeholder.webp"
