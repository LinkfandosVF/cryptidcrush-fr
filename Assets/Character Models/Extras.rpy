init offset = -1
# Character Name ---------------------------------------------------------------
default persistent.lex_narrator_unlocked = False
default narrColor = "#FFF"

init python:
    narrColor = "#FFF"
    if persistent.lex_narrator_unlocked:
        narrColor = "#70fffb"

define Narrator = Character("Narrator", callback = Bleep,ctc="end_of_msg", cb_id = "9A", who_color = narrColor) # NARRATOR
define NVL_Narrator = Character("Narrator", image = "narrator", callback = Bleep,ctc="end_of_msg", cb_id = "9A", who_color =  narrColor,kind=nvl)
define NVL_Text = Character("", image = "narrator", callback = Bleep,ctc="end_of_msg", cb_id = "9A", who_color =  narrColor,kind=nvl)

define Everyone = Character("Everyone", callback = Bleep,ctc="end_of_msg", cb_id = "1A", who_color = "#FFF")
image side narrator:
    zoom 0.2
    yalign 1.0
    xalign 0.8
    alpha 0
    "jamieplaceholder"

# Character Name ---------------------------------------------------------------
define Fern = Character("", image = "fern", callback = Bleep,ctc="end_of_msg", cb_id = "1A") #FERN
image fern:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.32
    yzoom 0.32
    ycenter 0.59
# Fridge WIP -------------------------------------------------------------------------
define fridge = Character("Fridge", image = "fridge", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#65cbe5") #Fridge
image fridge:
    xanchor 0.5
    ycenter 0.74
    zoom 0.26
    "images/Characters/TheExtras/fridge.png"
# Dewey WIP-----------------------------------------------------------------------------
define dewey = Character("Dewey", image = "dewey", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#Fea944") #Dewey
image dewey:
    xanchor 0.5
    ycenter 0.74
    zoom 0.31
    "images/Characters/TheExtras/dewey.png"

# Jodie WIP-----------------------------------------------------------------------------
define jodie = Character("Jodie", image = "jodie", callback = Bleep,ctc="end_of_msg", cb_id = "9D") #jodie
image jodie:
    xanchor 0.5
    ycenter 0.83
    zoom 0.32
    "images/Characters/TheExtras/jodie.png"


# HOPSKINVILLE GOBLIN---------------------------------------------------------------
define hobbes = Character("", image = "Hobskinville Goblin", callback = Bleep,ctc="end_of_msg", cb_id = "1A") #Hobs
image hobbes:
    zoom 0.25
    ycenter 0.9
    xanchor 0.5
    "images/Characters/TheExtras/Goblin.webp"
# LOBSTERMAN ---------------------------------------------------------------
define briggs = Character("Briggs", image = "Briggs", callback = Bleep,ctc="end_of_msg", cb_id = "11B") #Norman Briggs
image briggs:
    xanchor 0.5
    ycenter 0.6
    zoom 0.25
    "images/Characters/TheExtras/Lobsterman.webp"
# Sera ---------------------------------------------------------------
define sera = Character("", image = "Sera", callback = Bleep,ctc="end_of_msg", cb_id = "2D") #Sera
image sera:
    xanchor 0.5
    ycenter 0.7
    zoom 0.14
    "images/Characters/TheExtras/sera.webp"
# DUNGEON MAESTRO --------------------------------------------------------------
define Maestro = Character("{size=-5}Maestro", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#e83374")
define Neko = Character("Neko", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "8A", who_color = "#7f5fe8")

define slimie = Character("Slimie", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#1e85e4")
define slimie2 = Character("Slimie #2", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#1e85e4")
define slimier = Character("Slimier", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#113ae8")
define slimiest = Character("Slimiest", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#9e5ad2")
define slizzie = Character("Slizzie", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#0ecadd")
define Fslizzie = Character("F.H. Slizzie", image = "dm", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#dd3f2f")

image DMaestro:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/DM_Default.webp"

image DMaestro Awkward:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/DM_Awkward.webp"

image DMaestro Wink:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/DM_Wink.webp"

image DMaestro Cackle:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/DM_Cackle.webp"

image DMaestro Damaged:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/DM_Hurt.webp"
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1
    pause 0.1
    alpha 0
    pause 0.15
    alpha 1

image slimie:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/Slimie_Default.webp"

image slimie2:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/Slimie_Default.webp"

image slimier:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/Slimier_Default.webp"

image slimiest:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/Slimiest_Default.webp"

image slizzie:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/Slizzie_Default.webp"

image fhslizzie:
    xanchor 0.5
    yanchor 0.5
    xzoom 0.22
    yzoom 0.22
    ycenter 0.7
    "images/Characters/Dungeon Maestro/Battle/FlaminHotSlizzie_Default.webp"

# Goatma'am --------------------------------------------------------------------


image GM Default:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.7
    xzoom 0.2
    yzoom 0.2
    matrixcolor TintMatrix("#fadbb6")
    "images/Characters/Goatma'am/GM_Default.webp"

#Edith & Thursday

#Edith
#Bookmark
# image edith:
#     xanchor 0.5
#     yanchor 0.5
#     ycenter 0.8
#     xzoom 0.205
#     yzoom 0.205
#     "images/Characters/Edith/Edith_Default.webp"

define Domalomn = Character("Doma{color=#1dd91f}lomn{/color}", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ff36d9")

default domalomnEmote = 0
layeredimage domalomn_model:
    always:
        "domalomn"

    if domalomnEmote == 1:
        "domalomnEyesClosed"
    elif domalomnEmote == 2:
        "domalomn smile"
    else:
        "domalomnEyes"

    always:
        "domalomnGlow"

    always:
        "domalomnFireLeft"

    always:
        "domalomnFireRight"

image domalomn:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    "images/Characters/Dev Team/Domalomn.png"

image domalomn smile:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    "images/Characters/Dev Team/Domalomn_Smile.png"

image domalomnEyes:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    "images/Characters/Dev Team/Domalomn_Eyes.png"
    alpha 0.0
    choice:
        pause 5.0
    choice:
        pause 1.0
    choice:
        pause 3.0
    choice:
        pause 0.5
    alpha 1.0
    pause 0.15
    repeat

image domalomnEyesClosed:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    "images/Characters/Dev Team/Domalomn_Eyes.png"

image domalomnGlow:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    "images/Characters/Dev Team/Domalomn_Glow.png"
    alpha 0.3
    choice:
        ease 3.0 alpha 1.0
        pause 1.0
        ease 3.0 alpha 0.3
    choice:
        ease 2.0 alpha 1.0
        pause 1.0
        ease 2.0 alpha 0.3
    choice:
        ease 4.0 alpha 1.0
        pause 1.0
        ease 4.0 alpha 0.3
    repeat

image domalomnFireRight:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.6
    xzoom 0.19
    yzoom 0.19
    alpha 0.8
    "images/Characters/Dev Team/Domalomn_FireRight.png"
    ease 3.0 ycenter 0.5
    pause 0.5
    ease 3.0 ycenter 0.6
    repeat

image domalomnFireLeft:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.5
    xzoom 0.19
    yzoom 0.19
    alpha 0.8
    "images/Characters/Dev Team/Domalomn_FireLeft.png"
    ease 2.7 ycenter 0.6
    pause 0.5
    ease 2.7 ycenter 0.5
    repeat

define Ace = Character("Ace", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#ff8fea")

image ace:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.65
    zoom 0.4
    "images/Characters/Dev Team/Ace_Default.png"

image ace bean:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.5
    zoom 0.4
    "images/Characters/Dev Team/Ace_Bean.png"

define Mikey = Character("Mikey", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#f40f3f")

image mikey:
    xanchor 0.5
    yanchor 0.5
    ycenter 0.8
    zoom 0.18
    "images/Characters/Dev Team/Mikey_Default.png"
