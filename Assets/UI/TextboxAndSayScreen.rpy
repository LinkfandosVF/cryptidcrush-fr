init offset = -1
################################################################################
## In-game screens
################################################################################

# This label in Renpy-Version\renpy\common\00keymap.rpy should have renpy stop sound
#label _hide_windows:
#    ...
#    python:
#        renpy.sound.stop('blip')
#        _windows_hidden = True
#        ...

init python:
    def toggleQuickMenu(blockRollback=False):
        global quick_menu
        global quicker_menu_show

        quick_menu = not quick_menu

        if blockRollback : renpy.block_rollback()

        if renpy.get_screen("quicker_menu"):
            quicker_menu_show = False
            renpy.hide_screen("quicker_menu")

## Say screen ##################################################################
screen say(who, what):
    style_prefix "say"
    zorder 1

    #Side Image
    #add SideImage() xcenter 0.3 yanchor 1.0 ypos 0.78

    window:
        id "window"

        if who is not None and who is not "":

            window:

                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    if quick_menu:
        use quickmenu

    # timer 0.1 action Insert_Save_Function repeat False #(AUTO SAVES)

screen quickmenu():
    zorder 100
    if not quicker_menu_show:
        imagebutton at pause_button_tf:
            idle "pause_button"
            hover "pause_button"
            selected_idle "pause_button"
            selected_hover "pause_button"
            selected quicker_menu_show

            alt "Quick Menu"
            hover_sound audio.selecthover

            action [Show('quicker_menu'), SetVariable("quicker_menu_show",True), Show('quicker_menu_hide')]

            activate_sound renpy.random.choice(selectList)

    #Back Button
    imagebutton at backButton_tf:
        insensitive "backButton"
        idle "backButton"
        hover "backButton"
        alt "Back"
        action Rollback()
        hover_sound audio.selecthover

    #Fast Forward Button
    imagebutton at ffButton_tf:
        insensitive "ffButton"
        idle "ffButton"
        hover "ffButton"
        alt "Fastforward"
        action Skip(fast=False, confirm=False)
        hover_sound audio.selecthover


#style block2_multiplue2_say_window:

screen multiple_say(who, what,multiple):
    style_prefix "say"

    #Side Image
    #add SideImage() xcenter 0.3 yanchor 1.0 ypos 0.78

    if multiple[0] == 1:
        window:
            id "window"

            if (who is not None and who is not ""):

                window:
                    id "namebox"
                    style "namebox"
                    text who id "who"

            text what id "what":
                xmaximum 400


    else:

        #$what = what + " (" + who + ")"
        text what id "what":
            xpos 285 + 400 + 5
            ypos 515 #+ 20
            xmaximum 400
            color globals()[who].who_args['color']


    if quick_menu:
        use quickmenu

init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:

    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

init python:
    style.window.background = ConditionSwitch(
        "sframe == 1", Image("gui/textbox.webp", xalign=0.5, yalign=1.0),
        "sframe == 2", Image("gui/textbox.webp", xalign=0.5, yalign=1.0),
        )

image ccnamebox:
    xzoom 0.4
    yzoom 0.2
    yalign 0.18
    xalign gui.name_xalign

style namebox:
    xpos gui.name_xpos - 5
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos + 53
    ysize gui.namebox_height
    padding gui.namebox_borders.padding

    background "ccnamebox"

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    line_spacing 1.5
    line_leading 1.5

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos + 5


## Input screen ################################################################
screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

default hoveredChoice = ""

screen choice(items):
    zorder 101
    $displaymenu = True
    style_prefix "choice"

    vbox:
        python:
            choice_bg = ["_default", "_brawn",   "_brains", "_hustle", "_guts",   "_charm", "_occult"]
            choice_c  = ["#33ff96", "#ff5342", "#a1fffc", "#a7ff78", "#ff8941", "#ED2A82","#b480ff"]
            cNum = len(choice_bg)
        for i in items:
            hbox:
                spacing -60
                box_reverse True
                xcenter 0.5

                python:
                    cNum+=1
                    if cNum >= 1:#len(choice_bg):
                        cNum = 0

                    if " {image=end_of_msg}" in i.caption:
                        i.caption = i.caption.replace(" {image=end_of_msg}", "")

                if "**Brawn" in i.caption:
                    $i.caption = i.caption.replace("**Brawn", "")
                    add "images/Characters/Atlas/Battle/Atlas_Icon_Default.webp":
                        xysize (60,60)
                        xoffset 100
                        yoffset -15
                        
                textbutton i.caption at hovergrow:
                    action [SetVariable("displaymenu",False),i.action]
                    hover_sound audio.selecthover
                    activate_sound renpy.random.choice(selectList)
                    text_idle_color choice_c[cNum]
                    hover_background "choice_hover" + choice_bg[cNum]



transform hovergrow:
    xcenter 0.5
    ycenter 0.5
    on idle:
        ease 0.15 zoom 1.0
    on hover:
        ease 0.15 zoom 1.1
    on insensitive:
        zoom 1.0


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True

style choice_vbox is vbox

image choice_idle:
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_default:
    matrixcolor ColorizeMatrix("#33ff96","#33ff96")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

#"#a1fffc", "#a7ff78", "#ff8941", "#ED2A82","#b480ff"]
image choice_hover_brawn:
    matrixcolor ColorizeMatrix("#ff5342","#ff5342")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_brains:
    matrixcolor ColorizeMatrix("#a1fffc","#a1fffc")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_hustle:
    matrixcolor ColorizeMatrix("#a7ff78","#a7ff78")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_guts:
    matrixcolor ColorizeMatrix("#ff8941","#ff8941")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_charm:
    matrixcolor ColorizeMatrix("#ED2A82","#ED2A82")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

image choice_hover_occult:
    matrixcolor ColorizeMatrix("#b480ff","#b480ff")
    xcenter 0.5
    ycenter 0.5
    zoom 1.3
    "gui/button/choice_idle_background.png"

style choice_button is button


style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5
    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    background "choice_idle"
    hover_background "choice_hover"

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.
image backButton:
    "gui/quickmenu/Back_Button.webp"
    zoom 0.54

image ffButton:
    "gui/quickmenu/FF_Button.webp"
    zoom 0.5

transform backButton_tf:
    xcenter 0.24
    ycenter 0.96
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
    on insensitive:
        matrixcolor ColorizeMatrix("#292929", "#7d7d7d")
    on hover:
        matrixcolor ColorizeMatrix("#00376a", "#529ce9")

transform ffButton_tf:
    xcenter 0.8
    ycenter 0.955

    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
    on insensitive:
        matrixcolor ColorizeMatrix("#292929", "#7d7d7d")
    on hover:
        matrixcolor ColorizeMatrix("#28006a", "#9775f7")
        pause 0.05
        choice:
            xoffset 2
            yoffset 0
        choice:
            xoffset 0
            yoffset 2
        choice:
            xoffset -2
            yoffset -2
        choice:
            xoffset 2
            yoffset 2
        choice:
            xoffset -2
            yoffset 0
        choice:
            xoffset 0
            yoffset -2
        choice:
            xoffset 0
            yoffset 0
        repeat


default quicker_menu_show = False
default game_menu_show = False

image MenuSpace:
    xalign 0.0
    yalign 1.01
    zoom 0.63
    alpha 0.75
    "gui/quickmenu/MenuSpace.webp"

image MenuSpaceR:
    alpha 0.75
    zoom 0.7
    xalign 1.01
    yalign 1.01
    "gui/quickmenu/MenuSpaceRight.webp"

image pause_button:
    "gui/quickmenu/Pause_Button.webp"
    zoom 0.3

transform pause_button_tf:
    xcenter 0.03
    ycenter 0.68
    on idle:
        matrixcolor ColorizeMatrix("#000000", "#a0dda8")
    on hover:
        matrixcolor ColorizeMatrix("#000000", "#bfff38")
    on selected_idle:
        matrixcolor ColorizeMatrix("#000000", "#8b79ff")
    on selected_hover:
        matrixcolor ColorizeMatrix("#000000", "#6d41ff")

transform disappear_on_hide:
    on hide:
        alpha 1
        pause 0.3
        ease 0.3 alpha 0

# QUICK MENU -------------------------------------------------------------------
screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 101

    # if quick_menu:
    #     imagebutton at pause_button_tf:
    #         idle "pause_button"
    #         hover "pause_button"
    #         selected_idle "pause_button"
    #         selected_hover "pause_button"
    #         selected quicker_menu_show
    #
    #         alt "Quick Menu"
    #         hover_sound audio.selecthover
    #
    #         action [ToggleScreen('quicker_menu'), ToggleVariable("quicker_menu_show")]
    #
    #         activate_sound renpy.random.choice(selectList)
    #
    #     #Back Button
    #     imagebutton at backButton_tf:
    #         insensitive "backButton"
    #         idle "backButton"
    #         hover "backButton"
    #         alt "Back"
    #         action Rollback()
    #         hover_sound audio.selecthover
    #
    #     #Fast Forward Button
    #     imagebutton at ffButton_tf:
    #         insensitive "ffButton"
    #         idle "ffButton"
    #         hover "ffButton"
    #         alt "Fastforward"
    #         action Skip(fast=False, confirm=False)
    #         hover_sound audio.selecthover



#HOME
image home_button:
    "gui/quickmenu/HOME_MenuIcon.webp"
    zoom 0.33

transform home_button_tf:
    xcenter 0.033
    ycenter 0.78
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        rotate 0
    on hover:
        matrixcolor ColorizeMatrix("#006a0e", "#52e965")
        ease 0.8 rotate 8
        ease 0.8 rotate -8
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#fff", "#000") # Not sure this actually needed but doesn't hurt I figure
        rotate 0

#History
image history_button:
    "gui/quickmenu/SCRIPT_MenuIcon.webp"
    zoom 0.3

transform history_button_tf:
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        zoom 1.0
    on hover:
        matrixcolor ColorizeMatrix("#4f0b42", "#ff93dd")
        ease 0.85 zoom 1.05
        ease 0.85 zoom 1.0
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#fff", "#000")
        zoom 1.0

#Character Bio
image char_button:
    "gui/quickmenu/CHARACTERS_MenuIcon.webp"
    zoom 0.3

transform char_button_tf:
    xcenter 0.1
    ycenter 0.75
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        xzoom 1.0 yzoom 1.0
    on hover:
        matrixcolor ColorizeMatrix("#00376a", "#52e5e9")
        ease 1.0 yzoom 1.23 xzoom 0.8333
        ease 1.0 xzoom 1.0 yzoom 1.0
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#fff", "#000")
        zoom 1.0

#Save
image save_button:
    "gui/quickmenu/SAVEnLOAD_MenuIcon.webp"
    zoom 0.37

transform save_button_tf:
    xcenter 0.04
    ycenter 0.9
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        xzoom 1.0 yzoom 1.0
    on hover:
        matrixcolor ColorizeMatrix("#3e2254", "#bb67ff")
        ease 0.75 xzoom 1.135 yzoom 0.864
        ease 0.85 xzoom 1.0 yzoom 1.0
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#fff", "#000")
        xzoom 1.0 yzoom 1.0

#Settings
image settings_button_idle:
    "gui/quickmenu/SETTINGS_MenuIcon.webp"
    zoom 0.4

image settings_button_hover:
    "gui/quickmenu/SETTINGS_SPIN_MenuIcon.webp"
    zoom 0.4

transform settings_button_tf:
    xcenter 0.18
    ycenter 0.88
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        rotate 0
    on hover:
        matrixcolor ColorizeMatrix("#543122", "#ff8941")
        rotate 0
        linear 2.0 rotate 360
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#fff", "#000")
        rotate 0

#Gallery
image gallery_button:
    "gui/quickmenu/GALLERY_MenuIcon.webp"
    zoom 0.3

transform gallery_button_tf:
    xcenter 0.115
    ycenter 0.88
    on idle:
        matrixcolor ColorizeMatrix("#295763", "#a0dda8")
        blur 0
        zoom 1.0
    on hover:
        matrixcolor ColorizeMatrix("#156751", "#10FCBB")
        blur 2
        ease 0.9 zoom 1.166 blur 0
        ease 0.9 zoom 1.0 blur 2
        repeat
    on insensitive:
        matrixcolor ColorizeMatrix("#b0b0b0", "#303030")
        blur 0
        zoom 1.0

image menu_space_line:

    xalign 1.05
    yanchor 0.5
    ypos 600
    yzoom 0.45
    xzoom 1.05
    "gui/quickmenu/Menu_Space_Line.webp"

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")


# QUICKER MENU -----------------------------------------------------------------
define timeSlot = 3
default timeText = "12:00AM"
default songText = "Cryptid Crush"
default musicNote = 0

image song music note:
    zoom 0.15
    yalign 0.5
    xanchor 0.5
    xpos 0.4

    perspective True

    ConditionSwitch(
        "musicNote <= 0", "gui/quickmenu/Music/Music_Indicator.webp",
        "musicNote == 1", "gui/quickmenu/Music/Music_Indicator_Agitated.webp",
        "musicNote == 2", "gui/quickmenu/Music/Music_Indicator_AMOGUS.webp",
        "musicNote == 3", "gui/quickmenu/Music/Music_Indicator_Asleep.webp",
        "musicNote == 4", "gui/quickmenu/Music/Music_Indicator_Cow.webp",
        "musicNote == 5", "gui/quickmenu/Music/Music_Indicator_Depressed.webp",
        "musicNote == 6", "gui/quickmenu/Music/Music_Indicator_Happy.webp",
        "musicNote == 7", "gui/quickmenu/Music/Music_Indicator_Hyped.webp",
        "musicNote == 8", "gui/quickmenu/Music/Music_Indicator_LodosBinted.webp",
        "musicNote == 9", "gui/quickmenu/Music/Music_Indicator_MadhouseMusic.webp",
        "musicNote == 10", "gui/quickmenu/Music/Music_Indicator_NotSansIpROMISE.webp",
        "musicNote == 11", "gui/quickmenu/Music/Music_Indicator_Pensive.webp",
        "musicNote == 12", "gui/quickmenu/Music/Music_Indicator_Spooked.webp",
        "musicNote == 13", "gui/quickmenu/Music/Music_Indicator_Wha.webp",
        "musicNote == 14", "gui/quickmenu/Music/Music_Indicator_Wink.webp",
        "musicNote >= 15", "gui/quickmenu/Music/Music_Indicator_Wink star.webp")

    # block:
    #     matrixtransform rotated()
    #     linear 3.0 matrixtransform rotated(y=360)
    #     repeat

    # parallel:
    #     ease 1.15 yoffset -13
    #     block:
    #         matrixcolor ColorizeMatrix("#000000",PCnameColor)
    #         ease 2.3 yoffset 7
    #         ease 2.3 yoffset -13
    #         repeat
    # parallel:
    #     matrixtransform rotated()
    #     pause 1.0
    #     block:
    #         matrixtransform rotated()
    #         pause 1.6
    #         ease 1.4 matrixtransform rotated(y=360)
    #         pause 1.6
    #         repeat

transform menuSpace_tf:
    on show:
        alpha 0
        choice:
            ease 0.25 alpha 1
        choice:
            ease 0.25 alpha 1

    on hide:
        alpha 1
        pause 0.2
        ease 0.25 alpha 0

transform quicker_rightblock_tf1:
    on show:
        xoffset 300
        pause 0.2
        ease 0.4 xoffset 0

    on hide:
        xoffset 0
        yoffset 0
        ease 0.6 yoffset 300

transform quicker_rightblock_tf2:
    on show:
        xoffset 300
        pause 0.3
        ease 0.4 xoffset 0

    on hide:
        xoffset 0
        yoffset 0
        ease 0.5 yoffset 300

transform quicker_rightblock_tf3:
    on show:
        xoffset 300
        pause 0.4
        ease 0.4 xoffset 0

    on hide:
        xoffset 0
        yoffset 0
        ease 0.4 yoffset 300

transform quicker_leftblock_tf2:
    on show:
        yoffset 300
        pause 0.3
        ease 0.4 yoffset 0

    on hide:
        xoffset 0
        yoffset 0
        ease 0.5 xoffset -300

transform quicker_leftblock_tf1:
    on show:
        yoffset 300
        pause 0.2
        ease 0.4 yoffset 0

    on hide:
        xoffset 0
        yoffset 0
        ease 0.6 xoffset -300

default quickerMenuTime = 0
screen quicker_menu():

    use diceChangingMenu()

    #if not renpy.get_screen("song_notif"):
    #    use song_notif(0,True)

    zorder 100

    # Right Block
    frame at menuSpace_tf:
        background "MenuSpaceR"
        xalign 1.01
        yalign 1.01


    frame at quicker_rightblock_tf1:
        background None
        #Karma
        text "[pc_karma]/" + str(diceBot.maxKarma):
            xalign 1.0
            yanchor 1.0
            xpos 1185
            ypos 570

            color getPCNameColor()
            text_align 1.0
            size 55
            font "fonts/typwrng.ttf"

        #Karma Icon
        add "gui/text_icons/KARMA_StatIcon.webp":
            xpos 1265
            ypos 525
            xanchor 1.0
            yanchor 0.5
            zoom 0.27
            matrixcolor ColorizeMatrix("#000000", getPCNameColor())

    frame at quicker_rightblock_tf2:
        background None
        text OutputPCGradient(timeText):
            xanchor 1.0
            yanchor 0.0
            xpos 1270
            ypos 610
            size 45
            text_align 1.0
            font "fonts/MelmaCracked.ttf"



        add "menu_space_line":
            matrixcolor ColorizeMatrix(getPCNameColor(False), getPCNameColor(True))

        #Dice Name
        text OutputPCGradient(str(diceBot.dieName)):
            xalign 1.0
            yanchor 0.0
            xpos 1270
            ypos 580

            color getPCNameColor()
            size 23 - len(diceBot.dieName)*0.1
            text_align 1.0

    hbox at quicker_rightblock_tf3:
        xanchor 1.0
        xpos 1270
        ypos 710
        yanchor 1.0


        text songText: #"{image=song music note}" +
            color getPCNameColor() # "#a0dda8"


            size 18 - len(songText)*0.1
            xmaximum 170
            line_spacing 2
            text_align 1.0
            font "fonts/typwrng.ttf"

        add "song music note" at idleFloat(1.3,5):
            matrixcolor ColorizeMatrix("#000000",PCnameColor)

    #Left Block
    frame at menuSpace_tf:
        background "MenuSpace"

    frame at quicker_leftblock_tf1:
        background None
        #Home Button
        imagebutton at home_button_tf:
            focus_mask True
            idle "home_button"
            alt "Home"
            action [Stop("blip"),MainMenu()]
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #History Button
        imagebutton at history_button_tf:
            focus_mask True
            idle "history_button"
            xcenter 0.17
            ycenter 0.765
            alt "History"
            action [Stop("blip"),ShowMenu('history')] #MainMenu()
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #Character Sheet Button
        imagebutton at char_button_tf:
            focus_mask True
            idle "char_button"
            alt "Character Sheets"
            action [SensitiveIf(False),Stop("blip"),ShowMenu('history')] #MainMenu()
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

    frame at quicker_leftblock_tf2:
        background None
        #Save
        imagebutton at save_button_tf:
            focus_mask True
            idle "save_button"
            alt "Save"
            action [Stop("blip"),ShowMenu('save')] #MainMenu()
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #Settings
        imagebutton at settings_button_tf:
            focus_mask True
            idle "settings_button_idle"
            hover "settings_button_hover"
            alt "Settings"
            action [Stop("blip"),ShowMenu('preferences')]
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #Gallery
        imagebutton at gallery_button_tf:
            focus_mask True
            idle "gallery_button"
            alt "Settings"
            #action [Stop("blip"),ShowMenu('Gallery')]
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)


    imagebutton at pause_button_tf, disappear_on_hide:
        idle "pause_button"
        hover "pause_button"
        selected_idle "pause_button"
        selected_hover "pause_button"
        selected quicker_menu_show

        alt "Quick Menu"
        hover_sound audio.selecthover

        action [SetVariable("quickerMenuTime",10), Hide('quicker_menu'), Hide('quicker_menu_hide'), ToggleVariable("quicker_menu_show")]

        activate_sound renpy.random.choice(selectList)

screen quicker_menu_hide():
    timer 10.0 action [SetVariable("quicker_menu_show",False),Hide("quicker_menu", nwDissolve(0.3)), Hide("quicker_menu_hide")]

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
# screen quick_menu():
#     variant "touch"
#
#     zorder 100
#
#     if quick_menu:
#
#         hbox:
#             style_prefix "quick"
#
#             xalign 0.5
#             yalign 1.0
#
#             textbutton _("Back") action Rollback()
#             textbutton _("Auto") action Preference("auto-forward", "toggle")
#             textbutton _("Menu") action ShowMenu()
