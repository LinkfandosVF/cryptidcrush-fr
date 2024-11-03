label Ch1_LakeIntro:
    scene BG Black
    camera:
        camera_zoom(x=60,y=-30,z=-100)

    Narrator "You wrap up the day with a nature walk around the lake."

    Narrator "Strolling behind your apartment, you follow a footpath cutting through the thick brush leading down to the water."
    scene BG Lake Night
    play ambiance forest_ambianceb fadein 5.0 fadeout 4.0
    python:
        musicPlayer.playSong(song="boots_on_the_shore_bearsome")
        timeText = "7:00PM"

    with Dissolve(2.0)
    Narrator "The sun begins to set over the mountains. You hear the waves lap against the shore, and feel a cold breeze nip your ears. The temperature certainly drops around nightfall."

    Narrator "You walk the rocky shore, taking in the scenery as you go. Maybe it's nature's charm talking, but you feel at peace."

    Narrator "A pair of leather boots sit at the water's edge, a rolled up piece of paper poking out of one of the shoes."

    Narrator "You wander over and examine the misplaced gear. Did somebody lose these?"

    Narrator "You lean down and snatch the parchment out of the boot."

    Narrator "Unfolding the makeshift scroll, you realize it's a torn page from a wordy text book. Certain passages are circled in red pen."

    Narrator "It's no treasure map. Rather, a passage describing aquatic monsters across the world."

    Narrator "{bt=3}\"This could be a clue!\"{/bt} Your adventurous spirit declares, hastily crafting a wild story behind these misplaced boots."

    Narrator "{sc}{b}Ker-SPLOOSH!{/b}{/sc}"
    show CG Tail Peek
    with Dissolve (0.5)

    Narrator "With a gasp you see a sleek, shimmering emerald tail breach the water."

    Narrator "You scramble for your phone. There's no way that's a whale!"

    Narrator "It's got to be {b}her{/b}! \n\nHow'd she stray so far from home? Does she look like the picture books?"

    Narrator "The tail sways a moment before sinking back into the waves."
    scene BG Black
    with Dissolve (0.5)
    Narrator "With a wistful sigh, you stuff your hands in your coat pockets and head back."
    stop ambiance fadeout 1.0

    jump Ch1_AtlasAugustConvo

default ch1_gusatlas_choice = 1
label Ch1_AtlasAugustConvo:
    python:
        timeText = "7:15PM"
        musicPlayer.playSong(fadeOut=1.5)

    scene BG Cabin Night
    with Dissolve (0.5)

    nvl clear
    Narrator "After returning home, Atlas tucks himself away in the attic to work away at a broken down radio."

    $musicPlayer.playSong(song="supernatural_serenade_song",fadeIn=1,fadeOut=2)
    nvl show Dissolve(0.3)
    NVL_Narrator "Some time passes, and soon after, there's a knock on the mothman's door."

    NVL_August "I saved you a plate in the fridge, since you didn't come down for dinner."

    NVL_Atlas "Oh! Sorry, I lost track of time."

    NVL_August "What're you doing?"

    NVL_Atlas "Tryin' to get this frickin' radio to work."

    NVL_August "Want me to take a crack at it?"

    NVL_Atlas "You'll break it."

    NVL_Narrator "August sits on the edge of Atlas' bed, folds his arms behind his head and falls back onto the comforter."

    NVL_August "You're probably right."

    #NVL_Narrator "August sighs."

    NVL_Atlas "I’m sorry about last night. \n\nI should’ve stayed with you when you were hurt."

    NVL_August "It’s okay. I was rather unpleasant back there."
    #August "I’m just glad you’re getting out there and making friends."

    NVL_Narrator "August seems hesitant, his words hiding what he's really feeling."

    NVL_August "You think you could run some errands while I’m \nout tomorrow?\nI need you to pick up some fabric then swing\n by the pharmacy for me."

    NVL_Atlas "Sounds boring."

    NVL_August "Consider it a second chance after last night's kerfuffle."

    NVL_Atlas "I mean, it is kinda,, sorta,, slightly your fault. {nw}"

    extend "\n\nFor trusting the scatterbrain."

    NVL_August "Don’t say that Atlas."

    NVL_Atlas "Sorry."

    NVL_Narrator "...{nw}"

    if ch1_gusatlas_choice == 1:
        NVL_August "Wanna go apple picking this weekend? I'm itching for a piping hot cider. Maybe bake a pie or roast some cinnamon apples."

        NVL_Atlas "Shoot, I already made plans with Jamie."

        NVL_Atlas "They're off work Saturday so we're gonna hang out."

        NVL_August "Why don't you bring 'em along? Jamie's a good kid."

    elif ch1_gusatlas_choice in [2,3]:
        NVL_August "I like having you around."

        NVL_August "You’ve just gotta step it up. Set a good example."

        NVL_August "So no more all-nighters, got it?"

        NVL_Atlas "Yeah sure,, when you wear shirts that actually fit."

        NVL_August "HAH!"

    NVL_August "Now come downstairs, June wants to show you the jigsaw puzzle she’s been working on."

    NVL_Atlas "Hey, Gus?"

    NVL_Narrator "August glances over his shoulder as Atlas holds out the portable radio in his wings."

    NVL_Atlas "Could you., fix this, please?"

    NVL_August "I'll see what I can do."

    NVL_Narrator "The two make their way downstairs."
    nvl hide

    scene BG Black
    with Dissolve(1.0)

    pause 0.2
    jump Ch1_Day1Night
