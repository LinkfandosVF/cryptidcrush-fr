label Ch1_RobbieIntro:
    hide screen quicker_menu
    python:
        #musicPlayer.playSong(song="Midnight_Mallwave_Song",fadeIn=1.0)

        adjustChar("Robbie",armR=0,eye=2)
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "6A", who_color = "ea3c53")
        timeText = "3:30PM"
        songText = "(REDACTED)"
        quick_menu = False
        quicker_menu_show = False

    play music midnight_mallwave_song fadein 2.0 fadeout 1.0
    play ambiance river_calm fadein 2.0
    scene BG Black with Dissolve(0.5)
    window hide

    scene BG Bridge
    camera:
        camera_default
        camera_zoom(z=-220,y=80,x=150)
        matrixcolor TintMatrix("#ffffff")
        camera_zoom(z=-270,y=-80,x=-150,t=4.0)

    with Dissolve(0.5)

    pause 3.0
    scene BG Sky Day

    camera:
        camera_zoom(z=-450,y=-120,x=150)
        camera_zoom(z=-450,y=-60,x=150,t=2.0)

    show robbie:
        shaded("#FCE2D5")
        xcenter 0.5

    show robyn:
        xcenter -0.5
        shaded("#FCE2D5")
        matrixtransform rotated()
        ease 2.0 xcenter 0.2

    with Dissolve(0.5)
    $quick_menu = True
    $adjustChar("Robbie",eye=2,mouth=0)

    Someone "..."

    $adjustChar("Robbie",eye=1)
    Robyn "Je suis au pont, ouais! Je me suis arrêté à la clinique en passant. Heu, Je crois qu'il est rentré. \n\n'Ké, Je te vois là bas!"

    Narrator "Le cryptide fortement habillé t'attire l'attention, il à l'air complètement perdu dans ses pensées, observant la surface de l'eau. Sentant un coup d'inquètude, tu traverses rapidement la rue et l'interpelle."

    camera:
        camera_zoom(z=-350,y=-20,x=-175,t=2.0)

    python:
        adjustChar("Robyn",eyes=2,brow=2,mouth=4,armR=0)

    Robyn "Ça va?"

    python:
        adjustChar("Robyn",mouth=5)
        Robbie_State["eye"] = 0

    Narrator "L'étranger fouille dans sa poche et ramasse un gallet de granite. Enroulé autour de la pierre est un fil fait de trèfles."
    python:
        adjustChar("Robyn",brow=0,mouth=1)
        Robbie_State["mouth"] = 2

    voice robbie_tossingrocks

    Someone "J'balance des pierres."

    Narrator "Il la soulève et la lance par dessus le pont, la regardant tomber dans l'eau en s'écrasant au fond du lac."

    python:
        adjustChar("Robbie",eye=1,mouth=5)
        adjustChar("Robyn",brow=0,mouth=5)
    voice robbie_youwannatry

    Someone "Tu veux essayer?"

    show CGShade
    show Rock

    Narrator "Le cryptide t'offres une roche couverte de mousse enroulée dans des liasses de petites fleurs jaunes."

    python:
        adjustChar("Robbie",eye=1,mouth=0)
        adjustChar("Robyn",brow=2,mouth=4)

    Robyn "Et pourquoi., exactement?"

    hide Rock
    hide CGShade

    Narrator "Il lance une autre pierre, une enroulée dans des feuilles d'érables."

    python:
        adjustChar("Robbie",eye=0,mouth=3)
        adjustChar("Robyn",brow=1,mouth=5,eyes=0)

    show robbie:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        xcenter 0.45 yoffset 0
        camera_shake

    voice robbie_goddess
    Someone "{size=25Il y a une {b}{color=#57fcd0}déesse{/color}{/b} qui dors dans la bouche de la rivière.{/size}"

    show robbie:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        xoffset 0
        ease 0.5  matrixtransform RotateMatrix(0, 180, -10) xcenter 0.4

    show robyn:
        xcenter 0.2
        matrixtransform RotateMatrix(0,0,0)
        pause 0.3
        ease 0.3 xcenter 0.18

    python:
        adjustChar("Robbie",eye=1,mouth=0)
        adjustChar("Robyn",brow=0,eyes=4,mouth=3)

    voice robbie_igotquestions
    Someone "Donc j'éssaie de la réveiller. \n\nJ'ai masse de questions à lui poser."

    $adjustChar("Robyn",brow=2,eyes=1,mouth=1)
    Narrator "Weirdo."

    $adjustChar("Robyn",mouth=4,eyes=2)
    Robyn "Comment tu sais qu'elle est là dessous?"

    python:
        adjustChar("Robbie",eye=0,mouth=2)
        adjustChar("Robyn",brow=0,mouth=1,eyes=3)
    voice robbie_shetoreachunk
    Someone "Elle à essayé d'arracher un morceau de mon pied sur la baie."

    voice robbie_froglegs
    show robbie:
        matrixtransform RotateMatrix(0.0, 180.0, -7.0)
        ease 0.5  matrixtransform RotateMatrix(0, 180, 15)

    python:
        adjustChar("Robbie",eye=3,mouth=1)
        adjustChar("Robyn",brow=1,mouth=1,eyes=0)

    Someone "Excusez moi madame, mais les cuisses de grenouilles ne sont pas sur le menu!"

    python:
        adjustChar("Robbie",eye=1,mouth=0)
        adjustChar("Robyn",brow=0,mouth=5,eyes=2)

    #Someone "This town's seriously backwards."
    #$adjustChar("Robyn",brow=1,eyes=0)
    Narrator "Eeeeeetttt tu pensais que c'était une blague."

    python:
        adjustChar("Robyn",brow=2,eyes=3,mouth=0)
        adjustChar("Robbie",eye=2,mouth=3)

    voice robbie_stillgettingused
    Someone "Excuse moi ,, J'éssaie toujours de m'habituer à la vie par ici...,{nw}"

    python:
        adjustChar("Robyn",brow=0,eyes=2,mouth=0)
        adjustChar("Robbie",eye=0,mouth=3)

    extend "\n\nHeu, jm'appelle {b}Robbie{/b}...{nw}"

    $adjustChar("Robbie",eye=7,mouth=0)
    extend "T-tu,, tu peux garder la pierre, au fait..."

    $adjustChar("Robyn",brow=0,eyes=2,mouth=4)
    Robyn "Ah, t'es nouveau?"

    python:
        adjustChar("Robyn",brow=1,mouth=5)
        adjustChar("Robbie",eye=0,mouth=0)

    show robbie:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        ease 0.5  matrixtransform RotateMatrix(0, 180, 0)

    Robert "Très."

    show robbie:
        ease 1.0 yoffset 30

    python:
        Robyn_State["brow"] = 0
        adjustChar("Robbie",eye=1,mouth=3)

    Robert "Je me suis échoué sur la plage comme un vieux morceau de bois."

    python:
        adjustChar("Robyn",mouth=0,eyes=3,brow=0)
        Robbie_State["eye"] = 2

    Robyn "Wow. Vraiment une entrée de conte de fée. Peut-être que le destin t'a ammené içi?"

    python:
        adjustChar("Robyn",mouth=5,eyes=0)
        adjustChar("Robbie",eye=0,mouth=4)

    show robbie at jumpSquish(0.15,150,0.2)

    voice robbie_ribbita
    Robert "{size=60}{b}CROAK!{/b}{/size}.,.,{nw}"

    $adjustChar("Robbie",eye=4,mouth=3)

    show robbie:
        xzoom 1.0
        yzoom 1.0
        matrixtransform RotateMatrix(0,180,0)
        parallel:
            ease 0.6 xcenter 0.6
            ease 0.3 xcenter 0.65
        parallel:
            ease 0.7 yoffset 100
            ease 0.2 yoffset 0
        parallel:
            ease 0.6 xcenter 0.6 matrixtransform RotateMatrix(0,180,-25)
            ease 0.3 matrixtransform RotateMatrix(0,180,5)
            ease 0.15 matrixtransform RotateMatrix(0,180,0)

    Robert "{sc=4}Urk!{/sc}{nw}"

    python:
        adjustChar("Robyn",mouth=5,eyes=0,brow=0)
        adjustChar("Robbie",eye=3,mouth=0)

    extend "\n\n\Ke-HCK."

    show robbie:
        matrixtransform RotateMatrix(0,180,0)
        yoffset 0
        ease 0.75 xcenter 0.6


    python:
        adjustChar("Robyn",mouth=5,eyes=2,brow=1)
        adjustChar("Robbie",mouth=3,eye=5)

    Robert "Je suppose que ça ferait de moi un prince grenouille."


    python:
        adjustChar("Robyn",mouth=0,eyes=3,brow=2)
        adjustChar("Robbie",eye=2,mouth=0)

    Robyn "Je pensais que tu était un poisson."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=0)
        adjustChar("Robbie",mouth=2,eye=1)

    Robert "Un monstre dans tout les cas."

    $adjustChar("Robbie",mouth=0)
    Narrator "T'es obligé de demander—{nw}"

    menu:
        extend ""

        "Tu viens d'où?":
            show robbie:
                ease 1.5 xcenter 0.45

            python:
                adjustChar("Robyn",mouth=0)
                adjustChar("Robbie",mouth=1,eye=2)

            Robert "Cape Ann."
            python:
                adjustChar("Robyn",brow=1,eyes=0)
                adjustChar("Robbie",mouth=2,eye=0)

            extend "\n\nQui est à probablemennt des gazillions de killo-mètres d'içi."
            python:
                adjustChar("Robyn",mouth=5,brow=2,eyes=2)
                adjustChar("Robbie",mouth=3,eye=3)

            Robert "Donc, d'une manière ou d'une autre, je ne devrais pas être içi."
            python:
                adjustChar("Robyn",mouth=0,eyes=1)
                adjustChar("Robbie",mouth=2,eye=1)

            Robyn "A moins que—{nw}"
            python:
                adjustChar("Robyn",eyes=4,mouth=4,brow=1)
                adjustChar("Robbie",eye=1)

            extend "\n\nT'es une projection astrale?"
            python:
                adjustChar("Robbie",eye=7,mouth=3)
                adjustChar("Robyn",eyes=2,mouth=5,brow=0)

            voice robbie_eh
            show robbie:
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                xcenter 0.45
                ease 0.5  matrixtransform RotateMatrix(0, 180, 15.0)

            Robert "Bleugh, me parle pas de ce genre de truc."

        "A quoi ressemble cette {b}déesse{/b}?":
            python:
                adjustChar("Robbie",eye=3,mouth=6)
                adjustChar("Robyn",brow=1,eyes=0,mouth=1)

            show robbie at jumpSquish(0.15,150,0.25)

            Robert "{b}COMME MOI!{/b}"

            show robbie:
                xzoom 1
                yzoom 1
                yoffset 0
                ease 1.5 xcenter 0.55
                pause 0.3
                ease 1.5 xcenter 0.45

            $adjustChar("Robbie",eye=4,mouth=0)
            Robert "Vert,, long et fin,, horriblement territorial."
            $adjustChar("Robbie",eye=8,mouth=5)

            show robbie:
                xcenter 0.45
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.5  matrixtransform RotateMatrix(0, 180, 15.0)

            extend "\n\nComme un petit morceau de chez moi..."

    $adjustChar("Robyn",brow=0,eyes=2,mouth=0)
    Robyn "Tu va faire quoi maintenant du coup?"


    show robbie:
        matrixtransform RotateMatrix(0.0, 180.0, 15.0)
        ease 0.5  matrixtransform RotateMatrix(0, 180, 0.0)

    $adjustChar("Robbie",eye=2,mouth=2)
    Robert "Me balader en ville, trouver un p'tit étang et hiberner j'usqu'au primptemps."
    python:
        adjustChar("Robbie",eye=0,mouth=7)
        adjustChar("Robyn",mouth=4,brow=1)

    Robyn "Les cryptides hibernent?"
    python:
        adjustChar("Robbie",eye=8,mouth=5)
        adjustChar("Robyn",mouth=1,brow=0)

    voice robbie_laughb

    Narrator "Robbie éclate de rire."

    show robbie:
        ease 0.15 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, -10.0)

    $adjustChar("Robbie",eye=3)

    Robert "{b}Cryptids?!{/b} \n\nC'est comme ça qu'ils nous appellent? Comme une espèce d'alien?"
    python:
        adjustChar("Robbie",mouth=2,eye=0)
        adjustChar("Robyn",mouth=0,brow=2,eyes=4)

    Robyn "J'utilise juste le terme du coin."
    python:
        adjustChar("Robbie",eye=2)
        adjustChar("Robyn",mouth=0,eyes=2)

    show robbie:
        ease 0.15 yoffset 0 matrixtransform RotateMatrix(0.0, 180.0, -10.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 5.0)

    Robert "C'est hillarant!"
    $adjustChar("Robbie",eye=1)

    extend "\n\nC'est pas DU TOUT comme ça qu'ils nous appellent à la maison."
    $adjustChar("Robyn",mouth=4)

    Robyn "Qui est?"
    python:
        adjustChar("Robbie",eye=3,mouth=6)
        adjustChar("Robyn",mouth=5,eyes=0,brow=1,)

    show robbie at hoppies_flipped(xIntensity=2.5)

    Robert "{sc=2}BEUUURK, DEGAGE DE LA ESPECE DE {b}MONSTRE{/b}!{/sc}"

    show robbie:
        ease 0.15 yoffset 0 matrixtransform rotated(y=180)

    python:
        adjustChar("Robbie",eye=2,mouth=3)
        adjustChar("Robyn",mouth=1,eyes=1,brow=2,)

    Robyn "C'est térrible!"

    $adjustChar("Robbie",eye=1,mouth=2)
    Robert "Psh, ça m'embète pas."
    python:
        adjustChar("Robbie",eye=7,mouth=3)
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)

    voice robbie_laugha
    Robert "Où c'est ce que {i}j'aurais{/i} dit si ça ne m'emmerdais pas {i}vraiment beaucoup{/i}."

    $adjustChar("Robyn",eyes=3,mouth=0)
    Robyn "Moi je trouve que t'es plutôt cool comme prince grenouille."

    $adjustChar("Robbie",eye=0,mouth=2)

    voice robbie_flushed
    Robert "{sc=3}Wow,, t-tu trouve?{/sc}"

    python:
        adjustChar("Robbie",eye=2,mouth=0)
        adjustChar("Robyn",mouth=4,eyes=2,brow=1)

    Robyn "T'a un endroit pour dormir?"
    python:
        adjustChar("Robbie",eye=0)
        adjustChar("Robyn",mouth=5,eyes=2,brow=0)

    Robert "Je squatte un genre de serre que j'ai trouvé.{nw}"

    python:
        adjustChar("Robbie",eye=1,mouth=3)
    extend "\n\nL'humidité aide un peu."


    scene BG Black
    camera at camera_default:
        camera_zoom()

    with quickDissolve

    Narrator "Vous regardez tout les deux la surface de la rivière, éspèrant qu'un dragon sorte des vagues,, mais rien ne se passe. Avec un mouvement de la tête, Robbie se bouge un peu."

    jump Ch1_AtlasMeetup

label Ch1_AtlasMeetup:

    $timeText = "4:00PM"

    scene BG Empty Street Day
    camera at camera_default:
        camera_zoom(z=-200,x=100,y=50)
        matrixcolor TintMatrix("#ffe7ee")

    show robyn:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.7

    show taro:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 3 xcenter 0.8
        idleFloat(2,10)

    show atlas:
        xcenter 2
        ease 3 xcenter 0.5
        flipChar(0.5)

    with Dissolve(0.5)
    play music loosen_up_longhope_song fadeout 5.0
    $musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)

    voice atlas_greet

    $adjustChar("Atlas",eye=6)
    Atlas "Attends!"

    voice RobynSays("Chapter 1","WonderingWhenYoudShow")
    python:
        adjustChar("Robyn",mouth=6,eyes=3)
        adjustChar("Atlas",eye=1,armL=0,armR=0)

    Robyn "Je me demandais quand tu allais arriver, quoi de neuf?"

    python:
        adjustChar("Robyn",mouth=0,armL=0)
        Atlas_State["eye"] = 4

    show atlas at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.5
    voice atlas_newtypeofpossession

    Atlas "Je crois qu'on a découvert un nouveau type de {sc=1}possession!{/sc}"

    voice RobynSays("Chapter 1","OhYeah")
    python:
        adjustChar("Robyn",eyes=0,mouth=4)
        Atlas_State["eye"] = 6

    Robyn "Ah ouais?"

    voice atlas_illcallitpp

    python:
        adjustChar("Atlas",eye=1,eyeFrame=5,feelers=1)
        adjustChar("Robyn",brow=2,eyes=4,mouth=5)

    Atlas "Je vais l'appeller...{nw}"
    $adjustChar("Atlas",eye=0,eyeFrame=5,feelers=1,armR=2,armL=1)
    extend "\n\n{size=30}{color=#3bec27}l'empoisonement paranormal.{/color}{/size}"

    voice atlas_completewithalliteration
    python:
        adjustChar("Atlas",eyeFrame=0,sparkle=1,eye=6,feelers=0)
        adjustChar("Robyn",brow=0,eyes=2)

    Atlas "Complèté par alliteration!"

    show atlas:
        parallel:
            hoppies_flipped(xIntensity=4)
        parallel:
            startledSquish

    voice atlas_coolright
    python:
        adjustChar("Atlas",sparkle=0,eye=1,armR=0,armL=0)
        adjustChar("Robyn",eyes=2,mouth=3)

    Atlas "Cool pas vrai?"

    show atlas:
        ease 0.5 yoffset 0 matrixtransform rotated(y=180) yzoom 1 xzoom 1 xoffset 0

    python:
        adjustChar("Robyn",eyes=4,mouth=4,brow=1)
        Atlas_State["sparkle"] = 0

    voice RobynSays("Chapter 1","NameAlone")

    Robyn "Par son nom j'en conclus qu'il sagit d'une sorte de saignéee supernaturelle qui touche l'éssence vitale de quelqu'un d'autre?"

    python:
        adjustChar("Atlas",eye=6,armL=2)
        Robyn_State["mouth"] = 5

    Atlas "Bingo! T'es plutôt doué."

    $adjustChar("Robyn",mouth=3,eyes=1,brow=2)
    Robyn "Je viens de l'inventer.?"
    python:
        adjustChar("Robyn",mouth=0,eyes=3,brow=0)
        adjustChar("Atlas",feelers=1,eye=21,armL=0)

    Atlas "Roh. \n\nGaaaah, te moque pas de moi!"

    python:
        adjustChar("Atlas",eye=18,feelers=0)
        Robyn_State["eyes"] = 4

    Robyn "Okay okay, continue. Je t'écoute."

    python:
        Atlas_State["eye"] = 16
        Robyn_State["eyes"] = 2

    Atlas "Donc en gros, l'empoisonement paranormal c'est pas une possession complète, mais plûtot un genre d'affluence. \n\nCommme garder une poupée hantée sur le coté de ton lit."

    $adjustChar("Robyn",eyes=1,mouth=4,brow=0)
    Robyn "Ou boire une canette de soda hantée."

    show atlas at startledSquish
    $Atlas_State["eye"] = 1
    Atlas "T'a tout compris!"

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=2)
        Atlas_State["eye"] = 6

    Robyn "Comment t'a trouvé tout ça?"

    $adjustChar("Atlas",eye=14,feelers=3)

    show atlas:
        matrixtransform RotateMatrix(0,180,0)
        pause 0.3
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.2
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        pause 0.05
        ease 0.3 matrixtransform RotateMatrix(0,180,0)
        pause 0.1
        ease 0.3 matrixtransform RotateMatrix(0,0,0)
        pause 0.1
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    Narrator "..."
    python:
        adjustChar("Atlas",eye=16,feelers=0)
        adjustChar("Robyn",eyes=4,brow=0)

    Atlas "Taro, je peut parler à ton pote en privé?"

    $adjustChar("Taro",eye=2,mouth=2,pawR=0,pawL=1)
    Taro "Quoi, vous voulez un petit temps salon {bt=3}tout seul?{/bt}"

    python:
        adjustChar("Atlas",eye=21,feelers=3)
        adjustChar("Robyn",eyes=0,mouth=1,brow=3)

    show robyn:
        xcenter 0.7
        ease .5 xcenter 0.6
        matrixtransform RotateMatrix(0,180,0)
        ease 0.3 matrixtransform RotateMatrix(0,0,0)

    Atlas ""
    python:
        adjustChar("Atlas",blush=0,eye=13,feelers=1,eyeFrame=5)
        adjustChar("Robyn",eyes=1,brow=0)
        adjustChar("Taro",mouth=4,eye=5)

    Taro "{i}Myehehe,{/i} Je déconne! Allez faire vos trucs."
    python:
        Taro_State["eye"] = 1
        Atlas_State["eye"] = 1

    show taro:
        ease 5.0 yoffset 700

    Taro "Je serais à la maison, humain."
    python:
        adjustChar("Atlas",eye=0,eyeFrame=0)
        Robyn_State["mouth"] = 4

    show atlas:
        pause 0.3
        ease 0.4 xcenter 0.55

    show robyn:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.8 xcenter 0.8
        ease 0.4 matrixtransform RotateMatrix(0,180,0)


    Robyn "Oh! Eeeeeettt elle est partie. \n\nTu voulais me dire quoi?"

    hide taro
    python:
        Atlas_State["eye"] = 5
        adjustChar("Robyn",mouth=0,eyes=3)

    Atlas "Eh bien."

    $Atlas_State["eye"] = 3
    Atlas "Quand je ferme mes yeux, y'a ça qui se passe."
    $adjustChar("Atlas",eye=16,feelers=2)

    show atlas:
        ease 3.0 yoffset 45

    Narrator "..."

    python:
        musicPlayer.playSong(song="urgently_jammin_song")
        adjustChar("Atlas",eye=10,feelers=0)
        adjustChar("Robyn",eyes=0,mouth=1,brow=1)

    show atlas:
        blur 0
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    camera at camera_default:
        matrixcolor TintMatrix("#c0fac8")

    Narrator "Atlas fermes ses yeux et quand ils les réouvres, ils sont d'une brilliant lueur verte."

    $adjustChar("Atlas",feelers=1,eye=15)
    P_Atlas "J'suis sur que ça partira, mais j'ai gardé un oeuil dessus."

    python:
        adjustChar("Robyn",eyes=0,mouth=4,brow=3)
        adjustChar("Atlas",eye=10,feelers=3)

    show robyn:
        matrixtransform RotateMatrix(0,180,-6)
        xcenter 0.68

    show atlas:
        matrixtransform RotateMatrix(0,180,-6)
        ease 0.1 yoffset -35
        ease 0.1 yoffset 0

    camera at camera_shake:
        camera_zoom(z=-350,x=150,y=25)

    voice RobynSays("Chapter 1","YoureStillPossessed")

    Robyn "{size=30}T'es toujours possèdé?!{/size}\n\nAtlas, comment est-ce que tu {b}FONCTIONNE?{/b}"

    python:
        Robyn_State["mouth"] = 1
        adjustChar("Atlas",eye=11,feelers=0)

    show atlas:
        camera_shake

    voice atlas_gigglea
    P_Atlas "{bt=3}{color=#3bec27}La volonté, baby!{/color}{/bt}"

    $adjustChar("Robyn",eyes=1,mouth=4)
    Robyn "Je t'emmène chez le médecin immédiatement. J'appelle le contrôle du poison."
    python:
        adjustChar("Atlas",eye=10,feelers=2)
        adjustChar("Robyn",mouth=1,brow=2)

    show atlas:
        camera_shake

    P_Atlas "{sc=3}Nooooon!{/sc} Chillax! \n\nNe passons pas sur cette glorieuse {color=#3bec27}opportunité!{/color}"

    python:
        adjustChar("Atlas",eye=11,feelers=0)
        Robyn_State["eyes"] = 0

    show atlas at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show robyn:
        ease 0.5 xcenter 0.7 matrixtransform rotated(y=180)

    P_Atlas "J'dois te montrer ce que je peux faire avec {color=#3bec27}ça{/color} d'abord!"
    python:
        adjustChar("Atlas",eye=5,feelers=3)
        adjustChar("Robyn",eyes=1,mouth=4,brow=3)

    Robyn "D'accords,, mais honnêtement ça me fait chier."

    $adjustChar("Atlas",eye=9,feelers=1)

    show atlas at startledSquish:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    camera at camera_default:
        parallel:
            camera_zoom(z=-200,x=150,t=0.75)
        parallel:
            ease 0.5 matrixcolor TintMatrix("#ffe7ee")

    voice atlas_booyah
    Atlas "{sc=2}I knew you'd understand!{/sc}"

    show atlas:
        ease 3.0 yoffset 45

    play music loosen_up_longhope_song fadeout 1.0
    python:
        musicPlayer.playSong(song="loosen_up_longhope_loop",queueSong=True)
        adjustChar("Robyn",eyes=0,mouth=5)

    Robyn "I'm., gonna lose it."

    show robyn:
        xcenter 0.7
        matrixtransform rotated(y=180)

    show atlas:
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    python:
        adjustChar("Atlas",eye=3,feelers=0)
        adjustChar("Robyn",eyes=2,brow=0)

    Atlas "So, wanna join me and look around town?"

    if isSnooping:

        $adjustChar("Robyn",brow=1,mouth=3)
        Robyn "Look for what?"

        $Atlas_State["eye"] = 1
        Atlas "My buddy Lex! He owes me twenty bucks."

        $Atlas_State["eye"] = 5
        Narrator ""

        show atlas:
            matrixtransform RotateMatrix(0.0, 180.0, 7.0)

        $adjustChar("Atlas",eye=21,feelers=1)
        Atlas "I actually don't care about the money,, that part was a joke."

    else:
        show atlas:
            matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        $Atlas_State["eye"] = 1
        Robyn "You're still looking for a toothy spikey guy?"

        Atlas "With no eyes."

        Robyn "Aren't you just describing Madhouse?"
        show atlas:
            matrixtransform RotateMatrix(0,180,0)
            ease 0.5 matrixtransform RotateMatrix(0,0,0)

        $adjustChar("Atlas",eye=21,feelers=3)
        Atlas "{size=20}Nuh-uh.{/size}"

    show atlas:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.5 matrixtransform RotateMatrix(0,180,0)

    $adjustChar("Atlas",eye=16,feelers=1)
    Atlas "So, you wanna come with?"

    Robyn "Sure! It'd be good to catch up."
    voice atlas_letsgo
    Atlas "Great let's go!"

    jump Ch1_AtlasIntroExtended

label Ch1_AtlasIntroExtended:
    scene BG Avenue
    camera at camera_default:
        camera_zoom(z=-400,y=30,x=180)

    show robyn:
        matrixtransform RotateMatrix(0,180,0)
        xcenter 1.5
        pause 0.5
        ease 2.5 xcenter 0.6

    show atlas:
        xcenter 1.5
        ease 2.5 xcenter 0.75

    with pixellate

    python:
        musicPlayer.playSong(fadeOut=2,fadeIn=1,song="pleasant_conversation_song")
        timeText = "4:30PM"

    Robyn "How's the Atlas household?"

    $adjustChar("Atlas",eye=1,feelers=0)
    Atlas "We're doing good,, I'm in the middle of negotiating a family chore chart!"

    $Atlas_State["eye"] = 16
    Robyn "No no, I mean back {b}home.{/b}"

    call dice_roll(rMod=PC_Stats.cStats("charm"), rDiff=5, rDesc="Homesickness") from _call_dice_roll_8

    if isRollSuccess:
        $Atlas_State["eye"] = 19
        Robyn "With your dad."

        Atlas "Ah."

        $adjustChar("Atlas",eye=0,eyeFrame=3,feelers=1)
        Atlas "I just., needed to leave."

        Robyn "What happened? I thought your dad was cool."

        $adjustChar("Atlas",eye=5,eyeFrame=0,feelers=2)
        Atlas "I had a vision. \n\nLike a {i}bad{/i} one."

        Robyn "Did you tell Atticus about it?"

        $adjustChar("Atlas",eye=1,eyeFrame=3)
        Atlas "That's the thing—"

        $Atlas_State["eye"] = 0
        Atlas "I th{size=20}i{/size}{size=17}n{/size}{size=15}k—{/size}"

        $adjustChar("Atlas",eye=5,eyeFrame=0,feelers=2)
        Atlas "He w{size=20}a{/size}{size=17}s{/size}{size=15} th—{/size}"

        show atlas at startledSquish

        python:
            adjustChar("Atlas",eye=8,feelers=0)
            musicPlayer.playSong(fadeOut=1.0)

        Atlas "{size=35}I shouldn't dwell on it!{/size}"

        $Atlas_State["eye"] = 9
        Atlas "This {i}is{/i} the mothman we're talkin' about."

        Atlas "So what about you? How're you liking your new home?"
        menu:
            extend ""

            "What happened to your dad?":
                show robyn:
                    matrixtransform RotateMatrix(0,180,0)
                    ease 0.3 matrixtransform RotateMatrix(0,0,0)

                Robyn "What happened to your dad?"

                $adjustChar("Atlas",eye=3,feelers=2)
                Atlas "Huh? N-nothing {sc=3}{b}happened.{/b}{/sc}"

                $adjustChar("Atlas",eye=19,feelers=0)
                Atlas "It's a {i}vision.{/i} \n\nBesides,, this isn't something you should worry about. \n{size=20}{i}You're nosier than I am.{/i}{/size}"

                python:
                    adjustChar("Robyn",mouth=4,eyes=4,brow=2)
                    adjustChar("Atlas",feelers=1,eye=21,armL=0)

                Robyn "Atlas, if something's bothering you,, you can talk to me man."
                python:
                    adjustChar("Atlas",eye=17,feelers=0)
                    adjustChar("Robyn",eyes=2,brow=0,mouth=5)

                show atlas:
                    matrixtransform RotateMatrix(0,0,0)
                    ease 0.3 matrixtransform RotateMatrix(0,180,0)

                Atlas "Look,, it's better with me out of the picture."

                $adjustChar("Robyn",eyes=3,brow=2,mouth=4)
                Robyn "{sc=3}Atlaaaaas come on.{/sc}"

                show atlas:
                    matrixtransform RotateMatrix(0,180,0)
                    ease 0.3 matrixtransform RotateMatrix(0,0,0)

                python:
                    adjustChar("Atlas",eye=21,feelers=1)
                    adjustChar("Robyn",eyes=2,brow=2,mouth=3)

                #Atlas "I'm not gonna say anything with {sc=2}{color=#3bec27}that guy{/color}{/sc} around!"
                Atlas "I'm bad luck!"

                $adjustChar("Robyn",eyes=1,brow=0,mouth=1)
                #Robyn "Madhouse has zero reason to eavesdrop. He's probably catfishing chat bots or something."
                Robyn "No you're not."

                #show robyn:
                #    flipCharDelayed(0.8,0.5)

                python:
                    adjustChar("Atlas",eye=5,feelers=2)

                Atlas "Hmph."

            "It's been wild.":
                Robyn "It's been wild. I saw a bigfoot this morning!"

                Atlas "Wooooah!"

    else:
        Atlas "Last I heard they were carving out another lane to the highway."

        Atlas "And they dug up our favorite drain pipe."

        Robyn "Not devil's bendy straw!"

    pause 0.6

    python:
        musicPlayer.playSong(song="urgent_slower")
        Atlas_State["eye"] = 3
        adjustChar("Robyn",eyes=2,mouth=0)

    show atlas:
        linear 0.05 xcenter 0.75
        linear 0.05 xcenter 0.751
        linear 0.05 xcenter 0.75
        linear 0.05 xcenter 0.751
        pause 0.2
        repeat

    Narrator "{sc=3}Buzz- Buzz-{/sc}"

    $Atlas_State["eye"] = 6

    Atlas "{sc=2}Pardon me.{/sc}"

    show atlas:
        flipCharDelayed(0.8,0.5)

    python:
        adjustChar("Atlas",eyeFrame=0,sparkle=0,eye=2,phone=2,feelers=3)
        adjustChar("Robyn",brow=0,eyes=4,mouth=1)

    Narrator "Atlas turns away and plucks his phone out of his neck fluff."

    python:
        musicPlayer.playSong(song="undead_icebreakers_song",fadeOut=2,fadeIn=1)
        Atlas_State["eye"] = 16

    Atlas "Phew! It's just August."

    python:
        adjustChar("Robyn",brow=1,eyes=1,mouth=1)
        adjustChar("Atlas",feelers=0,eye=21)

    show atlas:
        blur 0
        matrixtransform RotateMatrix(0,180,-6)
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    August "{sc=3}{b}Atlas{/b}{/sc} where were you?"

    $Atlas_State["eye"] = 18

    show atlas:
        matrixtransform RotateMatrix(0,180,0)
        xcenter .75
        ease 3 xcenter 1.2

    voice atlas_isleptin
    Atlas "Jeez, could you talk any louder? \n\nI slept in."

    voice atlas_iwasgonnacall
    $adjustChar("Robyn",brow=0,eyes=1,mouth=5)
    Atlas "Yeah, yeah I was gonna call you!"

    voice atlas_changeofclothes

    $adjustChar("Robyn",brow=1,eyes=0,mouth=3)
    Atlas "Do you need a change of clothes?"

    voice atlas_homefordinner
    $adjustChar("Robyn",brow=0,eyes=1,mouth=5)
    Atlas ".,Alright,, I'll be home for dinner 'kay?"

    show atlas:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 1.2
        ease 2 xcenter .75

    Atlas "Sorry about that."

    show robyn:
        flipCharDelayed(0.8,0.5)

    show robyn fear
    $Atlas_State["phone"] = 0
    Robyn "Dude, I can't believe you're living with {i}him.{/i}"

    voice atlas_smug
    $adjustChar("Atlas",eye=6,sparkle=1,feelers=1,armR=1,armL=1)
    show robyn neutral
    Atlas "{bt=3}Jealous?{/bt}"

    $adjustChar("Atlas",eye=1,sparkle=0,feelers=3,armR=0,armL=0)
    show robyn sigh
    Robyn "A tiny bit."

    $adjustChar("Atlas",eyeFrame=5,eye=0,feelers=0,armL=2)
    Atlas "You and I are neighbors! \n\nThat's basically planet roommates."

    show robyn happy
    Robyn "This is true."

    $adjustChar("Atlas",eyeFrame=0,eye=19,feelers=3,armL=0)
    Atlas "Besides, I'd be a terrible roommate for you. I'm loud, I hardly sleep and I'm like {sc=2}super grouchy.{/sc}"

    show robyn neutral
    Robyn "But those are things I like about you."

    $adjustChar("Atlas",eye=21,feelers=1)
    show atlas at startledSquish
    Atlas "Yeah, cause you're not living with me!"

    show robyn smug
    Robyn "{bt=2}True!{/bt}"

    jump Ch1_AtlasMeetupLate

label Ch1_AtlasMeetupLate:
    scene BG SunsetRoadside
    camera at camera_default:
        camera_zoom()
        shaded("#ffffff")

    show oswald:
        shaded("#ffc6c1")
        xcenter 0.32

    show hazel behind oswald:
        shaded("#ffc6c1")
        matrixtransform RotateMatrix(0,180,0)
        xcenter 0.12

    python:
        adjustChar("Hazel",mouth=1,collar=0,eyes=3)
        adjustChar("OH",eyes=5,eyeFrame=0,armL=0,armR=2)

        musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1,fadeOut=2)
        timeText = "6:30PM"

    with pixellate
    voice hazel_yourelookingformybrother
    Hazel "Seriously,, you're looking for my dumbass brother not {i}me.{/i} \n\nI don't owe you squat."

    $adjustChar("OH",armL=0,armR=0,eyes=4,eyeFrame=0,brow=1)

    show oswald behind robyn:
        xcenter 0.32
        pause 0.5
        ease 2.5 xcenter 0.34


    Oz "..."
    voice hazel_sogetlost
    python:
        adjustChar("Hazel",mouth=2,eyes=0)
        adjustChar("OH",eyes=3,eyeFrame=1,brow=0)

    show hazel at startledSquish

    python:
        Oz_Stats = OzUnit()
        Hazel_Stats = Unit("{color=#ee6756}Hazel{/color}",2,-2,3,1,-1,0,14)

        playerUnitsInit("Oz")
        enemyUnitsInit("Hazel")

        InitializeCombatUI(playerUnits, enemyUnits)

        HighlightEnemyUnitBars([0])
        HighlightPlayerUnitBars([0])

    Hazel "So get lost before I kick your ass old man."

    python:
        Hazel_State["mouth"] = 0
        OH_State["armL"] = 6

    show Flickering Black
    pause 0.65
    play music elkhorn_radio_intro_song noloop
    pause (4.3)
    queue music dirt_nap_dreams
    voice atlas_heyhazel
    Atlas "{size=35}Hey Hazel!{/size}"

    hide Flickering Black

    python:
        Atlas_State['eye'] = 13
        Hazel_State["mouth"] = 0
        adjustChar("OH",eyes=1,eyeFrame=0,armL=6,armR=3,brow=1)
        adjustChar("Robyn",brow=0,eyes=2,mouth=5)
        HighlightEnemyUnitBars([])
        HighlightPlayerUnitBars([])

    show oswald:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)


    with nwDissolve(0.5)
    Hazel "Huh?{nw}"

    $adjustChar("OH",eyes=0,brow=1)

    show atlas:
        shaded("#ffc6c1")
        xcenter 1.5
        ease 2.0 xcenter 0.75

    show robyn behind atlas:
        shaded("#ffc6c1")
        matrixtransform RotateMatrix(0,180,0)
        xcenter 1.5
        pause 0.5
        ease 2.0 xcenter 0.6

    extend "\n\nWhat do you want?"

    python:
        adjustChar("Robyn",brow=2,eyes=3,mouth=0)
        adjustChar("Atlas",eyeFrame=5,feelers=3,eye=0)

    Robyn "Looks like we've come full circle huh Oz?"
    python:
        adjustChar("OH",eyes=4,eyeFrame=0,brow=0)
    voice oz_laughc
    Oz ""
    voice atlas_conspiringwiththeenemy
    show atlas:
        xcenter 0.75 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, -10.0)

    python:
        adjustChar("OH",eyes=5,eyeFrame=0,brow=1,armL=0,armR=0)
        adjustChar("Robyn",brow=1,eyes=4,mouth=1)
        adjustChar("Atlas",eyeFrame=5,feelers=1,eye=13)

    Atlas "You're conspiring with the enemy."
    python:
        adjustChar("Hazel",mouth=3,brow=1)
        adjustChar("Robyn",brow=0,eyes=1,mouth=5)
        adjustChar("Atlas",feelers=0,eye=0)

    Robyn "The what?"

    python:
        adjustChar("Hazel",mouth=4,brow=0,eyes=2)
        adjustChar("Atlas",feelers=0,eye=13)
        adjustChar("OH",eyes=1,eyeFrame=0,brow=4,armL=0,armR=0)

    show oswald behind hazel:
        ease 4 xcenter -1.5

    Hazel "{i}The{/i} enemy."

    camera:
        camera_zoom(z=-300,x=70,y=30,t=0.8)

    show hazel:
        ease 0.75 xcenter 0.4

    $adjustChar("Hazel",mouth=3,brow=1,eyes=0)

    Hazel "So what'dya want, Feathers?"

    python:
        adjustChar("Robyn",brow=0,eyes=2)
        adjustChar("Atlas",eyeFrame=0,eye=3,feelers=0)

    Atlas "You're gonna be late for dinner!"

    python:
        adjustChar("Robyn",brow=1,eyes=0,mouth=5)
        OH_State["eyes"] = 5
        Hazel_State["mouth"] = 0

    Hazel "I'm staying at a friend's place."
    hide oswald

    python:
        adjustChar("Robyn",brow=0,eyes=4)
        adjustChar("Atlas",eye=18,feelers=1)


    Atlas "Did you let August know?"

    $adjustChar("Hazel",eyes=3,mouth=4,brow=1)
    Hazel "Nah, he can shove it."

    python:
        adjustChar("Robyn",brow=1,eyes=2)
        adjustChar("Atlas",eye=5,feelers=3)

    Atlas "Aw jeez, what happened?"

    python:
        adjustChar("Hazel",mouth=6,eyes=0)
        Atlas_State['eye'] = 18

    Hazel "Gus was a total unapologetic crybaby at the hospital. Literally, freaked at me for being worried about his stupid ass."
    $adjustChar("Hazel",brow=0,eyes=2,mouth=2)
    Hazel "It's ticking me off."

    $adjustChar("Robyn",brow=2,eyes=2,mouth=4)
    Robyn "He seemed pretty on edge when I stopped by."
    python:
        Atlas_State['eye'] = 19
        adjustChar("Robyn",brow=0,mouth=1)

    Atlas "Jeez, I'm glad I don't have siblings."

    python:
        adjustChar("Hazel",mouth=3,eyes=2,brow=0)

    Hazel "Most of us aren't so lucky."

    python:
        adjustChar("Hazel",mouth=0,eyes=3,brow=2)
        adjustChar("Atlas",eye=7,feelers=1)

    Hazel ".,Gah, that's not true, I'm just annoyed."

    python:
        adjustChar("Hazel",mouth=0,eyes=0,brow=1)
        adjustChar("Atlas",eye=1,feelers=0,armL=2)

    #Atlas "I certainly haven't helped, if anything, I've caused more problems for you guys."
    Atlas "I getcha."

    python:
        adjustChar("Robyn",mouth=0,eyes=4,brow=0)
        adjustChar("Atlas",eye=0,feelers=1)

    Atlas "Sometimes [PCname] and I argue,, but we always work it out."

    Robyn "Usually."

    $adjustChar("Hazel",mouth=4,eyes=0)

    Hazel "So you're [PCname]! I've heard a lot about you."

    python:
        adjustChar("Atlas",eye=6,feelers=0,armL=0)
    Atlas "We can talk to Gus together! Then you can blame everythin' on me."
    python:
        adjustChar("Hazel",mouth=2,eyes=0,brow=1)
        adjustChar("Atlas",eye=13,feelers=1)
    Hazel "Thanks bro."
    show hazel:
        matrixtransform rotated(y=180)
        ease 0.5 matrixtransform rotated()
        ease 1.0 xcenter -0.2

    Narrator "Hazel walks away."
    show atlas:
        ease 0.5 yoffset 0 matrixtransform rotated(z=0)
    python:
        adjustChar("Robyn",brow=0,eyes=2)
        adjustChar("Atlas",eye=0)

    Atlas "She called me bro."
    hide hazel

    show atlas:
        ease 0.15 yoffset -35
        ease 0.15 yoffset 0

    python:
        adjustChar("Robyn",brow=0,mouth=0,eyes=2)
        adjustChar("Atlas",eye=16,feelers=0,armL=1,armR=1,sparkle=1)

    Atlas "Hehe!"
    $adjustChar("Atlas",eye=2,feelers=0,armL=0,armR=0,sparkle=0)
    voice atlas_heya
    Atlas "I'm gonna head home, but thanks for today!"

    Atlas "And for letting me crash at your place."

    scene BG Black
    camera at camera_default:
        camera_zoom()


    with quickDissolve
    Narrator "Atlas zips up into the air and soars away."

    jump Ch1_LakeIntro
