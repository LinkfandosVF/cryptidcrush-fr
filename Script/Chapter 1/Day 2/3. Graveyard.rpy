label Ch1_GraveyardExploration:

    camera at camera_default
    scene BG Black

    with Dissolve(0.5)
    #Narrator "Returning home, you text Atlas, checking up on the lad. He seems alright, just tired."
    Narrator "Taking a page from Taro's playbook, you spend the afternoon loafing around the house."
    #Narrator "Next time you see him, you're dragging Atlas to the nearest exorcist."
    #AUGUST PICKS U UP
    Narrator "After a lazy dinner, you wander outside where you meet up with August."
    window hide
    scene BG Road Side with pixellate #----------------------------------------- Road side
    window show
    python:
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1,fadeOut=2)
        timeText = "7:00PM"

    show Driving Night Graphic

    Narrator "August drives a blue pickup truck plastered in a scattershot of feel good bumper stickers."

    Narrator "Someone's scrawled 'WASH ME' on the dusty back window. The interior is littered with crayons, coloring books, a cup of mystery soda and a single palm tree air freshener dangling off the rear view mirror."

    play sfx carStart

    Narrator "You slide into the passenger seat., and the back cushion suddenly {sc=2}drops{/sc}, giving you a mini heart attack. \n\nAugust quickly grabs the seat and snaps it back into place."

    August "{sc=2}Sorry!{/sc} I forgot I broke that!"

    Robyn "How?!"

    Madhouse "Gus, why does your license plate say {i}Beach Babe{/i}?"

    August "Don't worry about it."

    play ambiance car_ambiance fadein 8.0

    pause 0.6

    Robyn "Do you have an aux cord?"

    August "No, but you can check my CD stash under the sun visor."

    Narrator "You flip the visor down and start digging through August's music collection."

    Narrator "Oh! It got awfully bright all of a sudden, someone must have turned a light on. The CDs are much easier to read. Classical music, spa ambience, baby sing-along songs... You don't wanna listen to any of this."

    Narrator "You look over and see two massive headlights blaring in the side mirror. You shield your eyes at an imposing crimson logger truck riding the blue pickup's rear. Don't brake check."

    play sfx truck_pass
    Narrator "The truck swerves into the opposite lane and veers past you."

    Narrator "Glancing at the cargo makes you uneasy,, you can't quite make the shapes out in the darkness but you swear it's squirming."
    play sfx truck_honk
    Narrator "August shoves his hand out the driver window and flips the truck off as it disappears around a bend."

    scene BG Black with Dissolve(1.0)

    #MOVING THIS ELSEWHERE
    # Robyn "Mike."
    #
    # extend "\n\nDo you remember., what happened {i}when{/i} you died?"
    #
    # Madhouse "Awfully bold question there pal."
    #
    # Robyn "Ah, I should've asked if you were cool with that sort of thing."
    #
    # scene BG Black
    #
    # with Dissolve(0.5)
    #
    # Madhouse "Let's see..."
    #
    # show CG Mike Wake Up at mwakeup_trans
    # with nwDissolve(1.0)
    #
    # Madhouse "I woke up to a flickering lightbulb, sprawled out on the tile with this annoying buzz ringing in my head."
    #
    # Madhouse "I thought it was a joke,, a cutesy prank played on the weird guy., but when I opened my eyes, that buzzing got louder and louder and {sc=3}{b}LOUDER—{/b}{/sc}"
    #
    # hide CG Mike Wake Up2
    # with nwDissolve(1.0)
    #
    # Madhouse ".,Ghosts are remnants of a tragedy, right? A sharp influx of grief concentrated into a single speck."
    #
    # Madhouse "Knowing that's what I am,, it screws with me."
    #
    # scene BG Road Side #-----------------------------------------
    # show Driving Night Graphic
    # with dissolve
    #
    # August "That's a pretty wild story!"
    #
    # Narrator "August looks nauseous."
    #
    # Madhouse "It's funny!"

    Narrator "The pickup rolls through the graveyard's broken gates, its bright headlights beaming across the abandoned lot."
    stop ambiance
    Narrator "The three of you hop out and August twirls his jangly car keys strung on a sea shell lanyard. He whistles."

    August "Phew! We're not driving back that way."

    Robyn "{sc=3}We could've been steamrolled.{/sc}"

    # August "Gus rule number two,, human gets the keys."
    #
    # Robyn "What, why?"
    #
    # August "In case you gotta run or lock the doors. We don't know what's out here and., you're squishy."
    #
    # Robyn "Uh-huh."
    #
    # Madhouse "Just admit you're a clutz and might lose them."

    $timeText = "7:30PM"

    jump Ch1_GraveyardArrival

label Ch1_GraveyardArrival:
    scene BG Graveyard Night
    play ambiance forest_ambianceb fadein 5.0 fadeout 4.0

    camera:
        camera_zoom(z=-500,x=100)
        camera_zoom(z=-250,x=60,y=-10,t=2.5)

    with dissolve

    Narrator "Gravel crunches under your shoes, your flashlight shining over mossy headstones. The singing crickets and icy wind bring a gloomy peace to these old resting grounds."
    camera:
        camera_zoom(z=-250,x=60,y=-10)
        camera_shake

    $musicPlayer.playSong(song="not_so_spooky_song")
    Madhouse "{size=40}HURRY UP SLOWPOKES!{/size}"

    python:
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        adjustChar("August",mouth=5,eye=3,eyeFrame=2,brow=5,coat=1)
        adjustChar("BM",arms=0,face=1)

    show august:
        shaded("#ebc0f8")
        enterFromLeftDelay(x=0.46,t=2.0,dTime=1.0)

    show robyn:
        shaded("#ebc0f8")
        enterFromLeftDelay(x=0.3,t=2.0,dTime=1.0)

    show blobhouse:
        shaded("#c0fac8")
        matrixtransform RotateMatrix(0.0,180.0,0.0)

        enterFromLeft(x=0.65,t=2.0)
        ease 0.3 matrixtransform RotateMatrix(0.0,0.0,0.0)
        idleFloat(2,20)

    August ".,Maybe keep it down? I'm sure there's spirits here trying to rest."

    $adjustChar("BM",face=9)
    Madhouse "You got a heartbeat?"
    python:
        adjustChar("Robyn",mouth=3,brow=1)
        adjustChar("August",mouth=7,eye=2,brow=2)

    August "Yeah, last I checked."
    python:
        adjustChar("Robyn",mouth=5,eyes=1,brow=0)
        adjustChar("August",mouth=0,eye=3,brow=0)
        adjustChar("BM",arms=0,face=13)

    show blobhouse:
        xcenter 0.65
        matrixtransform RotateMatrix(0.0,0.0,0.0)
        idleFloat(2,20)

    Madhouse "Then stay in your lane."

    $adjustChar("August",eyeFrame=0,eye=2)
    August "{size=18}{color=#cf0000}Grrhrgh{/color}{/size}{nw}"

    show august:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.45
        ease 0.2 xcenter 0.46 matrixtransform RotateMatrix(0,0,10) yoffset 50
        ease 0.2 xcenter 0.45 matrixtransform RotateMatrix(0,0,-5) yoffset 0
        ease 0.3 xcenter 0.46 matrixtransform RotateMatrix(0,0,0) yoffset 0

    python:
        adjustChar("Robyn",mouth=5,eyes=0,brow=1)
        adjustChar("August",mouth=6,eye=1,eyeFrame=3,wolfEars=1,brow=2)

    extend "{sc=6}\n\nURK.{/sc}"

    python:
        adjustChar("Robyn",mouth=5,eyes=1,brow=2)
        adjustChar("August",mouth=2,eye=0,eyeFrame=4,brow=1)

    show august:
        xcenter 0.46
        yoffset 0
        matrixtransform RotateMatrix(0.0, 0.0, -5.0)
        xoffset -1
        block:
            ease 0.1 xoffset 1
            ease 0.1 xoffset -1
            repeat 3


    August "{sc=2}Y-yeah sure, I mean,, you're the ghost here.{/sc}"

    show robyn:
        xcenter 0.3
        ease 0.4 xcenter 0.5

    show august:
        pause 0.1
        ease 0.3 xcenter 0.3 matrixtransform rotated() xoffset 0

    python:
        adjustChar("Robyn",mouth=4,eyes=2,brow=4)
        adjustChar("August",mouth=6,eye=3,eyeFrame=1)
        adjustChar("BM",face=4)

    voice RobynSays("Chapter 1","GusIsTryingToHelp")

    Robyn "Oh, bug off! Gus is {i}trying{/i} to help you!"

    show blobhouse at startledSquish:
        idleFloat(2,20)

    python:
        adjustChar("Robyn",mouth=2)
        adjustChar("August",brow=2,eye=1,eyeFrame=0,mouth=0)
        adjustChar("BM",face=14)

    Madhouse "{bt=3}Did he bring the shovels?{/bt}"

    $adjustChar("Robyn",mouth=4,eyes=4)
    Robyn "We're not doing that!"

    show august:
        xcenter 0.3
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        xoffset 0
        parallel:
            ease 0.6 xcenter 0.5
        parallel:
            pause 0.6
            ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 10.0)

    show blobhouse:
        xcenter 0.65
        pause 0.4
        ease 0.5 xcenter 0.7
        idleFloat(2,20)

    show robyn:
        xcenter 0.5
        pause 0.2
        ease 0.5 xcenter 0.4

    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=0)
        adjustChar("August",brow=6,mouth=2,eyeFrame=2,eye=1)
        adjustChar("BM",face=4)

    August "I'm starting to doubt this {bt=3}\"spiritual wellbeing\"{/bt} thing. \n\nWhat do you {i}actually{/i} want Mike?"

    python:
        musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=1.5,fadeOut=3)

        adjustChar("Robyn",eyes=1)
        adjustChar("August",mouth=5)
        adjustChar("BM",face=5)

    Madhouse "I uh..."

    $adjustChar("BM",face=13)
    extend "\n\nI'm searching for myself."

    show robyn:
        xcenter 0.4

    show blobhouse:
        idleFloat(2,20)
        xcenter 0.7

    show august:
        matrixtransform RotateMatrix(0.0, 0.0, 10.0)
        ease 0.3 matrixtransform rotated()

    python:
        adjustChar("Robyn",eyes=2)
        adjustChar("August",mouth=6,eyeFrame=0,eye=0,brow=2)

    August "Literally speaking?"
    python:
        adjustChar("Robyn",eyes=0)
        adjustChar("August",mouth=5,eye=2,brow=1,eyeFrame=2)


    August "I wouldn't get your hopes up."

    scene BG Black with quickDissolve
    Narrator "The three of you start looking around, hoping to find a stone marked with a \"Mike\"."

    scene BG Graveyard Night
    camera at camera_default:
        camera_zoom(z=-300,x=150,y=0)
        camera_zoom(z=-100,x=0,y=0,t=3.0)

    show august:
        xcenter 0.2
        matrixtransform rotated(y=180,z=-10) yoffset 200
        shaded("#ebc0f8")

    with dissolve

    $adjustChar("August",eye=3,eyeFrame=0,mouth=1,brow=2)
    voice august_foundamike

    August "I found a Mike!"

    $adjustChar("BM",arms=1,face=4)
    show blobhouse at enterFromRight(x=0.4,t=4.5):
        shaded("#c0fac8")
        idleFloat(2,20)

    Narrator "August calls out from a grave marker, gesturing you to come over."

    python:
        adjustChar("August",mouth=0)
        adjustChar("BM",arms=0)

    show blobhouse:
        ease 1.0 xcenter 0.4
        idleFloat(2,20)

    show august sigh:
        ease 0.5 matrixtransform rotated(y=180) yoffset 0

    show robyn sigh at enterFromRight(x=0.55,t=4.5):
        matrixtransform rotated(y=180)
        shaded("#ebc0f8")

    voice mm_thatsnotme
    Madhouse "That's{w=0.3} not{w=0.5} me. I'd know if it were me!"

    voice RobynSays("Chapter 1","WhatsYourLastName")
    show robyn:
        ease 1.0 xcenter 0.55

    Robyn "What's your last name?"

    voice mm_madhouse
    show blobhouse:
        xcenter 0.4
        shaded("#c0fac8")
        matrixtransform rotated()
        ease 0.3 matrixtransform rotated(y=180) yoffset 0
        idleFloat(2,20)

    Madhouse "Madhouse."

    voice RobynSays("Chapter 1","Serious")

    Robyn "No, I'm being serious."
    $adjustChar("BM",face=13)
    show blobhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        startledSquish
        idleFloat(2,20)

    voice mm_lookforaguynamedmadhouse
    Madhouse "My name is Madhouse! Look for a guy named Madhouse!"
    python:
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        adjustChar("August",mouth=5,eye=3,eyeFrame=2,brow=2)

    show august default:
        unflipChar(0.5)

    show robyn default

    show blobhouse:
        unflipChar(0.5)
        idleFloat(2,20)

    voice august_youdontremember
    August "You don't remember, do you?"

    show blobhouse:
        vibrate()
        idleFloat(2,20)

    voice mm_whatkindofloser
    Madhouse "{size=35}What kind of loser forgets their own name?!{/sc}"
    pause 0.5

    show blobhouse:
        ease 0.5 matrixtransform rotated(y=180) xoffset 0 yoffset 0
        idleFloat(2,20)

    python:
        adjustChar("Robyn",mouth=1,eyes=4,brow=1)
        adjustChar("August",mouth=5,eye=2,eyeFrame=2,brow=0)
        adjustChar("BM",face=8)

    Madhouse "..."

    Robyn "Let's come back when we've got more information."
    python:
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        adjustChar("BM",arms=1)

    Madhouse "You wanna leave?"
    show robyn sigh
    python:
        adjustChar("Robyn",eyes=2,brow=1)
        adjustChar("BM",arms=0)

    Robyn "It's getting pretty late."
    python:
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)
        adjustChar("August",mouth=0,eye=2,eyeFrame=1,brow=4)
        adjustChar("BM",arms=0,face=13)

    Madhouse "Then let's split up,, we'll cover more ground that way."
    $adjustChar("Robyn",eyes=2,brow=1)
    show blobhouse at disappear

    Narrator "Madhouse blinks out of sight."

    hide blobhouse
    Robyn "Be careful."
    camera:
        camera_zoom(z=-350,x=-80,y=0,t=1.0)

    python:
        musicPlayer.playSong(fadeOut=2,song="supernatural_serenade_song")

        adjustChar("Robyn",mouth=5,brow=0)
        adjustChar("August",eyeFrame=2,brow=0,eye=1,mouth=6)

    show robyn default
    show august:
        parallel:
            ease 1.0 xcenter 0.35

    August "I wanna go home."
    python:
        adjustChar("Robyn",mouth=5,brow=0)
        adjustChar("August",eye=2,mouth=4)

    August "We can leave right? I mean,, Mike's in his natural habitat."
    python:
        adjustChar("Robyn",eyes=1,brow=0)
        adjustChar("August",eye=3,mouth=1,brow=1)

    August "Like releasing a mountain lion back into the wild."
    python:
        adjustChar("Robyn",eyes=4,mouth=4,brow=2)
        adjustChar("August",mouth=5)

    Robyn "I couldn't do that to him."
    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("August",eye=2,eyeFrame=3,mouth=2)

    August "Well, you've got more patience than I do. I nearly freaked."
    python:
        adjustChar("Robyn",mouth=6,eyes=3,brow=0)
        adjustChar("August",eye=3,eyeFrame=0,mouth=5,brow=2)

    Robyn "That'd explain the ears."

    $adjustChar("August",eye=2,eyeFrame=2,brow=4)
    August "..."
    python:
        adjustChar("Robyn",mouth=1,brow=1,eyes=0)
        adjustChar("August",eye=0,eyeFrame=0,brow=2,mouth=1)

    August "Welp, tour's over!{nw}"
    python:
        adjustChar("Robyn",mouth=3,brow=2,eyes=4)
        adjustChar("August",eye=3,eyeFrame=2,brow=0,mouth=6)

    extend "\n\nI need to make a phone call."
    show august:
        flipChar(0.3)
        ease 1.8 xcenter 0.1

    python:
        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
        adjustChar("August",eye=0,eyeFrame=2,brow=0,mouth=5)

    Narrator "August strolls off the path, fishes his cellphone out of his pocket and dials up a number."
    show august:
        matrixtransform rotated(y=180)
        xcenter 0.1

    August "How's things? I wanted to check in."

    $adjustChar("Robyn",mouth=3,brow=2,eyes=4)
    August ".,Atlas, the oven is off limits."

    $adjustChar("Robyn",mouth=3,brow=0,eyes=2)

    show august:
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated(y=180,z=-10)

    August "You., invited {b}Jamie{/b} over?"

    $adjustChar("Robyn",mouth=5,brow=2,eyes=1)
    show august:
        matrixtransform rotated(y=180,z=-10)
        ease 0.5 matrixtransform rotated(y=180)

    August "Okay, just keep me posted. \n\n{size=18}And tell Junebug \"papa loves you!\"{/size}"

    $adjustChar("Robyn",brow=1,eyes=0)
    show august:
        matrixtransform rotated(y=180)
        vibrate(t=0.075)

    August "Not {i}you{/i},, {b}June!{/b}"

    #$adjustChar("Robyn",mouth=5,brow=2,eyes=1)

    show august:
        ease 0.1 xoffset 0
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated(y=180,z=-10)

    #August "{size=-7}Sorry, I didn't mean it like that.{/size}{nw}"

    $adjustChar("Robyn",mouth=1,brow=0,eyes=4)
    show august:
        matrixtransform rotated(y=180,z=-10)
        ease 0.5 matrixtransform rotated(y=180)

    extend "{size=-7} ...Yes, you too Atlas.{/size}"

    show august:
        matrixtransform rotated(y=180)

    show robyn smug

    jump Ch1_GraveyardMadhouse

label Ch1_GraveyardMadhouse:
    scene BG Graveyard Night
    python:
        musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=1.5,fadeOut=3)
        adjustChar("BM",face=1,arms=0)

    camera:
        matrixcolor TintMatrix("#c0fac8")
        camera_zoom(z=-500,y=200,x=-220)
        camera_zoom(z=-500,y=20,x=-220,t=2.5)

    show blobhouse:
        xcenter 0.3
        idleFloat(2.2,25)

    with pixellate
    Madhouse "{bt=3}HELLOOOOO? Anybody home?{/bt}"
    $adjustChar("BM",face=4,arms=0)
    show blobhouse:
        matrixtransform rotated()
        block:
            parallel:
                idleFloat(2.2,25)
            parallel:
                ease 0.3 matrixtransform rotated(y=180)
                choice:
                    pause 0.3
                choice:
                    pause 0.2
                choice:
                    pause 0.1
                ease 0.3 matrixtransform rotated()
                choice:
                    pause 0.3
                choice:
                    pause 0.2
                choice:
                    pause 0.1
                repeat

    Madhouse "I've gotta be lying around here somewhere."

    show blobhouse:
        ease 0.3 matrixtransform rotated() yoffset 0
        idleFloat(2.2,25)

    Narrator "Maybe they were right, Mike's got no clue what he's doing here."

    $adjustChar("BM",face=8,arms=1)
    Narrator "Or why anyone bothered."

    python:
        adjustChar("BM",arms=0)
        Ghost4 = Character("Ghostie", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "10A", who_color = "#7b78ff")
        Ghost1 = Character("???", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "3A", who_color = "#f0bf6c")
        Ghost3 = Character("Ghoul", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "#e96cf0")
        Ghost2 = Character("Ghost", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "7B", who_color = "#ff3232")

    Ghost4 "{size=30}Hey cutie!{/size} \n\nPlace your headstone next to mine!"

    $adjustChar("BM",face=5,arms=0)
    show blobhouse:
        idleFloat(2.2,25)

    Ghost3 "{sc=2}L-Let's spend an eternity together, darling!{/sc}"

    show blobhouse:
        flipChar(0.3)
        idleFloat(2.2,25)

    Ghost4 "Go to hell! I saw him first!"

    $adjustChar("BM",face=14,arms=0)
    show blobhouse at startledSquish:
        idleFloat(2.2,25)

    Madhouse "You freaks are the reason the dead don't speak!"

    $adjustChar("BM",face=1)

    show blobhouse:
        unflipChar(0.3)
        idleFloat(2.2,25)

    voice walker_theyllbegonebymorning
    python:
        songText = "Old Gods"
        musicNote = 7

    play music wrath_of_the_old_gods_song_bearsome

    Ghost1 "Please, pay them no mind. \n\nThey'll be gone by morning."

    show blobhouse at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        idleFloat(2.2,25)

    $adjustChar("BM",face=10,arms=0)
    Madhouse "HUH?"

    show Flickering Black

    Ghost1 "Now, allow me."

    $musicPlayer.playSong(fadeOut=3.0)
    stop ambiance fadeout 3.0

    scene BG Black
    Narrator "Madhouse feels a spectral hand touch the visor of his hat."

    Ghost1 "This momento is rather precious to you."

    $MM_Stats = MMUnit()
    call dice_roll(MM_Stats.cStats("guts"), 999, "{color=#EC2A2A}Hats Off{/color}") from _call_dice_roll_18

    Narrator "The hand gives Mike's cap a gentle tug.,., and {sc=2}{b}{color=#EC2A2A}tears{/color}{/b}{/sc} it off the little ghost's head."

    Narrator "He shrieks {nw}"
    play sfx radio_tuning

    camera:
        camera_default
        camera_zoom()

    scene BG Studio Room Spooky:
        matrixcolor SaturationMatrix(1)
        pause 0.15
        matrixcolor SaturationMatrix(0)

    $timeText = "???"
    extend "and reality is torn from him."
    stop sfx
    show BG Studio Room with nwDissolve(1.0)

    python:
        musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=3)
        SomeLady = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "4C", who_color = "#FC7979")

    SomeLady "Mike? You look like hell! Where've you been, bedhead?"

    Narrator "Mike's standing half asleep, slumped against the studio doorframe. He's face to face with his producer who's clicking a pen in her right hand, annoyed."

    $Mike = Character("Mike", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27")
    Mike "Is it {i}that{/i} obvious?"

    $Debbie = Character("Debbie", callback = Bleep,ctc="end_of_msg", cb_id = "4C", who_color = "#FC7979")
    SomeLady "Let's just say,, we're lucky this is radio. \n\nHave you been getting enough sleep?"

    Narrator "They both know the answer."

    Mike "Sure but uh,, what about you Debs?"

    Debbie "Yeesh, there's not enough hours in the day!"

    Debbie "Especially with our holiday special just around the corner. Boss wants things wrapped up in a real tidy bow."

    Debbie "I'm holding out for this year's holiday bonus."

    Mike "..,..,..,If we even get one."

    Narrator "Debbie takes a sharp breath."

    Debbie "Let focus on you, 'kay? You're the star here,, I just schedule interviews and push your buttons."

    Mike "Aw c'mon, you got me this gig! Mistletoe Mike wouldn't exist without ya."

    Debbie "You do look good in a Santa costume."

    Narrator "They both laugh."

    Debbie "{size=35}Now give us an {b}outro.{/b}{/size}"

    Mike "Like on the spot?"
    play music elkhorn_radio_blues_song_radio fadeout 4.0

    Debbie "Boss' orders."

    pause 0.8
    show BG Studio Room Spooky
    stop music fadeout 1.0
    show BG Black

    camera:
        matrixcolor TintMatrix("#c0fac8")
        camera_zoom(z=-500,y=20,x=-220)

    show blobhouse:
        xcenter 0.3
        matrixcolor SaturationMatrix(0.2)*BrightnessMatrix(-0.05)*ColorizeMatrix("#18110a","#ffd028")

    $adjustChar("BM",face=10,arms=0,hat=0)
    Ghost1 "That's it?"

    play music bad_prophecy_song
    Ghost1 "Your heart clung to {b}this?{/b}"

    extend "\n\nNo glory,, nor tragedy,, but a boring day job?"

    $adjustChar("BM",face=11)

    Ghost1 "You poor little nothing."

    $adjustChar("BM",face=12)

    Ghost1 "Even oblivion didn't want you."
    stop music

    camera:
        camera_default
        camera_zoom()
    hide blobhouse

    show BG Studio Room Spooky:
        matrixcolor TintMatrix("#ff7e7e")*SaturationMatrix(0)
        ease 0.5 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(0)
        #matrixcolor SaturationMatrix(1)

    camera screens:
        matrixcolor TintMatrix("#ff7e7e")*SaturationMatrix(0)
        ease 0.5 matrixcolor TintMatrix("#ffffff")*SaturationMatrix(1)

    $MM_Stats.modifyHP(-10,1)

    Madhouse "{sc=2}Ghyrck!{/sc}"

    #Ghost1 "You wanted the attention. The ghost hunters,, the mediums,, you wanted people to {i}talk{/i}."
    show BG Black
    with nwDissolve(1.0)
    #show CG MM_Scrunch

    Narrator "Madhouse chokes, straining against the crushing grip of this invisible foe."

    Narrator "He squeezes his eyes shut and blinks back into your phone—"

    extend "\n\nBut nothing happens."

    Narrator "He strayed too far."

    #Ghost1 "Ghosts are remnants of grief! A powerful memory living on as a shadow of one's former self."
    #A sharp influx of grief concentrated into a single speck."
    #Narrator "Wriggling in the wraith's grip, Madhouse angles himself just enough to bare his dagger teeth and {b}BITE{/b} the wraith."

    #Ghost1 "What a lonely way to die."

    #Ghost1 "Waiting for the life you didn't chase."

    stop sfx
    stop music
    jump Ch1_GraveyardOz

label Ch1_GraveyardOz:
    scene BG Graveyard Night
    python:
        musicPlayer.playSong(song="magic_birdbrain_song",fadeIn=2)
        timeText = "8:00PM"

        adjustChar("OH",eyes=5,armL=1,armR=3,eyeFrame=0,brow=0)


    camera at camera_default:
        camera_zoom(z=-500,x=200,y=0)

    show oswald:
        matrixcolor TintMatrix("#ebc0f8")
        matrixtransform RotateMatrix(0.0,180.0,0.0)
        xcenter 0.6

    with nwDissolve(1.5)

    Narrator "Oz shambles through the graveyard like a zombie, a tired zombie. \n\nHe plucks a toadstool here and a moss chunk there. Per Edith's orders."
    camera:
        camera_zoom(z=-500,x=200,y=-175,t=2)

    $adjustChar("OH",eyes=4,eyeFrame=0,brow=3)
    Narrator "Squeezing his eyes shut, he stifles a big yawn."
    camera:
        camera_zoom(z=-500,x=200,y=-175)
        camera_shake_off(200)

    $adjustChar("OH",eyes=0,eyeFrame=1,brow=0)
    Narrator "He steps in something and nearly slips."

    show mmhat:
        shaded("#ebc0f8")
        xcenter 0.64
        yoffset 700
        matrixtransform rotated(z=20)
        ease 1.5 yoffset 150

    $adjustChar("OH",eyes=1)
    Narrator "Oz lifts his boot and peels whatever it is off the bottom of his shoe."

    show mmhat:
        yoffset 150


    $adjustChar("OH",eyes=0,eyeFrame=0,brow=2)
    Narrator "A mushroom? No, it's a melted baseball cap. Oz scoffs,{nw}"

    show mmhat:
        parallel:
            ease 0.5 xcenter 0.3
        parallel:
            ease 0.25 yoffset 50
            ease 0.25 yoffset 150
    extend "tossing the hat aside. Gross."
    hide mmhat

    $adjustChar("OH",eyes=1)
    Robyn "{sc=3}MIKE WHERE ARE YOU?!{/sc}"
    camera:
        camera_zoom(z=-250,x=0,y=-80,t=1)

    python:
        adjustChar("OH",eyes=5,eyeFrame=0,brow=1)
        adjustChar("Robyn",eyes=3,brow=1,mouth=1,armR=1)

    show oswald at flipCharDelayed(2.0,0.45) behind robyn:
        matrixcolor TintMatrix("#ebc0f8")

    show robyn:
        shaded("#ebc0f8")
        matrixtransform rotated()
        parallel:
            enterFromLeft(0.45,1.2)
        parallel:
            pause 1.0
            ease 0.3 matrixtransform rotated(z=10)
        ease 0.2 matrixtransform rotated()

    Narrator "You come running, skidding to a stop as you nearly crash into the howler."

    camera:
        camera_zoom(z=-250,x=0,y=-80)

    show robyn fear:
        xcenter 0.45
        matrixtransform rotated()
        parallel:
            ease 0.1 matrixtransform RotateMatrix(0.0, 0.0, -6.0)
        parallel:
            vibratenum(t=0.1,x=6,r=2)
        ease 0.3 xcenter 0.4 matrixtransform rotated() xoffset 0

    Narrator "You scream at the sight of— Oh! It's just Oz. Lurking around in the dark, alone, in a graveyard. Just like you! Except he's a monster and built like a sycamore tree."

    show robyn:
        xcenter 0.4
        matrixtransform rotated()
        xoffset 0

    Robyn "I-I'm so sorry!"

    show robyn surprised:
        matrixtransform rotated()
        ease 0.3 matrixtransform rotated(y=180)

    #FEELS WEIRD TO RANDOMLY SAY
    #Robyn "You gotta help,, Mike disappeared and I think he's in trouble."

    August "YOU!"

    python:
        adjustChar("August",eye=2,eyeFrame=3,mouth=6,brow=0)
        adjustChar("Robyn",brow=2,eye=2)

    camera:
        camera_zoom(z=-250,x=0,y=-80)
        camera_zoom(z=-150,x=-10,y=-40,t=1.5)

    show robyn default:
        matrixtransform rotated(y=180)

    show august at enterFromLeft(0.25,1.5):
        shaded("#ebc0f8")

    Narrator "August marching through the dark paces behind you."

    show robyn:
        matrixtransform rotated(y=180+360)
        pause 0.2
        parallel:
            ease 0.6 matrixtransform rotated(z=-10) yoffset 15
            ease 0.2 matrixtransform rotated() yoffset 0
        parallel:
            ease 0.4 xcenter 0.3

    show august:
        xcenter 0.25
        ease 0.5 xcenter 0.55

    show oswald:
        xcenter 0.6
        matrixtransform rotated()
        pause 0.4
        ease 0.3 xcenter 0.65 matrixtransform rotated(z=7.5)

    python:
        adjustChar("August",eye=3,eyeFrame=2,mouth=5)
        adjustChar("Robyn",brow=1,eye=1)
        adjustChar("OH",eyes=0)

    August "What does Edith want? Did she send you to come screw with me?"

    $adjustChar("August",eye=0,eyeFrame=3,mouth=5)
    Narrator "August eyes the sky with suspicion."
    python:
        adjustChar("August",eye=3,eyeFrame=2,mouth=0)
        adjustChar("OH",eyeFrame=1,brow=0,eyes=5)

    camera:
        camera_zoom(z=-500,x=150,y=-80,t=0.75)

    show oswald:
        xcenter 0.65
        matrixtransform rotated(z=7.5)
        ease 0.75 yoffset 50 xoffset -50

    show august:
        xcenter 0.55
        matrixtransform rotated()
        ease 0.75 matrixtransform rotated(z=-5) xoffset 20

    August "Where's the bird?"
    $adjustChar("OH",eyeFrame=0,eyes=0,brow=4)

    voice oz_ugh
    Narrator "Oz rolls his eyes."
    python:
        adjustChar("August",eye=2)
        adjustChar("OH",brow=1)

    Robyn "Did something happen between you two?"
    python:
        adjustChar("August",eye=3,mouth=1)
        adjustChar("OH",eyes=1)

    #August "He won't quit hounding me! I'll pay my stupid bill!"
    August "All Oswald cares about is his so-called favors!"
    python:
        adjustChar("August",eye=1,mouth=2,eyeFrame=3)
        adjustChar("OH",eyes=5)

    #show august:
        #matrixtransform rotated(y=180)
        #xoffset 0
        #ease 0.3 matrixtransform rotated()

    August "I'll pay my stupid bill. So quit hounding me!"
    python:
        adjustChar("August",mouth=0)
        adjustChar("OH",eyes=4,brow=3,armL=3,armR=1)

    show oswald:
        yoffset 50
        xoffset -50
        matrixtransform rotated(z=7.5)
        ease 0.6 yoffset 0 xoffset 0 matrixtransform rotated()

    Narrator "Oz lifts a finger and August pauses mid rant."
    python:
        adjustChar("August",eyeFrame=0,eye=3,mouth=1,brow=2)
        adjustChar("OH",eyes=4,brow=3,armL=1,armR=2)

    August "Oh-{nw}"
    show august:
        ease 0.5 xcenter 0.5

    extend "\n\nYou go ahead."
    python:
        adjustChar("OH",eyes=5,brow=0)
        adjustChar("August",eyeFrame=2,eye=2,mouth=0)

    Narrator "August waits patiently as Oz writes something on his little clipboard."
    python:
        adjustChar("OH",eyes=4,brow=0,armR=0)
        adjustChar("August",eyeFrame=3,eye=3,mouth=2)


    Narrator "He shimmies over and glances at the note. Oz holds it out for August to read."
    python:
        adjustChar("OH",eyes=3,brow=0,armR=0,eyeFrame=1)
        adjustChar("August",eyeFrame=0,eye=4,mouth=3)

    August "Oswald says I'm right,, he is horribly wrong and he'll be fleeing to Alaska post haste!"
    python:
        adjustChar("August",eye=4,mouth=2)
        adjustChar("OH",eyes=4,brow=4,eyeFrame=0)

    play sfx blip_11a
    pause 0.9

    python:
        adjustChar("August",eye=4,mouth=2)
        adjustChar("OH",eyes=2,brow=0,eyeFrame=0)

    camera:
        pause 0.35
        camera_shake_off(150)

    show oswald:
        ease 0.2 xoffset 10 yoffset -20 matrixtransform rotated(z=7.5)
        parallel:
            ease 0.1 xoffset -5
        parallel:
            pause 0.05
            ease 0.1 matrixtransform rotated(z=-7.5) yoffset 45

    show august:
        xcenter 0.5


    pause 0.35
    $adjustChar("August",eye=1,eyeFrame=4,mouth=6,brow=1)

    play sfx hurt_b
    play voice2 august_damagedb

    show oswald:
        matrixtransform rotated(z=-7.5)
        yoffset 45
        xoffset -5

        pause 0.1
        parallel:
            ease 0.3 xoffset 0
        parallel:
            pause 0.1
            ease 0.3 matrixtransform rotated() yoffset 0

    show august:
        matrixtransform rotated(z=-7.5)
        vibratenum(t=0.1,x=2,r=3)

    Narrator "Oz stomps on the wolfman's foot."
    python:
        adjustChar("August",eye=4,eyeFrame=0,mouth=7)
        adjustChar("Robyn",brow=0,eyes=1,mouth=5)

    voice august_damagedg

    August "{sc}{b}OUAGH!{/b}{/sc}"
    camera:
        camera_zoom(z=-500,x=-350,y=-40,t=0.75)

    show robyn:
        xcenter 0.3
        pause 0.75
        flipChar(0.3)

    show august:
        pause 0.5
        matrixtransform rotated(z=-5)
        ease 0.5 matrixtransform rotated(z=0) xcenter 0.6

    show oswald:
        matrixtransform rotated()
        yoffset 0
        xoffset 0
        pause 0.75
        ease 0.5 xcenter 0.75

    Narrator "You don't have time for this. Turning away, you zone out the bickering and wave your phone around trying to pick up a signal."
    $adjustChar("Robyn",brow=1,eyes=0,mouth=5,armR=0)
    show mmhat:
        shaded("#ebc0f8")
        xcenter 0.25
        yoffset 700
        matrixtransform rotated(z=-20,y=180)
        ease 1.5 yoffset 270

    Narrator "A red splotch catches your eye. Strolling over, you squat down and pluck a hat off the ground. It's Madhouse's hat!"

    python:
        musicPlayer.playSong(fadeOut=1.5)

        Gus_Stats = Unit("{color=#e8850c}August{/color}",3,1,2,-2,1,-2,20)
        Gus_Stats.cHP = 15
        Gus_Stats.baseDiff = 8
        Gus_Stats.SetMTA(0)
        Oz_Stats = OzUnit()
        playerUnitsInit("Oz")
        enemyUnitsInit("Gus")
        InitializeCombatUI(playerUnits, enemyUnits)
        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0])

    show mmhat:
        yoffset 270
        vibrate(t=0.05,x=2)

    hide august
    show halfaugust behind oswald:
        xcenter 0.6 matrixtransform rotated(y=0)
        shaded("#ebc0f8")

    Narrator "It's hot in your hands, crackling with a supernatural energy."
    $adjustChar("Robyn",brow=2,eyes=4,mouth=4)
    show mmhat:
        yoffset 270
        ease 1.5 yoffset 700 xoffset 0

    Robyn "Uh,, guys?"
    python:
        adjustChar("Robyn",mouth=5)

        playerUnits[0].modifyHP(-1,1.0,"guts")
        enemyUnits[0].modifyHP(2,1.0,"guts")

    camera:
        camera_zoom(z=-500,x=-350,y=-40)

    stop ambiance fadeout 4.0
    Narrator "An eerie hush falls over the resting grounds."
    python:
        musicPlayer.playSong(song = "supernatural_foe_intro_song")
        musicPlayer.playSong(song = "supernatural_foe_loop_song",queueSong=True)

        ToggleBarState([1,2,3,4], 0)
        enemyUnits[0].modifyHP(-1,1.0,"guts")

        adjustChar("Robyn",brow=0,eyes=2,mouth=1)

    show robyn:
        unflipChar(0.3)

    Narrator "You look back to find the two cryptids brawling like monsters.\n\n{nw}"

    $enemyUnits[0].modifyHP(-4,1.0,"guts")
    extend "Oz lunges, aiming for the wolfman's neck, but the sleek facemask blocks his bite. {nw}"
    python:
        playerUnits[0].modifyHP(-7,1.0,"guts")
        #enemyUnits[0].modifyHP(2,1.0,"guts")
        adjustChar("Robyn",brow=1,eyes=0,mouth=7)

    camera:

        camera_shake_off(-350)


    extend "August retaliates by chomping the howler's arm, shaking him out like a chew toy."

    python:
        ToggleBarState([1,2,3,4], 0)
        enemyUnits[0].modifyHP(-5,1.0,"guts")

        adjustChar("Robyn",brow=3,eyes=1,mouth=4)

    show halfaugust:
        matrixtransform RotateMatrix(0, 0.0, 15)
        #enemyUnits[0].modifyHP(2,1.0,"guts")

    Robyn "What the hell are you doing?!"

    Robyn "We're not supposed to be fighting {b}each other!{/b}"

    python:
        adjustChar("HalfAugust",eye=1,mouth=7,eyeFrame=5,brow=1,armR=1,ear=2,shirt=1,pants=1,blush=0)
        adjustChar("OH",armL=6,armR=3,eyes=2)
        adjustChar("Robyn",eyes=1,mouth=1)

    Robyn "{size=40}{b}AUGUST!{/b}{/size}"

    camera:
        camera_zoom(z=-500,x=-350,y=-40)
        camera_zoom(z=-200,x=-10,y=-40,t=0.75)

    show robyn:
        xcenter 0.3
        ease 0.3 xcenter 0.25

    python:

        adjustChar("HalfAugust",eye=3,eyeFrame=0,brow=0,mouth=4,ear=1)
        adjustChar("OH",eyes=6,eyeFrame=1)
        adjustChar("Robyn",brow=3,mouth=5,eyes=2)

    August "{sc=3}...{/sc}"

    python:
        adjustChar("HalfAugust",eye=0,eyeFrame=1,armR=0,mouth=2,ear=0)
        adjustChar("OH",eyes=5,eyeFrame=1)
        HighlightEnemyUnitBars([])
        HighlightPlayerUnitBars([])
        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1,fadeOut=2)

    show halfaugust behind oswald at flipCharDelayed(1.2,0.5):
        matrixtransform RotateMatrix(0.0, 0.0, 15.0)
        ease 0.5  matrixtransform RotateMatrix(0, 0.0, 0)

    Narrator "August spits the howler's arm out of his mouth with a disgruntled whine."
    python:
        adjustChar("HalfAugust",eye=2,eyeFrame=0,brow=2,mouth=6)
        adjustChar("Robyn",mouth=4)

    Robyn "Both of you!"
    python:
        adjustChar("OH",eyes=6,eyeFrame=1,brow=2,mouth=0,armR=0,armL=5)
        adjustChar("HalfAugust",eye=1,eyeFrame=0,brow=0,mouth=2,ear=1)
        adjustChar("Robyn",mouth=3)

    show oswald at hoppies(xIntensity=1.5):
        xcenter 0.75

    voice oz_frustrated
    Oz "{sc}-!{/sc}"
    python:
        adjustChar("HalfAugust",mouth=3,eyeFrame=3,brow=2,blush=1,ear=2)
        adjustChar("Robyn",brow=0,eyes=1,mouth=5)
        adjustChar("OH",armR=0,armL=2)

    show oswald:
        xcenter 0.75
    show halfaugust:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5  matrixtransform RotateMatrix(0, 180, -10.0) yoffset 30

    voice august_chuckle
    August "Sorry."
    python:
        adjustChar("OH",eyes=5,brow=1,eyeFrame=0,armL=0,armR=0)
        adjustChar("HalfAugust",mouth=3,eyeFrame=1,eye=1)

    show oswald at flipCharDelayed(1.2,0.5)

    voice oz_bleuhgh
    Narrator "Oz folds his arms and sulks."
    show halfaugust:
        matrixtransform RotateMatrix(0.0, 180.0, -10.0) yoffset 30
        ease 0.5  matrixtransform RotateMatrix(0, 180, 0.0) yoffset 0

    $adjustChar("HalfAugust",mouth=0,eyeFrame=0,eye=3,ear=0,blush=0)

    August "What were we doing again?"
    python:
        adjustChar("HalfAugust",mouth=1,eyeFrame=0,eye=2,brow=2)
        adjustChar("Robyn",brow=2,eyes=2,mouth=4,armR=1)
        adjustChar("OH",eyes=6)

    Robyn "I can't get ahold of Mike!"
    show robyn:
        flipCharDelayed(1.2,0.5)

    python:
        adjustChar("HalfAugust",eyeFrame=1)
        adjustChar("Robyn",brow=2,eyes=4,mouth=1,armR=1)
        adjustChar("OH",eyes=1)

    Robyn "Sure, we split up, but I didn't think he'd disappear!"
    python:
        adjustChar("HalfAugust",brow=0,eye=1,ear=2)
        adjustChar("Robyn",brow=2,eyes=1,mouth=5,armR=0)
        adjustChar("OH",brow=0,eyeFrame=1,eyes=0)

    Robyn "I knew this was a bad idea."

    show robyn:
        unflipCharDelayed(1.2,0.5)

    python:
        adjustChar("Robyn",brow=0,eyes=2,mouth=5)
        adjustChar("HalfAugust",eye=2,mouth=2)
        adjustChar("OH",eyes=6)

    August "Gimme that hat you're holding. It's Mike's, right?"

    python:
        adjustChar("Robyn",brow=1,eyes=2,mouth=1)
        adjustChar("HalfAugust",eyeFrame=0,brow=1,mouth=5)
        adjustChar("OH",brow=5)

    extend "\n\nI'll sleuth 'em out."
    python:
        adjustChar("Robyn",brow=0,eyes=1,mouth=4)
        adjustChar("HalfAugust",brow=0,eye=2,mouth=1)
        adjustChar("OH",eyes=0)
    Robyn "What, you've got a sixth sense?"

    $adjustChar("Robyn",brow=1,eyes=2,mouth=1)
    show oswald:
        unflipChar()

    Narrator "Oz reaches into his overshirt and bumps into the wolfman."

    python:
        adjustChar("HalfAugust",eyeFrame=1,brow=1,eye=1,mouth=2,ear=0)
        adjustChar("Robyn",brow=0,mouth=5)
        adjustChar("OH",eyes=1,brow=1)
    August "Nah, ghosts got this., ozone sorta smell to 'em."
    python:
        adjustChar("OH",brow=1,eyes=1)
        adjustChar("HalfAugust",ear=3,mouth=6)

    Narrator "Oz draws a silver dagger from his coat and{nw}"

    show halfaugust:
        xcenter 0.6
        parallel:
            matrixtransform rotated(y=180)
            ease 0.6 matrixtransform rotated(y=360*2+180)
        parallel:
            ease 0.3 xcenter 0.75

    show oswald:
        xcenter 0.8
        ease 0.25 xcenter 0.55

    python:
        adjustChar("HalfAugust",eyeFrame=1,brow=1,eye=0)
        adjustChar("OH",brow=5,eyes=2,armL=7)
        adjustChar("Robyn",brow=1,eyes=3,mouth=1)
    extend " cuts through the air before him."

    python:
        adjustChar("HalfAugust",eyeFrame=0,brow=2,mouth=2,eye=3,ear=1)
        adjustChar("Robyn",brow=2,eyes=0,mouth=5)
    show halfaugust:
        startledSquish
    August "{sc}{b}E E K!{/b}{/sc}"

    #Narrator "Oz pushes forward and slashes again, this time his blade connects."

    stop ambiance fadeout 0.5

    if gameVersion == 3:
        Narrator "Skip Fight?{nw}"
        menu:
            extend ""
            "Yes":
                jump Ch1_GraveyardPostFight
            "No":
                pass

    call FIGHT_05_MISTWALKER from _call_FIGHT_05_MISTWALKER
    $HideBars()
    camera at camera_default

    jump Ch1_GraveyardPostFight

label Ch1_GraveyardPostFight:
    scene BG Black
    camera at camera_default
    stop ambiance fadeout 4.0
    stop music

    Narrator "The lantern shatters,, and a geyser of ghostly light spills from the broken glass. \n\nWith a wail, the shadow shields his face from the flash and just like that,, disappears."
    scene BG Studio Room:
        matrixcolor SaturationMatrix(1)
        pause 0
        matrixcolor SaturationMatrix(0)

    with Dissolve(0.75)

    python:
        musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=3)
        timeText = "???"
        Debbie = Character("Debbie", callback = Bleep,ctc="end_of_msg", cb_id = "4C", who_color = "#FC7979")
        Mike = Character("Mike", image = "madhouse", callback = Bleep,ctc="end_of_msg", cb_id = "8B", who_color = "#3bec27")

    Debbie "Today's my last day, Mike. I'm moving to Seattle."

    Narrator "Her last day? But the season hasn't wrapped! Debbie can't just {i}leave.{/i}"

    Mike "Why didn't you tell me?"

    Debbie "I didn't want you to quit,, not because of me."

    Mike "You know I can't do this without you! If you go,, I go."

    Debbie "Aw man, don't be like that. You gotta hold down the fort, 'kay?"

    Narrator "Turning away, Debbie reaches into her backpack."

    Debbie "Here,, I want you to have this."

    Narrator "Debbie holds out a small box wrapped in festive paper and ribbons. A tag noted, {i}'To the host I owe the most'{/i} is taped to the side with a little heart. Cheesy."

    Mike "It's a bit early for a gift exchange, Debs."

    Debbie "M'yeah, I'd rather save on shipping."

    Narrator "Mike takes the gift and slides it open. Inside is a simple red cap, horns sewn to the crown."

    Debbie "The embroidery's not the best and it was hell finding matching thread,, but I had fun making it."

    Mike "You made this?"

    Narrator "After examining the hat like it's some sort of rare specimen, Mike twirls it around and plops it onto his head."

    Mike "I love it!"

    Debbie "Eh, decent at best."

    Narrator "Debbie playfully elbows the host's shoulder and cracks a grin."

    #Mike "Now you're clowning on me."

    Narrator "Tossing the gift box aside the two hug. There's a moment of ease before Debbie swats the red cap off Mike's head and catches it in her other hand."

    Debbie "Can I get an outro?"

    Mike "Like on the spot?"

    Narrator "She hands the hat back."

    Debbie "If you've got one."

    show BG Studio Room Spooky
    stop music fadeout 0.5
    Madhouse "Call me king tut cause that's a {b}wrap{/b}!\n\nNow close the casket and watch out for spike {b}traps{/b}!"

    Debbie "{sc=3}Yeahaha!{/sc}{nw}"

    extend "\n\nYou've still got it!"

    #Mike "I'm gonna miss you."

    Debbie "Raise hell for me,, 'kay?"

    #stop music fadeout 0.5
    scene BG Graveyard Night

    camera:
        camera_zoom(z=-500,x=-250,y=-200)
        pause 0.5
        camera_zoom(z=-500,x=-250,y=200,t=3.0)

    play ambiance forest_ambianceb fadein 5.0
    python:
        adjustChar("OH",eyes=1,brow=0,armR=0,eyeFrame=1)
        adjustChar("MM",hat=0,eyes=7,mouth=3,armR=2,armL=2)

    show halfaugust:
        shaded("#ebc0f8")
        xcenter 0.65
        matrixtransform rotated(y=180)

    show oswald:
        shaded("#ebc0f8")
        xcenter 0.8

    with Dissolve(0.5)

    python:
        adjustChar("OH",eyes=0,brow=1,eyeFrame=1,armL=0,armR=0)
        adjustChar("HalfAugust",mouth=1,eyeFrame=0,eye=2,brow=0,ear=0)

    Narrator "A bright green hand shoots out of the shattered lantern. It slaps down and grabs a mossy headstone."
    show madhouse:
        matrixtransform rotated(y=180,z=60)
        shaded("#c0fac8")
        yoffset 700
        xcenter 0.2
        parallel:
            pause 0.25
            ease 1.5 matrixtransform rotated(y=180)
        parallel:
            ease 1.5 yoffset 0

    camera:
        camera_zoom(z=-500,x=-250,y=200)
        pause 2.0
        camera_zoom(z=-100,t=3.0)

    $musicPlayer.playSong(song = "missing_you_song",fadeIn=4)
    Narrator "Madhouse drags himself through the dirt, gasping and coughing up ectoplasm."

    $adjustChar("MM",eyes=11)
    extend "\n\nHis cap is gone."
    python:
        adjustChar("OH",eyes=5,brow=0,eyeFrame=0)

    camera:
        camera_zoom(z=-100,t=0.5)
    #Madhouse "I win!"

    $adjustChar("HalfAugust",mouth=3,eyeFrame=3,eye=0,ear=1,brow=3)
    show halfaugust:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0
    August "He's okay!"

    python:
        adjustChar("HalfAugust",eyeFrame=0,eye=2,ear=1,brow=0)
        adjustChar("MM",eyes=9)
    Madhouse "..."
    show halfaugust:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5  matrixtransform RotateMatrix(0, 180, -10.0) yoffset 30

    $adjustChar("HalfAugust",mouth=0,eyeFrame=1,eye=3,ear=0,brow=3)
    August "I'll uh,, give you some space."
    $adjustChar("MM",mouth=3,armR=2,armL=2,eyes=8)

    camera:
        camera_zoom(z=-100)
        pause 0.75
        camera_zoom(z=-450,x=-300,y=-40,t=1.0)

    show robyn behind oswald:
        matrixtransform rotated(y=180)
        shaded("#ebc0f8")
        enterFromRight(x=0.35,t=1.5)

    show halfaugust:
        xcenter 0.65
        pause 0.5
        ease 0.4 xcenter 0.62


    show oswald:
        xcenter 0.8
        pause 0.5
        ease 0.4 xcenter 0.83

    Narrator "You brush past the two cryptids, your boots kicking up pebbles as you run to the phantom."
    show madhouse:
        ease 0.5 xcenter 0.15 yoffset 0

    $adjustChar("MM",hat=0,eyes=9,mouth=1,armR=3,armL=2,blush=1)

    Madhouse "{size=35}Don't look at me!{/size}"

    $adjustChar("Robyn",mouth=0,eyes=3,brow=2)

    show robyn:
        parallel:
            unflipCharDelayed(1.2,0.5)
        parallel:
            pause 1.2
            ease 0.5 xcenter 0.37

    Narrator "Mike recoils as you approach, shielding his face from your prying eyes. You turn around."

    $adjustChar("Robyn",mouth=4,eyes=1,brow=2)

    show robyn:
        xcenter 0.37
        matrixtransform rotated()

    Robyn "What am I gonna do with you?"

    python:
        adjustChar("MM",hat=0,eyes=8,mouth=2,armR=2,armL=1,blush=0)
        adjustChar("Robyn",mouth=1,eyes=3,brow=2)

    show madhouse:
        parallel:
            unflipCharDelayed(0.7,0.5)

        #parallel:
            #ease 0.5 yoffset 0
            #idleFloat(2.2,25)

    Madhouse "You could smash your phone. That'd be the smart move."

    $adjustChar("Robyn",mouth=5,eyes=2,brow=2)
    show madhouse:
        matrixtransform rotated()
        ease 0.5 yoffset 0
        #idleFloat(2.2,25)

    Robyn "I wouldn't dream of it."

    $adjustChar("MM",mouth=3,armR=2,armL=1,eyes=8)

    Madhouse "Are you hurt?"

    Robyn "No, you can thank team fido for that."

    #Narrator "You gesture to Oz and August who're caught up silently bickering with each other."

    $adjustChar("MM",mouth=1,eyes=7)

    Madhouse "That's a relief. \n\nI shouldn't have ditched y'all."
    $adjustChar("MM",mouth=3,eyes=11)
    Madhouse "I thought., I was done for."

    python:
        adjustChar("Robyn",mouth=4,eyes=0,brow=0)

    Robyn ".,How'd you get your body back?"

    python:
        adjustChar("MM",mouth=1,eyes=9)
        adjustChar("Robyn",mouth=5)

    Madhouse "I did some self reflecting."

    $adjustChar("MM",eyes=7)
    Madhouse "Looks like {color=#bc8bff}Granny{/color} was right!"

    show madhouse:
        parallel:
            ease 0.5 yoffset 0
            #idleFloat(2.2,10)
        parallel:
            flipChar(0.5)

    $adjustChar("MM",mouth=3,eyes=10,armR=1)
    $adjustChar("Robyn",mouth=5,eyes=4,brow=2)

    Madhouse "But don't go thinking y'all're getting rid of me just yet."

    $adjustChar("MM",eyes=9,mouth=0)

    Madhouse "Not before I learn bass guitar."

    $adjustChar("Robyn",mouth=1,eyes=1,brow=2)

    Robyn "Did you always have horns?"

    $adjustChar("MM",mouth=1,eyes=11)
    Madhouse "On my hat, sure, but that asshole stole it."
    $adjustChar("MM",eyes=11,mouth=3)
    $adjustChar("Robyn",mouth=0,eyes=2,brow=0)

    Robyn "You mean., this hat was stolen?"
    $adjustChar("MM",mouth=1,eyes=7)

    show robyn:
        flipChar(0.5)

    show mmhat:
        xcenter 0.26
        yoffset 700
        matrixtransform rotated(y=180)
        shaded("#ebc0f8")
        ease 1.0 yoffset 250

    Narrator "You hold out a crumbled red cap bleeding ectoplasm. \n\nMadhouse hesitates before taking it off your hands."

    $adjustChar("MM",mouth=2,armR=2,armL=2,eyes=9)


    Madhouse "It's covered in dirt and wolf hair."
    $adjustChar("MM",mouth=0,armR=2,armL=2,eyes=11)

    Madhouse "Thanks for savin' it."

    $adjustChar("MM",mouth=1,eyes=8,armL=2,armR=3)

    show mmhat:
        yoffset 250
        matrixcolor TintMatrix("#ebc0f8")
        parallel:
            ease 1.0 matrixcolor TintMatrix("#c0fac8") xcenter 0.15
        parallel:
            ease 0.5 yoffset -100 ycenter 0.715
            ease 0.5 yoffset 0.5

        vibrate()

    show madhouse:
        ease 1.0 yoffset 0

        vibrate()

    stop music fadeout 3.0

    Narrator "He forces the hat over his head."

    hide mmhat

    play music digihouse_mike_song
    python:
        adjustChar("MM",mouth=11,eyes=3,armL=0,armR=0,hat=1)
        adjustChar("Robyn",mouth=5,eyes=0,brow=1)
        songText= "Digihouse Mike"
        musicNote= 9

    show madhouse:
        parallel:
            hoppies_flipped(xIntensity=4)
        parallel:
            startledSquish

    voice mm_laughi

    Madhouse "{sc=10}{size=40}\nB L U A H U H A H A H A H A H A H A \nA H A A A H A H A H A H A H A A A A!{/size}{/sc}"

    show madhouse:
        ease 0.5 yoffset 0 matrixtransform rotated(y=180) yzoom 1 xzoom 1 xoffset 0
        idleFloat(2.2,10)

    show halfaugust:
        shaded("#ebc0f8")
        xcenter 0.65
        matrixtransform rotated(y=180)
        yoffset 0

    show oswald:
        shaded("#ebc0f8")
        xcenter 0.8

    python:
        adjustChar("MM",mouth=1,eyes=5)
        adjustChar("Robyn",mouth=0,eyes=3,brow=2)

    Robyn "{bt}Ehehe!{/bt}"

    $adjustChar("MM",mouth=10,eyes=0,armL=3,armR=3)

    Madhouse "Yours could use some work."

    $adjustChar("Robyn",mouth=6,eyes=4,brow=0)
    $adjustChar("MM",mouth=4,eyes=5,armL=1,armR=1,blush=0)

    Robyn "It's good to have you back."

    $adjustChar("MM",mouth=0,armL=0,armR=0)

    Madhouse "Happy to be here."
    python:
        adjustChar("MM",mouth=1,eyes=0,armL=0,armR=0)
        adjustChar("OH",eyes=5,brow=0,eyeFrame=0)
        adjustChar("HalfAugust",mouth=1,eye=2)
        adjustChar("Robyn",mouth=0,eyes=3,brow=0)

    camera:
        camera_zoom(z=-450,x=-300,y=-40)
        camera_zoom(z=-100,t=2.0)

    Narrator "He points to the two cryptids."
    voice mm_greet

    python:
        adjustChar("MM",mouth=12,armL=1,armR=1,eyes=0)
        adjustChar("OH",eyes=0,brow=1,eyeFrame=0)
        adjustChar("HalfAugust",brow=0,eyeFrame=0,mouth=6)

    show madhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        startledSquish
        idleFloat(2.2,12)

    Madhouse "{b}{sc=3}GENTLEMEN!{/sc}{/b}"

    $adjustChar("MM",mouth=9)
    Madhouse "Thanks for keepin' an eye on {color=#EC2A2A}Meatball{/color} here. I hope [PCthey] didn't cause any trouble for ya."

    Madhouse "Sadly, it seems our efforts were in vain. I'm not buried here."

    python:
        adjustChar("MM",mouth=3,eyes=3)
        adjustChar("Robyn",mouth=5,eyes=1,brow=2)
        adjustChar("OH",eyes=0,brow=0,eyeFrame=1)
        adjustChar("HalfAugust",mouth=2,eye=0,eyeFrame=1,brow=0)


    Robyn "That's the nickname that stuck? You can do better."

    $adjustChar("MM",eyes=1,mouth=4)

    Madhouse "M'yeah that's fair. I'll keep workshopping it.{nw}"

    $adjustChar("MM",mouth=0,eyes=3)

    extend "\n\nLet's get outta here."

    python:
        adjustChar("Robyn",eyes=3,brow=0,mouth=0)
        adjustChar("HalfAugust",eye=2,eyeFrame=1,mouth=6)
        adjustChar("MM",mouth=9,eyes=1)

        musicPlayer.playSong(fadeOut=1.5,song="supernatural_serenade_song")

    show robyn:
        unflipChar(0.3)
        ease 3.0 xcenter -0.5

    show madhouse behind robyn:
        pause 0.9
        ease 4.0 xcenter -0.5

    Robyn "We'll meet you at the car."

    August "..."
    camera:
        camera_zoom(z=-370,x=180,y=-100,t=1.1)

    python:
        adjustChar("OH",eyes=5,brow=0,eyeFrame=0)
        adjustChar("HalfAugust",mouth=3,eye=1,eyeFrame=0,ear=1)

    voice august_nicemoves
    August "Nice moves back there."

    python:
        adjustChar("OH",eyes=1,brow=1)

    Oz "{size=-10}{i}...{/i}{/size}"

    python:
        adjustChar("HalfAugust",mouth=2,eye=0,eyeFrame=1,brow=2,ear=2)

    voice august_ididreadyournote
    August "I uh,, I did read your note. Sorry for bein' a jerk about it."

    $adjustChar("OH",eyes=5)
    Narrator "Oz doesn't budge. Like he gives a rat's ass."

    $adjustChar("HalfAugust",mouth=6,eye=2,eyeFrame=1)
    $adjustChar("OH",eyes=0)
    voice august_godknowsthiscounty
    August "Wanting to help people is pretty admirable,, god knows this county needs it."

    Oz "..."

    $adjustChar("HalfAugust",mouth=2,eye=1,eyeFrame=0,brow=0,ear=0)
    voice august_isthatwhyyouwearthat
    August "Is that why you wear that thing?"

    $adjustChar("HalfAugust",mouth=1,eyeFrame=1,brow=0)
    $adjustChar("OH",eyes=6,brow=3,eyeFrame=0)
    Oz ""

    $adjustChar("HalfAugust",mouth=0,eye=3,eyeFrame=3,brow=2)
    voice august_momwouldflickmynose
    August "Yeah, my mom'd flick my nose whenever I'd bite or gnaw on the furniture. {nw}"

    python:
        adjustChar("HalfAugust",mouth=2,eye=2,eyeFrame=1,ear=2)


    extend "\n\nIt left me flinchy and never fixed a thing,, but at least it wasn't a muzzle."

    python:
        adjustChar("HalfAugust",mouth=6,eye=1,brow=0,eyeFrame=0,ear=1)
        adjustChar("OH",eyes=4,brow=1)

    Narrator "Oz gives the wolfman a hefty pat on the back."

    python:
        adjustChar("HalfAugust",eye=0,mouth=3,eyeFrame=3,brow=2,ear=0)
        adjustChar("OH",eyes=6,brow=0)

    voice august_doyouneedaridehome
    August "Do you need a ride home? It's a hell of a walk."
    python:
        adjustChar("OH",eyes=0)
        adjustChar("HalfAugust",eye=1,eyeFrame=0)

    Narrator "Oz thinks a moment,{nw}"

    $adjustChar("OH",eyes=1)
    extend " before shaking his head no."
    python:
        adjustChar("OH",eyes=2,brow=0,armL=2,armR=0)
        adjustChar("HalfAugust",eye=0,mouth=1,ear=1)

    show oswald:
        xcenter 0.8
        ease 3.0 xcenter 1.2

    show halfaugust:
        unflipChar(0.5)

    Narrator "The howler slinks away, disappearing into the dense woods beyond."

    scene BG Black with Dissolve(0.5)

    pause 0.5
    play sfx phone_notif

    $unlockHangout("MM",1)
    Narrator "Looks like {color=#3bec27}{b}Madhouse Mike{/b}{/color} wishes to spend time with you! Would you like to view this {color=#ED2A82}{b}hangout{/b}{/color} now?{nw}"

    menu:
        extend ""

        "Yes!":
            call MM_Hangout1 from _call_MM_Hangout1
        "Not now.":
            Narrator "You can access this event in the {color=#ED2A82}{b}Chapter Select{/b}{/color} menu."
            pass

    $musicPlayer.playSong(fadeOut=1.5)
    jump Ch1_Day2Night
