label MM_fightAftermath:
    scene BG Studio Room Spooky
    camera:
        matrixcolor TintMatrix("#cbffd6")
    python:
        HideBars()

        barHidden = True
        showBar1 = False
        showBar2 = False
        showBar3 = False
        showBar4 = False

        Jamie_State["brow"] = 0
        Jamie_State["mouth"] = 0
        Jamie_State["armL"] = 0
        Jamie_State["pants"] = True
        Jamie_State["rings"] = True,
        Jamie_State["alFace"] = False
        Jamie_State["blush"] = False
        Jamie_State["sweat"] = False
        Jamie_State["steam"] = False
        Jamie_State["hurt"] = False
        Jamie_State["wispEyes"] = 0
        Robyn_State["brow"] = 0
        Robyn_State["armR"] = 0
        Robyn_State["armL"] = 0
        Atlas_State["eye"] = 0
        Atlas_State["armL"] = 0
        Atlas_State["armR"] = 0
        Atlas_State["feelers"] = 0

        Jamie_State["eye"] = 6
        Jamie_State["armR"] = 2
        Jamie_State["fire"] = 0
        Jamie_State["r3fire"] = 0

        Atlas_State["eyeFrame"] = 2

        Robyn_State['eyes'] = 0
        Robyn_State['mouth'] = 2

    show jamie:
        xcenter 0.5
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show atlas:
        xcenter 0.4

    show tarobig:
        xcenter 0.175

    show robyn:
        xcenter 0.1
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show demon_madhouse:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        xcenter 0.85

    with Fade(0.1, 0.2, 2.0, color="#FFF")
    python:
        musicNote = 5
        musicPlayer.playSong(3)

    voice dmm_realdeal
    Madhouse "Pff vous lâchez vraiment jamais, hein? Heh, c'est un match..."

    show demon_madhouse:
        matrixcolor BrightnessMatrix(0)
        ease 1.0 alpha 0 blur 30 matrixcolor BrightnessMatrix(1.0)

    Narrator "La forme du spectre clignote, il se ramasse au sol et recrache de l'éctoplasme."
    $Jamie_State["armR"] = 2
    $Jamie_State["fire"] = 0
    $Jamie_State["r3fire"] = 0
    hide demon madhouse
    Jamie "Let me finish this."

    show jamie:
        ease 0.4 xcenter 0.65

    Narrator "Jamie fait un pas en avant, de la rage brûlant dans ses yeux."

    ##TODO voice PC_Frustrated
    show robyn:
        ease 0.1 yoffset -20
        ease 0.1 yoffset 0

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 7
    $MM_State["mouth"] = 9
    Robyn "Nooon! J'ai toujours des questions!"

    show robyn:
        ease 0.5 xcenter 0.45

    show atlas:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 xcenter 0.25 matrixtransform RotateMatrix(0.0, 180.0, 0.0)

    show tarobig:
        ease 0.5 xcenter 0.05



    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 1
    $Robyn_State['brow'] = 4
    Narrator "Tu t'aggripes au bras de Jamie, en éssayant de l'empècher d'agir."

    Madhouse "C'est vraiment tout ce qui t'importe?! Vous êtes vraiment tous désespérés!"

    show jamie:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.9
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    show robyn:
        ease 0.3 xcenter 0.45

    show madhouse:
        alpha 0 blur 30
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        xcenter 0.6
        ease 0.5 alpha 1 blur 0

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    Narrator "Essouflé, Mike utilise le peu de force qu'il lui reste et se jette sur toi."
    $Jamie_State["steam"] = 1

    Madhouse "Et toi tu vients avec moi!"
    $Robyn_State['eyes'] = 4
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 1
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    jump ghostzone_ch0

label ghostzone_ch0:
    scene BG Spirit World

    python:
        musicPlayer.playSong(song = "ghost_space",fadeIn=5)
        timeText = "UNKOWN"

    with Fade(2.0, 1.0, 1.0, color="#fff")
    camera:
        matrixcolor TintMatrix("#ffffff")
    Narrator "Tu te débat pour réster éveillé, tu cligne tes yeux qui percoivent une douce lumière. C'est quoi cet endroit? Tu fronce les sourcils et te couvre le visage de la forte lumière."

    Narrator "Tu regarde en bas et voits une silhouette verte accrochée a toi."

    show CG Floating Away
    with Fade(0.5, 0.1, 0.5, color="#fff")

    Narrator "C'est Madhouse qui à l'air complètement paumé, il tient d'une manière ferme ta jambe et te garde en place."

    Robyn "Lâche moi!"

    Madhouse "NON!"

    Madhouse "{b}Tu va disparaitre!{/b}"

    Robyn "C'était pas le but? C'est ce que tu voulais non?!"

    Narrator "Tu te débat les larmes presque aux yeux, tentant de faire lacher prise au fantôme."

    Madhouse "Attend! Chillax une seconde!"

    Narrator "Il te tire comme un balon, et le lâche la jambe puis regarde ailleurs l'air de rien."

    show CG Floating Away:
        alpha 1
        ease 0.5 alpha 0

    show madhouse:
        matrixcolor TintMatrix("#ffded1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        xcenter 0.25
        pause 0.25
        ease 0.7 yoffset 10
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    show dead_robyn:
        matrixcolor TintMatrix("#ffded1")
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        yoffset 700
        xcenter 0.75
        pause 0.5
        ease 0.65 yoffset -15
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    $MM_State["armL"] = 2
    $MM_State["armR"] = 2
    Madhouse "É-Écoute! C'est pas un important! Je t'ai rammené ton âme en dehors de ton corps et je t'ai mit dans le vide!"
    hide CG Floating Away

    $D_RobynFace = 1
    $MM_State["mouth"] = 3
    Robyn "TU VEUX DIRE QUE JE SUIS MORT!?"



    $MM_State["eyes"] = 1
    $MM_State["mouth"] = 9
    $MM_State["armL"] = 1
    $MM_State["armR"] = 1
    $D_RobynFace = 2
    Madhouse "Yeesh,, ça a l'air encore pire quand tu le dit comme ça."

    Robyn "On est où?!"
    $MM_State["mouth"] = 2
    $D_RobynFace = 0
    Madhouse "Entre rien du tout, et le monde du vivant."

    $MM_State["mouth"] = 3

    Madhouse "Des fois je me réveille là si je m'endors sur le bureau trop longtemps."


    $MM_State["mouth"] = 11
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    $MM_State["eyes"] = 0
    Madhouse "Maintenant donne moi ton âme!"

    $D_RobynFace = 1
    $MM_State["mouth"] = 10
    Robyn "Nan,, TU me donne TON ÂME!"

    $MM_State["mouth"] = 4
    Madhouse "Nah."

    $D_RobynFace = 2

    Robyn "Pourquoi tu m'a ammené içi? Qu'est-ce que tu veux?!"

    $MM_State["eyes"] = 3
    $MM_State["mouth"] = 0
    $MM_State["armL"] = 1
    $MM_State["armR"] = 1

    Madhouse "J'ai besoin d'un réceptacle pour me casser, un corps! Tu te sent pas mal pour moi? Alllezzz, t'a vu des films, tu sait comment ça fini!"

    Robyn "..."

    $musicPlayer.playSong(song="drink_it_song",fadeOut=0.5)
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0

    Madhouse "Je peux te dire ce que tu veux! Et cette malédiction stupide?"

    $hatKnock = False
    $displaymenu = True
    menu:
        extend ""
        "Frappe moi ct'enculé.":
            pass
        "Explose moi son chapeau.":
            $hatKnock = True
        "Met fin a son après-vie avec ton poing.":
            pass
    $displaymenu = False
    Narrator "Tu ferme tes mains en boule et lance une 'grosse patate' dans son visage."
    $D_RobynFace = 1
    show dead_robyn:
        ease 0.2 xcenter 0.4 matrixtransform RotateMatrix(0.0, 180.0, -15.0)
        pause 0.5
        ease 0.3 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    show madhouse:
        pause 0.15
        matrixtransform RotateMatrix(0,0,0)
        parallel:
            ease 0.1 xcenter 0.2 matrixtransform RotateMatrix(0.0, 0.0, -40.0)
            linear 4.9 matrixtransform RotateMatrix(0.0, 0.0, -80.0) blur 10
        parallel:
            ease 5.0 yoffset 300

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 1
    pause 0.15
    play sfx hurt_d
    with hpunch

    $musicPlayer.playSong(song = "ghost_space")

    if hatKnock:
        Narrator "Tu ferme les yeux, et ton bras connecte avec son visage, et expulse son chapeau de son crâne."

        Narrator "Mike panique un instant et reprend sa casquette avant de l'enfoncer fermement sur son lôbe frontal."
    else:
        Narrator "Tu ferme les yeux, et ton bras connecte majéstueusement avec son visage."

    show madhouse:
        ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)  xcenter 0.3 yoffset 0 blur 0
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat
    $MM_State["eyes"] = 3
    $MM_State["mouth"] = 1

    show dead_robyn:
        matrixtransform RotateMatrix(0.0, 180.0, 0.0)
        ease 0.5 xcenter 0.6
        block:
            ease 2.75 yoffset 15
            ease 2.75 yoffset -15
            repeat

    Madhouse "Gyaaughck!"

    voice RobynSays("Chapter 0","YoureAnAsshole")
    Robyn "Trou du cul!"

    $MM_State["eyes"] = 7
    $MM_State["mouth"] = 1
    $MM_State["armR"] = 3
    $MM_State["armL"] = 2
    $D_RobynFace = 2
    Madhouse "Eh mon nez!! Comment est-ce que tu m'a touché?!"

    Narrator "Il se touche le visage, sentant l'éspace vide où sont nez serait habituellement."

    $D_RobynFace = 1
    voice RobynSays("Chapter 0","YouDraggedMeIntoThisHellDimension")
    Robyn "Tu m'a ammené dans cet endroit,,FLASH INFO! On est tout les deux des fantômes!"

    Narrator "Tu jettes tes bras sur les cotés, montrant l'éspace vide dans lequel vous êtes tout deux situés."
    $Robyn_State['eyes'] = 2
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 2

    $D_RobynFace = 2

    voice RobynSays("Chapter 0","OfCourseIFeelBadForYouMike")
    Robyn "Evidement que je me sens mal pour toi, Mike. Tu ne méritait pas de mourir,, où même de devenir un monstre, mais là toute suite tu agis exactement comme l'un deux!"

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3
    Narrator "Mike est figé, sans vraiment savoir quoi dire."

    voice RobynSays("Chapter 0","SoIfYoureGonnaEatMySoul")
    Robyn "Donc si tu vas voler mon âme, tu ferais mieux de le faire maintenant!"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 9
    $MM_State["armR"] = 0
    $MM_State["armL"] = 0

    voice mm_gladly
    Madhouse "Très bien!"

    show madhouse:
        ease 0.3 xcenter 0.35
        pause 0.5
        ease 0.3 xcenter 0.4
        pause 0.5



    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 11

    $D_RobynFace = 3

    Robyn "Mais tu le feras pas."
    pause 5.0

    show madhouse:
        ease 0.5 xcenter 0.36
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 4
    $MM_State["armL"] = 2
    $MM_State["armR"] = 2

    Narrator "Le spectre recule."

    ##TODO voice MM_Quit1
    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3
    Madhouse "Ouais;., Je peux pas faire ça."
    $D_RobynFace = 2
    Robyn "Pourquoi pas?"

    show madhouse:
        ease 0.3 xcenter 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        block:
            ease 2.6 yoffset -10
            ease 2.6 yoffset 10
            repeat

    $MM_State["mouth"] = 1
    Madhouse "J'ai pas envie de te blésser."

    $MM_State["mouth"] = 2
    Madhouse "J'aurais jamais du tous vous mettre là dedans. Je... Je sais pas quoi faire."

    Madhouse "J'ai envie de me barrer, mais est-si je disparais? Tout ce que j'ai c'est ce boulot. Je me souviens même pas de mon ancienne vie."

    $MM_State["mouth"] = 9

    Madhouse "Putain, je me souviens même plus de mon visage."

    $MM_State["armR"] = 2
    $MM_State["armL"] = 3
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    Narrator "Mike baisse son chapeau sur son visage pour couvrir ses yeux."

    Madhouse "Dammit."

    Robyn "Tu vas pas disparaitre."

    $MM_State["mouth"] = 1

    Madhouse "Vas dire ça aux autre demeurés en bas."

    $D_RobynFace = 3

    Robyn "Si tu veux faire un nouveau départ, tu pourrais faire un podcast! C'est un peu comme une radio mais partout avec toi."

    $MM_State["eyes"] = 4
    $MM_State["mouth"] = 2
    $MM_State["armL"] = 0
    $MM_State["armR"] = 0
    Madhouse "Sur ton tél?"

    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 0
    Narrator "Mike réagis, une petite lueur dans ses yeux."

    Narrator "Tu éssaie de sortir ton portable, seulement pour réaliser qu'il n'est que dans le monde matériel."

    Robyn "Erm, je te montrerais plus tard."

    $MM_State["eyes"] = 5
    $MM_State["mouth"] = 3

    Robyn "Même si t'es un connard."

    $D_RobynFace = 2

    Robyn "Et puis, Je crois que tu vaux bien plus que cette vielle station radio."

    $MM_State["armR"] = 2
    $MM_State["armL"] = 3
    $MM_State["eyes"] = 0
    $MM_State["mouth"] = 2

    show CG Lifeline at lifeline_pos
    hide madhouse
    hide dead_robyn
    with Dissolve(0.3)
    Narrator "Mike hésite un instant avant d'envelopper ses bras autours de toi, t'offrant un gros câlin."

    voice mm_thanksfornotgivingup
    Madhouse "Merci,, de pas m'avoir abandonné."

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 6
    $Robyn_State['brow'] = 2
    Robyn "T'a pas besoin d'être le fantôme de la station d'Elkhorn. \n\n Plus maintenant."

    Robyn "Pas si ça te fait sentir misérable."

    show CG Lifeline2

    Madhouse "{sc=5}...{/sc}"

    Madhouse "{sc=2}Dégage de là.{/sc}"

    jump leavingElkhornRadio_ch0

label leavingElkhornRadio_ch0:
    python:
        musicPlayer.playSong(fadeOut=10)
        timeText = "???"

    #Narrator "As the two of you are drowned in light, you swear you catch a glimpse of the phantom’s old face, his expression determined with eyes full of life."
    scene BG Black with Dissolve(1.0)
    Narrator "..."

    voice taro_thisisallyourfault
    Taro "C'est de ta faute!"

    voice atlas_howsitmyfault
    Atlas "Eh pourquoi ça le serait?"

    voice jamie_youknewbringingahumanhere
    Jamie "Tu savais qu'ammener un humain serait dangereux!"

    voice taro_ghostgobblingdemon
    Taro "Dit le putain de démon."

    voice jamie_tarowherewereyou
    Jamie "Ah ouais. Taro, t'étais où, putain??"

    voice taro_iwastheretoprotectmyhuman
    Taro "Pff, on s'en fout! J'étais là pour protéger [PCname] et c'est ce qui compte!"

    voice jamie_bareminimum
    Jamie "T'a fait le minimum syndical."

    voice taro_biteyourtongue
    Taro "Pff-."

    voice atlas_knewwouldworkout
    Atlas "Je savais ce qui allait se passer."

    voice jamie_stoplyingatlas
    Jamie "Arrète de te mentir, Atlas."

    voice atlas_canseethefuture
    Atlas "M-mais, je peux vraiment voir le futur!"

    voice taro_proveitmothball
    Taro "Alors prouve le, mothball."

    voice RobynSays("Chapter 0","Urgh")
    Robyn "Oof..."

    #" "
    show BG Studio Room Aftermath
    camera:
        matrixcolor TintMatrix("#abbdeb")

    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 0
    $Jamie_State["steam"] = 0

    $Taro_State["eye"] = 1
    $Taro_State["mouth"] = 3

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 5

    show jamie:
        xcenter 0.8

    show taro:
        xcenter 0.75
        matrixtransform RotateMatrix(0,180,0)

    show atlas:
        xcenter 0.3
        matrixtransform RotateMatrix(0,180,0)

    with Dissolve(0.5)

    $Taro_State["eye"] = 3
    $Taro_State["mouth"] = 1

    Taro "Ferme là! Regarde, [PCname] se réveille!"
    python:
        musicPlayer.playSong(song="dirt_nap_dreams")
        timeText = "Fatigué."

        Atlas_State["eyeFrame"] = 0
        Atlas_State["eye"] = 7

        Robyn_State['eyes'] = 3
        Robyn_State['mouth'] = 2
        Robyn_State['brow'] = 2

    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, -30.0)
        xcenter 0.5
        yoffset 700
        ease 1.2 yoffset 0 matrixtransform RotateMatrix(0.0, 0.0, 0.0)


    Robyn "Ugh. Je me sens horrible."

    $Atlas_State["armL"] = 0
    $Atlas_State["eye"] = 16
    Atlas "Dieu merci tu vas bien!...\nEt j'avais raison."

    hide taro
    show robyn:
        yoffset 0
        ease 0.3 matrixtransform RotateMatrix(0.0, 0.0, 0.0)
    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        xcenter 0.75
        ease 0.5 xcenter 0.5 matrixtransform RotateMatrix(0.0, 180.0, 0.0)
    $Taro_State["eye"] = 5
    $Taro_State["mouth"] = 0

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 1
    Narrator "Taro se jette dans tes bras, elle se frotte contre ton cou et ronronne."

    ##TODO voice Taro_Cute
    Taro "C'est mon humain!"
    $Jamie_State["eye"] = 2
    $Jamie_State["armR"] = 1
    $Jamie_State["steam"] = 1
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["tears"] = 0
    Jamie "Plus important, ce foutu fantôme est parti."

    Narrator "Jamie soupire, soulagé."
    $Jamie_State["armR"] = 0
    $Jamie_State["steam"] = 0

    ##TODO voice Atlas_Dismissive
    $Atlas_State["eyeFrame"] = 3
    $Atlas_State["eye"] = 2
    $Atlas_State["armL"] = 0
    Atlas "Ouais bon, on se tire d'içi."

    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 1
    Narrator "Tu ne répond pas, une douleur se forme dans le bas de ton éstomac."

    scene BG Black with Dissolve(0.5)
    $musicPlayer.playSong(song = "missing_you_song")
    play ambiance forest_ambianceb fadein 5.0
    Narrator "Tu traîne derrière le groupe, et regarde le sol, écoutant le bruit du gravier sous tes pieds. Le groupe arrive à la voiture, et te regarde alors que tu sort tes clés."

    Narrator "Vous regardez tous en direction de ce qui était la station abandonnée. Tu regarde les fissures dans les murs, la tour radio clignote en rouge avant de s'arrèter une dernière fois. "

    show BG Outside Radio Station Spooky3


    show atlas: ##TODO doteyes think:
        xcenter 1.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.2 xcenter 0.7
    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 0
    $Atlas_State["armL"] = 0

    show jamie: ##TODO casual:
        xcenter 1.5
        matrixtransform RotateMatrix(0,0,0)
        ease 2.6 xcenter 0.2
        ease 0.4 matrixtransform RotateMatrix(0,180,0)

    show robyn: ##TODO pc pensive hand:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 2.4 xcenter 0.45

    show taro: ##smile:
        xcenter 1.5
        matrixtransform RotateMatrix(0,180,0)
        ease 2.0 xcenter 0.85
    with Dissolve(1.0)

    $Robyn_State['eyes'] = 4
    $Robyn_State['brow'] = 3
    $Jamie_State["eye"] = 1
    $Jamie_State["armR"] = 2
    $Jamie_State["mouth"] = 4
    $Jamie_State["brow"] = 3

    Jamie "Ca vas pas? Tu à l'air stréssé."

    Narrator "Jamie place une main sur ton épaule."

    pause 1.0
    $Robyn_State['eyes'] = 0
    $Robyn_State['mouth'] = 4
    $Robyn_State['brow'] = 1

    Robyn "Oh ouais, t'inquète! Haha."
    $Robyn_State['eyes'] = 2

    $Jamie_State["armR"] = 1
    $Jamie_State["eye"] = 4
    $Jamie_State["mouth"] = 2
    $Jamie_State["sweat"] = 1
    $Robyn_State['mouth'] = 1

    Jamie "Se te dérange si on te suit? Mes jambes me font horriblement mal."

    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 1

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 5
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Jamie_State["eye"] = 2

    Atlas "Eeeeeet on peut dormir chez toi? Je préfère pas réveiller mon coloc August à cet heure là."

    $Taro_State["eye"] = 3
    $Taro_State["mouth"] = 2

    Taro "On s'en fout! Plus ont est plus on ris~!"

    $Robyn_State['eyes'] = 1
    $Robyn_State['mouth'] = 5
    $Robyn_State['brow'] = 3
    $Jamie_State["eye"] = 3
    $Jamie_State["brow"] = 0
    $Jamie_State["sweat"] = 0
    Robyn "Eh mais répond pas à ma place—!"

    $Taro_State["eye"] = 0
    $Taro_State["mouth"] = 3
    $Atlas_State["eye"] = 1
    Taro "Dans tout les cas t'aurais dit oui."

    $Jamie_State["eye"] = 2
    $Jamie_State["mouth"] = 0
    $Jamie_State["armR"] = 3

    Jamie "J'aime bien les soirées pyjama."

    $Jamie_State["eye"] =3
    $Jamie_State["armR"] = 2
    $Jamie_State["eye"] = 0
    $Jamie_State["wispEyes"] = 1
    $Robyn_State['eyes'] = 4
    $Robyn_State['mouth'] = 3
    $Robyn_State['brow'] = 0
    $Taro_State["eye"] = 1
    $Taro_State["pawR"] = 2

    Robyn "Pff, oké. C'est pas vraiment comme si j'avais le choix."

    $Atlas_State["eyeFrame"] = 3
    $Atlas_State["eye"] = 2
    $Atlas_State["armL"] = 0
    $Jamie_State["armR"] = 4
    $Jamie_State["eye"] = 3
    $Robyn_State['mouth'] = 5
    $Robyn_State['brow'] = 2
    Atlas "Qu'est-ce qui va pas? C'est à cause de Gus? Il est sympa, si ont écarte..."

    $Robyn_State['mouth'] = 4
    $Robyn_State['eyes'] = 4

    Robyn "Non, C'est juste—., Je sais pas comment je me sens. J'ai eu zéro réponse sur cette foutue malédiction, Je suis presque mort, et ma seule source d'information s'est vaporisée!"

    $Jamie_State["armR"] = 0
    $Jamie_State["eye"] = 1
    $Jamie_State["mouth"] = 3
    $Robyn_State['mouth'] = 1
    $Robyn_State['eyes'] = 1

    Jamie "Tant mieux pour ce cas là."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 16
    $Atlas_State["armL"] = 2
    $Atlas_State["armR"] = 0
    $Jamie_State["mouth"] = 0

    show atlas at startledSquish: #.Startled Squish
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        zoom 1
        alpha 1

    Atlas "J'suis une super source d'infos!"

    $Atlas_State["eye"] = 1
    $Robyn_State['eyes'] = 0

    Atlas "Toute les rumeurs cachent une vérité."

    $Jamie_State["eye"] = 0
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 1

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 9
    $Atlas_State["armL"] = 1
    $Atlas_State["armR"] = 1
    $Taro_State["eye"] = 4

    Atlas "Comme avaler des araignées pendant ton someil!"
    $Jamie_State["eye"] = 4
    $Jamie_State["mouth"] = 2
    $Taro_State["eye"] = 0

    ##TODO voice Jamie_joking
    Jamie "Atlas, elle a été debunk. C'est pas vrai."

    $Atlas_State["eyeFrame"] = 0
    $Atlas_State["eye"] = 7
    $Atlas_State["armL"] = 0
    $Atlas_State["armR"] = 0
    $Jamie_State["eye"] = 3
    $Jamie_State["mouth"] = 0
    $Jamie_State["sweat"] = 0
    Atlas "Oh dieu merci."

    $Robyn_State['mouth'] = 5
    $Robyn_State['eyes'] = 5
    $Robyn_State['brow'] = 1

    Robyn "Pour de vrai,, vous allez bien vous au moins?"

    $Jamie_State["mouth"] = 0
    $Taro_State["eye"] = 5
    $Taro_State["mouth"] = 4
    $Taro_State["pawL"] = 1
    $Taro_State["pawR"] = 2

    Taro "Je vais super!"

    $Jamie_State["eye"] = 1

    Jamie "Enfin fatigué."
    $Atlas_State["eye"] = 5
    $Atlas_State["feelers"] = 1

    Atlas "Mais tout vas bien,, je suis juste,, un peu dégouté de la couleur vert."

    $Robyn_State['mouth'] = 6
    $Robyn_State['eyes'] = 0
    $Robyn_State['brow'] = 2
    $Taro_State["eye"] = 0
    $Taro_State["mouth"] = 0
    $Taro_State["pawL"] = 0
    $Taro_State["pawR"] = 0


    Robyn "Ouais je vois pourquoi."

    $Atlas_State["eye"] = 8
    $Atlas_State["feelers"] = 0
    $Robyn_State['mouth'] = 5
    $Robyn_State['eyes'] = 5
    $Robyn_State['brow'] = 0
    $Taro_State["eye"] = 2

    $musicPlayer.playSong(song="the_visitor_radio_song")

    show atlas:
        linear 0.05 xcenter 0.700
        linear 0.05 xcenter 0.704
        linear 0.05 xcenter 0.690
        linear 0.05 xcenter 0.703
        linear 0.05 xcenter 0.694
        linear 0.05 xcenter 0.7


    Atlas "Mais c'était quand même sympa d'être le plus grand un moment!"

    $Jamie_State["eye"] = 4
    $Robyn_State['eyes'] = 0

    Narrator "Tu échange des regards avec Jamie."
    $Jamie_State["eye"] = 2
    $Jamie_State["brow"] = 1
    $Jamie_State["mouth"] = 2


    Jamie "Nan, je te préfère taille pikmin."

    $musicPlayer.playSong(song="dirt_nap_dreams",fadeIn=1)

    $Atlas_State["eye"] = 18
    $Atlas_State["feelers"] = 1
    $Jamie_State["eye"] = 3
    $Jamie_State["mouth"] = 0
    $Robyn_State['eyes'] = 3
    $Robyn_State['mouth'] = 0


    Robyn "Ouaaaais-, plus jamais."
    $Atlas_State["eye"] = 19
    $Taro_State["mouth"] = 2
    $Taro_State["pawL"] = 1
    $Taro_State["pawR"] = 2
    $Taro_State["eye"] = 5


    Taro "Et t'inquète pas Atlas,, Je suis sur t'avais l'air cool!"

    $Atlas_State["eye"] = 5

    show atlas:
        ease 3.0 yoffset 35

    Atlas "Hmph."


    scene BG Black with Dissolve (1.0)
    play sfx carStart
    stop ambiance fadeout 1.0

    python:
        musicNote = 3
        musicPlayer.playSong(fadeOut=8)

    Narrator "Tu sort du parking, et démarre pour te tailler de cet horrible endroit.\n\nTa tête est toujours pleine de pensés un chouilla atroces."
    jump drivingHome_ch0

label drivingHome_ch0:
    scene BG Road Side
    show Driving Dawn Graphic
    play ambiance car_ambiance fadein 8.0
    with Dissolve (1.0)

    Narrator "Une fois dans les bois tu allume la radio. Ton coeur fait mal alors que tout ce que tu entend c'est le bruit de ton moteur. Le show est vraiment fini, 103.1 c'est juste de l'air sur la radio."

    Narrator "Tu prend une grande réspiration, et trouve le courage de changer de musique, ton téléphone se connecte et affiche les anciennes radios."

    Narrator "Tu jette un oeuil au rétroviseur, tu vois Jamie avec sa tête contre la vitre, déja presque endormis... Par contre, un seul coup de tête un peu trop rapide et ses cornes finissent dans la vitre. Au moins Taro a l'air adorable dans les bras de Jamie."
    python:
        displaymenu = True
        musicNote = 9
        songText = "Annoying Phonecall"

    show MM_Phone 1 CG:
        xcenter 1.5
        ease 0.75 xcenter 0.75

    #play sfx phone_notif
    $musicPlayer.playSong(song = "digihouse_mike_song")
    Narrator "Ton téléphone sonne, c'est un appel. Le numéro est un charabia plein de chiffre et de lettres, même l'écran glitch.{nw}"

    menu:
        extend ""

        "Eww des appels, non.":
            pass
        "Yes.":
            jump drivingHomep2_ch0

    show MM_Phone 2 CG

    #play sfx phone_notif

    Narrator "Stupidement, Tu ignore l'appel. Ca coupe même pas à la méssagerie. Sa continue de sonner, le téléphone se secoue dans tout les sens. S'il te plaît décroche.{nw}"

    menu:
        extend ""

        "NOPE.":
            pass
        "Bon ok.":
            jump drivingHomep2_ch0

    Narrator "Le téléphone vibre tellement que on dirait qu'Android souffre.{nw}"

    menu:
        extend ""

        "UGH, bon ok!":
            jump drivingHomep2_ch0
        "*Missclick accidentellement et décroche*":
            jump drivingHomep2_ch0

label drivingHomep2_ch0:
    $displaymenu = False
    show MM_Phone 3 CG
    Narrator "Le portable s'éjecte sur le siège, l'écran se fige alors qu'une masse verte sort de la vitre. Avec un bruit un peu dégeu, la boule s'éjecte et forme une petite masse verte volante."
    $BM_State["face"] = 0
    $BM_State["arms"] = 0
    $musicPlayer.playSong(song="not_so_spooky_song")

    show MM_Phone:
        ease 0.5 yoffset 700
    show blobhouse:
        xcenter 0.75
        xzoom 0
        matrixtransform RotateMatrix(0,0,0) yoffset 0
        parallel:
            ease 0.2 xzoom 1.0
        parallel:
            ease 0.5 yoffset -300
            ease 0.5 yoffset 0
        parallel:
            ease 1.0 matrixtransform RotateMatrix(0,0,360*3)

        ease 1.5 yoffset 30
        idleFloat(2.3, 15)


    Madhouse "{bt=4}Hey hey heeeey~!{/bt}"

    Atlas "RACCROCHE!"

    $BM_State["face"] = 1
    $BM_State["arms"] = 1
    Madhouse "J'suis enfin libre! Enfin j'ai perdu quelques membres, mais je suis libre!"

    Robyn "Tu tu fesais du camping dans mon portable!? \n\nJ-je pensais que tu était {i}mort!{/i}"

    Madhouse "Bingo! Y'a pas moyen que je clamse maintenant! J'ai encore une tonne de vie en moi!"

    Atlas "Comment?!"

    $BM_State["face"] = 3
    $BM_State["arms"] = 0

    Madhouse "T'attacher à une personne ça prend beaucoup d'énergie, alors pourquoi pas éssayer un portable? Ce truc est bourré de mauvaises intentions."

    Atlas "M-mais tu peux pas partir! T'es le fantôme de la station d'Elkhorn!"

    $BM_State["face"] = 1
    Madhouse "{bt=4}Plus maintenant{/bt}"
    $BM_State["face"] = 5
    $BM_State["arms"] = 1
    Jamie "{sc=5}TOI{/sc}!"

    Narrator "De la fumée blanche sort de la bouche de Jamie, de la colère émanne du démon maintenant réveillé. Ses yeux enragés se fixent sur le blob, qui laisse un léger cris de terreur."

    ##TODO voice Jamie_CCD
    Jamie "SPECTRE MAUDIT, TU OSE TE MONTRER APRÈS CE QUE TU À FAIT?"

    Robyn "Jamie?"

    Atlas "Jamie! Calme-toi! Tu te souvient à quoi on s'est entrainé? RESTE COOL!"

    $BM_State["face"] = 2
    $BM_State["arms"] = 0

    Madhouse "Hiya, tête d'os!"

    voice jamie_yella
    Jamie "{sc=3}GRAWWWRGH{/sc}!"

    $BM_State["face"] = 0
    $BM_State["arms"] = 2

    show blobhouse:
        xcenter 0.75
        matrixtransform RotateMatrix(0,0,0)
        ease 0.3 yoffset 50

        block:
            parallel:
                ease 0.8 xcenter 0.25
                ease 0.2 matrixtransform RotateMatrix(0,180,0)
                ease 0.8 xcenter 0.75
                ease 0.2 matrixtransform RotateMatrix(0,0,0)
            parallel:
                linear 0.25 yoffset -100
                linear 0.5 yoffset -250
                linear 0.5 yoffset 50
                linear 0.5 yoffset -250
                linear 0.25 yoffset 50
            repeat

    Narrator "Jamie lance un coup de griffe en avant, touchant Mike qui rebondis sur le siège passagé."

    $BM_State["face"] = 2
    $BM_State["arms"] = 0

    Madhouse "Frapper un fantôme dans la merde, hein? Typique de démon."

    $BM_State["face"] = 0
    $BM_State["arms"] = 2

    show Driving Dawn Graphic:
        ycenter 0.4
        ease 0.05 xcenter 0.495
        ease 0.05 xcenter 0.505
        repeat
    Narrator "Il bouge dans la voiture, provoquant Jamie d'un air narquois."

    Atlas "[PCname], regarde la route!"

    Robyn "J'éssaie!!"

    ##TODO voice Jamie_ConsumeSoul
    Jamie "Je vais dévorer ton âme!!"
    $BM_State["arms"] = 0
    Taro "ATTENMEEOOOWW-!"
    $WolfAugust_State["head"] = 1
    $WolfAugust_State["eyes"] = 0
    $WolfAugust_State["hurt"] = 0
    show Driving Dawn Graphic:
        ease 0.6 xcenter 0.1 ycenter -0.8 rotate -720 yzoom 2.0 xzoom 0.7
    camera:
        matrixcolor TintMatrix("#abbdeb")
        ease 0.5 matrixcolor TintMatrix("#ffffff")
    show BG Road Side:
        matrixcolor TintMatrix("#ffffff")
        ease 0.5 matrixcolor TintMatrix("#abbdeb")

    show blobhouse:
        matrixtransform RotateMatrix(0,0,0)
        ease 0.6 xcenter 0.5 yoffset 700 matrixtransform RotateMatrix(0,0,800) yzoom 2.0 xzoom 0.7

    show wolfaugust:
        xcenter 0.5
        yoffset 700
        matrixcolor SaturationMatrix(0.4)*TintMatrix("#2b2a37")
        ease_bounce 0.3 yoffset 0

    show WGusEyeglow:
        xanchor 0.5
        zoom 0.18
        ycenter 0.66
        xcenter 0.5
        yoffset 700
        ease_bounce 0.3 yoffset 0
    Narrator "Une figure gigantesque se tient devant la route, observant le regard vide la voiture qui l'approche. Atlas attrape le volant et le tourne violament."

    Everyone "A.,a.,a.,h.,h.,h.,!"

    Narrator "La voiture s'arrète en avant alors que tu appuis sur le frein."

    jump Ch1_Start
