image chapter0 title:
    zoom 0.44
    blur 10
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_BW.webp"
    matrixcolor ColorizeMatrix("#000000","#000000")
    ease_bounce 3.0 matrixcolor ColorizeMatrix("#000000","#f91359") blur 3

image chapter0 glitch:
    zoom 0.44
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchA.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchB.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchC.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchB.webp"
    pause 0.12
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_GlitchA.webp"
    pause 0.12
    matrixcolor SaturationMatrix(1.3)
    "images/CGs/Chapter Title Cards/Chapter 0/DeadAir_Base.webp"

label CH0_TitleCard:
    $musicPlayer.playSong(fadeOut=2)
    scene black with Dissolve(0.5)
    window hide
    $quick_menu = False
    $quicker_menu_show = False

    scene chapter0 title
    camera:
        zoom 1.3 ycenter 0.7 xcenter 0.7
    with Fade(0.5, 0.5, 1.0, color="#000000")

    $musicPlayer.playSong(song="chapter_0_song",songLoop=False,notif=False)
    pause 1.5
    camera:
        zoom 1.0 zpos 0 ycenter 0.5 xcenter 0.5
    show chapter0 glitch
    $musicPlayer.playSong(song="radioStatic",fadeIn=20,music2=True)
    $renpy.music.set_volume(1.0, delay=0.0, channel=u'music2')
    pause 1.0
    camera:
        zpos 0 ycenter 0.5 xcenter 0.5

    show Ch_0_Title_Text

    pause
    stop music2 fadeout 3.0
    return

layeredimage ch0ttxt:
    always:
        Text("{ddd=#32f3ff-#ce2aff}{size=75}  Chaptitre 0  \n   Dead Air   {/size}{/ddd}")

    always:
        Text("{glitch=3.0}{size=75}{color=#32ff84}  Chaptitre 0  \n   Dead Air   {/color}{/size}{/glitch}")

image Ch_0_Title_Text:
    #WaveImage("ch0ttxt", amp = 2.75, strip_height = 6,melt=True,freq=35)
    "ch0ttxt"
    xanchor 0.0
    yanchor 0.0
    xpos -30
    ypos 30
    alpha 0
    blur 3
    pause 0.6
    ease 0.5 alpha 1

label Ch0_Intro:
    stop music2
    stop music

    python:
        musicPlayer.playSong()
        timeText = "12:00AM"

    scene BG Apartment Bedroom

    show Atlas_Phone Ring CG:
        xcenter 0.5

    with Fade(0.5, 1.0, 0.5, color="#000000")

    play sfx phone_notif
    Narrator "{sc=3}Buzz- Buzz-{/sc}"

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 1
        Robyn_State["armR"] = 1


        Taro_State["pawR"] = 1
        Taro_State["eyes"] = 2
        Taro_State["mouth"] = 4

    Narrator "Ton téléphone sonne et te réveille avec une nuée de messages qui apparaissent sur l'écran de vérouillage."
    play music astral_reflection
    show Atlas_Phone CG
    Atlas "Hey, t'es réveillé?"

    Atlas "{bt=3}C'est l'heure~{/bt}"

    Atlas "L'heure fantôme."

    Atlas "Je t'ai envoyé l'adresse!"

    Atlas "Suit la tour radio et tu trouvera!"

    Narrator "Tu est toujours a moitié endormis quand tu lit le message. Le nombre de notifications ayant un effet néfaste sur ton cerveau."

    Narrator "Tout ce que tu parvient a répondre dans ta somnolance est—"
    stop music
    $musicPlayer.playSong()
    Robyn "K."
    scene black with dissolve

    $timeText = "12:30AM"
    Narrator "..."

    $timeText = "1:00AM"
    $musicPlayer.playSong(song="eating_in_the_car_song",fadeIn=10)

    Narrator "Soundainement un sentiment froid te parcourt la colone vertébrale,, te réveillant sur le coup avec des frissons dans le dos."

    scene BG Apartment Bedroom
    camera:
        zoom 3.0
        xcenter 1.05
        ycenter 0.8

    python:
        Taro_State["pawR"] = 1
        Taro_State["eyes"] = 2
        Taro_State["mouth"] = 4

    show taro:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter 0.7
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat
    Robyn "..!"

    Narrator "Tu appercois une silhouette large et floue, formant un chat gris avec 3 yeux et une queue en feu, en train d'enfoncer ses pates translucides dans ton visage maintenant complètement éveillé."

    voice taro_greetingsmortal
    Taro "Salutations mortel."

    with hpunch
    camera:
        ease 2.0 xcenter 0.5 ycenter 0.5 zoom 1.0

    Narrator "D'un cri, tu te dégage du lit, trandis le félin transparent phase a travers ton corps."
    camera:
        ease 0.5 xcenter 0.5 ycenter 0.5 zoom 1.0

    python:
        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 2

        Taro_State["pawR"] = 0
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

    show robyn pjs:
        xcenter -0.6
        pause 0.5
        matrixcolor TintMatrix("#bbb4ff")

        xcenter 0.6
        yoffset 700
        ease 0.5 xcenter 0.3 yoffset 0

    voice RobynSays("Chapter 0","CantYouJustBeNormal")
    Robyn "Tu peux pas juste être {sc=3}NORMAL?!{/sc}"

    python:
        Taro_State["eye"] = 3
        Taro_State["mouth"] = 4

    voice taro_iwasgettingdesperate
    Taro "T'a loupé 3 alarmes! Tu commencais a me désespérer!."

    python:
        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 1

        Taro_State["eye"] = 0
        Taro_State["mouth"] = 4

    show robyn:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter 0.3
        yoffset 0
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)


    Robyn "Okay, OKAY. Je suis réveillé! Et en retard aussi!"

    $Robyn_State["mouth"] = 3

    show robyn:
        ease 0.5 xcenter -0.3

    Narrator "Tu court dans tout l'appartement a la recherche de ce tu aurais potentiellement besoin pour cette nuit."

    show robyn default:
        xcenter -0.3
        matrixtransform RotateMatrix(0,0,0)

        ease 0.5 xcenter 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.5
        linear 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        ease 0.25 xcenter 0.7
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        ease 0.25 xcenter 0.9
        pause 0.5
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        linear 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        pause 0.7
        linear 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "Tu relis ta liste mentale, ‘N'oublie pas la lampe, pince, granola bars, et….’"

    show robyn:
        xcenter 0.9
        ycenter 0.8
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

        ease 0.5 ycenter 1.1 matrixtransform RotateMatrix(0.0, 180.0, -20.0)
        pause 0.7
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 ycenter 0.8
        ease 2.0 xcenter -0.2

    Narrator "Tu t'accroupis pour faire tes lacets et enfile ta veste. Tu ouvre la porte brusquement et parcourt le couloir en direction de la voiture."

    python:
        Taro_State["eye"] = 2
        Taro_State["mouth"] = 3

    Taro "A-Attend moi!"

    python:
        Taro_State["eye"] = 4
        Taro_State["mouth"] = 3

    show taro:
        ease 0.6 xcenter -0.2

    Narrator "Taro doit tracer pour te rattraper, elle proteste en miaulant alors qu'elle saute de la première marche des escaliers et déscend, en passant a travers le mur de ton appartement."

    python:
        songText = "Midway to Nowhere"
        musicNote = 8

    hide screen quicker_menu

    call CH0_TitleCard from _call_CH0_TitleCard

    camera:
        zpos 0 ycenter 0.5 xcenter 0.5

    python:
        quick_menu = True
        musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=8,fadeOut=1)

    scene BG Road Side with Fade(0.5, 0.5, 0.5, color="#000000")
    window show

    Narrator "Taro arrive finallement sur ton épaule en te mordant l'oreille."

    play sfx hurt_a
    Robyn "OW!"

    Narrator "Tu essaie d'écarter le chat fantôme de ton épaule mais ta main passe tout simplement à travers."

    Taro "J'te tient!"

    #Robyn "Ugh."

    #Narrator "Après avoir convaincu Taro que le siège passager est le siège le plus cool de la voiture, elle s'installe enfin, te laissant t'attacher et démarrer le moteur."

    show Driving Night Graphic
    play sfx carStart
    Narrator "Tu allume les phares avant d'avancer dans la rue."

    stop sfx fadeout 1.0
    play ambiance car_ambiance fadein 8.0
    Taro "T'es sûr qu'Atlas va vraiment être utile?"

    Narrator "Elle garde ses petites pattes sous ses poils comme un petit pain."

    Taro "Tu sais ce qu'ont dit sur les mothmans…"

    voice RobynSays("Generic","Annoyed")
    Robyn "Qu'ils porte malheur?"

    Taro "Bingo."

    Robyn "Malheur où pas, j'ai besoin de toute l'aide que je peux avoir."

    Taro "Ah ouais, cette horrible malediction."

    Taro "Tu devrais consulter quelqu'un."

    Robyn "Et c'est pas censé être TON BOULOT?"

    voice taro_smuga
    Taro "Tu crois pas que je vais travailler avec l'estomac vide,, n'est-ce pas?{nw}"

    #Narrator "Taro whimpers, bringing a weak paw to her forehead."

    extend "\n\nJe me sens faible..."

    Robyn "Tu veux que je m'arrète pour t'acheter un truc?"

    Taro "Oh non t'inquète pas pour moi. Je vais... survive... T'es celui qui est maudis, pas moi."

    Robyn "Je me sens pas vraiment différent."

    voice taro_laughab
    Taro "Ohoho, tu vas, et ça va être {i}AGONISANT.{/i}"

    Robyn "Tu n'a jamais mentionné ça!"

    Taro "Je voulais pas te faire peur! Même décrire cette malédiction ammène des choses {i}térrible{/i}."

    Robyn "Donc, tu peux pas la dissiper, tu peux même pas en parler, et ça va être atroce. Y'a quelque chose d'autre que t'a oublié de me dire ou?"

    #Taro "Ouais..."

    #Narrator "Taro bouge un peu et s'allonge dans son siège. Elle prend une pause et ferme son troisième oeuil en réflechissant."

    Taro "Bien... Y'a un décompte."

    Robyn "Un décompte?"

    Taro "Exactement. Un décompte pour ta {sc=1}MORT IMMINENTE{/sc}!"

    Narrator "Tu jette à Taro un regard de juge."

    Robyn "C'est pas drôle!"

    Taro "Prrrh, je rigole pas, débile."

    Robyn "Combien de temps il me reste?"

    Taro "C'est à un chat de savoir, et à un physicien de découvrir."

    Robyn "Mais c'est pour ça que t'est là non? Guardien comsique et tout. Tu est censé me protéger."

    #Taro "..."

    Taro "...Absolument!"

    show Atlas_Phone Ring CG:
        xcenter 0.7
        yoffset 700
        ease 0.5 yoffset 0

    play sfx phone_notif
    Narrator "Ton téléphone sonne en vibrant dans le porte goblet."

    show Atlas_Phone CG
    Atlas "{sc=2}T'es où?{/sc}"

    Robyn "J'arrive. Et serieux, comparé à toi nous on peux pas voler."

    Atlas "Tu t'es rendormis, pas vrai?"

    Robyn "Je suis pas nocturne!"

    Atlas "Pas avec cette attitude! \n\nBref tu vois la station?"

    Narrator "Tu t'avance sur le siège, ta tête presque collée contre le parre brise tu appercois une tour radio qui coupe le ciel illuminé de la nuit."

    Robyn "Je crois?{nw}"

    extend "\n\nC'est juste nous trois?"

    Atlas "Sa dépend... Tu pense quoi des démons?"

    Robyn "J'aime bien. pourquoi?"

    Atlas "J'ai un ami qui vient de finir le travail et iel se demandais si iel pouvait venir! \n\nJe pensais que j'allais te demander avant!"

    Robyn "Ouais, je préfererais être dans un groupe plus large."

    voice atlas_booyah
    Atlas "Cool!"

    Robyn "A toute."

    Atlas "N'oublie pas la fréquence fantôme!"

    #Taro "There’s ghosts on the radio waves?"

    Robyn "Chaine 103.1, Elkhorn Radio, Je sais. Je sais."

    Atlas "Cool ça—{nw}"


    show Atlas_Phone CG:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        parallel:
            ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 360.0)
        parallel:
            ease 0.25 yoffset -150
            ease 0.25 yoffset 0

        on hide:
            ease 1.0 yoffset 700

    play sfx hurt_b
    Narrator "{i}BONK{/i}"

    Narrator "On peut entendre des plummes qui frottent contre le microphone et l'audio qui coupe avant qu'Atlas gémisse."

    Atlas "Pardon. J'ai mangé un lampadaire."

    Atlas "O-On se voit plus tard. \n\n\Fait gaffe sur la route!"

    hide Atlas_Phone
    Narrator "Atlas raccroche."

    #Taro "Psh, classic moth move."

    Narrator "T'imaginer atlas se taper contre une ampoule géante te fait réaliser..."

    Robyn "J'ai oublié la lampe!"

    Taro "On dirait qu'on va devoir faire une pose snack après tout!"

    #voice RobynSays("Generic","HmphB")
    #Robyn "Putain..."

    Narrator "Passant par la fenètre est une vielle station de gas appelée Al’s Owl Nighter. Plusieurs publicitées tarnies par le soleil replissent les vitres salles du magasin, des vignes poussant sur les cotés du batiment dans le ciment."

    Narrator "Ca à l'air plûtot sécurisé, pas vrai? C'est bien éclairé en tout cas."

    $musicPlayer.playSong(song = "next_time_on_song",songLoop=False,fadeOut=0.5)
    stop ambiance fadeout 4.0
    jump Ch0_Minimart

label Ch0_Minimart:
    scene BG Gas Station Night with Fade(0.5, 4, 0.5, color="#000000")
    python:
        musicPlayer.playSong(song="pleasant_conversation_song",fadeOut=2,fadeIn=1)
        timeText = "1:30AM"

        Robyn_State["armR"] = 0
        Robyn_State["brow"] = 0
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 0

        Taro_State["eye"] = 0
        Taro_State["mouth"] = 0

    Narrator "Un petit jingle retenti dans l'aire de nuit, alors que les portes automatiques du magasin souvre horizontallement."

    Narrator "Tu sort sous le ciel étoilé, avec du sushi de super-marché et une lampe-torche franchement cheap."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 4
        Robyn_State["mouth"] = 3

    show robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.6
        appearBlack(shading="#bbb4ff",t=0.5)

    voice RobynSays("Chapter 0","SuspiciouslyUnderpriced")
    Robyn "Ce sushi était... {i}suspicieusement peu-cher.{/i}"

    Narrator "Tu porte le ticket devant le panneau illumé par des néons, en le regardant \navec précision."

    $Robyn_State["eyes"] = 2
    show robyn:
        matrixcolor TintMatrix("#bbb4ff")
        alpha 1
        blur 0
        ease 0.15 yoffset -20
        ease 0.15 yoffset 0

    voice RobynSays("Chapter 0","HmOhWell")
    Robyn "Bon et bah."

    show robyn:
        ease 1.6 xcenter 0.3
        linear 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    Narrator "Tu te rend vers ta voiture, tes achats en main, et observe l'horizon."

    Narrator  "Tu observe silencieusement la ville endormie de Longhope, ta nouvelle maison, perdu dans tes pensées."

    Narrator "T'a pas vraiment eu un moment pour toi depuis que ce chat est pratiquement apparu dans ta vie sans rien dire."
    
    Narrator "..."

    Narrator "Tu reprend tes esprits d'un soupir fatigué et te redirige vers la voiture."

    python:
        Robyn_State["eyes"] = 1
        Robyn_State["mouth"] = 5

    Narrator "Tu ouvre la porte, et balance le sac plastique sur les sièges arrière avec un peu de colère."

    python:
        Robyn_State["brow"] = 1
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 5

    Narrator "Tes tympans receuillent un son léger, camouflé comme des griffes qui grattent contre du cuir, le son d'une personne horrible en train de cacher son crime."

    python:
        Robyn_State["brow"] = 3
        Robyn_State["eyes"] = 0
        Robyn_State["mouth"] = 4

    Robyn "Taro,, sale peste! {sc=2.5}C'est {b}MA{/b} voiture!{/sc}"

    python:
        Robyn_State["mouth"] = 5

        Taro_State["eye"] = 1
        Taro_State["mouth"] = 4
        Taro_State["pawR"] = 2
        Taro_State["pawL"] = 1

    show robyn:
        ease 0.5 xcenter 0.5

    show taro:
        matrixcolor TintMatrix("#bbb4ff")
        xcenter -0.3
        ease 0.5 xcenter 0.3

    voice taro_laughab
    Taro "{bt=4}Prrrrb{/bt}?"

    python:
        Taro_State["pawR"] = 1
        Taro_State["pawL"] = 0

    show robyn:
        xcenter 0.5
    Narrator "Taro relache sa patte et s'étire, déchiquetant le siège avec ses griffes."

    python:
        Taro_State["eye"] = 0
    Taro "Et bien m'a mère m'a toujours dit que le monde était mon griffoire!"

    #Narrator "Elle lève son visage et ronronne."

    python:
        Robyn_State["brow"] = 0
        Robyn_State["mouth"] = 3

        Taro_State["eye"] = 3

    Taro "J'épargnerais peut-être l'interieur de ta voiture si tu me donne quelque chose que je veux~"

    python:
        Robyn_State["eyes"] = 2
        Robyn_State["mouth"] = 0

        Taro_State["eye"] = 5

    Narrator "Elle penche sa tête sur le coté et ferme les yeux."

    python:
        Robyn_State["brow"] = 2
        Robyn_State["eyes"] = 3
        Robyn_State["mouth"] = 0

    #Robyn "{bt=2.5}Rooh okeeeh-...{/bt}"

    python:
        Robyn_State["eyes"] = 3
        Robyn_State["mouth"] = 0

    show robyn:
        ease 2.0 xcenter 0.35

    Narrator "Tu lève les yeux et approche le félin, puis gratouille gentiment Taro derrière les oreilles. Elle est plûtot froide pour être une grosse boule de poils."

    show robyn:
        xcenter 0.35

    Robyn "T'es vraiment impossible Taro. Serieux, quel genre de chat me rammène après minuit pour du sushi expiré? On est censé être avec Atlas!"

    $Taro_State["eye"] = 3

    show robyn:
        ease 2.0 xcenter -0.2

    show taro:
        ease 2.0 xcenter -0.25

    Taro "Un nyange évidemment! Où plûtot c'est ce que j'aime bien m'appeler. Tu sais que je suis pas juste un chat normal, hein?"

    hide robyn
    hide taro
    Narrator "Tu arrache l'embalage plastique et le glisse près du matou."

    #Robyn "How does a ghost cat eat? The world may never know."

    Narrator "Tu tourne la clé, la vielle voiture démarre."

    Robyn "On ferais mieux de y'aller avant que je tombe de someil."

    $musicPlayer.playSong(fadeOut=6)
    play sfx car_ignition
    Narrator "La voiture démarre, sort du parking du magasin et s'enfonce dans les rues faiblement éclairées de Longhope."

    window hide
    scene BG Road Side with pixellate #----------------------------------------- Road side
    window show

    play ambiance car_ambiance fadein 8.0
    $musicPlayer.playSong(song="midway_to_nowhere_song",fadeIn=8)
    stop sfx fadeout 1.5
    show Driving Night Graphic
    python:
        timeText = "1:45AM"
        songText = "Midway to Nowhere"
        musicNote = 11

    #Maybe put in a Robyn line here to warrant the Taro response more

    Narrator "Taro dévore le reste du poisson et se lèche les coussinets."

    #Taro "You’ve got nothing to worry about, [PCname]."

    Taro "Dit [PCname]? On était pas censé chercher une fréquence fantôme?"

    #Narrator "Taro meows, as she gazes out the window and the car drives up the road." #as you drive further up the mountain.

    Robyn "Ah, ouais."

    Narrator "Tu glisse ta main sur la stéréo et allume le système."

    play sfx radio_tuning
    Narrator "La radio s'allume, avec un son blanc très aigu, elle change entre les fréquences jusqu'a atteindre 103.1 FM."

    stop sfx

    $musicPlayer.playSong(song="elkhorn_radio_intro_song",songLoop=False,notif=False)
    Narrator "Le static est coupé par un jingle stupide, suivit par une sorte d'émission radio."

    $musicPlayer.playSong(song="elkhorn_radio_blues_song_radio",fadeIn=3)
    voice mm_radio_goodeveningfreaksters
    Madhouse "{color=#3bec27}Booooonne soirée freaksters! Vôtre hôte préférée {b}MADHOUSE MIKE{/b} est en LIVE à la station du conté d'Elkhorn."

    voice mm_radio_whatsthatdebbie
    Madhouse "{color=#3bec27}C'est quoi? On dirait que mon producteur est en train de m'annoncer que, je suis en fait, MORT! Haha! Merci Debbie."

    voice mm_radio_shoutout
    Madhouse "{color=#3bec27}Donc avant de commencer! J'aimerais dire un mot à tout les gens qui m'écoutent!"

    voice mm_radio_supportandfanmail
    Madhouse "{color=#3bec27}C'est votre support qui garde ce show en vie a l'instart de moi même, donc pour vous remercier, je vais commencer le show de ce soir en lisant quelques-unes de vos lettres!"

    Narrator "Il néttoie sa gorge et débute son discours."

    voice mm_radio_heylovely
    Madhouse "{color=#3bec27}{bt=5}{color=#3bec27}Hey choupi!{/bt}Tu veux travailler proche de chez toi avec des horaires flexible? Evidement que oui mon chou!"

    voice mm_radio_girlboss
    Madhouse "{color=#3bec27}Rejoins notre loyale famille, et devient la girl boss de tes rèves!"

    voice mm_radio_joinusandflourish
    Madhouse "{color=#3bec27}Pour un petit prix de vingt-mille dollars tu peux t'enroller dans nos courses et commencer à {glitch=40}{color=#3bec27}nourrir~{/color}{/glitch} notre entreprise aujourd'hui! Rejoins nous et fleuris la grande mère!"

    voice mm_radio_fleshyletter
    Madhouse "{color=#3bec27}Wow. Merci beaucoup pour cette lettre d'une étrange menacante et {bt=4}{color=#3bec27}charnue{/bt} écriture! Serieusement ce truc est bien {sc=3}{color=#3bec27}CHAIR et en OS!—{/sc}"

    python:
        musicPlayer.playSong(fadeOut=2)
        pauseEnable = True

    Narrator "Tu éteint la radio."

    Robyn "Dégeu."

    voice taro_meowf
    Taro "T'avais pas envoyé une lettre de fan?"

    Robyn "Je m'appelerait pas un 'fan',, serieux, j'ai jamais entendu parler de ce type!" #I wouldn't call myself a "fan" Taro.

    Narrator "Tu grimace, regardant par la fenètre alors que les bois commencent a s'éclaircir dans un certain vide."
    voice taro_laughc
    Taro "C'est pas très sympa d'embèter un type que tu connais même pas."

    Narrator "Le squelette de la tour radio s'étend à l'horizon, souvrant sur ta destination... \nElkhorn Radio Station."

    jump atTheStation