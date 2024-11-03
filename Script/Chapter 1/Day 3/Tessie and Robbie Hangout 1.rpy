label Ch1_TessieGusTalk:

    python:
        musicPlayer.playSong(song="boots_on_the_shore_bearsome",fadeIn=1,fadeOut=2)
        timeText = "12:00AM"
        adjustChar("August",eye=3,eyeFrame=2,brow=2,hair=2,sweater=1,mouth=5,wolfEars=0,coat=0)

    camera at camera_default
    scene BG Near Cafe
    with quickDissolve

    camera:
        shaded("#ffe7ee")
        camera_zoom(z=-400,y=-100,x=-300)
        camera_zoom(z=-250,x=160,t=4.0)

    show august:
        xcenter 0.6
        matrixtransform RotateMatrix(0.0, 0.0, -2.0)

    show tessie:
        xcenter 0.8

    $adjustChar("August",eye=2)
    $adjustChar("Tessie",eye=0,eyeFrame=0,mouth=3)

    Tessie "Are you ready for Friday? What do you think of the story so far?"

    $adjustChar("August",eye=4,eyeFrame=0,mouth=3)
    $adjustChar("Tessie",mouth=4)

    August "Oh! Yeah, it's pretty neat. I like the bit where the Duchess of Nottingham drove a flaming carriage through the paper factory."

    $adjustChar("August",eye=1,eyeFrame=0)

    August "...{nw}"

    $adjustChar("August",eye=2,eyeFrame=2,mouth=5)
    $adjustChar("Tessie",mouth=5)

    August "I didn't read it."
    $adjustChar("Tessie",eye=1,eyeFrame=2,mouth=1,brow=2)

    Tessie "Auguuust, I thought you liked books!"
    $adjustChar("August",eye=3,eyeFrame=4,mouth=6,brow=2)

    August "Not historical romance! I like mystery and intrigue!"

    $adjustChar("August",eyeFrame=2,mouth=5)
    $adjustChar("Tessie",eye=0,mouth=0,eyeFrame=0)

    Tessie "There is intrigue!"

    $adjustChar("Tessie",eye=0,mouth=5,eyeFrame=1)

    Tessie "Why didn't you say no? We could've picked a different book!"
    $adjustChar("August",eye=4,eyeFrame=0,brow=1,mouth=2)

    August "Because I'm a people pleaser!"
    $adjustChar("Tessie",mouth=0,eyeFrame=2,brow=1)

    Tessie "Well, stop that!"

    $adjustChar("August",eye=3,eyeFrame=2,mouth=5,brow=2)

    August "Tess, I go to book club to eat fancy cheeses and make goo-goo eyes at the host. I don't have the energy to be a contrarian."

    $adjustChar("Tessie",mouth=5,eyeFrame=2,brow=0)
    Tessie "Can you at least try to engage?"

    $adjustChar("August",eye=2,eyeFrame=0)
    August "Alright, alright,, I'll pick up the audiobook."

    $adjustChar("Tessie",mouth=2,eyeFrame=0)
    Tessie "Yaaay!"

    python:
        adjustChar("Tessie",mouth=1,eyeFrame=2,eye=2)
        adjustChar("Robbie",eye=2,mouth=0,armR=0)

    show robbie:
        xcenter -0.5
        ease 0.9 xcenter 0.1

    Tessie "You're not trying to people please me right now, are you?"

    $adjustChar("August",eye=3,eyeFrame=2,mouth=1,brow=4)

    August "Maybe."

    python:
        adjustChar("Tessie",mouth=4,eyeFrame=0,eye=0)
        adjustChar("August",eye=4,eyeFrame=0,brow=1,mouth=2)

        musicPlayer.playSong(song="silence",fadeOut=1,fadeIn=3)


    Tessie "Haha! Ah, you're a scamp."

    python:
        musicPlayer.playSong(song="day_crimes_song")
        adjustChar("Tessie",eye=0,mouth=0,eyeFrame=2)
        adjustChar("August",eye=2,eyeFrame=0,mouth=5,brow=2)

    camera:
        camera_zoom(t=3.0)

    show robbie:
        ease 1.4 xcenter 0.2

    show august:
        ease 1 xcenter 0.68 matrixtransform RotateMatrix(0.0, 0.0, -3.0)

    Robert "..."

    $adjustChar("Tessie",eye=1,eyeFrame=0,mouth=1)

    Tessie "Gus, look! It's that guy I told you about!"

    $adjustChar("August",eye=3,eyeFrame=1,brow=3)

    show august:
        ease 0.5 matrixtransform rotated(y=180,z=0.0)

    August "Frog guy?"

    camera:
        camera_zoom(z=-500,x=-380,y=-130,t=0.5)

    show robbie:
        matrixtransform rotated() xcenter 0.2
        ease 0.4 matrixtransform rotated(y=180) xcenter 0.2

    $adjustChar("Robbie",eye=2,mouth=2)

    Narrator "Robbie quickly turns away. He zoned out not realizing he was staring at strangers!"

    $adjustChar("Robbie",eye=3,mouth=0)

    August "Wasn't he the one throwing rocks off the south road bridge?"

    $adjustChar("Robbie",eye=2,mouth=7)
    show robbie at startledSquish

    Tessie "Yeah! One of 'em nearly hit me!"

    August "I'll talk to him."
    $adjustChar("Robbie",eye=1,mouth=3)

    camera:
        camera_zoom(z=-500,x=-380,y=-130)

    show august:
        xcenter 0.5

    show tessie:
        xcenter 0.65

    $adjustChar("Robbie",eye=2,mouth=0)
    Narrator "Running isn't an option now. It looks like Robbie's gotta wing-it."

    camera:
        camera_zoom(z=-200,x=-125,t=0.75)

    show robbie:
        matrixtransform rotated(y=180)
        ease 0.6 xcenter 0.2 matrixtransform rotated()

    python:
        adjustChar("Tessie",mouth=1,eyeFrame=2)
        adjustChar("August",eye=1,eyeFrame=0,mouth=5,brow=2)
        adjustChar("Robbie",eye=5,mouth=1)

    Robert "{sc=2}{b}Graaawrh!{/b}{/sc}\n\nRun away puny surface dwellers!"
    show robbie at hoppies(xIntensity=0.6)

    python:
        adjustChar("Robbie",eye=1,mouth=6)
        adjustChar("Tessie",mouth=5,brow=1)
        adjustChar("August",eye=3)

    Robert "Behold my twisted form! Do my crooked fangs and putrid flesh not make you quake in terror? Flee while you can!"

    show robbie:
        ease 0.15 yoffset 0

    $adjustChar("August",eye=2,eyeFrame=4,mouth=6,brow=1)

    August "Aw man, don't say that."

    $adjustChar("Tessie",mouth=3,brow=0,eyeFrame=0)

    Tessie "Yeah, no offense,, but you're the least weird thing I've seen all day."

    python:
        adjustChar("Tessie",mouth=4)
        adjustChar("August",eye=3,brow=2,eyeFrame=2,mouth=5)
        adjustChar("Robbie",eye=2,mouth=0)

    Robert "What?"

    $adjustChar("Robbie",eye=1,mouth=3)

    Robert "But you're supposed to run away."

    $adjustChar("Tessie",mouth=5,brow=2,eyeFrame=2,eye=0)

    Tessie "Oh no no."

    $adjustChar("Tessie",mouth=3,eye=2)

    Tessie "You're in Longhope sweetheart. Nobody's gonna laugh or run away from you."

    python:
        adjustChar("Robbie",eye=2)
        adjustChar("Tessie",mouth=4,eyeFrame=0,eye=0)
        adjustChar("August",eye=4,eyeFrame=0,brow=1,mouth=3)

    August "Yeah, I think your scales look nice!"

    python:
        adjustChar("Robbie",eye=3,mouth=0)
        adjustChar("August",mouth=2)
    Robert "{sc}Huh?{/sc}"

    python:
        adjustChar("Robbie",eye=7,mouth=7)

    Robert "{sc}I-I uh uhm.{/sc}"

    python:
        adjustChar("Robbie",eye=2,mouth=1)
        adjustChar("Tessie",brow=0,eye=1)
        adjustChar("August",eye=3,mouth=5,brow=2)

    Robert "Okay, now I'm confused."

    $adjustChar("Robbie",eye=3,mouth=3)

    Robert "So like,, a couple days ago I spoke to some owl fella with bright red eyes."

    python:
        adjustChar("Robbie",eye=1,mouth=0)
        adjustChar("Tessie",mouth=1)
        adjustChar("August",eyeFrame=2)

    extend "\n\nHe kept askin' me these stupid questions."

    Robert "Like \"What're you ignoring right now?\" and \"What's your greatest weakness?\""

    $adjustChar("Robbie",eye=3,mouth=1)
    Robert "What're you a cop?! Get outta my face!"

    python:
        adjustChar("Robbie",eye=5,mouth=7)

    Robert "Then I woke up here."

    python:
        adjustChar("Robbie",eye=2,mouth=0)
        adjustChar("Tessie",mouth=0,eye=0,brow=0,eyeFrame=2)
        adjustChar("August",eye=2,mouth=1,eyeFrame=1,brow=3)

    August "Like the Mothman?"

    python:
        adjustChar("Robbie",eye=0)
        adjustChar("Tessie",mouth=5,brow=1,eye=3)
        adjustChar("August",eye=2,mouth=0,eyeFrame=0,brow=2)

    Tessie "No way. Nobody's seen that deadbeat in ages."

    python:
        adjustChar("Robbie",eye=0)
        adjustChar("Tessie",mouth=1,brow=0,eye=2)

    Tessie "I bet he's frozen in the artic tundra by now."

    $adjustChar("August",eye=3,mouth=4,eyeFrame=2,brow=1)

    August "I., don't wanna talk about this."

    $adjustChar("August",eye=1,mouth=0,eyeFrame=2,brow=1)
    $adjustChar("Tessie",mouth=5,brow=2,eyeFrame=2,eye=0)

    Tessie "Oh,, sorry Auggie."

    $adjustChar("August",eye=4,mouth=6,eyeFrame=0,brow=1)

    August "It's fine!"

    $adjustChar("Tessie",eye=0)

    Tessie "Did Atlas ever talk to you about it?"

    $adjustChar("August",eye=2,mouth=0,eyeFrame=2,brow=1)

    August "He doesn't talk to me about anything."

    python:
        adjustChar("Robbie",eye=2)
        adjustChar("Tessie",mouth=4,eyeFrame=0,eye=1,brow=0)
        adjustChar("August",eye=3,eyeFrame=2,brow=2,mouth=5)

    Tessie "Well,, I hope you enjoy your time here frogman."

    $adjustChar("Robbie",eye=5,mouth=7)

    Robert "How can I?"

    $adjustChar("Robbie",eye=1,mouth=3)

    Robert "I didn't ask to be tossed out like week old lo mein."

    $adjustChar("August",eye=2,eyeFrame=2,mouth=6,brow=5)
    show august:
        ease 0.5 matrixtransform rotated(y=0,z=-5.0)

    August "Wait. I'm sensing tomfoolery."

    $adjustChar("August",eye=1,eyeFrame=2,mouth=5,brow=0)

    show august at startledSquish:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    August "I need to make a phonecall."

    jump Ch1_AtlasDoctorVisit_Confrontation
