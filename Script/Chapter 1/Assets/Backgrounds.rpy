init offset = -1

#outdoors

image BG Hill Day:
    xysize (1280,720)
    "images/BGs/Camp/hill day.webp"

image BG Pond:
    xysize (1280,720)
    "images/BGs/Chapter 1/pondbg.webp"

image BG Hiking Trail:
    blur 2
    xysize (1280,720)
    "images/BGs/Chapter 1/hiking_trail.webp"

image BG Apartment Kitchen:
    xysize (1280,720)
    "images/BGs/Chapter 1/Kitchen BG_Day.webp"

image BG Apartment Day:
    xysize (1280,720)
    "images/BGs/Chapter 1/apartment_day.webp"

image BG Hospital Room:
    xysize (1280,720)
    "images/BGs/Chapter 1/hospitalroom.webp"

#-------------------------------------------------------OUTSIDE
image BG Bridge:
    xysize (1280,720)
    "images/BGs/Chapter 1/bridge.webp"

image BG Sky Day:
    xysize (1280,720)
    "images/BGs/Chapter 1/skybg-day.webp"

image BG Sky Night:
    xysize (1280,720)
    "images/BGs/Chapter 1/skybg-night.webp"

image BG Sky Gray:
    xysize (1280,720)
    "images/BGs/Chapter 1/skybg-gray.webp"

image BG RoadSideBlur:
    contains:
        "images/BGs/Road_Side.webp"
    contains:
        alpha 0.5
        WaveImage("images/BGs/Road_Side.webp", amp = 10, strip_height = 3,melt=True,freq=35)
        matrixcolor HueMatrix(0)
        ease 15.0 matrixcolor HueMatrix(540)
        ease 20.0 alpha 0 matrixcolor HueMatrix(1080)

image BG RoadSideBlurAfter = "images/BGs/Road_Side.webp"

# ---------------------------------------------------- DREAM
image BG Orange:
    xysize (1280,720)
    "images/BGs/Chapter 1/orange_bg.webp"

image BG Dream Yard:
    xysize (1280,720)
    "images/BGs/Chapter 1/dream_yard.webp"

image BG Dream Beach:
    xysize (1280,720)
    "images/BGs/Chapter 1/dream_beach.webp"

image BG Dream Sky:
    xysize (1280,720)
    "images/BGs/Chapter 1/dream_sky.webp"

layeredimage BG DreamBedroom:
    always:
        "DreamBedroomBase"
    always:
        "DreamBedroomAnim"

layeredimage BG DreamBedroom 2:
    always:
        "DreamBedroomBase"
    always:
        "DreamBedroomWave"

image DreamBedroomWave:
    xsize 1280
    ysize 720
    xcenter 0.5
    ycenter 0.5
    blur 5
    alpha 0
    WaveImage("images/BGs/Dream Bedroom.webp", amp = 10, strip_height = 3,melt=True,freq=35)
    pause 5.0
    ease 30.0 alpha 1.0

image DreamBedroomBase:
    xsize 1280
    ysize 720
    "images/BGs/Dream Bedroom.webp"

image DreamBedroomAnim:
    xsize 1280
    ysize 720
    "images/BGs/Dream Bedroom.webp"
    blur 0
    ease 5.0 blur 7
    pause 1.0
    ease 5.0 blur 0
    pause 0.5
    repeat
image BG Dream Meadow:
    xysize (1280,720)
    "images/BGs/Chapter 1/dream_meadow.webp"

image RoadSideWave:
    alpha 0.5
    WaveImage("images/BGs/Road_Side.webp", amp = 10, strip_height = 3,melt=True,freq=35)
    matrixcolor HueMatrix(0)
    ease 10.0 matrixcolor HueMatrix(360)
    ease 15.0 alpha 0 matrixcolor HueMatrix(720)

image BG atTheTableFright:
    xysize (1280,720)
    "images/BGs/Chapter 1/Wor_Galaxy.webp"

image BG Cafe:
    xysize (1280,720)
    "images/BGs/Chapter 1/cafe.webp"

image BG SunsetRoadside:
    xysize (1296,729)
    "images/BGs/Chapter 1/Road_Side_Sunset.webp"

image BG DaytimeRoadside:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/Roadside_Day_Cloudy.webp"

image BG Default:
    xysize (1280,720)
    "images/BGs/Generic BG.webp"

image BG OutsideHospital:
    xysize (1280,720)
    "images/BGs/Generic BG2.webp"

image BG Library:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/Longhope_Library.webp"

image BG Graveyard Night:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Graveyard/Graveyard Night.webp"

image BG Avenue:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/fresnoavenue_bg.webp"


image BG Main Street:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.4
    "images/BGs/Chapter 1/Main-street.webp"

image BG Empty Street Day:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/street_day.webp"
image BG Empty Street Night:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/street_night.webp"

#gus house-------------------------------------------
image BG Cabin:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/auggiecabin.webp"

image BG Cabin Inside:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/august_house_inside.webp"

#atlas room
image BG Atlas Room Wip:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/atlasroom_wip.png"

image BG Cabin Night:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/auggiecabin_night.webp"

image BG Lake Night:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Camp/Lake_night.webp"
image BG Lake Day:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Camp/boat_day.webp"

image BG Atlas Spooky:
    xysize (1280,720)
    "AT_Spook_Layers"

layeredimage AT_Spook_Layers:
    always:
        "images/CGs/Chapter Title Cards/Chapter 1/LeviathanWaltzB.webp"
    always:
        "AT_Spook_Wave"

image AT_Spook_Wave:
    WaveImage("images/CGs/Chapter Title Cards/Chapter 1/LeviathanWaltzB.webp", amp = 8, strip_height = 3,melt=True,freq=35)
    block:
        alpha 0
        choice:
            ease 5.0 alpha 0.3
        choice:
            ease 3.0 alpha 0.3
        choice:
            ease 7.0 alpha 0.5
        pause 1.0
        choice:
            ease 5.0 alpha 0
        choice:
            ease 3.0 alpha 0
        choice:
            ease 7.0 alpha 0
        pause 1.0
        repeat
image BG Autumn Road:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5

    "images/BGs/Chapter 1/AutumnRoad.webp"


image BG Near Cafe:
    blur 2
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5

    "images/BGs/Chapter 1/NearCafe.webp"


image BG August Cabin Inside:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/august_house_inside.webp"

image BG Atlas Room Day:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/atlasroom_morning.png"

image BG Cabin Bathroom:
    xysize (1280,720)
    xcenter 0.5
    ycenter 0.5
    "images/BGs/Chapter 1/bathroom_bg.webp"
