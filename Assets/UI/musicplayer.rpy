# $musicPlayer.playSong(song = "",songLoop=True,fadeOut=0,fadeIn=0,music2=False,notif=True,queueSong=False)
init python:
    class MusicPlayer: ##This defines what a unit is and has
        def __init__(self):
            return

        def playSong(self,song = "",songLoop=True,fadeOut=0,fadeIn=0,music2=False,notif=True,queueSong=False):
            global songText, musicNote


            if song in list(self.songs.keys()):
                songinfo = self.songs[song]
                playChannel = { True: "music2", False: "music"}

                if queueSong:
                    renpy.music.queue(filenames = songinfo[0],channel=playChannel[music2],loop=songLoop,fadein=fadeIn)
                else:
                    renpy.music.play(filenames = songinfo[0],channel=playChannel[music2],loop=songLoop,fadeout=fadeOut,fadein=fadeIn)

                if not music2:
                    songText = songinfo[1]
                    musicNote = songinfo[2]

                    discord_ingame_update("Crushing on Cryptids","Listening to " + songinfo[1],"Madhouse","")

                    if notif:
                        renpy.hide_screen("song_notif")
                        renpy.show_screen("song_notif",fadeOut=fadeOut)


            else:
                update_discord("Listening to the void", "madhouse")

                renpy.music.stop(fadeout=fadeOut)
                songText = "Silence"
                musicNote = 3
                renpy.hide_screen("song_notif")




        songs = {

            "astral_reflection": [audio.astral_reflection, "Astral Reflection",7],
            "ghastly_resurgence": [audio.abyss_stares_back_song, "Ghastly Resurgence",10],
            "atlas_theme": [audio.atlas_theme_intro, "Atlas Moth",7],
            "atlas_theme_loop": [audio.atlas_theme_loop, "Atlas Moth",7],

            "broken_horns_song_bearsome": [audio.broken_horns_song_bearsome, "Broken Horns",3],
            "boots_on_the_shore_bearsome": [audio.boots_on_the_shore_bearsome, "Boots on the Shore",14],

            "chapter_0_song": [audio.chapter_0_song, "Dead Air",10],
            "cloudless_rain": [audio.cloudless_rain, "Cloudless Rain",7],

            "day_crimes_song": [audio.day_crimes_song, "Day Crimes",0],
            "digihouse_mike_song": [audio.digihouse_mike_song, "Digihouse Mike",9],
            "dirt_nap_dreams": [audio.dirt_nap_dreams, "Dirt Nap Dreams",5],
            "dreamlike_state_song": [audio.dreamlike_state_song, "Dreamlike State",4],
            "dreamlike_state_song_distorted": [audio.dreamlike_state_song_distorted, "Dreamlike State",10],
            "drink_it_song": [audio.drink_it_song, "Drink It",13],

            "eating_in_the_car_song": [audio.eating_in_the_car_song, "Eating in the Car",7],
            "elkhorn_radio_song": [audio.elkhorn_radio_blues_song ,"Elkhorn Radio Blues",9],
            "elkhorn_radio_blues_song_radio": [audio.elkhorn_radio_blues_song_radio, "Elkhorn Radio Blues",9],
            "elkhorn_radio_intro_song": [audio.elkhorn_radio_intro_song, "Elkhorn Radio Intro",9],

            "forever_evergreen_intro": [audio.forever_evergreen_intro, "Forever Evergreen", 3],
            "forever_evergreen_loop": [audio.forever_evergreen_loop, "Forever Evergreen", 3],

            "ghost_space": [audio.ghost_space, "Ghost Space",3],

            "inevitable_insanity": [audio.inevitable_insanity_intro, "Inevitable Insanity",10],
            "inevitable_insanity_loop": [audio.inevitable_insanity_loop, "Inevitable Insanity",10],
            "itsOff": [audio.its_off_song, "It's Off",5],

            "loosen_up_longhope_song": [audio.loosen_up_longhope_song, "Loosen up Longhope",6],
            "loosen_up_longhope_loop": [audio.loosen_up_longhope_loop, "Loosen up Longhope",6],

            "lure_gaff_bait_tackle_intro": [audio.sirmeow_lgbt_intro,"Lure Gaff Bait Tackle",6],
            "lure_gaff_bait_tackle_loop": [audio.sirmeow_lgbt_loop,"Lure Gaff Bait Tackle",6],

            "mage_hands": [audio.mage_hands, "Mage Hands",7],
            "magic_birdbrain_song": [audio.magic_birdbrain_song, "Magic Birdbrain",5],
            "midway_to_nowhere_song": [audio.midway_to_nowhere_song, "Midway to Nowhere",8],
            "missing_you_song": [audio.missing_you_song, "Missing You",5],

            "next_time_on_song": [audio.next_time_on_song, "Next Time On",1],
            "not_so_spooky_song": [audio.not_so_spooky_song, "Not So Spooky",9],


            "orbitalNap": [audio.orbital_nap_song, "Orbital Nap",3],
            "pleasant_conversation_song": [audio.pleasant_conversation_song, "Pleasant Conversation",14],

            "cryptidcrush_cafe2": [audio.cryptidcrush_cafe2, "Summerstone",3],
            "supernatural_foe_intro_song": [audio.supernatural_foe_intro_song, "Supernatural Foe",7],
            "supernatural_foe_loop_song": [audio.supernatural_foe_loop_song, "Supernatural Foe",7],
            "supernatural_serenade_song": [audio.supernatural_serenade_song, "Supernatural Serenade",3],

            "the_hound_song": [audio.the_hound_samples, "The Hound",10],
            "the_prowl": [audio.the_prowl_song, "The Prowl",8],
            "the_unwelcome_visitor": [audio.the_unwelcome_visitor, "The UNWELCOME Visitor",10],
            "the_visitor_radio_song": [audio.the_visitor_radio_song, "The Visitor",10],
            "the_leviathan_waltz": [audio.the_leviathan_waltz, "The Leviathan Waltz",8],

            "undead_icebreakers_song": [audio.undead_icebreakers_song, "Undead Icebreakers",0],
            "urgently_jammin_song": [audio.urgently_jammin_song, "Urgently Jammin'",8],
            "urgently_jammin_sir_meow_remix_loop": [audio.urgently_jammin_sir_meow_remix_loop, "Urgently Jammin' (Sir Meow Remix)",7],
            "urgent_slower": [audio.urgent_slower, "Urgently Slower",8],

            "stygian_scuffle_song": [audio.stygian_scuffle_song, "Stygian Scuffle",7],

            "thaumaturgy_thursdays_song": [audio.thaumaturgy_thursdays_song, "Thaumaturgy Thursdays",8],

            "wrath_of_the_recolors": [audio.wrath_of_the_recolors_song, "Wrath of the Recolors",7],
            "wistfulOnes": [audio.wistful_ones_song, "Wistful Ones",13],

            "song_name": [audio.eating_in_the_car_song, "Song Text Name",1],
            "song_name": [audio.eating_in_the_car_song, "Song Text Name",1],

            "radioStatic": [audio.radiostatic, "Static",13]
        }


    musicPlayer = MusicPlayer()

image songtext_bg:
    "gui/Music_Indicator.webp"

transform songbox_tf(hideWait=0,fadeOut=0):
    on show:
        xoffset limitValue(len(songText)*12 + 85,85,300)


    on hide:
        xoffset limitValue(len(songText)*12 + 85,85,300)
        pause fadeOut
        ease 1.0 xoffset 0
        pause hideWait
        xoffset 0
        yoffset 0
        ease 1.0 yoffset -120

transform songbox_tfAlt:
    on show:
        xoffset limitValue(len(songText)*12 + 85,85,300)
        yoffset 0
        ease 1.0 xoffset 0

    on hide:
        xoffset limitValue(len(songText)*12 + 85,85,300)
        xoffset 0
        yoffset 0
        ease 1.0 yoffset -120

screen song_notif(fadeOut=0,instaHide=True):
    zorder 500

    #Song Text
    frame:
        if instaHide:
            at songbox_tf(limitValue(len(songText)*0.1+1,0.5,5),fadeOut)
        else:
            at songbox_tfAlt

        background None

        add "songtext_bg":
            xcenter 1.0
            ycenter 0.0
            xysize (limitValue(len(songText)*21 + 170,60,610),115)

        hbox:
            xanchor 1.0
            xpos 1270
            ypos 0
            yanchor 0.0
            spacing -13


            text songText: #"{image=song music note}" +
                color getPCNameColor() # "#a0dda8"


                size 16
                xmaximum 250
                line_spacing 2
                text_align 1.0
                font "fonts/typwrng.ttf"

            add "song music note" at idleFloat(1.3,5):
                matrixcolor ColorizeMatrix("#000000",PCnameColor)

    if instaHide:
        timer 0.01 action [Hide("song_notif")] repeat True

transform popup_text_tf(t=0.5):
    on show:
        xcenter 0.5
        ycenter -0.5
        ease t ycenter 0.3

    on hide:
        ycenter 0.3
        ease t ycenter -0.5

transform alpha_tf(a=1):
    alpha a

screen popup_text(txt="Hello World",confirmTxt = "Okay!",showTime=0.5):
    default isShowing = False
    zorder 1000
    timer showTime+0.25 action ToggleScreenVariable("isShowing") repeat False

    frame:
        at DarkCGShade_tf
        modal True
        background Solid("#000000")


    dismiss action Hide()
    frame at popup_text_tf(showTime):
        xcenter 0.5
        ycenter 0.3
        modal True
        padding (20, 20)

        has vbox

        text txt:
            xalign 0.5
            text_align 0.5

        textbutton confirmTxt:
            xalign 0.5
            action Hide()

    if not isShowing:
        frame at alpha_tf(0):
            modal True
            background Solid("#ff0000")
