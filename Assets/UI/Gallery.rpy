init -10 python:
    class GalleryPicture():
        def __init__(self, name = "Picture Name", desc = "This is a description",artist = "Mikey", imgpath = "images.png", slot = 0):
            global maxThumbSize
            self.name = name
            self.desc = desc
            self.artist = artist
            self.imgpath = imgpath
            self.thumbnail = self.ResizePicture(maxThumbSize)
            self.slot = slot


        def ResizePicture(self, maxSize): ##Works!

            xscale,yscale = renpy.image_size(self.imgpath)
            xscale = float(xscale)
            yscale = float(yscale)
            #renpy.say(Narrator, str(xscale) +" "+ str(yscale))
            #xscale, yscale = renpy.image_size(imgpath)
            if xscale >= yscale:
                ymult = float(yscale/xscale)
                xscale = limitValue(maxSize,1,config.screen_width)
                yscale = xscale * ymult
            else:
                xmult = xscale/yscale
                yscale = limitValue(maxSize,1,config.screen_height)
                xscale = yscale * xmult

            #renpy.say(Narrator, str(xscale) +" "+ str(yscale))

            return im.Scale(self.imgpath, xscale, yscale)
        def FullScreenResize(self):

            xscale,yscale = renpy.image_size(self.imgpath)
            xscale = float(xscale)
            yscale = float(yscale)

            if yscale > config.screen_height:
                xmult = xscale/yscale
                yscale = config.screen_height
                xscale = yscale * xmult

            if xscale > config.screen_width:
                ymult = float(yscale/xscale)
                xscale = config.screen_width
                yscale = xscale * ymult


            #renpy.say(Narrator, str(xscale) +" "+ str(yscale))

            return im.Scale(self.imgpath, xscale, yscale)

    class Gallery():
        def __init__(self):
            self.GPics = []


        def orderBy(self,pic):
            return pic.slot

        def AddPicture(self, galPic): ##When adding a picture, if a slot is the same, the picture gets updated instead with the new values. ALSO WORKS

            CheckForPic = next((x for x in self.GPics if x.slot == galPic.slot), None) ##Get index of picture if picture with the same slot already exists, otherwise return None
            if CheckForPic == None:
                self.GPics.append(galPic)
                self.GPics.sort(key=self.orderBy)
            else:
                self.GPics[self.GPics.index(CheckForPic)] = galPic

    def refreshGallery():
        renpy.show_screen("GalleryPictures")
        #renpy.restart_interaction()




default unlockedImages = ["Hiking Trail","Title"]
define galleryStorage = Gallery()
define maxThumbSize = 225 ##Change this value to change how big the thumbnails will look
define maxShowcaseSize = 900 ##Change this value to change how big the pictures will look when displayed
define maxGalPicsX = 4 ##Changes the amount of pictures shown on the grid (x axys)
define maxGalPicsY = 2

init python:
    galleryStorage.AddPicture(GalleryPicture("Hiking Trail", "A hiking trail that August takes you down.", "Squidinu", "images/BGs/Chapter 1/hiking_trail.webp", 1))

    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Chapter 1/Road_Side_Sunset.webp", 2))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Chapter 1/Longhope_Library.webp", 3))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Graveyard/Graveyard Night.webp", 4))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Chapter 1/auggiecabin.webp", 5))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Camp/Lake_night.webp", 6))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/CGs/MM_Appears_CG.webp", 7))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/Props/Ch 0/DebbieCG.webp", 8))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/BGs/Chapter 1/dream_yard.webp", 9))
    galleryStorage.AddPicture(GalleryPicture("Title", "Description", "Artist", "images/CGs/Thanks_CG.webp", 10))

    #galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 3))
    #galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/BGs/Chapter 1/hiking_trail.webp", 4))
    #galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 5))
    #galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/BGs/Chapter 1/hiking_trail.webp", 6))
    #galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 7))
    #galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/BGs/Chapter 1/hiking_trail.webp", 8))
    #galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 9))
    #galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/BGs/Chapter 1/hiking_trail.webp", 10))


label InitializeGallery:
     ##Changes the amount of pictures shown on the grid (x axys)

    ## Notice how the numbers at the end are placed, that determines in what order theyll show at the gallery, so if you wanna add picture 1 and 3, theyll show beside one another
    ## but if you add picture with a number 2, itll show up in between the previous 2 pictures.
    ## using this with a gallery image with the same number will replace said image.
    Narrator "Test, adding pictures"
    #$galleryStorage.AddPicture(GalleryPicture("Devs say thanks!", "Dom and Mikey wish you\n to have a good game\n experience!", "@Squidinu", "images/CGs/Dev_Thanks.png", 0))

    #$galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 3))
    #$galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/CGs/Dev_Thanks.png", 5))
    #$galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 4))
    #$galleryStorage.AddPicture(GalleryPicture("Hello", "World", "Jos", "images/CGs/Dev_Thanks.png", 7))
    #$galleryStorage.AddPicture(GalleryPicture("World", "Hello", "Mike", "images/CGs/DM CG.webp", 6))
    return

screen Gallery_screen():
    tag menu
    zorder 0
    default currentGalleryPage = 0
    default galleryState = 0
    default chosenImage = GalleryPicture("No Name", "No desc", "No Artist", "images/BGs/Chapter 1/hiking_trail.webp", -1)

    use game_menu("Gallery")
    showif galleryState > 0:
        frame:
            at DarkCGShade_tf
            modal True
            background Solid("#000000")



    showif galleryState == 0:

        frame:
            background None
            ypos 25
            xpos 230

            grid maxGalPicsX maxGalPicsY:
                xfill True
                yfill True

                xmaximum 1000
                ymaximum 480

                for i in range(maxGalPicsX*maxGalPicsY):

                    if (currentGalleryPage*maxGalPicsX*maxGalPicsY)+i < len(galleryStorage.GPics) and galleryStorage.GPics[i].name in unlockedImages: ##Works!
                        ##add galleryStorage.GPics[i].imgpath #Works!
                        imagebutton at hovergrow:
                            idle galleryStorage.GPics[(currentGalleryPage*maxGalPicsX*maxGalPicsY)+i].thumbnail ##Works!
                            action [SetScreenVariable("galleryState", 1), SetScreenVariable("chosenImage", galleryStorage.GPics[(currentGalleryPage*maxGalPicsX*maxGalPicsY)+i])]
                            ##action showGalleryPicture(galleryStorage.GPics[(currentGalleryPage*maxGalPicsX*maxGalPicsY)+i])

                    else:
                       image "images/Characters/Dev Team/Ace/Ace_Bean.png":
                           zoom 0.3
                           alpha 0


        textbutton "Next Page":
            action SetScreenVariable('currentGalleryPage', currentGalleryPage+1)
            anchor (0.5,1.0)
            ypos 550
            xpos 900
            sensitive ((currentGalleryPage+1)*maxGalPicsX*maxGalPicsY) < len(galleryStorage.GPics)


        textbutton "Previous Page":
            action SetScreenVariable('currentGalleryPage', currentGalleryPage-1)
            anchor (0.5,1.0)
            ypos 550
            xpos 700
            sensitive currentGalleryPage >0



    elif galleryState ==1: ##Details
        frame:
            background None
            image chosenImage.ResizePicture(maxShowcaseSize):
                at truecenter
                xoffset -200
            text chosenImage.name:
                at truecenter
                xoffset 340
                yoffset -150
            text chosenImage.artist:
                at truecenter
                xoffset 340
                yoffset -110
            text chosenImage.desc:
                at truecenter
                xoffset 340
                yoffset -60
            textbutton "Return":
                at truecenter
                action SetScreenVariable("galleryState", 0)
                yoffset 200
                xoffset 340
            textbutton "FullScreen":
                at truecenter
                action SetScreenVariable("galleryState", 2)
                yoffset 200
                xoffset 450

    elif galleryState ==2: ##FullScreenPicture.
        imagebutton:
            at truecenter
            idle chosenImage.FullScreenResize()
            action SetScreenVariable("galleryState",1)





transform DarkCGShade_tf:

    alpha 0
    ease 0.75 alpha 0.5

    on show:
        alpha 0
        ease 1.0 alpha 0.6
    on hide:
        alpha 0.6
        ease 0.5 alpha 0



## --------- Old comments

#action [SetVariable('currentGalleryPage', currentGalleryPage+1),Function(refreshGallery)] ## "Solution" to the problem I had, making the game call a screen that DOES update, but i cant call that screen when
                                                                                           ## starting the game, so i have this frame thats exactly the same for the first page and dissappears when the page is changed
#showif currentGalleryPage == 0: ##Weird error I havent been able to work around, I cant update the screen with the gallery images, so I wanted to use a separate screen and "show" it every time
                                ##i change page (scentially refreshing it), but I cant call a screen inside a screen, and calling a function on the button that calls this screen to show the gallery pages
                                ##will show the gallery in the game, rather than on the new context, I can only refresh the pictures if I set the first page on the gallery screen and then refresh it on a separate screen
                                ##that gets disabled.
