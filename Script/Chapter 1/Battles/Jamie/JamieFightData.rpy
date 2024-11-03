init python:
    renpy.register_shader("flashColor",
        variables="""
        uniform vec4 u_color;
        uniform float u_mix;

        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

    """,
        vertex_300="""
        v_tex_coord = a_tex_coord;
    """,
        fragment_300="""
        vec4 baseTexture = texture2D(tex0, v_tex_coord.xy);

        gl_FragColor = mix(baseTexture,u_color,u_mix);
        gl_FragColor*= baseTexture.a;
    """)

transform hurt_flash_shader:
    shader "flashColor"
    u_mix 1.0
    u_color (1.0,1.0,1.0,1.0)

    pause 0.15

    u_mix 1.0
    u_color (0.0,0.0,0.0,1.0)
    pause 0.15

    u_mix 0.0
    alpha 0

    pause 0.15

    alpha 1

transform battle_jamie_pos:
    matrixcolor IdentityMatrix()
    xcenter 0.7
    matrixtransform rotated()
    xoffset 0

transform battle_jamie_mm_pos:
    matrixcolor IdentityMatrix()
    xcenter 0.3
    matrixtransform rotated()
    xoffset 0

transform battle_jamie_hurt_pos:
    xcenter 0.7
    matrixtransform rotated()
    matrixcolor ColorizeMatrix("#6b192d","#f23a3a")*SaturationMatrix(0)
    xoffset -30

    parallel:
        ease 0.1 xoffset 20
        ease 0.1 xoffset -15
        ease 0.1 xoffset 10
        ease 0.1 xoffset -5
        ease 0.05 xoffset 0
    parallel:
        ease 0.5 matrixtransform rotated(y=-360) matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)

    pause 0.5

transform battle_jamie_mm_hurt_pos:
    xcenter 0.3
    matrixtransform rotated()
    matrixcolor ColorizeMatrix("#6b192d","#f23a3a")*SaturationMatrix(0)
    xoffset -10

    parallel:
        ease 0.1 xoffset 10
        ease 0.1 xoffset -10
        ease 0.1 xoffset 10
        ease 0.1 xoffset -10
        ease 0.05 xoffset 0
    parallel:
        ease 0.5 matrixtransform rotated(y=360) matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)

transform battle_jamie_attack_pos:
    xcenter 0.7
    xoffset -10

    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.05 xoffset 0

transform battle_jamie_mm_attack_pos:
    xcenter 0.3
    xoffset -10

    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.1 xoffset 10
    ease 0.1 xoffset -10
    ease 0.05 xoffset 0

image Jamie_Battle_MM_CG Default:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.7
    "images/Characters/Madhouse/Battle/MM_Duel_Default.webp"
    ghostShader_trans(0.75,1.3,1.3)

image Jamie_Battle_MM_CG Hurt:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.7
    "images/Characters/Madhouse/Battle/MM_Duel_Hurt.webp"
    ghostShader_trans(0.75,1.3,1.3)

image Jamie_Battle_MM_CG Attack:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.7
    "images/Characters/Madhouse/Battle/MM_Duel_Attack.webp"
    ghostShader_trans(0.75,1.3,1.3)

layeredimage Jamie_Battle_CG Default:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.57
    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Base.webp"

    always:
        "Jamie_Battle_Wisp"

image Jamie_Battle_Wisp:
    "images/Characters/Jamie/Battle/Jamie_Battle_Wisp.webp"
    yoffset -20

    block:
        parallel:
            ghostShader_trans(1.0,0.3,0.3)
        parallel:
            ease 2.0 yoffset 0
            ease 2.0 yoffset -20
            repeat

image Jamie_Battle_Wisp_Panic:
    "images/Characters/Jamie/Battle/Jamie_Battle_Wisp_Panic.webp"
    yoffset -20

    block:
        parallel:
            ghostShader_trans(1.0,0.3,0.3)
        parallel:
            ease 2.0 yoffset 0
            ease 2.0 yoffset -20
            repeat

layeredimage Jamie_Battle_CG Hurt:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.57

    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Base.webp"

    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Hurt.webp"

    always:
        "Jamie_Battle_Wisp_Panic"

layeredimage Jamie_Battle_CG Attack:
    anchor (0.5,0.5)
    zoom 0.35
    ycenter 0.57

    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Base.webp"

    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Attack.webp"

    always:
        "images/Characters/Jamie/Battle/Jamie_Battle_Attack_Fire.png"

    always:
        "Jamie_Battle_Wisp"

image CG Crowd:
    anchor (0.5,1.0)
    ypos 1.0
    zoom 0.4
    "images/CGs/Chapter 1/Crowd.webp"

image CG2 Crowd:
    xzoom -1
    "CG Crowd"

image CG_RobbieRobynDuo:
    zoom 0.3
    ycenter 0.5
    anchor (0.5,0.5)
    "images/CGs/Chapter 1/RobbieRobynDuo.webp"

image GrabbingMadhouse:
    zoom 0.5
    xcenter 0.5
    ycenter 0.4
    anchor (0.5,0.5)

    "images/CGs/Chapter 1/GrabhouseMike.webp"
