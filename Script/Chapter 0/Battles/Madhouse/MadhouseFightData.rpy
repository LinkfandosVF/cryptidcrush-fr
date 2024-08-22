transform MMD_Entry_Pos:
    yoffset 700
    xcenter 0.5
    ycenter 0.6

    ease 1.0 yoffset 0
    block:
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

transform MMD_Default_Pos:
    yoffset 0
    xcenter 0.5
    ycenter 0.6

    block:
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

transform MMD_Attack_Pos:
    xcenter 0.5
    ycenter 0.6
    yoffset 0
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.05 xoffset 0
    block:
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

transform MMD_Damaged_Pos:
    xcenter 0.5
    ycenter 0.6
    yoffset 0
    xoffset 0
    block:
        ease 2.6 yoffset -10
        ease 2.6 yoffset 10
        repeat

image MMFight_Chair:
    zoom 0.25
    "images/Props/Elkhorn Radio/MM_Chair.webp"

image MMFight_Speaker:
    zoom 0.28
    "images/Props/Elkhorn Radio/MM_Speaker.webp"

transform MMFight_LeftProp_Entry:
    alpha 1
    zoom 1.0
    blur 0
    matrixtransform RotateMatrix(0.0, 0.0, -360.0)
    xcenter 0.2
    ycenter 1.5

    choice:
        pause 0.2
    choice:
        pause 0.3
    choice:
        pause 0.4

    ease 1.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) ycenter 0.5

    block:
        parallel:
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            choice:
                ease 2.5 yoffset -20
                ease 2.5 yoffset 20
            choice:
                ease 2.0 yoffset -20
                ease 2.0 yoffset 20
            choice:
                ease 3.0 yoffset -20
                ease 3.0 yoffset 20
        repeat

transform MMFight_RightProp_Entry:
    alpha 1
    zoom 1.0
    blur 0
    matrixtransform RotateMatrix(0.0, 0.0, 360.0)
    xcenter 0.8
    ycenter 1.5

    choice:
        pause 0.2
    choice:
        pause 0.3
    choice:
        pause 0.4

    ease 1.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0) ycenter 0.5

    block:
        parallel:
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            choice:
                ease 2.5 yoffset -20
                ease 2.5 yoffset 20
            choice:
                ease 2.0 yoffset -20
                ease 2.0 yoffset 20
            choice:
                ease 3.0 yoffset -20
                ease 3.0 yoffset 20
        repeat

transform MMFight_LeftProp_Pos:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    xcenter 0.2
    ycenter 0.5
    alpha 1
    zoom 1.0
    blur 0

    block:
        parallel:
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            choice:
                ease 2.5 yoffset -20
                ease 2.5 yoffset 20
            choice:
                ease 2.0 yoffset -20
                ease 2.0 yoffset 20
            choice:
                ease 3.0 yoffset -20
                ease 3.0 yoffset 20
        repeat

transform MMFight_RightProp_Pos:
    matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    xcenter 0.8
    ycenter 0.5
    alpha 1
    zoom 1.0
    blur 0

    block:
        parallel:
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -70.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, -15.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            choice:
                ease 4.0 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
                matrixtransform RotateMatrix(0.0, 0.0, 0.0)

        parallel:
            choice:
                ease 2.5 yoffset -20
                ease 2.5 yoffset 20
            choice:
                ease 2.0 yoffset -20
                ease 2.0 yoffset 20
            choice:
                ease 3.0 yoffset -20
                ease 3.0 yoffset 20
        repeat

transform MMFight_LeftProp_Exit:
    zoom 1.0
    alpha 1

    pause 0.3

    parallel:
        ease 1.0 zoom 2.5 matrixtransform RotateMatrix(0.0, 0.0, 360.0*2) blur 10
    parallel:
        pause 0.5
        ease 0.4 alpha 0

transform MMFight_RightProp_Exit:
    zoom 1.0
    alpha 1

    choice:
        pause 0.01
    choice:
        pause 0.7

    parallel:
        ease 1.0 zoom 2.5 matrixtransform RotateMatrix(0.0, 0.0, -360.0*2) blur 10
    parallel:
        pause 0.5
        ease 0.4 alpha 0
