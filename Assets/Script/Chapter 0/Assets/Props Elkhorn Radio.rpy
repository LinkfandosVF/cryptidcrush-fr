init offset = -1

#------------------------------------------------------------------------------- Backgrounds/CGs
image testBG = Solid("#191f1a")

image testHeightBG:
    contains:
        ypos 0
        Solid("#14ff3c")
    contains:
        ypos 930- (5*12+6)*10
        Solid("#191f1a")

layeredimage BG Dream Zone:
    always:
        "images/BGs/Dream_Zone.webp"
    always:
        "DZWAVE"

image DZWAVE:
        alpha 0.4
        WaveImage("images/BGs/Dream_Zone.webp", amp = 10, strip_height = 3,melt=True,freq=35)

image DreamZoneBase = "images/BGs/Dream_Zone.webp"

image BG Dream Bedroom:
    zoom 0.73
    "images/BGs/Dream Bedroom.webp"

image BG Black:
    Solid("#000000")

image Overlay Slow Black:
    Solid("#000000")
    alpha 0
    ease 10.0 alpha 0.4

image Overlay Green Flashing:
    Solid("#2b9e1a")
    alpha 0
    ease 10.0 alpha 0.25
    choice:
        ease 6.0 alpha 0.1
        ease 6.0 alpha 0.25
        repeat

image Driving Night Graphic:
    xzoom 0.2
    yzoom 0.2
    xcenter 0.5
    ycenter -0.4
    "images/CGs/Driving_Night.webp"
    ease 1.0 ycenter 0.4

image Driving Dawn Graphic:
    xzoom 0.2
    yzoom 0.2
    xcenter 0.5
    ycenter -0.4
    "images/CGs/Driving_Dawn.webp"
    ease 1.0 ycenter 0.4

image Radio On Air Graphic:
    xzoom 0.15
    yzoom 0.15
    xcenter 1.8
    ycenter 0.4
    "images/CGs/OnAir.webp"
    ease 1.0 xcenter 0.7

image Overlay Dreamy:
    alpha 0
    pause 2.0
    "images/Props/effects/Dreamy.webp"
    ease 4.0 alpha 1
    pause 1.0
    ease 4.0 alpha 0
    pause 2.0
    "images/Props/effects/Dreamy2.webp"
    ease 4.0 alpha 1
    pause 1.0
    ease 4.0 alpha 0
    repeat

image MM_Appears Cackle CG:
    xzoom -0.25
    yzoom 0.25

    ycenter 0.39
    "images/CGs/MM_Cackle_CG.webp"

image MM_Appears CG:
    zoom 0.3

    yalign 0.0
    yoffset 30
    "images/CGs/MM_Appears_CG.webp"

image Jamie_Pissed CG:
    xzoom 0.25
    yzoom 0.25

    ycenter 0.5
    "images/CGs/JamiePissed2.webp"

image Jamie_Pissed 2 CG:
    contains:
        xzoom 0.25
        yzoom 0.25

        ycenter 0.5
        xcenter 0.5
        "images/CGs/Jamie_Pissed1.webp"
    contains:
        xzoom 0.25
        yzoom 0.25

        ycenter 0.5
        xcenter 0.5
        "images/CGs/JamiePissed2.webp"
        alpha 1
        ease 1.0 alpha 0

image MM_PC_Hug CG:
    xzoom 0.34
    yzoom 0.34
    ycenter 0.6
    "images/CGs/MMxPC_Hug.webp"

image MM_PC_Hug 2 CG:
    xzoom 0.34
    yzoom 0.34
    ycenter 0.6
    "images/CGs/MMxPC_Hug2.webp"

image Madlas_Fire CG:
    xzoom 0.25
    yzoom 0.25
    ycenter 0.4
    "images/CGs/Madlas_Fire_CG2.webp"

image Madlas_Fire2 CG:
    xzoom 0.25
    yzoom 0.25
    alpha 0
    ycenter 0.4
    "images/CGs/Madlas_Fire_CG.webp"
    ease_bounce 3.0 alpha 1

image Atlas_Phone Ring CG:
    xzoom 0.27
    yzoom 0.27
    ycenter 0.4
    "images/CGs/Atlas_Phone.webp"
    pause 1.5
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    pause 0.5
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    repeat

image Atlas_Phone CG:
    xzoom 0.27
    yzoom 0.27
    ycenter 0.4
    "images/CGs/Atlas_Phone.webp"

image MM_Phone 1 CG:
    xzoom 0.27
    yzoom 0.27
    ycenter 0.4
    "images/CGs/MM_Phone1.webp"
    pause 1.5
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    pause 0.5
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    linear 0.03 ycenter 0.395
    linear 0.03 ycenter 0.405
    repeat

image MM_Phone 2 CG:
    xzoom 0.27
    yzoom 0.27
    ycenter 0.4
    "images/CGs/MM_Phone2.webp"
    pause 1.5
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    pause 0.5
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    repeat

image MM_Phone 3 CG:
    xzoom 0.27
    yzoom 0.27
    ycenter 0.4
    "images/CGs/MM_Phone3.webp"
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    linear 0.03 ycenter 0.39
    linear 0.03 ycenter 0.41
    repeat

image ThankYou CG:
    xcenter 0.5
    ycenter 0.5
    xzoom 0.5
    yzoom 0.5
    "images/CGs/Thanks_CG.webp"

image DevThankYou CG:
    xzoom 0.3
    yzoom 0.3
    "images/CGs/Dev_Thanks.webp"

image CG Floating Away:
    matrixcolor TintMatrix("#ffded1")
    xalign 1.0
    yalign 0.0
    zoom 0.3
    xoffset 1
    yoffset -20
    "images/CGs/Chapter 0/Floating Away CG.webp"
    block:
        ease 3 yoffset -1
        ease 3 yoffset -41
        repeat

image CG Lifeline:
    "images/CGs/Chapter 0/lifeline.webp"

layeredimage CG Lifeline2:
    always:
        "images/CGs/Chapter 0/lifeline.webp"
    always:
        "images/CGs/Chapter 0/lifelineB.webp"

transform lifeline_pos:
    matrixcolor TintMatrix("#ffded1")
    xcenter 0.5
    ycenter 0.7
    zoom 0.4
    yoffset -41
    block:
        ease 3 yoffset -1
        ease 3 yoffset -41
        repeat
#------------------------------------------------------------------------------- Props
image Flickering Black:
    Solid("#000000")
    alpha 0
    pause 0.1
    alpha 1
    pause 0.1
    alpha 0
    pause 0.05
    alpha 1
    pause 0.1
    alpha 0
    pause 0.3
    alpha 1

image DDS Logo:
    xcenter 0.5
    ycenter 0.5
    xzoom 0.5
    yzoom 0.5
    "images/Props/DDS.webp"

layeredimage Debbie Prop:
    always:
        "DarkBG"
    always:
        "DebbieCG"

layeredimage Debbie Prop Leave:
    always:
        "DarkBG"
    always:
        "DebbieCG2"
image DarkBG:
    Solid("#000000")
    alpha 0.4
image DebbieCG:
    zoom 0.15
    ycenter 0.35
    xcenter 0.5
    yoffset 700
    "images/Props/Ch 0/DebbieCG.webp"
    pause 0.5
    ease 0.5 yoffset 0

image DebbieCG2:
    zoom 0.15
    ycenter 0.35
    xcenter 0.5
    yoffset 0
    "images/Props/Ch 0/DebbieCG.webp"
    ease 0.5 yoffset 700

image ToxicWasteCG:
    zoom 0.16
    ycenter 0.35
    "images/Props/Ch 0/Toxic Waste.webp"
