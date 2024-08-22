init offset = -1

################################################################################
## Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

#081820
#346856
#88c070
#e0f8d0

default persistent.gm_curPal = "default"
init -2 python:
    persistent.gm_curPal = "default"
    # ------------ [Dark,      Light,     Accent1,   Accent2,   TextDark,  TextLight, TextAccent, BG]
    gm_palDict = {# 0          1          2          3          4          5          6           7
        "default": ["#120d29", "#c8b1ff", "#80f9ca", "#e880f9", "#545565", "#80f9ca", "#80f9ca", "#3c3d4d"],
        "madhouse": ["#0d0203", "#acffb5", "#58fe69", "#ff3951", "#607458", "#ff3951", "#ff3951", "#151d18"] }

style gm_darkbutton:
    idle_color gm_palDict[persistent.gm_curPal][4]
    hover_color gm_palDict[persistent.gm_curPal][6]

transform nav_button_dark:
    on idle:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    on insensitive:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])
    on hover:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][renpy.random.randint(2,3)],gm_palDict[persistent.gm_curPal][0])

transform nav_button_light:
    on idle:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])
    on insensitive:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    on hover:
        matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][renpy.random.randint(2,3)],gm_palDict[persistent.gm_curPal][0])

transform set_zoom(xZoom=1.0):
    zoom xZoom

layeredimage nav_history:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/SCRIPT_MenuIcon.webp" at set_zoom(0.4)

layeredimage nav_save:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/SAVEnLOAD_MenuIcon.webp" at set_zoom(0.4)

layeredimage nav_load:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/SAVEnLOAD_MenuIcon.webp" at set_zoom(-0.4)

layeredimage nav_pref:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/SETTINGS_MenuIcon.webp" at set_zoom(0.4)

layeredimage nav_home:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/HOME_MenuIcon.webp" at set_zoom(0.4)

layeredimage nav_bios:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/CHARACTERS_MenuIcon.webp" at set_zoom(0.4)

layeredimage nav_home:
    always:
        "gui/MenuBGs/cc menu square.png"

    always:
        "gui/quickmenu/HOME_MenuIcon.webp" at set_zoom(0.4)

image nav_quit:
    "gui/MenuBGs/cc menu exit game button.png"

screen navigation():
    hbox:
        xpos 101
        yanchor 1.0
        ypos 694
        style_prefix "navigation"

        spacing 22

        # if main_menu:
        #     textbutton _("Start"):
        #         action Start()
        #         text_idle_color gm_palDict[persistent.gm_curPal][4]
        #         text_hover_color gm_palDict[persistent.gm_curPal][6]
        if not main_menu:
            #imagebutton at nav_button_dark:
            #    idle  "nav_history"

            textbutton "Historique":
                action ShowMenu("history")

                hover_sound audio.selecthover
                activate_sound renpy.random.choice(selectList)

            #imagebutton at nav_button_dark:
            #    idle "nav_save"

            textbutton "Sauv.":
                action ShowMenu("save")

                hover_sound audio.selecthover
                activate_sound renpy.random.choice(selectList)

        #imagebutton at nav_button_light:
        #    idle "nav_load"

        textbutton "Charger":
            action ShowMenu("load")

            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #imagebutton at nav_button_dark:
        #    idle "nav_pref"

        textbutton "Préférences":
            action ShowMenu("preferences")

            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        #imagebutton at nav_button_dark:
        #    idle "nav_bios"

        textbutton "A propos":
            action ShowMenu("about")

            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)

        if gameVersion >= 3:
            textbutton "Gallery" action ShowMenu("Gallery_screen"):
                hover_sound audio.selecthover
                activate_sound renpy.random.choice(selectList)

        if _in_replay:
            textbutton _("End Replay"):
                action EndReplay(confirm=True)
                text_idle_color gm_palDict[persistent.gm_curPal][4]
                text_hover_color gm_palDict[persistent.gm_curPal][6]

        elif not main_menu:
            #imagebutton at nav_button_dark:
            #    idle "nav_home"

            textbutton "Main Menu":
                action MainMenu()

                hover_sound audio.selecthover
                activate_sound renpy.random.choice(selectList)

screen extras_navigation():
    frame:
        xpos gui.navigation_xpos
        yalign 0.7
        background "pref_Scrap_2"
        vbox:
            style_prefix "navigation"

            spacing gui.navigation_spacing

            textbutton _("About") action ShowMenu("about")

            #textbutton _("Preferences") action ShowMenu("preferences")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Controls") action ShowMenu("help")

            #textbutton _("Album") action ShowMenu("album")
            #textbutton _("Characters") action ShowMenu("characters")
            #textbutton _("Music") action ShowMenu("Name")
            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)

            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()

            textbutton _("Less") action ShowMenu("load")

style navigation_button is gui_button
style navigation_button_text is gui_button_text
style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.
image gameMenuBase:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])*BrightnessMatrix(0.15)
    xysize (1280,720)
    "gui/MenuBGs/cc menu base.png"

image gameMenuBase2:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    xysize (1280,720)
    "gui/MenuBGs/cc menu.png"

image gameMenu1:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    xysize (1280,720)
    "gui/MenuBGs/cc menu 1.png"

image gameMenu3:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    xysize (1280,720)
    "gui/MenuBGs/cc menu 3.png"

image gameMenu4:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][1],gm_palDict[persistent.gm_curPal][0])
    xysize (1280,720)
    yoffset -50

    "gui/MenuBGs/cc menu 4.png"

image gameMenu5:
    xysize (1280,720)
    block:
        "gui/MenuBGs/cc menu 5 - static 1.png"
        matrixcolor TintMatrix(gm_palDict[persistent.gm_curPal][2])
        choice:
            pause 0.5
        choice:
            pause 1.0
        choice:
            pause 2.0
        choice:
            pause 8.0
        choice:
            pause 4.0



        parallel:
            pause 0.15
            "gui/MenuBGs/cc menu 5 - static 2.png"
            pause 0.15
            "gui/MenuBGs/cc menu 5 - static 3.png"
            pause 0.15
            "gui/MenuBGs/cc menu 5 - static 4.png"
            pause 0.15
            "gui/MenuBGs/cc menu 5 - static 5.png"
            pause 0.15
        parallel:
            ease 0.15 matrixcolor TintMatrix(gm_palDict[persistent.gm_curPal][3])
            pause 0.45
            ease 0.15 matrixcolor TintMatrix(gm_palDict[persistent.gm_curPal][2])
        repeat

image gameMenu6:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])
    xysize (1280,720)
    "gui/MenuBGs/cc menu 6.png"

image holecirc:
    matrixcolor TintMatrix(gm_palDict[persistent.gm_curPal][2])
    #"Unorganized Assets/CircleSwoosh.png"
    xcenter 0.975
    ycenter 0.775
    zoom 0.5
    block:
        matrixtransform RotateMatrix(0,0,0)
        ease 8.0 matrixtransform RotateMatrix(0,0,360)

        pause 1.0
        ease 8.0 matrixtransform RotateMatrix(0,0,0)
        pause 1.0
        repeat

image holecirc2:
    matrixcolor TintMatrix(gm_palDict[persistent.gm_curPal][3])
    #"Unorganized Assets/CircleSwoosh.png"
    xcenter 0.975
    ycenter 0.775
    zoom 0.5
    block:
        matrixtransform RotateMatrix(0,0,360+22.5)
        ease 8.0 matrixtransform RotateMatrix(0,0,0+22.5)
        pause 1.0

        ease 8.0matrixtransform RotateMatrix(0,0,360+22.5)
        pause 1.0
        repeat

image spincirc:
    contains:
        "holecirc"

    contains:
        "holecirc2"
        zoom 0.7

    contains:
        "holecirc"
        zoom 0.5

    contains:
        "holecirc2"
        zoom 0.3

screen gm_title(title):
    zorder 400
    label title :
        xanchor 0.0
        xpos 0.19
        ycenter 0.73

        text_color gm_palDict[persistent.gm_curPal][5]
        text_size 50

image gMenuPronouns:
    xpos 195
    ypos 40
    ConditionSwitch(
        PCthey == "they","gui/MenuBGs/they pronoun.png",
        PCthey == "she","gui/MenuBGs/she pronoun.png",
        True,"gui/MenuBGs/he pronoun.png")


    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])

image gMenuVoice_Placeholder:
    xpos 150
    ypos 40
    "gui/MenuBGs/cc voice placeholder.png"

    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"
    add "gameMenuBase":
        alpha 0.6

    use gm_title(title)

    #if not (title in ["About", "History", "Controls"]):
        #add "spincirc"
    add "gameMenuBase2":
        alpha 0.6
    # if title in ["About", "History", "Controls"]:
    #     add "About_Page_Paper"

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True
                        transclude

                else:
                    transclude

    #add "gameMenu1"
    use navigation
    # if title in ["About", "Controls"]:
    #     use extras_navigation
    # else:
    #     use navigation

    add "gameMenu3"
    add "gMenuVoice_Placeholder"
    add "gMenuPronouns"

    # TODO Make so that name doesn't go off the screen at max length :)
    label (PCname + " " + PClastname):
        xanchor 0.0
        xpos 20
        ycenter 148
        text_color gm_palDict[persistent.gm_curPal][6]
        text_size 30 - (len(PCname) + len(PClastname))*0.8

    # TODO Fix 0. Robyn Creation.rpy to not do the quiz exactly the same twice you dumb bastard

    use game_menu_stats_toggle

    add "gameMenu5"

    add "gameMenu4"
    textbutton _("Exit Menu"):
        #action Quit(confirm=not main_menu)
        text_idle_color gm_palDict[persistent.gm_curPal][4]
        text_hover_color gm_palDict[persistent.gm_curPal][6]

        text_size 30
        xalign 1.0
        xoffset -30
        ycenter 0.91
        yoffset -50

        action Return()
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)

    add "gameMenu6"

    label songText:
        xpos 950
        yalign 0
        yoffset -47
        text_color gm_palDict[persistent.gm_curPal][1]
        text_size 23

    label timeText:
        xpos 530
        yalign 0
        yoffset -47
        text_color gm_palDict[persistent.gm_curPal][1]
        text_size 23

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


    imagebutton at nav_button_light:
        yalign 1.0
        xpos 10
        yoffset -10

        action Return()
        idle "gui/MenuBGs/cc menu exit game button.png"

        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)



transform gm_stats_open(w=100,h=100,t=1.0):
    crop (0,0,w,0)
    ease t crop (0,0,w,h)


transform gm_stats_close(w=100,h=100,t=1.0):
    crop (0,0,w,h)
    ease t crop (0,0,w,0)

    on show:
        crop (0,0,w,0)

define gmIsOpen = False
define playGmOpenAnim = 0
screen game_menu_stats_toggle:
    zorder 5000
    default openTime = 0.4

    vbox:
        xpos 20
        ypos 163
        yanchor 0
        spacing 0
        frame:
            background "game_stats_bg"
            if gmIsOpen:
                at gm_stats_open(w=197,h=381,t=openTime*playGmOpenAnim)
            else:
                at gm_stats_close(w=197,h=381,t=openTime*playGmOpenAnim)
            vbox:
                spacing 0
                for x in range(len(PC_Stats.getRawStats()[0])):
                    hbox:
                        spacing 100
                        text PC_Stats.getRawStats()[0][x]:
                            xanchor 0.0
                            yanchor 0.0
                            size 25
                            color gm_palDict[persistent.gm_curPal][0]

                        text PC_Stats.getRawStats()[1][x]:
                            xanchor 1.0
                            yanchor 0.0
                            size 25
                            color gm_palDict[persistent.gm_curPal][0]


        imagebutton:
            if gmIsOpen:
                at yoff_trans(sY=0,eY=-20,r=[3,1],t=openTime*playGmOpenAnim)
            else:
                at yoff_trans(sY=-20,eY=0,r=[3,1],t=openTime*playGmOpenAnim)
            xanchor -0.5
            idle "game_stats_button_bg"
            action [ToggleVariable('gmIsOpen'),SetVariable('playGmOpenAnim',1)]

        if playGmOpenAnim:
            timer 0.4 action SetVariable('playGmOpenAnim',0) repeat False

transform yoff_trans(sY=0,eY=0,r=[1,1],t=0):
    #yoffset sY
    ease t yoffset eY

transform off_delay(x=0,y=0,z=0,t=0,d=0):
    pause d
    camera_zoom(x=x,y=y,z=z,t=t)

image game_stats_bg:
    "gui/MenuBGs/cc menu 3 stats backdrop.png"
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])
    #matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][0])

image game_stats_button_bg:
    zoom 1.2
    "gui/MenuBGs/cc menu 3 stats backdrop toggle.png"
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][1])
    #matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][0],gm_palDict[persistent.gm_curPal][0])

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 170
    top_padding 20

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin -45
    right_margin 40
    top_margin 10
    bottom_margin 35

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screens

    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"


        vbox:
            xoffset 10

            label "[config.name!t]":
                text_color gm_palDict[persistent.gm_curPal][1]
            #text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "\n[gui.about!t]\n":
                    color gm_palDict[persistent.gm_curPal][1]

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]\n\n This game uses Kinetic Text Tags Created by {a=http://twitter.com/sodara9}Daniel Westfall{/a} <SoDaRa2595@gmail.com>"):
                color gm_palDict[persistent.gm_curPal][1]

## This is redefined in options.rpy to add text to the about screen.
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Load and Save screens #######################################################
screen save():

    tag menu

    use file_slots(_("Sauv."))

screen load():

    tag menu

    use file_slots(_("Charger"))

image save_load_BG1:
    xanchor 0.25
    yanchor 0.25
    xzoom 0.475
    yzoom 0.475
    "gui/MenuBGs/SaveMenuProps/Sticky1.png"

image save_load_BG2:
    xanchor 0.25
    yanchor 0.25
    xzoom 0.43
    yzoom 0.43
    "gui/MenuBGs/SaveMenuProps/Sticky2.png"

image save_load_BG3:
    xanchor 0.15
    yanchor 0.25
    xzoom 0.475
    yzoom 0.475
    "gui/MenuBGs/SaveMenuProps/Sticky3.png"

image save_load_BG4:
    xanchor 0.225
    yanchor 0.2
    xzoom 0.425
    yzoom 0.425
    "gui/MenuBGs/SaveMenuProps/Sticky6.png"

image save_pageNum_BG:
    alpha 0
    "gui/MenuBGs/setting_menu_scraps-01.webp"

image save_load_BG:
    "gui/MenuBGs/SaveMenuProps/cc menu save data - asset.png"

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Sauv. Auto"), quick=_("Sauv. Rapides"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            frame:
                xalign 0.4
                ycenter 0.0
                background "save_pageNum_BG"
                button:
                    style "page_label"

                    key_events True


                    action page_name_value.Toggle()

                    input:
                        style "page_label_text"
                        value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xcenter 0.4
                ypos 0.05

                yspacing 5
                xspacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        background "save_load_BG"
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xcenter 0.5 ycenter 0.5 xoffset 5

                        #text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("C'est vide.)):
                            #style "slot_time_text"
                        # text "Chapter 0": #FileSaveName(slot)
                        #     style "slot_name_text" ycenter -0.25

                        text FileTime(slot, format=_("{#file_time}%m/%d/%Y"), empty=_("C'est vide.")):
                            style "slot_time_text"
                            ycenter -0.26

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.4
                ycenter 0.9

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")

image pref_Scrap_1:
    "gui/MenuBGs/setting_menu_scraps-01.webp"
    xcenter 0.625
    yanchor 0.39
    ypos 0.1
    xzoom 1.0
    yzoom 1.0
    matrixcolor SaturationMatrix(0.3)*ColorizeMatrix("#8a96a3","#e6f1ff")

image pref_Scrap_2:
    "gui/MenuBGs/setting_menu_scraps-02.webp"
    xcenter 0.5
    yanchor 0.13
    ypos 0.1
    xzoom 0.8
    yzoom 0.8
    matrixcolor SaturationMatrix(0.3)*ColorizeMatrix("#8a96a3","#e6f1ff")

image pref_Scrap_3:
    "gui/MenuBGs/setting_menu_scraps-03.webp"
    xcenter 0.2
    yanchor 0.35
    ypos 0.1
    xzoom 0.95
    yzoom 0.95
    matrixcolor SaturationMatrix(0.3)*ColorizeMatrix("#8a96a3","#e6f1ff")

image pref_Scrap_4:
    "gui/MenuBGs/setting_menu_scraps-04.webp"
    xcenter 0.25
    yanchor 0.1
    ypos 0.0
    xzoom 0.8
    yzoom 0.8
    matrixcolor SaturationMatrix(0.3)*ColorizeMatrix("#8a96a3","#e6f1ff")

## Preferences screen ##########################################################

style bar_pallete:
    left_bar gm_palDict[persistent.gm_curPal][3]
    right_bar gm_palDict[persistent.gm_curPal][0]
    thumb None
    xysize (300,30)

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport")

    if renpy.variant("pc") or renpy.variant("web"):
        vbox:
            xpos 275
            ypos 50
            style_prefix "radio"
            label _("Display"):
                text_color gm_palDict[persistent.gm_curPal][2]

            textbutton _("Window") action Preference("display", "window"):
                text_idle_color gm_palDict[persistent.gm_curPal][4]
                text_hover_color gm_palDict[persistent.gm_curPal][6]

            textbutton _("Fullscreen") action Preference("display", "fullscreen"):
                text_idle_color gm_palDict[persistent.gm_curPal][4]
                text_hover_color gm_palDict[persistent.gm_curPal][6]

    vbox:
        xpos 500
        ypos 50
        style_prefix "radio"
        label _("Rollback Side"):
            text_color gm_palDict[persistent.gm_curPal][2]

        textbutton _("Disable") action Preference("rollback side", "disable"):
            text_idle_color gm_palDict[persistent.gm_curPal][4]
            text_hover_color gm_palDict[persistent.gm_curPal][6]

        textbutton _("Left") action Preference("rollback side", "left"):
            text_idle_color gm_palDict[persistent.gm_curPal][4]
            text_hover_color gm_palDict[persistent.gm_curPal][6]

        textbutton _("Right") action Preference("rollback side", "right"):
            text_idle_color gm_palDict[persistent.gm_curPal][4]
            text_hover_color gm_palDict[persistent.gm_curPal][6]

    vbox:
        xpos 275
        ypos 200
        box_wrap True
        label _("Text Speed"):
            text_color gm_palDict[persistent.gm_curPal][2]

        bar value Preference("text speed") style "bar_pallete"

        label _("Auto-Forward Time"):
            text_color gm_palDict[persistent.gm_curPal][2]

        bar value Preference("auto-forward time") style "bar_pallete"

    vbox:
        box_wrap True
        xpos 750
        ypos 50
        if config.has_music:
            label _("Music Volume"):
                text_color gm_palDict[persistent.gm_curPal][2]

            bar value Preference("music volume") style "bar_pallete"

        if config.has_sound:
            label _("Sound Volume"):
                text_color gm_palDict[persistent.gm_curPal][2]

            bar value Preference("sound volume") style "bar_pallete"
            # if config.sample_sound:
            #     textbutton _("Test") action Play("sound", config.sample_sound)

        if config.has_voice:
            label _("Voice Volume"):
                text_color gm_palDict[persistent.gm_curPal][2]

            bar value Preference("voice volume") style "bar_pallete"
            # if config.sample_voice:
            #     textbutton _("Test") action Play("voice", config.sample_voice)

        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing
            textbutton _("Toggle Text Bleeps"):
                action ToggleVariable('playBleeps')
                style "mute_all_button"
                text_idle_color gm_palDict[persistent.gm_curPal][4]
                text_hover_color gm_palDict[persistent.gm_curPal][6]
#vbox:
    #style_prefix "check"
    #label _("Skip")
    #textbutton _("Unseen Text") action Preference("skip", "toggle")
    #textbutton _("After Choices") action Preference("after choices", "toggle")
    #textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

## Additional vboxes of type "radio_pref" or "check_pref" can be
## added here, to add additional creator-defined preferences.

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

## History screen ##############################################################
image history_namebubble:
    matrixcolor ColorizeMatrix(gm_palDict[persistent.gm_curPal][7],gm_palDict[persistent.gm_curPal][7])
    alpha 0
    "gui/MenuBGs/history/cc menu history namebubble.png"

image history_textbubble:
    alpha 0
    "gui/MenuBGs/history/cc menu history textbubble.png"

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    add "gui/MenuBGs/history/cc menu history.png":
        alpha 0.7
        matrixcolor BrightnessMatrix(-0.6)

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        $xLastName = ""
        vbox:
            spacing 15
            for h in _history_list:
                window:

                    if h.who:
                        frame:
                            #xoffset renpy.random.randint(0,20)
                            background "history_namebubble"

                            if xLastName != h.who:
                                label h.who:
                                    style "history_name"

                                    substitute False
                                    text_color gm_palDict[persistent.gm_curPal][6]

                                    if "color" in h.who_args and h.who_args["color"]:
                                        text_color h.who_args["color"]
                                $xLastName = h.who

                    frame:
                        background "history_textbubble"
                        xpos 150
                        xmaximum 1000


                        text renpy.filter_text_tags(h.what, allow=gui.history_allow_tags):
                            substitute False
                            color gm_palDict[persistent.gm_curPal][5]
                            size 17

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.
define gui.history_allow_tags = set()

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos 2
    xanchor 0.5
    ypos 5
    xsize 50

style history_name_text:
    min_width gui.history_name_width
    text_align 0.5

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

## Help screen #################################################################
screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Controls"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()

style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0
