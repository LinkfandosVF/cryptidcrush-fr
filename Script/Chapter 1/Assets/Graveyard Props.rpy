layeredimage CG Mike Wake Up:
    always:
        "images/CGs/Chapter 1/mikewakeup.webp"

    always:
        "mwakeup_wave"

layeredimage CG Mike Wake Up2:
    always:
        "images/CGs/Chapter 1/mikewakelook.webp"

    always:
        "mwakeup_wave2"

image mwakeup_wave2:
    alpha 0.5
    matrixcolor TintMatrix("#50ff76")
    WaveImage("images/CGs/Chapter 1/mikewakelook.webp", amp = 10, strip_height = 4,melt=True,freq=35)
    block:
        parallel:
            choice:
                ease 4.0 alpha 0.3
            choice:
                ease 4.0 alpha 0.4
            choice:
                ease 4.0 alpha 0.6
            ease 4.0 alpha 1.0
        parallel:
            choice:
                pause 3
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 3
            choice:
                pause 1
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 5
            choice:
                pause 4
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 2
            choice:
                pause 6
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")

        repeat

transform mwakeup_trans:
    size (1280,720)
    xcenter 0.5
    ycenter 0.5

    on show:
        zpos 100
        ease 1.5 zpos 0

image mwakeup_wave:
    alpha 0.5
    matrixcolor TintMatrix("#50ff76")
    WaveImage("images/CGs/Chapter 1/mikewakeup.webp", amp = 10, strip_height = 4,melt=True,freq=35)
    block:
        parallel:
            choice:
                ease 4.0 alpha 0.3
            choice:
                ease 4.0 alpha 0.4
            choice:
                ease 4.0 alpha 0.6
            ease 4.0 alpha 1.0
        parallel:
            choice:
                pause 3
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 3
            choice:
                pause 1
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 5
            choice:
                pause 4
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")
                pause 2
            choice:
                pause 6
                ease 1 matrixcolor TintMatrix("#ff2020")
                ease 1 matrixcolor TintMatrix("#50ff76")

        repeat


image CG MM_HowDoILook:
    size (1280,720)
    xcenter 0.5
    ycenter 0.5
    "cg_mm_howdoilook2_layers"
image CG MM shoes:
    size (1280,720)
    xcenter 0.5
    ycenter 0.45
    zoom 0.6
    "images/CGs/Chapter 1/mikeshoes.webp"

image CG MM hands:
    size (1280,720)
    xcenter 0.5
    ycenter 0.45
    zoom 0.6
    "images/CGs/Chapter 1/mikehands.webp"

image cg_mm_howdoilook2_wave:
    WaveImage("images/CGs/Chapter 1/mikewakelook.webp", amp = 10, strip_height = 4,melt=True,freq=35)
    alpha 0.5

layeredimage cg_mm_howdoilook2_layers:
    always:
        "images/CGs/Chapter 1/mikewakelook.webp"
    always:
        "cg_mm_howdoilook2_wave"


layeredimage CG MikeInTheMirror 1:
    always:
        "MikeInTheMirror"
    always:
        "MikeInTheMirrorWave"

layeredimage CG MikeInTheMirror 2:
    always:
        "MikeInTheMirror2"
    # always:
    #     "MikeInTheMirrorWave2"


image MikeInTheMirror2:
    size (1280,720)
    "images/CGs/Chapter 1/CG MirrorMike 3.webp"

image MikeInTheMirrorWave2:
    size (1280,720)
    WaveImage("images/CGs/Chapter 1/CG MirrorMike 3.webp", amp = 10, strip_height = 4,melt=True,freq=35)
    alpha 0.5


image MikeInTheMirror:
    size (1280,720)
    "images/CGs/Chapter 1/CG MirrorMike 1.webp"

image MikeInTheMirrorWave:
    size (1280,720)
    WaveImage("images/CGs/Chapter 1/CG MirrorMike 2.webp", amp = 10, strip_height = 4,melt=True,freq=35)
    alpha 0.5
    pause 3.0
    ease 3.0 alpha 0

    #matrixcolor TintMatrix("#ffffff")
    block:
        choice:
            pause 1.0
        choice:
            pause 0.5
            ease 0.2 alpha 0.5 #matrixcolor TintMatrix("#61ff90")
            ease 0.2 alpha 0 #matrixcolor TintMatrix("#ffffff")
            pause 0.5
        choice:
            pause 3.0
        choice:
            pause 5.0
        ease 0.2 alpha 0.5 #matrixcolor TintMatrix("#61ff90")
        ease 0.2 alpha 0 #matrixcolor TintMatrix("#ffffff")
        repeat
