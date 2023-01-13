## This script was created by Angel Seraph and is available here : https://glsuoa.itch.io/renpy-achievements

python early:


    class Achievement(NoRollback):
        def __init__(self, name='', image='', message='', **kwargs):
            self.name = name
            if image == '':
                ## If image is None, we will give a default image.
                self.image = Transform('gui/trophy_icon.png', fit='contain')
            else:
                self.image = Transform(image, fit='contain')
            self.message = message


        def __eq__(self, value):
            """
            Since we are using a persistent list we need to do an equality
            check.

            Below we are simply checking 'self.name == value.name, self.message == value.message'
            """
            return all((self.name == value.name, self.message == value.message))

        def add(trophy):
            """
            Add/Grant Trophies/Achievements to the list.

            As a standard python expression  ::  Achievement.add( <trophy> )
            As a screen action  ::  Function( Achievement.add, <trophy> )
            """
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                ## New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)

        def purge(self):
            """
            This will clear the achievements AND persistent list.

            As a standard python expression  ::  achievements.purge()
            As a screen action  ::  Function( achievements.purge )
            """
            achievement.clear_all()
            persistent.my_achievements.clear()


## DO NOT TOUCH/REUSE/CHANGE THIS AT ANY TIME!
## To clear this list use ::  achievements.purge()
default persistent.my_achievements = []
default achievements = Achievement()

init python:

    achievement.steam_position = "bottom right"

    achievement_name = {

        ## How to set up achievements
        # "achievement_key": [_("Name of Achievement"), _("Description"), '<image_path_here>', '<type>'],

        ## Note: If you decide to add/amend any achievement's data long after the game has started or
        ##       an achievement has been granted you will have to do a full reset of the game for those
        ##       changes to be reflected. I.e. Delete persistent data.

        ## Example
        "flee": [_("The Runner."), _("Flee as soon as you get to uni."), 'gui/trophy_icon.png', 'hidden'],

        ## The None, means that the achievement will be displayed greyed-out before it is granted (or achieved).
        ## I use these terms to describe the type of achievement it is;
        ##            None = default (greyed out and can see the name and description of the achievement.)
        ##        'hidden' = Achievements with this label will be displayed as hidden.
        ##      'platinum' = The final achievement to be granted once all other achievements have been granted.

        "riot": [_("Red Riot."), _("Start a riot."), 'gui/trophy_icon.png', 'hidden'],
        "banana": [_("Here's a banana for scale."), _("Acquire a banana."), 'gui/trophy_icon.png', 'hidden'],
        "nerd": [_("Nerd alert."), _("Attend class two times during the semester."), 'gui/trophy_icon.png', 'hidden'],
        "actor": [_("Golden globe."), _("Beautifuly fake a heart attack."), 'gui/trophy_icon.png', 'hidden'],
        "lockpicking": [_("Robin hood."), _("Pick a lock."), 'gui/trophy_icon.png', 'hidden'],
        "gamelab": [_("Illuminati."), _("Join a secret society."), 'gui/trophy_icon.png', 'hidden'],
        "wow": [_("Outstanding!"), _("Get all achievements."), 'gui/trophy_icon.png', 'platinum'],

        ## More of this is explained in 'achievement_screen.rpy'.

    }

    ## Here we are simply registering the achievements.
    ## This is solely for backend use.
    for k, v in achievement_name.items():
        achievement.register(v[0])


## Here are the instances of the achievements.
## These will be added to the persistent
## list we made earlier.
default achievement_flee = Achievement(name=achievement_name['flee'][0], message=achievement_name['flee'][1], image=achievement_name['flee'][2])
default achievement_riot = Achievement(name=achievement_name['riot'][0], message=achievement_name['riot'][1], image=achievement_name['riot'][2])
default achievement_banana = Achievement(name=achievement_name['banana'][0], message=achievement_name['banana'][1], image=achievement_name['banana'][2])
default achievement_nerd = Achievement(name=achievement_name['nerd'][0], message=achievement_name['nerd'][1], image=achievement_name['nerd'][2])
default achievement_actor = Achievement(name=achievement_name['actor'][0], message=achievement_name['actor'][1], image=achievement_name['actor'][2])
default achievement_lockpicking = Achievement(name=achievement_name['lockpicking'][0], message=achievement_name['lockpicking'][1], image=achievement_name['lockpicking'][2])
default achievement_gamelab = Achievement(name=achievement_name['gamelab'][0], message=achievement_name['gamelab'][1], image=achievement_name['gamelab'][2])
default achievement_platinum = Achievement(name=achievement_name['wow'][0], message=achievement_name['wow'][1], image=achievement_name['wow'][2])

