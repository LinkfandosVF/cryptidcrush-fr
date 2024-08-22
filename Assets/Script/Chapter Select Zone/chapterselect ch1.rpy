#Chapter 1
label Ch1_SectionSelect_Label:
    menu:
        extend ""

        "Intro" if seenLabel("Ch1_Start"):
            jump Ch1_Start

        "Nightmare" if seenLabel("Ch1_SundayNightmare"):
            jump Ch1_SundayNightmare

        "Welcome to Longhope" if seenLabel("Ch1_OnTheTownToEdiths"):
            menu:
                extend ""

                "Edith's Shop":
                    $displaymenu = True
                    menu:
                        extend ""
                        "To Ediths":
                            $displaymenu = False
                            jump Ch1_OnTheTownToEdiths
                        "August Room" if seenLabel("Ch1_August_Hospital"):
                            $displaymenu = False
                            jump Ch1_August_Hospital
                        "Back to Edith" if seenLabel("Ch1_BackToEdith"):
                            $displaymenu = False
                            jump Ch1_BackToEdith
                        "back":
                            jump Ch1_SectionSelect_Label

                "Library" if seenLabel("Ch1_LibraryIntro"):
                    jump Ch1_LibraryIntro

                "Cafe w/ Jamie" if seenLabel("Ch1_CafeIntro"):
                    jump Ch1_CafeIntro

                "Robbie Intro" if seenLabel("Ch1_RobbieIntro"):
                    jump Ch1_RobbieIntro

                "Atlas Meetup" if seenLabel("Ch1_AtlasMeetup"):
                    jump Ch1_AtlasMeetup

                "Lake Intro" if seenLabel("Ch1_LakeIntro"):
                    jump Ch1_LakeIntro

                "Atlas & August" if seenLabel("Ch1_AtlasAugustConvo"):
                    jump Ch1_AtlasAugustConvo

                "Night" if seenLabel("Ch1_Day1Night"):
                    jump Ch1_Day1Night

                "back":
                    jump Ch1_SectionSelect_Label

        "August & The Graveyard" if seenLabel("Ch1_Day2Wakeup"):
            $displaymenu = True
            menu:
                extend ""
                "Morning":
                    jump Ch1_Day2Wakeup

                "August Checkup" if seenLabel("Ch1_AugustCheckup_ToGus"):
                    jump Ch1_AugustCheckup_ToGus

                "Tessie & Goatma'am" if seenLabel("Ch1_AugustCheckup_TessieGoatmaam"):
                    jump Ch1_AugustCheckup_TessieGoatmaam

                "Graveyard" if seenLabel("Ch1_GraeyardExploration"):
                    jump Ch1_GraveyardExploration

                "Sleepy Time" if seenLabel("Ch1_Day2Night"):
                    jump Ch1_Day2Night

                "back":
                    jump Ch1_SectionSelect_Label
