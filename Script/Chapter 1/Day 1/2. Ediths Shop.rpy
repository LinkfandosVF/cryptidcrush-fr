default isSnooping = False

label Ch1_PotionShopVisit:
    camera:
        camera_default
        camera_zoom()
        shaded("#ffe7ee")

    python:
        timeText = "11:30AM"
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "4B", who_color = "aad8dd")
        musicPlayer.playSong(fadeOut=5.0)

    scene BG Black


    with Dissolve(0.75)

    #Could stand to be changed
    #Narrator "In spite of the array of strange artifacts and eerie curiosities, the inside of Edith’s shop has a surprisingly cozy atmosphere."
    Narrator "You follow Oz to the Hocus Health Center & Potions and enter to find an unexpectly cozy atmosphere."
    #smell, sight, sound

    Narrator "Alors que tu pénètre dans le magasin, tu admire l'étagère sur laquelle est déposée multiples bibelots et décorations."
    voice taro_meowc
    Taro "Aloooo? Y'a quelqu'un?"

    Narrator "Le contoir est vide et Oz est introuvable."
    python:
        Someone = Character("???", callback = Bleep,ctc="end_of_msg", cb_id = "2A", who_color = "#d5a0cb")
        adjustChar("Robyn",mouth=2,eyes=2,brow=0)

    scene BG Default:
        matrixcolor ColorizeMatrix("#1c1c1c","#77f6bd")

    show robyn:
        xcenter -0.5
        ease 2.0 xcenter 0.4

    show taro:
        xcenter -0.5
        ease 1.75 xcenter 0.6
        idleFloat(2,10)

    with Dissolve(0.5)

    Robyn "Uh,, il est passé où?"
    $musicPlayer.playSong(song="magic_birdbrain_song",fadeOut=1,fadeIn=3)
    voice thursday_cawe
    camera:
        camera_zoom(z=-550,x=300,y=235,t=1)

    show Thursday Smile:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.79
        yoffset 500
        ease 1.0 yoffset 273

    Someone "Peut-être puis-je aider?"

    Narrator "Se rapproche sur le sol un petit corbeau blanc."

    show Thursday Caw
    Someone "Edith s'occupe d'un autre patient,, donc je m'occupe du reste pour l'instant!"

    show Thursday Default
    voice taro_inquisitive
    show taro:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 0.6
        ease 1.25 matrixtransform RotateMatrix(0,0,220) xcenter 0.64
        block:
            ease 2.0 yoffset -10
            ease 2.0 yoffset 10
            repeat


    Taro "C'est qui ce tas de plumes?"
    show Thursday Smile

    Someone "Je me nome {b}Thursday{/b}, à votre service!"

    show Thursday Caw
    voice thursday_cawd
    Thursday "Je suppose que tu cherche un certain rouquin?"

    show Thursday Smile

    Thursday "Sur l'aile est! Je suis sur qu'il sera heureux de te voir."

    Narrator "{size=30}August est içi?{/size} \n\nTu est tout sauf prêt pour {sc=3}cette{/sc} conversation."

    Robyn "Ouais...{nw}"

    extend "\n\nVous auriez des charmes pour les chauchemards? J'ai un problème de {i}monstre{/i}."

    show Thursday Look
    voice thursday_cawi
    Thursday "Tu veux dire le chat avec les trois yeux hétérochromatiques?"
    voice taro_meowb
    python:
        Taro_State["pawR"] = 0
        Taro_State["pawL"] = 0
        Taro_State["eye"] = 0
        Taro_State["mouth"] = 2

    Taro "J'suis pas un monstre!"
    show Thursday Smile

    Thursday "Dans ce ças, ne t'inquète pas! Je suis sûr qu'Edith peut faire le chârme parfait pour ça."

    show Thursday Caw

    Thursday "Reprend tes occupations, je l'informerai de la situation."

    show Thursday Default

    Taro "Et je vais rester içi!...En sécurité."

    show Thursday Smirk

    Thursday "Très sécurisé."

    show robyn behind thursday zorder 1:
        ease 2.5 xcenter 1.3

    show Thursday Default zorder 0:
        matrixtransform RotateMatrix(0,0,0)
        pause 0.7
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    Narrator "Tu avance seul j'usqu'au second bâtiment. C'est pas grand chose,, après tout, tu a déja parlé à des gens avant!"
    jump Ch1_August_Hospital

label Ch1_August_Hospital:

    python:
        musicPlayer.playSong(fadeOut=5)
        Robyn_State["mouth"] = 5
        timeText = "NOON"

    scene BG OutsideHospital

    camera:
        camera_zoom()
        shaded("#ffe7ee")

    show robyn:
        xcenter -0.5
        pause 0.75
        ease 2.0 xcenter 0.5

    with Fade(0.5, 0.5, 0.5, color="#000000")

    Narrator "Tu t'arrète devant la dernière porte du couloir,, celle dans la quelle August se trouve."

    #$musicPlayer.playSong(fadeOut=5,fadeIn=5,song="supernatural_serenade_song")

    Narrator "Des voix étouffées peuvent être entendues depuis derrière la porte."

    $displaymenu = True
    Narrator "Tu écoute?{nw}"
    menu:
        extend ""

        "Ouais.":
            $displaymenu = False
            $isSnooping = True
            call dice_roll(rMod=PC_Stats.cStats("guts"), rDiff=8, rDesc="Snooping") from _call_dice_roll_5
            if not isRollSuccess:
                $isSnooping = False
                Narrator "Tu t'approche de la porte, mais n'a pas le courage de poser ton oreille contre celle-ci."

        "Non merci.":
            $isSnooping = False
            $displaymenu = False
            call dice_roll(rMod=PC_Stats.cStats("brains"), rDiff=5, rDesc="Restraint") from _call_dice_roll_6
            if not isRollSuccess:
                $isSnooping = True
                Narrator "Tu te retient d'écouter. La curiosité c'est un peu le truc qui t'a ammené pleins de problèmes."


    $UpsetSister = Character("???", image = "augustus", callback = Bleep,ctc="end_of_msg", cb_id = "8C", who_color = "#ee6756")
    if isSnooping:
        scene BG Black with Dissolve(0.3)
        $musicPlayer.playSong(fadeOut=5,fadeIn=5,song="supernatural_serenade_song")

        voice hazel_ifindyoureinthehospital
        UpsetSister "{size=30}Je me lève ce matin, et le premier truc que j'apprends c'est que tu est à l'hôpital?!{/size} \n\n C'est quoi ton problème??"

        voice august_iwasinwolfmode
        August "J'étais en mode loup!"

        voice hazel_youdontgettousethatexcuse
        UpsetSister "N'éssaie pas d'utiliser cette excuse avec moi!"

        voice august_youdontknowwhatitslike
        August "C'est pas des excuses! C'est juste-., \n\n\Tu ne sais même pas ce que ça fait."

        voice hazel_idontknowwhatitslike
        UpsetSister "{i}JE{/i} sais pas ce que ça fait? \n\n\ {size=30}Je vis avec toi et June!{/size}"

        voice august_moveout
        August "Si sa t'emmerde tant de vivre ici-., déménage! Vas vivre ailleurs!"

        voice hazel_whosgonnalookafterjune
        UpsetSister "{size=30}OUAIS?.,{/size} Et qui vas s'occuper de June? \n\nDieu merci d'empècher quelque chose de t'arriver à {b}toi.{/b}"

        voice august_stoptalkingaboutjune
        August "{size=35}Arrète de parler de June!{/size}"

        voice august_idontneedyourhelp
        August "Je t'ai pas demandé ton aide. J'ai pas BESOIN de ton aide!"

        voice hazel_okaymom
        UpsetSister "OKAY, {color=#ee6756}MAMAN{/color}. Ouais,, j'ai l'impression de l'entendre parler {sc}{color=#ee6756}ELLE!{/color}{/sc}"

        August "{sc}. . .{/sc}"

        voice august_pleasedontsaythathazel
        extend "\n\nS'il te plaît, ne dis pas ça, Hazel."

        voice hazel_okaysorry
        Hazel "Okay désolé,, putain."

        voice august_ishouldnthaveyelled
        August "Non ah, c'est bon,, j'aurais pas dû crier."

        voice hazel_gottagotoclass
        Hazel "Je dois aller en classe. Fait moi savoir quand tu sort de l'hosto."

    else:
        Narrator "Tu décide de ne rien faire.{nw}"
        voice mm_ringtonea

        extend " Après un moment, ton {color=#3bec27}portable vibre{/color}."
        $Robyn_State["armR"] = 1
        stop voice

        show CGShade

        show Atlas_Phone Ring CG:
            xcenter 0.5
            yoffset 700
            ease 0.5 yoffset 0
            on hide:
                yoffset 0
                ease 1.0 yoffset 700

        Narrator "C'est Atlas! Dieu merci,, un semblant de familiarité."

        call Ch1_AtlasPhoneConvo from _call_Ch1_AtlasPhoneConvo

        hide Atlas_Phone CG with None
        hide CGShade with { "master" : Dissolve(0.5) }
        Narrator "L'appel fini brusquement. \n\nIl fait tout le temps ça."

    scene BG OutsideHospital
    show robyn:
        xcenter 0.5

    with { "master" : Dissolve(1.0) }
    Narrator "Tu entends des bruits de pas en direction de la porte."

    show hazel:
        matrixtransform RotateMatrix(0,0,0)
        xcenter 1.5
        ease 2 xcenter 0.8

    python:
        adjustChar("Hazel",mouth=3,eyes=2,brow=0,collar=0)
    Narrator "Sortant de la chambre se trouve une jeune femme avec des cheuveux roux emmêlé et un bonnet noir."

    show robyn:
        ease 3.0 xcenter 1.3

    show hazel:
        ease 4.0 xcenter -0.3

    Narrator "Tu t'approches et toque à la porte.{nw}"

    #play sfx hurt_c
    #camera:
        #camera_shake
    extend "\n\nTu entends un gros bruit et des griffes glisser sur du mur."
    scene BG Hospital Room

    python:
        adjustChar("HalfAugust",mouth=6,eye=0,ear=2,eyeFrame=0,shirt=2,pants=0,brow=0,armR=1)
        Robyn_State["armR"] = 0
        musicPlayer.playSong(fadeOut=5,fadeIn=5,song="supernatural_serenade_song")

    camera:
        shaded("#ffe7ee")
        camera_zoom(x=150,y=-150,z=-500)

    show robyn:
        xcenter -0.5
        ease 1.5 xcenter 0.5

    show halfaugust:
        xcenter 0.7
        matrixtransform RotateMatrix(0,180,-16)

    with pixellate

    $adjustChar("HalfAugust",mouth=2,eye=1,ear=1)
    August "Grrrwuh? Hein?"

    show halfaugust:
        matrixtransform RotateMatrix(0,180,-16)
        ease 0.3 matrixtransform RotateMatrix(0,180,0)

    $adjustChar("HalfAugust",eye=2,mouth=1,brow=2,eyeFrame=0,ear=0,armR=0)
    Narrator "Tu à l'impression d'intérompre quelque chose."
    show robyn:
        xcenter 0.5
        ease 2.0 xcenter 0.4

    camera:
        camera_zoom(z=-305,y=-40,x=75,t=2.5)

    python:
        adjustChar("HalfAugust",brow=0,eyeFrame=1,eye=1)
        adjustChar("Robyn",eyes=3,mouth=0,brow=2)


    Robyn "Hey! Je voulais dire bonjour! \n\nEt m'excuser de,, t'avoir roulé dessus."

    python:
        adjustChar("HalfAugust",mouth=3,eye=0,eyeFrame=0)
        adjustChar("Robyn",eyes=2,mouth=0,brow=2)

    voice august_chuckle
    #show halfaugust:
        #unflipChar(0.4)
    show robyn:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)
        ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, -8.0)

    August "Hey t'inquète,, j'était déja {sc=3}{b}épuisé de toute façon!{/b}{/sc} \n\n{size=17}Eheheh, heh.{/size}"

    $adjustChar("Robyn",eyes=1,brow=0,mouth=5)
    $adjustChar("HalfAugust",eye=3)
    Narrator "Tu fronce les sourcils."

    #show halfaugust:
        #flipChar(0.4)

    python:
        adjustChar("HalfAugust",eye=2,eyeFrame=1,mouth=1)
        adjustChar("Robyn",eyes=2,mouth=0)

    August "Juuuuste, dit moi que t'a pas entendu tout le reste."

    $Robyn_State["eyes"] = 3
    if isSnooping:

        Narrator "Tu préfère ne pas avouer avoir écouté une conversation privé dans un hôpital."

        $HalfAugust_State['eye']= 2
        call dice_roll(rMod=PC_Stats.cStats("charm"), rDiff=8, rDesc="Lying, a bit.") from _call_dice_roll_7

    Robyn "Nope!"

    Robyn "Je suppose que c'était de la famille?"

    python:
        adjustChar("HalfAugust",eye=0,mouth=5)

    August "Ma soeur, ouais."

    $adjustChar("HalfAugust",mouth=2,eye=1,brow=2)
    August "Elle en a déja beaucoup sur le plateau,, avec l'école et., les trucs de famille."

    python:
        adjustChar("Robyn",mouth=5,brow=2,eyes=2)
        adjustChar("HalfAugust",mouth=1,eye=2)

    Robyn "Je ne peux qu'immaginer."

    August "Tu as vu Atlas? Il était avec toi?"

    python:
        adjustChar("Robyn",eyes=3,mouth=0,brow=0)


    Robyn "Ouais, il est resté chez moi cette nuit."

    python:
        adjustChar("HalfAugust",eye=0,mouth=6,brow=0,eyeFrame=1)
        adjustChar("Robyn",eyes=2,mouth=0)

    voice august_disappointed
    August "{sc=3}Wow.{/sc}"

    $adjustChar("HalfAugust",eye=3,eyeFrame=3,brow=1,mouth=2)
    August "Je suppose que c'était {i}vraiment{/i} la dernière option."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("HalfAugust",eye=1,eyeFrame=1,brow=2,mouth=1,ear=2)

    August "Surtout après l'incident de stroganoff."

    Narrator "Le quoi? Tu décide de garder la question dans ta tête."

    python:
        adjustChar("Robyn",eyes=2,mouth=5,brow=1)
        adjustChar("HalfAugust",eye=3,eyeFrame=1,mouth=2)

    August "Atlas veut pas m'écouter."

    python:
        adjustChar("HalfAugust",eyeFrame=1,mouth=0,eye=2)

    August "Qu'est-ce que je devrais faire?{nw}"

    menu:
        extend ""

        "Faites un truc marrant!":

            python:
                ch1_gusatlas_choice = 1
                adjustChar("Robyn",mouth=0,eyes=3,brow=0)
                adjustChar("HalfAugust",eye=0,mouth=1)

            Robyn "Pourquoi vous passez pas un peu de temps essemble? \n\nJe sais qu'Atlas aime le mini golf,, et puis vous pourriez manger une glace!"

            python:
                adjustChar("HalfAugust",eye=2,eyeFrame=0,mouth=3)
                adjustChar("Robyn",eyes=2,brow=1)

            August "C'est un peu tard cette saison pour ça,, mais je suis sur que on trouveras un truc."

        "Une conversation honnète.":
            python:
                ch1_gusatlas_choice = 2
                adjustChar("HalfAugust",eye=2,mouth=0)
                adjustChar("Robyn",mouth=0,brow=0,eyes=3)

            Robyn "Pourquoi ne pas essayer de communiquer et de vous expliquer en tant que colocataires? \n\nJe suis sur que vous vous sentirez mieux après."

            $adjustChar("HalfAugust",eye=0,mouth=6)
            August "C'est pas une mauvaise idée,, ouais."

        "N'y pense pas trop.":
            python:
                ch1_gusatlas_choice = 3
                adjustChar("HalfAugust",eye=2,mouth=1)
                adjustChar("Robyn",mouth=4,brow=1,eyes=1)

            Robyn "J'y ferais pas trop gaffe si j'était toi. S'il il y a un vrai problème, Je suis un peu près sur qu'Atlas viendrais te voir en premier."

            python:
                Robyn_State["mouth"] = 5
                adjustChar("HalfAugust",eye=1)

            August "Ouais,, t'as probablement raison. \n\nIl est toujours en avance sur moi."

    $adjustChar("HalfAugust",eye=3,mouth=2)
    August "Merci."
    voice august_sodoyouneedsomething
    $adjustChar("HalfAugust",mouth=3,eye=2,eyeFrame=0,brow=0,ear=0)

    August "Sinon, tu avais besoin d'un truc?"

    show halfaugust:
        ease 3.0 xcenter 0.73

    $adjustChar("HalfAugust",eye=1,mouth=0)
    Narrator "August tourne la tête et regarde la fenètre."
    python:
        adjustChar("Robyn",eyes=2,mouth=0,brow=0)
        HalfAugust_State['brow']= 0

    Robyn "J'était pas loin, donc j'ai pensé que je pourrais venir te voir."
    voice august_homebeforelunch
    python:
        adjustChar("HalfAugust",mouth=3,eye=3,brow=2,eyeFrame=3)

    August "Ah, c'est sympa. \n\n Je devrais rentrer avant midi."

    python:
        adjustChar("Robyn",mouth=5,brow=2,eyes=2)
        HalfAugust_State['mouth']= 0

    Robyn "Tant que ça?"

    $adjustChar("HalfAugust",mouth=5,eye=1,brow=0,eyeFrame=0)


    August "Je dois me barrer avant que le médecin revienne."
    $HalfAugust_State['mouth']= 1

    Robyn "Oz?"

    python:
        adjustChar("HalfAugust",mouth=2,eye=2,brow=1,armR=1,ear=1)
        adjustChar("Robyn",eyes=0,mouth=1,brow=1)

    August "Nan,, celui qui est {i}méchant{/i}. Ce matin elle m'a couru après avec des {sc=2}SERINGUES!{/sc}"

    python:
        adjustChar("Robyn",brow=2,eyes=1)
        HalfAugust_State['eye']= 2

    Robyn "On dirais que t'en à a te faire alors."

    $adjustChar("HalfAugust",armR=0,eye=0,eyeFrame=1,mouth=6,brow=1,ear=2)
    show halfaugust:
        ease 3.0 yoffset 0

    August "Rien que je puisse pas supporter."

    if isSnooping and not isRollSuccess:

        $adjustChar("Robyn",brow=0,eyes=3,mouth=0)
        Robyn "Je serais un peu stressé aussi si je devais vivre avec des loup-garou! \n\n Haha."

        python:
            Robyn_State["eyes"] = 0
            adjustChar("HalfAugust",eye=3,mouth=2,eyeFrame=0,brow=0)

        show halfaugust:
            blur 0
            ease 0.15 yoffset -35
            ease 0.15 yoffset 0

        Narrator "August hatèle."
        #voice line?
        voice august_weirdoshit
        python:
            adjustChar("HalfAugust",mouth=5,eye=2,brow=2,eyeFrame=1)
            Robyn_State["mouth"] = 5

        August "Donc tu {i}écoutait{/i}! C'est super chelou!"

        python:
            HalfAugust_State['mouth'] = 1
            adjustChar("Robyn",brow=2,eyes=1)

        Robyn "Désolé,, J-je-!"

        python:
            adjustChar("HalfAugust",eye=2,mouth=2)
            Robyn_State["eyes"] = 0

        show halfaugust:
            ease 0.5 xcenter 0.68

        August "On croirais entendre docteur Edith! Tu vas me demander des poils et des dents aussi? \n\nWhoo!"

        #[Fades to black]
        scene BG Black with Dissolve(1.0)

        Narrator "Vaincu, tu retourne dans l'entrée avec l'impression d'être le pire être sur terre."

        jump Ch1_BackToEdith

    Narrator "Tu n'es pas sur quoi dire ensuite.{nw}"

    menu:
        extend ""

        "Welp! Je ferais mieux de y aller!":

            python:
                adjustChar("Robyn",mouth=4,brow=1)
                HalfAugust_State['eye']= 0

            Robyn "On se vois plus tard."

            python:
                Robyn_State["mouth"] = 0
                adjustChar("HalfAugust",brow=3,eyeFrame=0,eye=2,mouth=3)

            August "Ca roule. J'me tire de là."

        "Donc t'es un loup-garou?":

            show halfaugust:
                blur 0
                ease 0.15 yoffset -35
                ease 0.15 yoffset 0

            python:
                adjustChar("HalfAugust",mouth=8,eye=3,brow=0,eyeFrame=0,ear=1)
                adjustChar("Robyn",mouth=1,brow=0,eyes=0)

            August "{size=30}GAH! Je {i}SAVAIS{/i} que t'allait demander!{/size}"

            show halfaugust:
                yoffset 0
                ease 0.5 xcenter 0.68

            $adjustChar("HalfAugust",eyeFrame=0,eye=2,brow=1,mouth=2,ear=2)

            August "T'était pas censé le découvrir comme ça."

            show halfaugust:
                ease 1.0 xcenter 0.64

            python:
                adjustChar("HalfAugust",mouth=0,eye=1,eyeFrame=1)
                adjustChar("Robyn",eyes=2,mouth=1,brow=0)

            August "J'aurais pu être {bt=3}{i}sombre et mysterieux!{/i}{/bt}"

            $adjustChar("HalfAugust",mouth=3,eye=3,eyeFrame=2,brow=2,sparkle=1,ear=0)

            show halfaugust:
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)
                ease 0.5 matrixtransform RotateMatrix(0.0, 0.0, 10.0)

            August "{i}{bt=3}Oh wow, que s'est il passé hier?{/bt}{/i}"

            August "Hein? Quel {b}loup-garou?{/b}"

            show halfaugust:
                matrixtransform RotateMatrix(0.0, 0.0, 15.0)
                ease 0.5 matrixtransform RotateMatrix(0.0, 180.0, -15.0)

            python:
                adjustChar("HalfAugust",mouth=4,brow=0,ear=1)
                adjustChar("Robyn",eyes=1,mouth=5,brow=1)

            August "C'est juste un mythe!"
            show halfaugust at startledSquish:
                matrixtransform RotateMatrix(0.0, 180.0, 0.0)

            $adjustChar("HalfAugust",eyeFrame=1,eye=1,brow=1,ear=0,mouth=2,sparkle=0)

            August "Mais non,, Je l'ai ruiné jour un."

            $adjustChar("Robyn",eyes=4,mouth=1,brow=0)
            Narrator "Est-ce que la Lycanthropie c'est un peu comme un jeu pour lui?"

            python:
                adjustChar("HalfAugust",eyeFrame=1,eye=2,brow=0,mouth=1)
                adjustChar("Robyn",eyes=1,mouth=4,brow=2)

            Robyn "Enfin, tu {b}vis{/b} dans une ville pleine de monstres,, donc y'a des chances que tu en soit un aussi."

            $Robyn_State["mouth"] = 5
            Robyn "Et puis-{nw}"

            menu:
                extend ""

                "T'avais l'air tellement mignon!":
                    python:
                        adjustChar("HalfAugust",brow=2,eyeFrame=0,eye=1,ear=1)
                        adjustChar("Robyn",eyes=3,mouth=0,brow=0)

                    show halfaugust:
                        blur 0
                        ease 0.15 yoffset -35
                        ease 0.15 yoffset 0

                    Robyn "Avec tout les poils orange? T'es adorable!"

                    $adjustChar("HalfAugust",eyeFrame=3,mouth=3,brow=2,eye=0,ear=0,blush=1)

                    show halfaugust:
                        yoffset 0
                        ease 1.0 xcenter 0.65

                    August "Grrrehehe,, mensonges. Tu sort de là!"

                    $adjustChar("Robyn",mouth=6,brow=1)
                    $adjustChar("HalfAugust",eye=2,eyeFrame=0,mouth=1)
                    show robyn:
                        blur 0
                        ease 0.15 yoffset -35
                        ease 0.15 yoffset 0
                        ease 0.15 yoffset -35
                        ease 0.15 yoffset 0

                    Robyn "Je suis honnète!"

                    camera:
                        pause 1.0
                        camera_shake

                    show halfaugust:
                        matrixtransform RotateMatrix(0,180,0)
                        ease 0.2 matrixtransform RotateMatrix(0,0,0) xcenter 0.7

                        parallel:
                            pause 0.2
                            ease 0.5 xcenter 1.5
                        parallel:
                            ease 0.2 yoffset 30 yzoom 0.8
                            ease 0.4 yoffset -180 matrixtransform RotateMatrix(0,0,100) yzoom 1.6

                    python:
                        adjustChar("HalfAugust",mouth=2,eye=0,eyeFrame=3,ear=3)
                        adjustChar("Robyn",brow=1,eyes=0,mouth=1)

                        musicPlayer.playSong()

                    play sfx ["<silence 1.0>", "audio/SFX Battle/Hurt_B.ogg"]
                    Narrator "August ouvre la fenètre de la clinique et saute dans l'ouverture."

                    $adjustChar("Robyn",eyes=1,mouth=5)
                    Robyn "Hein."

                "T'avais l'air super flippant!":
                    python:
                        adjustChar("Robyn",mouth=4,brow=1,eyes=0)
                        adjustChar("HalfAugust",brow=2,eye=1,mouth=3,eyeFrame=0,ear=1)

                    show halfaugust:
                        blur 0
                        ease 0.15 yoffset -35
                        ease 0.15 yoffset 0

                    Robyn "C'était flippant! J'ai cru que j'était fini."
                    show halfaugust:
                        yoffset 0
                        ease 1.0 xcenter 0.65
                    python:
                        adjustChar("Robyn",mouth=5,brow=0,eyes=2)
                        adjustChar("HalfAugust",eye=2,eyeFrame=1,mouth=8,ear=3)

                    August "Ca arriveras plus, promis. \n\nJ'sais pas ce qui m'arrive en ce moment."

                    $adjustChar("HalfAugust",eye=0,mouth=2)
                    August "Mais ca commence à me les briser."

                    $adjustChar("Robyn",eyes=3,mouth=0,brow=0)
                    Robyn "C'est pas grave,, on a tous des jours comme ça."

                    python:
                        adjustChar("Robyn",eyes=2,mouth=5)
                        adjustChar("HalfAugust",eyeFrame=0,eye=2,brow=3,mouth=3,ear=1)

                    August "{sc=2}Est-ce que t'est un...?{/sc}"

                    $adjustChar("Robyn",eyes=4,mouth=6,brow=2)
                    Robyn "Nan,, J'éssayait juste de faire le rapprochement."

                    $adjustChar("HalfAugust",mouth=0,brow=0,eyeFrame=3,ear=0)
                    August "J'y aurais cru!"

                    $adjustChar("Robyn",eyes=1,mouth=8)
                    Robyn "Ouais si tu le dit."

    scene BG Black with Dissolve(1.0)
    camera:
        camera_zoom()
    Narrator "Tu sorts vers l'entrée."

    jump Ch1_BackToEdith

label Ch1_AtlasPhoneConvo:
    voice atlas_heyc
    #$musicPlayer.playSong(fadeOut=5,fadeIn=5,song="astral_reflection")

    play music astral_reflection
    Atlas "T'aurais pas vu un mec avec des grosse cornes et une bouche énorme? Genre, piquant."

    Robyn "Heeeey,, r'gardez qui est enfin réveillé! \n\nMais non, J'ai vu personne comme ça récemment."

    Atlas "T'a regardé les égouts? Des cryptes peut-être?"

    Robyn "Vu que je suis ni un vampire, ni un alligator des égouts,, la réponse est non."

    Atlas "T'aimerais?"

    voice atlas_nervouslaugh
    Atlas "Regarder les égouts je veux dire."

    Robyn "Dégeu!"

    Atlas "Okay, okay. Garde ton cerveau vivant, \n\n{size=20}Je commence à flipper.{/size}"

    Robyn "Gros mec qui pique. Je retient."

    Atlas "Cool! M-merci,, c'est sympa. Reste vivant,, prends soin de toi!"

    Robyn "Attends, tout vas bien?"

    Atlas "{size=40}OUAIS!{/size} \n\n Tout vas super bien."

    stop music fadeout 0.5

    return

label Ch1_BackToEdith:
    camera:
        camera_default
        camera_zoom()
        shaded("#ffe7ee")

    python:
        musicPlayer.playSong()
        adjustChar("Robyn",mouth=0,brow=1,eyes=2)

    scene BG OutsideHospital

    show robyn:
        xcenter -0.5
        ease 2.0 xcenter 0.35

    show taro:
        xcenter 1
        ease 1.75 xcenter 0.5
        idleFloat(2,10)

    with Dissolve(1.0)
    Taro "Tu est de retour en un morceau! \n\nAlors comment ca c'est passé?"

    if isSnooping and not isRollSuccess:

        Robyn "J'crois j'ai tapé dans un truc personel."

        Taro "Oh? Allez crache le morceau!"

        $adjustChar("Robyn",mouth=5,brow=2,eyes=1)
        Robyn "Je devrais vraiment pas."

        Taro "Raah allez!"

    else:

        $adjustChar("Robyn",mouth=5,brow=2,eyes=1)
        Robyn "Ca vas. Je me sens toujours comme un étron, mais August à pas l'air de s'en faire."

        Taro "Genre se faire rentrer dedans par une force de 2 tonnes?"

        Robyn "Ouais. C'était un peu génant."

    $adjustChar("Robyn",mouth=4,brow=2,eyes=2)
    Robyn "Est-ce que Thursday t'a renvoyé?"

    $Taro_State["mouth"] = 2
    Taro "Mw'ouais, Je m'ennuyait. \n\nOz à gagné la bataille de regards."
    python:
        adjustChar("Taro",eye=2,mouth=3)
        adjustChar("Robyn",mouth=1,brow=0)

    Narrator "Les poils de Taro s'érrisent."

    scene BG Black with nwDissolve(0.75)
    Taro "Par contre je crois j'ai oublié un truc. \n\nAttends ici."

    python:
        musicPlayer.playSong(song="thaumaturgy_thursdays_song",fadeOut=1,fadeIn=3)
        timeText = "12:00PM"


    voice edith_everythingweneed
    Edith "On dirais que t'a trouvé tout ce dont on avait besoin."
    voice thursday_indeedb
    Thursday "En effet."

    voice edith_didanyoneseeyou
    Edith "Est-ce que quelqu'un t'a vu?"

    Oz "..."

    voice edith_mouthshut
    Edith "Tu à intérêt à l'avoir fermé."

    voice oz_growlc
    Oz "{sc}-!{/sc}"

    voice edith_shootsorry
    Edith "Merde,, pardon je voulais pas—"

    voice thursday_contact
    Thursday "T'a contacté les autres?"

    voice edith_nowwewait
    Edith "Oui, et maintenant, on attends."

    voice oz_hmshort
    Oz "{sc}-?{/sc}"

    voice thursday_saturday
    Thursday "Samedis."

    voice taro_whatreyoutalkingabout
    Taro "De quoi vous parlez?"
    scene BG Default:
        matrixcolor ColorizeMatrix("#1c1c1c","#77f6bd")

    camera:
        camera_zoom(z=-150,y=-60)

    show oswald at startledSquish:
        xcenter 0.8

    show Thursday Caw behind oswald:
        yoffset -260
        xcenter 0.8
        ease 0.2 yoffset -290
        ease 0.2 yoffset -260

    show edith:
        xcenter 0.75

    show taro:
        xcenter 0.25
        idleFloat(2,10)

    python:
        adjustChar("OH",eyeFrame=1,eyes=0,armR=0,armL=0,brow=0)
        adjustChar("Taro",eye=1,mouth=2)
        adjustChar("Edith",eye=1,eyeFrame=1,brow=4)

    with Dissolve(0.3)

    voice thursday_cawb
    Thursday "{size=40}Gwuah!{/size}\n\nRien du tout!"
    voice taro_uhuha
    python:
        adjustChar("Edith",eyeFrame=0,eye=1)
        OH_State["eyeFrame"] = 0
        Taro_State["eye"] = 2

    Taro "Rien? Alors y'a quoi ce weekend?!"

    $adjustChar("Edith",eye=0,brow=0,mouth=2)
    voice edith_gether
    Edith "Um... \n\nOzzie., choppe là."

    show oswald:
        ease 0.3 xcenter 0.6
    show Thursday Default:
        ease 0.3 xcenter 0.6

    python:
        adjustChar("OH",brow=3,eyes=5)
        adjustChar("Taro",mouth=1,eye=2)

    Oz "..."
    camera:
        camera_zoom(z=-350,y=-30,x=-130,t=0.3)

    python:
        adjustChar("Taro",mouth=3,eye=3,pawR=2,pawL=1)
        adjustChar("OH",armL=6,armR=0,eyes=3,eyeFrame=1,drool=1,brow=0)
        musicPlayer.playSong(song="the_unwelcome_visitor")

    show oswald:
        ease 0.3 xcenter 0.4

    show Thursday Default:
        ease 0.35 xcenter 0.4

    show taro:
        matrixtransform RotateMatrix(0.0, 0.0, -6.0)
        xcenter 0.25
        block:
            ease 0.05 xoffset -5
            ease 0.1 xoffset 5
            ease 0.1 xoffset -5
            ease 0.1 xoffset 5
            ease 0.05 xoffset 0
            repeat


    voice oz_growlc
    Taro "NON ME CHOPPE PAS!" with hpunch

    camera:
        camera_zoom(z=-195,y=-10,t=1.0)

    python:
        musicPlayer.playSong()
        adjustChar("Edith",mouth=1,brow=1,eye=1)

    voice edith_jk
    Edith "J'rigole."

    $adjustChar("Edith",eye=0,brow=0)

    voice edith_hurtanybody
    Edith "Ozzie ferais pas de mal à une mouche,, pas vrai mon grand?"

    show taro:
        ease 0.1 xoffset 0
        idleFloat(2,10)

    python:
        musicPlayer.playSong(song="thaumaturgy_thursdays_song",fadeOut=1,fadeIn=3)
        adjustChar("OH",eyes=1,brow=1,eyeFrame=0)
        Edith_State["brow"] = 2

    show oswald:
        ease 3.0 yoffset 60
    show Thursday Look:
        ease 2.5 yoffset -160

    voice oz_ugh
    Oz "{sc=4}...{/sc}"

    python:
        adjustChar("Edith",mouth=2,eye=1)
        adjustChar("Taro",eye=1,pawR=1,pawL=1)

    show robyn behind taro:
        xcenter -1
        ease 3.0 xcenter 0.15
    voice taro_hiss
    Taro "Ugh! Vous êtes les pire!"

    python:
        adjustChar("OH",eyes=0,eyeFrame=1,brow=0)
        Edith_State["eyeframe"] = 1

    Robyn "Um, tu fesais quoi?"

    show oswald:
        matrixtransform RotateMatrix(0.0, 0.0, -8.0)
        xcenter 0.7 yoffset 35
        ease 0.05 xoffset -5
        ease 0.1 xoffset 5
        ease 0.1 xoffset -5
        ease 0.1 xoffset 5
        ease 0.05 xoffset 0

    show Thursday Caw:
        matrixtransform RotateMatrix(0.0, 180.0, -6.0)
        xcenter 0.7 yoffset -210
        ease 0.05 xoffset -5
        ease 0.1 xoffset 5
        ease 0.1 xoffset -5
        ease 0.1 xoffset 5
        ease 0.05 xoffset 0

    python:
        adjustChar("OH",eyeFrame=0,eyes=5,drool=0,brow=3,armL=0)
        adjustChar("Edith",eyeframe=0,mouth=0)

    Narrator "Oz recule alors que tu approche."
    voice thursday_cawh
    Thursday "Salut humain!"

    show Thursday Default

    python:
        adjustChar("Edith",brow=0,mouth=0)
        adjustChar("OH",brow=1,eyes=0)
        adjustChar("Taro",pawR=1,pawL=0,eye=0)

    voice edith_hmph
    Edith "T'es celui qui à mis le chien-chien à l'hosto? Wow. C'est brûtal."

    python:
        OH_State["eyes"] = 1
        adjustChar("Robyn",mouth=4,brow=1,eyes=0)

    show robyn behind taro:
        xcenter 0.15
        ease 3.0 xcenter 0.4

    show oswald:
        ease 3.0 xcenter 0.75

    show Thursday Default:
        ease 3.0 xcenter 0.75

    Robyn "C'était un accident."

    python:
        adjustChar("Edith",brow=1,eye=0,mouth=0)
        adjustChar("Robyn",mouth=5,brow=0)

    Edith "Pas besoin de jouer sur la défensive,, Je comprends. Cette ville doit être super dangereuse pour un humain. \n\nAvec des monstres comme nous un peu partout."

    python:
        adjustChar("Edith",eyeFrame=0,brow=0,eye=1)
        adjustChar("OH",eyeFrame=1,brow=0,eyes=6)
        Taro_State["eye"] = 2
        adjustChar("Robyn",eyes=1,mouth=3,brow=4)

    show robyn:
        xcenter 0.4
        ease 3.0 xcenter 0.35

    Robyn "Est-ce que t'es genre, un {i}vrai{/i} docteur?"

    $adjustChar("Edith",mouth=1,armR=1)
    $adjustChar("OH",eyes=5)
    $Robyn_State["brow"] = 0

    Edith "Je porte la blouse, non?"
    $adjustChar("Edith",mouth=2,eye=0,brow=2)

    Edith "Bref, Je suis Edith, et ça c'est mon magasin."

    $adjustChar("Robyn",eyes=4,mouth=5)
    Taro "{size=20}{i}J'lui fait pas confiance.{/i}{/size}"

    Robyn "{size=20}{i}Mais Madhouse oui,, Je crois.{/i}{/size}"

    python:
        Taro_State["eye"] = 0
        adjustChar("Edith",brow=2,mouth=0,eye=3)
        OH_State["eyeFrame"] = 0
        Robyn_State["eyes"] = 2

    Edith "Donc,, un petit oiseau m'as dit que t'avais des cauchemards."

    show Thursday Caw behind oswald:
        yoffset -210
        xcenter 0.75
        ease 0.2 yoffset -220
        ease 0.2 yoffset -210

    voice thursday_facepalm

    Thursday "C'est moi!"

    $adjustChar("Edith",mouth=1,eye=1,armR=0)
    show Thursday Default
    Edith "Tient, ça devrais aider."

    show CGShade:
        on hide:
            ease 0.5 alpha 0
    show Charm_Bracelet:
        on hide:
            yoffset 0
            ease 1.0 yoffset 700

    Narrator "Edith t'envoies un petit bracelet fait de perles. Il est un peu chelou, mais on vois qu'il à été fait avec amour."

    Edith "Il est pas mignon? J'adore faire ces trucs."

    python:
        OH_State["eyes"] = 4
        adjustChar("Robyn",eyes=3,mouth=0)

    Robyn "J'aime trop! Merci."

    python:
        adjustChar("OH",eyes=5,brow=1)
        adjustChar("Taro",eye=1,mouth=0)
        Edith_State["eye"] = 0

    Taro "Super.,Moche."

    $adjustChar("Edith",mouth=2,brow=0)

    Edith "Ecoute minou,, Je sais que c'est Sketchy, mais ça c'est la version portable d'un {i}sort de protection.{/i}"
    voice taro_meowf
    $adjustChar("Taro",eye=2,mouth=3)
    hide Charm_Bracelet with None
    hide CGShade with nwDissolve(0.5)
    Taro "Et ça fait quoi?"

    python:
        adjustChar("Edith",mouth=4,eye=1,eyeframe=1,armR=1)
        Taro_State["eye"] = 1

    show edith:
        matrixtransform RotateMatrix(0.0, 0.0, -8.0)
        xcenter 0.75 yoffset 0
        ease 0.05 xoffset -5
        ease 0.1 xoffset 5
        ease 0.1 xoffset -5
        ease 0.05 xoffset 0

    Edith "Beh, c'est un porte bonheur., ça te \n\n{sc=2}{b}protège!{/b}{/sc}"

    python:
        adjustChar("Robyn",eyes=2,mouth=4)
        adjustChar("Edith",eyeframe=0,eye=1,mouth=0,armR=0,brow=2)

    show edith:
        matrixtransform RotateMatrix(0.0, 0.0, 0.0)

    Robyn "Combien je te dois?"
    voice edith_sigh

    python:
        adjustChar("Edith",eye=2,mouth=0)
        OH_State["eyes"] = 1
        Robyn_State["mouth"] = 5

    Edith "Oh,, disons juste que tu me dois une {i}faveur.{/i}"

    $Edith_State["eye"] = 0

    Edith "L'argent compte pas beaucoup pour moi."

    if isSnooping and not isRollSuccess:
        Narrator "C'est ça qu'August disais quand il parlait de poils? Dents? \n\nTu flippes un peu."

        $adjustChar("Robyn",eyes=4,mouth=3)
        Robyn "Je vais heu. Garder ça en tête."
    else:
        $Robyn_State["mouth"] = 0
        Robyn "O-oh! Okay, si tu veux."

    $adjustChar("Edith",eyeFrame=0,brow=0,eye=2)

    show Thursday Caw:
        matrixtransform RotateMatrix(0.0, 180.0, -6.0)
        xcenter 0.75 yoffset -200
        ease 0.05 xoffset -5
        ease 0.1 xoffset 5
        ease 0.1 xoffset -5
        ease 0.1 xoffset 5
        ease 0.05 xoffset 0.75

    voice thursday_surpriseb
    Thursday "Moi j'adore l'argent!"

    voice oz_laughc
    $adjustChar("OH",eyes=4,brow=0)
    Narrator "Oz acquiesce de la tête."

    voice edith_hmph

    show Thursday Smile

    python:
        adjustChar("Edith",eye=0,mouth=3)
        OH_State["eyes"] = 1

    Edith "Ignore le,, Thursday pense que tout ce qui brille est de l'Or. \n\n Et Oz,, et bien,, probablement pas mais qui sait."

    Robyn "Donc vous travaillez ensemble?"

    python:
        adjustChar("Edith",brow=2,eye=1,mouth=0)
        adjustChar("Robyn",eyes=2,mouth=0)
        OH_State["eyes"] = 5

    Edith "On est associés"

    show Thursday Caw:
        matrixtransform RotateMatrix(0.0, 180.0, -6.0)
        xcenter 0.75 yoffset -200
        ease 0.05 xoffset -5
        ease 0.1 xoffset 5
        ease 0.1 xoffset -5
        ease 0.1 xoffset 5
        ease 0.05 xoffset 0

    Thursday "Yeowch, c'est tout?"

    $adjustChar("Edith",mouth=2,eye=0,brow=0)
    show Thursday Default

    Narrator "Tu a juste à demander—{nw}"

    menu:
        extend ""

        "Y'a quoi entre vous, {i}pour de vrai?{/i}":
                call dice_roll(rMod=PC_Stats.cStats("charm"), rDiff=9, rDesc="Persuasion") from _call_dice_roll_31

                if isRollSuccess:
                    python:
                        adjustChar("OH",eyes=1,brow=1)
                        adjustChar("Edith",eye=2,mouth=1)
                        adjustChar("OH",brow=0)

                    Edith "Comme je vient de le dire,, on est associés."

                    show Thursday Smile:
                        matrixtransform RotateMatrix(0.0, 180.0, -6.0)
                        xcenter 0.75 yoffset -200
                        ease 0.05 xoffset -5
                        ease 0.1 xoffset 5
                        ease 0.1 xoffset -5
                        ease 0.1 xoffset 5
                        ease 0.05 xoffset 0

                    Thursday "MECHANT!"

                    show Thursday Default
                    python:
                        adjustChar("Edith",mouth=0,eye=0,brow=3)
                        OH_State["eyes"] = 5

                    Edith "J'ai sorti Ozzie d'une méchante situation. Maintenant il travaille pour moi,, à collecter des faveurs..."

                    Taro "Genre un {b}ésclave.{/b}"

                    voice oz_hurtf
                    python:
                        adjustChar("Edith",mouth=1,eye=2,brow=1,eyeFrame=0,armR=1)
                        adjustChar("OH",brow=1,eyes=4)

                    Edith "Yeah, bien sur, si c'est son truc~"

                else:
                    Edith "Rien d'intérrésant. Et puis c'est un peu personel, non?"



        "Pourquoi le nom Thursday?":
            $adjustChar("Edith",mouth=1,eye=1,brow=2)
            Edith "Il est né un Jeudi."

            Thursday "J'aurais pu jurer que c'était plus profond."

            Edith "Nope, deux heures de plus et c'était Vendredi."

            Thursday "Vous êtes tous nul avec les noms!"

        "Pourquoi tu m'aides?":
            $adjustChar("Edith",mouth=0,eye=1,brow=2)
            Edith "Pourquoi pas."

            show Thursday Caw:
                matrixtransform RotateMatrix(0.0, 180.0, -6.0)
                xcenter 0.75 yoffset -200
                ease 0.05 xoffset -5
                ease 0.1 xoffset 5
                ease 0.1 xoffset -5
                ease 0.1 xoffset 5
                ease 0.05 xoffset 0

            voice thursday_cawd

            Thursday "Même si tu à refusé de signer les papiers!"
            python:
                adjustChar("Edith",eye=5,mouth=1)
                adjustChar("OH",eyes=4,brow=4)

            Edith "Et puis, J'ai jamais vu Ozzie parler autant."
    python:
        adjustChar("Edith",eye=1,eyeFrame=1,brow=4)
        adjustChar("OH",eyeFrame=0,brow=0,eyes=1)

    Edith "Serieux par contre, tu ferais mieux d'y aller,, tu coupe ma pause déjeuner."

    scene BG Black with Dissolve(1.0)

    voice thursday_angryd
    Thursday "'Ey boss, votre chien s'est échappé!"

    Edith "Ne l'appelle pas comme-ça!"

    jump Ch1_LibraryIntro
