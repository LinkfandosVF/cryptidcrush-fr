init offset = -10
# -------------------------------------------------------------- Game Difficulty
default persistent.gD = 2
# 1 | Mortal
# 2 | Cryptid
# 3 | Demon

define gameDiffText = ["{color=#3AE9F6}Mortal","{color=#3bec27}Cryptid","{color=#e8850c}Ghoul","{color=#eb278d}Demon"]
init python:
    gameDiff = persistent.gD

# ------------------------------------------------------------------- UNIT CLASS
init python:

    class Unit: ##This defines what a unit is and has
        def __init__(self,name = "default", brawn = 0, brains = 0, hustle = 0, guts = 0, charm = 0, occult = 0, hp = 10): ##Default values and input
            self.name = name

            self.InmuneToStatChanges = False ## Immunization from changes

            self.maxHP = hp ##Setting HP
            self.cHP = self.maxHP
            self.isAlive = True ##dont commit the die.
            self.status = 0 ##Current status, 0 = normal, 1 = kobold, -1 = Special for Taro.

            self.MaxStamina = 4
            self.MinStamina = -4
            self.recoveryStamina = 1 ##Default stamina from recovery from exhaustion
            self.recoveryRate = 1 ##Rate at which units recover stamina per turn

            self.Defense = 2 ##Base defense. The default is 2 but usually increased for low-Guts bosses.

            self.Stamina = 4 ##Stamina, do not confuse, dom peepeepoopoo make your names more descriptive.
            self.exhausted = False ##Exhausted, they cannot act if this is True, if player has 2 stam, and use a 3 stam move, exhaustion happens.

            self.powerMod = 0 ## attack power Modifier, if its a number (1) then itll add to the attack (Attack+1)
            self.defenseMod = 0 ## Same as attack power modifier but for defense.

            self.rollMod = 0 ##Roll mod, if you roll 5, and you have rollmod = 1, then the roll is 6.
            self.HPChanged = 0 ##When someone took damage, this value stores the amount of damage done.

            self.attacks = [] ##List of attacks the unit can use, look at functions at the bottom.

            self.canTarget = True

            self.stats = { ##sets stats, used variably by attacks.
                "brawn": brawn, #Brawn, used for physical power
                "brawnMod": 0,
                "brains": brains, #Brains, used for investigations, smarts, resistances to mental effects.
                "brainsMod": 0,
                "hustle": hustle, #hustle, speed and dextirity.
                "hustleMod": 0,
                "guts": guts, #Guts, used for defense
                "gutsMod": 0,
                "charm": charm, #Charm, attractiveness, soothing tongue
                "charmMod": 0,
                "occult": occult, #occult, eldricth magic
                "occultMod": 0
            }


            self.isResistant = { ##Set resistances for types of attacks, if true, they receive reduced damage.
                "slashing": False,
                "bludgeoning": False,
                "burning": False,
                "numbing": False,
                "arcane": False,
                "normal": False
            }

            self.tempIsResistant = { ##Temporary resistances, applied by battle attacks or effects. Stacks with original resistances.
                "slashing": False,
                "bludgeoning": False,
                "burning": False,
                "numbing": False,
                "arcane": False,
                "normal": False
            }

            self.isVulnerable = { ##Weaknesses, same idea as resistances, as well as tIsVulnerable.
                "slashing": False,
                "bludgeoning": False,
                "burning": False,
                "numbing": False,
                "arcane": False,
                "normal": False
            }

            self.tempIsVulnerable = {
                "slashing": False,
                "bludgeoning": False,
                "burning": False,
                "numbing": False,
                "arcane": False,
                "normal": False
            }

            self.VulResPotency = 0.34


            ##Enemy exclusive stats:


            self.baseDiff = 0 ##Base difficulty (for enemies only)

            self.diffMod = 0 ##Difficult modifier. if enemy is getting stronger, the difficulty value will reflect that. 1-3 range.

            ##Visual Functions
            self.icon = None
            self.iconState = 0
            self.Color = "#ffffff"

            ##Enemy-Only
            self.MTA = 3 ##Moves until attack. Previously known as eDelay
            self.MaxMTA= 3 ##Default MTA, it resets to this value once the enemy does their move
            self.enemyAttackLabel = "" ##Label enemy uses on their turn
            self.NOCA = 1 ##Number of consecutive attacks
            self.CALeft = 1 ##ConsecutiveAttacksLeft, used for actual current attacks left.
            self.defaultCA = 1 ##How many attacks the enemy does when they act

            self.battleLines = {
                "success": ["<silence .5>"],
                "fail": ["<silence .5>"],
                "hurt": ["<silence .5>"]
            }


        ##Vocal Functions________________________________________
        def getLine(self,type = "hurt",num = -1):
            if (type in list(self.battleLines.keys())):
                xLine = ["audio/SFX Menu/Select_Choice_A.ogg"]
                if (num < 0 or num >= len(self.battleLines)):
                    xLine = self.battleLines[type]
                    return renpy.random.choice(xLine)
                else:
                    return self.battleLines[type][num]
            else:
                return "audio/SFX Menu/Select_Choice_A.ogg"

        def setLines(self,type = "hurt",xList = ["audio/SFX Menu/Select_Choice_A.ogg"]):
            if (type in list(self.battleLines.keys())):
                self.battleLines[type] = xList
        ##Stat functions_________________________________________
        def getcStats(self, isEnemy = False): #Returns all current stats as strings
            global pc_karma

            if not isEnemy: #Adds Name to the Text if a player unit
                tStats = self.name
                tStats = tStats + "\n- - - - - - -"

                #Brawn
                if self.cStats("brawn") > -1:
                    tStats = tStats + "\n[kwBrawnL]{color=#ff5342}: +" + str(self.cStats("brawn"))
                else:
                    tStats = tStats + "\n[kwBrawnL]{color=#ff5342}: " + str(self.cStats("brawn"))
            else:
                tStats = ""

                #Brawn
                if self.cStats("brawn") > -1:
                    tStats = tStats + "[kwBrawnL]{color=#ff5342}: +" + str(self.cStats("brawn"))
                else:
                    tStats = tStats + "[kwBrawnL]{color=#ff5342}: " + str(self.cStats("brawn"))

            stat_list = [('brains', 'a1fffc'), ('hustle','a7ff78'), ('guts','ff8941'), ('charm','ED2A82'), ('occult','b480ff')]
            for stat, stat_color in stat_list:
                stat_plus = "" if self.cStats(stat) < 0 else "+"
                tStats += "{/color}\n[kw"+ stat.capitalize() + "L]{color=#" + stat_color + "}: " + stat_plus + str(self.cStats(stat))

            if isEnemy != 2:
                #Defense Mod
                tStats = tStats + "{/color}\n[kwPDefenseL]{color=#3cb0d9}: +"    + str(self.cDefense("guts"))

                tStats = tStats + "{/color}\n[kwSDefenseL]{color=#3cb0d9}: +"    + str(self.cDefense("brains"))

                #Power Mod
                if self.powerMod > -1:
                    tStats = tStats + "\n{/color}[kwPowerModL]{color=#d05576}: +"    + str(self.powerMod)
                else:
                    tStats = tStats + "\n{/color}[kwPowerModL]{color=#d05576}: "    + str(self.powerMod)

                #Enemy Exclusive Stats
                if isEnemy:
                    tStats = tStats + "\n{/color}{color=#7aff44}Difficulty: " + str(self.cDifficulty())
                    tStats = tStats + "\n{/color}{color=#ffe603}MTA: " + str(self.MTA) + " more{/color}"

            else:
                tStats = tStats + "{/color}\n[kwKarmaL]{color=#fff069}: "      + str(pc_karma)

            return tStats

        def ChangeStats(self,hp = None,reset = True, **kwargs): ##Default values and input
            for key in kwargs:
                if key in self.stats:
                    self.stats[key] = kwargs[key]
                    if reset:
                        self.stats[key+"Mod"] = 0

            if hp is not None:
                self.maxHP = hp ##Setting HP

        def cPower(self, stat="brawn"): ##Stat is a key, statmod is a second key, then returns the power stat + its modifier, default is brawn
            statmod = stat + "Mod"
            return (self.powerMod + self.stats[stat] + self.stats[statmod])

        def cDefense(self, stat="guts"): ##Guts is defense, self.Defense is a base defense usually used for bosses with lower guts stats.%%
            statmod = stat + "Mod"
            tmpDef = self.Defense + self.stats[stat]
            if tmpDef < 0: ##Making sure it cannot be negative.
                tmpDef = 0
            tmpDef+= self.defenseMod + self.stats[statmod] ##Guts is also defense.
            return int(tmpDef)

        def cStats(self, stat="brawn"): #Call specific unit's stats for rolling.
            statmod = stat + "Mod"

            ##This might be better to add during battle instead of here TODO
            coolMod = 0 ##if stamina is at max, or below 0, it adds a modifier which is this.

            if self.exhausted:
                coolMod = -1

            if stat == "none":
                return coolMod

            ##Coolmod in the end just changes the value slightly depending if you are fresh or exhausted (1,0,-1)
            return self.stats[stat] + self.stats[statmod] + self.rollMod + coolMod

        def modifyStatMod(self,stat="brawn", mod=0, minVal = -4, maxVal = 4):
            if mod == 0:
                return

            cType = "lowered"
            cStat = ""
            xSign = ""
            xValue = 0

            if mod > 0:
                xSign = "+"
                temp = [audio.powerup_a,audio.powerup_a2,audio.powerup_a3]
                yValue = limitValue(mod,1,3)
                renpy.sound.play(temp[yValue-1],"sfx")
                renpy.show("powerup " + str(yValue))
                renpy.hide("powerdown")
                cType = "raised"
            elif mod < 0:
                temp = [audio.powerdown_a,audio.powerdown_a2,audio.powerdown_a3]
                yValue = limitValue(abs(mod),1,3)
                renpy.sound.play(temp[yValue-1],"sfx")
                renpy.show("powerdown " + str(yValue))
                renpy.hide("powerup")

            if stat == "rollMod":
                xValue = self.rollMod = limitValue(self.rollMod+mod, minVal, maxVal)
                cStat = "RollMod"
            elif stat == "power":
                xValue = self.powerMod = limitValue(self.powerMod+mod, minVal, maxVal)
                cStat = "PowerMod"
            elif stat == "defense":
                xValue = self.defenseMod = limitValue(self.defenseMod+mod, minVal, maxVal)
                cStat = "DefenseMod"
            elif stat == "diff":
                xValue = self.diffMod = limitValue(self.diffMod+mod, minVal, maxVal)
                cStat = "DifficultyMod"
            else:
                statmod = stat + "Mod"
                self.stats[statmod] = limitValue(self.stats[statmod]+mod, minVal, maxVal)
                xValue = self.cStats(stat)
                cStat = stat.capitalize()
                minVal+=self.stats[stat]
                maxVal+=self.stats[stat]

            cStat = globals()["kw" + cStat]

            ySign = ""
            if xValue >= 0:
                ySign = "+"

            curVal =  "! (current: " + ySign + str(xValue) + "){fast}"


            if xValue >= maxVal:
                renpy.say(Narrator, self.name + "'s " + cStat + " is maxed out" + curVal)
            elif xValue <= minVal:
                renpy.say(Narrator, self.name + "'s " + cStat + " is minimized" + curVal)
            else:
                renpy.say(Narrator, self.name + "'s " + cStat + " is " + cType + " by " +  xSign +str(mod) + curVal)

        def battleSFX(self,sfx):
            if renpy.sound.is_playing("sfx"):
                renpy.sound.queue(sfx,"sfx")
            else:
                renpy.sound.play(sfx,"sfx")
            return

        def modifyHP(self, mod=0, pierce=0.0, defType="guts",autoMsg=False,spareUnit=False): #Damage calculation and application, Pierce is a float that is multiplied by defenses. 0 to 1. 0 no pierce and 1 full pierce
            global sfxDmg, gameDiff

            if (not self.baseDiff) and (gameDiff < 2):
                if (mod < 0):
                    mod = limitValue(mod+2, mod, -1)
                elif (mod > 0):
                    mod+=2

            elif (gameDiff > 2):
                if (mod > 0):
                    mod+=2
                elif (mod < 0):
                    mod-=2


            xMod = mod #Number damage * Vulnerabilities/Res, positive mod increases hp, negative mod decreases it.
            self.HPChanged = 0

            if (xMod < 0): ##If receiving attack.
                if not self.isAlive:
                    return

                xDef = int(round((1-pierce)*self.cDefense(defType)))
                if xDef > 0 and pierce > 1 and self.cDefense(defType) <= 0:
                    xDef = int(round(-pierce))

                self.HPChanged = xMod + xDef
                if self.HPChanged >= 0: ##At least do ONE damage.
                    self.HPChanged = -1

                if spareUnit and abs(self.HPChanged) > self.cHP:
                    self.HPChanged = -(self.cHP-1)
                self.iconState = 2

            elif (xMod>0): ##If its healing...
                self.HPChanged = int(xMod)

            self.cHP+=self.HPChanged

            if (self.cHP == 0 and self.HPChanged < 0):
                self.cHP-=1
                self.HPChanged-=1

            sfxDmg = 0-self.HPChanged


            if sfxDmg > 0:

                if sfxDmg > 9:
                    self.battleSFX(audio.hurt_d) #10+
                elif sfxDmg > 6:
                    self.battleSFX(audio.hurt_c) #7-9
                elif sfxDmg > 3:
                    self.battleSFX(audio.hurt_b) #4-6
                else:
                    self.battleSFX(audio.hurt_a) #1-3

                if self.baseDiff == 0:
                    renpy.show_layer_at([camera_shake], layer='master', reset=False, camera=True)
                    if sfxDmg > 3:
                        voice(self.getLine())

                if autoMsg:
                    renpy.say(Narrator, self.name + " takes " + str(sfxDmg) + " damage!")

            elif sfxDmg < 0:
                if sfxDmg > -3:
                    self.battleSFX(audio.healing_b) #3-4
                elif sfxDmg > -6:
                    self.battleSFX(audio.healing_c) #5-7
                elif sfxDmg > -9:
                    self.battleSFX(audio.healing_d) #8-9
                else:
                    self.battleSFX(audio.healing_e) #10+

                if autoMsg:
                    renpy.say(Narrator, self.name + " regains " + str(regen) + " [kwHealth].")

            if (self.cHP <=0): ##Make the undead do be dead
                self.cHP = limitValue(self.cHP, -int(self.maxHP*0.5), 0)
                self.exhausted = False
                self.Stamina = 0

                if self.isAlive and self.baseDiff <= 0:
                    self.battleSFX(audio.ko)
                elif self.isAlive and self.baseDiff > 0:
                    self.MTA = self.MaxMTA

                self.isAlive = False
                self.InmuneToStatChanges = False
                self.CureStatus(False)
            else: ##Make the dead do be undead
                if self.cHP > self.maxHP:
                    self.cHP = self.maxHP
                self.isAlive = True

            if (self.HPChanged != 0):
                RefreshBarHP()


            return abs(self.HPChanged)

        def calcAggro(self):
            xAggro = 0

            if not self.isAlive:
                return xAggro

            #Max HP - some of current HP
            xAggro+= self.maxHP

            #Guts - Charm
            xAggro+= (abs(self.cStats("guts")) - self.cStats("charm"))*2.5

            #Missing HP added in
            xAggro+= (1 - self.cHP/self.maxHP)*10

            if self.powerMod > 0:
                xAggro+= 5*self.powerMod

            xAggro = int(xAggro*0.34)

            if xAggro < 1:
                xAggro = 1


            return xAggro
        ##Stamina functions________________________________________
        def canAct(self): ##Returns boolean that checks if stamina is up and its alive.
            if self.status in [1,2,3]:
                return False

            return (self.isAlive and not self.exhausted)

        def isBloodied(self):
            return (self.cHP < self.maxHP*0.5)

        def willMoveExhaust(self, xMod = 2): ##if xMod (stamina used by a skill or similar) will exhaust the player when they use it. a CHECK, not applies.
            return (xMod > self.Stamina)

        def modifyStamina(self, xMod = 2): ##Mod stamina, it absolutely changes the stamina. modCooldown(2) gains 2 stamina, -2 decreases, used for increased too
            if self.status == 1:
                return
            ##Positive values will increase stamina, negative values will decrease stamina.

            if self.isAlive: ##If alive, check if move will exhaust,
                self.Stamina += xMod ##Making stamina change by xMod

                if self.Stamina < self.MinStamina: ##RubberbandStamina
                    self.Stamina = self.MinStamina
                elif self.Stamina > self.MaxStamina: ##Maximum stamina
                    self.Stamina = self.MaxStamina
            else:
                regen = 1 - round(float(self.cHP*0.49))
                self.cHP+= regen
                RefreshBarHP()
                if self.cHP > 0:
                    renpy.say(Narrator, self.name + " gets back up.")
                    if self.baseDiff > 0:
                        self.cHP = 0
                    else:
                        if self.cHP > self.maxHP:
                            self.cHP = self.maxHP
                        self.isAlive = True
                else:
                    renpy.say(Narrator, self.name + " regains " + str(regen) + " [kwHealth].")

            if self.Stamina >= 1 and self.exhausted:#Recovering from exhaustion puts you to 2
                self.Stamina = self.recoveryStamina #Recovering from exhaustion puts you to 2
                self.exhausted = False
            elif self.Stamina <= -1 and not self.exhausted: ##Ensure that stamina is set to -2 so it can increase it sets of 2.
                self.exhausted = True

        ##Difficulty enemy functions______________________________
        def setDiffMod(self, val = 0):
            self.diffMod += val

        def resetDiffMod(self):
            self.diffMod = 0

        def cDifficulty(self, stat="none"): #Returns current difficulty, its a check not a changer. Can return difficulties based on specific stat.
            aDif = self.baseDiff + self.diffMod

            if stat != "none":
                aDif+= self.cStats(stat)

            if (aDif < 2):
                aDif = 2

            return aDif

        def cDiffAvg(self): ##Average difficulty of all stats. Whoops. all brawn, *0.17 to simmulate /6, weird behaviour.
            statAvg = int(((self.cStats("brawn") + self.cStats("brains") + self.cStats("guts") + self.cStats("hustle") + self.cStats("charm") + self.cStats("occult"))/6) + self.cDifficulty())

            return statAvg

        ##Status Effect functions_________________________________

        def InflictStatus(self, statusNumber=1, playSound = True):
            self.status = statusNumber
            if (statusNumber == 1):
                renpy.sound.play(audio.statuseffect_a,"sfx")
                self.modifyStamina(-8)
            elif (statusNumber == 4):
                self.modifyStatMod("guts",-2,-4,4)

            # 1: Sleep
            # 2: Stun
            # 3: Head in the cloudss
            # 4: Spooked: Can't use attacking moves

        def CureStatus(self,playSound = False):
            if(self.status == 1):
                modifyStamina(8)
                ##TODO Change icon back to normal from kobold.

            self.status = 0

        ##Vulnerability and Resistance functions___________________________________

        def toggleRes(self,dType): #Changes resistances. Used to enable OR disable. Called at the beginning of the battle, not temporary
            self.isResistant[dType] = not self.isResistant[dType]

        def toggleVul(self,dType): #Same as resistances but as vulnerabilities. Called at the beginning of the battle, not temporary.
            self.isVulnerable[dType] = not self.isVulnerable[dType]

        def toggleTRes(self,dType): #Changes resistances. Used to enable OR disable. Called at the beginning of the battle, not temporary
            self.tisResistant[dType] = not self.isResistant[dType]

        def toggleTVul(self,dType): #Same as resistances but as vulnerabilities. Called at the beginning of the battle, not temporary.
            self.tisVulnerable[dType] = not self.isVulnerable[dType]

        def resetSelf(self): #Resets all stats to base, ONLY MODIFIERS, the base stats remain.
            self.defenseMod = 0
            self.powerMod = 0
            self.stats["brawnMod"] = 0
            self.stats["brainsMod"] = 0
            self.stats["hustleMod"] = 0
            self.stats["gutsMod"] = 0
            self.stats["charmMod"] = 0
            self.stats["occultMod"] = 0
            self.rollMod = 0
            self.diffMod = 0
            self.exhausted = False
            self.InmuneToStatChanges = False
            self.cHP = self.maxHP

        def calculateTotalMatchup(self, dType = "normal"): #Mult for damage. checks vuln. and Res. and gives a flat number representing the accumulation of said things.
            xMod = 0
            if (self.isResistant[dType]):
                xMod +=1

            if (self.tIsResistant[dType]):
                xMod +=1

            if (self.isVulnerable[dType]):
                xMod -=1

            if (self.tIsVulnerable[dType]):
                xMod -=1

            return (1-(xMod*self.VulResPotency))

        def cIsResistant(self, dType = "normal"): #Boolean to return if you are resistant to some type of damage.
            return (self.cVulMod(dType) > 1)

        def cIsVulnerable(self,dType="normal"): #Same as Resistance.
            return (self.cVulMod(dType) < 1)

        def DiminishModifiers(self, type=[1]): ##Returns stats to normal after rolling/acting gradually. type is an array of stats used.
            # DiminishModifiers([1,2])
            #1 = Physical Stats
            #2 = Mental Stats
            #3 = Defense
            #4 = Power
            #5 = Roll Mod
            #6 = Difficulty Mod
            #7 = Reset vul and res

            stack = []

            if self.InmuneToStatChanges: ##If true, then stats will not be changed, not used yet, but for keeps stats rigid.
                pass
            else:
                for x in type:
                    if x < 3:
                        stack = ["brawnMod", "hustleMod", "gutsMod","brainsMod", "charmMod", "occultMod"]
                        for y in stack:
                            if (abs(self.stats[y]) > 0):
                                if (abs(self.stats[y]) == 1):
                                    self.stats[y] = 0
                                elif (self.stats[y] < 0):
                                    self.stats[y]+=2
                                else:
                                    self.stats[y]-=2

                    elif x == 3:
                        if (self.defenseMod !=0):
                            if (abs(self.defenseMod) == 1):
                                self.defenseMod = 0
                            elif (self.defenseMod < 0):
                                self.defenseMod+=2
                            else:
                                self.defenseMod-=2
                    elif x == 4:
                        if (self.powerMod !=0):
                            if (abs(self.powerMod) == 1):
                                self.powerMod = 0
                            elif (self.powerMod < 0):
                                self.powerMod+=2
                            else:
                                self.powerMod-=2
                    elif x == 5:
                        if (self.rollMod !=0):
                            if (abs(self.rollMod) == 1):
                                self.rollMod = 0
                            elif (self.rollMod < 0):
                                self.rollMod+=2
                            else:
                                self.rollMod-=2
                    elif x == 6:
                        if (self.diffMod !=0):
                            if (abs(self.diffMod) == 1):
                                self.diffMod = 0
                            elif (self.diffMod < 0):
                                self.diffMod+=2
                            else:
                                self.diffMod-=2


        ## Attack functions

        def SetAttackMoves(self, Attacks): ##You pass in an array of attacks, attacks are defined below this.
            self.attacks = Attacks

        ##Visual functions

        def SetIcon(self, icon):
            self.icon = icon

        ##Enemy-only functions

        def SetMTA(self, number): ##Set moves-til-attack
            self.MTA = number

        def SetMaxMTA(self, number):
            self.MaxMTA = number
            self.SetMTA(number)

        def ResetMTA(self):
            self.MTA = self.MaxMTA

        def ChangeMTA(self, number): ##Difference with previous is the previous sets, this one changes by a certain amount
            self.MTA += number
            if self.MTA < 0:
                self.MTA = 0

        def SetEnemyAttackLabel(self, elabel):
            self.enemyAttackLabel = elabel

        def SetNOCA(self, number): ##Set number of consecutive actions, enemy units may attack more than once when it's their turn, default is 1.
            self.NOCA = number
            self.ResetNOCA()

        def ResetNOCA(self):
            self.CALeft = self.NOCA

        def ChangeCALeft(self, number):
            self.CALeft += number
            if not self.isAlive:
                self.CALeft = 0

# -------------------------------------------------------------- UNIT SUBCLASSES
init python:
    class PlayerUnit(Unit):
        def __init__(self, name, stats):
            Unit.__init__(self, name, *stats)

        def getcStats(self):
            return Unit.getcStats(self)

        def setAttackPartner(self,aIndex = 0,pIndex = []):
            self.attacks[aIndex].comboUnit = pIndex

# ----------------------------------------------------------- ATTACK MOVES CLASS
init python:
    class AttackMove:
        def __init__(self, name = "defaultmovename", desc = "defaultmovedesc", staminaUsed = 1, attackLabel= "", unitMod = "brawn", enemyMod = "brawn", targetsAll = 0, isSupport = False, comboUnit = [], MTD =  10):
            self.name = name
            self.desc = desc
            self.targetsAll = targetsAll ## 0 for no, 1 for optionally, and 2 for always.
            self.isSupport = isSupport ## If True, the targets are your party rather than the enemy.
            self.attackLabel = attackLabel
            self.staminaUsed = staminaUsed
            self.comboUnit = comboUnit ##This is so for multi-unit attacks. it checks which units BESIDE the user use the attack, you pass in integers corresponding to their index in playerUnits.
            self.unitMod = unitMod ## Modifier used for attack by user
            self.enemyMod = enemyMod ## Modifier for enemy, can be set to integers and then checked wether or not is String or Integer
            self.MTD = MTD ##Multi-target difficulty, the game rolls this instead of enemy difficulty in case the player uses a multi-target move
        def copy(self):
            return AttackMove(self.name, self.desc, self.staminaUsed, self.attackLabel, self.unitMod, self.enemyMod, self.targetsAll, self.isSupport, self.comboUnit, self.MTD)




# --------------------------------------------------------------- REFERENCE CODE
# ------------------------------------------------------------------------- Unit
# init python:
#     class PUnit(PlayerUnit):
#         def __init__(self):
#             PlayerUnit.__init__(self, "{color=#C064FF}Taro{/color}", pcBaseStats)
#             self.SetIcon('taroIcon')
#
#         attack_desc = {
#             'Attack' :                "Description"
#         }
#
#         #                           AttackMove("Name",              "", -1, "", "stat", "resist/fixed", 0, False, [],11)
#         attack_bases = {
#             'Attack' :                AttackMove("Bash",              "", -1, "", "brawn",    "hustle",   0, False, [],0)
#         }
#
#         # Sets attack moves
#         # attacks: List of attack names to add. Should coorespond to keys in attack_bases.
#         # attack_label_base: String - The base label to construct label. Typically of the form 'FIGHT_00_MADLAS_ROBYN_'
#         # label_override: list of ints. If Robyn has several attacks that might not be in their set, make a separate list of numbers to help the function setup the attack label. This can be omitted from more traditional characters.
#         def SetAttackMoves(self, attacks, attack_label_base, label_override=None):
#             attack_list = []
#             for i, attack in enumerate(attacks):
#                 if attack in RobynUnit.attack_bases:
#                     new_attack = RobynUnit.attack_bases[attack].copy()
#                     new_attack.desc = RobynUnit.attack_desc[attack]
#                     new_attack.attackLabel = attack_label_base + str(i) if label_override is None else attack_label_base + str(label_override[i])
#                     attack_list.append(new_attack)
#             self.attacks = attack_list
