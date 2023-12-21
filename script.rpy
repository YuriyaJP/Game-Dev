# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define h = Character("Haru", image="c haru")
define y = Character("Yukino", image="c yukino")
define a = Character("Ayaka", image="c ayaka")
define b = Character("Board", image="c board")
define bs = Character("Board Signed", image="c board signed")
define t = Character("Teacher", image="c teacher")
define s = Character("Sara", image="c sara happy")
define hi = Character("Hinata", image="c hinata")
define ft =Character("Teacher", image="c fteacher")
define l = Character("Lucus", image="c lucus")

# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "background music.mp3"
    scene bg inage with dissolve

    # Show both characters initially.
    show c haru at right with fade
    h "Hello and welcome to Sogo High School!"

    show c yukino at left with fade
    y "Let's play the game together."

    # These display lines of dialogue.

    # The first menu
    menu:
        "Which character will you choose?"

        "Haru":
            h "I'm happy you chose me! Let's play together!"
            $ choose = True
            jump haru_scene #Jump to Haru's scene
        "Yukino":
            y "Thank you for choosing me. Let's enjoy this game!"
            $ choose = False
            jump yukino_scene #Jump to Yukino's scene
# End of the 'label start' segment.
# Continue the story in a separate label.

label haru_scene:
    scene bg hall with fade
    show c haru at right with fade
    h "I'm late for my class. Wait, is there something on a notice board?"
    show c board at left with fade  # Show the board character
    h "Wow! It says there will be an audition for a volleyball team. I wonder whether I should join though."
    menu:
        "What should Haru do?"

        "Join":
            play sound "writing.wav"
            show c board signed at left with fade  # Show the signed board character
            h "Okay, I wrote my name. I hope I can do my best at the audition. Time to go to class."
            $ haru_choice = True
            jump classroom_teacher_haru #Jumps to a classroom scene with a teacher but this choice has a new story development.
        "Ignore":
            h "No, I don't want to risk losing my reputation. Besides, those volleyball players look way too scary."
            $ haru_choice = False
            jump classroom_teacher_yukino #Jumps to a classroom scene with a teacher

label classroom_teacher_haru:
    scene bg classroom with fade
    show c haru at left with fade
    h "Ehem...Sensei, there is a problem..."
    show c teacher at right with fade
    menu:
        t "What is it AGAIN, Haru?"

        "I lost my homework":
            t "I guess it's... The 5th time this week you lost it??"
            t "No way you can make excuses now, you stay after school as a punishment."
            $ homework_lost = True
            jump ayaka_haru #Jumps to a scene with Ayaka
        "I didn't do my homework":
            t "Well, it is not nice. But I like your honesty. You can bring your homework tomorrow, but don't do it again. This is your last chance. "
            $ homework_lost = False
            jump sara_haru #Jumps to a scene with Sara
label ayaka_haru:
    scene bg afternoon
    play sound "JapaneseSchoolBell.mp3"
    show c haru at left with fade
    h "Finally, homework finished! I shouldn't have lied to the teacher..."

    show c ayaka at right with fade
    a "Hey Haru! How are you?"

    show c haru at left with fade
    h "Hey Ayaka, I didn't do my homework, so I stayed late."

    show c ayaka at right with fade
    a "That's a pity. By the way, I heard there is a volleyball audition today."
 
    menu:
        a "Do you want to go take a look?"

        "Alright":
            a "Cool, let's go!"
            $ volleyball_choose = True
            jump volleyball #Jumps to a volleyball scene
        "Not really":
            a "Suit yourself. I will go alone."
            $ volleyball_choose = False
            jump sara_haru #Jumps to a scene with Sara

label volleyball:
    scene bg gym
    show c ayaka at left
    a "Wow, this is Hinata - the best volleyball player at Sogo! Hello senpai!"
    show c hinata at right
    hi "Hey Ayaka and... Is it Haru? Wow, I saw you looking at a volleyball audition this morning."

    menu:
        hi "Do you want to play?"

        "Sure":
            scene bg game
            play sound "applause.wav"
            scene bg gym            
            $ play = True
            show c hinata at right
            hi "What a game! Great job man! Consider yourself on a team!"
            jump sara_haru

        "Sorry, I can't":
            show c haru at left
            h "Sorry, I can't, my knee hurts."
            show  c hinata at right
            hi "Alright, take care. See ya!"
            $ game = False
            jump sara_haru #Jumps to a scene with Sara

label sara_haru:
    scene bg classroom
    show c sara happy at right
    s "Hello, are you Haru?"
    show c haru at left
    h "Hi, yes I am. And you are...?"
    s "My name is Sara, I am from New Zealand. Are you a friend of Yukino?"
    h "Nice to meet you, Sara. Yes, we are friends."
    s "Great! Listen, we are gathering tonight to watch the fireworks."

    menu:
        s "Wanna join us?"

        "Sounds nice. I'll go.":
            s "Great! I will be waiting in front of the classroom for you to pack your things."
            $ fireworks = True
            jump fireworks

        "Sorry, I can't.":
            show c sara sad at right
            s "That's too bad. But I'll see you around. Bye!"
            $ fireworks = False
            scene bg end


label fireworks:
    scene bg fireworks
    play sound "fireworks.wav"
    "Everyone has made it to the fireworks!"


#### Here I will write the code for Yukino's character and all possible pathways

label yukino_scene:
    scene bg classroom with fade
    show c yukino at left with fade
    y "Hello sensei! You look strict as always today!"
    show c fteacher at right with fade
    ft "I am very happy to see you too, Yukino."

    menu:
        ft "Is there anything I can help you with?"

        "Nothing, I just wanted to say hello to you.":
            ft "Well, hello. Now I have to go, but I'll see you in class."
            $ ask_sth = True
            jump warinpia #Jumps to the last scene with Yukino before fireworks

        "I want to know about Lucus.":
            ft "Ah, you're talking about our new international student Lucus!"
            menu:
                ft "He is a very diligent boy, just a bit shy. Can I ask you to try to make friends with him?"

                "Yes":
                    ft "Thank you, Yukino, I hope you will be good friends."
                    $ be_friends = True
                    jump warinpia #Jumps to the last scene with Yukino before fireworks
                "No":
                    ft "I see. It's okay, I can ask someone else."
                    $ be_friends = False
                    jump warinpia #Jumps to the last scene with Yukino before fireworks

label warinpia:
    scene bg warinpia
    show c lucus at right with fade
    l "Oh hey, glad I've seen you. I am Lucus."
    show c yukino at left with fade
    y "Hi Lucus. My name is Yukino. The teacher told me about you. Are you from the US?"
    show c lucus at right with fade
    l "No, I am actually from New Zealand. You know, lots of greenery, kiwi birds..."
    show c yukino at left with fade
    y "Sounds cool, I want to go there someday."
    show c lucus at right with fade
    l "Please come! By the way, me and my firends are going to the beach to watch fireworks tonight."

    menu:
        l "Do you want to come with us?"

        "Yes, I do!":
            l "Cool, let's buy some food before we go."
            l "There is a shopping mall right behind us."
            $ go_beach = True
        "I need to go home.":
            l "Oh, it's okay...I guess next time..."
            l "Let me walk you to the station then."
            scene bg inagekaigan
            l "Here we are...Are you sure you cannot come?"
            menu:

                "Sorry":
                    l "Okay, I see you in class. Bye!"
                    scene bg end
                    $ last_chance = True
                "I've changed my mind":
                    l "I'm so happy you did! Let's enjoy the fireworks!"
                    $ last_chance = False
                    jump fireworks
return
