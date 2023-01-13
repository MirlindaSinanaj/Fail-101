# Variables permanentes
default persistent.frustrated = False
default persistent.upstairs = False
default persistent.uni_employee_pissed = False
default persistent.first_ask= False
default persistent.revenge = False
default persistent.key = False
default persistent.banana = False
default banana_placed = False
default persistent.attend_class = 0
default persistent.homework = False

label start:
    play music "audio/jazz_music.mp3"

    scene outdoor

    inner_thoughts "Sooooo..."
    inner_thoughts "First day here."
    inner_thoughts "I guess I envisioned college differently..."
    inner_thoughts "It doesn't really matter, I have only one goal..."
    inner_thoughts "Fail in the fastest way possible."


    menu:
        "Go in front of the building.":
            jump uni_front
        "Flee.":
            jump flee_victory


    return


label uni_front:

    scene uni

    inner_thoughts "I really wonder who decided to make this place this big."


    menu:
        "Enter the building.":
            jump uni_hall

        "Smoke a cigarette.":
            jump uni_cigarette


label uni_hall:

    scene uni_hall

    if banana_placed:
        jump banana_victory

    inner_thoughts "Wow, so much grey."
    menu:
        "Go to the staircase.":
            jump staircase

        "Go to the cafeteria.":
            jump cafeteria

        "Enter a classroom.":
            inner_thoughts "Let's check this out, it's the main thing here I guess."
            jump classroom

        "Go outside the building.":
            jump uni_front


    return

label uni_cigarette:
    inner_thoughts "I think I need a litte break before I enter this hellhole."
    inner_thoughts "..."
    inner_thoughts "You gotta be kidding me..."
    inner_thoughts "I really did forget my cigarettes."

    menu:
        "Ask someone for a cig.":
            jump cigarette_encounter
        "Renounce your cigarette and go inside the building frustrated.":
            $ persistent.frustrated = True
            jump uni_hall

    return

label flee_victory:
    play sound "audio/achievement.mp3"
    $ Achievement.add(achievement_flee)
    stop music
    play sound "audio/victory.mp3"
    victory "You flee this place and go off-grid. There has been rumours going around of you owning a bagel shop along the coast, but who knows... "
    return

label staircase:

    inner_thoughts "Let's visit this place."

    menu:
        "Go up.":
            if persistent.upstairs:
                jump upstairs_discovered
            else:
                jump upstairs

        "Go down.":
            jump downstairs

    return

label cafeteria: 

    scene cafeteria

    inner_thoughts "Ew. Disgusting."
    inner_thoughts "Who would eat there?"

    menu:
        "Pick up trash lying on the floor.":
            $ persistent.banana = True
            play sound "audio/achievement.mp3"
            $ Achievement.add(achievement_banana)
            inner_thoughts "You acquired a banana!"
            inner_thoughts "Maybe it will be of some use later."
            jump cafeteria

        "Start a student riot.":
            inner_thoughts "You start shouting in the middle of the cafeteria."
            inner_thoughts "FREE THE STUDENTS!"
            inner_thoughts "Maybe it will get you expelled ahahha LOL."
            inner_thoughts "But a few people around join you and start shouting as well."
            scene riot
            inner_thoughts "You are now a few hundred in front of the building, still shouting with banners flying in the air."
            inner_thoughts "Fast forward a few weeks, you've now established a true social policy in your country."
            inner_thoughts "Uni is now free and every course is interesting."
            play sound "audio/achievement.mp3"
            play sound "audio/achievement.mp3"
            $ Achievement.add(achievement_riot)
            stop music
            play sound "audio/defeat.mp3"
            defeat "You're such a loser."
            defeat "Why would you help the people like that?"
            defeat "You disgust me."

        "Go back to the main hall.":
            jump uni_hall


    return

label classroom:

    scene classroom

    inner_thoughts "So this is what this place is about."
    inner_thoughts "You spot the teacher downstairs giving a lecture on pizza bread."

    menu:
        "Sit down and attend a class.":
            $ persistent.attend_class +=1
            inner_thoughts "After 45 mins of pure gibberish, you walk out the classroom almost dizzy."
            if persistent.attend_class >=2:
                jump class_defeat
            else:
                inner_thoughts "What the hell was that."
                jump uni_hall
        "Go down the stairs to the front of the class.":
            inner_thoughts "You walk slowly."
            teacher "Excuse me?"
            you "Yes?"
            teacher "What are you doing?"
            menu:
                "I'm just looking for a seat.":
                    $ persistent.attend_class +=1
                    inner_thoughts "You sit down and listen to the entire course, ashamed of yourself."
                    inner_thoughts "That was so boring."
                    inner_thoughts "They even told us to write an essay."
                    $ persistent.homework = True
                    if persistent.attend_class >=2:
                        jump class_defeat
                    else:
                        jump uni_hall
                "Get lost and let me teach something interesting." if persistent.frustrated:
                    teacher "Do you even know who you're talking to?!"
                    inner_thoughts "But you really do. Ironed shirt. Short grey hair. The Devil in person."
                    inner_thoughts "It is your holy mission to defeat this monster."
                    inner_thoughts "You jump and break their neck."
                    inner_thoughts "You liberated the whole class."
                    inner_thoughts "Round of applause."
                    stop music
                    play sound "audio/defeat.mp3"
                    defeat "You got promoted to professor and are now teaching. You die alone in your office."
                    defeat "Pathetic."


        "Leave the class.":
            inner_thoughts "Hugh I can't stand this."
            jump uni_hall





    return


label cigarette_encounter:

    show smoker at truecenter with moveinright


    you "Excuse me, do you mind giving me a cigarette?"
    smoker "Sorry I don't smoke."

    menu:
        "Ask them again.":
            you "You're kidding me, right?"
            smoker "I don't know what you mean..."
            menu:
                "Ask them AGAIN.":
                    you "You're seriously not going to give me a cigarette?"
                    smoker "..."
                    inner_thoughts "You look around and spot a chair lying a few meters away. You casually walk towards it, grab it, and proceed to throw it right at the face of the smoker. "
                    inner_thoughts "They didn't even see it coming. They're now lying on the floor. You hear lound noises coming from behind and a security guard running towards you."
                    stop music
                    play sound "audio/victory.mp3"
                    victory "After a trial for aggravated assault, you're expelled! Congratulations!"
                    return
                "Go inside the building, you don't have time for this kind of interactions.":
                    you "Unbelievable..."
                    inner_thoughts "You're now super grumpy. Welcome to uni."
                    $ persistent.frustrated = True
                    jump uni_hall

        "Renounce your heavenly cigarette, what a day.":
            $ persistent.frustrated = True
            jump uni_hall

    return

label upstairs:

    scene upstairs

    inner_thoughts "Who thought there could be that many doors in a building, I don't even know where I am."

    menu:
        "Have a look aroud.":
            $ persistent.upstairs = True
            inner_thoughts "Okay, there are actually THAT many people paid doing nothing."
            jump upstairs_discovered


        "Go back downstairs.":
            inner_thoughts "Nervemind, I'll come back later."
            jump uni_hall

    return

label downstairs:

    scene basement

    inner_thoughts "Mhh."
    inner_thoughts "I see."
    inner_thoughts "This is even more depressing than upstairs."

    menu:

        "Go to the library.":
            scene library
            inner_thoughts "I'm supposed to study here?"
            inner_thoughts "Talk about depressing."
            menu:
                "Work on the essay you were given in class." if persistent.homework:
                    inner_thoughts "Hugh this is the last thing I want to do."
                    inner_thoughts "Unless..."
                    menu:
                        "Plagiarize the whole paper and hope getting caught.":
                            inner_thoughts "Hahahah this is so easy."
                            inner_thoughts "You copy 20 pages from a book and hand it over to the teacher."
                            jump award_loss

                        "Stay honest and write your own paper.":
                            inner_thoughts "I wonder what it feels like to be a teacher's pet."
                            jump honesty_win
                    return
                "I'd better shoot myself.":
                    return
            return

        "Wander into the caves.":
            if persistent.key:
                inner_thoughts "Mhh I could try that key i found in Pr. Brown's desk."
                menu:
                    "Enter the caves, at your own risk.":
                        jump gamelab

                    "Go back to explore the rest of the basement.":
                        inner_thoughts "This place creeps me out. I'm out."
                        jump downstairs

            else:
                you "You need a key to open this door."
                jump downstairs
            return

        "Enter the technical room.":

            inner_thoughts "You walk towards the door and try to open it."
            inner_thoughts "It opens."
            scene black
            inner_thoughts "It's so dark in here."
            menu:
                "Continue exploring in the dark.":
                    inner_thoughts "You walk slowly with your hands in front of you."
                    inner_thoughts "You feel a button with your fingers, it could possibly be for the light."
                    inner_thoughts "But it wasn't."
                    inner_thoughts "The button released a deadly gas that turns people into zombies in the whole building."
                    scene zombies
                    inner_thoughts "This is the best day of your life."
                    inner_thoughts "You hurry out, smiling like you've never been before, while you break a car's window to flee to the countryside."
                    stop music
                    play sound "audio/victory.mp3"
                    victory "Bravo!"
                    victory "You live a happy life after you destroyed your whole uni."
                    victory "You have a pet zombie named Mark."
                    return



                "Return to the entrance of the basement.":
                    you "Yeah, let's turn back."
                    jump downstairs

            return

        "Go back to the main hall.":
            jump uni_hall


    return

label upstairs_discovered:

    scene upstairs


    menu:
        "Go to the students' secretariat.":
            jump uni_employee

        "Go to the dean's office.": 
            scene dean
            you "Hello."
            dean " Hello! What brings you here today?"
            jump dean

        "Go to Pr. Brown's office.":
            jump brown_office_door

        "Return to the main hall.":
            jump uni_hall


    return


label uni_employee:

    scene useless_employee

    uni_employee "Hello, can I do something for you?"
    menu:
        "Ask about the procedure to register to a course.":

            uni_employee "Ooof, complicated."
            uni_employee "Come back with an appointment."
            inner_thoughts "You leave, slightly pissed by their tone."
            $ persistent.first_ask = True
            jump upstairs_discovered

        "Ask how to get exepelled.":
            uni_employee "Hahahaah! I see you're a joker."
            you "Yes, indeed."
            uni_employee "I think as long as you don't atack anyone, you'll be fine."
            jump upstairs_discovered

        "Take an appointment to discuss your courses." if persistent.first_ask:
            uni_employee "Oh don't worry about that!"
            uni_employee "I've got time right now if you want."
            you "How convenient."
            inner_thoughts "You painfully contain your rage."
            inner_thoughts "You now proceed to listen to pure bureaucratic nonsense for 35 minutes."
            inner_thoughts "When you walk out the office, you swear on your grand-parent's grave to get revenge on this filthy employee."
            $ persistent.revenge = True 
            jump upstairs_discovered

        "Insult the employee." if persistent.frustrated:
            uni_employee "How dare you?!"
            you "Ahhhh this feels so good."
            uni_employee "You'll never succeed in your studies with this attitude."
            you "Thank you!"
            uni_employee "Get out of here! You'll hear from me again I guarantee it..."
            $ persistent.uni_employee_pissed = True
            inner_thoughts "You didnt get expelled this time, but keep at it champ!"
            jump upstairs_discovered

        "Jump to the employee and beat them to a pulp." if persistent.uni_employee_pissed:
            you "Here goes nothing."
            inner_thoughts "Everyone on the floor hears the employee screaming. When they open the door, they see you hitting the employee with your bag."
            stop music
            play sound "audio/victory.mp3"
            victory "You got expelled, congratulations! You can never go back to uni in your country, but hitting that useless employee was totally worth it."
            return

        "Leave the banana peel that you found in the cafeteria at the door." if persistent.banana:
            $ banana_placed = True
            inner_thoughts "Hahaha that'll teach them a lesson."
            inner_thoughts "Mischief managed."
            inner_thoughts "Google it if you want, it's not that nerdy."
            jump upstairs_discovered



label dean:

    scene dean


    menu:
        "Mention the weather.":
            you "Such a beautiful weather outside!"
            dean "..."
            dean "It's raining."
            you "I know."
            dean "..."
            jump dean

        "Create a diversion.":
            you "Oh!"
            inner_thoughts "You point to the window."
            dean "What?!"
            inner_thoughts "The dean is now facing the window."
            menu:
                "Grab the coffee mug on the table and spill it on the ground.":
                    you "Oh my bad, I'm so sorry."
                    dean "It's ok. Just wait a minute, I'll go and grab paper."
                    jump diversion

                "Lose all self-respect for the sake of your goal.":
                    inner_thoughts "You grab the glass of water sitting on the desk and empty it on your pants."
                    dean "I didn't see any-"
                    inner_thoughts "He noticed."
                    inner_thoughts "Haha."
                    dean "I think you had a little accident..."
                    you "Oh !! I'm so embarassed..."
                    inner_thoughts "The dean walks out rapidly."
                    dean "I'll bring you some paper!"

                    jump diversion 

                "Improvise.":
                    inner_thoughts "You've dreamt of this moment for your whole life."
                    inner_thoughts "Yes."
                    inner_thoughts "It's time."
                    you "AHHHHH!"
                    inner_thoughts "You faked a heart attack."
                    dean "Oh my god!!"
                    dean "Help!!"
                    dean "Please!"
                    inner_thoughts "The dean sprints out of the room."
                    play sound "audio/achievement.mp3"
                    $ Achievement.add(achievement_actor)
                    jump diversion
        
        "Assault the dean." if persistent.frustrated:
            inner_thoughts "This is it."
            inner_thoughts "You can't take this anymore."
            inner_thoughts "With an elegant movement, you jump above the desk and send your right foot flying into the dean's jaw."
            inner_thoughts "Three day days later, the police found a tooth stuck in the wall."
            inner_thoughts "Nicotine deprevation can be dangerous. Stay smokey."
            stop music
            play sound "audio/victory.mp3"
            victory "Congratulations! You got expelled!"


    return


label diversion:

    inner_thoughts "This is your moment."

    menu:
        "Jump on the computer.":
            jump dean_computer

        "Wait for the dean to comeback.":
            inner_thoughts "Come on."
            inner_thoughts "Don't be ridiculous."
            inner_thoughts "This is a perfect opportunity."
            jump dean_computer


    return

label dean_computer:

    scene dean_computer


    inner_thoughts "Okay. Let's see what we got here."

    menu:
        "Try and change your notes in your student folder.":
            inner_thoughts "Ok... and it's done!"
            inner_thoughts "You quickly go back to where you were standing before when the dean comes back."
            dean "Are you ok-"
            you "Yes everything's ok."
            dean "Are you sure?"
            you "YES."
            inner_thoughts "You run out of the office leaving the dean speechless."
            stop music
            play sound "audio/victory.mp3"
            victory "Congratulations!"
            victory "You managed to change your grades and are now failing!"
            return
        "Leave the office. You don't want to break the law.":
            stop music
            play sound "audio/defeat.mp3"
            defeat "Due to your lack of commitment to the task, you didn't modify your grades, and therefore you passed you first year."
            defeat "What a shame..."
            return
    return


label brown_office_door:

    scene door


    inner_thoughts "This is Pr. Brown's office."
    inner_thoughts "I hear they can be quite... aggressive."
    menu:
        "Knock on the door.":
            inner_thoughts "No response."
            you "Pr. Brown, are you there?"
            inner_thoughts "Still nothing."
            menu:
                "Come back later.":
                    inner_thoughts "As you want, but I expected better."

                "Try to break into the office.":
                    inner_thoughts "I knew I'd use my lock picking set!"
                    inner_thoughts "Warning! The lock picking set can be faulty sometimes."
                    jump lockpicking

        "Leave.":
            inner_thoughts "What are you afraid of?"
            jump upstairs_discovered


    return

    label lockpicking:
        menu:
            "Continue picking the lock.":
                $ random_number = renpy.random.randint(1,3)
                if random_number == 1:
                    play sound "audio/achievement.mp3"
                    $ Achievement.add(achievement_lockpicking)
                    "Succes!"
                    jump brown_office

                else:
                    "Sorry... You suck at lockpicking apparently."
                    jump lockpicking

            "No, I shouldn't break into this office.":
                inner_thoughts "Coward."
                jump upstairs_discovered


        return


label brown_office:

    scene brown


    inner_thoughts "You are now in Pr. Brown's office."
    inner_thoughts "This is smaller than I imagined."
    inner_thoughts "Let's see..."

    menu:
        "Go sit at the desk.":
            inner_thoughts "Comfy chair."
            jump brown_desk


        "Leave before you get caught.":
            inner_thoughts "You just realized what you were doing and freaked out."
            inner_thoughts "You run out of the office but someone notices you leaving in a rush."
            stop music
            play sound "audio/victory.mp3"
            victory "Congratulations!"
            victory "You got expelled for breaking into Pr. Brown's office!"

            return

    return

label brown_desk:

    scene brown_computer

    inner_thoughts "What can I find here...."
    menu:
        "Try to use the computer.":
            inner_thoughts "The computer is protected by a password."
            jump brown_desk
        "Check the drawers.":
            inner_thoughts "Let's see what we can find..."
            inner_thoughts "Uh?"
            inner_thoughts "You found a key!"
            $ persistent.key = True
            inner_thoughts "Who knows, it could be useful."
            jump brown_desk
        "Leave the office.":
            inner_thoughts "Let's go."
            jump upstairs_discovered


    return


label gamelab:

    scene gamelab

    gamelab_member "Hey, who are you?"

    menu:
        "Flee.":
            inner_thoughts "Good idea."
            inner_thoughts "You start running but your foot gets caught on a wire and you trip."
            inner_thoughts "Your corpse never got discovered."
            stop music
            play sound "audio/victory.mp3"
            victory "You died!"
            victory "Therefore you win!"
            victory "It's as simple as that."
            victory "Reload the game now please."

        "Introduce yourself.":
            you "Hi."
            you "My name's ###."
            you "I was just wandering in the basement and came across this place."
            gamelab_member "Oh it's alright, we were just about to start a game."
            you "What kind of game?"
            gamelab_member "It's a card game called CIA, du you want to try it?"

            menu:
                "No.":
                    you "It's ok thank you, I've got to go back to my classes."
                    gamelab_member "No problem."
                    inner_thoughts "Good thinking. You just saved yourself."
                    jump downstairs
                "Why not.":
                    inner_thoughts "You spend 4 hours playing."
                    inner_thoughts "You had lots of fun."
                    inner_thoughts "It's now time to leave..."
                    you "Bye guys!"
                    gamelab_member "Bye! See you soon."
                    play sound "audio/achievement.mp3"
                    $ Achievement.add(achievement_gamelab)
                    inner_thoughts "You leave the basement with a weird feeling."
                    inner_thoughts "Wall, that was kinda fun."
                    inner_thoughts "What was this place called again?"
                    inner_thoughts "The Game somthing..."
                    inner_thoughts "Well, maybe this place is not that bad after all."
                    stop music
                    play sound "audio/defeat.mp3"
                    defeat "You lost!"
                    defeat "You start to like uni and don't want to leave anymore."
                    defeat "Pfff.."
                    return


label banana_victory:
    scene uni_hall

    inner_thoughts "You hear a falling sound, followed by a scream."
    inner_thoughts "Somebody just slipped on your banana peel."
    stop music
    play sound "audio/victory.mp3"
    victory "Congrats! You got caught on the camera leaving the banana."
    victory "You were chargend with manslaughter!"
    victory "You spend the rest of your life in a penitenciary facility, what a life well lived!"


label class_defeat:
    inner_thoughts "Mhh it wasn't that bad after all."
    play sound "audio/achievement.mp3"
    $ Achievement.add(achievement_nerd)
    stop music
    play sound defeat
    defeat "You attented 2 courses and liked it."
    defeat "You will now finish your semester."
    defeat "Nerd."
    $ persistent.attend_class = 0
    return

label award_loss:
    scene award

    inner_thoughts "The teacher was too lazy to check your essay for plagiarism."
    inner_thoughts "You won the faculty award for your paper on the evolution of paper clips."
    stop music
    play sound "audio/defeat.mp3"
    defeat "Sorry."
    defeat "You achieved your first year in a brilliant manner."

    return

label honesty_win:
    stop music
    play sound "audio/victory.mp3"
    inner_thoughts "Congratulations!!"
    inner_thoughts "Your essay was so bad that you got expelled immediately."
    inner_thoughts "Well done!"
    return