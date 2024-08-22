init offset = -1

default Jamie_Stats = JamieUnit()
# ------------------------------------------------------------------------- Unit
init python:
    class JamieUnit(PlayerUnit):
        def __init__(self):
            PlayerUnit.__init__(self, "{color=3AE9F6}Jamie{/color}", [1,2,-1,0,-2,3,13])
            self.Color = "#3AE9F6"
            self.SetIcon("jamieIcon")

            vLines = []
            vLines.append([audio.jamie_hurta, audio.jamie_hurtb, audio.jamie_hurtc, audio.jamie_hurtd, audio.jamie_hurte, audio.jamie_hurtf])
            vLines.append([audio.jamie_faila, audio.jamie_failb, audio.jamie_failc])
            vLines.append([audio.jamie_successa, audio.jamie_successb, audio.jamie_successc ])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

        attack_desc = {
            'Skull Cracker' :   "[kwSuccess] Deals medium piercing damage, and lowers Target [kwGutsD]. Jamie also takes 50% recoil\n\n[kwFailure] Move works, but Jamie takes 100% recoil, and slightly lowers their [kwGutsD].\n\nChecks [kwGutsD] vs [kwGutsD]\nCost: 1 Stamina",
            'Spirit Blaze' :    "[kwSuccess] Deals heavy damage to all enemies.\n\n[kwFailure] Deals reduced damage to everyone in the fight.\n\nChecks [kwOccultD] vs Fixed(11)\nCost: 3 Stamina",
            'Healing Wave' :    "[kwSuccess] Target(s) regain medium [kwHealth] or a lot when used on a single target.\n\n[kwFailure] Target(s) regain a reduced amount of [kwHealth]\n\nChecks [kwOccultD] vs Fixed(10)\nCost: 3 Stamina",
            'FluxFlare' :       "[kwSuccess] Deals devestating damage.\n\n[kwFailure] Everyone takes reduced damage. Also raises everyone's [kwBrawn].\n\nChecks [kwOccultD] vs Fixed(11)\nCost: 4 Stamina",
            'ChainFlare' :     "[kwSuccess] Deals medium physical damage, and then low piercing magical damage. Lowers Target [kwHustleD] on the second hit.\n\n[kwFailure] Move works but only hits once.\n\nChecks [kwBrawnD] vs [kwHustleD]\nCost: 2 Stamina",
            'See You in Hell' :                "[kwSuccess] Deals damage to both a Target & Taro. If Taro is KOed, damage is increased drastically.\n\n[kwFailure] Move fails but Taro still takes damage.\n\nChecks [kwOccultD] vs [kwHustleD]\nCost: 2 Stamina",
            'Inescapable Flex' :                "Raises [kwRollModD] for all allies, as well as [kwPowerModD] for Jamie. Additionally increases all Enemy [kwMTAD] by +1. If Used without Karma, only raises Jamie's [kwPowerModD].\n\nCost: 1 [kwKarmaD]",
            'Hellhound Hurricane':              "[kwSuccess] Deals both physical and supernatural damage to a Target. \n\n[kwFailure] Move works but August takes moderate recoil.\n\nChecks [kwOccultD] vs Fixed(11)\nCost: 3 Stamina"
        }

        #                           AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Skull Cracker' :   AttackMove("Skull Cracker", '', -1, "", "guts",   "guts",   0, False, [],  0),
            'Spirit Blaze' :    AttackMove("Spirit Blaze",  '', -3, "", "occult", "fixed",  2, False, [], 11),
            'Healing Wave' :    AttackMove("Healing Wave",  '', -3, "", "occult", "fixed",  1, True,  [], 10),
            'FluxFlare' :       AttackMove("FluxFlare",     '', -3, "", "occult", "fixed",  2, False, [0],12),
            'ChainFlare' :     AttackMove("ChainFlare",   '', -2, "", "brawn",  "hustle", 0, False, [],  7),
            'See You in Hell' :                AttackMove('See You in Hell', '', -2, "", "occult",   "hustle",   0, False, [],  0),
            'Inescapable Flex' :                AttackMove('Inescapable Flex', '', 0, "", "guts",   "fixed",   2, True, [],  -1),
            'Hellhound Hurricane': AttackMove('Hellhound Hurricane', '', -3, "", "occult",   "fixed",   0, False, [1],  11),
            '' :                AttackMove(),
        }

        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
        # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in JamieUnit.attack_bases:
                    new_attack = JamieUnit.attack_bases[attack].copy()
                    new_attack.desc = JamieUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

# ------------------------------------------------------------------------- Icon
#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged

image jamieIcon:
    ConditionSwitch(
        "Jamie_Stats.iconState == 2","jamieIcon damaged",
        "Jamie_Stats.iconState == 3","jamieIcon glow",
        "Jamie_Stats.iconState == -1 or not Jamie_Stats.isAlive","jamieIcon ko",
        "Jamie_Stats.exhausted","jamieIcon exhausted",
        "Jamie_Stats.iconState == 1","jamieIcon select",
        "True","jamieIcon base")

layeredimage jamieIcon base:
    always:
        "jamie backdrop"

    if not Jamie_Stats.isBloodied():
        "jamie icon"
    else:
        "jamie icon hurtidle"

layeredimage jamieIcon exhausted:
    always:
        "jamie backdrop exhausted"
    always:
        "jamie icon exhausted"

layeredimage jamieIcon select:
    always:
        "jamie backdrop selected"

    if not Jamie_Stats.isBloodied():
        "jamie icon"
    else:
        "jamie icon hurtidle"

layeredimage jamieIcon damaged:
    # if Jamie_Stats.status == 1:
    #     "jamie backdrop kobold damaged"
    # else:

    always:
        "jamie backdrop damaged"

    # if Jamie_Stats.status == 1:
    #     "jamie icon kobold"
    # else:

    always:
        "jamie icon hurt"

layeredimage jamieIcon ko:
    always:
        "jamie backdrop KO"
    always:
        "jamie icon KO"

layeredimage jamieIcon glow:
    always:
        "jamie backdrop glow"

    always:
        "jamie icon glow"

image jamie icon:
    fightIconPos(tZoom=0.16)
    "images/Characters/Jamie/Battle/Jamie_Icon_Default.webp"

image jamie icon exhausted:
    matrixcolor exIconHue(Jamie_Stats)
    fightIconPos(tZoom=0.16)
    "images/Characters/Jamie/Battle/Jamie_Icon_Default.webp"

image jamie icon glow:
    fightIconPos(tZoom=0.16)
    "images/Characters/Jamie/Battle/Jamie_Icon_Glow.webp"

image jamie icon hurt:
    fightIconPos(tZoom=0.16)
    "images/Characters/Jamie/Battle/Jamie_Icon_Hurt.webp"
    fightIconHurt

image jamie icon hurtidle:
    fightIconPos(tZoom=0.16)
    "images/Characters/Jamie/Battle/Jamie_Icon_Hurt.webp"

image jamie icon KO:
    fightIconPos(tZoom=0.16)

    "images/Characters/Jamie/Battle/Jamie_Icon_Hurt.webp"
    matrixcolor koIconHue()

image jamie backdrop:
    matrixcolor backdropHue(Jamie_Stats)
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Default.webp"

image jamie backdrop glow:
    matrixcolor HueMatrix(90)*BrightnessMatrix(-0.1)
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Default.webp"

image jamie backdrop selected:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Selected.webp"

image jamie backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16,xAnchor=0.48)

    "images/Characters/Jamie/Battle/Jamie_Backdrop_Default.webp"

image jamie backdrop damaged:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    backdropDamaged("images/Characters/Jamie/Battle/Jamie")
    xanchor 0.48

image jamie backdrop KO:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Jamie/Battle/Jamie_Backdrop_KO.webp"

# ----------------------------------------------------------------------- Kobold
image jamie icon kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Jamie/Battle/Jamie_Icon_Kobold.webp"

image jamie backdrop kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Kobold.webp"

image jamie backdrop kobold damaged:
    xzoom 0.18
    yzoom 0.18


    xanchor 0.52
    yanchor 0.5
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Kobold_Damage.webp"
    pause 0.1
    xanchor 0.42
    pause 0.1
    xanchor 0.32
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Default.webp"
    pause 0.1
    "images/Characters/Jamie/Battle/Jamie_Backdrop_Kobold.webp"
    xanchor 0.42
