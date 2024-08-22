init offset = -1

default pcBaseStats = persistent.RobynStats
default PC_Stats = RobynUnit()

# -------------------------------------------------------------------- RobynUnit
init python:
    def OutputPCGradient(xText):
        # persistent.RobynSettings[8]

        xTextArr = [ "{gradient=#236b41-#1AE65A}",
            "{gradient=#7d1335-#ff81aa}",
            "{gradient=#124499-#639dff}",
            "{gradient=#951b1b-#ff4545}",
            "{gradient=#604982-#bb8cff}",
            "{gradient=#774f2d-#b39275}",
            "{gradient=#cfb133-#ebff87}",
            "{gradient=#404181-#a3a4ff}"]

        xStr = xTextArr[persistent.RobynSettings[8]] + xText +"{/gradient}"

        return xStr

    def getPCNameColor(isDark=False):
        global PCnameColors, PCnameColorsDark

        if isDark:
            return PCnameColorsDark[persistent.RobynSettings[8]]
        return PCnameColors[persistent.RobynSettings[8]]

    class RobynUnit(PlayerUnit):
        attack_desc = {
            'Bash' :                "[kwSuccess] Deals medium damage, and slightly lowers Target's [kwPowerMod].\n\n[kwFailure] Lowers Target's [kwDifficultyModD].\n\nChecks [kwBrawn] vs [kwHustleD]\nCost: 1 Stamina",
            'Cheer' :               "[kwSuccess] Slightly raises Target(s)' [kwPowerMod], and regains [kwHealth] when used on a single Target.\n\n[kwFailure] Move works, but raises Opponent [kwPowerMod].\n\nChecks [kwCharm] vs Fixed(7)\nCost: 2 Stamina",
            'Focus' :               "[kwSuccess] Raises [kwKarmaD] by +2.\n\n[kwFailure] Raises an allies stats.\n\nCheck [kwBrainsD] vs Fixed(8)\nCost: 3 Stamina",
            'Heart Out' :           "[kwSuccess] Delays Target's attack slightly, and lowers both Target's [kwDifficultyModD] and [kwBrawn].\n\n[kwFailure] Target will act sooner, and slightly raises Target's [kwDifficultyModD].\n\nChecks [kwCharm] vs [kwBrainsD]\nCost: 4 Stamina",
            'Unarmed Smite' :       "[kwSuccess] Deals light piercing damage 3 times.\n\n[kwFailure] Move works but doesn't pierce.\n\nChecks [kwBrawnD] vs [kwGutsD]\nCost: 2 Stamina",
            'Identify' :            "[kwSuccess] Greatly Lowers Target [kwDifficultyModD].\n\n[kwFailure] Slightly Raises Target [kwDifficultyModD].\n\nChecks [kwBrainsD] vs [kwCharmD]\nCost: 2 Stamina",
            'Rapier Thrust' :       "[kwSuccess] Deals medium piercing damage and lowers target [kwPowerMod]. The bonus modifiers for damage are doubled for this move. \n\n[kwFailure] Move works, but deals reduced damage and doesn't lower [kwPowerMod].\n\nChecks [kwHustleD] vs [kwHustleD]\nCost: 2 Stamina",
            'Stretch!' :            "[kwSuccess] Raises all base stats excluding [kwGutsD].\n\n[kwFailure] Lowers all base stats excluding [kwGutsD].\n\nChecks [kwGutsD] vs Fixed(10)\nCost: 1 Stamina",
            'Enthrall' :            "[kwSuccess] Delays Target turn. Target will have a high chance to skip their turn whenever they act. Effect ends when they skip their turn.\n\n[kwFailure] Target acts immediately. \n\nChecks [kwCharmD] vs [kwBrainsD]\nCost: 3 Stamina",
            'Kazam Kadabra' :       "[kwSuccess] Deals medium damage. User gains HP based on damage dealt. Raises [kwOccultD]. Lowers target [kwBrainsD].\n\n[kwFailure] Move works, but user instead takes 100% recoil. \n\nChecks [kwOccultD] vs [kwOccultD]\nCost: 4 Stamina",
            'KaFlux' :              "[kwSuccess] Deals medium damage.\n\n[kwFailure] The target's [kwBrawn] and [kwBrainsD] are raised slightly.\n\nChecks [kwOccultD] vs [kwHustleD]\nCost: 2 Stamina",
            'Sleight of Crowbar' :  "[kwSuccess] Deals heavy piercing damage.\n\n[kwFailure] Deals reduced damage.\n\nCheck [kwHustleD] vs [kwBrainsD]\nCost: 2 Stamina",
            'Flex' :                "[kwSuccess] Raises all your core stats.\n\n[kwFailure] Move works, but also raises the enemy team's [kwDifficultyModD].\n\nChecks [kwGutsD] vs Fixed(9)\nCost: 1 Stamina",
            'Healing Sprite' :      "[kwSuccess] Everyone regains [kwHealth].\n\n[kwFailure] Move works, but everyone regains less [kwHealth].\n\nChecks [kwOccultD] vs Fixed(10)\nCost: 3 Stamina",
            'Pillow Pummel' :       "[kwSuccess] Deals medium damage, and lowers both Target's [kwPowerMod] and [kwDifficultyModD].\n\n[kwFailure] Lowers Target's [kwDifficultyModD].\n\nChecks [kwHustleD] vs [kwHustleD]\nCost: 1 Stamina",
            'Sheer Focus' :         "Raises [kwKarmaD] by +1 and regenerates a small amount of health for all allies.\n\nCost: 3 Stamina",
            'Mind Palace' :         "[kwSuccess] All allies regain a massive amount of [kwHealth].\n\n[kwFailure] Move works, but {color=#5cefff}Dream Eater{/color} moves forward one level.\n\nChecks [kwOccultD] vs Fixed(8)\nCost: 4 Stamina",
            'Jarhouse toss' :       "Combo w/ Madhouse\n\n[kwSuccess] Deals moderate damage to a target.\n\n[kwFailure] Madhouse takes damage.\n\nChecks [kwHustleD] vs [kwHustleD]\nCost: 2 Stamina",
            'Kazap' :                   "[kwSuccess] Deals moderate damage and slightly lowers both target [kwBrainsD] and [kwBrawnD]. \n\n[kwFailure] Move works but only deals damage.\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 2 Stamina",
            'Jersey Tango': "A combo with jamie where the two create an electrical blaze which fries a single target for massive damage. If used with less than 2 [kwKarmaD], they instead do a dance which gains +3[kwKarmaD]\n\nCost: 2 [kwKarmaD]",
            'Idle' : 'Raises [kwMTAD] and slightly lowers [kwDifficultyModD] of all enemies.\n\n If used without [kwKarmaD], you gain +1 [kwKarmaD].\n\nCost: 1 [kwKarmaD]',
            '' : '',
        }

        #                           AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Bash' :                AttackMove("Bash",              "", -1, "", "brawn",    "hustle",   0, False, [],0),
            'Cheer' :               AttackMove("Cheer",             "", -2, "", "charm",    "fixed",    1, True,  [],7),
            'Focus' :               AttackMove("Focus",             "", -3, "", "brains",   "fixed",    2, True,  [],8),
            'Heart Out' :           AttackMove("Heart Out",         "", -4, "", "charm",    "brains",   0, False, [],0),
            'Unarmed Smite' :       AttackMove("Unarmed Smite",     "", -2, "", "brawn",    "guts",     0, False, [],0),
            'Identify' :            AttackMove("Identify",          "", -2, "", "brains",   "charm",    0, False, [],0),
            'Rapier Thrust' :       AttackMove("Rapier Thrust",     "", -2, "", "hustle",   "hustle",   0, False, [],0),
            'Stretch!' :            AttackMove("Stretch!",          "", -1, "", "guts",     "fixed",    2, True,  [],10),
            'Enthrall' :            AttackMove("Enthrall",          "", -3, "", "charm",    "brains",   0, False, [],0),
            'Kazam Kadabra' :       AttackMove("Kazam Kadabra",     "", -4, "", "occult",   "occult",   0, False, [],0),
            'KaFlux' :              AttackMove("KaFlux",            "", -2, "", "occult",   "hustle",   0, False, [],0),
            'Sleight of Crowbar' :  AttackMove("Sleight of Crowbar","", -2, "", "hustle",   "brains",   0, False, [],0),
            'Flex' :                AttackMove("Flex",              "", -1, "", "guts",     "fixed",    2, True,  [],9),
            'Healing Sprite' :      AttackMove("Healing Sprite",    "", -3, "", "occult",   "fixed",    2, True,  [],10),
            'Pillow Pummel' :       AttackMove("Pillow Pummel",     "", -1, "", "hustle",   "hustle",   0, False, [],0),
            'Sheer Focus' :         AttackMove("Sheer Focus",       "", -3, "", "brains",   "fixed",    2, True,  [],-1),
            'Mind Palace' :         AttackMove("Mind Palace",       "", -4, "", "occult",   "fixed",    2, True,  [], 8),
            'Jarhouse toss' :       AttackMove("Jarhouse toss",     "", -2, "", "hustle",   "hustle",   0, False, [2],8),
            'Jersey Tango' :       AttackMove("Jersey Tango",     "", 0, "", "hustle",   "fixed",   0, False, [2],-1),
            'Kazap' :               AttackMove("Kazap",             "", -2, "", "occult",   "brains",   0, False, [],8),
            'Idle' :                AttackMove("Idle",               "", 0, "", "hustle", "fixed", 2, True, [0],-1),
        }

        def __init__(self):
            global pcBaseStats, PCname,robCoat, PCnameColor
            rNameColor = ["{color=#1AE65A}","{color=#ff81aa}","{color=#639dff}","{color=#ff4545}","{color=#bb8cff}","{color=#b39275}","{color=#ebff87}","{color=#a3a4ff}"]

            PlayerUnit.__init__(self, rNameColor[robCoat] + PCname + "{/color}", pcBaseStats)
            self.SetIcon('pcIcon')

            self.Color = PCnameColor

            vLines = []
            vLines.append([RobynSays("Generic","SurpriseC")])
            vLines.append([RobynSays("Generic","Concern"),RobynSays("Generic","Annoyed"),RobynSays("Generic","ConfusedA"),RobynSays("Generic","DefeatedA")])
            vLines.append([RobynSays("Generic","Excited")])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

        def updateStats(self):
            global pcBaseStats, robCoat,PCname
            rNameColor = ["{color=#1AE65A}","{color=#ff81aa}","{color=#639dff}","{color=#ff4545}","{color=#bb8cff}","{color=#b39275}","{color=#ebff87}","{color=#a3a4ff}"]

            pc_dict = {
                'brawn': pcBaseStats[0],
                'brains': pcBaseStats[1],
                'hustle': pcBaseStats[2],
                'guts': pcBaseStats[3],
                'charm': pcBaseStats[4],
                'occult': pcBaseStats[5],
                'hp': pcBaseStats[6],
            }
            self.ChangeStats(**pc_dict)
            self.name = rNameColor[robCoat] + PCname + "{/color}"

        # Sets Robyn's attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
        # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in RobynUnit.attack_bases:
                    new_attack = RobynUnit.attack_bases[attack].copy()
                    new_attack.desc = RobynUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

        # Used in the game menu to show player stats.
        def getRawStats(self):
                global pc_karma
                global diceBot

                tStats = [[""],[""]]
                stat_types = ['brawn', 'brains', 'hustle', 'guts', 'charm', 'occult']
                #Brawn
                for type in stat_types:
                    tStats[0].append(type.capitalize() + ':')
                    plus_sign = '+' if self.cStats(type) > -1 else ''
                    tStats[1].append(plus_sign + str(self.cStats(type)))

                tStats[0].append("\n" + diceBot.dieName)
                tStats[1].append("\n")

                tStats[0].append("\nKarma:")
                tStats[1].append("\n" + str(pc_karma) + "/" + str(diceBot.maxKarma))

                return tStats


# ------------------------------------------------------------------------- Icon
#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged

image pcIcon:
    ConditionSwitch(
        "PC_Stats.iconState == 2","pcIcon damaged",
        "PC_Stats.iconState == -1 or not PC_Stats.isAlive","pcIcon ko",
        "PC_Stats.exhausted","pcIcon exhausted",
        "PC_Stats.iconState == 1","pcIcon select",
        "True","pcIcon base")

layeredimage pcIcon base:

    always:
        "pc backdrop"

    if not PC_Stats.isBloodied():
        "pc icon"
    else:
        "pc icon hurtidle"

    if Robyn_State["fHair"]:
        "pc facialhair"

    if Robyn_State["glasses"]:
        "pc glasses"

layeredimage pcIcon exhausted:
    always:
        "pc backdrop exhausted"
    always:
        "pc icon exhausted"

    if Robyn_State["fHair"]:
        "pc facialhair"

    if Robyn_State["glasses"]:
        "pc glasses"

layeredimage pcIcon select:
    always:
        "pc backdrop selected"

    if not PC_Stats.isBloodied():
        "pc icon"
    else:
        "pc icon hurtidle"

    if Robyn_State["fHair"]:
        "pc facialhair"

    if Robyn_State["glasses"]:
        "pc glasses"

layeredimage pcIcon damaged:
    always:
        "pc backdrop damaged"

    always:
        "pc icon hurt"

    if Robyn_State["fHair"]:
        "pc facialhair"

    if Robyn_State["glasses"]:
        "pc glasses"

layeredimage pcIcon ko:
    always:
        "pc backdrop KO"
    always:
        "pc icon KO"

    if Robyn_State["fHair"]:
        "pc facialhair"

    if Robyn_State["glasses"]:
        "pc glasses"

image pc facialhair:
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Hair.webp"

image pc glasses:
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Glasses.webp"

image pc icon:
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Default.webp"

image pc icon exhausted:
    matrixcolor exIconHue(PC_Stats)
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Default.webp"

image pc icon hurt:
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Hurt.webp"
    fightIconHurt

image pc icon hurtidle:
    fightIconPos(tZoom=0.19,xAnchor=0.50)
    "images/Characters/Robyn/Battle/P_Icon_Hurt.webp"

image pc icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.19,xAnchor=0.50)

    "images/Characters/Robyn/Battle/P_Icon_Hurt.webp"

image pc backdrop:
    matrixcolor backdropHue(PC_Stats)
    fightIconPos(tZoom=0.19,xAnchor=0.55)
    "images/Characters/Robyn/Battle/P_Backdrop_Default.webp"

image pc backdrop selected:
    fightIconPos(tZoom=0.19,xAnchor=0.55)
    "images/Characters/Robyn/Battle/P_Backdrop_Selected.webp"

image pc backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.19,xAnchor=0.55)
    "images/Characters/Robyn/Battle/P_Backdrop_Default.webp"

image pc backdrop damaged:
    fightIconPos(tZoom=0.19,xAnchor=0.55)
    backdropDamaged("images/Characters/Robyn/Battle/P")
    xanchor 0.42

image pc backdrop KO:
    fightIconPos(tZoom=0.19,xAnchor=0.55)
    "images/Characters/Robyn/Battle/P_Backdrop_KO.webp"

# ----------------------------------------------------------------------- KOBOLD
image pc icon kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Robyn/Battle/P_Icon_Kobold.webp"

image pc backdrop kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Robyn/Battle/P_Backdrop_Kobold.webp"

image pc backdrop kobold damaged:
    xzoom 0.18
    yzoom 0.18


    xanchor 0.52
    yanchor 0.5
    "images/Characters/Robyn/Battle/P_Backdrop_Kobold_Damage.webp"
    pause 0.1
    xanchor 0.42
    pause 0.1
    xanchor 0.32
    "images/Characters/Robyn/Battle/P_Backdrop_Default.webp"
    pause 0.1
    "images/Characters/Robyn/Battle/P_Backdrop_Kobold.webp"
    xanchor 0.42
