default numWisp = 0

define Walker = Character("Mr. Walker", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "3A", who_color = "#f0bf6c")

transform randOffset:
    parallel:
        choice:
            yoffset 0
        choice:
            yoffset 5
        choice:
            yoffset -5
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 5
        choice:
            xoffset -5
    pause 0.275
    repeat


image willowisp:
    zoom 0.16
    "lwisp"
    on hide:
        ease 0.5 blur 10 alpha 0 zoom 1.0

layeredimage lwisp:
    always:
        "images/Characters/Mistwalker/will-o-wisp-flame.webp" at randOffset
    always:
        "images/Characters/Mistwalker/will-o-wisp-body.webp" at randOffset


image willowisp1 = "willowisp"
image willowisp2 = "willowisp"
image willowisp3 = "willowisp"
image willowisp4 = "willowisp"
image willowisp5 = "willowisp"

transform mw_lantern_tf:
    zoom 0.2
    anchor (0.5,0.5)
    xpos 1100
    ypos 320

image mw_lantern default:
    mw_lantern_tf
    "images/Characters/Mistwalker/Lantern.webp"
    idleFloat(2,10)
    hueFloat(2.6,40)

image mw_lantern glow:
    mw_lantern_tf
    "images/Characters/Mistwalker/Lantern.webp"
    parallel:
        idleFloat(2,10)
    parallel:
        matrixcolor HueMatrix(-100)
        ease 0.6 matrixcolor HueMatrix(0)
        hueFloat(2.6,40)

image mw_lantern hurt:
    mw_lantern_tf
    parallel:
        matrixcolor HueMatrix(-150)
        "images/Characters/Mistwalker/Lantern.webp"
        ease 0.75 matrixcolor HueMatrix(0)
        hueFloat(2.6,40)
    parallel:
        matrixtransform rotated()
        ease 0.6 matrixtransform rotated(y=360)
    parallel:
        idleFloat(2,10)

transform hueFloat(t=2,hv=50,sv=0):
    matrixcolor HueMatrix(sv)
    block:
        ease t matrixcolor HueMatrix(hv)
        ease t matrixcolor HueMatrix(sv)
        repeat

transform flicker(tv=0.1,ti=0.1,r=2):
    alpha 0
    pause ti
    alpha 1
    pause tv
    repeat r

transform WispEnter:
    zoom 1.5
    alpha 0
    blur 10

    ease 0.75 blur 0 alpha 1 zoom 1.0

transform wispPos(xNum=1,xTotal=1):
    xcenter 0.9
    ycenter (0.5 + renpy.random.choice([0,0.03,-0.03]))
    ease 0.5 xcenter 0.3 + (xNum-numWisp*.5)*0.15

    idleFloat(xNum*0.3+2,10)
    on hide:
        ease 0.5 blur 10 alpha 0 zoom 1.0

transform wispPosEase(xNum=1,xTotal=1):
    alpha 1
    blur 0
    zoom 1.0
    ease 0.5 xcenter 0.3 + (xNum-numWisp*.5)*0.15 ycenter (0.5 + renpy.random.choice([0,0.03,-0.03]))
    idleFloat(xNum*0.3+2,10)
    on hide:
        ease 0.5 blur 10 alpha 0 zoom 1.0



transform WalkerSpin:
    matrixtransform rotated()
    ease 0.5 matrixtransform rotated(z=360*2)

transform WalkerEnter:
    zoom 1.5
    alpha 0
    blur 10

    ease 0.75 blur 0 alpha 1 zoom 1.0

transform WalkerPos:
    xcenter 0.5
    ycenter 0.7
    zoom 0.2


image mw_armLTilt:
    "images/Characters/Mistwalker/MW_ArmL.webp"
    yzoom 1
    matrixtransform rotated()
    parallel:
        ease 0.25 yzoom -1
        pause 1.75
        ease 0.25 yzoom 1
    parallel:
        ease 0.75 matrixtransform rotated(z=-50)
        pause 0.1

        ease 0.3 matrixtransform rotated(z=-20)
        pause 0.2
        ease 0.3 matrixtransform rotated(z=-50)

        pause 0.1
        ease 0.75 matrixtransform rotated()
    parallel:
        ease 0.55 yoffset -2300 xoffset 1300
        pause 0.3

        ease 0.3 yoffset -1300 xoffset 1300
        pause 0.2
        ease 0.3 yoffset -2300 xoffset 1300

        pause 0.2
        ease 0.55 yoffset 0 xoffset 0

    randOffset

image mw_hatTilt:
    matrixtransform rotated() yoffset 0
    "images/Characters/Mistwalker/MW_Hat.webp"
    pause 0.85
    ease 0.3 matrixtransform rotated(z=30) yoffset -500
    pause 0.2
    ease 0.3 matrixtransform rotated() yoffset 0
    pause 0.85
    randOffset

layeredimage mw_normalface:
    always:
        "images/Characters/Mistwalker/MW_Eyes.webp" at randOffset
    always:
        "images/Characters/Mistwalker/MW_Mouth.webp" at randOffset

image mwface_hurt:
    "images/Characters/Mistwalker/MW_EvilFace.webp"
    pause 0.15
    "mw_normalface"

image mwhat_hurt:
    "images/Characters/Mistwalker/MW_Hat.webp"
    parallel:
        ease 0.3 yoffset -400
        ease 0.3 yoffset 0
    parallel:
        pause 0.05
        #WalkerSpin


image mw_head:
    choice:
        "images/Characters/Mistwalker/MW_Head.webp"
    choice:
        "images/Characters/Mistwalker/MW_Head.webp"
    choice:
        "images/Characters/Mistwalker/MW_Head.webp"
    choice:
        choice:
            "images/Characters/Mistwalker/MW_Head.webp"
        choice:
            "images/Characters/Mistwalker/MW_Head.webp"
        choice:
            "images/Characters/Mistwalker/MW_Head.webp"
        choice:
            "images/Characters/Mistwalker/MW_HeadAlt.webp"

layeredimage MrWalker:

    always:
        "images/Characters/Mistwalker/MW_Body.webp" at randOffset

    group head:
        attribute base default:
            "images/Characters/Mistwalker/MW_Head.webp" at randOffset
        attribute hurt:
            "mw_head"
        attribute evil:
            "mw_head"
        attribute attack:
            "mw_head"

    group face:
        attribute base default:
            "mw_normalface"
        attribute hurt:
            "mwface_hurt"
        attribute evil:
            "images/Characters/Mistwalker/MW_EvilFace.webp" at randOffset
        attribute attack:
            "mw_normalface"


    group hat:
        attribute base default:
            "images/Characters/Mistwalker/MW_Hat.webp" at randOffset
        attribute hurt:
            "mwhat_hurt" at randOffset
        attribute evil:
            "images/Characters/Mistwalker/MW_Hat.webp" at randOffset
        attribute attack:
            "mw_hatTilt"

    group armR:
        attribute base default:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset
        attribute hurt:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset
        attribute attack:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset


    group armL:
        pos (2000,1400)
        attribute base default:
            "images/Characters/Mistwalker/MW_ArmL.webp" at randOffset
        attribute hurt:
            "images/Characters/Mistwalker/MW_ArmL.webp" at randOffset
        attribute attack:
            "mw_armLTilt"

layeredimage MrBald:

    always:
        "images/Characters/Mistwalker/MW_Body.webp" at randOffset

    group head:
        attribute base default:
            "images/Characters/Mistwalker/MW_Head.webp" at randOffset
        attribute hurt:
            "mw_head"
        attribute evil:
            "mw_head"
        attribute attack:
            "mw_head"

    group face:
        attribute base default:
            "mw_normalface"
        attribute hurt:
            "mwface_hurt"
        attribute evil:
            "images/Characters/Mistwalker/MW_EvilFace.webp" at randOffset
        attribute attack:
            "mw_normalface"

    group armR:
        attribute base default:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset
        attribute hurt:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset
        attribute attack:
            "images/Characters/Mistwalker/MW_ArmR.webp" at randOffset


    group armL:
        pos (2000,1400)
        attribute base default:
            "images/Characters/Mistwalker/MW_ArmL.webp" at randOffset
        attribute hurt:
            "images/Characters/Mistwalker/MW_ArmL.webp" at randOffset
        attribute attack:
            "mw_armLTilt"
