# Characters go there

# Good-looking italic
init:
    $ config.font_replacement_map["DejaVuSans.ttf", False, True] = ("DejaVuSans-Oblique.ttf", False, False)

define inner_thoughts = Character(None, what_italic = True) 


define you = Character("You")

define smoker = Character("Bare-foot smoker")

define uni_employee = Character("Uni employee")

define victory = Character("Victory!")

define defeat = Character("Defeat...")

define dean = Character("The Dean")

define gamelab_member = Character("???")

define teacher = Character("Undefind teacher")


image outdoor = "outdoorHD.png"

image uni = "uniHD.png"

image uni_hall = "uni_hallHD.png"

image upstairs = "upstairsHD.png"

image useless_employee = "useless_employeeHD.png"

image dean = "deanHD.png"

image dean_computer = "dean_computerHD.png"

image door = "doorHD.png"

image brown = "brownHD.png"

image brown_computer = "brown_computerHD.png"

image basement = "basementHD.png"

image gamelab = "gamelabHD.png"

image cafeteria = "cafeteriaHD.png"

image classroom = "classroomHD.png"

image riot = "riotHD.png"

image library = "libraryHD.png"

image zombies = "zombiesHD.png"

image award = "awardHD.png"

## This function is used when the user clicks the "Delete Permanent Data" button.
init python:
    def clear_variables():
        persistent.frustrated = False
        persistent.upstairs = False
        persistent.uni_employee_pissed = False
        persistent.first_ask= False
        persistent.revenge = False
        persistent.key = False
        persistent.banana = False
        banana_placed = False
        persistent.attend_class = 0
        persistent.homework = False
        return