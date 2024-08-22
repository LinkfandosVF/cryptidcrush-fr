init python:
    def nwDissolve(xTime = 0.5):
        return { "master" : Dissolve(xTime) }

    def nwPixellate(xTime = 0.5,xSteps=7):
        return { "master" : Pixellate(xTime,xSteps) }

    def rotated(x=0,y=0,z=0):
        return RotateMatrix(x, y, z)

    def BGFade(bg="BG Default",t1=1.0,tp=0,t2=None,pixel=False):
        if t2 is None:
            t2 = t1

        if pixel:
            return MultipleTransition([
                False, Pixellate(t1),
                bg, Pause(tp),
                bg, Pixellate(t2),
                True])
        else:
            return MultipleTransition([
                False, Dissolve(t1),
                bg, Pause(tp),
                bg, Dissolve(t2),
                True])

    def BGSwing(bg="BG Default",newBG="BG Default",t=1.0):
        trans = Swing(delay=t, background="#000", flatten=False)

        _window_hide(False)
        renpy.scene()
        renpy.show(bg)
        renpy.with_statement(trans)

        renpy.scene()
        renpy.show(newBG)
        renpy.with_statement(trans)
        _window_show(False)

    def BGDissolve(name="",t=1.0,r=4,reverse=False,tw=None):
        img = "images/TransitionImages/" + name

        return ImageDissolve(img, t, r, reverse, tw)

    # Swing(delay=0.65, background="#000", flatten=False)

transform gameboy:
    matrixcolor ColorizeMatrix("#04200c","#dadda0")*SaturationMatrix(0)

transform climbfromhole(t=1.7,y=0):
    xoffset -300
    matrixtransform RotateMatrix(0, 0, 180)
    yoffset 900 + y

    parallel:
        pause t*0.3
        ease t*0.71 xoffset 0
    parallel:
        ease t*0.88 matrixtransform RotateMatrix(0, 0, 0)
    parallel:
        ease t*0.94 yoffset 0 + y

transform cDot(x,y):
    zoom 0.1
    xcenter 0.5
    ycenter 0.5
    xoffset x
    yoffset y

screen camera_dot(xDot,yDot):
    imagebutton:
        idle "images/CGs/Chapter 1/rock_cg.webp"
        at cDot(xDot,yDot)
        action Hide()

transform zoomed(xZoom):
    zoom xZoom

transform shaded(xColor="#ffffff"):
    matrixcolor TintMatrix(xColor)

transform transluscent(xAlpha =0.5):
    alpha xAlpha

transform vibrate(t=0.05,x=2):
    ease t xoffset x
    ease t xoffset -x
    repeat

transform vibratenum(t=0.1,x=2,r=2):
    ease t*0.5 xoffset x
    block:
        ease t xoffset -x
        ease t xoffset x
        repeat r
        ease t*0.5 xoffset 0

transform disappear(t=0.3):
    xzoom 1.0
    yzoom 1.0
    alpha 1
    blur 0
    ease t xzoom 0 yzoom 1.5 yoffset -100 alpha 0 blur 30

transform camera_zoom(z=0,x=0,y=0,t=0):
    ease t zpos z yoffset y xoffset x

transform hoppies_flipped(xIntensity=2.5):
    matrixtransform RotateMatrix(0.0, 180.0, 0)
    block:
        parallel:
            pause 0.1
            ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, -xIntensity)
            pause 0.1
            ease 0.2 matrixtransform RotateMatrix(0.0, 180.0, xIntensity)
        parallel:
            ease 0.15 yoffset xIntensity*-2
            ease 0.15 yoffset 0
            ease 0.15 yoffset xIntensity*-2
            ease 0.15 yoffset 0
        repeat

transform hoppies(xIntensity=2.5):
    matrixtransform RotateMatrix(0.0, 0.0, 0)
    block:
        parallel:
            pause 0.1
            ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, -xIntensity)
            pause 0.1
            ease 0.2 matrixtransform RotateMatrix(0.0, 0.0, xIntensity)
        parallel:
            ease 0.15 yoffset xIntensity*-2
            ease 0.15 yoffset 0
            ease 0.15 yoffset xIntensity*-2
            ease 0.15 yoffset 0
        repeat

transform giggle(xIntensity=0.1):
    yzoom 1.0
    xzoom 1.0
    ease 0.125 xzoom (1 + xIntensity) yzoom (1 - xIntensity)
    ease 0.125 yzoom 1.0 xzoom 1.0
    repeat 2

transform appearBlack(shading="#bbb4ff",t=0.5):
    matrixcolor TintMatrix(shading)*BrightnessMatrix(-1)
    blur 20
    alpha 0
    ease t blur 0 alpha 1
    ease t*0.5 matrixcolor TintMatrix(shading)*BrightnessMatrix(0)
    matrixcolor TintMatrix(shading)
# ------------------------------------------------------------------------ ENTER
transform enterFromLeftDelay(x=0.5,t=0.5,dTime=0.01):
    xcenter -0.5
    pause dTime
    ease t xcenter x

transform enterFromRightDelay(x=0.5,t=0.5,dTime=0.01):
    xcenter 1.5
    pause dTime
    ease t xcenter x

transform enterFromLeft(x=0.5,t=0.5):
    xcenter -0.5
    ease t xcenter x

transform enterFromRight(x=0.5,t=0.5):
    xcenter 1.5
    ease t xcenter x

# ------------------------------------------------------------------------- FLIP
transform flipped:
    matrixtransform rotated(y=180)

transform unFlipped:
    matrixtransform rotated()

transform flipChar(tSpeed = 0.5):
    matrixtransform rotated()
    ease tSpeed matrixtransform RotateMatrix(0,180,0)

transform unflipChar(tSpeed = 0.5):
    matrixtransform RotateMatrix(0,180,0)
    ease tSpeed matrixtransform RotateMatrix(0,0,0)

transform flipCharDelayed(xDelay = 0.5,tSpeed = 0.5):
    matrixtransform RotateMatrix(0,0,0)
    pause xDelay
    ease tSpeed matrixtransform RotateMatrix(0,180,0)

transform unflipCharDelayed(xDelay = 0.5,tSpeed = 0.5):
    matrixtransform RotateMatrix(0,180,0)
    pause xDelay
    ease tSpeed matrixtransform RotateMatrix(0,0,0)

# ------------------------------------------------------------------------- SPIN
transform spin(tSpeed = 0.6, tSpins = 1):
    matrixtransform RotateMatrix(0,0,0)
    ease tSpeed matrixtransform RotateMatrix(0,360*tSpins,0)

transform spinFlip(tSpeed = 0.6, tSpins = 1):
    matrixtransform RotateMatrix(0,180,0)
    ease tSpeed matrixtransform RotateMatrix(0,180+360*tSpins,0)

# ------------------------------------------------------------------------ FLOAT
transform idleFloat(tSpeed = 2.0, tOffset = 10):
    ease tSpeed*0.5 yoffset tOffset
    block:
        ease tSpeed yoffset -tOffset
        ease tSpeed yoffset tOffset
        repeat

# ------------------------------------------------------------------------- TINT
transform tintChar(xTint="#ffffff",yTint="#ffffff",tSpeed=0.5):
    matrixcolor TintMatrix(xTint)
    ease tSpeed matrixcolor TintMatrix(yTint)

# ----------------------------------------------------------------------- SQUISH
transform startledSquish:
    xzoom 1.1 yzoom 0.9
    ease 0.15 xzoom .9 yzoom 1.1

    ease 0.15 xzoom 1 yzoom 1

transform hypersquish:
    ease 0.2 xzoom 1.1 yzoom 0.9
    ease 0.2 xzoom .9 yzoom 1.1
    repeat

# ------------------------------------------------------------------------- JUMP
transform jumpSquish(xPower = 0.2,xHeight = 200, tSpeed = 0.4):
    parallel:
        ease tSpeed*0.5 yoffset int(xHeight*.1)
        ease tSpeed yoffset -xHeight
        pause tSpeed*0.25
        ease tSpeed yoffset 0
    parallel:
        ease tSpeed*0.5 xzoom 1 + xPower yzoom 1 - xPower
        ease tSpeed*0.25 xzoom 1 - xPower yzoom 1 + xPower
        ease tSpeed xzoom 1 yzoom 1
        pause tSpeed*0.75
        ease tSpeed*0.25 xzoom 1 + xPower yzoom 1 - xPower
        ease tSpeed*0.5 xzoom 1 yzoom 1

# -------------------------------------------------------------------------- NOD
transform nodding(tSpeed = 0.3, tNodAmt = 10, tHeight = 20):
    matrixtransform RotateMatrix(0,0,0)
    yoffset 0
    ease tSpeed matrixtransform RotateMatrix(0,0,tNodAmt) yoffset tHeight
    ease tSpeed matrixtransform RotateMatrix(0,0,0) yoffset 0
    pause tSpeed

transform noddingFlip(tSpeed = 0.3, tNodAmt = -10, tHeight = 20):
    matrixtransform RotateMatrix(0,180,0)
    yoffset 0
    ease tSpeed matrixtransform RotateMatrix(0,180,tNodAmt) yoffset tHeight
    ease tSpeed matrixtransform RotateMatrix(0,180,0) yoffset 0
