init offset = -1
default persistent.RobynSettings = [renpy.random.randint(0,1),renpy.random.randint(0,1),renpy.random.randint(0,1),renpy.random.randint(0,1),renpy.random.randint(0,2),renpy.random.randint(0,1),renpy.random.randint(0,1),renpy.random.randint(0,3),renpy.random.randint(0,3)]

define PCnameColors =     ["#1AE65A","#ff81aa","#639dff","#ff4545","#bb8cff","#b39275","#ebff87","#a3a4ff"]
define PCnameColorsDark = ["#236b41","#7d1335","#124499","#951b1b","#604982","#774f2d","#cfb133","#404181"]
define PCnameColor = PCnameColors[persistent.RobynSettings[8]]
define Robyn = Character("[PCname]", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor)

define NVL_Robyn = Character("[PCname]", image = "robyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)
define NVL_DRobyn = Character("[PCname]", image = "drobyn", callback = Bleep,ctc="end_of_msg", cb_id = "1C", who_color = PCnameColor,kind=nvl)


#0 = Green #1AE65A
#1 = Pink #ff81aa
#2 = Blue #639dff
#3 = Red #ff4747

# "#8162fb" "#6024af" old purple

image side robyn:
    matrixcolor ColorizeMatrix("#1b1b1b",PCnameColors[persistent.RobynSettings[8]])
    zoom 0.3
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_Robyn.png"
    block:
        yzoom 1.0 xzoom 1.0
        pause 0.8
        yzoom 0.9 xzoom 1.15
        pause 0.8
        repeat

layeredimage robyn_side:
    always:
        "images/Characters/Minis/Mini_Robyn.png"
    always:
        "srName"
image srName:
    xpos 310
    ypos 180
    yanchor 1.0
    rotate -7
    Text(PCname,size=50-len(PCname)*1.5)

image side drobyn:
    matrixcolor ColorizeMatrix("#1b1b1b",PCnameColors[persistent.RobynSettings[8]])
    zoom 0.2
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/Mini_DRobyn.webp"
    block:
        yzoom 1.0 xzoom 1.0
        pause 0.8
        yzoom 0.9 xzoom 1.15
        pause 0.8
        repeat


default persistent.RobynStats = [0,0,0,0,0,0,11]
default persistent.RobynCreated = False
default persistent.RobynPronouns = 2
default persistent.RobynName = ["Robyn","Hart"]
default Robyn_State = { "eyes": 0, #0-4
    "brow": 0, #0-3
    "mouth" : 0, #0-7
    "armR": 0, #0-1
    "armL": 0, #0-1
    "shirt": 0, #0-3
    "hair": 0, #0-1
    "msg": False, #Phone message
    "shoes": True,
    "coat": 1,
    "fPomf": False, #Front Hair Pomf
    "fHair": False, #Facial hair
    "glasses": False,
    "hairpin": False,
    "earring": False,
    "choker": False,
    "necklace": False,
    "beanie": False,
    "eyeliner": False}

default Robyn_State_Default = { "eyes": 0, #0-4
    "brow": 0, #0-3
    "mouth" : 0, #0-7
    "armR": 0, #0-1
    "armL": 0, #0-1
    "shirt": 0, #0-3
    "hair": 0, #0-1
    "msg": False, #Phone message
    "shoes": True,
    "coat": 1,
    "fPomf": False, #Front Hair Pomf
    "fHair": False, #Facial hair
    "glasses": False,
    "hairpin": False,
    "earring": False,
    "choker": False,
    "necklace": False,
    "beanie": False,
    "eyeliner": False}


#------------------------------------------------------------------ Model Emotes
image robyn default = "robyn"
layeredimage robyn:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        ConditionSwitch(
            "Robyn_State['eyes'] <= 0", "robyn default blink",
            "Robyn_State['eyes'] == 1", "robyn annoyed blink",
            "Robyn_State['eyes'] == 2", "robyn look blink",
            "Robyn_State['eyes'] == 3", "robyn_blink",
            "Robyn_State['eyes'] >= 4", "robyn up blink")

    #Brow
    always:
        ConditionSwitch(
            "Robyn_State['brow'] <= 0", "images/Characters/Robyn/Robyn_Eyebrow_Default.webp",
            "Robyn_State['brow'] == 1", "images/Characters/Robyn/Robyn_Eyebrow_Up.webp",
            "Robyn_State['brow'] == 2", "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp",
            "Robyn_State['brow'] >= 3", "images/Characters/Robyn/Robyn_Eyebrow_Angry.webp")

    #Mouth
    always:
        ConditionSwitch(
            "Robyn_State['mouth'] <= 0", "images/Characters/Robyn/Robyn_Mouth_Smile.webp",
            "Robyn_State['mouth'] == 1", "images/Characters/Robyn/Robyn_Mouth_Frown.webp",
            "Robyn_State['mouth'] == 2", "images/Characters/Robyn/Robyn_Mouth_Grimace.webp",
            "Robyn_State['mouth'] == 3", "images/Characters/Robyn/Robyn_Mouth_Hrmgh.webp",
            "Robyn_State['mouth'] == 4", "images/Characters/Robyn/Robyn_Mouth_Open.webp",
            "Robyn_State['mouth'] == 5", "images/Characters/Robyn/Robyn_Mouth_Pout.webp",
            "Robyn_State['mouth'] == 6", "images/Characters/Robyn/Robyn_Mouth_Smug.webp",
            "Robyn_State['mouth'] >= 7", "images/Characters/Robyn/Robyn_Mouth_TeethConcern.webp")

    always:
        "Robyn_Foreground"

layeredimage robyn pjs:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    if Robyn_State["hair"] == 0:
        "images/Characters/Robyn/Robyn_Pomf.webp"
    elif Robyn_State["hair"] == 1:
        "images/Characters/Robyn/Robyn_Pomf_Shortie.webp"

    #Base
    always:
        "images/Characters/Robyn/Robyn_Base.webp"

    #Eyes
    always:
        ConditionSwitch(
            "Robyn_State['eyes'] <= 0", "robyn default blink",
            "Robyn_State['eyes'] == 1", "robyn annoyed blink",
            "Robyn_State['eyes'] == 2", "robyn look blink",
            "Robyn_State['eyes'] == 3", "robyn_blink",
            "Robyn_State['eyes'] >= 4", "robyn up blink")

    #Brow
    always:
        ConditionSwitch(
            "Robyn_State['brow'] <= 0", "images/Characters/Robyn/Robyn_Eyebrow_Default.webp",
            "Robyn_State['brow'] == 1", "images/Characters/Robyn/Robyn_Eyebrow_Up.webp",
            "Robyn_State['brow'] == 2", "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp",
            "Robyn_State['brow'] >= 3", "images/Characters/Robyn/Robyn_Eyebrow_Angry.webp")

    #Mouth
    always:
        ConditionSwitch(
            "Robyn_State['mouth'] <= 0", "images/Characters/Robyn/Robyn_Mouth_Smile.webp",
            "Robyn_State['mouth'] == 1", "images/Characters/Robyn/Robyn_Mouth_Frown.webp",
            "Robyn_State['mouth'] == 2", "images/Characters/Robyn/Robyn_Mouth_Grimace.webp",
            "Robyn_State['mouth'] == 3", "images/Characters/Robyn/Robyn_Mouth_Hrmgh.webp",
            "Robyn_State['mouth'] == 4", "images/Characters/Robyn/Robyn_Mouth_Open.webp",
            "Robyn_State['mouth'] == 5", "images/Characters/Robyn/Robyn_Mouth_Pout.webp",
            "Robyn_State['mouth'] == 6", "images/Characters/Robyn/Robyn_Mouth_Smug.webp",
            "Robyn_State['mouth'] >= 7", "images/Characters/Robyn/Robyn_Mouth_TeethConcern.webp")

    always:
        "images/Characters/Robyn/Robyn_PJs.webp"

    #Etc
    if Robyn_State["fHair"]:
        "images/Characters/Robyn/Robyn_Etc_FacialHair.webp"


    if Robyn_State["fPomf"]:
        "images/Characters/Robyn/Robyn_Pomf_Front.webp"

# Basic Emotes
# Neutral   | Happy
# Annoyed   | Angry
# Sad       | Fear
# Surprised | Smug
# Thinking  | Sigh

# Todo Sigh
layeredimage robyn happy:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    always:
        "robyn look blink"

    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Up.webp"

    always:
        "images/Characters/Robyn/Robyn_Mouth_Smile.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn angry:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    always:
        "robyn look blink"

    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Angry.webp"

    always:
        "images/Characters/Robyn/Robyn_Mouth_Grimace.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn sad:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    always:
        "robyn annoyed blink"

    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp"

    always:
        "images/Characters/Robyn/Robyn_Mouth_Frown.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn annoyed:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    always:
        "robyn annoyed blink"

    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Angry.webp"

    always:
        "images/Characters/Robyn/Robyn_Mouth_Hrmgh.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn surprised:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        ConditionSwitch(
            "Robyn_State['eyes'] <= 0", "robyn default blink",
            "Robyn_State['eyes'] >= 1", "robyn look blink")

    #Brow
    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Up.webp"

    #Mouth
    always:
        "images/Characters/Robyn/Robyn_Mouth_Open.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn smug:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    always:
        "robyn annoyed blink"

    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp"

    always:
        "images/Characters/Robyn/Robyn_Mouth_Smile.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn neutral:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        "robyn look blink"

    #Brow
    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Default.webp"

    #Mouth
    always:
        "images/Characters/Robyn/Robyn_Mouth_Pout.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn thinking:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        "robyn up blink"

    #Brow
    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp"

    #Mouth
    always:
        "images/Characters/Robyn/Robyn_Mouth_Hrmgh.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn fear:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        "robyn default blink"

    #Brow
    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp"

    #Mouth
    always:
        "images/Characters/Robyn/Robyn_Mouth_Grimace.webp"

    always:
        "Robyn_Foreground"

layeredimage robyn sigh:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "Robyn_Background"

    #Eyes
    always:
        "robyn annoyed blink"

    #Brow
    always:
        "images/Characters/Robyn/Robyn_Eyebrow_Concern.webp"

    #Mouth
    always:
        "images/Characters/Robyn/Robyn_Mouth_Hrmgh.webp"

    always:
        "Robyn_Foreground"

#------------------------------------------------------------------ Model Pieces
layeredimage Robyn_Foreground:
    #R Arm
    if Robyn_State["coat"] == 1:
        ConditionSwitch(
            "Robyn_State['armR'] <= 0", "images/Characters/Robyn/Robyn_ArmR_Down.webp",
            "Robyn_State['armR'] >= 1", "images/Characters/Robyn/Robyn_ArmR_Phone.webp")

    #Phone
    if Robyn_State["msg"]:
        "images/Characters/Robyn/Robyn_Phone_Message.webp"

    #Shirt
    if Robyn_State["shirt"] == 0:
        "images/Characters/Robyn/Robyn_Shirt_UFO.webp"
    elif Robyn_State["shirt"] == 1:
        "images/Characters/Robyn/Robyn_Shirt_Spooky.webp"
    elif Robyn_State["shirt"] == 2:
        "images/Characters/Robyn/Robyn_Shirt_Robbie.webp"
    elif Robyn_State["shirt"] == 3:
        "images/Characters/Robyn/Robyn_Shirt_Mount.webp"

    #Coat
    if Robyn_State["armR"] == 0 and Robyn_State["coat"] == 1:
        "Robyn_Coat_Sleeves_ArmR_Down"

    if Robyn_State["coat"] == 1:
        "Robyn_Coat"

    if Robyn_State["armR"] == 1 and Robyn_State["coat"] == 1:
        "Robyn_Coat_Sleeves_Phone"


    #L Arm
    if Robyn_State["coat"] < 2:
        ConditionSwitch(
            "Robyn_State['armL'] <= 0", "images/Characters/Robyn/Robyn_ArmL_Down.webp",
            "Robyn_State['armL'] >= 1", "images/Characters/Robyn/Robyn_ArmL_Up.webp")

    if Robyn_State["coat"] == 1 and Robyn_State['armL'] <= 0:
        "Robyn_Coat_Sleeves_ArmL_Down"

    if Robyn_State["coat"] == 2:
        "images/Characters/Robyn/Robyn_PJs.webp"
    #Etc
    if Robyn_State["fHair"]:
        "images/Characters/Robyn/Robyn_Etc_FacialHair.webp"

    if Robyn_State["glasses"]:
        "images/Characters/Robyn/Robyn_Etc_Glasses.webp"

    if Robyn_State["hairpin"]:
        "images/Characters/Robyn/Robyn_Etc_Hairpin.webp"

    if Robyn_State["earring"]:
        "images/Characters/Robyn/Robyn_Etc_Earring.webp"

    if Robyn_State["choker"]:
        "images/Characters/Robyn/Robyn_Etc_Choker.webp"

    if Robyn_State["necklace"]:
        "images/Characters/Robyn/Robyn_Etc_Necklace.webp"

    if Robyn_State["beanie"]:
        "images/Characters/Robyn/Robyn_Etc_Beanie.webp"

    if Robyn_State["fPomf"]:
        "images/Characters/Robyn/Robyn_Pomf_Front.webp"

layeredimage Robyn_Background:
    #Base
    always:
        "images/Characters/Robyn/Robyn_Base.webp"

    #Hair pomf
    if Robyn_State["hair"] == 0 and Robyn_State["beanie"]:
        "images/Characters/Robyn/Robyn_Pomf_Beanie.webp"
    elif Robyn_State["hair"] == 0:
        "images/Characters/Robyn/Robyn_Pomf.webp"
    elif Robyn_State["hair"] == 1 and not Robyn_State["beanie"]:
        "images/Characters/Robyn/Robyn_Pomf_Shortie.webp"

    #Shoes
    if Robyn_State["shoes"]:
        "images/Characters/Robyn/Robyn_Shoes.webp"

#Robyn Eyes
layeredimage robyn_blink:
    always:
        "images/Characters/Robyn/Robyn_FaceMask.webp"
    always:
        "images/Characters/Robyn/Robyn_Eye_Closed.webp"

layeredimage robyn_annoyed_eyes:
    always:
        "images/Characters/Robyn/Robyn_FaceMask.webp"
    always:
        "images/Characters/Robyn/Robyn_Eyeframe_Annoyed.webp"
    always:
        "images/Characters/Robyn/Robyn_Eye_Annoyed.webp"
    if Robyn_State["eyeliner"]:
        "images/Characters/Robyn/Robyn_Base_Eyeliner.webp"

image robyn annoyed blink:
    "robyn_annoyed_eyes"
    choice:
        pause 5.0
    choice:
        pause 1.5
    choice:
        pause 3.0
    choice:
        pause 0.75

    "robyn_blink"
    pause 0.17
    repeat

layeredimage robyn default eyes:
    always:
        "images/Characters/Robyn/Robyn_Eye_Default.webp"
    if Robyn_State["eyeliner"]:
        "images/Characters/Robyn/Robyn_Base_Eyeliner.webp"

image robyn default blink:
    "robyn default eyes"
    choice:
        pause 5.0
    choice:
        pause 1.5
    choice:
        pause 3.0
    choice:
        pause 0.75

    "robyn_blink"
    pause 0.17
    repeat

layeredimage robyn look eyes:
    always:
        "images/Characters/Robyn/Robyn_Eye_Look.webp"
    if Robyn_State["eyeliner"]:
        "images/Characters/Robyn/Robyn_Base_Eyeliner.webp"

image robyn look blink:
    "robyn look eyes"
    choice:
        pause 5.0
    choice:
        pause 1.5
    choice:
        pause 3.0
    choice:
        pause 0.75

    "robyn_blink"
    pause 0.17
    repeat

layeredimage robyn up eyes:
    always:
        "images/Characters/Robyn/Robyn_Eye_Up.webp"

    if Robyn_State["eyeliner"]:
        "images/Characters/Robyn/Robyn_Base_Eyeliner.webp"

image robyn up blink:
    "robyn up eyes"
    choice:
        pause 5.0
    choice:
        pause 1.5
    choice:
        pause 3.0
    choice:
        pause 0.75

    "robyn_blink"
    pause 0.17
    repeat

#Robyn Coat
define robCoat = 0
image Robyn_Coat:
    ConditionSwitch(
        "robCoat == 0", "images/Characters/Robyn/Robyn_Coat.webp",
        "robCoat == 1", "Pink_Robyn_Coat",
        "robCoat == 2", "Blue_Robyn_Coat",
        "robCoat == 3", "Black_Robyn_Coat",
        "robCoat == 4", "Purple_Robyn_Coat",
        "robCoat == 5", "Dusty_Robyn_Coat",
        "robCoat == 6", "Toxic_Robyn_Coat",
        "robCoat == 7", "Navy_Robyn_Coat")


image Robyn_Coat_Sleeves_ArmL_Down:
    ConditionSwitch(
        "robCoat == 0", "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp",
        "robCoat == 1", "Pink_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 2", "Blue_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 3", "Black_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 4", "Purple_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 5", "Dusty_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 6", "Toxic_Robyn_Coat_Sleeves_ArmL_Down",
        "robCoat == 7", "Navy_Robyn_Coat_Sleeves_ArmL_Down")

image Robyn_Coat_Sleeves_ArmR_Down:
    ConditionSwitch(
        "robCoat == 0", "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp",
        "robCoat == 1", "Pink_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 2", "Blue_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 3", "Black_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 4", "Purple_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 5", "Dusty_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 6", "Toxic_Robyn_Coat_Sleeves_ArmR_Down",
        "robCoat == 7", "Navy_Robyn_Coat_Sleeves_ArmR_Down")

image Robyn_Coat_Sleeves_Phone:
    ConditionSwitch(
        "robCoat == 0", "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp",
        "robCoat == 1", "Pink_Robyn_Coat_Sleeves_Phone",
        "robCoat == 2", "Blue_Robyn_Coat_Sleeves_Phone",
        "robCoat == 3", "Black_Robyn_Coat_Sleeves_Phone",
        "robCoat == 4", "Purple_Robyn_Coat_Sleeves_Phone",
        "robCoat == 5", "Dusty_Robyn_Coat_Sleeves_Phone",
        "robCoat == 6", "Toxic_Robyn_Coat_Sleeves_Phone",
        "robCoat == 7", "Navy_Robyn_Coat_Sleeves_Phone")

#--------------------------------------------------------------- Alt Robyn Coats

#Black
image Black_Robyn_Coat:
    matrixcolor BrightnessMatrix(-0.15)*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Black_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor BrightnessMatrix(-0.15)*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Black_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor BrightnessMatrix(-0.15)*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Black_Robyn_Coat_Sleeves_Phone:
    matrixcolor BrightnessMatrix(-0.15)*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"

#Pink
image Pink_Robyn_Coat:
    matrixcolor HueMatrix(150.0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Pink_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor HueMatrix(150.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Pink_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor HueMatrix(150.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Pink_Robyn_Coat_Sleeves_Phone:
    matrixcolor HueMatrix(150.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"

#Blue
image Blue_Robyn_Coat:
    matrixcolor HueMatrix(90.0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Blue_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor HueMatrix(90.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Blue_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor HueMatrix(90.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Blue_Robyn_Coat_Sleeves_Phone:
    matrixcolor HueMatrix(90.0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"

#Purple
image Purple_Robyn_Coat:
    matrixcolor TintMatrix("#bb8cff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Purple_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor TintMatrix("#bb8cff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Purple_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor TintMatrix("#bb8cff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Purple_Robyn_Coat_Sleeves_Phone:
    matrixcolor TintMatrix("#bb8cff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"

#Dusty
image Dusty_Robyn_Coat:
    matrixcolor TintMatrix("#b39275")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Dusty_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor TintMatrix("#b39275")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Dusty_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor TintMatrix("#b39275")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Dusty_Robyn_Coat_Sleeves_Phone:
    matrixcolor TintMatrix("#b39275")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"

#Toxic
image Toxic_Robyn_Coat:
    matrixcolor TintMatrix("#ebff87")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Toxic_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor TintMatrix("#ebff87")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Toxic_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor TintMatrix("#ebff87")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Toxic_Robyn_Coat_Sleeves_Phone:
    matrixcolor TintMatrix("#ebff87")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"


#Navy
image Navy_Robyn_Coat:
    matrixcolor TintMatrix("#a3a4ff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat.webp"

image Navy_Robyn_Coat_Sleeves_ArmL_Down:
    matrixcolor TintMatrix("#a3a4ff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmL_Down.webp"

image Navy_Robyn_Coat_Sleeves_ArmR_Down:
    matrixcolor TintMatrix("#a3a4ff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_ArmR_Down.webp"

image Navy_Robyn_Coat_Sleeves_Phone:
    matrixcolor TintMatrix("#a3a4ff")*SaturationMatrix(0)
    "images/Characters/Robyn/Robyn_Coat_Sleeves_Phone.webp"


#------------------------------------------------------------------- Ghost Robyn
default D_RobynFace = 0
layeredimage dead_robyn:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82

    always:
        "images/Characters/Robyn/Dead/DRobyn_Base.webp"

    if D_RobynFace > 0:
        ConditionSwitch(
            "D_RobynFace == 1", "images/Characters/Robyn/Dead/DRobyn_Face1.webp",
            "D_RobynFace == 2", "images/Characters/Robyn/Dead/DRobyn_Face2.webp",
            "D_RobynFace >= 3", "images/Characters/Robyn/Dead/DRobyn_Face3.webp")

    if Robyn_State["fHair"]:
        "images/Characters/Robyn/Dead/DRobyn_FHair.webp"

    if Robyn_State["glasses"]:
        "images/Characters/Robyn/Dead/DRobyn_Glasses.webp"
#------------------------------------------------------------------- Sketch Robyn
image robyn sketch:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82
    "images/Characters/Robyn/robyn_sketch.webp"

#------------------------------------------------------------------- Moth Robyn
image robyn moth:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82
    "images/Characters/Robyn/robyn_moth.webp"
#------------------------------------------------------------------- Melt Robyn
image robyn melt:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82
    "images/Characters/Robyn/robyn_melt.webp"
#------------------------------------------------------------------- Doodle Robyn
image robyn doodle:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82
    "images/Characters/Robyn/robyn_doodle.webp"
#------------------------------------------------------------------- Doot Robyn
image robyn doot:
    xanchor 0.5
    zoom 0.17
    ycenter 0.82
    "images/Characters/Robyn/rooby_doot.webp"
