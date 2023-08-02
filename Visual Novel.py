# Define characters
define eileen = Character('Eileen', color="#c8ffc8")
define international_student = Character('International Student', color="#ffffaa")

# Define images
image bg_school = "school.jpg"
image bg_classroom = "classroom.jpg"
image bg_basketball_court = "basketball_court.jpg"
image eileen_normal = "eileen_normal.png"
image international_student_normal = "international_student_normal.png"

# Start of the visual novel
label start:

    # Background music
    play music "background_music.mp3"

    # Background image
    scene bg_school

    "It's another day at Junior High School."

    "Meet our protagonist, Eileen, a cheerful and lively student."

    show eileen_normal
    e "Good morning, everyone!"

    "And here's the international student who recently joined the school."

    show international_student_normal
    international_student "Hello, everyone. Nice to meet you all."

    "The day starts with a morning assembly."

    # Transition to the classroom scene
    scene bg_classroom

    "In the classroom, the teacher starts the day's lessons."

    e "I wonder what we'll learn today."

    # Transition to the teacher scene
    scene bg_classroom with dissolve
    show eileen_normal
    show international_student_normal
    show teacher_normal

    teacher "Good morning, class. Today, we will learn about history."

    "After an engaging class, it's time for lunch."

    "Eileen and the international student decide to eat together."

    show eileen_normal
    show international_student_normal
    e "Hey, wanna sit together?"

    international_student "Sure, I'd love to."

    "The two of them enjoy their meal and share stories."

    "In the afternoon, they head to the basketball court."

    # Transition to the basketball court scene
    scene bg_basketball_court with fade
    show eileen_normal
    show international_student_normal

    e "Let's play a friendly basketball match!"

    "They play an exciting match with their classmates, and it's a lot of fun."

    "The sun starts to set, and the day comes to an end."

    "As they head home, they look forward to more adventures at Junior High School."

    "And so ends another memorable day."

    # End of the visual novel
    return

# Start the visual novel
return start