#PREDEFINED ICONS ----------------------------------------
#Health
image Health_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#fa74d0")

    "gui/text_icons/HEALTH_StatIcon.webp"

image Health_StatIconL:
    zoom 0.10
    yoffset -3
    xoffset -10
    matrixcolor ColorizeMatrix("#000000", "#fa74d0")

    "gui/text_icons/HEALTH_StatIcon.webp"

#Karma
image Karma_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#fff069")

    "gui/text_icons/KARMA_StatIcon.webp"

image Karma_StatIconD:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#ccb100")

    "gui/text_icons/KARMA_StatIcon.webp"

image Karma_StatIconL:
    zoom 0.11
    yoffset -4
    matrixcolor ColorizeMatrix("#000000", "#fff069")

    "gui/text_icons/KARMA_StatIcon.webp"

#Brawn
image Brawn_StatIcon:
    zoom 0.09
    yoffset -4
    matrixcolor ColorizeMatrix("#000000", "#ff5342")
    "gui/text_icons/BRAWN_StatIcon.webp"

image Brawn_StatIconL:
    zoom 0.11
    yoffset -5
    matrixcolor ColorizeMatrix("#000000", "#ff5342")
    "gui/text_icons/BRAWN_StatIcon.webp"


#Brains
image Brains_StatIcon:
    zoom 0.09
    yoffset -5
    matrixcolor ColorizeMatrix("#000000", "#a1fffc")
    "gui/text_icons/BRAINS_StatIcon.webp"

image Brains_StatIconD:
    zoom 0.09
    yoffset -5
    matrixcolor ColorizeMatrix("#000000", "#00c1ba")
    "gui/text_icons/BRAINS_StatIcon.webp"

image Brains_StatIconL:
    zoom 0.11
    yoffset -5
    matrixcolor ColorizeMatrix("#000000", "#a1fffc")
    "gui/text_icons/BRAINS_StatIcon.webp"

#Hustle
image Hustle_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#a7ff78")
    "gui/text_icons/HUSTLE_StatIcon.webp"

image Hustle_StatIconD:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#20a83a")
    "gui/text_icons/HUSTLE_StatIcon.webp"

image Hustle_StatIconL:
    zoom 0.11
    yoffset -5
    matrixcolor ColorizeMatrix("#000000", "#a7ff78")
    "gui/text_icons/HUSTLE_StatIcon.webp"


#Guts
image Guts_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#ff8941")

    "gui/text_icons/GUTS_StatIcon.webp"

image Guts_StatIconL:
    zoom 0.11
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#ff8941")

    "gui/text_icons/GUTS_StatIcon.webp"

image Guts_StatIconD:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#e85800")

    "gui/text_icons/GUTS_StatIcon.webp"

#Charm
image Charm_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#ED2A82")

    "gui/text_icons/CHARM_StatIcon.webp"

image Charm_StatIconL:
    zoom 0.11
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#ED2A82")

    "gui/text_icons/CHARM_StatIcon.webp"

#Occult
image Occult_StatIcon:
    zoom 0.09
    yoffset -3
    "gui/text_icons/OCCULT_NEW_StatIcon.webp"
    #"gui/text_icons/OCCULT_StatIcon.webp"
    matrixcolor ColorizeMatrix("#000000", "#b480ff")

image Occult_StatIconL:
    zoom 0.11
    yoffset -3
    "gui/text_icons/OCCULT_NEW_StatIcon.webp"
    #"gui/text_icons/OCCULT_StatIcon.webp"
    matrixcolor ColorizeMatrix("#000000", "#b480ff")

image Occult_StatIconD:
    zoom 0.09
    yoffset -3
    "gui/text_icons/OCCULT_NEW_StatIcon.webp"
    #"gui/text_icons/OCCULT_StatIcon.webp"
    matrixcolor ColorizeMatrix("#000000", "#7e25fe")

#PowerMod
image PowerMod_StatIcon:
    zoom 0.09
    yoffset -6
    matrixcolor ColorizeMatrix("#000000", "#d05576")

    "gui/text_icons/POWERMOD_StatIcon.webp"

image PowerMod_StatIconL:
    zoom 0.12
    yoffset -6
    matrixcolor ColorizeMatrix("#000000", "#d05576")

    "gui/text_icons/POWERMOD_StatIcon.webp"

#DefenseMod
image DefenseMod_StatIcon:
    zoom 0.09
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#3cb0d9")

    "gui/text_icons/DEFENSE_StatIcon.webp"

image DefenseMod_StatIconL:
    zoom 0.12
    yoffset -3
    matrixcolor ColorizeMatrix("#000000", "#3cb0d9")

    "gui/text_icons/DEFENSE_StatIcon.webp"


#RollMod
image RollMod_StatIcon:
    zoom 0.09
    yoffset -15
    matrixcolor ColorizeMatrix("#000000", "#83ed6e")
    "gui/text_icons/ROLLMOD_StatIcon.webp"

image RollMod_StatIconD:
    zoom 0.09
    yoffset -15
    matrixcolor ColorizeMatrix("#000000", "#5caf4b")
    "gui/text_icons/ROLLMOD_StatIcon.webp"

image RollMod_StatIconL:
    zoom 0.11
    yoffset -15
    matrixcolor HueMatrix(0.0)*ColorizeMatrix("#000000", "#83ed6e")
    "gui/text_icons/ROLLMOD_StatIcon.webp"

#PREDEFINED COLORS ----------------------------------------
init python:
    KarmaGold = "#fff069"
    HealthPink = "#fa74d0"

    BrawnRed = "#ff5342"
    BrainsBlue = "#a1fffc"
    HustleBlue = "#a7ff78"
    GutsOrange = "#ff8941"
    CharmRed = "#ED2A82"
    OccultPurple = "#b480ff"

    kwSuccess = "{color=#54ba3f}{u}Success{/b}{/color}"
    kwFailure = "{color=#d252a4}{u}Failure{/b}{/color}"
    #PREDEFINED KEYWORDS ---------------------------------------
    #Health
    kwHealth = "{image=Health_StatIcon}{color=#fa74d0}Health{/color}"
    kwHealthD = kwHealth

    #Karma
    kwKarma = "{image=Karma_StatIcon}{color=#fff069}Karma{/color}"
    kwKarmaD = "{image=Karma_StatIconD}{color=#ccb100}Karma{/color}"
    kwKarmaL = "{image=Karma_StatIconL}{color=#fff069}Karma{/color}"
    #Power
    kwPowerMod = "{image=PowerMod_StatIcon}{color=#d05576}Pow Mod{/color}"
    kwPowerModL = "{image=PowerMod_StatIconL}{color=#d05576}Pow Mod{/color}"
    kwPowerModD = "{image=PowerMod_StatIcon}{color=#d05576}Pow Mod{/color}"

    #Defense
    kwPDefense = "{image=DefenseMod_StatIcon}{color=#3cb0d9}P Def{/color}"
    kwPDefenseL = "{image=DefenseMod_StatIconL}{color=#3cb0d9}P Def{/color}"
    kwPDefenseD = "{image=DefenseMod_StatIcon}{color=#3cb0d9}P Def{/color}"

    kwSDefense = "{image=DefenseMod_StatIcon}{color=#3cb0d9}S Def{/color}"
    kwSDefenseL = "{image=DefenseMod_StatIconL}{color=#3cb0d9}S Def{/color}"
    kwSDefenseD = "{image=DefenseMod_StatIcon}{color=#3cb0d9}S Def{/color}"

    kwDefenseMod = "{image=DefenseMod_StatIcon}{color=#3cb0d9}Def{/color}"
    kwDefenseModD = "{image=DefenseMod_StatIcon}{color=#3cb0d9}Def{/color}"

    #RollMod
    kwRollMod = "{image=RollMod_StatIcon}{color=#83ed6e}Roll Mod{/color}"
    kwRollModD = "{image=RollMod_StatIconD}{color=#5caf4b}Roll Mod{/color}"
    kwRollModL = "{image=RollMod_StatIconL}{color=#83ed6e}Roll Mod{/color}"

    #Difficulty
    kwDifficultyMod = "{color=#7aff44}Difficulty{/color}"
    kwDifficultyModD = "{color=#5bbe32}Difficulty{/color}"
    kwDifficultyModL = "{color=#7aff44}Difficulty{/color}"

    #MTA
    kwMTA = "{color=#ffe603}MTA{/color}"
    kwMTAD = "{color=#c6b200}MTA{/color}"
    kwMTAL = "{color=#ffe603}MTA{/color}"

    #Brawn
    kwBrawn = "{image=Brawn_StatIcon}{color=#ff5342}Brawn{/color}"
    kwBrawnL = "{image=Brawn_StatIconL}{color=#ff5342}Brawn{/color}"
    kwBrawnD = kwBrawn

    #Brains
    kwBrains = "{image=Brains_StatIcon}{color=#a1fffc}Brains{/color}"
    kwBrainsL = "{image=Brains_StatIconL}{color=#a1fffc}Brains{/color}"
    kwBrainsD = "{image=Brains_StatIconD}{color=#00c1ba}Brains{/color}"

    #Hustle
    kwHustle = "{image=Hustle_StatIcon}{color=#a7ff78}Hustle{/color}"
    kwHustleL = "{image=Hustle_StatIconL}{color=#a7ff78}Hustle{/color}"
    kwHustleD = "{image=Hustle_StatIconD}{color=#20a83a}Hustle{/color}"

    #Guts
    kwGuts = "{image=Guts_StatIcon}{color=#ff8941}Guts{/color}"
    kwGutsL = "{image=Guts_StatIconL}{color=#ff8941}Guts{/color}"
    kwGutsD = "{image=Guts_StatIconD}{color=#e85800}Guts{/color}"

    #Charm
    kwCharm = "{image=Charm_StatIcon}{color=#ED2A82}Charm{/color}"
    kwCharmL = "{image=Charm_StatIconL}{color=#ED2A82}Charm{/color}"
    kwCharmD = kwCharm

    #Occult
    kwOccult = "{image=Occult_StatIcon}{color=#b480ff}Occult{/color}"
    kwOccultL = "{image=Occult_StatIconL}{color=#b480ff}Occult{/color}"
    kwOccultD = "{image=Occult_StatIconD}{color=#7e25fe}Occult{/color}"

#. BACKGROUNDS
image semiSolidBlack:
    alpha 0.5
    Solid("#000000")
