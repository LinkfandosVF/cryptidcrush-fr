label Ch1_MondayMorning:
    python:
        renpy.music.set_volume(1.0, delay=0, channel=u'music')
        musicPlayer.playSong()
    stop music2 fadeout 10.0

    Narrator "Tu est réveillé par Taro qui te saute sur le ventre."

    scene BG Apartment Day

    python:
        musicPlayer.playSong(song="undead_icebreakers_song",fadeIn=2,fadeOut = 1)
        timeText = "10:30AM"

        adjustChar("Taro",pawR=1,eye=1,mouth=3)

    show taro:
        matrixcolor TintMatrix("#ffd5bd")
        xcenter 0.7
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat

    camera:
        blur 0
        camera_zoom(z=-600,x=300,y=10)

    with Dissolve(2.0)

    voice taro_forgoodnesssake
    Taro "Rooh serieux nom de dieu!"

    Robyn "Taro!"

    camera:
        camera_zoom(z=-350,x=80,y=10,t=1.5)

    python:
        adjustChar("Robyn",armR=0,brow=3,eyes=1,mouth=2)
        adjustChar("Taro",pawR=0,eye=5,mouth=1)

    show robyn pjs:
        matrixcolor TintMatrix("#ffd5bd")
        xcenter -0.6
        pause 0.8

        xcenter 0.35
        yoffset 700
        ease 0.8 xcenter 0.35 yoffset 0

    Taro "Tu bougeait tellement dans ton someil que tu m'a presque éjecté!"

    show robyn pjs:
        xcenter 0.35
        yoffset 0

    python:
        Taro_State["eye"] = 1
        adjustChar("Robyn",brow=0,eyes=2,mouth=5)

    #Narrator "She sits down with a huff and looks away."

    $adjustChar("Robyn",brow=1,mouth=4)
    Robyn "J'ai fait un rève horrible... et Atlas était dedans!"


    $adjustChar("Taro",pawR=2,eye=3,mouth=3)
    Taro "Wow, en effet c'est horrible. Les cauchemards c'est commun avec toi?"

    python:
        adjustChar("Taro",pawR=0,eye=0,mouth=3)
        adjustChar("Robyn",brow=3,eyes=3,mouth=3)

    Robyn "Pas depuis que j'ai déménagé!"

    Narrator "Tu est fatigué et plus que de mauvais poil."

    python:
        Robyn_State["eyes"] = 1
        adjustChar("Taro",mouth=0,pawL=1)

    Taro "Bon mwien, ravis que toi sait réveillé."

    Narrator "Taro ammène sa pate sur son menton et réfléchis."

    $adjustChar("Taro",eye=1,mouth=2)
    Taro "Tu peux décrire ton rève pendant que tu fait le déjeuné."


    python:
        adjustChar("Taro",pawR=0,eye=0,mouth=3)
        adjustChar("Robyn",brow=0,eyes=2,mouth=5)

    Robyn "T'es sur? C'est un peu zarbi."


    Narrator "Tu sort tu lit, et trébuche presque sur le papillon qui dors sur le sol. C'est un peu mignon.{nw}"
    menu:
        extend ""

        "Le réveiller!":
            Narrator "Tu t'accroupis a coté de lui."

            Robyn "Atlas, réveille toi."

            Atlas "..."

            Robyn "Psst."

            voice atlas_snorea

            Atlas "{sc}....{/sc}"

            Narrator "Tu caresse gentillement l'antenne d'Atlas, un peu comme une corde de guitare."

            show atlas:
                matrixcolor TintMatrix("#ffd5bd")
                xcenter 0.5
                yoffset 600
                ease 0.3 yoffset 0

            camera at camera_shake

            $adjustChar("Atlas",feelers=1,eye=21)
            Atlas "{size=30}QUOI.{/size}"

            Narrator "Atlas s'assois,, et ronchonne."

            Atlas "[PCname], He vais te mordre les doigts."

            $adjustChar("Robyn",mouth=0,eyes=3)

            Robyn "Est ce que tu {i}as{/i} une bouche, même?"

            python:
                adjustChar("Atlas",eye=8,feelers=0)

            Atlas "Tu me réveille juste pour me demander {sc=3}CA?!{/sc}"

            $adjustChar("Robyn",mouth=0,eyes=1)
            Robyn "T'évite la question."

            python:
                Atlas_State["eye"] = 17
                audio.delayedThunk = ["<silence .4>", "audio/SFX Battle/Hurt_B.ogg"]

            camera:
                pause 0.4
                camera_shake

            show atlas:
                matrixtransform RotateMatrix(0, 0, 0)
                ease 0.5 yoffset 700 matrixtransform RotateMatrix(0, 0, 180) xcenter 0.75

            play sfx delayedThunk
            $musicPlayer.playSong()

            Narrator "Atlas se retourne et couvre ses yeux avec ses ailes."

            Atlas "{sc=2}Grrrmghrgmh.{/sc}"

            Robyn "Gru.,mpy."

            Atlas "Oui."

            Atlas "Et je te vole ton lit."
            
            Robyn "Bon allez, si tu veux. Repose toi."

            $musicPlayer.playSong(song="pleasant_conversation_song",fadeOut=2,fadeIn=1)
            scene BG Black with nwDissolve(0.5)

            Narrator "Tu te lève et te dirige vers la cuisine alors qu'Atlas se roule dans ta couverture."

        "Laisser la marmotte dormir.":
            Narrator "Taro flotte lentement vers toi."

            $Taro_State["mouth"] = 2
            Taro "Mettons le dans la baignoire."

            $Robyn_State["eyes"] = 1
            Robyn "Nan. Cette nuit était pas facile."

            scene BG Black with nwDissolve(0.5)

            Narrator "Tu évite la boulle de plume et continue de te lever, tu te douche, t'habille. Et miraculeusement sans réveiller Atlas."

    $timeText = "11:00AM"
    Taro "Dooonc, se rève que t'a eu."

    Narrator "Tu décris l'appartement au chat alors que tu te sert un bol de céréales."
    show BG Apartment Kitchen

    camera:
        camera_zoom(z=-400,y=200,x=-100)
        camera_zoom(z=-400,x=-100,t=3.0)

    show taro:
        xcenter 0.48
        matrixtransform RotateMatrix(0,180,0)
        matrixcolor TintMatrix("#fee3eb")
        idleFloat(2,10)

    show robyn:
        xcenter 0.3
        matrixcolor TintMatrix("#fee3eb")

    with { "master" : Dissolve(1.0) }

    python:
        adjustChar("Robyn",eyes=1,mouth=5,brow=2)
        adjustChar("Taro",eye=2,mouth=3,pawL=0)

    voice taro_wowthatisbad
    Taro "Wow, c'est vraiment pas cool."

    $Taro_State["eye"] = 0
    voice taro_nightmaresvaccumscatfood
    Taro "Les cauchemards sont censé être genre des aspirateurs géants... ou des croquettes sèche!"

    $adjustChar("Robyn",mouth=4,eyes=2)
    Robyn "Des croquettes?"

    python:
        Robyn_State["mouth"] = 5
        adjustChar("Taro",mouth=0,pawL=1,eye=5)

    Taro "Ouais, des trucs débiles."

    Taro "T'a besoin d'un truc pour éviter ses genres de rèves."

    python:
        Taro_State["eye"] = 0
        adjustChar("Robyn",eyes=1,mouth=3,brow=3)

    Robyn "Ouais ouais, avec un bon régime et des heures de sommeil normales. J'sais."

    $adjustChar("Robyn",eyes=0,mouth=5,brow=0)
    Robyn "J'suis peut être juste stréssé."

    $Taro_State["pawL"] = 0
    voice taro_nosilly
    Taro "Mais non!"

    Taro "C'est comme si c'était à cause d'autre chose. Un genre de force bizare"

    Narrator "Taro se pose près de ton portable et le regarde."

    $adjustChar("Robyn",eyes=1,mouth=1,brow=3)
    Robyn "Tu crois c'est a cause de Madhouse?"

    python:
        adjustChar("Taro",mouth=0,eye=5)
        adjustChar("Robyn",eyes=0,mouth=5,brow=1)

    Taro "Purr-être."

    $adjustChar("Robyn",armR=1,eyes=0,mouth=1,brow=0)
    Narrator "Tu tapote l'écran de ton téléphone et l'écran s'allume."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=3)
        BM_State["face"] = 14

        musicPlayer.playSong(song="not_so_spooky_song")

    camera:
        camera_zoom(z=-200,t=0.5)

    show taro:
        xcenter 0.48
        ease 0.5 xcenter 0.675
        idleFloat(2,10)

    show blobhouse:
        zoom 0
        matrixtransform RotateMatrix(0,0,0)
        matrixcolor TintMatrix("#fee3eb")
        xcenter 0.4
        parallel:
            ease 0.6 xcenter 0.5
        parallel:
            ease 0.2 zoom 1.0
        parallel:
            ease 0.3 yoffset -200
            ease 0.3 yoffset 0
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0,0,360*2)

        matrixtransform RotateMatrix(0,0,0)
        pause 0.3
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.2
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        pause 0.05
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.3 matrixtransform RotateMatrix(0,0,0)

        idleFloat(2.2,12)

    voice mm_helplessghostieguy
    Madhouse "Hey,, Laissez moi dormir! Je suis un petit fantôme sans défense."

    show taro:
        xcenter 0.675
        idleFloat(2,10)

    $adjustChar("Taro",eye=1,mouth=2,pawR=1)
    Taro "Tu vois? Suspicieux."

    show blobhouse:
        xcenter 0.5
        zoom 1.0
        yoffset 0
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        idleFloat(2.2,12)

    python:
        adjustChar("Robyn",eyes=2,brow=1,mouth=5)
        BM_State["face"] = 1
        Taro_State["mouth"] = 1

    Madhouse "C'est juste ma voix."

    python:
        adjustChar("Taro",pawR=0,eye=0,mouth=3)
        adjustChar("Robyn",mouth=3,brow=0)

    Taro "Si tu en est si sur, pourquoi tu était en train de te balader hier soir?"

    Madhouse "Non, ca c'était toi!"

    $adjustChar("Taro",pawR=2,pawL=1,mouth=0,eye=3)
    Taro "Je suis incorporel, Tu crois qu'une boite en plastique m'arrète?"

    $adjustChar("Robyn",eyes=1,mouth=1,brow=3)
    Robyn "Cela éxplique ainsi mon budget nourriture."

    show blobhouse:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        idleFloat(2.2,12)

    python:
        BM_State["face"] = 4
        Taro_State["eye"] = 0

    Madhouse "T'es sur que ce chat c'est un fantôme? C'est que la dernière fois que j'ai verifié, les fantômes ça mange pas."

    Taro "T'a déja éssayé?"

    $BM_State["face"] = 5
    Madhouse "Plein de fois. Mais le livreur à jamais passsé les grillages."

    $adjustChar("Taro",eye=1,mouth=2)
    Taro "Un peu comme s'il se sont fait {sc=2}{b}{color=#EC2A2A}executés!{/color}{/b}{/sc}"

    python:
        BM_State["face"] = 3
        Taro_State["mouth"] = 3

    show blobhouse:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 xcenter 0.55
        block:
            ease 0.07 xoffset 3
            ease 0.07 xoffset -3
            repeat

    show taro:
        ease 0.29 xcenter 0.6 xoffset -3
        block:
            ease 0.07 xoffset 3
            ease 0.07 xoffset -3
            repeat

    Narrator "Ils se regardent dans les yeux en ricannant."

    $adjustChar("Robyn",eyes=0,mouth=5,brow=1)
    Robyn "{bt=3}Boooon{/bt}, on c'est que c'est pas Madhouse."

    show taro:
        xoffset 0
        ease 0.3 xcenter 0.65
        idleFloat(2,10)

    show blobhouse:
        xoffset 0
        yoffset 0
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0) xcenter 0.5
        idleFloat(2.2,12)

    python:
        adjustChar("Taro",pawR=1,pawL=0)
        BM_State["face"] = 9

    Madhouse "Hey, Si t'a besoin d'un porte bonheur… Je pourrais te passer ma casquette!"

    $adjustChar("Robyn",eyes=2,mouth=0,brow=0)
    Robyn "Aw, c'est trop chou."

    $BM_State["face"] = 8
    Madhouse "Pas celui là,, le {i}vrai.{/i}"

    $adjustChar("Robyn",eyes=4,brow=2)
    Robyn "Ouais,, mais je sais qu'il compte quand même beaucoup pour toi. C'est gentil, merci."

    python:
        adjustChar("Taro",eye=2,mouth=2,pawR=2)
        adjustChar("Robyn",eyes=2,mouth=5)

    Taro  "T'es pas {i}MORT{/i} en le portant ce chapeau?"

    python:
        BM_State["face"] = 9
        Taro_State["mouth"] = 1

    Madhouse "Ca ne change rien à la chance qu'il porte!"

    python:
        adjustChar("Taro",mouth=0,eye=5)
        adjustChar("Robyn",eyes=1,mouth=3,brow=2)

    Taro "Personne ne fouillerais ta tombe pour un vieux chapeau."

    python:
        adjustChar("BM",arms=0,face=14)
        adjustChar("Taro",eye=0,pawR=0)

    voice mm_areyoukiddingurbanlegend
    Madhouse "Tu rigole? J'suis une légende urbaine!"

    $adjustChar("BM",face=6)
    voice mm_worthafortune
    Madhouse "Il doit valoir une fortune."

    $adjustChar("BM",arms=0,face=7)

    voice mm_nowthatimdead
    Madhouse "{sc=2}{b}Peut être même plus vu que je suis mort!{/b}{/sc}"

    python:
        adjustChar("BM",face=1,arms=0)
        adjustChar("Taro",mouth=3,eye=2)

    Taro "J'suis certain que n'importe quel charme ferait l'affaire."

    $adjustChar("Robyn",eyes=2,mouth=4,brow=1,armR=0)

    Robyn "Où est-ce que je pourrais trouver ça? Je veux dire, j'ai toujours ma plumme porte bonheur,, mais c'est un peu éxtreme quand même."

    python:
        BM_State["face"] = 6
        Taro_State["mouth"] = 0
        Robyn_State["mouth"] = 1

    Madhouse "T'auras besoin de magie."

    $adjustChar("Taro",pawR=2,eye=5)
    Taro " Il y a plein de boutiques chics par ici, pleines de pierres brillantes et de bougies. Je suis sûr qu'elles auront de quoi éloigner ces cauchemards."
    $adjustChar("Robyn",brow=0,mouth=0)
    Robyn "Sounds like a solid excuse to go out."

    python:
        adjustChar("BM",face=4,arms=1)
        Taro_State["eye"] = 0

    Madhouse "Nan tout ca c'est de la dope! Si tu veux vraiment un truc qui marche, le magason de potion d'Edith est juste au coin de la rue. \n\n\ Elle à payé une pub une fois!"

    $adjustChar("Taro",pawR=1,eye=1,mouth=3)
    Taro "Comme si ca avait l'air mieux."

    $adjustChar("BM",face=1,arms=0)
    Madhouse "Ca vaut la peine d'éssayer."

    $adjustChar("Robyn",eyes=4,brow=2)
    Robyn "Okay, on va aller chez Edith."

    $BM_State["face"] = 9
    Madhouse "Cool!"

    python:
        BM_State["face"] = 1
        adjustChar("Taro",mouth=0,eye=5,pawR=0)

    Taro "{bt=4}Et Atlas?{/bt}"

    $adjustChar("Robyn",eyes=1,mouth=3,brow=0,arm=0)
    show robyn at flipChar(0.3)
    Robyn "Il s'en sortiras."

    camera:
        camera_zoom(y=10,z=-600,t=2)

    show robyn:
        unflipChar(0.3)
        ease 1.5 xcenter 1.2

    show taro:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        ease 1.5 xcenter 1.2

    Narrator "Tu prend tes clés et ton porte feuille, les mets dans tes poches et sort de l'appartement."

    $BM_State["face"] = 8
    Madhouse "\n\n{size=20}Ouais il s'en sortiras.{/size}"

    jump Ch1_OnTheTownToEdiths

image chapter1 title:
    xysize (1280,720)
    blur 10
    "images/CGs/Chapter Title Cards/Chapter 1/LeviathanWaltzA.webp"
    matrixcolor ColorizeMatrix("#000000","#f474ff")
    ease 3.0 matrixcolor ColorizeMatrix("#000000","#ffffff") blur 0

layeredimage ch1ttxt:
    always:
        Text("{ddd=#ba0fed-#32d4ff}{size=60}  Chapitre 1  \n   La valse du léviathan   {/size}{/ddd}")

    always:
        Text("{glitch=3.0}{size=60}{color=#1c112e}  Chapter 1  \n   La valse du léviathan   {/color}{/size}{/glitch}")

image Ch_1_Title_Text:
    #WaveImage("ch0ttxt", amp = 2.75, strip_height = 6,melt=True,freq=35)
    "ch1ttxt"
    xanchor 0.0
    yalign 1.0
    xpos -20
    yoffset -10
    alpha 0
    blur 3
    pause 0.6
    ease 0.5 alpha 1

label CH1_TitleCard:
    $musicPlayer.playSong(fadeOut=2)
    scene black with Dissolve(0.5)
    window hide
    $quick_menu = False
    $quicker_menu_show = False

    scene chapter1 title
    camera:
        camera_default
        camera_zoom()



    with Dissolve(0.75)
    play music chapter_1_song noloop
    $musicPlayer.playSong(song="radioStatic",fadeIn=20,music2=True)
    $renpy.music.set_volume(1.0, delay=0.0, channel=u'music2')
    show Ch_1_Title_Text

    pause
    stop music2 fadeout 3.0
    $renpy.music.set_volume(0.0, delay=3.0, channel=u'music2')
    $quick_menu = True
    return

label Ch1_OnTheTownToEdiths:
    hide screen quicker_menu
    call CH1_TitleCard from _call_CH1_TitleCard
    python:
        musicPlayer.playSong(song="day_crimes_song",fadeOut=2)
        timeText = "11:30AM"

    scene BG DaytimeRoadside

    camera:
        camera_default
        shaded("#dbeaff")
        camera_zoom(z=-500,y=200,x=130)
        camera_zoom(z=-300,x=130,y=50,t=3.0)

    show robyn:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.5

    show taro:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.7
        idleFloat(2,10)

    with Fade(0.5, 0.5, 0.5, color="#000000")

    Narrator "Alors que tu déscend le trottoir, tu prend note mentallement des rues principales de Longhope. \n\nDes lampadères ornées de feuilles d'érable séchées, traçant ton chemin entre les batiments et éshopes dans la rue."

    show robyn:
        xcenter 0.5

    show taro:
        xcenter 0.7
        idleFloat(2,10)

    Narrator "C'est plûtot vivant, des cryptides parlent entre-eux devant un café. L'un d'eux, une grande silouhette poilue te salue de la main, mais tu écarte rapidement ton regard."

    $adjustChar("Robyn",brow=1,eyes=0,mouth=6)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)

    Robyn  "Taro, tu m'as jamais dit que Bigfoot était réel!"

    python:
        adjustChar("Robyn",brow=2,eyes=2,mouth=1)
        adjustChar("Taro",eye=3,mouth=2)

    voice taro_themystiquewearsoff
    Taro "Crois moi, une semaine et la magie disparais."

    $adjustChar("Robyn",mouth=0,brow=0)
    Robyn "Ca change la vie."

    python:
        adjustChar("Robyn",eyes=3)
        adjustChar("Taro",eye=2,mouth=1)

    Taro "Comment est-ce qie ca peut t'impressioner? Tu parle a des fantômes! T'es pote avec le mothman!"
    $Robyn_State["eyes"] = 2

    Robyn "UN., mothman."

    python:
        adjustChar("Robyn",armR=1)
        adjustChar("Taro",mouth=3,eye=5)
    Narrator "Tu continue de marcher, jettant de petits coups d'oeuils à la carte sur ton portable. Seulement deux patés avant d'arriver à la clinique."

    python:
        Robyn_State["msg"] = 1
        Taro_State["eye"] = 0

    voice mm_boopc
    Narrator "Ton téléphone {color=#3bec27}vibre{/color} dans ta poche, un méssage apparais sur ton écran."

    $Robyn_State["eyes"] = 2
    Narrator "C'est un SMS de Jamie."

    Jamie "{i}Salut [PCname], J'éspère que tout vas bien. Merci pour la super, mais chaotique soirée. J'ai presque pas dormi! Je trouve Taro plûtot collante,, mais ton ami est aussi le mien—{/i}"

    # show robyn:
    #     matrixtransform RotateMatrix(0,0,0)
    #     ease 0.3 matrixtransform RotateMatrix(0,180,0)
    #
    # $adjustChar("Robyn",eyes=1,mouth=1)
    # Narrator "You're starting to zone out while reading."

    python:
        adjustChar("Robyn",eyes=1,mouth=1)
        adjustChar("Taro",eye=2,mouth=4)
        adjustChar("OH",armL=-1,armR=-1)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)

    show oswald:
        xcenter 0
        matrixtransform RotateMatrix(0,180,0)
        ease 2 xcenter 0.25

    camera:
        camera_zoom(z=-300,y=50,x=-20,t=2)

    Jamie "{i}—Peut être qu'on devrais sortir un de ses quatres? Je connais quelqu'un qui pourra peut-être réparer ta voiture. Je t'en doit une après tout.{/i}"

    $Robyn_State["msg"] = 0
    $Taro_State["mouth"] = 0


    Narrator "Tu commence à répondre—"
    python:
        adjustChar("Robyn",eyes=3,brow=1)
        adjustChar("Taro",mouth=2)

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.4 matrixtransform RotateMatrix(0,180,0)
        ease 0.4 xcenter 0.3
        parallel:
            matrixtransform RotateMatrix(0,180,10)
            ease 0.2 xcenter 0.45
        parallel:
            ease 0.075 yoffset -30
            ease 0.075 yoffset 0
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    show oswald:
        xcenter 0.25

    play sfx ["<silence .8>", "audio/SFX Battle/Hurt_A.ogg"]
    Narrator "Et bonk., tu bourre dans un large cryptide gris qui porte plusieurs sac de course sur chaque bras,, un peu comme un super héros."
    camera:
        camera_zoom(z=-300,y=-100,x=-20,t=0.5)

    python:
        adjustChar("Robyn",eyes=0,brow=2,mouth=7)
        adjustChar("OH",eyeFrame=1,brow=0,eyes=5)

    Robyn "Pardon!"
    python:
        adjustChar("Robyn",armR=0,eyes=2,mouth=6)
        OH_State["brow"] = 0

    camera:
        camera_zoom(z=-150,t=2.0)

    Robyn "H-heeey mais c'est toi! Oz,, c'est ça?"
    python:
        OH_State["eyes"] = 0
        adjustChar("Taro",eye=1,mouth=4)
        adjustChar("Robyn",eyes=4,mouth=5)

    show oswald behind taro:
        matrixtransform RotateMatrix(0,180,0) yoffset 0

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        ease 0.4 xcenter 0.6

    show taro:
        ease 0.4 xcenter 0.45
        idleFloat(2,10)


    Taro "J'ai des vibes de canibal en regardant ce masque."
    voice taro_laughc
    python:
        adjustChar("Taro",eye=2,mouth=2)
        adjustChar("Robyn",eyes=2,mouth=5,brow=0)
    Taro "{bt=4}Biting problems?{/bt}"
    $adjustChar("Robyn",eyes=1,mouth=4,brow=2)

    Robyn "Ne dit pas des trucs comme ça!"

    python:
        adjustChar("OH",brow=1,eyeFrame=2,eyes=5)
        adjustChar("Robyn",mouth=5,brow=0)
    voice oz_ugh
    Oz "{sc=4}...{/sc}"

    Narrator "Oz se penche en avant pour caresser le chat,, mais ses mains sont pleines."

    show CGShade:
        on hide:
            ease 0.5 alpha 0

    show CG Taro Pet:
        zoom 0.95
        xcenter 0.5
        yoffset 700
        ease 0.5 yoffset 50

        on hide:
            yoffset 0
            ease 0.5 yoffset 700

    show oswald:
        xcenter 0.25
        ease 0.4 xcenter 0.3

    Narrator "Determiné, Oz change l'organisation des sacs dans ses mains, finissant par en libérer une. Il pose l'un des sac plastique par terre et gratouille le visage touffu de Taro."
    voice taro_hiss
    Narrator "Taro recule est crache, les poils irrisés."
    python:
        adjustChar("OH",eyeFrame=1,brow=0)
        adjustChar("Robyn",brow=2,mouth=1)
        adjustChar("Taro",eye=1,mouth=4)

    hide CG Taro Pet with None
    hide CGShade with nwDissolve(0.5)
    Robyn "Taro,, calmos! Elle um,, ne griffe pas normallement."
    voice taro_meowa
    python:
        Taro_State["pawL"] = 1
        OH_State["eyes"] = 1
        adjustChar("Robyn",eyes=2,mouth=5,brow=0)

    Taro "C'est une exception."

    $adjustChar("OH",eyeFrame=0,brow=3)
    Narrator "Ramassant ses courses, Oz frotte son front et change d'éxpression faciale, en essayant de former un sourire, mais il a l'air... triste."
    python:
        adjustChar("Robyn",eyes=2,mouth=6,brow=2)
        OH_State["eyes"] = 5

    Robyn "Ouaaais-"

    $adjustChar("Robyn",eyes=4,mouth=0)

    Narrator "Tu sais pas vraiment quoi dire."
    python:
        adjustChar("OH",eyeFrame=0,eyes=1,brow=0)
        adjustChar("Robyn",brow=1,eyes=2,mouth=4)

    Robyn "Ah merde,, en parlant de courses je dois acheter à manger moi aussi."

    python:
        OH_State["eyes"] = 0
        adjustChar("Robyn",brow=0,mouth=0,eyes=4)

    voice oz_hmshort
    Oz "..?"

    $Robyn_State["eyes"] = 3
    voice RobynSays("Chapter 1","CoffeePBCereal")

    Robyn "Je tourne sur du café, beurre de cacahouète et des cereales depuis une semaine{nw}"

    python:
        Robyn_State["eyes"] = 0
        OH_State["eyes"] = 0

    camera:
        shaded("#dbeaff")
        camera_zoom(z=-520,x=-300,y=-150,t=2.0)

    extend "\n\nEt je dois faire réparer ma voiture aussi! Comment je suis censé payer ça??"

    voice RobynSays("Chapter 1","JamieKnowsAGuy")

    Robyn "Jamie dit qu'iel connait quelqu'un, mais..."

    $OH_State["brow"] = 2
    Narrator "Oz hausse les épaules."

    $adjustChar("OH",eyes=0,brow=1)
    voice RobynSays("Chapter 1","DeadEnds")

    Robyn "Je sais qu'il veut aider mais,, Atlas ne fait que de finir dans des impasses. C'est juste que... il prend pas vraiment tout ça au serieux."

    $adjustChar("OH",eyes=5,brow=0,eyeFrame=1)
    Taro "Il a touché un loup-garou avec un bâton!"
    voice oz_huh
    $OH_State["eyes"] = 0
    Oz "{sc=5}-!{/sc}"

    voice RobynSays("Chapter 1","YouThinkAugustRemembers")
    Robyn "Tu crois qu'August se souvient de ce qu'il s'est passé hier?"

    voice taro_uhuhb
    $adjustChar("OH",eyeFrame=0,brow=0)

    Taro "J'éspère que non!"
    voice oz_happy
    $OH_State["brow"] = 2
    Oz "{sc=4}...{/sc}"

    $OH_State["brow"] = 0
    voice RobynSays("Chapter 1","ALotOnTheBrain")
    Robyn "Um,, merci d'avoir écouté au moins. J'ai beaucoup dans la tête en ce moment."

    $OH_State["eyes"] = 5
    voice RobynSays("Chapter 1","WhatCryptidAreYou")
    Robyn "J'ai jamais vu un cryptide comme ça avant. J'veux dire, les mothman et fantômes c'est plûtot évident,, mais t'es quoi en fait?"
    show oswald:
        matrixtransform RotateMatrix(0,180,0) yoffset 0
        ease 0.4 matrixtransform RotateMatrix(0,0,0)
    Taro "Comment il est censé répondre?"

    $OH_State["eyes"] = 4
    #Robyn "Gah, sorry your hands are full and I'm holding you up!"

    show oswald:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 1.0 xoffset -4
        ease 1.1 xoffset 5
        ease 1.1 xoffset -5
        ease 0.5 xoffset 5
        ease 0.8 xoffset 0

    $adjustChar("OH",eyes=5,brow=1)
    Narrator "Oz s'écarte de la route et se met sur un petit tas de terre dans l'herbe a coté, avant de se mettre a tracer avec la pointe de son pied dans la terre. \n\nCa te prend un moment avant de réaliser qu'il essaie d'écrire un truc."

    Narrator "H-O-W.,-L-E-R."

    Narrator "Tu réfléchis un instant."

    $OH_State["eyes"] = 0
    Robyn "C'est genre... \n\n{size=40}un vampire?{/size}"

    $adjustChar("OH",brow=0,eyeFrame=1)

    voice taro_zombiewerewolf
    Taro "Excuse le débile. \n\n{i}Evidement,{/i} t'es un zombi loup-garou."

    $adjustChar("OH",eyes=4,eyeFrame=0,brow=5)
    Robyn "Mais c'est pas logique!"

    show oswald:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.4 matrixtransform RotateMatrix(0,180,10)

    python:
        adjustChar("OH",brow=4,eyes=5)
        adjustChar("Robyn",eyes=2,mouth=1,brow=0)

    voice oz_bleuhgh
    Narrator "Oz laisse passer un souffle surpris amusé."
    camera:
        camera_zoom(t=1.6)
        camera_default
        shaded("#dbeaff")

    show oswald behind robyn:
        matrixtransform RotateMatrix(0,180,10)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        ease 3.0 xcenter 1.5

    show taro:
        pause 0.2
        matrixtransform RotateMatrix(0,180,0)
        ease 0.4 matrixtransform RotateMatrix(0,0,0)
        idleFloat(2,10)

    $adjustChar("OH",eyes=5,brow=0)
    Narrator "Et se met a marcher dans la direction opposée."

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        pause 0.5
        ease 0.4 matrixtransform RotateMatrix(0,0,0)

    $adjustChar("Robyn",mouth=1,eyes=0,brow=1)
    Robyn "Il a l'air sympa."

    hide oswald
    jump Ch1_PotionShopVisit
