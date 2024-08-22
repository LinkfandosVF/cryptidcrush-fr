define Lex = Character("{glitch=30}{color=#70fffb}Lex{/color}{/glitch}", callback = Bleep,ctc="end_of_msg", cb_id = "11B", who_color = "#aad8dd")

define NVL_Latlas = Character("{glitch=30}{color=#70fffb}Atlas?{/color}{/glitch}", image = "Latlas", callback = Bleep,ctc="end_of_msg", cb_id = "2b", who_color = "#aad8dd",kind=nvl)
define Latlas = Character("{glitch=30}{color=#70fffb}Atlas?{/color}{/glitch}", image = "Latlas", callback = Bleep,ctc="end_of_msg", cb_id = "2b", who_color = "#aad8dd")

image side Latlas:
    matrixcolor ColorizeMatrix("#1c1f4d","#aad8dd")
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

image lexgod Default:
    zoom 0.18
    yalign 1.2
    "images/Characters/Lex/Lex God Default.webp"


image Lex God Disgust:
    zoom 0.18
    yalign 1.2
    "images/Characters/Lex/Lex God Disgust.webp"

image Lex God Mouth:
    zoom 0.18
    yalign 1.2
    "images/Characters/Lex/Lex God Mouth.webp"

default Lex_State = { "armR": 0,
    "head": 0,
    "eyes": 0,
    "mouth": 0,
    "tongue": 0,
    "miniArmR": 1,
    "miniArmL": 1}

default Lex_Default = { "armR": 0,
    "head": 0,
    "eyes": 0,
    "mouth": 0,
    "tongue": 0,
    "miniArmR": 1,
    "miniArmL": 1}

layeredimage lex:
    xanchor 0.5
    zoom 0.31
    ycenter 0.65

    always:
        "images/Characters/Lex/Lex_WingL.webp"

    always:
        ConditionSwitch(
            "Lex_State['armR'] <= 0" , "images/Characters/Lex/Lex_ArmR1.webp",
            "Lex_State['armR'] >= 1" , "images/Characters/Lex/Lex_ArmR2.webp")

    always:
        "images/Characters/Lex/Lex_Body.webp"

    always:
        ConditionSwitch(
            "Lex_State['head'] <= 0" , "images/Characters/Lex/Lex_Head1.webp",
            "Lex_State['head'] >= 1" , "images/Characters/Lex/Lex_Head2.webp")

    if Lex_State['mouth'] > 0:
        ConditionSwitch(
            "Lex_State['mouth'] == 1" , "images/Characters/Lex/Lex_Mouth1.webp",
            "Lex_State['mouth'] == 2" , "images/Characters/Lex/Lex_Mouth2.webp",
            "Lex_State['mouth'] == 3" , "images/Characters/Lex/Lex_Mouth3.webp",
            "Lex_State['mouth'] == 4" , "images/Characters/Lex/Lex_Mouth4.webp",
            "Lex_State['mouth'] >= 5" , "images/Characters/Lex/Lex_Mouth5.png")

    if Lex_State['eyes'] > 0:
        "images/Characters/Lex/Lex_Eyes1.webp"

    if Lex_State['mouth'] == 2 and Lex_State['tongue'] > 0:
        ConditionSwitch(
            "Lex_State['tongue'] == 1" , "images/Characters/Lex/Lex_Mouth2Tongue1.webp",
            "Lex_State['tongue'] >= 2" , "images/Characters/Lex/Lex_Mouth2Tongue2.webp")

    if Lex_State['miniArmR'] > 0:
        ConditionSwitch(
            "Lex_State['miniArmR'] <= 1" , "images/Characters/Lex/Lex_DarmR1.webp",
            "Lex_State['miniArmR'] == 2" , "images/Characters/Lex/Lex_DArmR2.webp",
            "Lex_State['miniArmR'] >= 3" , "images/Characters/Lex/Lex_DArmR3.webp")

    elif Lex_State['miniArmL'] == 0:
        "images/Characters/Lex/Lex_DArm0.webp"

    if Lex_State['miniArmL'] > 0:
        ConditionSwitch(
            "Lex_State['miniArmR'] <= 1" , "images/Characters/Lex/Lex_DarmL1.webp",
            "Lex_State['miniArmR'] >= 2" , "images/Characters/Lex/Lex_DArmL2.webp")

    always:
        "images/Characters/Lex/Lex_ArmL1.webp"


image dupeLex:
    "lex"

image dupeLex default:
    "lex"

image dupe2Lex:
    "lex"

image dupe2Lex Atticus:
    "dupeLex Atticus"
    
image dupe2Lex Jamie:
    "dupeLex Jamie"

image dupe2Lex Gus:
    "dupeLex Gus"

image dupeLex Gus:
    xanchor 0.5
    zoom 0.22
    ycenter 0.675
    "images/Characters/Lex/Dupe_Lex_Gus.webp"

image dupeLex Jamie:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.7
    "images/Characters/Lex/Dupe_Lex_Jamie.webp"

image dupeLex Atticus:
    xanchor 0.5
    ycenter 0.7
    zoom 0.3
    "images/Characters/Lex/Dupe_Lex_Atticus.webp"

image dupeLex Taro:
    xanchor 0.5
    zoom 0.22
    ycenter 0.3
    "images/Characters/Lex/Dupe_Lex_Taro.webp"
