init offset = -1

init python:

    renpy.register_shader("ghostShader",
        variables="""
        varying float v_gradient;

        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform float u_shader_time;
        uniform float u_time_scale;

        uniform float u_intensity;
        uniform float u_base_bonus;
    """,
        vertex_300="""
        v_gradient = a_tex_coord.y;
        v_tex_coord = a_tex_coord;
    """,
        fragment_300="""
        float timeMult = sin(u_shader_time*u_time_scale)*(u_intensity) + u_base_bonus;
        float gradient = (1. - (pow(v_gradient,3.1))*timeMult);

        gl_FragColor*=gradient;
    """) # gl_FragColor = texture2D(tex0, v_tex_coord.xy,2.-2.*gradient)*gradient;


transform ghostShader_trans(timeScale=1.0,amp=0.4,base=0.6):
    shader "ghostShader"
    u_intensity amp
    u_base_bonus base
    u_shader_time 0.
    u_time_scale timeScale
    function advance_shader_time

image madhouse:
    xanchor 0.5
    zoom 0.23
    ycenter 0.715


    Flatten("madhouse_model")
    ghostShader_trans(0.5)


define Madhouse = Character("Madhouse", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27") #MADHOUSE
define NVL_Madhouse = Character("Madhouse", image = "MM", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27",kind=nvl)
define Madlas = Character("{swap=?At@Mad@0.53}{color=#ED2A82}Mad{/swap} {swap=house?@las???@0.67}{color=#3bec27}house{/swap}", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "2B10B")
define NVL_Mike = Character("Mike", image = "dmike", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27",kind=nvl)

define Mad = Character("Maddie", image = "MM", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27",kind=nvl)

image side dmike:
    matrixcolor ColorizeMatrix("#131c11","#3bec27")
    zoom 0.3
    yalign 1.0
    xalign 0.85
    "images/Characters/Minis/Mini_Dmike.webp"
    block:
        rotate 7
        pause 0.8
        rotate -7
        pause 0.8
        repeat

image side MM:
    matrixcolor ColorizeMatrix("#131c11","#3bec27")
    zoom 0.2
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_Madhouse.webp"
    block:
        yzoom 1.0
        pause 0.7
        yzoom 0.96
        pause 0.7
        repeat

image mmhat:
    zoom 0.23
    "images/Characters/Madhouse/MM_Hat.webp"

#Madhouse --------------------------------------------------
default MM_State = { "eyes": 4,
    "mouth" : 9,
    "body": 0,
    "armL": 0,
    "armR": 0,
    "hair": 0,
    "outfit": 0,
    "hat": True,
    "blush": False}

default MM_Default = { "eyes": 4,
    "mouth" : 9,
    "body": 0,
    "armL": 0,
    "armR": 0,
    "hair": 0,
    "outfit": 0,
    "hat": True,
    "blush": False}

image MM_Eyes_Neutral:
    "images/Characters/Madhouse/MM_Eye_Neutral.webp"
    choice:
        pause 5.0
    choice:
        pause 1.0
    choice:
        pause 3.0
    choice:
        pause 0.5
    "images/Characters/Madhouse/MM_Eye_Closed_Single.webp"
    pause 0.1
    repeat

image MM_Eyes_Dizzy:
    "images/Characters/Madhouse/MM_Eye_Dizzy.webp"

image MM_Eyes_Pensive:
    "images/Characters/Madhouse/MM_Eye_Pensive.webp"
    choice:
        pause 5.0
    choice:
        pause 1.0
    choice:
        pause 3.0
    choice:
        pause 0.5
    "images/Characters/Madhouse/MM_Eye_Closed_Single.webp"
    pause 0.1
    repeat



layeredimage madhouse_model:


    #Arms
    if MM_State["armL"] == 1:
        "images/Characters/Madhouse/MM_Arms_Left1.webp"
    elif MM_State["armL"] == 2:
        "images/Characters/Madhouse/MM_Arms_Left2.webp"

    #Body
    if MM_State["outfit"] != 1:
        "images/Characters/Madhouse/MM_Body.webp"

    if MM_State["body"] == 1:
        "images/Characters/Madhouse/MM_Belly.webp"

    if MM_State["armR"] == 1:
        "images/Characters/Madhouse/MM_Arms_Right1.webp"
    elif MM_State["armR"] == 2:
        "images/Characters/Madhouse/MM_Arms_Right2.webp"

    #Arms 2
    if MM_State["armL"] == 0 and MM_State["armR"] == 0:
        "images/Characters/Madhouse/MM_Arms_Up.webp"

    #Coat Sleve Left
    if MM_State["armL"] == 1:
        "images/Characters/Madhouse/MM_Coat_Sleeve1.webp"
    elif MM_State["armL"] == 2:
        "images/Characters/Madhouse/MM_Coat_Sleeve2.webp"

    #Coat
    if MM_State["armR"] == 0:
        "images/Characters/Madhouse/MM_Arms_Up.webp"
    elif MM_State["armR"] == 1:
        "images/Characters/Madhouse/MM_Coat_2.webp"
    elif MM_State["armR"] == 2:
        "images/Characters/Madhouse/MM_Coat_3.webp"
    elif MM_State["armR"] == 3:
        "images/Characters/Madhouse/MM_Coat_4.webp"

    #Invisible
    if MM_State["outfit"] == 1:
        "images/Characters/Madhouse/MM_Coat_Back.webp"

    #Hair
    if MM_State["hair"] == 0:
        "images/Characters/Madhouse/MM_Hair_1.webp"
    elif MM_State["hair"] == 1:
        "images/Characters/Madhouse/MM_Hair_2.webp"

    #Eye Shadow
    if MM_State["eyes"] != 0 and MM_State["hat"]:
        "images/Characters/Madhouse/MM_ShadowBig.webp"
    elif MM_State["outfit"] != 1 and MM_State["hat"]:
        "images/Characters/Madhouse/MM_ShadowSmall.webp"

    #Mouth
    always:
        ConditionSwitch(
            "MM_State['mouth'] <= 0", "images/Characters/Madhouse/MM_Mouth_Default.webp",
            "MM_State['mouth'] == 1", "images/Characters/Madhouse/MM_Mouth_Frown1.webp",
            "MM_State['mouth'] == 2", "images/Characters/Madhouse/MM_Mouth_Frown2.webp",
            "MM_State['mouth'] == 3", "images/Characters/Madhouse/MM_Mouth_Frown3.webp",
            "MM_State['mouth'] == 4", "images/Characters/Madhouse/MM_Mouth_Frown4.webp",
            "MM_State['mouth'] == 5", "images/Characters/Madhouse/MM_Mouth_Cat.webp",
            "MM_State['mouth'] == 6", "images/Characters/Madhouse/MM_Mouth_Grin.webp",
            "MM_State['mouth'] == 7", "images/Characters/Madhouse/MM_Mouth_Grin_Open.webp",
            "MM_State['mouth'] == 8", "images/Characters/Madhouse/MM_Mouth_Oh.webp",
            "MM_State['mouth'] == 9", "images/Characters/Madhouse/MM_Mouth_Smile.webp",
            "MM_State['mouth'] == 10", "images/Characters/Madhouse/MM_Mouth_Unamused.webp",
            "MM_State['mouth'] == 11", "images/Characters/Madhouse/MM_Mouth_11.webp",
            "MM_State['mouth'] >= 12", "images/Characters/Madhouse/MM_Mouth_12.webp")


    #Eyes

    if MM_State['eyes'] > 0: #and MM_State["hat"]:
        ConditionSwitch(
            "MM_State['eyes'] == 1", "images/Characters/Madhouse/MM_Eye_Closed.webp",
            "MM_State['eyes'] == 2", "images/Characters/Madhouse/MM_Eye_Closed_Single.webp",
            "MM_State['eyes'] == 3", "MM_Eyes_Dizzy",
            "MM_State['eyes'] == 4", "MM_Eyes_Neutral",
            "MM_State['eyes'] == 5", "MM_Eyes_Pensive",
            "MM_State['eyes'] == 6", "images/Characters/Madhouse/MM_Eye_Spotted.webp",
            "MM_State['eyes'] == 7", "images/Characters/Madhouse/Madhouse_Eye10.webp",
            "MM_State['eyes'] == 8", "images/Characters/Madhouse/Madhouse_Eye11.webp",
            "MM_State['eyes'] == 9", "images/Characters/Madhouse/Madhouse_Eye12.webp",
            "MM_State['eyes'] == 10", "images/Characters/Madhouse/Madhouse_Eye13.webp",
            "MM_State['eyes'] >= 11", "images/Characters/Madhouse/MM_Eye14.webp")



    #TOP ARMS
    if MM_State["armL"] == 3:
        "images/Characters/Madhouse/MM_Arms_Left3.webp"
    if MM_State["armR"] == 3:
        "images/Characters/Madhouse/MM_Arms_Right3.webp"

    #Blush
    if MM_State["blush"]:
        "images/Characters/Madhouse/MM_Body_Blush.webp"
    #Hat
    if MM_State["hat"]:
        "images/Characters/Madhouse/MM_Hat.webp"
    else:
        "images/Characters/Madhouse/MM_Hair_Base.webp"

image madhousetiny:
    xanchor 0.5
    alpha 0.8
    zoom 0.23
    ycenter 0.57
    "images/Characters/Madhouse/MM_Tiny.webp"

#Madlas --------------------------------------------------
default MD_State = { "eyes": -1,
    "mouth" : 2,
    "feelerL": 0,
    "feelerR": 0}

default MD_Default = { "eyes": -1,
    "mouth" : 2,
    "feelerL": 0,
    "feelerR": 0}

image MD_Body:
    "images/Characters/Madhouse/Madlas/MD_Body1.webp"
    choice:
        pause 2.5
    choice:
        pause 1.25
    choice:
        pause 3.0
    choice:
        pause 5.0

    "images/Characters/Madhouse/Madlas/MD_Body1.webp"
    choice:
        "images/Characters/Madhouse/Madlas/MD_Body2.webp"
        pause 0.15
        "images/Characters/Madhouse/Madlas/MD_Body3.webp"
        pause 0.15
    choice:
        "images/Characters/Madhouse/Madlas/MD_Body3.webp"
        pause 0.15
        "images/Characters/Madhouse/Madlas/MD_Body2.webp"
        pause 0.15

    repeat

layeredimage madlas:
    xanchor 0.5
    zoom 0.3
    ycenter 0.62
    always:
        "MD_Body"

    #feeler
    if MD_State["feelerL"] == 0:
        "images/Characters/Madhouse/Madlas/MD_Feeler_Left1.webp"
    elif MD_State["feelerL"] == 1:
        "images/Characters/Madhouse/Madlas/MD_Feeler_Left2.webp"

    if MD_State["feelerR"] == 0:
        "images/Characters/Madhouse/Madlas/MD_Feeler_Right1.webp"
    elif MD_State["feelerR"] == 1:
        "images/Characters/Madhouse/Madlas/MD_Feeler_Right2.webp"

    #mouth
    if MD_State["mouth"] == 0:
        "images/Characters/Madhouse/Madlas/MD_Mouth1.webp"
    elif MD_State["mouth"] == 1:
        "images/Characters/Madhouse/Madlas/MD_Mouth2.webp"
    elif MD_State["mouth"] == 2:
        "images/Characters/Madhouse/Madlas/MD_Mouth3.webp"
    elif MD_State["mouth"] == 3:
        "images/Characters/Madhouse/Madlas/MD_Mouth4.webp"

    #eyes
    if MD_State["eyes"] == 0:
        "images/Characters/Madhouse/Madlas/MD_Eye1.webp"
    elif MD_State["eyes"] == 1:
        "images/Characters/Madhouse/Madlas/MD_Eye2.webp"
    elif MD_State["eyes"] == 2:
        "images/Characters/Madhouse/Madlas/MD_Eye3.webp"
    elif MD_State["eyes"] == 3:
        "images/Characters/Madhouse/Madlas/MD_Eye4.webp"
    elif MD_State["eyes"] == 4:
        "images/Characters/Madhouse/Madlas/MD_Eye5.webp"
    elif MD_State["eyes"] == 5:
        "images/Characters/Madhouse/Madlas/MD_Eye6.webp"

layeredimage fakeAtlas:
    always:
        "images/Characters/Atlas/Atlas_Base.webp"
    always:
        "images/Characters/Atlas/Atlas_Feelers2.webp"
    always:
        "images/Characters/Atlas/Atlas_armL1.webp"
    always:
        "images/Characters/Atlas/Atlas_Shirt.webp"
    always:
        "images/Characters/Atlas/Atlas_armR1.webp"
    always:
        "images/Characters/Atlas/Atlas_Sleeve.webp"
    always:
        "images/Characters/Atlas/Atlas_EyeShadow2.webp"
    always:
        "images/Characters/Atlas/Atlas_Eye9.webp"

#Demon Maddie --------------------------------------------------
default MMD_State = { "mouth": 0,
    "eye": 0,
    "frenzy" : False,
    "hurt": False,
    "glitch": 0}

default MMD_Default = { "mouth": 0,
    "eye": 0,
    "frenzy" : False,
    "hurt": False,
    "glitch": 0}

image MMD_Glitch:
    alpha 1
    "images/Characters/Madhouse/Demon/MMD_Body1.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body2.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body3.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body4.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body1.webp"

image MMD_Glitch_Loop:
    alpha 1
    "images/Characters/Madhouse/Demon/MMD_Body1.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body2.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body3.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body4.webp"
    pause 0.15
    "images/Characters/Madhouse/Demon/MMD_Body1.webp"

    choice:
        pause 2.5
    choice:
        pause 1.25
    choice:
        pause 3.0
    choice:
        pause 5.0
    repeat

image MMD_Glitch_Blink:
    parallel:
        "images/Characters/Madhouse/Demon/MMD_Body1.webp"
        pause 0.15
        "images/Characters/Madhouse/Demon/MMD_Body2.webp"
        pause 0.15
        "images/Characters/Madhouse/Demon/MMD_Body3.webp"
        pause 0.15
        "images/Characters/Madhouse/Demon/MMD_Body4.webp"
        pause 0.15
        "images/Characters/Madhouse/Demon/MMD_Body1.webp"
    parallel:
        alpha 1
        pause 0.2
        alpha 0
        pause 0.2
        alpha 1
        pause 0.2
        alpha 0
        pause 0.2
        alpha 1
        pause 0.2
        alpha 0
        pause 0.2
        alpha 1

image MMD_BodyBlink:
    "images/Characters/Madhouse/Demon/MMD_Body1.webp"
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1

image MMD_EyeBlink:
    "images/Characters/Madhouse/Demon/MMD_Mouth_Pain.webp"
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1

image MMD_DroolBlink:
    "images/Characters/Madhouse/Demon/MMD_Drool_Pain.webp"
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1
    pause 0.2
    alpha 0
    pause 0.2
    alpha 1

image demon_madhouse:
    xanchor 0.5
    zoom 0.19
    ycenter 0.6
    Flatten("demon_madhouse_model")
    ghostShader_trans(0.5)

layeredimage demon_madhouse_model:

    #Body
    if (not MMD_State["hurt"]) and MMD_State["glitch"] == 0:
        "images/Characters/Madhouse/Demon/MMD_Body1.webp"
    elif (not MMD_State["hurt"]) and MMD_State["glitch"] == 1:
        "MMD_Glitch"
    elif (not MMD_State["hurt"]) and MMD_State["glitch"] == 2:
        "MMD_Glitch_Loop"
    elif MMD_State["hurt"] and MMD_State["glitch"] == 0:
        "MMD_BodyBlink"
    elif MMD_State["hurt"] and MMD_State["glitch"] == 1:
        "MMD_Glitch_Blink"

    if MMD_State["frenzy"] and MMD_State["mouth"] == 0 and not MMD_State["hurt"]:
        "images/Characters/Madhouse/Demon/MMD_Drool_Default.webp"

    if MMD_State["hurt"]:
        "MMD_EyeBlink"
    elif MMD_State["mouth"] == 1:
        "images/Characters/Madhouse/Demon/MMD_Mouth_Grin.webp"

    if MMD_State["frenzy"] and MMD_State["hurt"]:
        "images/Characters/Madhouse/Demon/MMD_Drool_Pain.webp"
    elif MMD_State["frenzy"] and MMD_State["mouth"] == 1:
        "images/Characters/Madhouse/Demon/MMD_Drool_Grin.webp"

    if MMD_State["eye"] == 1:
        "images/Characters/Madhouse/Demon/MMD_Eye.webp"

# Blobhouse ------------------------------------------------------
default BM_State = { "face": 0,
    "arms" : 0,
    "hat" : True}

default BM_Default = { "face": 0,
    "arms" : 0,
    "hat" : True}

image blobhouse:

    zoom 0.2
    ycenter 0.5
    xanchor 0.5
    Flatten("blobhouse_model")
    ghostShader_trans(0.5)

layeredimage blobhouse_model:

    always:
        ConditionSwitch(
            "BM_State['hat']", "images/Characters/Madhouse/Blob/BM_Base.webp",
            "True", "images/Characters/Madhouse/Blob/BM_Base_Alt.png")


    if BM_State['arms'] <= 0:
        "images/Characters/Madhouse/Blob/BM_Arms1.webp"

    if BM_State['face'] > 0:
        ConditionSwitch(
            "BM_State['face'] == 1", "images/Characters/Madhouse/Blob/BM_Face1.webp",
            "BM_State['face'] == 2", "images/Characters/Madhouse/Blob/BM_Face2.webp",
            "BM_State['face'] == 3", "images/Characters/Madhouse/Blob/BM_Face3.webp",
            "BM_State['face'] == 4", "images/Characters/Madhouse/Blob/BM_Face4.webp",
            "BM_State['face'] == 5", "images/Characters/Madhouse/Blob/BM_Face5.webp",
            "BM_State['face'] == 6", "images/Characters/Madhouse/Blob/BM_Face6.webp",
            "BM_State['face'] == 7", "images/Characters/Madhouse/Blob/BM_Face7.webp",
            "BM_State['face'] == 8", "images/Characters/Madhouse/Blob/BM_Face8.webp",
            "BM_State['face'] == 9", "images/Characters/Madhouse/Blob/BM_Face9.webp",
            "BM_State['face'] == 10", "images/Characters/Madhouse/Blob/BM_Face10.png",
            "BM_State['face'] == 11", "images/Characters/Madhouse/Blob/BM_Face11.png",
            "BM_State['face'] == 12", "images/Characters/Madhouse/Blob/BM_Face12.png",
            "BM_State['face'] == 13", "images/Characters/Madhouse/Blob/BM_Face13.png",
            "BM_State['face'] >= 14", "images/Characters/Madhouse/Blob/BM_Face14.png")

    if BM_State['arms'] >= 1:
        "images/Characters/Madhouse/Blob/BM_Arms2.webp"
