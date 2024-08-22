transform zoomfade(duration=1.0,bg="BG Black", new_widget=None, old_widget=None):
    delay duration

    #Background
    contains:
        #Center it
        xcenter 0.5
        ycenter 0.5
        xysize (1280,720)
        bg

    #Old Image
    contains:
        #Center it
        xcenter 0.5
        ycenter 0.5

        #Old Image
        old_widget
        events False

        #Zoom Out
        zoom 1.0
        alpha 1
        matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)
        ease 0.2*duration zoom 0.8 matrixcolor ColorizeMatrix("#12581f","#9efbaf")*SaturationMatrix(0)
        pause 0.4*duration

        #Disappear when covered
        ease 0.2*duration alpha 0
        events True

    #New Image
    contains:
        #Center it
        xcenter 0.5
        ycenter 0.5

        #Invisible
        events False
        pause  0.3*duration

        #Appear Zoomed out
        alpha 0
        zoom 0.8
        matrixcolor ColorizeMatrix("#12581f","#9efbaf")*SaturationMatrix(0)

        new_widget
        events True

        ease 0.2*duration alpha 1

        pause 0.1*duration

        #Zoom back in
        ease 0.4*duration zoom 1.0 matrixcolor ColorizeMatrix("#000000","#ffffff")*SaturationMatrix(1)
