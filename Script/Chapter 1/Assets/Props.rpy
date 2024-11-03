init offset = -1

image CG Pet Taro:
    zoom 0.3
    ycenter 0.35
    "images/CGs/Chapter 1/pettaro.webp"

image bigAssStick:
    xzoom 0.3
    yzoom 0.5
    "images/Props/Stick.webp"

image CG August Dead:
    yalign 1.0
    yoffset 160
    zoom 0.28
    "images/CGs/Chapter 1/August Dead CG.webp"

image AugustTail:
    yalign 1.0
    yoffset 130
    matrixtransform RotateMatrix(0,0,-60)
    zoom 0.2
    "images/CGs/Chapter 1/August Tail CG.webp"

image WereGusWakes2:
    ycenter 0.5
    xcenter 0.5
    zoom 0.36
    "images/CGs/Chapter 1/august_snap.webp"

image WereGusWakes1:
    ycenter 0.5
    xcenter 0.5
    zoom 0.36
    "images/CGs/Chapter 1/august_snap2.webp"

image WereGusWakes3:
    ycenter 0.4
    xcenter 0.5
    zoom 1.4
    "images/CGs/WereGusWakes_3.webp"

transform galaxyFright:
    matrixcolor HueMatrix(0)
    choice:
        ease 18.0 matrixcolor HueMatrix(360)
    choice:
        ease 18.0 matrixcolor HueMatrix(-360)
    repeat

image BGCG atTheTableFright:
    "images/BGs/Chapter 1/Wor_Visor.webp"
    xcenter 0.5
    ycenter 0.47

transform floatingVisor:
    ease 1.0 ycenter 0.47 rotate 1440 yzoom 1.0 xzoom 1.0
    choice:
        ease 4 ycenter 0.53
        pause 0.2
        ease 4 ycenter 0.47
        pause 0.2
        repeat

transform enterVisor:
    xzoom 0
    yzoom 0

    ease 5.0 xzoom 1 yzoom 1 rotate 1440

    choice:
        ease 4 ycenter 0.53
        pause 0.2
        ease 4 ycenter 0.47
        pause 0.2
        repeat

image CGShade:
    Solid("#000000")
    alpha 0
    ease 0.75 alpha 0.35

    on show:
        alpha 0
        ease 0.75 alpha 0.35
    on hide:
        alpha 0.35
        ease 0.75 alpha 0

image CG Robyn_Card:
    "images/CGs/Chapter 1/Robyn Letter.webp"
    xcenter 0.5
    ycenter 0.32
    zoom 0.23
    on show:
        yoffset -700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset -700

image CG Jamie_Card:
    "images/CGs/Chapter 1/Jamie Letter.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.2
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG Madhouse_Snooze1:
    "images/CGs/Chapter 1/madhousezzz.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.23

image CG Madhouse_Snooze2:
    "images/CGs/Chapter 1/madhousezzzsmile.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.23

image CG Howler:
    zoom 0.3
    "images/CGs/Chapter 1/howlernewspaper.webp"

image CG Hocus_Call:
    zoom 0.7
    yanchor 1.0
    ypos 0.9
    xcenter 0.7
    "images/CGs/Chapter 1/hoscus_phonecall.webp"
    ease 3.0 ypos 1.3
    ease 4.0 xpos 0.5

image CG Tessie Peek:
    xcenter 0.5
    ycenter 0.5
    zoom 0.41
    "images/CGs/Chapter 1/tessiepeek_visit1.webp"

image CG Tessie Peek2:
    xcenter 0.5
    ycenter 0.5
    zoom 0.41
    "images/CGs/Chapter 1/tessiepeek_visit2.webp"

#dream
image CG Dream2:
    zoom 0.432
    ycenter 0.5
    xalign 0.0
    "images/CGs/Chapter 1/dream2-alien.webp"

image CG Dream3:
    zoom 0.45
    yanchor 1.0
    ypos 0.7
    xcenter 0.5
    "images/CGs/Chapter 1/dream3-intruder.webp"
    ease 4.0 ypos 1.0

image CG Dream4:
    zoom 0.5
    xcenter 0.5
    ycenter 0.5
    "images/CGs/Chapter 1/dream4-fear.webp"
    ease 7.0 zoom 1.5 yoffset 500 xoffset -1100

image tCG Dream4:
    xcenter 0.5
    ycenter 0.5
    zoom 1.5
    yoffset 500
    xoffset -1100

    "images/CGs/Chapter 1/dream4-fear.webp"

image CG Dream5:
    xysize (1280,720)
    xalign 1.0
    ycenter 0.5
    xoffset 250
    zoom 2.3
    "images/CGs/Chapter 1/dream5-fury.webp"
    ease 5.0 xoffset 0 zoom 1.0

transform DreamRainbow:
    matrixcolor ColorizeMatrix("#000000","#ffffff")

    ease 7.5 matrixcolor ColorizeMatrix("#000000","#ff4034")
#library
image CG Library Lore 1:
    "images/CGs/Chapter 1/Library-Lore-CG1.webp"
    zoom 0.3

image CG Library Lore 2:
    "images/CGs/Chapter 1/Library-Lore-CG2.webp"
    zoom 0.2

image CG Library Lore 3:
    "images/CGs/Chapter 1/Library-Lore-CG3.webp"
    zoom 0.3

image CG Library Lore 4:
    "images/CGs/Chapter 1/Library-Lore-CG4.webp"
    zoom 0.25

image CG Library DEMON 1:
    "images/CGs/Chapter 1/demon1_concept.webp"
    zoom 0.25
    xcenter 0.75
image CG Library DEMON 2:
    "images/CGs/Chapter 1/demon2_concept.webp"
    zoom 0.27
    xcenter 0.9
image CG Library WereFolk:
    "images/CGs/Chapter 1/werehare_concept.webp"
    zoom 0.2
    xcenter 0.5

image Dreamlads1:
    "images/CGs/Chapter 1/dreamboys-1.webp"
    zoom 0.2

image Dreamlads2:
    "images/CGs/Chapter 1/dreamboys-2.webp"
    zoom 0.2

image Dreamlads3:
    "images/CGs/Chapter 1/dreamboys-3.webp"
    zoom 0.2

image Dreamlads4:
    "images/CGs/Chapter 1/dreamboys-4.webp"
    zoom 0.2

image Dreamlads5:
    "images/CGs/Chapter 1/dreamboys-5.webp"
    zoom 0.2

image TessieTailCG_L:
    zoom 0.27
    anchor (0.5,1.0)
    matrixtransform rotated()

    "images/Props/Tessie_Tail_L.webp"

image TessieTailCG_R:
    zoom 0.27
    anchor (0.5,1.0)
    matrixtransform rotated()

    "images/Props/Tessie_Tail_R.webp"

image Jamie_Mini:
    ycenter 0.6
    xcenter 0.8
    zoom 0.65
    "images/Characters/Minis/Mini_Jamie.webp"

image CG Black Tome:
    zoom 0.15
    "images/CGs/Chapter 1/ER_Tome.webp"

define NVL_BlackTome = Character("Tome", image = "blacktome", callback = Bleep,ctc="end_of_msg",ctc_pause="end_of_msg", cb_id = "9A", who_color = "#ED2A82",kind=nvl)

image side blacktome:
    yalign 1.2
    xalign 0.8
    zoom 0.13
    "images/CGs/Chapter 1/ER_Tome.webp"


image Rock:
    ycenter 0.45
    xcenter 0.4
    zoom 0.2
    "images/CGs/Chapter 1/rock_cg.webp"
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image Charm_Bracelet:
    ycenter 0.45
    xcenter 0.5
    zoom 0.3
    "images/CGs/Chapter 1/Protection_Charm.webp"
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG WIP Cafe Jamie:
    "images/CGs/Chapter 1/jamiecafewip.png"
    xcenter 0.5
    ycenter 0.4
    zoom 0.25

default drinkChoice = 1
image CG Cafe Drink:
    zoom 0.28
    xcenter 0.56
    ycenter 0.47
    ConditionSwitch(
        "drinkChoice <= 1","images/Props/Ch 1/CG Dagon Drink.webp",
        "drinkChoice == 2","images/Props/Ch 1/CG Divine Drink.webp",
        "drinkChoice >= 3","images/Props/Ch 1/CG Prismatic Drink.webp")

    on show:
        yoffset -700
        ease 1.0 yoffset 0
        idleFloat(2,10)

image SmallCafeDrink:
    zoom 0.07
    xcenter 0.56
    ycenter 0.5
    ConditionSwitch(
        "drinkChoice <= 1","images/Props/Ch 1/CG Dagon Drink.webp",
        "drinkChoice == 2","images/Props/Ch 1/CG Divine Drink.webp",
        "drinkChoice >= 3","images/Props/Ch 1/CG Prismatic Drink.webp")

image CG Taro wip:
    "images/CGs/Chapter 1/tarowip.webp"
    xcenter 0.5
    ycenter 0.45
    zoom 0.3

image CG Madhouse Hold Hand Wip:
    "images/CGs/Chapter 1/madhousehandhold.jpg"
    xcenter 0.69
    ycenter 0.5
    zoom 0.19
#WIP ZONE----------------

image CG_Rob Carry:
    zoom 0.4
    xcenter 0.56
    ycenter 0.5
    "images/CGs/chapter 1/robcarry_wip.jpg"
image CG MM Hold:
    "images/CGs/Chapter 1/mm_tired.webp"
    xcenter 0.65
    ycenter 0.49
    zoom 0.34

image CG AugustAtlas 1:
    size (1280,720)
    "images/CGs/Chapter 1/AugustAtlas1.webp"

image CG AugustAtlas 2:
    size (1280,720)
    "images/CGs/Chapter 1/AugustAtlas2.webp"

image CG MM_Chill:
    "images/CGs/Chapter 1/madhousezzz2frown.png"
    xcenter 0.5
    ycenter 0.45
    zoom 0.4
image CG MM_Chill2:
    "images/CGs/Chapter 1/madhousezzz2.png"
    xcenter 0.5
    ycenter 0.45
    zoom 0.4

#JAMIE FIGHT----------------------------------
image CG Mike Wins:
    xcenter 0.5
    ycenter 0.45
    zoom 0.4
    "images/CGs/Chapter 1/mike_win.png"

image CG Jamie Wins:
    xcenter 0.5
    ycenter 0.6
    zoom 0.5
    "images/CGs/Chapter 1/jamie_win.png"

image CG Gus Walk:
    xcenter 0.5
    ycenter 0.45
    zoom 0.4
    "images/CGs/Chapter 1/guswalk.png"

image CG Stranger:
    "images/CGs/Chapter 1/strangerwalkhome.png"
    xcenter 0.5
    ycenter 0.7
    zoom 0.6

image CG Tail Peek:
    size (1280,720)
    "images/CGs/Chapter 1/tailpeek.webp"

image CG August Lost:
    "images/CGs/Chapter 1/august_lost.webp"
    xcenter 0.5
    ycenter 0.55
    zoom 0.34

image CG August Lost Paws:
    "images/CGs/Chapter 1/august_lost_paws.webp"
    xcenter 0.5
    ycenter 0.45
    zoom 0.4

image CG August Lost Snow:
    "images/CGs/Chapter 1/august_lost_snow.webp"
    xcenter 0.5
    ycenter 0.45
    zoom 0.65

image CG August Lost Legs:
    "images/CGs/Chapter 1/august_lost_legs.webp"
    xcenter 0.5
    ycenter 0.45
    zoom 0.65

image CG August Lost Face:
    "images/CGs/Chapter 1/august_lost_face.webp"
    xcenter 0.5
    ycenter 0.429
    zoom 0.65

image CG Cellphone:
    "images/CGs/Chapter 1/cellphone.webp"
    xcenter 0.3
    ycenter 0.48
    zoom 0.35
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CGlonghope_map:
    "images/CGs/Chapter 1/longhope_map.png"
    xcenter 0.5
    ycenter 0.48
    zoom 0.2
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG Spruce_Photo:
    "images/CGs/Chapter 1/August_House_CG1.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700


image CG August_Group_Photo:
    "images/CGs/Chapter 1/August_House_CG3.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.25
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG August_Family_Photo:
    "images/CGs/Chapter 1/summersfamily.png"
    xcenter 0.5
    ycenter 0.48
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700
image CG August_License:
    "images/CGs/Chapter 1/August_House_CG4.webp"
    xcenter 0.5
    ycenter 0.4
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image Oz Ambulance:
    zoom 0.6
    xcenter 0.56
    ycenter 0.5
    "images/Props/Oz_Ambulance.webp"

image CG AugustCar:
    zoom 0.5
    ycenter 0.5
    "images/CGs/Chapter 1/August_Car.webp"

image AugustCar Black:
    Solid("#000000")

image CG Jamie Hug:
    "images/CGs/Chapter 1/jamie_hug.webp"
    xcenter 0.5
    ycenter 0.59
    zoom 0.4

image CG RobynInGusClothes:
    "images/CGs/Chapter 1/RobynInGusClothes.webp"
    xcenter 0.5
    ycenter 0.5
    zoom 0.37

    on show:
        yoffset 700
        ease 1.0 yoffset 0

        idleFloat(2.2,10)
    on hide:
        ease 1.0 yoffset 700

image CG Dinner WIP:
    "images/CGs/Chapter 1/cabincgwip1.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.65

#Atlas Room Investigation

image CG Atlas Alien Pic:
    "images/CGs/Chapter 1/AugustHouse_CG6.png"
    xcenter 0.5
    ycenter 0.4
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG Atlas Notebook:
    "images/CGs/Chapter 1/Atlas_Room_CG1.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.3
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG Atlas Portrait:
    "images/CGs/Chapter 1/moths.webp"
    xcenter 0.5
    ycenter 0.5
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700

image CG Atlas Vacation:
    "images/CGs/Chapter 1/August_House_CG5.png"
    xcenter 0.5
    ycenter 0.5
    zoom 0.4
    on show:
        yoffset 700
        ease 1.0 yoffset 0
    on hide:
        yoffset 0
        ease 1.0 yoffset 700
#------------------------------------------- Gus kiss
image CG Gus kiss 1:
    "images/CGs/Chapter 1/guskiss1.webp"
    xcenter 0.3
    ycenter 0.4
    zoom 0.45

image CG Gus kiss 2:
    "images/CGs/Chapter 1/guskiss2.webp"
    xcenter 0.7
    ycenter 0.5
    zoom 0.35
