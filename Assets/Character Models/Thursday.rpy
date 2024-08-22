define Thursday = Character("Thursday", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#d5a0cb")

transform thursdaysize:
    zoom 0.11
    ycenter 0.5
    xanchor 0.5

# image Thursday:
#     ConditionSwitch(
#         "Thursday_State['face'] <= 0", "Thursday Default",
#         "Thursday_State['face'] == 1", "Thursday Caw",
#         "Thursday_State['face'] == 2", "Thursday Wings",
#         "Thursday_State['face'] == 3", "Thursday Angry",
#         "Thursday_State['face'] == 4", "Thursday Look",
#         "Thursday_State['face'] == 5", "Thursday Smile",
#         "Thursday_State['face'] == 6", "Thursday Smirk",
#         "Thursday_State['face'] >= 7", "-")
#
# image Thursday Reset:
#     "Thursday"

image Thursday Default:
    thursdaysize
    "images/Characters/Thursday/Thursday_Default.webp"

image Thursday Caw:
    thursdaysize
    "images/Characters/Thursday/Thursday_Caw.webp"

image Thursday Wings:
    thursdaysize
    "images/Characters/Thursday/Thursday_Flying.webp"

image Thursday Angry:
    thursdaysize
    "images/Characters/Thursday/Thursday_Scowl.webp"

image Thursday Look:
    thursdaysize
    "images/Characters/Thursday/Thursday_Concerned.webp"

image Thursday Smile:
    thursdaysize
    "images/Characters/Thursday/Thursday_Smile.webp"

image Thursday Smirk:
    thursdaysize
    "images/Characters/Thursday/Thursday_Smirk.webp"
