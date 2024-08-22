label Ch2_SectionSelect_Label:

    menu:
        extend ""

        "Jamie VS Madhouse" if seenLabel("Ch1_Day3Morning"):
            menu:
                extend ""

                "Morning":
                    jump Ch1_Day3Morning

                "Atlas Doctor Visit" if seenLabel("Ch1_AtlasDoctorVisit") :
                    jump Ch1_AtlasDoctorVisit

                "Jamie Fight" if seenLabel("Ch1_JamieFightBuildup"):
                    jump Ch1_JamieFightBuildup

                "Walking Home" if seenLabel("Ch1_WalkHomeWithJamie"):
                    jump Ch1_WalkHomeWithJamie

                "back":
                    jump Ch2_SectionSelect_Label

        "Lexulathu’al"  if seenLabel("Ch2_RobynMeetsLex"):

            jump Ch2_RobynMeetsLex
