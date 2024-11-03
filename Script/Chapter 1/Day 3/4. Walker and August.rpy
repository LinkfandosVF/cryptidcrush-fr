label Ch1_WalkingHome_Day3:

    scene BG Autumn Road
    camera at camera_default:
        shaded("#ffe7ee")

    python:
        Bush = Character("Stranger", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "1A", who_color = "#ea3c53")
        Bush2 = Character("Stranger", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "4C", who_color = "#fffb42")
        timeText = "5:00PM"
        musicPlayer.playSong(fadeOut=1.5)
        HighlightEnemyUnitBars([])
        HighlightPlayerUnitBars([])

    with Dissolve (0.5)
    $musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=1,fadeOut=2)
    play ambiance forest_ambianceb fadein 5.0 fadeout 4.0
    Narrator "Time to make the trek back home."
    Narrator "Yeesh, it’s cold. You could see the sunset from here if the tree line didn’t block the view. You’re pretty high up the ridge."

    $PC_Stats = RobynUnit()

    python:
        Who_Stats = Unit("{color=#ea3c53}???{/color}",5,1,1,0,-1,1,25)
        Who_Stats.cHP = 20
        Who_Stats.baseDiff = 8
        PC_Stats = RobynUnit()
        playerUnitsInit("PC")
        enemyUnitsInit("Who")
        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0])

    Bush "What's a duckling like you doing wandering around a ghost town like this?"

    Narrator "An artificially deep, metallic voice rings out through the chilled air."

    Bush "There are wolves you know."

    call dice_roll(rMod=0, rDiff=9, rDesc="Perception") from _call_dice_roll_69

    if isRollSuccess:

        if ch1_alreadyMetHound:
            camera:
                    camera_zoom(x=20,y=10,z=-400,t=0.8)

            #musicPlayer.playSong(song="its_off")

            play music its_off_song
            Robyn "{b}Hound{/b}? Are you following me?"
            show hound at climbfromhole:
                xcenter 0.53
                shaded("#ffc6c1")
            python:
                HighlightEnemyUnitBars([])
                HighlightPlayerUnitBars([])
                adjustChar("Hound",eyes=4,eyeFrame=1)

            Hound "You've got a sharp eye."

            $adjustChar("Hound",eyes=0)

            Hound "{b}No{/b},, I have no interest following the likes of you."

            Hound "I'm patrolling the area."

            Robyn "Well stop it. You're creeping people out."

            $adjustChar("Hound",eyes=2)
            Hound "Hm, fair. I'll try to behave."

            Robyn "Sooo, you're August's brother in-law huh? Who's the lucky someone?"

            $adjustChar("Hound",eyes=0)

            show hound at startledSquish
            Hound "He told you?"

            $adjustChar("Hound",eyes=4)

            Robyn "Is that bad?"
            $adjustChar("Hound",eyes=3)

            Hound "A bit,, but that's fine. I'm just bashful."

            Hound "I'd like to keep my personal and work life separate."

            $adjustChar("Hound",eyes=4)
            show hound:
                matrixtransform rotated(z=0)
                ease 0.6 matrixtransform rotated(z=15)
            Hound "Now, if I may be so bold,, are you a human?"

            Robyn "Yeah? That's a weird question."
            stop music

            $adjustChar("Hound",eyes=0,eyeFrame=0)
            camera:
                camera_zoom(z=-550,x=40,y=-20,t=0.25)
            houndyell2 "{size=25}I don't believe you.{/size}"

            Robyn "{sc=2}What?{/sc}"

            $adjustChar("Hound",eyes=3,eyeFrame=1)

            show hound:
                matrixtransform rotated(y=0,z=15)
                ease 0.6 matrixtransform rotated(y=180,z=0)

            Hound "I don't believe it's an odd question!"
            $adjustChar("Hound",eyes=2)

            Hound "No need to act so nervous."

            show hound:
                unflipCharDelayed(0.8,0.5)
                ease 2.5 xcenter -0.5
            Hound "Us humans gotta stick together after all."

            camera:
                camera_zoom(y=-20,z=-550,x=40)
                camera_zoom(y=20, z=-20,t=4.0)

            Narrator "The wanderer saunters off, venturing into the woods. You're alone again."
        else:
            show CG Stranger
            with { "master" : Dissolve(0.5) }

            Narrator "You catch the faint outline of an imposing figure lurking in the brush. They're looking away from you, as if listening for something. Waiting."

            Robyn "What do you want?"

            Bush "Nothing you could give."

            Narrator "Well, whoever the hell that was, they seem to be gone now."


    else:
        Narrator "You can't see who's speaking."

    python:
        HighlightEnemyUnitBars([])
        HighlightPlayerUnitBars([])
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1,fadeOut=2)
    hide CG Stranger
    with { "master" : Dissolve(0.5) }

    Robyn "Mike you there?"

    Narrator "No answer. You look at your phone but the ghost has gone quiet."

    Robyn "Taro? Where'd you go? Taro!!"

    Narrator "You call for your cosmic guardian."

    Narrator "But she doesn't answer."

    Narrator "Maybe walking Jamie home was a bad idea. You've got no clue where you are and it's getting dark fast."

    Narrator "Not like you want to go trudge back to your apartment anyway. Not if it means another microwave dinner and more restless sleep. Ugh, you're starting to feel homesick."

    Narrator "And now you're lost."

    Narrator "This calls for desperate measures. \n\nA phonecall."
    show CGlonghope_map
    pause 0.5

    Robyn "Hey August? It’s [PCname]. Can you pick me up?"

    $musicPlayer.playSong(song="supernatural_serenade_song",fadeIn=1,fadeOut=2)

    August "Oh howdy! Where are you right now?"

    Robyn "I was walking Jamie home and I’m super lost."

    Narrator "There’s a brief pause, you hear August’s muffled voice talking to his daughter in the background."

    August "I’m on my way."

    Narrator "Something about talking to August comforts you, and you can’t stop the words from spilling out."
    hide CGlonghope_map
    Robyn "I know it’s short notice but, I don’t wanna go home right now. Last night was really scary and I can hardly sleep and-"

    August "I know how freaky striking it out on your own can be. It’s no biggie."

    August "I’ll swing by and pick you up."

    show CGShade
    show CG AugustCar:
        xcenter -0.5
        ease 1.5 xcenter 0.5

    Narrator "You spot a blue pickup rolling up the road. The truck slows to a stop and you quickly clamber inside. \n\nAugust is kicked back, listening to showtunes and drinking an orange soda."

    August "June, turn off the flashlight please, I can’t drive with it on."

    June "I’m reading!"

    August "It can wait until we get home."

    Narrator "Behind you, you see June in a booster seat, tearing and chewing up a picture book about giraffes. She looks at you and tries kicking your seat but can’t reach."

    August "Sorry for the ruckus. June had a rough day of school."

    June "{sc=3}RAWRGH!{/sc}"

    show CG AugustCar:
        xcenter 0.5
        ease 0.75 xcenter 0.1
        ease 1.5 xcenter 1.5

    show AugustCar Black behind CG:
        blur 10
        xanchor 0.0
        ycenter 0.5
        xpos -0.1
        xysize (1280,720)
        xzoom 0
        yzoom 0.025
        pause 1.0
        ease 1.5 xzoom 2.0

    Robyn "It’s okay! I really appreciate the save."

    show CG AugustCar:
        ease 0.2 xcenter 1.45

    show AugustCar Black:
        ease 0.2 xzoom 2.0
        xzoom 1.0
        xpos 0
        ease 0.4 yzoom 1.0

    $renpy.pause(0.6,hard=True)

    scene BG Cabin Night with Dissolve (0.5)

    Narrator "After a drive through town, the three of you reach August's cabin. June’s gone quiet after realizing her book is ruined."

    Robyn "Can I use your shower?"

    August "Of course! If you need to change, there's spare clothes in the towel closet. Werewolf thing."

    stop music fadeout 0.5
    Narrator "June bursts into tears."

    August "Oh dear."

    Narrator "August looks over the torn up mess with a sigh."

    Narrator "He nods for you to head inside. August unbuckles June and scoops her up in his arms."

    August "We’ll tape it back together, okay? Remember to be gentle Junebug. Things can break."

    August "Wanna help me make dinner? You and Jamie made such good cookies the other night. You’ll have to show me how it’s done."

    jump Ch1_AugustSleepover

label Ch1_AugustSleepover:

    scene BG Black with Dissolve(0.5)
    stop ambiance

    $musicPlayer.playSong(song="undead_icebreakers_song",fadeIn=1,fadeOut=0.5)
    scene BG Cabin Bathroom
    Narrator "After a refreshing shower paired with coconut shampoo and honeycomb bar soap, you break into the emergency clothing stash."

    show CGShade
    show CG RobynInGusClothes

    with nwDissolve(0.5)

    Narrator "A starchy church camp t-shirt and jeans. They’re fairly big on you, certainly designed for werefolks. You wonder what it’d be like. Inconvenient and frustrating? Probably."

    Narrator "Are you taking advantage of their kindness? Between the station and the car crash. You've caused such a mess—"

    hide CG RobynInGusClothes with None
    hide CGShade with nwDissolve(0.3)
    scene BG Cabin Night with Dissolve (0.5)


    Atlas "Heeey! You hungry? Auggie's baking stuffed bell peppers, and tilapia."

    Robyn "Be right there!"

    Narrator "You head to the kitchen and see June setting the table with her dad. She’s chipper again, and wearing a giant floral apron with the word ‘Papa Bear’ on it."

    Narrator "A giant, fluffy red monster leans against the fridge bickering with August."

    August "No wolf in the kitchen!"

    Hazel "It's fine! I'm clean. See?"

    Narrator "The wolf wipes her paws on the back of August's sweater. He grumbles."

    August "Go sit down."

    Atlas "Auguuuuust, where are the batteries? Can I borrow a phillips-head?"

    August "Dinner first!"

    scene CG Dinner WIP
    with Dissolve(0.75)

    Narrator "You enjoy a nice meal with Atlas and his pack. Everyone’s so chatty, Hazel demands you dish out embarrassing stories while Atlas panics, and August tries not to laugh."

    Narrator "Except, you notice Atlas doesn't eat."

    Narrator "He's always been food shy, preferring to eat by himself or waiting until everyone's left the table. You've pestered him about it but, he insists it's improper for a moth to show his fangs."

    Narrator "Hazel wolfs down her dinner, licks the plate clean, and heads for the door."
    scene BG August Cabin Inside with nwDissolve(0.3)

    Hazel "Sun's down, I'm out. Me and the girlies are gonna go wreck stuff."

    August "Brigg's junkyard?"

    Hazel "You guessed it."

    August "Be careful."

    Narrator "The monster races out the back door, while August stands on the porch, hands in his pockets. He shouts towards the woods."

    August "Don't wander too far!"

    June "How come Hazel gets to play outside when it's bedtime?"

    August "She's a grown up."

    Robyn "Can I help clean up from dinner?"

    August "Nah, I've got it. You're our guest, take a load off."

    Narrator "You start protest but stop short. It'd be rude to argue with the cook."

    August "Can I get ya a drink?"

    Robyn "Nah, I'm good right now."

    June "Apple juice!"

    Narrator "August clicks his tongue and snaps his fingers."

    August "Not until you finish what's on your plate little lady."

    June "{sc}{b}RAWRGH!{/b}{/sc}"

    scene BG Cabin Inside
    Narrator "Wandering into the living room, you take look around."

    python:
        choicesLeft = 3
        augustInvestigationChoices = [True,True,True]
    call Ch1_AugustInvestigationLoop from _call_Ch1_AugustInvestigationLoop

    Robyn "Is Atlas upstairs? I'm gonna go say hi."

    August "Yeah! He should be."

    Narrator "You head up to check on Atlas in the loft."

    jump Ch2_AtlasInvestigation


default choicesLeft = 3
default augustInvestigationChoices = [True,True,True]

label Ch1_AugustInvestigationLoop:

    menu:
        extend ""

        "Phtotographs" if augustInvestigationChoices[0]:
            call Ch1_AI_Photo from _call_Ch1_AI_Photo
            $augustInvestigationChoices[0] = False

        "Console" if augustInvestigationChoices[1]:
            call Ch1_AI_GameConsole from _call_Ch1_AI_GameConsole
            $augustInvestigationChoices[1] = False

        "Coffee Table" if augustInvestigationChoices[2]:
            call Ch1_AI_CoffeeTable from _call_Ch1_AI_CoffeeTable
            $augustInvestigationChoices[2] = False

        "Check on Atlas":
            $augustInvestigationChoices = [False,False,False]
    if not True in augustInvestigationChoices:
        Narrator "You poke your head around the corner and eye the stairs. Atlas is up there."
        $adjustChar("August",brow=2,mouth=5,eyeFrame=2,eye=1,sweater=0,hair=1)
        show august:
            matrixtransform RotateMatrix(0.0, 0.0, 0.0)
            xcenter -0.5
            yoffset 150
            zoom 2
            ease 0.9 matrixtransform RotateMatrix(0.0, 0.0, 35.0) xcenter -0.02

        August "Doin' alright?"

        Robyn "The shirt's a little big."

        $adjustChar("August",mouth=2,eyeFrame=3,eye=0)

        August "Yeaaah, it's leftovers from my time working as a camp counselor. They gave me some overstock."

        Robyn "Oh? What'd you do?"

        show august:
            ease 0.9 xcenter 0.2 yoffset 250 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        $adjustChar("August",mouth=3,eyeFrame=0,eye=3)

        August "I was the campfire guitar man! The campers swore I was a werewolf."
        $adjustChar("August",mouth=5,eyeFrame=2,eye=1,brow=2)

        August "They were right of course,, but I was still offended."

        Robyn "Maaan, I've never been the camping type. I always end up getting sick and going home early."
        $adjustChar("August",mouth=2,eyeFrame=0,eye=4,brow=1)

        August "Aw, there's no shame in that.\n\n Everybody's got their own idea of roughing it."
        $adjustChar("August",mouth=6,eyeFrame=0,eye=1,brow=2)
        $adjustChar("August",mouth=5,eyeFrame=2,eye=3)

        Robyn "Yeaaah. \n\nThanks again for having me over."

        $adjustChar("August",mouth=2,eyeFrame=0,eye=4,brow=1)

        August "Anytime. A friend of Atlas is a friend of mine."

        Robyn "Right back at ya."

        $adjustChar("August",mouth=5,eyeFrame=2,eye=3)

        August "Are you feeling better?"

        Robyn "Mhmm. I'm just a bit tired."

        August "Glad to hear it. \n\n We don't mind if you spend the night. That sofa folds out into an extra bed."

        Robyn "You sure? I could call a cab."

        $adjustChar("August",brow=2,mouth=5,eyeFrame=2,eye=1,sweater=0,hair=1)

        August "Nah, it's no trouble at all. None of those ride share apps work out here anyway."

        Robyn "Figures."

        August "But we have other alternatives!"

        August "Like haunted taxis."

        Robyn "Booo, haunted taxis are so twenty first century! Show me a ghost pirate ship."

        August "Were there ever pirates on the west coast? I thought that was an Atlantic ocean thing."

        Robyn "Maybe? I'm too lazy to check."

        scene BG Black
        camera:
            camera_default
        python:
            timeText = "7:30PM"
            musicPlayer.playSong(fadeOut=5.0)

        with Dissolve(0.75)

        return

    Narrator "You glance around the living room, wondering where to check next."

    jump Ch1_AugustInvestigationLoop

label Ch1_AI_Photo:
    Narrator "You admire the photos hanging on the wall."
    show CGShade
    show CG August_Family_Photo

    Narrator "A crowded group photo catches your eye."

    Narrator "Is this August's family? Everyone's dressed so casually."

    Robyn "Are these your folks?"

    Narrator "You call to August who's back in the kitchen."

    August "Hm? Oh, no,, that's my dad's sister, April."

    August "The big guy in the back is my great grandpa November."

    #Robyn "Isn't it a dangerous leaving your secret out in the open like this? With the photos?"
    Robyn "Is the kid on the left {i}October{/i}?"

    August "Nah,, he changed his name to Casey. Then Hazel followed suit. And I can't blame 'em! \n\nIt's a pretty stupid tradition."
    hide CG August_Group_Photo with None
    hide CGShade with nwDissolve(0.3)
    Robyn "Wacky."

    #August "It's a family joke that got out of hand."

    #August "It's my house! These folks mean a lot to me. It'd be a shame to hide them away."

    #Robyn "That’s really sweet."

    return

label Ch1_AI_GameConsole:
    Narrator "An outdated game console sits on the television stand covered in dust. A stack of games sit on top, bowling, fishing, unlicensed go-karting, bowling again."

    Narrator "They’re the kind of games a tired parent would scavenge at the bottom of a clearance bin. You're unimpressed."

    Narrator "Atlas was never allowed to play video games. Atticus said it was bad for his eyes. You both ignored this of course, much to the Mothman’s annoyance."

    show CGShade
    show CG August_License

    Narrator "Hm? Tucked between two games is an expired driver's license the from Wisconsin. August seems to have a knack for leaving things scattered about. Augustus James? \n\nHe's got such a grandpa name too."

    hide CG August_License with None
    hide CGShade with nwDissolve(0.3)

    return

label Ch1_AI_CoffeeTable:
    Narrator "You see a bunch of loose junk, English flashcards, letters, and a photo."

    show CGShade
    show CG Spruce_Photo

    Narrator "It's a picture of a large, fluffy mammal smiling warmly for the camera. There's a note on the back that reads, \"Spruce, Alpine Lakes\"."

    Narrator "Should you ask about this? Maybe not. You're starting to feel like a sleuth."

    hide CG Spruce_Photo with None
    hide CGShade with nwDissolve(0.3)

    return
