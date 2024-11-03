label Ch1_LibraryIntro:
    scene BG DaytimeRoadside

    play music loosen_up_longhope_song fadeout 2.5
    python:
        timeText = "12:15PM"

        adjustChar("Robyn",eyes=4,mouth=4,brow=1)
        adjustChar("Taro",eye=4,pawR=0,pawL=0)

    camera:
        camera_zoom(z=-300)
        shaded("#ffffff")


    show robyn:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.5

    show taro:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.6
        idleFloat(2,10)

    with Fade(0.5, 0.5, 0.5, color="#000000")
    $musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)

    Robyn "Taro, what happened back there? You seem startled."

    $Robyn_State["mouth"] = 5
    $Taro_State['eye'] = 3

    Taro "Edith sicced her lapdog on me!"

    Robyn "{size=30}Seriously?{/size}"

    $adjustChar("Taro",eye=2,mouth=4,pawL=1)
    Taro "Don't worry, he didn't stand a chance against me. \n\n I'm a menace.{nw}"

    $adjustChar("Robyn",eyes=3,brow=2,mouth=0)

    Robyn "You're adorable."

    python:
        Taro_State["eye"] = 1
        adjustChar("Robyn",eyes=2,brow=0)

    Taro ".,So where's Mike?"

    Robyn "I was hoping he'd make the first move."

    Narrator "You tap the screen of your phone and it flickers green."

    python:
        adjustChar("Robyn",armR=1,eyes=0,mouth=1,brow=0)
        BM_State['face'] = 2

    show blobhouse:
        zoom 0
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.4
        ycenter 0.5
        parallel:
            ease 0.6 xcenter 0.3 ycenter 0.4
        parallel:
            ease 0.2 zoom 1.0
        parallel:
            ease 0.3 yoffset -200
            ease 0.3 yoffset 0
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0,180,360*2)

        idleFloat(2.0, 15)
    voice mm_nob
    Madhouse "I chickened out!"

    python:
        Taro_State["mouth"] = 3
        adjustChar("Robyn",eyes=1,mouth=4,brow=2)

    Robyn "Chickened out?"

    python:
        adjustChar("Robyn",eyes=1,mouth=5)
        adjustChar("Taro",eye=1,pawR=0,pawL=0)

    show blobhouse: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        zoom 1
        alpha 1
        ycenter 0.4
        parallel:
            startledSquish
        parallel:
            idleFloat(2.0, 15)

    Madhouse "I can't face Edith."
    $BM_State["face"] = 8

    Madhouse "I look like a boiled legume."

    Robyn "Aw, don't say that! Would she even recognize you?"
    $BM_State["face"] = 7


    Madhouse "{size=30}Probably not!{/size}"

    $BM_State["face"] = 8

    Madhouse "But forget it. \n\nWho cares."

    python:
        adjustChar("Taro",eye=2,mouth=4,pawL=1)
        adjustChar("Robyn",eyes=4,mouth=1,brow=0)


    Taro "{b}Relax!{/b} You just ditched your job,, change is bound to be scary!"

    Taro "Why do you think I nap all the time?"

    $BM_State['face'] = 4

    Madhouse "Because you're a cat?"
    voice taro_uhuha
    python:
        adjustChar("Taro",eye=1,mouth=2,pawR=2)
        adjustChar("Robyn",eyes=2,brow=2)

    Taro "No, it's because the world's exhausting!"
    $adjustChar("Taro",eye=0,mouth=4,pawL=0,pawR=0)
    Taro "You'll figure things out."

    $adjustChar("Taro",eye=2,mouth=4,pawL=0,pawR=0)
    Taro "And no,, you're not a boiled legume,, you're a tennis ball."

    $BM_State['face'] = 3
    Madhouse "Thanks?"

    scene BG Black
    camera at camera_default:
        camera_zoom()

    with dissolve

    Robyn "Let's keep walking."

    scene BG Avenue

    show robyn:
        xcenter -0.5
        ease 2.0 xcenter 0.5

    show taro:
        xcenter -0.5
        ease 2.5 xcenter 0.4
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat

    show blobhouse:
        zoom 0
        xcenter 0.25
        matrixtransform RotateMatrix(0,180,0)
        pause 1.75
        parallel:
            ease 1.0 zoom 1.0
        parallel:
            ease 1.75 matrixtransform RotateMatrix(0,180,360*3)
        block:
            idleFloat(2.2,12)

    python:
        adjustChar("Robyn",mouth=0,eyes=2,armR=0,brow=0)
        Taro_State["eye"] = 0
        BM_State["face"] = 1

        timeText = "12:30PM"

    with pixellate

    Narrator "You pass through the empty city square and come to a stop in front of a tall red-bricked building."
    Narrator "Through the glass doors you catch a glimpse of a figure dressed in a brightly colored cloak pushing a cart full of books through the lobby."

    Robyn "Cuuute! They’ve got a library!"

    $BM_State["face"] = 3
    Madhouse "Don’t be fooled, libraries are treacherous labyrinths. Without a specific goal in your heart, you’ll be lost in a maze of books."

    $adjustChar("Robyn",eyes=4,mouth=1,brow=1)
    Robyn "Bad experience?"

    $BM_State["face"] = 4
    Madhouse "Nah, I’ve never actually been here."

    $adjustChar("Robyn",eyes=3,mouth=0)
    Robyn "Then let's check it out!"

    jump Ch1_LibraryIntro_Inside

label Ch1_LibraryIntro_Inside:
    scene BG Library

    $BM_State["face"] = 1
    camera at camera_default:
        camera_zoom(z=-500,y=200)
        camera_zoom(z=-500,t=2.5)
        camera_zoom(z=-200,t=2)

    with Fade(0.5, 0.5, 0.5, color="#000000")

    $musicPlayer.playSong(song="broken_horns_song_bearsome",fadeOut=2,fadeIn=1)

    show robyn:
        xcenter -0.5
        ease 3.0 xcenter 0.6

    show taro:
        xcenter -0.5
        ease 3.5 xcenter 0.45
        idleFloat(2.0, 10)

    show blobhouse:
        matrixtransform RotateMatrix(0,180,0)
        xcenter -0.5
        ease 3.5 xcenter 0.3
        idleFloat(2.3, 15)

    Narrator "Entering the lobby, you’re welcomed by a hushed peace and contemplative quiet."

    Narrator "The front desk is tucked off to the side, unmanned."

    Narrator "To the other side is a framed map of the library’s layout. The map makes it appear much larger than the outside would lead you to believe."

    show robyn:
        xcenter 0.6
        flipChar()

    $adjustChar("Robyn",eyes=2,brow=0)
    Robyn "So, where to first?"

    $BM_State["face"] = 4

    show blobhouse at startledSquish:
        xcenter 0.3
        idleFloat(2.3, 15)

    Madhouse "The town archives, no minotaur can find us in there."

    $adjustChar("Taro",mouth=1,eye=1)
    #Taro "Does he think this is an actual labyrinth?"

    #$BM_State["face"] = 1
    #Madhouse "And play right into the monster’s hands? Reading is exactly what they’d expect!"

    #$adjustChar("Taro",mouth=3,pawL=1,eye=2)
    #Robyn "Well there should be books in the archives. Let's just start there!"
    #Robyn "Taro, commit to the bit."

    $BM_State["face"] = 6
    extend "\n\nThey might have an article about me!"

    $Taro_State["mouth"] = 4
    Taro "You’d have to be relevant for that."

    $BM_State["face"] = 4
    Madhouse "Tch."

    show robyn:
        unflipChar(0.4)
        ease 2.5 xcenter 1.3

    show taro:
        ease 2 xcenter 1.3

    show blobhouse:
        alpha 1
        blur 0
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 yoffset -100 alpha 0 blur 30

    Narrator "You walk down a set of stairs into a dark, sectioned off area labeled {i}‘Archives’{/i}. \n\nShelves line the small space. A table rests in the center of the room covered in scattered papers, notebooks, and diaries."

    hide blobhouse
    hide taro
    hide robyn
    Madhouse "Looks like somebody had the same idea."
    Taro "Yeah and they left a mess!"

    Robyn "Let’s take a look around and maybe put some things back?"

    Madhouse "I'm on it."

    nvl clear
    $nvl_show(Dissolve(0.5))
    show CGShade

    NVL_Narrator "You sort through the books and papers on the table, and several things catch your eye., first of which being an open newspaper."


    call Ch1_omalleymonster from _call_Ch1_omalleymonster
    call Ch1_ArchiveLoop from _call_Ch1_ArchiveLoop
    call Ch1_JamieText from _call_Ch1_JamieText

    show blobhouse onlayer screens zorder 100 at startledSquish:
        xcenter 0.65
        ycenter 0.5
        zoom 6

    python:
        musicPlayer.playSong(song="not_so_spooky_song")
        BM_State['face'] = 7
        adjustChar("Robyn",eyes=3,brow=2,mouth=4)
    voice mm_boob
    NVL_Madhouse "All tidied up!"

    nvl hide
    hide CGShade
    window show
    hide blobhouse onlayer screens

    show blobhouse:
        xcenter 0.65
        ycenter 0.5
        pause 0.5
        idleFloat(2.2,12)
    with Dissolve(0.4)

    show robyn:
        xcenter 0.5
        yoffset 700
        matrixtransform RotateMatrix(0,-180,0)
        parallel:
            ease 0.4 yoffset -50
            ease 0.1 yoffset 0
        parallel:
            pause 0.3
            ease 0.5 matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 0.4 yzoom 1.2 xzoom 0.8
            ease 0.15 yzoom 0.8 xzoom 1.2
            ease 0.15 yzoom 1 xzoom 1



    Robyn "{sc=3}{b}GWUAH!{/b}{/sc}"
    $adjustChar("Robyn",eyes=0,brow=1,mouth=1)
    $BM_State['face'] = 1
    Narrator "You look around and find all the papers and journals have been neatly tucked away."
    $adjustChar("Robyn",eyes=2,brow=0,mouth=5)
    $musicPlayer.playSong(song="broken_horns_song_bearsome",fadeOut=2,fadeIn=1)
    Robyn "Oh hey! Did you put them back in the right spots?"

    Madhouse "NOPE! So did you find any articles on me?"

    Robyn "No luck."

    $BM_State["face"] = 4
    voice mm_groan
    Madhouse "Bummer,, guess it was worth a shot."

    show taro:
        xcenter 0.0 matrixtransform RotateMatrix(0,180,0)
        ease 1.5 xcenter 0.09 matrixtransform RotateMatrix(0,180,30)
        on hide:
            xcenter 0.09 matrixtransform RotateMatrix(0,180,30)
            ease 1.0 xcenter -0.9 matrixtransform RotateMatrix(0,180,0)

    Taro "If it's that important to you, why not ask the librarian?"

    Robyn "True! All we’ve gotta do is find them. Somewhere."

    Taro "I'll scout on ahead."

    hide taro

    Narrator "Taro fades out of view, leaving you to wander the library aimlessly."

    jump Ch1_LibraryIntro_GM #jump Ch1_LibraryIntro_Neko

label Ch1_JamieText:
    #Mikey Signal
    nvl clear

    NVL_Narrator "Oh right! You've gotta reply to Jamie's text."

    NVL_Narrator "You respond with a simple smiley face and a thumbs up. \nKeeping things short and sweet."

    #NVL_Jamie "Hi i'm a test dummy."

    #Insert more of a hook to Tessie and put a text conversation here that unlocks a hangout with Tessie to meet her
    return

label Ch1_omalleymonster:
    $ch1_archiveinv[0] = False
    nvl clear
    NVL_Text "{i}The O'Malley Monster{/i}{nw}"

    NVL_Text "A menace on campus!{nw}"

    NVL_Text "As if finals week couldn't get any worse, there's been reports of a monster roaming the school grounds."

    NVL_Text "Not just any monster, but a wild eyed, ragged beast with iron teeth and a wail like a tornado siren."

    NVL_Text "One student claims they saw muddy handprints tracked through the co-ed dorms! Campus security's brushed it off as a lost black bear, but last I checked, {b}bears don't have {sc=3}dorm keys!{/sc}{/b}"

    NVL_Text "The professors are scared, freshmen are petrified and the howling hasn't stopped. \n\nHow is anybody supposed to wrap up fall semester with a monster running amok?!"

    nvl clear
    NVL_Narrator "Want my take? This is some elaborate prank by some loser looking for attention. Try not to give it to them."

    NVL_Text "{image=CG Howler}\nYou turn the page and see a rough photograph of a monster peering out from behind a half open window."
    return

default ch1_archiveinv = [True,True,True,True]
label Ch1_ArchiveLoop:
    if True in ch1_archiveinv:
        python:
            PC_Stats.updateStats()
            xDiff = 4
            for x in range(3):
                if not ch1_archiveinv[x+1]:
                    xDiff+=2

        nvl clear
        nvl hide
        window show

        with dissolve
        call dice_roll(PC_Stats.cStats("brains"), xDiff, "Focus") from _call_dice_roll_56
        nvl show dissolve
        if isRollSuccess:
            nvl clear
            NVL_Narrator "You return to the main pile, checking if anything else might interest you."
        else:
            return

    else:
        return

    menu(nvl=True):
        extend ""
        "The O'Malley Monster" if ch1_archiveinv[0]:
            call Ch1_omalleymonster from _call_Ch1_omalleymonster_1
        "Werefolk and New Magics" if ch1_archiveinv[1]:
            $ch1_archiveinv[1] = False
            nvl clear

            NVL_Narrator "Star Marks, known as etches are a magical tattoo inked onto a werefolk's skin. \n\nThe most common place for an etch is between the shoulders or the forearms, acting as a shock guard and easing the physical strain of a lunar curse."
            nvl clear

            NVL_Text "{image=CG Library WereFolk}\nThis magic isn't without pushback however. Some werefolk take issue with the Etch, claiming it reduces endurance needed to shift. Keeping a clear head under the effects of moonlight is considered a feat of strength. \n\nA shaggy fur coat easily masks these markings, making it difficult to tell who's the {i}\"real\"{/i} lycanthrope."

            #NVL_Narrator "{b}A Grand Discovery{/b}{nw}"

            #NVL_Text "Thanks to the valiant efforts of Miss Patch, the County Library has officially reopened its doors!{nw}"

            #NVL_Text "While it's far from perfect, we've taken steps to recover what we can from the flood."

            #NVL_Text "After a catastrophic wave of darkness cut access to the lower floors, a small group were tasked to recover Longhope's history and fend off the stygian force."

            #NVL_Text "The task was near impossible, there were nights I wept over books stained black. Miss Patch regales. But with the help of this community, we managed to restore what we could."

            #NVL_Text "And remember, story time is this saturday morning!"
        "Citizens of the Underworld" if ch1_archiveinv[2]:
            nvl clear
            NVL_Narrator "{image=CG Black Tome}\n\nAh-hah! A hefty textbook catches your eye,, a black tome etched with gold and red thread. \n\nLucky find!"

            NVL_Text "You pluck the black book off the shelf and admire the handywork. The face of a large bat, jaws agape is delicately embroidered on the tome's face, the edge of each page dyed a shiny red."

            nvl clear
            NVL_BlackTome "{b}Citizens of the Underworld{/b}{p}Devils are considered a high class, haughty demon subtype.{p}\nMuch like their vampire counterparts,, devils hunger for life force and tend to keep to themselves.{p}\nUnlike vampires however, devils are known for their horns and wings. Both requiring proper care and with the right tools can be styled.\n\n{image=CG Library DEMON 2}{space=150}"
            nvl clear
            NVL_BlackTome "{image=CG Library DEMON 1}\nGold horn etching and antler jewelry are rather popular among the younger devils.{p}Do be careful, if a horn is snapped, the break is painful and permanent."

            $ch1_archiveinv[2] = False

            nvl clear
            NVL_Narrator "The book yanks itself out of your hands and slams shut."

            #NVL_Robyn "{b}Hey!{/b}"
        "Anomolium" if ch1_archiveinv[3]:
            #Mikey Signal
            $ch1_archiveinv[3] = False
            NVL_Text "{image=CG Library Lore 1}\n\n...Humans talk. They talk a lot."

            NVL_Text "And whether it be by their own volition or a cacophony of wills,, someone is bound to listen."

            nvl clear
            NVL_Text "{image=CG Library Lore 2}\n\nMost revel in the act of \"playing the part\". It's why they're here after all. \n\nWhile others choose to flee,, ultimately rejecting the wishes of humankind and living cut off from the world."
            nvl clear

            NVL_Text "{image=CG Library Lore 3}\n\nThese outsiders are called {b}cryptids{/b}.{nw}"

            NVL_Text "Ellusive anomalies shaped by the world's whispers. \nPerhaps born from a dying god's prayer or tear in reality..."
            #nvl clear
            #NVL_Text "{image=CG Library Lore 4}\n\nCryptids come in a variety of sizes, forms and families. While uncommon, this phenomenon isn't exclusive to the living."

        "Check your phone! (Quit)":
            return

    jump Ch1_ArchiveLoop

label Ch1_LibraryIntro_GM:
    scene BG Black
    $timeText = "1:30PM"
    with quickDissolve
    Narrator "..."

    Narrator "Madhouse was right, you’re totally lost in this labyrinth of a library."

    Madhouse "Y’know, I tried writing a book once. I thought it’d be a great way to get thoughts outta my head., but I couldn't hold a pencil."

    Narrator "You give Madhouse a sad look."

    voice mm_laughh
    Madhouse "No no, it’s cool! That’s how I got my telekinetic power!"

    Robyn "Ghosts don't have that ability from the start?"
    python:
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "#bc8bff")
        musicPlayer.playSong(song="mage_hands",fadeOut=1,fadeIn=0.5)

    voice gm_specterderivestheirpower
    Someone "A specter derives their power through dissonance.\n\nSo I'd imagine it'd take years for a skill like {i}that{/i} to manifest."

    voice gm_nottopry
    Someone "Oh, not to pry of course."

    voice mm_woah
    Madhouse "Who the heck are you?"
    scene BG OutsideHospital

    camera at camera_default:
        shaded("#ffd5bd")
        camera_zoom(z=-480,x=-200)
        camera_zoom(z=-480,x=0,t=2)

    show goatmaam:
        xcenter 0.45

    with nwDissolve(0.5)

    $adjustChar("GM",eyes=1,armR=2,mouth=5)
    voice gm_callmegoatmaam
    Someone "Why, I'm the librarian! \n\n You can call me the {bt=3}{color=#bc8bff}Goatma'am{/color}!{/bt}"

    $adjustChar("GM",eyes=0,armR=0,mouth=4)
    Robyn "There you are! I thought we'd be trapped wandering here forever."

    voice gm_yougotlost
    $adjustChar("GM",eyes=2,mouth=1)
    Goatmaam "You got lost?"

    $adjustChar("GM",eyes=5,mouth=2,ears=1)
    Goatmaam "I knew I should've required emergency whistles on entry."

    $adjustChar("GM",eyes=2,mouth=0,ears=0,armL=2,armR=1)
    Goatmaam "Sorry about that,, I haven't gotten around to updating today's map."

    $GM_State["eyes"] = 3
    Goatmaam "Can I help you with anything?{nw}"

    call Ch1_Library_GM_Loop from _call_Ch1_Library_GM_Loop

    $adjustChar("GM",eyes=0,mouth=5,armL=0,armR=0)
    voice gm_backtothefrontdesk
    Goatmaam "Let me guide you rascals back to the front desk."

    camera at camera_default
    scene BG Black

    with quickDissolve

    Narrator "Goatmaam takes you through the library, ducking and weaving through the aisles. She's fast!"

    Madhouse "{i}Pssst,, would you ask the nice lady how to get my body back?{/i}"

    Robyn "Your., {sc=3}{b}body?{/b}{/sc}"

    voice mm_nob
    Madhouse "{sc=2}Ew,, not that one!{/sc} \n\nSure I'm desperate but not enough to warrant {i}crimes against nature.{/i}"

    Robyn "Well, if we had enough toothpicks,, I could sculpt you something out of lime jelly."

    Madhouse "{size=17}You'd do that for {i}me?{/i}{/size}"
    scene BG Library
    python:
        GM_State["mouth"] = 0
        BM_State["face"] = 0

    camera at camera_default:
        camera_zoom(y=-250,z=-600)
        camera_zoom(z=-200,t=3)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 2
        ease 3.0 xcenter 0.6

    show goatmaam:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.8
        ease 1.2 xcenter 0.35
        ease 0.4 matrixtransform RotateMatrix(0,0,0)

    show blobhouse:
        xcenter 2
        ease 3.5 xcenter 0.8
        idleFloat(2,10)

    with nwDissolve(0.75)

    Robyn "Goatma'am,, how would a rogue ghost go about regaining, lets say,, their limbs?"

    $adjustChar("GM",eyes=2,mouth=2)
    voice gm_necromancy
    Goatmaam "Necromancy's out of my jurisdiction, dear."

    python:
        adjustChar("GM",eyes=6,mouth=6)
        BM_State["face"] = 13

    show blobhouse at startledSquish:
        xcenter 0.8
        idleFloat(2,10)

    Madhouse "Not like that!"

    python:
        adjustChar("GM",eyes=1,mouth=4,ears=1)
        BM_State["face"] = 1
    voice gm_relieved
    Goatmaam "Oh, thank goodness."

    Robyn "Is there a way to like,, glue him back together?"
    python:
        adjustChar("GM",eyes=4,mouth=1,armL=1,ears=0)
        BM_State["face"] = 4

    Goatmaam "Well,, the best thing one can do is strive to find peace and move on."
    show blobhouse at startledSquish:
        idleFloat(2,10)

    python:
        GM_State["mouth"] = 0
        BM_State["face"] = 9

    voice mm_laughawkward

    Madhouse "{bt=3}Not happening Granny!{/bt}"
    python:
        adjustChar("GM",eyes=3,mouth=5,armL=2)
        BM_State["face"] = 1
    voice gm_hmm
    Goatmaam "Is it not a spirit's goal to find eternal rest? You should take this time to reflect."

    python:
        adjustChar("GM",eyes=3,mouth=0,armL=0)
        BM_State["face"] = 4

    Madhouse "Ah.{nw}"

    $BM_State["face"] = 7
    show blobhouse at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2,10)

    extend "{sc=3}\n\nNevermind, get me a {b}necromancer.{/b}{/sc}"

    python:
        adjustChar("GM",eyes=1,mouth=0,ears=1)
        BM_State["face"] = 13

    show goatmaam at startledSquish
    voice gm_laugha
    Goatmaam "Aw, aren't you silly one!"

    $adjustChar("GM",eyes=5,mouth=5,armR=1,ears=0)

    voice gm_pamphlets
    Goatmaam "Let me get you kids some {bt=4}helpful pamphlets!{/bt}"

    scene BG Black
    camera at camera_default
    with quickDissolve

    play music loosen_up_longhope_song fadeout 2.5
    python:
        timeText = "1:45PM"
        musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)

    Narrator "Strolling out of the library, you flit through the pamphlets the Goatma'am gave you."

    #Mikey Signal
    python:
        PC_Stats.updateStats()
        bookNames = {
            "brawn": "{color=#ff5342}How to Punch Ghosts",
            "brains": "{color=#a1fffc}Existence for Geeks",
            "hustle": "{color=#a7ff78}Exercise for Spector Guys",
            "guts": "{color=#ff8941}Phantom Hunger Pains",
            "charm": "{color=#ED2A82}To Charm a Reaper",
            "occult": "{color=#b480ff}Share the Abyss" }

        xBooks = []
        for x in ["brawn","brains","hustle","guts","charm","occult"]:
            if PC_Stats.cStats(x) > 0:
                xBooks.append(bookNames[x])

        xBookA = xBooks[0]
        xBookB = xBooks[1]
        xBookC = xBooks[2]

    Robyn "[xBookA],., [xBookB]. [xBookC]? \n{bt=3}{color=#3bec27}Life in Ectoplasm?{/bt}"

    Robyn "These are all terrible!"

    Madhouse "Actually, open that last one. It sounds interesting."

    Narrator "You unfold the ectoplasmic pamphlet and Mike begins quietly reading over your shoulder."

    Robyn "Let's find a place to sit and read these. \n\nNow I'm invested."

    Madhouse "I think we passed a café back there."

    Robyn "Perfect."

    Narrator "The ghost blips back into your phone, leaving you to turn around and nod along, skimming through self improvement for the undead."

    jump Ch1_CafeIntro

default gm_questions = [True,True,True]
label Ch1_Library_GM_Loop:
    menu:
        extend ""

        "What do you mean by {b}today's{/b} map?" if gm_questions[0]:
            python:
                gm_questions[0] = False
                adjustChar("GM",eyes=1,mouth=5,ears=1,armL=1,armR=2)

            show goatmaam at startledSquish
            Goatmaam "This building loves scrambling its layout on the daily."

            $adjustChar("GM",eyes=5,mouth=4,ears=1,armL=0,armR=1)
            Goatmaam "Which makes our jobs an absolute nightmare,, but I live for the \n{sc=3}challenge!{/sc}"

            show goatmaam:
                yoffset 0
                block:
                    parallel:
                        ease 1.25 yoffset -40
                        ease 2.0 yoffset -10
                        repeat
                    parallel:
                        matrixtransform rotated()
                        ease 1.5 matrixtransform rotated(y=360)
                        repeat 1

            $adjustChar("GM",eyes=3,ears=3,mouth=3)
            voice gm_laugha
            Goatmaam "Yes! {b}Ya-HAHA!{/b} No un-whirly magic can dissuade me!"

            show goatmaam:
                parallel:
                    parallel:
                       ease 0.15 yoffset 0
                    parallel:
                        pause 0.1
                        ease 0.05 yzoom 0.9 xzoom 1.1
                    ease 0.2 yzoom 1 xzoom 1
                parallel:
                    ease 0.5 matrixtransform RotateMatrix(0,0,0)

            $adjustChar("GM",eyes=2,ears=0,mouth=0,armR=0)
            Goatmaam "So don't hesitate to ask for directions."

            Robyn "Gotcha."

        "What else do you know about ghosts?" if gm_questions[1]:
            python:
                gm_questions[1] = False
                adjustChar("GM",eyes=6,ears=1,mouth=1,armR=0)
            Goatmaam "Most specters love passively wreaking havoc,, quietly but just enough to irritate you. \n\nBut if you manage to befriend one,, they're great for countering the summer heat!"

            $adjustChar("GM",eyes=3,ears=1,mouth=3)
            Goatmaam "And they glow in the dark when they're happy! Isn't that adorable?"

            $adjustChar("GM",eyes=2,ears=0,mouth=0,armL=1)
            Goatmaam "Gosh, I'm a little jealous."

        "What are you?" if gm_questions[2]:
            python:
                gm_questions[2] = False
                adjustChar("GM",eyes=4,mouth=4,armR=0,armL=0)

            Goatmaam "Why, I'm a dreadful and fearsome {b}devil!{/b}"

            $adjustChar("GM",eyes=1,mouth=5,ears=1)
            show goatmaam at startledSquish
            Goatmaam "You can tell by my lovely wings and horns."

            $adjustChar("GM",eyes=3,mouth=1,ears=0)
            Goatmaam "Or what's left of them anyway."

            $GM_State["mouth"] = 0

            Robyn "{size=20}Isn't Jamie a devil?{/size}"

            Madhouse "{size=20}I think so.{/size}"

        "I'm good!":
            return

    if True in gm_questions:
        jump Ch1_Library_GM_Loop
    return
