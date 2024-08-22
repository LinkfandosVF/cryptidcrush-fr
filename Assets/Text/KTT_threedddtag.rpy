

init python:
    class ThreeDText(renpy.Displayable):
        def __init__(self, child, col_0, col_1, col_2, **kwargs):
            super(ThreeDText, self).__init__(**kwargs)
            if col_0 != None:
                self.base_child = Text("{" + col_0 + "}" + child)
            else:
                self.base_child = Text(child)
            self.child_1 = Text("{color=" + col_1 + "}" + child)
            self.child_2 = Text("{color=" + col_2 + "}" + child)

        def render(self, width, height, st, at):
            child_render = renpy.render(self.base_child, width, height, st, at)
            col_1_render = renpy.render(self.child_1, width, height, st, at)
            col_2_render = renpy.render(self.child_2, width, height, st, at)

            self.width, self.height = child_render.get_size()
            render = renpy.Render(self.width, self.height)
            render.subpixel_blit(col_1_render, (renpy.random.randint(-3,-2), renpy.random.randint(2,3)))
            render.subpixel_blit(col_2_render, (renpy.random.randint(2,3), renpy.random.randint(-3,-2)))
            render.subpixel_blit(child_render, (0, renpy.random.randint(0,1)))

            renpy.redraw(self,0.25)
            return render

    # Expects 2 Colors seperated by an @.
    # Example: {ddd=#00ff00-#00f}Text{/ddd}
    def threeddd_tag(tag, argument, contents):
        new_list = [ ]
        col1,_,col2 = argument.partition('-')
        my_style = DispTextStyle()
        for kind,text in contents:
            if kind == renpy.TEXT_TEXT:
                for char in text:
                    if 'color' in my_style.tags and my_style.tags['color'] != None:
                        temp = my_style.tags['color']
                        my_style.tags.pop('color')
                        char_disp = ThreeDText(my_style.apply_style(char), temp, col1, col2)
                        my_style.tags['color'] = temp
                    else:
                        char_disp = ThreeDText(my_style.apply_style(char), None, col1, col2)
                    new_list.append((renpy.TEXT_DISPLAYABLE, char_disp))
            elif kind == renpy.TEXT_TAG:
                if not my_style.add_tags(text):
                    new_list.append((kind, text))
            else:
                new_list.append((kind,text))
        return new_list

    config.custom_text_tags["ddd"] = threeddd_tag
