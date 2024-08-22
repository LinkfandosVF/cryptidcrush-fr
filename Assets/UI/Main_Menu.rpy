init offset = -1
#------------------------------------------------------------------------------- Intro Screen

image FlashingWarning:
    zoom 0.5
    matrixcolor ColorizeMatrix("#ffffff", "#ffffff")
    "images/Props/Flash Warning/Madlas1.webp"
    pause 0.2
    "images/Props/Flash Warning/Madlas2.webp"
    pause 0.2
    "images/Props/Flash Warning/Madlas3.webp"
    pause 0.2
    "images/Props/Flash Warning/Madlas4.webp"
    pause 0.2
    "images/Props/Flash Warning/Madlas5.webp"
    pause 0.2
    repeat

image drakeDrowzy:
    zoom 0.45
    xcenter 0.5
    ycenter 0.45
    matrixcolor ColorizeMatrix("#000000", "#ffffff")
    "images/Props/DD Logo/DrowzyLogo1.webp"
    pause 0.2
    "images/Props/DD Logo/DrowzyLogo2.webp"
    pause 0.2
    "images/Props/DD Logo/DrowzyLogo3.webp"
    pause 0.2
    "images/Props/DD Logo/DrowzyLogo4.webp"
    pause 0.2
    "images/Props/DD Logo/DrowzyLogo5.webp"
    pause 0.2
    repeat

image OzWarning:
    zoom 0.4
    "images/Props/Flash Warning/Oz_Warning.webp"

label splashscreen:

    $init_discord()


    # 0: Public
    # 1: Patron
    # 2: Beta Testers
    # 3: Devs


    show OzWarning:
        xcenter 0.225
        ycenter 0.5

    show text "{glitch=1.5}{size=80}{b}WARNING!{/b}{/size}{size=40}\n{b}This game is a Work-in-Progress!{/b}{/size}\n\n\n{size=30}Some aspects are unfinished, and there \nmay be bugs.{/size}\n\n\nSaves from previous versions are incompatible, \nbut you can jump-in using CHAPTER SELECT \nif you've made a character.{/glitch}":
        xcenter 0.67
        ycenter 0.45
    with Dissolve(1.0)
    play voice thursday_splashwarning
    $renpy.pause(5.0,hard=True)
    pause 12
    $update_discord()
    stop voice fadeout 1.0
    hide OzWarning
    hide text
    with Dissolve(0.75)
    play music2 radiostatic fadein 5.0

    $persistent.staticAlreadyPlaying = True
    $PCname = persistent.RobynName[0]
    $PClastname = persistent.RobynName[1]

    show FlashingWarning:
        xcenter 0.5
        ycenter 0.45
        zoom 0.8
    show text "{glitch=2.0}{size=40}Warning: Potential Eye Strain{/size}{/glitch}":
        xcenter 0.5
        ycenter 0.8
    with Dissolve(1.0)

    pause 3.0
    hide FlashingWarning
    hide text
    with Dissolve(1.0)
    pause 0.5

    show drakeDrowzy
    show text "{glitch=4.0}{size=40}{font=fonts/typwrng.ttf}Drowsy Drake{/font}{/size}{/glitch}":
        xcenter 0.5
        ycenter 0.74
    with Dissolve(1.5)

    pause 2.5
    hide drakeDrowzy
    hide text
    with Dissolve(0.75)
    pause 0.5

    call startTheGame from _call_startTheGame_1
    return

#------------------------------------------------------------------------------- Main Menu

#Menu Label
label main_menu:
    python:
        discord_ingame_update("Main Menu","Getting Ready to play","Madhouse","")
        persistent.staticAlreadyPlaying = False

    call setAboutPage from _call_setAboutPage
    window hide
    show screen main_menu

    with Dissolve(1.5)
    if not persistent.democompleted:
        play music cryptid_crush_song fadein 15.0

    else:
        play music cryptid_crush_song_radio fadein 15.0
    python:
        renpy.music.set_volume(0.5, delay=15.0, channel=u'music2')
        renpy.pause(hard=True)

#Main Menu UI
image main_menu_glow:
    contains:
        alpha 1
        "gui/MainMenuEffects/DefaultMain.webp"

    contains:
        alpha 0
        pause 1.0
        choice:
            pause 3.0
            "gui/MainMenuEffects/GlowMain.webp"
            alpha 1.0
            pause 0.1
            alpha 0
            pause 0.1
            alpha 1.0
            pause 0.1
            alpha 0
            pause 0.5
            alpha 1.0
            pause 3.0
            alpha 0
            pause 0.05
            alpha 1.0
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1.0
            pause 0.05
            alpha 0
        choice:
            pause 1.0
            "gui/MainMenuEffects/GlowMain.webp"
            ease 4.0 alpha 1.0
            pause 1.0
            ease 4.0 alpha 0
        choice:
            pause 2.0
            alpha 1
            "gui/MainMenuEffects/GlitchMain.webp"
            pause 0.1
            "gui/MainMenuEffects/GlitchMain2.webp"
            pause 0.1
            alpha 0
        choice:
            pause 1.5
            "gui/MainMenuEffects/GlowMain.webp"
            ease 4.0 alpha 1.0
            pause 1.0
            "gui/MainMenuEffects/GlitchMain.webp"
            pause 0.1
            "gui/MainMenuEffects/GlitchMain2.webp"
            pause 0.1
            alpha 0
        choice:
            pause 0.5
            alpha 1
            "gui/MainMenuEffects/GlitchMain.webp"
            pause 0.1
            "gui/MainMenuEffects/GlitchMain2.webp"
            pause 0.1
            "gui/MainMenuEffects/GlowMain.webp"
            pause 1.0
            ease 4.0 alpha 0
        choice:
            pause 2.5
            "gui/MainMenuEffects/GlowMain.webp"
            alpha 1.0
            pause 0.1
            alpha 0
            pause 0.1
            alpha 1.0
            pause 0.1
            alpha 0
            pause 1.0
            alpha 1
            "gui/MainMenuEffects/GlitchMain.webp"
            pause 0.1
            "gui/MainMenuEffects/GlitchMain2.webp"
            pause 0.1
            "gui/MainMenuEffects/GlowMain.webp"
            pause 3.0
            alpha 0
            pause 0.05
            alpha 1.0
            pause 0.05
            alpha 0
            pause 0.05
            alpha 1.0
            pause 0.05
            alpha 0

        repeat

default mm_start_button = "Start"
default mm_load_button = "Load"
default mm_pref_button = "Preferences"
default mm_about_button = "About"
default mm_quit_button = "Quit"

# image MM_L2D = Live2D("Resources/mike2D", base=.5, loop=True, height=0.7)
# transform MM_L2D_Pos:
#     matrixcolor TintMatrix("#fad4ff")
#     xcenter 0.75
#     rotate 17
#     ycenter 0.4
#     block:
#         ease 3.5 yoffset -60
#         pause 0.25
#         ease 3.5 yoffset 50
#         pause 0.25
#         repeat
#
# default MM_L2D_mainmenu = "MM_L2D vibin"

define config.log_live2d_loading = True

# choice:
#     matrixcolor SaturationMatrix(1.2)*TintMatrix("#ea5bff")*BrightnessMatrix(0.07)
#     "images/BGs/Outside_Radio_Station2.webp"
image BGRandomMainMenu:
    #Dom Signal Background choices
    matrixcolor SaturationMatrix(1.2)*TintMatrix("#f4a7ff")

    choice:
        "BG Studio Room Aftermath"
    choice:
        "BG SunsetRoadside"
    choice:
        "images/BGs/Dream_Zone.webp"
    choice:
        "BG Cabin Night"
    choice:
        "BG Lake Night"
    choice:
        "BG Bridge"

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu
    if not persistent.staticAlreadyPlaying:
        on "show" action Play("music2",audio.radiostatic)
    style_prefix "main_menu"

    # Chooses the background of the main menu
    add 'BGRandomMainMenu':
        xysize (1280,720)
        xcenter 0.5
        ycenter 0.5


    # Menu UI Image
    add "main_menu_glow"

    # if renpy.has_live2d():
    #     add MM_L2D_mainmenu at MM_L2D_Pos
    #
    #     button:
    #         idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DDFBF2}{size=35}MM"))
    #         hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#FF53F0}MM{/color}{/size}{/font}{/bt}"))
    #         hover_sound audio.selecthover
    #         activate_sound renpy.random.choice([audio.mm_laugha,audio.mm_laughb,audio.mm_laughc,audio.mm_laughd,audio.mm_laughe,audio.mm_laughf,audio.mm_laughg])
    #         xcenter 0.9
    #         ycenter 0.7
    #         action ToggleVariable("MM_L2D_mainmenu", true_value="MM_L2D giggle", false_value="MM_L2D vibin")

    ## Menu Buttons ------------------------------------------------------------

    #Start Button
    if persistent.RobynCreated:
        button:
            idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=45}Début"))
            hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=45}{color=#10FCBB}Début{/color}{/size}{/font}{/bt}"))
            selected_hover_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=45}Début"))
            selected_idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=45}Début"))
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)
            xcenter 0.2
            ycenter 0.45
            action Start()
    else:
        button:
            idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=35}Nouveaux"))
            hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#10FCBB}Nouveaux{/color}{/size}{/font}{/bt}"))
            selected_hover_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=35}Nouveaux"))
            selected_idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#F5DEF3}{size=35}Nouveaux"))
            hover_sound audio.selecthover
            activate_sound renpy.random.choice(selectList)
            xcenter 0.2
            ycenter 0.45
            action Start()


    #Load
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#E4D4F1}{size=40}Charger"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=40}{color=#37FF58}Charger{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.29
        ycenter 0.58
        action ShowMenu("load")

    #Options
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DAE5FB}{size=28}Options"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=28}{color=#6B9DFF}Options{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.2
        ycenter 0.71
        action ShowMenu("preferences")

    #About
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#CAF3D1}{size=35}A propos"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#BC6BFF}A propos{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.24
        ycenter 0.83
        action ShowMenu("about")

    #Quit
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DDFBF2}{size=35}Quitter"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#FF53F0}Quitter{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.21
        ycenter 0.915
        action Quit(confirm=not main_menu)


    #Patreon
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DDFBF2}{size=35}Patreon"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#FF53F0}Patreon{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.9
        ycenter 0.76
        action OpenURL("https://www.patreon.com/DrowsyDrake")

    #Discord
    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DDFBF2}{size=35}Discord"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#FF53F0}Discord{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.9
        ycenter 0.83
        action OpenURL("https://discord.gg/QQYcb33rft")

    button:
        idle_child Text(_("{font=fonts/Inika-Bold.ttf}{color=#DDFBF2}{size=35}Patch Français"))
        hover_child Text(_("{bt=5}{font=fonts/Inika-Bold.ttf}{size=35}{color=#FF53F0}Vers Github{/color}{/size}{/font}{/bt}"))
        hover_sound audio.selecthover
        activate_sound renpy.random.choice(selectList)
        xcenter 0.9
        ycenter 0.9
        action OpenURL("https://github.com/LinkfandosVF/cryptidcrush-fr")

    vbox:
        xcenter 0.95
        ycenter 1.0
        text "{color=#fff}[config.version]{/color}":
            style "main_menu_version"

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True


style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
