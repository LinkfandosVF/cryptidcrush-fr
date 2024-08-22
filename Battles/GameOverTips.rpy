default persistent.firstGameOver = True
#persistent.unlockedDice[2] = True

image GameOver CG:
    xcenter 0.525
    ycenter 0.5
    yzoom 0.5
    xzoom 0.5
    "images/Props/GameOver1.webp"
    choice:
        pause 2.0
    choice:
        pause 1.0
    choice:
        pause 0.5
    choice:
        pause 3.0
    "images/Props/GameOver2.webp"
    pause 0.1
    "images/Props/GameOver3.webp"
    pause 0.1
    repeat

default curBattleNum = 0
default curInBattle = False
label gameOverScreen:
    camera:
        camera_zoom()
    $toggleQuickMenu(True)
    window hide
    scene black
    play music radiostatic fadein 4.0 fadeout 1.0
    stop music2
    show GameOver CG:
        on hide:
            xzoom 1.0
            yzoom 1.0
            ease 0.2 yzoom 5.0 xzoom 0

    with Dissolve(2.0)
    if curInBattle:
        pause 10.0
        $toggleQuickMenu(True)
        Atticus "Seems like you could use some help."

        hide GameOver CG
        $curBattleNum = 1
        call BattleAdvice(curBattleNum) from _call_BattleAdvice
    else:
        pause 10.0
        hide GameOver CG
        pause 1.0


    $renpy.load("Checkpoint")
    return

label BattleAdvice(bNum=0):
    camera:
        camera_zoom()
    scene BG Dream Zone Blur:
        xzoom -1
        matrixcolor HueMatrix(0)
        ease 6.0 matrixcolor HueMatrix(90)
        ease 10.0 matrixcolor HueMatrix(-60)
        block:
            ease 10.0 matrixcolor HueMatrix(90)
            ease 10.0 matrixcolor HueMatrix(-60)
            repeat
    show atticusdie:
        xcenter 0.5
        yoffset 30

    with Dissolve(2.0)

    Atticus "Seems like you're having a rough time of it. Would you like to change up your difficulty?{nw}"
    menu:
        extend ""

        "Human (Easy)":
            Atticus "Ah easy. This mode lowers the damage you and your allies take in battles as well as slightly making rolls easier."
            $gameDiff = persistent.gD = 1

        "Cryptid (Default)":
            Atticus "I see. Going with the intended difficulty."
            $gameDiff = persistent.gD = 2

        "Ghoul (Hard)":
            Atticus "So you're looking for a challenge. Ghoul essentially raises the damage/healing everyone takes. It's more explosive, but designed to be faster for those looking for low turn counts in battles."
            $gameDiff = persistent.gD = 3

        "Demon (Extra Hard)":
            Atticus "Oh you're a masochist. On top of raising all damage/healing values, this difficulty raises all roll difficulties as well."
            $gameDiff = persistent.gD = 4
        "No thanks":
            pass


    if persistent.firstGameOver:
        python:
            persistent.unlockedDice[2] = True
            persistent.firstGameOver = False


        Atticus "Since it's your first time here, how about I offer you up something to even the playing field? This is a new kinda dice called Lemon Squeezy. Even if you fail your rerolls, you still get a point of karma back.{nw}"

        menu:
            extend ""

            "Sure!":
                python:
                    persistent.dieSettings = 3
                    diceBot.setDieType(persistent.dieSettings)
                    pc_karma = diceBot.maxKarma


                voice atticus_chuckle
                Atticus "Wanna test them out?{nw}"

                menu:
                    extend ""

                    "Sure!":
                        call dice_roll(rMod=0, rDiff=7, rDesc="Test Roll") from _call_dice_roll_45

                        $pc_karma = diceBot.maxKarma
                    "No thanks.":
                        pass
            "Not my sorta thing":
                Atticus "No hard feelings bud."

    #Atticus "Alright then, need any advice for the battle ahead while we're here?{nw}"
    #menu:
    #    extend ""
    #    "I could use the help":
    #        $renpy.say(Atticus, renpy.random.choice(battleAdvice[bNum]))
    #    "No thanks, i'm a gamer":
    #        pass

    Atticus "Well then, good luck. I'm rooting for you."
    return

define battleAdvice = [
    ["Try using your karma defensively. You can always make a big attack another turn."], #0: ...
    ["Tuna Defender has taro Guard against all of Madhouses' moves for the party. Why not use that for some extra defense","Have you tried having Atlas reach out to madhouse? Might go pretty interestingly.", "Spirit Blaze deals supernatural damage, so if you can lower Madhouse's brains, that'll be even more powerful","If you figured out how to use Kinesis, that move lowers brains, so it'll do more damage using it back to back."], #1: Madhouse
    [""], #2
    [""], #3
    [""], #4
    ["Onslaught does a large amount of damage when August get's his damage buffed because of it being multi-hit.","Oz' Gut Punch lowers the target's Guts, so that could combo pretty easily into an attack from August.","Don't just ignore Mr. Walker. Take him out right before he gets a chance to attack, so he loses more time being reset back to his max MTA.","Silver Stab does a lot of damage to the lantern on a crit. Just watch the target's Occult since the damage scales with it."], #5: Mr. Walker
    [],
    []]


image floating_atticus_die:
    parallel:
        "images/Characters/Atticus Indrid/Dice/Atticus Dice Die1.webp"
        pause 1.3

        choice:
            pause 0.5
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die2.webp"
            pause 0.15
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die3.webp"
            pause 0.15
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die1.webp"
        choice:
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die2.webp"
            pause 0.15
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die3.webp"
            pause 0.15
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die1.webp"
        choice:
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die1.webp"
        choice:
            "images/Characters/Atticus Indrid/Dice/Atticus Dice Die1.webp"
    parallel:
        ease 1.5 yoffset -60
        ease 1.5 yoffset 0
    repeat

layeredimage atticusdie:
    yalign 1.0
    xcenter 0.5
    zoom 0.4

    always:
        "images/Characters/Atticus Indrid/Dice/Atticus Dice Base.webp"

    always:
        "images/Characters/Atticus Indrid/Dice/Atticus Dice Hand.webp"

    always:
        "floating_atticus_die"
