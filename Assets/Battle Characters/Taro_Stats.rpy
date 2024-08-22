init offset = -1

default Taro_Stats = TaroUnit()
# ------------------------------------------------------------------------- Unit
init python:
    class TaroUnit(PlayerUnit):
        taroTuna = False

        def __init__(self):
            PlayerUnit.__init__(self, "{color=#C064FF}Taro{/color}", [2,-1,1,2,0,-1,15])

            self.Color = "#C064FF"
            self.SetIcon("taroIcon")

            vLines = []
            vLines.append([audio.taro_damageda,audio.taro_damagedb,audio.taro_damagedc,audio.taro_damagedd,audio.taro_damagede,audio.taro_damagedf])
            vLines.append([audio.taro_faila,audio.taro_failb,audio.taro_failc,audio.taro_faild])
            vLines.append([audio.taro_successa,audio.taro_successb,audio.taro_successc,audio.taro_successd])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

        stat_loadouts = {
            "base" : [2,-1,1,2,0,-1,15],
            "dream" : [4,-1,-3,2,0,-1,15]
        }
        def setVariant(self,type="base"):
            xVar = TaroUnit.stat_loadouts[type]
            self.ChangeStats(hp=xVar[6],brawn=xVar[0],brains=xVar[1],hustle=xVar[2],guts=xVar[3],charm=xVar[4],occult=xVar[5])

        def modifyHP(self, mod=0, pierce=0.0, defType="guts"):
            xHp = PlayerUnit.modifyHP(self,mod, pierce, defType)
            if not self.isAlive:
                self.taroTuna = False

            return xHp

        attack_desc = {
            'Pounce' :               "[kwSuccess] Deals medium damage to Target. When Taro is at 5 [kwHealth] or lower, deals heavy damage.\n\n[kwFailure] Deals reduced damage to Target\n\nChecks [kwBrawn] vs [kwHustleD]\nCost: 2 Stamina",
            'Tuna Defender' :        "[kwSuccess] Taro intercepts all incoming attacks, and slightly raises her [kwDefenseMod]. Taro maintains stat changes until she uses a different move.\n\n[kwFailure] Move works, but slightly lowers Taro's [kwDefenseMod]. Also raises her [kwPowerMod].\n\nChecks [kwGutsD] vs Fixed(7)",
            'Jeer' :                 "[kwSuccess] Lowers Target [kwPowerMod], and slightly lowers their [kwDifficultyModD].\n\n[kwFailure] Raises Target [kwPowerMod]\n\nChecks [kwCharm] vs [kwBrainsD]\nCost: 3 Stamina",
            'HexFlare' :             "[kwSuccess] Deals medium damage and increases Taro's [kwBrawnD].\n\n[kwFailure] Move Works but lower's Taro's [kwGutsD] and [kwBrainsD].\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 1 Stamina",
            'Meow-raculous Suplex' : "[kwSuccess] Deals heavy damage and delays the Target's attack slightly.\n\n[kwFailure] Move fails. \n\nChecks [kwBrawn] vs [kwHustleD]\nCost: 4 Stamina",
            'The Cats Meow' :        "Combo w/ [PCname]\n[kwSuccess] Greatly raises Taro's [kwPowerModD] and slightly raises her [kwDefenseModD].\n\n[kwFailure] Move works but the [kwPowerModD] gained is reduced.\nChecks [kwCharm] vs Fixed(8)\nCost: 2 Stamina",
            'No Brakes' :            "Combo w/ Gus\n\n[kwSuccess] Deals heavy damage to all enemies. \n\n[kwFailure] Move works, but Gus also takes damage.\n\nChecks [kwOccultD] vs Fixed(7)\nCost: 3 Stamina",
            '---' :                  "Description"
        }

        #                             AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Pounce' :                AttackMove("Pounce",              "", -2,  "", "brawn",  "hustle", 0, False, [], 0),
            'Tuna Defender' :         AttackMove("Tuna Defender",       "", 0,   "", "guts",   "fixed",  2, True,  [], 7),
            'Jeer' :                  AttackMove("Jeer",                "" , -3, "", "charm",  "brains", 0, False, [],10),
            'HexFlare' :              AttackMove("HexFlare",            "", -1,  "", "occult", "brains", 0, False, [],11),
            'Meow-raculous Suplex' :  AttackMove("Meow-raculous Suplex","", -4,  "", "brawn",  "hustle", 0, False, [], 0),
            'The Cats Meow' :         AttackMove("The Cat's Meow",      "", -2,  "", "charm",  "fixed",  2, True,  [0],8),
            'No Brakes' :             AttackMove("No Brakes",           "", -3,  "", "occult", "fixed",  2, False, [3],9),
            '---' :                   AttackMove(),
        }

        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_Taro_'
        # label_override: list of ints. If Taro has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in TaroUnit.attack_bases:
                    new_attack = TaroUnit.attack_bases[attack].copy()
                    new_attack.desc = TaroUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list


        def pounceMult(self,dmg=0):
            if self.cHP <= 5:
                return int(dmg*1.5)

            return dmg

# ------------------------------------------------------------------------- Icon
#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged

image taroIcon:

    ConditionSwitch(
        "Taro_Stats.iconState == 2","taroIcon damaged",
        "Taro_Stats.iconState == -1 or not Taro_Stats.isAlive","taroIcon ko",
        "Taro_Stats.exhausted","taroIcon exhausted",
        "Taro_Stats.iconState == 1","taroIcon select",
        "True","taroIcon base")

layeredimage taroIcon base:
    always:
        "taro backdrop"

    if not Taro_Stats.isBloodied():
        "taro icon"
    else:
        "taro icon hurtidle"

layeredimage taroIcon exhausted:
    always:
        "taro backdrop exhausted"
    always:
        "taro icon Exhausted"

layeredimage taroIcon select:
    always:
        "taro backdrop selected"

    if not Taro_Stats.isBloodied():
        "taro icon"
    else:
        "taro icon hurtidle"

layeredimage taroIcon damaged:

    always:
        "taro backdrop damaged"

    always:
        "taro icon hurt"

layeredimage taroIcon ko:
    always:
        "taro backdrop KO"
    always:
        "taro icon KO"

image taro icon:
    fightIconPos(tZoom=0.16)
    "images/Characters/Taro/Battle/Taro_Icon_Default.webp"

image taro icon Exhausted:
    matrixcolor exIconHue(Taro_Stats)
    fightIconPos(tZoom=0.16)
    "images/Characters/Taro/Battle/Taro_Icon_Default.webp"

image taro icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.16)
    "images/Characters/Taro/Battle/Taro_Icon_Hurt.webp"

image taro icon hurt:
    fightIconPos(tZoom=0.16)
    "images/Characters/Taro/Battle/Taro_Icon_Hurt.webp"
    fightIconHurt

image taro icon hurtidle:
    fightIconPos(tZoom=0.16)
    "images/Characters/Taro/Battle/Taro_Icon_Hurt.webp"

image taro backdrop:
    matrixcolor backdropHue(Taro_Stats)
    fightIconPos(tZoom=0.16,xAnchor=0.45)
    "images/Characters/Taro/Battle/Taro_Backdrop_Default.webp"

image taro backdrop selected:
    fightIconPos(tZoom=0.16,xAnchor=0.45)
    "images/Characters/Taro/Battle/Taro_Backdrop_Selected.webp"

image taro backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16,xAnchor=0.45)
    "images/Characters/Taro/Battle/Taro_Backdrop_Default.webp"

image taro backdrop damaged:
    fightIconPos(tZoom=0.16)
    backdropDamaged("images/Characters/Taro/Battle/Taro")
    xanchor 0.45

image taro backdrop KO:
    fightIconPos(tZoom=0.16,xAnchor=0.45)
    "images/Characters/Taro/Battle/Taro_Backdrop_KO.webp"

# ----------------------------------------------------------------------- Kobold
image taro icon kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Taro/Battle/Taro_Icon_Kobold.webp"

image taro backdrop kobold:
    xzoom 0.18
    yzoom 0.18

    xanchor 0.42
    yanchor 0.5
    "images/Characters/Taro/Battle/Taro_Backdrop_Kobold.webp"

image taro backdrop kobold damaged:
    xzoom 0.18
    yzoom 0.18


    xanchor 0.52
    yanchor 0.5
    "images/Characters/Taro/Battle/Taro_Backdrop_Kobold_Damage.webp"
    pause 0.1
    xanchor 0.42
    pause 0.1
    xanchor 0.32
    "images/Characters/Taro/Battle/Taro_Backdrop_Default.webp"
    pause 0.1
    "images/Characters/Taro/Battle/Taro_Backdrop_Kobold.webp"
    xanchor 0.42
