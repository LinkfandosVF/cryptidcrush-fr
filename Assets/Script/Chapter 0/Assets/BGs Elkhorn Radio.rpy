init offset = -1

image BG Gas Station Night = "images/BGs/Gas_Station_Night.webp"

image BG Apartment Bedroom:
    size (1280,720)
    "images/BGs/Apartment Bedroom.webp"

image BG Outside Radio Station:
    "BG Outside Radio Station Spooky"

image BG Outside Radio Station Spooky:
    contains:
        matrixcolor SaturationMatrix(1.3)*TintMatrix("#b2d1bd")
        alpha 1
        "images/BGs/Outside_Radio_Station2.webp"
    contains:
        matrixcolor SaturationMatrix(1.3)*TintMatrix("#b2d1bd")
        alpha 0
        "images/BGs/Outside_Radio_Station3.webp"
        choice:
            ease 3.0 alpha 1
            pause 0.5
            ease 3.0 alpha 0
        choice:
            ease 2.0 alpha 0.5
            pause 1.0
            ease 2.0 alpha 0
        choice:
            ease 1.0 alpha 0.75
            pause 0.5
            ease 1.0 alpha 0

        pause 1.0

        repeat

image BG Outside Radio Station Spooky3 = "images/BGs/Outside_Radio_Station2.webp"

image BG Outside Radio Station Near:
    xysize (1280,720)
    matrixcolor TintMatrix("#d1ffe1")
    zoom 1.1
    "images/BGs/Chapter 0/Outside_Radio_Station_Close.webp"

image BGCG Outside Radio Station Fence:
    matrixcolor TintMatrix("#d1ffe1")*BrightnessMatrix(-0.0)
    xzoom 0.4
    yzoom 0.5
    "images/BGs/Chapter 0/Outside_Radio_Station_Fence.webp"

image BG Road Side:
    matrixcolor TintMatrix("#8d78d2")
    "images/BGs/Road_Side.webp"

image BG Office Dark Spooky:
    contains:
        alpha 1
        "images/BGs/Office_dark.webp"

    contains:
        alpha 0
        "images/BGs/Office_dark2.webp"
        pause 2.0

        choice:
            pause 3.0
            ease_bounce 1.0 alpha 0.7
            ease_bounce 0.5 alpha 0.2
            ease_bounce 2.0 alpha 1.0
            pause 2.0
            ease_bounce 1.5 alpha 0.2
            ease_bounce 2.0 alpha 0.7
            ease_bounce 1.0 alpha 0.25
            ease_bounce 0.5 alpha 0
        choice:
            alpha 1
            pause 0.1
            alpha 0
            pause 0.05
            "images/BGs/Office_dark4.webp"
            alpha 1
            pause 0.1
            "images/BGs/Office_dark2.webp"
            alpha 0
            pause 0.3
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            "images/BGs/Office_dark4.webp"
            pause 1.5
            alpha 0
            pause 3.0
        choice:
            alpha 1
            pause 0.1
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 3.0
        choice:
            ease 7.0 alpha 1.0
            pause 1.0
            ease 7.0 alpha 0
        choice:
            "images/BGs/Office_dark4.webp"
            alpha 1.0
            pause 5.0
            alpha 0.0
            pause 3.0

        repeat

    contains:
        alpha 0
        pause 10.0
        "images/BGs/Office_dark3.webp"
        ease 5.0 alpha 1.0
        pause 10.0
        ease 5.0 alpha 0
        repeat

image BG Office Dark:
    contains:
        "images/BGs/Office_dark.webp"
    contains:
        alpha 0
        "images/BGs/Office_dark2.webp"
        pause 3.0
        ease_bounce 1.0 alpha 0.7
        ease_bounce 0.5 alpha 0.2
        ease_bounce 2.0 alpha 1.0
        pause 2.0
        ease_bounce 1.5 alpha 0.2
        ease_bounce 2.0 alpha 0.7
        ease_bounce 1.0 alpha 0.25
        ease_bounce 0.5 alpha 0
        repeat

image BG Hallway Radio Station = "images/BGs/Hallway_Radio_Station.webp"

image BG Hallway Radio Station Spooky = "images/BGs/Hallway_Radio_Station2.webp"

image BG Spirit World =  "images/BGs/Spirit_World.webp"

image BG Studio Room = "images/BGs/Studio_Room.webp"

image BG Studio Room Dark:
    contains:
        "images/BGs/Studio_Room.webp"

    contains:
        Solid("#000000")
        alpha 1
        ease 5.0 alpha 0

image BG Studio Room2:
    contains:
        "images/BGs/Studio_Room.webp"

    contains:
        "images/BGs/Studio_Room_Danger.webp"
        alpha 0
        matrixcolor TintMatrix("#a2d0a8")
        ease_bounce 10.0 alpha 1

image BG Studio Room Spooky:
    contains:
        "images/BGs/Studio_Room_Spooky.webp"

        pause 10.0

        choice:
            "images/BGs/Studio_Room_Spooky_You.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Are.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_So.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 1.2
        choice:
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5
            "images/BGs/Studio_Room_Spooky.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5
            "images/BGs/Studio_Room_Spooky.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5


        repeat

    contains:
        alpha 0
        "images/BGs/Studio_Room_Spooky_Monitors.webp"
        choice:
            ease 5.0 alpha 1
            ease 10.0 alpha 0
        choice:
            pause 3.0
            ease_bounce 1.0 alpha 0.7
            ease_bounce 0.5 alpha 0.2
            ease_bounce 2.0 alpha 1.0
            pause 2.0
            ease_bounce 1.5 alpha 0.2
            ease_bounce 2.0 alpha 0.7
            ease_bounce 1.0 alpha 0.25
            ease_bounce 0.5 alpha 0
        choice:
            alpha 1
            pause 0.1
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 3.0
        repeat

    contains:
        alpha 0
        "images/BGs/Studio_Room_Spooky_Monitors2.webp"

        choice:
            ease 5.0 alpha 1
            ease 5.0 alpha 0
        choice:
            alpha 0
            pause 10.0
        choice:
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 3.0
            alpha 0
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 2.0


        alpha 0
        pause 2.1
        repeat

    contains:
        alpha 1
        choice:
            yzoom -1
            xzoom 1
        choice:
            xzoom -1
            yzoom 1
        choice:
            xzoom -1
            yzoom -1
        choice:
            xzoom 1
            yzoom 1
        "images/BGs/Studio_Room_Glitch1.webp"
        pause 0.01
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom 1
            yzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom -1
            yzoom -1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom -1
            yzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            yzoom -1
            xzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        alpha 0

image BG Studio Room Spookier:
    choice:
        yzoom -1
        xzoom 1
    choice:
        xzoom -1
        yzoom 1
    choice:
        xzoom -1
        yzoom -1
    choice:
        xzoom 1
        yzoom 1
    "images/BGs/Studio_Room_Glitch1.webp"
    choice:
        "images/BGs/Studio_Room_Glitch1.webp"
        pause 0.1
        xzoom 1
        yzoom 1
        "images/BGs/Studio_Room_Glitch2.webp"
        pause 0.1
    choice:
        "images/BGs/Studio_Room_Glitch1.webp"
        pause 0.1
        xzoom -1
        yzoom -1
        "images/BGs/Studio_Room_Glitch2.webp"
        pause 0.1
    choice:
        "images/BGs/Studio_Room_Glitch1.webp"
        pause 0.1
        xzoom -1
        yzoom 1
        "images/BGs/Studio_Room_Glitch2.webp"
        pause 0.1
    choice:
        "images/BGs/Studio_Room_Glitch1.webp"
        pause 0.1
        yzoom -1
        xzoom 1
        "images/BGs/Studio_Room_Glitch2.webp"
        pause 0.1

    xzoom 1
    yzoom 1
    "images/BGs/Studio_Room_Spooky.webp"

    choice:
        pause 2.5
    choice:
        pause 5
    choice:
        pause 10
    repeat

image BG Studio Room Spookier2:
    contains:
        "images/BGs/Studio_Room_Spooky.webp"

        pause 10.0

        choice:
            "images/BGs/Studio_Room_Spooky_You.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Are.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_So.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 1.2
        choice:
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5
            "images/BGs/Studio_Room_Spooky.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5
            "images/BGs/Studio_Room_Spooky.webp"
            pause 0.3
            "images/BGs/Studio_Room_Spooky_Dead.webp"
            pause 0.5


        repeat

    contains:
        alpha 0
        "images/BGs/Studio_Room_Spooky_Monitors.webp"
        choice:
            ease 5.0 alpha 1
            ease 10.0 alpha 0
        choice:
            pause 3.0
            ease_bounce 1.0 alpha 0.7
            ease_bounce 0.5 alpha 0.2
            ease_bounce 2.0 alpha 1.0
            pause 2.0
            ease_bounce 1.5 alpha 0.2
            ease_bounce 2.0 alpha 0.7
            ease_bounce 1.0 alpha 0.25
            ease_bounce 0.5 alpha 0
        choice:
            alpha 1
            pause 0.1
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 3.0
        repeat

    contains:
        alpha 0
        "images/BGs/Studio_Room_Spooky_Monitors2.webp"

        choice:
            ease 5.0 alpha 1
            ease 5.0 alpha 0
        choice:
            alpha 0
            pause 10.0
        choice:
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 3.0
            alpha 0
            pause 0.5
            alpha 1
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1
            pause 0.1
            alpha 0
            pause 0.3
            alpha 1
            pause 1.0
            alpha 0
            pause 2.0


        alpha 0
        pause 2.1
        repeat

    contains:
        alpha 0
        choice:
            yzoom -1
            xzoom 1
        choice:
            xzoom -1
            yzoom 1
        choice:
            xzoom -1
            yzoom -1
        choice:
            xzoom 1
            yzoom 1
        alpha 1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom 1
            yzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom -1
            yzoom -1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            xzoom -1
            yzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        choice:
            "images/BGs/Studio_Room_Glitch1.webp"
            pause 0.1
            yzoom -1
            xzoom 1
            "images/BGs/Studio_Room_Glitch2.webp"
            pause 0.1
        alpha 0
        choice:
            pause 5.0
        choice:
            pause 10.0
        choice:
            pause 15.0
        choice:
            pause 1.0
        choice:
            pause 20.0

        repeat

image BG Studio Room Aftermath = "images/BGs/Studio_Room_Aftermath.webp"
