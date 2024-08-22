init offset = -1

default Gus_Stats = GusUnit()
# ------------------------------------------------------------------------- Unit
init python:
    class GusUnit(PlayerUnit):

        def __init__(self):
            PlayerUnit.__init__(self, "{color=#e8850c}August{/color}",[3,1,2,-2,1,-2,20])
            self.SetIcon("wolfGusIcon")
            self.Color = "#e8850c"

            vLines = []
            vLines.append([audio.august_damageda,audio.august_damagedb,audio.august_damagedc,audio.august_damagedd,audio.august_damagede,audio.august_damagedf,audio.august_damagedg])
            vLines.append([audio.august_faila,audio.august_failb,audio.august_failc])
            vLines.append([audio.august_successa,audio.august_successb])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

        stat_loadouts = {
            "base" : [3,2,1,-1,0,-2,18],
            _ : [],
        }
        def setVariant(self,type="base"):
            xVar = GusUnit.stat_loadouts[type]
            self.ChangeStats(hp=xVar[6],brawn=xVar[0],brains=xVar[1],hustle=xVar[2],guts=xVar[3],charm=xVar[4],occult=xVar[5])

        attack_desc = {
            'idWolf Howl' :       "[kwSuccess] Gus' next attack will do x3 damage. Gus maintains stat changes until he uses a different move.\n\n[kwFailure] Move works but his next attack will instead do x1.5 damage.\n\nChecks [kwGutsD] vs Fixed(7)\nCost: 1 Stamina",
            'Headlights!':      "[kwSuccess] Lowers Target [kwHustleD] and [kwDifficultyModD]. \n\n[kwFailure] Lowers Gus' [kwHustleD] and [kwRollModD].\n\nChecks [kwBrainsD] vs [kwHustleD]\nCost: 2 Stamina",
            'Pavlov Dog' :      "[kwSuccess] Deals low damage and lowers Gus' [kwGutsD]. Repeating this attack exponentially increases damage. Chain resets if Gus uses another move, or if he succeeds 3 times in a row. \n\n[kwFailure] Move works but resets chain.\n\nChecks [kwBrawn] vs [kwGutsD]\nCost: 1 Stamina",
            'Ephemeral Slash' : "[kwSuccess] Deals medium damage twice and lowers target [kwGutsD].\n\n[kwFailure] Move fails.\n\nChecks [kwBrawn] vs [kwHustleD]\nCost: 2 Stamina",
            'Be Polite' :       "[kwSuccess] Raises target [kwMTAD] and lowers their [kwPowerModD].\n\n[kwFailure] Raises target [kwPowerModD] and slightly lowers Gus' [kwCharmD].\n\nChecks [kwHustleD] vs Fixed(8)\nCost: 1 Stamina",
            'Look Out!' :       "Raises target's [kwCharmD] and [kwRollModD].\n\nCost: 2 Stamina",
            'Open Mike Nite' :  "Combo w/ Madhouse\n[kwSuccess] Deals heavy damage to all enemies, and regains [kwHealth] for all allies.\n\n[kwFailure] Move works, but [PCname] and Gus take damage.\n\nChecks [kwCharmD] vs Fixed(11)\nCost: 2 Stamina",
            'Words of Wisdom' :  "Combo w/ Atlas\n[kwSuccess] Greatly Raises Gus and Atlas' [kwPowerMod].\n\n[kwFailure] Gus takes severe emotional damage.\n\nChecks [kwCharmD] vs Fixed(10)\nCost: 1 Stamina",
            'Onslaught' :                '[kwSuccess] Deals Low damage 1-3 times. \n\n[kwFailure] Move works but additional hits are less likey.\n\nChecks [kwBrawnD] vs [kwHustleD]\nCost: 2 Stamina',
            'Howl' :                '[kwSuccess] Raises Gus’ [kwBrawnD]. Additionally raises target [kwMTAD].\n\n[kwFailure] Move works but lowers target [kwMTAD].\n\nChecks [kwCharmD] vs [kwBrainsD]\nCost: 2 Stamina',
            'Bite Back' :                '[kwSuccess] Raises [kwGutsD]. If an enemy attacks before you act next, you deal damage to the attacker. If used while active, the counter is strengthened.\n\n[kwFailure] Move works but instead lowers [kwGutsD]. \n\nChecks [kwBrawnD] vs Fixed(10) \nCost: 0 Stamina',
            'Sniff' :                '[kwSuccess] Lowers Target [kwDifficultyModD].\n\n[kwFailure] Move fails. \n\nChecks [kwBrainsD] vs Fixed(8) \nCost: 1 Stamina',
            '' :                '',
        }  #'Onslaught','Howl', 'Bite Back', 'Sniff'

        #     AttackMove("Name",              "", -stamcost, "", "stat", "resist/fixed", 0(1choice,2everyone), False, [],11)
        attack_bases = {
            'idWolf Howl' :          AttackMove("idWolf Howl",         '', -1, "", "guts",   "fixed",  2, True,  [],  7),
            'Headlights!':      AttackMove("Headlights!",       '', -3, "", "brains", "hustle", 0, False, [], 11),
            'Pavlov Dog' :      AttackMove("Pavlov Dog",        '', -1, "", "brawn",  "guts",   0, False, [], 11),
            'Ephemeral Slash' : AttackMove("Ephemeral Slash",   '', -2, "", "brawn",  "hustle", 0, False, [], 10),
            'Be Polite' :       AttackMove("Be Polite",         '', -1, "", "charm",  "brains", 0, False, [],  8),
            'Look Out!' :       AttackMove("Look Out!",         '', -2, "", "brains", "hustle", 0, True,  [], -1),
            'Open Mike Nite' :  AttackMove("Open Mike Nite",    '', -2, "", "charm",  "fixed",  2, False, [2],11),
            'Words of Wisdom' :  AttackMove("Parental Magic",    '', -1, "", "charm",  "fixed",  2, True,  [3],10),
            'Onslaught' :                AttackMove("Onslaught",              "", -2, "", "brawn", "hustle", 0, False, [],11),
            'Howl' :                AttackMove("Howl",              "", -2, "", "charm", "brains", 0, False, [],11),
            'Bite Back' :               AttackMove("Bite Back",              "", 0, "", "brawn", "fixed", 2, True, [],10),
            'Sniff' :                AttackMove("Sniff",              "",-1, "", "brains", "fixed", 0, False, [],8),
            '' :                AttackMove(),
        }

        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
        # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in GusUnit.attack_bases:
                    new_attack = GusUnit.attack_bases[attack].copy()
                    new_attack.desc = GusUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

        counterPow = 0
        idWolf = 1.0
# ------------------------------------------------------------------------- Icon
#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged
image gusIcon:
    ConditionSwitch(
        "Gus_Stats.iconState == 2","gusIcon damaged",
        "Gus_Stats.iconState == -1 or not Gus_Stats.isAlive","gusIcon ko",
        "Gus_Stats.exhausted","gusIcon exhausted",
        "Gus_Stats.iconState == 1","gusIcon select",
        "True","gusIcon base")

layeredimage gusIcon base:
    always:
        "gus backdrop"

    if not Gus_Stats.isBloodied():
        "gus icon"
    else:
        "gus icon hurtidle"

layeredimage gusIcon exhausted:
    always:
        "gus backdrop exhausted"
    always:
        "gus icon Exhausted"

layeredimage gusIcon select:
    always:
        "gus backdrop selected"

    if not Gus_Stats.isBloodied():
        "gus icon"
    else:
        "gus icon hurtidle"

layeredimage gusIcon damaged:
    if Gus_Stats.status == 1:
        "gus backdrop kobold damaged"
    else:
        "gus backdrop damaged"

    if Gus_Stats.status == 1:
        "gus icon kobold"
    else:
        "gus icon hurt"

layeredimage gusIcon ko:
    always:
        "gus backdrop KO"
    always:
        "gus icon KO"

image gus icon:
    fightIconPos(tZoom=0.18)

    "images/Characters/August/Battle/Gus_Icon_Default.webp"

image gus icon Exhausted:
    matrixcolor exIconHue(Gus_Stats)
    fightIconPos(tZoom=0.18)

    "images/Characters/August/Battle/Gus_Icon_Default.webp"

image gus icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.18)

    "images/Characters/August/Battle/Gus_Icon_Default.webp"


image gus icon hurt:
    fightIconPos(tZoom=0.18)

    "images/Characters/August/Battle/Gus_Icon_Default.webp"
    fightIconHurt

image gus icon hurtidle:
    fightIconPos(tZoom=0.18)

    "images/Characters/August/Battle/Gus_Icon_Default.webp"

image gus backdrop:
    matrixcolor backdropHue(Gus_Stats)
    fightIconPos(tZoom=0.19,xAnchor=0.5)
    "images/Characters/August/Battle/WolfGus_Backdrop_Default.webp"

image gus backdrop selected:
    fightIconPos(tZoom=0.19,xAnchor=0.5)

    "images/Characters/August/Battle/WolfGus_Backdrop_Selected.webp"

image gus backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.19,xAnchor=0.5)

    "images/Characters/August/Battle/WolfGus_Backdrop_Default.webp"

image gus backdrop damaged:
    fightIconPos(tZoom=0.19,xAnchor=0.5)
    backdropDamaged("images/Characters/August/Battle/WolfGus")

image gus backdrop KO:
    fightIconPos(tZoom=0.19,xAnchor=0.5)

    "images/Characters/August/Battle/WolfGus_Backdrop_KO.webp"

# ------------------------------------------------------------------------- Wolf
image wolfGusIcon:
    ConditionSwitch(
        "Gus_Stats.iconState == 2","wolfGusIcon damaged",
        "Gus_Stats.iconState == -1 or not Gus_Stats.isAlive","wolfGusIcon ko",
        "Gus_Stats.exhausted","wolfGusIcon exhausted",
        "Gus_Stats.iconState == 1","wolfGusIcon select",
        "True","wolfGusIcon base")

layeredimage wolfGusIcon base:
    always:
        "wolfGus backdrop"

    if not Gus_Stats.isBloodied():
        "wolfGus icon"
    else:
        "wolfGus icon hurtidle"

layeredimage wolfGusIcon exhausted:
    always:
        "wolfGus backdrop exhausted"
    always:
        "wolfGus icon Exhausted"

layeredimage wolfGusIcon select:
    always:
        "wolfGus backdrop selected"

    if not Gus_Stats.isBloodied():
        "wolfGus icon"
    else:
        "wolfGus icon hurtidle"

layeredimage wolfGusIcon damaged:
    if Gus_Stats.status == 1:
        "wolfGus backdrop kobold damaged"
    else:
        "wolfGus backdrop damaged"

    if Gus_Stats.status == 1:
        "wolfGus icon kobold"
    else:
        "wolfGus icon hurt"

layeredimage wolfGusIcon ko:
    always:
        "wolfGus backdrop KO"
    always:
        "wolfGus icon KO"

image wolfGus icon:
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Icon_Default.webp"

image wolfGus icon Exhausted:
    matrixcolor exIconHue(Gus_Stats)
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Icon_Default.webp"

image wolfGus icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Icon_Default.webp"

image wolfGus icon hurt:
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Icon_Hurt.webp"
    fightIconHurt

image wolfGus icon hurtidle:
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Icon_Default.webp"

image wolfGus backdrop:
    matrixcolor backdropHue(Gus_Stats)
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Backdrop_Default.webp"

image wolfGus backdrop selected:
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Backdrop_Selected.webp"

image wolfGus backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Backdrop_Default.webp"

image wolfGus backdrop damaged:
    fightIconPos(tZoom=0.18)
    backdropDamaged("images/Characters/August/Battle/WolfGus")

image wolfGus backdrop KO:
    fightIconPos(tZoom=0.18)
    "images/Characters/August/Battle/WolfGus_Backdrop_KO.webp"
