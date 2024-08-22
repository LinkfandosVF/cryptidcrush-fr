init offset = -1

default MM_Stats = MMUnit()
# ------------------------------------------------------------------------- Unit
init python:
    class MMUnit(PlayerUnit):
        def __init__(self):
            PlayerUnit.__init__(self, "{color=#3bec27}Madhouse{/color}",[0,-1,1,-1,2,2,12])
            self.SetIcon("madhouseIcon")
            self.Color = "#3bec27"

            vLines = []
            vLines.append([audio.mm_damageda,audio.mm_damagedb,audio.mm_damagedc,audio.mm_damagedd,audio.mm_damagede,audio.mm_damagedf,audio.mm_damagedg,audio.mm_damagedh])
            vLines.append([audio.mm_faila,audio.mm_failb,audio.mm_failc,audio.mm_faild,audio.mm_faile])
            vLines.append([audio.mm_successa,audio.mm_successb,audio.mm_successc,audio.mm_successd])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

        attack_desc = {
            'Hype Up' :             "[kwSuccess] Slightly raises Target(s)' [kwRollModD], and regains [kwHealth] when used on a single Target.\n\n[kwFailure] Move works, but raises Opponent [kwDifficultyModD].\n\nChecks [kwCharm] vs Fixed(10)\nCost: 1 Stamina",
            'Annoy' :               "[kwSuccess] Lowers Target [kwGutsD] and [kwBrainsD], but slightly raises their [kwPowerModD].\n\n[kwFailure] Move works but greatly raises their [kwPowerModD].\nChecks [kwCharm] vs [kwBrainsD]\nCost: 3 Stamina",
            'Kinesis' :             "[kwSuccess] Deals medium damage and lowers target [kwGutsD].\n\n[kwFailure] Move works but user takes heavy recoil.\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 3 Stamina",
            'Gossip Ghouls' :       "Combo w/ MM[kwSuccess] Sets Nekonomicon's [kwMTAD] to 0, but also lowers their [kwDifficultyModD] and [kwPowerModD].\n\n[kwFailure] Increases Nekonomicon's [kwDifficultyModD], but delays their turn.\nChecks [kwCharmD] vs Fixed(10)\nCost: 2 Stamina",
            'Noxious Fist' :        "[kwSuccess] Deals moderate damage and lowers target [kwBrainsD].\n\n[kwFailure] Move works deals reduced damage.\n\nChecks [kwGutsD] vs [kwGutsD]\nCost: 1 Stamina",
            'Polterheist' :         "[kwSuccess] Steals [kwBrainsD] and [kwOccultD] from the target.\n\n[kwFailure] The target steals [kwBrainsD] and [kwOccultD] from Madhouse.\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 3 Stamina",
            'EctoKinesis' :         "[kwSuccess] Deals medium damage.\n\n[kwFailure] The Skill misses entirely. \n\nChecks [kwOccultD] vs [kwHustleD]\nCost: 2 Stamina",
            'Ad Break' :            "[kwSuccess] Lowers Target [kwBrawn] and [kwHustleD] \n\n[kwFailure] Lowers Madhouse's [kwCharm] \n\nChecks [kwCharm] vs [kwBrainsD]\nCost: 2 Stamina",
            'Beyond the Grave' :    "[kwSuccess] Deals low damage, and Target regains 2 stamina. Exhausted Targets become unexhausted.\n\n[kwFailure] Move works but target takes increased damage \n\nChecks [kwOccultD] vs Fixed(10)\nCost: 2 Stamina",
            'Heckle' :            "User Regains +4 Stamina\n[kwSuccess] Raises Target [kwMTAD] and [kwDifficultyModD]. \n\n[kwFailure]  Lowers Target [kwDifficultyModD] and the target immediately acts. \n\nChecks [kwCharm] vs [kwBrainsD]",
            'Sucker Punch' :        "[kwSuccess] Deals Piercing damage to the target. \n\n[kwFailure] Target gets an attack on the user. \n\nChecks [kwCharm] vs [kwBrainsD]\nCost: 1 Stamina",
            'Flaunt' :                    "[kwSuccess] Raises target [kwMTAD] by +1, but causes them to make an attack on Radhouse..\n\n[kwFailure] Lowers target [kwMTAD] by -1.\n\nChecks [kwCharmD] vs [kwBrainsD]\nCost: 2 Stamina",
            'Weisheitsmüll' :                    "[kwSuccess] Deals piercing damage and significantly delays Target attack.\n\n[kwFailure] Move works but everyone's stamina is set to 0 (excluding Radhouse).\n\nChecks [kwBrainsD] vs Fixed(10)\nCost: 3 Stamina",
            'Grave Splitter' :                    "[kwSuccess] Deals physical and piercing supernatural damage to a target.\n\n[kwFailure] Move works but Radhouse also takes piercing supernatural damage.\n\nChecks [kwBrawnD] vs Fixed(8)\nCost: 2 Stamina",
            'Psycho-Kinesis' :                    "[kwSuccess] Deals devestating damage and lowers both target [kwBrainsD] and [kwGutsD]. \n\n[kwFailure] Move works but Radhouse also takes recoil damage and has both their [kwBrainsD] and [kwGutsD] lowered.\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 5 Stamina",
            'Not The Face' :                    "Target [kwMTAD] is lowered to 0 and both Madhouse's [kwDefenseModD] and [kwRollModD] are raised."
        }

        #Grave Splitter(2)
        #Success: Deals physical then piercing supernatural damage. Failure: Move works but Radhouse also takes piercing supernatural damage.

        #                           AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Hype Up' :         AttackMove("Hype Up",           '', -1, "", "charm",  "fixed",  1, True,  [], 10),
            'Annoy' :           AttackMove("Annoy",             '', -3, "", "charm",  "brains", 0, False, [], 11),
            'Kinesis' :         AttackMove("Kinesis",           '', -3, "", "occult", "brains", 0, False, [], 10),
            'Gossip Ghouls' :   AttackMove("Gossip Ghouls",     '', -2, "", "charm",  "fixed",  2, False, [1],10),
            'Noxious Fist' :    AttackMove("Noxious Fist",      '', -1, "", "brawn",   "guts",   0, False, [], 11),
            'Polterheist' :     AttackMove("Polterheist",       '', -3, "", "occult", "brains", 0, False, [], 10),
            'EctoKinesis' :     AttackMove("EctoKinesis",       '', -2, "", "occult", "brains", 0, False, [],  0),
            'Ad Break' :        AttackMove("Ad Break",          '', -2, "", "charm",  "brains", 0, False, [],  0),
            'Beyond the Grave': AttackMove("Beyond the Grave",  '', -2, "", "occult", "fixed",  0, True,  [], 10),
            'Heckle' :        AttackMove("Heckle",          '',  4, "", "charm", "brains",  0, False,  [], 10),
            'Sucker Punch' :    AttackMove("Sucker Punch",      '', -1, "", "charm", "brains",  0, False,  [], 10),
            'Flaunt' :          AttackMove("Flaunt",            '', -2, "", "charm", "brains",  0, False, [], 0),
            'Weisheitsmüll' :   AttackMove("Weisheitsmüll",     '', -3, "", "brains", "fixed",  0, False, [], 10),
            'Grave Splitter' :  AttackMove("Grave Splitter",    '', -2, "", "brawn", "fixed",  0, False, [], 8),
            'Psycho-Kinesis' :  AttackMove("Psycho-Kinesis",    '', -5, "", "occult", "brains",  0, False, [], 0),
            'Not The Face' :    AttackMove("Not The Face",      '', 0,  "", "occult", "fixed",  2, True, [], -1),
        }

        icon_dict = {
            "base": 'madhouseIcon',
            "dream": 'madhouseIcon'
        }

        name_dict = {
            "base": "{color=#3bec27}Madhouse{/color}",
            "dream": "{color=#3bec27}Radhouse{/color}"
        }

        stat_loadouts = {
            "base" : [0,-1,1,-1,2,2,13],
            "dream" : [1,-1,1,-2,2,2,14]
        }

        def setVariant(self,type="base"):
            self.SetIcon(MMUnit.icon_dict[type])

            self.name = MMUnit.name_dict[type]

            xVar = MMUnit.stat_loadouts[type]
            self.ChangeStats(hp=xVar[6],brawn=xVar[0],brains=xVar[1],hustle=xVar[2],guts=xVar[3],charm=xVar[4],occult=xVar[5])

        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
        # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in MMUnit.attack_bases:
                    new_attack = MMUnit.attack_bases[attack].copy()
                    new_attack.desc = MMUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

# ------------------------------------------------------------------------- Icon



#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged

image madhouseIcon:
    ConditionSwitch(
        "MM_Stats.iconState == 2","madhouseIcon damaged",
        "MM_Stats.iconState == -1 or not MM_Stats.isAlive","madhouseIcon ko",
        "MM_Stats.exhausted","madhouseIcon exhausted",
        "MM_Stats.iconState == 1","madhouseIcon select",
        "True","madhouseIcon base")

layeredimage madhouseIcon base:
    always:
        "madhouse backdrop"

    if not MM_Stats.isBloodied():
        "madhouse icon"
    else:
        "madhouse icon hurtidle"

layeredimage madhouseIcon exhausted:
    always:
        "madhouse backdrop exhausted"

    always:
        "madhouse icon Exhausted"

layeredimage madhouseIcon select:
    always:
        "madhouse backdrop selected"

    if not MM_Stats.isBloodied():
        "madhouse icon Selected"
    else:
        "madhouse icon hurtidle"

layeredimage madhouseIcon damaged:
    always:
        "madhouse backdrop damaged"

    always:
        "madhouse icon hurt"

layeredimage madhouseIcon ko:
    always:
        "madhouse backdrop KO"
    always:
        "madhouse icon KO"

image madhouse icon:
    fightIconPos(tZoom=0.155)
    "images/Characters/Madhouse/Battle/MM_Icon_Default.webp"

image madhouse icon Selected:
    fightIconPos(tZoom=0.155)
    "images/Characters/Madhouse/Battle/MM_Icon_Selected.webp"

image madhouse icon Exhausted:
    matrixcolor exIconHue(MM_Stats)
    fightIconPos(tZoom=0.155)
    "images/Characters/Madhouse/Battle/MM_Icon_Default.webp"

image madhouse icon hurt:
    fightIconPos(tZoom=0.155)
    "images/Characters/Madhouse/Battle/MM_Icon_Hurt.webp"
    fightIconHurt

image madhouse icon hurtidle:
    fightIconPos(tZoom=0.155)
    "images/Characters/Madhouse/Battle/MM_Icon_Hurt.webp"

image madhouse icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.155)

    "images/Characters/Madhouse/Battle/MM_Icon_Hurt.webp"


image madhouse backdrop:
    matrixcolor backdropHue(MM_Stats)
    fightIconPos(tZoom=0.16)
    "images/Characters/Madhouse/Battle/MM_Backdrop_Default.webp"

image madhouse backdrop selected:
    fightIconPos(tZoom=0.16)
    "images/Characters/Madhouse/Battle/MM_Backdrop_Selected.webp"

image madhouse backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16)

    "images/Characters/Madhouse/Battle/MM_Backdrop_Default.webp"

image madhouse backdrop KO:
    fightIconPos(tZoom=0.16)

    "images/Characters/Madhouse/Battle/MM_Backdrop_KO.webp"

image madhouse backdrop damaged:
    fightIconPos(tZoom=0.16)
    backdropDamaged("images/Characters/Madhouse/Battle/MM")

image mmicon = LayeredImageProxy("madhouseIcon")
