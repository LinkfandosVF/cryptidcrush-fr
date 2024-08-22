define June = Character("June", image = "june", callback = Bleep,ctc="end_of_msg", cb_id = "4D", who_color = "#ed822b")
define NVL_June = Character("June", image = "june", callback = Bleep,ctc="end_of_msg", cb_id = "4D", who_color = "#ed822b",kind=nvl)

default June_State = { "mouth": 0}

default June_Default = { "mouth": 0}

#nvl_mode-----------------------
image side june:
    matrixcolor ColorizeMatrix("#1c1f4d","#f5824b")
    zoom 0.15
    yalign 1.0
    xalign 0.8
    "images/Characters/Minis/june_mini.webp"
    block:
        rotate 5
        pause 0.9
        rotate -5
        pause 0.9
        repeat
#june-------------------------------------------------

layeredimage june:
    xanchor 0.5
    zoom 0.14
    ycenter 1.0
    always:
        "images/Characters/June/june_base.webp"

    always:
        "juneblink"

    if June_State['mouth'] >= 1:
        "images/Characters/June/june_smile.webp"

image juneblink:
    alpha 0
    "images/Characters/June/june_blink.webp"
    choice:
        pause 2.0
    choice:
        pause 6.0
    choice:
        pause 0.5

    alpha 1
    pause 0.2
    repeat
