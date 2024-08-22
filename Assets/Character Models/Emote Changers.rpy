init python:
    def ResetChar(xChar="Robyn"):
        if xChar == "Robyn":
            globals()[xChar+"_State"] = getRobynDefaults()
        else:
            globals()[xChar+"_State"] = globals()[xChar+"_Default"]

    def getRobynDefaults():
        xNum = persistent.RobynSettings[4]
        RobynDefault = { "eyes": 0, #0-4
            "brow": 0, #0-3
            "mouth" : 0, #0-7
            "armR": 0, #0-1
            "armL": 0, #0-1
            "shirt": persistent.RobynSettings[7], #0-3
            "hair": persistent.RobynSettings[0], #0-1
            "msg": False, #Phone message
            "shoes": True,
            "coat": 1,
            "fPomf": persistent.RobynSettings[1], #Front Hair Pomf
            "fHair": persistent.RobynSettings[2], #Facial hair
            "glasses": persistent.RobynSettings[3],
            "hairpin": persistent.RobynSettings[6],
            "earring": False,
            "choker": (xNum == 1),
            "necklace": (xNum == 2),
            "beanie": persistent.RobynSettings[5],
            "eyeliner": (xNum == 1)}

        return RobynDefault

screen EmoteChanger(xChar="Robyn",xPos=0.0,yPos=0.0,Zoom=1):
    default EmoteIndex = 0
    default EmoteTypeIndex = 0

    python:
        User_State = globals()[xChar+"_State"]
        EmoteType = list(User_State.keys())

    if gameVersion == 3:
        frame at zoomed(Zoom):
            xmaximum 300
            xminimum 300
            ymaximum 160
            yminimum 160
            xalign xPos
            yalign yPos
            background "semiSolidBlack"

            text EmoteType[EmoteTypeIndex] + " (" + str(EmoteTypeIndex+1) + "/" + str(len(EmoteType))+ ")":
                yoffset 5
                xoffset 5
                text_align 0.5
                color "#b0ff79"

            text ":: Index: " + str(EmoteIndex):
                yoffset 5
                xoffset 160
                text_align 0.5
                color "#b0ff79"

            #Character is also referenced here
            #Applies the Change
            textbutton xChar + " Apply" action SetDict(User_State, EmoteType[EmoteTypeIndex], EmoteIndex):
                text_size 25
                yoffset 35
                xoffset 70
                text_align 0.5
                text_color "#ffddef"
                text_hover_color "#ff41e1"

            #Changes the
            textbutton "Prev Emote" action SetScreenVariable('EmoteIndex',EmoteIndex-1):
                yoffset 70
                xoffset 5
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            textbutton "Next Emote" action SetScreenVariable('EmoteIndex',EmoteIndex+1):
                yoffset 70
                xoffset 150
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            #Changes the Body Part To be adjusted
            textbutton "Prev Type" action [SensitiveIf(EmoteTypeIndex > 0), SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex-1)]:
                yoffset 110
                xoffset 5
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

            textbutton "Next Type" action [SensitiveIf(EmoteTypeIndex < len(EmoteType)-1),SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex+1)]:
                yoffset 110
                xoffset 150
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

screen EmoteChanger2(xChar="Robyn",xPos=0.33,yPos=0.0,Zoom=1):
    default EmoteIndex = 0
    default EmoteTypeIndex = 0

    python:
        User_State = globals()[xChar+"_State"]
        EmoteType = list(User_State.keys())


    if gameVersion == 3:
        frame at zoomed(Zoom):
            xmaximum 300
            xminimum 300
            ymaximum 160
            yminimum 160
            xalign xPos
            yalign yPos
            background "semiSolidBlack"

            text EmoteType[EmoteTypeIndex] + " (" + str(EmoteTypeIndex+1) + "/" + str(len(EmoteType))+ ")":
                yoffset 5
                xoffset 5
                text_align 0.5
                color "#b0ff79"

            text ":: Index: " + str(EmoteIndex):
                yoffset 5
                xoffset 160
                text_align 0.5
                color "#b0ff79"

            #Character is also referenced here
            #Applies the Change
            textbutton xChar + " Apply" action SetDict(User_State, EmoteType[EmoteTypeIndex], EmoteIndex):
                text_size 25
                yoffset 35
                xoffset 70
                text_align 0.5
                text_color "#ffddef"
                text_hover_color "#ff41e1"

            #Changes the
            textbutton "Prev Emote" action SetScreenVariable('EmoteIndex',EmoteIndex-1):
                yoffset 70
                xoffset 5
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            textbutton "Next Emote" action SetScreenVariable('EmoteIndex',EmoteIndex+1):
                yoffset 70
                xoffset 150
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            #Changes the Body Part To be adjusted
            textbutton "Prev Type" action [SensitiveIf(EmoteTypeIndex > 0), SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex-1)]:
                yoffset 110
                xoffset 5
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

            textbutton "Next Type" action [SensitiveIf(EmoteTypeIndex < len(EmoteType)-1),SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex+1)]:
                yoffset 110
                xoffset 150
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

screen EmoteChanger3(xChar="Robyn",xPos=0.66,yPos=0.0,Zoom=1):
    default EmoteIndex = 0
    default EmoteTypeIndex = 0

    python:
        User_State = globals()[xChar+"_State"]
        EmoteType = list(User_State.keys())


    if gameVersion == 3:
        frame at zoomed(Zoom):
            xmaximum 300
            xminimum 300
            ymaximum 160
            yminimum 160
            xalign xPos
            yalign yPos
            background "semiSolidBlack"

            text EmoteType[EmoteTypeIndex] + " (" + str(EmoteTypeIndex+1) + "/" + str(len(EmoteType))+ ")":
                yoffset 5
                xoffset 5
                text_align 0.5
                color "#b0ff79"

            text ":: Index: " + str(EmoteIndex):
                yoffset 5
                xoffset 160
                text_align 0.5
                color "#b0ff79"

            #Character is also referenced here
            #Applies the Change
            textbutton xChar + " Apply" action SetDict(User_State, EmoteType[EmoteTypeIndex], EmoteIndex):
                text_size 25
                yoffset 35
                xoffset 70
                text_align 0.5
                text_color "#ffddef"
                text_hover_color "#ff41e1"

            #Changes the
            textbutton "Prev Emote" action SetScreenVariable('EmoteIndex',EmoteIndex-1):
                yoffset 70
                xoffset 5
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            textbutton "Next Emote" action SetScreenVariable('EmoteIndex',EmoteIndex+1):
                yoffset 70
                xoffset 150
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            #Changes the Body Part To be adjusted
            textbutton "Prev Type" action [SensitiveIf(EmoteTypeIndex > 0), SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex-1)]:
                yoffset 110
                xoffset 5
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

            textbutton "Next Type" action [SensitiveIf(EmoteTypeIndex < len(EmoteType)-1),SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex+1)]:
                yoffset 110
                xoffset 150
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

screen EmoteChanger4(xChar="Robyn",xPos=1.0,yPos=0.0,Zoom=1):
    default EmoteIndex = 0
    default EmoteTypeIndex = 0

    python:
        User_State = globals()[xChar+"_State"]
        EmoteType = list(User_State.keys())


    if gameVersion == 3:
        frame at zoomed(Zoom):
            xmaximum 300
            xminimum 300
            ymaximum 160
            yminimum 160
            xalign xPos
            yalign yPos
            background "semiSolidBlack"

            text EmoteType[EmoteTypeIndex] + " (" + str(EmoteTypeIndex+1) + "/" + str(len(EmoteType))+ ")":
                yoffset 5
                xoffset 5
                text_align 0.5
                color "#b0ff79"

            text ":: Index: " + str(EmoteIndex):
                yoffset 5
                xoffset 160
                text_align 0.5
                color "#b0ff79"

            #Character is also referenced here
            #Applies the Change
            textbutton xChar + " Apply" action SetDict(User_State, EmoteType[EmoteTypeIndex], EmoteIndex):
                text_size 25
                yoffset 35
                xoffset 70
                text_align 0.5
                text_color "#ffddef"
                text_hover_color "#ff41e1"

            #Changes the
            textbutton "Prev Emote" action SetScreenVariable('EmoteIndex',EmoteIndex-1):
                yoffset 70
                xoffset 5
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            textbutton "Next Emote" action SetScreenVariable('EmoteIndex',EmoteIndex+1):
                yoffset 70
                xoffset 150
                text_color "#e6ddff"
                text_hover_color "#b26eff"
                text_insensitive_color "#4d4282"

            #Changes the Body Part To be adjusted
            textbutton "Prev Type" action [SensitiveIf(EmoteTypeIndex > 0), SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex-1)]:
                yoffset 110
                xoffset 5
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"

            textbutton "Next Type" action [SensitiveIf(EmoteTypeIndex < len(EmoteType)-1),SetScreenVariable('EmoteTypeIndex',EmoteTypeIndex+1)]:
                yoffset 110
                xoffset 150
                text_color "#98cdff"
                text_hover_color "#6effe0"
                text_insensitive_color "#428273"
