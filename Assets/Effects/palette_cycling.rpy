"""
 Wave Rendering Ren'Py Module
 2021 Daniel Westfall <SoDaRa2595@gmail.com>

 http://twitter.com/sodara9
 I'd appreciate being given credit if you do end up using this! :D Would really
 make my day to know I helped some people out!
 http://opensource.org/licenses/mit-license.php
 Github: https://github.com/SoDaRa/WaveRendering
 itch.io: https://wattson.itch.io/renpy-wave-rendering
"""
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


init python:
    class PaletteCycler(renpy.Displayable):
        # file_path: (String) A file path to the images that'll be used. Should be numbered 0,1,2,etc and should be the length of palette + 1 or more.
        #                     0 Should be the base image that will remain unaltered. 1-n will be the entries that cycle through the palette.
        # file_end:  (String) The file extension of the images. ie. ".png", ".jpg", ".webp"
        # palette:   (List of Strings) A list of strings for all the images used in the palette.
        # nFiles = Number of files you have (excluding the base)
        def __init__(self, file_path, file_end, palette,nFiles=1,hasBase = True,pDelay=15, *args, **kwargs):
            super(PaletteCycler, self).__init__(*args, **kwargs)
            self.width, self.height = 0,0
            self.hasBase = hasBase
            self.csDelay = pDelay

            if self.hasBase:
                self.base = Image(file_path + "0" + file_end) # The base image
            else:
                self.base = Image(file_path + "1" + file_end) # The base image

            self.col = []
            for i in range(1,nFiles):
                self.col.append(file_path + str(i) + file_end) # Load up all the file names for the background
            self.palette = palette                             # The color palette we'll cycle through

        def render(self, width, height, st, at):
            offset = int((st/float(self.csDelay*0.01)) % len(self.palette))                    # Updates which palette entry we're on every tenth of a second


            base_render = renpy.render(self.base, width, height, st, at) # The base image render
            self.width, self.height = base_render.get_size()             # Get the size of the new render we want to create, based on the base image
            render = renpy.Render(self.width, self.height)               # Generate that render

            if self.hasBase:
                render.blit(base_render, (0,0))                              # Apply the base render
            for img in self.col:
                # Loop through the palette and pixel images, applying each in sequence
                # Only uses the black part of colorize so images are 1-to-1 with the palette.
                col_render = renpy.render(im.MatrixColor(img, im.matrix.colorize(self.palette[offset], "#000")), self.width, self.height, st, at)
                render.blit(col_render, (0,0))
                offset = (offset + 1) % len(self.palette)
            renpy.redraw(self, 0) # Request redraw
            return render         # Output our new render


init python:
    palCycle = ["#2d1f5e","#621bbb","#cb01e4","#e90185","#e16b00","#fac80a","#b9ee02","#55e71d","#3dfc89","#0efbe6","#0e5ffb","#220efb","#621bbb","#2d1f5e","#201a3a"]

image EB_BG1:
    contains:
        xzoom 1.25
        yzoom 1.25
        xcenter 0.5
        ycenter 0.5
        PaletteCycler("/images/BGs/Chapter 1/EB/Colorful Lines", ".png", palCycle,nFiles=7,hasBase = True,pDelay=10)
        #WaveImage(PaletteCycler("/images/BGs/Chapter 1/EB/Colorful Lines", ".png", palCycle,nFiles=7), amp = 40, strip_height = 3,melt=True,freq=20)
