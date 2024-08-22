default Atlas_Stats = AtlasUnit()
# ------------------------------------------------------------------------- Unit
init python:
    class AtlasUnit(PlayerUnit):
        def __init__(self):
            PlayerUnit.__init__(self, "{color=#ED2A82}Atlas{/color}", [-1,2,2,-1,1,0,13])
            self.SetIcon('atlasIcon')
            self.Color = "#ED2A82"

            vLines = []
            vLines.append([audio.atlas_hurta, audio.atlas_hurtb, audio.atlas_hurtc, audio.atlas_hurtd])
            vLines.append([audio.atlas_faila, audio.atlas_failb, audio.atlas_failc])
            vLines.append([audio.atlas_successa, audio.atlas_successb, audio.atlas_successc, audio.atlas_successd, audio.atlas_successe])

            self.setLines("hurt",vLines[0])
            self.setLines("fail",vLines[1])
            self.setLines("success",vLines[2])

            # vLines = []
            # vLines.append([])
            # vLines.append([])
            # vLines.append([])
            #
            # self.setLines("hurt",vLines[0])
            # self.setLines("fail",vLines[1])
            # self.setLines("success",vLines[2])

        icon_dict = {
            "base": 'atlasIcon',
            "bird": 'birdlasIcon'
        }

        name_dict = {
            "base": "{color=#ED2A82}Atlas{/color}",
            "bird": "{color=#ED2A82}Birdlas{/color}"
        }

        stat_loadouts = {
            "base" : [-1,2,2,-1,1,0,13],
            "bird" : [-2,2,1,-2,1,3,13]
        }
        def setVariant(self,type="base"):
            self.SetIcon(AtlasUnit.icon_dict[type])

            self.name = AtlasUnit.name_dict[type]

            xVar = AtlasUnit.stat_loadouts[type]
            self.ChangeStats(hp=xVar[6],brawn=xVar[0],brains=xVar[1],hustle=xVar[2],guts=xVar[3],charm=xVar[4],occult=xVar[5])

        attack_desc = {
            'Lore Dump' :           "[kwSuccess]Deals piercing damage and significantly delays Target attack.\n\n[kwFailure] Move works but everyone's stamina is set to 0 (excluding Atlas).\n\nChecks [kwBrainsD] vs Fixed(10)\nCost: 3 Stamina",
            'Pump Up' :             "[kwSuccess] Jamie gains +1 stamina, and both their [kwOccultD] and [kwBrawn] are raised. \n\n[kwFailure] Jamie's [kwOccultD] and [kwBrawn] are raised slightly.\n\nChecks [kwCharm] vs Fixed(9)\nCost: 1 Stamina",
            'Kinesis' :             "[kwSuccess] Deals heavy damage, and lowers Target [kwBrainsD]. Atlas takes 30% recoil.\n\n[kwFailure] Move works but Atlas' [kwBrainsD] is lowered, and Atlas Takes 60% recoil.\n\nChecks [kwOccultD] vs [kwBrainsD]\nCost: 4 Stamina",
            'Reach Out' :           "(SPECIAL) Try to reason with Madhouse.",
            'Cryptic Collection' :  "[kwSuccess] Deals variable damage and increases Target [kwBrawnD]. Also decreases Target [kwBrainsD].\n\n[kwFailure] The Move fails..\n\nChecks [kwHustleD] vs [kwHustleD]\nCost: 1 Stamina",
            "PsyHeal" :             "[kwSuccess] Target(s) regain medium [kwHealth] or a lot when used on a single target.\n\n[kwFailure] Target(s) regain a reduced amount of [kwHealth]\n\nChecks [kwOccultD] vs Fixed(7)\nCost: 3 Stamina",
            "PsyFire" :             "[kwSuccess] Deals heavy damage. \n\n[kwFailure] Deals reduced damage.\n\nChecks [kwOccult] vs Fixed(7)\nCost: 3 Stamina",
            "PsyShield" :           "[kwSuccess] Raises all allies' [kwOccultD] and [kwBrainsD].\n\n[kwFailure] Move Fails. \n\nChecks [kwOccult] vs Fixed(8)\nCost: 2 Stamina",
            "PsyPeck" :             "[kwSuccess] Deals medium piercing damage, and lowers Target [kwGutsD].\n\n[kwFailure] Deals 1 damage.\n\nChecks [kwHustleD] vs [kwGutsD]\nCost: 2 Stamina",
            'KaCheer' :               "[kwSuccess] Slightly raises All allies' [kwRollModD] and Stamina by +1 except for Atlas'.\n\n[kwFailure] Move works, but raises Opponent [kwPowerMod].\n\nChecks [kwCharm] vs Fixed(7)\nCost: 2 Stamina",
            "Sabotage":             "[kwSuccess] Lowers Target [kwDifficultyModD] and raises their [kwMTAD] by +1.\n\n[kwFailure] Both the target and Atlas take damage. \n\nChecks [kwBrainsD] vs Fixed(12) \nCost: 1 Stamina",
            '--' :                "Description"
        }

        #                           AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Lore Dump' :           AttackMove("Lore Dump",                     "", -2, "", "brains", "fixed",  2, False, [],7),
            "KaCheer" :           AttackMove("KaCheer",                     "", -2, "", "charm", "fixed",  2, True,  [], 8),
            'Pump Up' :             AttackMove("Pump Up",                       "", -1, "", "charm",  "fixed",  2, True,  [],9),
            'Kinesis' :             AttackMove("Kinesis",                       "", -4, "", "occult", "brains", 0, False, [], 7),
            'Reach Out' :           AttackMove("Reach out",                     "",  0, "", "occult", "fixed",  2, True,  [],-1),
            'Cryptic Collection' :  AttackMove("Cryptic Collection",            "", -1, "", "hustle", "hustle", 0, False, [],10),
            "PsyHeal" :             AttackMove("PsyHeal",                       "", -3, "", "occult", "fixed",  1, True,  [], 7),
            "PsyFire" :             AttackMove("PsyFire",                       "", -3, "", "occult", "fixed",  1, False, [], 7),
            "PsyShield" :           AttackMove("PsyShield",                     "", -2, "", "occult", "fixed",  2, True,  [], 8),
            "PsyPeck" :             AttackMove("Psy{size=+2}{b}PECK{/b}{/size}","", -2, "", "hustle", "guts",   0, False, [],10),
            "Sabotage":             AttackMove("Sabotage",                     "", -1, "", "brains", "fixed",  2, False, [],12),
            '---' :               "Description"
        }

        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_Atlas_'
        # label_override: list of ints. If Atlas has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in AtlasUnit.attack_bases:
                    new_attack = AtlasUnit.attack_bases[attack].copy()
                    new_attack.desc = AtlasUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

# ------------------------------------------------------------------------- Icon
#-1:    KO
# 0:    Default
# 1:    Selected/Targeted
# 2:    Damaged

image atlasIcon:
    ConditionSwitch(
        "Atlas_Stats.iconState == 2","atlasIcon damaged",
        "Atlas_Stats.iconState == 3","atlasIcon spooky",
        "Atlas_Stats.iconState == -1 or not Atlas_Stats.isAlive","atlasIcon ko",
        "Atlas_Stats.exhausted","atlasIcon exhausted",
        "Atlas_Stats.iconState == 1","atlasIcon select",
        "True","atlasIcon base")

layeredimage atlasIcon base:
    always:
        "atlas backdrop"

    if not Atlas_Stats.isBloodied():
        "atlas icon"
    else:
        "atlas icon hurtidle"

layeredimage atlasIcon exhausted:
    always:
        "atlas backdrop exhausted"

    always:
        "atlas icon exhausted"

layeredimage atlasIcon spooky:
    always:
        "atlas backdrop spooky"

    always:
        "atlas icon spooky"

layeredimage atlasIcon select:
    always:
        "atlas backdrop selected"

    if not Atlas_Stats.isBloodied():
        "atlas icon"
    else:
        "atlas icon hurtidle"

layeredimage atlasIcon damaged:
    always:
        "atlas backdrop damaged"

    always:
        "atlas icon hurt"

layeredimage atlasIcon ko:
    always:
        "atlas backdrop KO"
    always:
        "atlas icon KO"

image atlas icon:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Icon_Default.webp"

image atlas icon spooky:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Icon_Spooky.webp"

image atlas icon exhausted:#
    matrixcolor exIconHue(Atlas_Stats)
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Icon_Default.webp"

image atlas icon hurt:
    fightIconPos(tZoom=0.16)


    "images/Characters/Atlas/Battle/Atlas_Icon_Hurt.webp"
    fightIconHurt

image atlas icon hurtidle:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Icon_Hurt.webp"

image atlas icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Icon_Hurt.webp"


define tempHPVar = 1#
image atlas backdrop:
    matrixcolor backdropHue(Atlas_Stats)
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Backdrop_Default.webp"

image atlas backdrop spooky:
    matrixcolor backdropHue(Atlas_Stats)*SaturationMatrix(1.5)
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Backdrop_Default.webp"

image atlas backdrop selected:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Backdrop_Selected.webp"

image atlas backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Backdrop_Default.webp"

image atlas backdrop KO:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Atlas_Backdrop_KO.webp"

image atlas backdrop damaged:
    fightIconPos(tZoom=0.16)
    backdropDamaged("images/Characters/Atlas/Battle/Atlas")

#Birdlas
image birdlasIcon:
    ConditionSwitch(
        "Atlas_Stats.iconState == 2","birdlasIcon damaged",
        "Atlas_Stats.iconState == -1 or not Atlas_Stats.isAlive","birdlasIcon ko",
        "Atlas_Stats.exhausted","birdlasIcon exhausted",
        "Atlas_Stats.iconState == 1","birdlasIcon select",
        "True","birdlasIcon base")

layeredimage birdlasIcon base:
    always:
        "birdlas backdrop"

    if not Atlas_Stats.isBloodied():
        "birdlas icon"
    else:
        "birdlas icon hurtidle"

layeredimage birdlasIcon exhausted:
    always:
        "birdlas backdrop exhausted"

    always:
        "birdlas icon exhausted"

layeredimage birdlasIcon select:
    always:
        "birdlas backdrop selected"

    if not Atlas_Stats.isBloodied():
        "birdlas icon"
    else:
        "birdlas icon hurtidle"

layeredimage birdlasIcon damaged:
    always:
        "birdlas backdrop damaged"

    always:
        "birdlas icon hurt"

layeredimage birdlasIcon ko:
    always:
        "birdlas backdrop KO"
    always:
        "birdlas icon KO"

image birdlas icon:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Icon_Default.webp"

image birdlas icon exhausted:#
    matrixcolor exIconHue(Atlas_Stats)
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Icon_Default.webp"

image birdlas icon hurt:
    fightIconPos(tZoom=0.16)


    "images/Characters/Atlas/Battle/Bird/Birdlas_Icon_Hurt.webp"
    fightIconHurt

image birdlas icon hurtidle:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Icon_Hurt.webp"

image birdlas icon KO:
    matrixcolor koIconHue()
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Icon_Hurt.webp"


image birdlas backdrop:
    matrixcolor backdropHue(Atlas_Stats)
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Backdrop_Default.webp"

image birdlas backdrop selected:
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Backdrop_Selected.webp"

image birdlas backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16)

    "images/Characters/Atlas/Battle/Bird/Birdlas_Backdrop_Default.webp"

image birdlas backdrop KO:
    fightIconPos(tZoom=0.16)
    "images/Characters/Atlas/Battle/Bird/Birdlas_Backdrop_KO.webp"

image birdlas backdrop damaged:
    fightIconPos(tZoom=0.16)
    backdropDamaged("images/Characters/Atlas/Battle/Bird/Birdlas")
