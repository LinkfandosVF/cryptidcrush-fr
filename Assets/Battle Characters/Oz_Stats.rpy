default Oz_Stats = OzUnit()

init python:
    class OzUnit(PlayerUnit):
        def __init__(self):
            PlayerUnit.__init__(self, "{color=#fffb42}Oz{/color}", [2,2,-2,1,1,-1,12])
            self.Color = "#fffb42"
            self.SetIcon("ozIcon")

            self.battleLines = {
                "success": ["<silence .5>"],
                "fail": ["<silence .5>"],
                "hurt": ["<silence .5>"],
                "crit": ["<silence .5>"]
            }

            vLines = []
            vLines.append([audio.oz_hurta,audio.oz_hurtb,audio.oz_hurtc,audio.oz_hurtd,audio.oz_hurte,audio.oz_hurtf])
            vLines.append([audio.oz_laugha,audio.oz_laughb,audio.oz_laughc])

            self.setLines("hurt",vLines[0])
            self.setLines("crit",vLines[1])

        attack_desc = { #'Silver Stab', 'Glare', 'Gut Punch', 'Bandage Wounds'
            'Silver Stab' :                "[kwSuccess] Deals moderate damage based on brains that increases the higher target [kwOccult] is. On a [critNum]+ roll, pierces defense. \n\n[kwFailure] Move fails.\n\nChecks [kwBrainsD] vs [kwHustleD]\nCost: 1 Stamina",
            'Glare' :                "[kwSuccess] Deals low piercing damage and slightly lowers target [kwPowerModD]. On a [critNum]+ roll, increases target [kwMTAD].\n\n[kwFailure] Move fails. \n\nChecks [kwCharmD] vs [kwBrainsD] \nCost: 1 Stamina",
            'Gut Punch' :                "[kwSuccess] Deals moderate damage and lowers target [kwGutsD]. On a [critNum]+ roll, greatly lowers target [kwGutsD] \n\n[kwFailure] Move works but deals reduced damage.\n\nChecks [kwBrawnD] vs [kwBrawnD]\nCost: 2 Stamina",
            'Bandage Wounds' :                "Target regains a large portion of [kwHealthD], and has their [kwRollMod] raised.\n\n If used without [kwKarmaD] , you gain +2 [kwKarmaD].\n\nCost: 1 [kwKarmaD]",
            '' :                ''
        }

        #                   AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
        attack_bases = {
            'Silver Stab' :                AttackMove("Silver Stab",              "", -1, "", "brains", "hustle", 0, False, [],11),
            'Glare' :                AttackMove("Glare",              "", -1, "", "charm", "brains", 0, False, [],11),
            'Gut Punch' :                AttackMove("Gut Punch",              "", -2, "", "brawn", "brawn", 0, False, [],11),
            'Bandage Wounds' :                AttackMove("Bandage Wounds",              "", 0, "", "hustle", "fixed", 0, True, [],-1),
            '' :                AttackMove()
        }



        # Sets attack moves
        # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
        # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
        # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
        def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
            attack_list = []
            for i, attack in enumerate(attacks):
                if attack in OzUnit.attack_bases:
                    new_attack = OzUnit.attack_bases[attack].copy()
                    new_attack.desc = OzUnit.attack_desc[attack]
                    new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
                    attack_list.append(new_attack)
            self.attacks = attack_list

image ozIcon:
    ConditionSwitch(
        "Oz_Stats.iconState == 2","ozIcon damaged",
        "Oz_Stats.iconState == 3","ozIcon crit",
        "Oz_Stats.iconState == -1 or not Oz_Stats.isAlive","ozIcon ko",
        "Oz_Stats.exhausted","ozIcon exhausted",
        "Oz_Stats.iconState == 1","ozIcon select",
        "True","ozIcon base")

layeredimage ozIcon base:
    always:
        "oz backdrop"

    if not Oz_Stats.isBloodied():
        "oz icon"
    else:
        "oz icon hurtidle"

layeredimage ozIcon exhausted:
    always:
        "oz backdrop exhausted"
    always:
        "oz icon exhausted"

layeredimage ozIcon select:
    always:
        "oz backdrop selected"

    if not Oz_Stats.isBloodied():
        "oz icon"
    else:
        "oz icon hurtidle"

layeredimage ozIcon damaged:
    # if Oz_Stats.status == 1:
    #     "oz backdrop kobold damaged"
    # else:

    always:
        "oz backdrop damaged"

    # if Oz_Stats.status == 1:
    #     "oz icon kobold"
    # else:

    always:
        "oz icon hurt"

layeredimage ozIcon ko:
    always:
        "oz backdrop KO"
    always:
        "oz icon KO"

layeredimage ozIcon crit:
    always:
        "oz backdrop"

    always:
        "oz icon crit"

image oz icon:
    fightIconPos(tZoom=0.16)
    "images/Characters/Oswald Howler/Battle/Oz_Icon_Default.webp"

image oz icon crit:
    fightIconPos(tZoom=0.16)
    ConditionSwitch(
        "Oz_Stats.isBloodied()","images/Characters/Oswald Howler/Battle/Oz_Icon_CritDrool.webp",
        "True","images/Characters/Oswald Howler/Battle/Oz_Icon_Crit.webp")

image oz icon exhausted:
    matrixcolor exIconHue(Oz_Stats)
    fightIconPos(tZoom=0.16)
    "images/Characters/Oswald Howler/Battle/Oz_Icon_Default.webp"

image oz icon hurt:
    fightIconPos(tZoom=0.16)
    ConditionSwitch(
        "Oz_Stats.isBloodied()","images/Characters/Oswald Howler/Battle/Oz_Icon_CritDrool.webp",
        "True","images/Characters/Oswald Howler/Battle/Oz_Icon_Hurt.webp")

    fightIconHurt

image oz icon hurtidle:
    fightIconPos(tZoom=0.16)
    "images/Characters/Oswald Howler/Battle/Oz_Icon_Crit.webp"

image oz icon KO:
    fightIconPos(tZoom=0.16)

    "images/Characters/Oswald Howler/Battle/Oz_Icon_Default.webp"
    matrixcolor koIconHue()

image oz backdrop:
    matrixcolor backdropHue(Oz_Stats)
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Oswald Howler/Battle/Oz_Backdrop_Default.webp"

image oz backdrop selected:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Oswald Howler/Battle/Oz_Backdrop_Selected.webp"

image oz backdrop exhausted:
    matrixcolor exBackdrop()
    fightIconPos(tZoom=0.16,xAnchor=0.48)

    "images/Characters/Oswald Howler/Battle/Oz_Backdrop_Default.webp"

image oz backdrop damaged:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    backdropDamaged("images/Characters/Oswald Howler/Battle/Oz")
    xanchor 0.48

image oz backdrop KO:
    fightIconPos(tZoom=0.16,xAnchor=0.48)
    "images/Characters/Oswald Howler/Battle/Oz_Backdrop_KO.webp"
