 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
default name = ""
define Y = Character("[name]")
define A = Character ("Abelardo")
image Abelardo = "Abelardo.png"
transform half_size:
    zoom 0.5
define Pe = Character ("Petro")
image Petro = "petro.png"
define U = Character ("Uribe")
define P = Character ("Polo Polo")
define C = Character ("Cepeda")
image Cepeda = "cepeda.png"
define N = Character ("Narrator")
default A_relationship = 0
default Pe_relationship = 0
default U_relationship = 0
default P_relationship = 0
default C_relationship = 0
image Abelardo= im.Scale ("Abelardo.png", 800, 800)
image Cepeda= im.Scale ("cepeda.png", 800, 800)
image Petro= im.Scale ("petro.png", 800, 800)
# The game starts here.

label start:

scene lol with fade:
    fit "cover"
play music "Music audio.mp3" volume 0.5 loop
N "You land an internship at a public institution in Bogotá."
N "On your first day, you meet several politicians who, for reasonsthat are completely inexplicable, begin to meddle in your life."
N "You are doing the internship at the Palace of Justice."
N "Your first day goes smoothly: you had given a simple task to deliver some documents to Abelardo."
N "Abelardo is already a prominent political figure, and has just been elected president following Petro’s resignation."
image Hallway = "Hallway.jpg"
scene Hallway with fade:
    fit "cover"
N "You are going through the halls of your new workplace, Palace of Justice in Bogota, Colombia."
N "You're holding a bunch of paperwork that the elected president needs so you go and hand it to him,you have never seen him in person."
Y  "I don’t know why public institutions always feels like a maze…"
N "You arrive at the main office where Abelardo is going through his mails, waiting for you."
image Puerta = "Puerta.png"
scene Puerta with fade:
    fit "cover"
play sound door
N "Knock Knock." 
A "Come in!"
play sound creak
N "You come inside with slow steps and closing the door behind you."
image Office = "Office.png"
scene Office:
    fit "cover"
    yoffset -300 
show Abelardo at center
Y "Good morning Mr. President."
Y "They send me to handle you these documents..."

N "Abelardo raise his gaze and stares at her for a few seconds"
A "Are you new here?"
Y "Yes sr."
A " I can tell…"
N "He spreads an almost unnoticiable smirk before his eyes focus back on his computer"
A "Not necessarily."
N "You extend your arms offering him the papers"
Y "These are the documents I was assigned to leave here, sr."
N "Abelardo takes the documents but he does not take a look at it immediately"
A " What's your name, lady?"
$ name = renpy.input("Enter your name: ")
$ name = name.strip()
Y "Uhmm… My name is [name], sr."
A "Ohhh.. And… What are you doing here… [name]?"
Y "I am an intern, sr."
A " I know, but I mean, what's going to be your role here in the Palace of Justice?"
N "Choose your answer:"

menu:
    "I'm going to be working as your assistant, if you want something you call to my desk and I'll do the favor you ask me to.":
        $ A_relationship += 2
        A "..."
        A "And they told you to bring me these documents?"
        Y "Yes, sr."
        A"So you are effitient"
        Y "I only do my job, sr."
        A "Do you have anything else to do?"
        Y"I guess so... It's my first day. I don't really know what to do yet."
        A "So just stay here"
        Y "Uhm..."
        Y "Excuse me?"
        A "I need you to organise these documents for me"
        Y "Oh... Okay, sr."
        N "You take the documents and sigh."
        Y "Where do I need to organise them?"
        A "Here, in this desk. I need you to organise them by date and by importance."
        Y "And what do I do when I finish the task?"
        A "You ask me what's next"
        Y "And if you're not here?"
        N"Abelardo looks at you with a confident gaze and a smirk on his face"
        A"I'll be here, don't worry. I have a lot of work to do, but I can always find time for you."
        N "You look at him for a few seconds"
        Y "What a confidence"
        A "I need it"

    "They told me to bring these documents, don't you see?":
        $ A_relationship += 1  
        A "..."
        A "So just do it and go back to your desk"
        Y "I was thinking of doing it, but you keep asking me questions"
        A"You always answer like this with your superiors?"
        Y"Only when my superiors talk me like this"
        A "You have a lot of attitude for an intern"
        Y" And you hae a lot of free time for an elected president"
        A "..."
        Y "Anything else?"
        A "No, you may do your assignment"
        Y "With pleasure"
        N "You leave the office and go back to your desk, you start organising the documents."
scene black
N "Weeks later.."
N "The Palace of Justice is filled of people. The possesion ceremony of the new president it's about to take place. Abelardo has become the President after the mandate of Gustavo Petro."
if A_relationship == 2:
    image possesion = "Posss.jpg"
    scene possesion with fade:
        fit "cover"
    show Abelardo at center
    N "You stand next to Abelardo with a folder between your hands. You are not just a simple intern anymore"
    A"Do you have everything?"
    Y "Yes, sr."
    A"The speeches?"
    Y "Ready."
    A "The documents?"
    Y "Yes, sr."
    A "My agenda"
    Y "Yes, sr."
    A "Good"
    N "You look around and see the people that are going to attend the ceremony, you see a lot of politicians and journalists"
    A "One month ago you were archiving documents for me, and now you are here next to me, you are doing a good job"
    Y "Only that?"
    A "Nah, you're not here just because of that"
    Y "There's something else?"
    A "I got used to you being around me, and I like it"
    N "You stay silent for a few seconds, you don't know what to say"
    Y "That doesn't sound very professional, sr."
    A "Probably not, but..."
    N "Before Abelardo can finish his sentence, someone aproaches you"
    A "It seems that we have company"
    N "You turn around and see two men in suit"
    show Abelardo at right
    show Petro at left
    show Cepeda at center
    Pe "Abelardo."
    A "Petro, Cepeda, what a surprise."
    N "Petro looks at you"
    Pe "And who is this?"
    A "She's working with me, she's my assistant"
    N "Petro raises his eyebrows slightly"
    Pe "With you?"
    C "So... You are [name], right?"
    Y "You know me?"
    C "Not personally"
    Pe "But, apparently, we are gonna have to do it"
    N "You look at Abelardo slightly confussed"
    Y "It doesn't make me feel comfortable if you are the one who is saying it"
    Pe "I like her"
    A "That´s too fast"
    Pe "We're just talking"
    A "That's what I hope"
    N "You look between the three of them, right then, the ceremony begins"
    Pe "I want to take you somewhere in these days, maybe a coffee?"
    N "Said Petro, whispering at her"
scene black
N " You accept the offer of Petro and start hanging out with him and Cepeda after work for 6 months. You meet new people, meet new places and have wonderful experiences with them."
N "But one day you went normally to work and..."
scene Office:
    fit "cover"
    yoffset -300
play sound creak
N"It's night time, the Palace is almost empty. You just finished saving some documents when you hear the door opening"
show Abelardo at center
A "[name]..."
Y "Yes?"
A "Come here, we need to talk"
N "You stand up"
Y "Did something happened?"
A "Yes. You. You have been busy lately."
Y "I have work"
A "I didn't meant about work"
N "Silence."
Y "So... What do you mean?"
A "Petro and Cepeda"
Y "What about them?"
A "You spend way to much time with them"
Y "And what does that have to do with you?"
A "Everything"
Y "I didn't know that I needed a permission to spend time with anybody"
A "You don't need a permission... but..."
A "You have to decide. If you want to stay with me, you need to stop playing both sides"
Y "And if I don't want to?"
A "Then you have to leave..."
Y  "That simple?!"
A "That simple."
N "You cross your arms"
Y "And what am I supposed to choose?"
A "Me."
Y "I already understood that"
A "No, you didn't understand."
N "Abelardo comes closer to you"
A "You can stay here. You can grow here. You can be part of something big"
Y "And the other option?"
A "Them."
A "That little rebel opponents"
Y "Are you kidding me?"
A "Petro and Cepeda have their own world. There ideas, their speeches, their poems..."
Y "Cepeda writes really good"
A "That's not the point"
Y "I think you're getting jealous"
A "I'm not jealous, I'm trying to avoid the fact that you could lose your potential"
N "You stay in silence, thinking"
A "You know what you can achieve here. With me."
A "Power. Influence. A position that no one would have given to you months ago"
Y "And what do you want in change?"
A "Loyalty."
Y "That sounds very egocentric"
A "Probably"
Y "And what if I choose Petro and Cepeda?"
N "Abelardo comes even closer, until your breath exchanges with his"
A "Then it's over"
Y "My job?"
A "Everything"
N "Who are choosing?"
menu:
    "I'll stay with you.":
        N "Abelardo smirks"
        A "I knew you would take the right decision"
        Y "Don't get excited"
        A "We'll see that..."
        $ A_relationship += 1
        return

    "I'll leave.":
        N "Abelardo steps away"
        A "I understand."
        Y "Abelardo..."
        A "No."
        A "You already make your decision. Take your things and you can leave."
        $ A_relationship == 0

        scene black
        N "In these last days, you found a new job who fortunately you like, and spent the most of your time hanging out alone with Petro and Cepeda, nothing serious, for now."
        image teatro = "Exterior_Teatro_Libre_editada1.jpg"
        scene teatro with fade:
            fit "cover"
        show Cepeda at center
        N "You and Cepeda are leaving the theater after watching Romeo and Juliet. You walk calmly down the street."
        Y "I don't know what to think."
        C "About the play?"
        Y "Yes. It was all... intense..."
        C "It's Shakespeare. The intensity is obligatory."
        Y "Romeo and Juliet had known each other for just five minutes, and they were already willing to die for one another."
        C "And you think that's absurd?"
        Y "A little bit"
        C "Why?"
        Y "Because I don't think that loving someone means to completely lose one's mind."
        C "So, what do you think it means to love?"
        menu:
            "I think loving someone is truly knowing him and still staying.":
                C "That's interesting"
                Y "Why?"
                C "Because it means that love doesnn't depend solely on what you feel. It also depends on what you choose to do with those feelings."
                Y "I guess so."
                C "I like how you think."
                $ C_relationship +=3
            
            "I think that love should make you feel free. If you have to loose yourself for someone else, then it's not worth it.":
                C "Free?"
                Y "Yes. Loving someone should not mean stopping being yourself."
                C "I agree."
                Y "Were you hoping for another answer?"
                C "No. But I was hoping you'd surprise me."
                $ C_relationship +=1
        
        N "You continue walking. Cepeda stays thoughtful for a few seconds."
        C "You know what I find interesting about the play?"
        Y "What?"
        C "Everyone talks about love as if it could explain itself."
        Y "And you think so?"
        C "Not completely."
        Y "Maybe that's why the poetry exists."
        C "Exactly."
        Y "You write poetry, right?"
        C "Sometimes. What do you think of it?"
        menu:
            "I think poetry is beautiful, but people often use it to say things they don't dare to say directly.":
                C "That is completely true."
                Y "Although I guess that it has its own charm."
                C "You like it?"
                Y "It depends on the artist."
                C "A dangerous answer."
                Y "Why?"
                C "Because now I want to know what do you think of my poetry."
                $ C_relationship +=2

            "I think poetry is one of the most honest ways to say what you feel. Even when it has a lot of metaphors.":
                N "Cepeda looks at you with a smile."
                C "I didn't expect you to say that."
                Y "Why?"
                C "Because most of the people say that poetry exaggerates."
                Y "Sometimes it does, but that doesn't mean that it's not true."
                C "I like that answer."
                Y "Really?"
                C "More than I should."
                $ C_relationship += 3

        N "You continue walking. The conversation turns more intimate."
        C "I'm glad I invited you."
        Y "Why?"
        C "Because with you, I can talk about things that normally no one wants to listen to for that long."
        Y "Is that a compliment?"
        C "It is."
        Y "Then thanks..."
        N "Cepeda smiles at you."
        C "Also, you are different from what I expected."
        Y "What did you expect?"
        C "I don't know yet"
        Y "That doesn't make much sense."
        C "Maybe I need to get to know you better."
        N "Cepeda gets closer to you, brushing your hand."
        menu:
            "Then you'll have to invite me again.":
                N "Cepeda grins"
                C "Is that an hint?"
                Y "Maybe."
                C "I like it... and I like you too."
                $ C_relationship += 3

            "Don't get excited. I just came to see the play.":
                N "Cepeda chuckles."
                C "Understood."
                Y "But I enjoyed it."
                C "So all is not lost."
                $ C_relationship += 1

            "I think you're confusing things. I like you, but not like that, and this is definitely.":
                N "Cepeda stays in silence for a moment, taking one step back."
                C "I understand."
                Y "I didn't want to sound rude."
                C "You didn't. I'd rather you be honest."
                
        scene black
        N "You also spent a lot of time with Petro..."
        play music "salsa.mp3" volume 0.5 loop
        image parque = "parque-93.jpg"
        scene parque:
            fit "cover"
            yoffset -400
        N "It's a quiet afternoon. You arrive at the park and see Petro waiting for you near an area where several people are dancing salsa. Music is playing, and there are quite a few people around."
        show Petro at center
        Y "Was this the surprise?"
        Pe "What did you expect?"
        Y "I don't know. A restaurant. A cafeteria. Something normal."
        Pe "Normal? You already spend enough time in the office. I'm not taking you to another one."
        N "Petro smiles and points at some people dancing."
        Pe "Do you know how to dance?"
        Y "Not really."
        Pe "Perfect. Now I have an excuse to teach you."
        N "Petro extends his hand."
        Pe "Trust me. Please."
        menu:
            "Alright. Teach me.":
                N "You take Petro's hand. He guides you to the center, vybing with the music."
                Pe "See? It's not that hard."
                Y "We haven't started yet."
                Pe "Exactly. And you're already worried."
                Y "Because I don't know what are you gonna do."
                Pe "Nothing too complicated. Just follow the beat and feel it... Feel me..."
                $ Pe_relationship += 3
            
            "I prefer to look first...":
                Pe "You sure?"
                Y "Yes. I want to see how you do it before I end stepping on you."
                Pe "Coward"
                Y "Prudent"
                $ Pe_relationship += 1

        N "After dancing, both of you took a break and sat for a moment."
        Pe "Did you enjoy it?"
        Y "Yes."
        Pe "Good, because I wanted today to be different to everything you do normally."
        
        scene black
        "After dancing, you walk to a nearby to restaurant."
        play music "restaurant.mp3" volume 0.5 loop
        image resta = "elcielo-restaurant-bogota.jpg"
        scene resta with fade:
            fit "cover"
        show Petro at center
        Pe "For me a... baby beef. And for the lady..?"
        menu:
            "Triple Burger.":
                N "Petro smiles."
                Pe "So you have good judgement?"
                Y "I didn't know there was a correct answer."
                Pe "For me? Yes."
                $ Pe_relationship += 3

            "A salad.":
                N "Petro looks at you for a few second."
                Pe "Really?"
                Y "Really."
                Pe "After dancing Salsa... salad?"
                Y "Yes."
                Pe "I though you would be more interesting..."
                $ Pe_relationship += 2

        N "After eating, you stayed at the restaurant."
        Pe "You know what?"
        Y "What?"
        Pe "I like you when you aren't working, because... you don't look stressed."
        Y "Is that that bad?"
        Pe "I mean... this could be ours."
        Y "That sounds very intense."
        N "Silence"
        Pe "I'm glad you came. We should do this again."
        Y "Is that an invitation?"
        Pe "Yes."
        Y "What if I say no?"
        Pe "So I'll have to convinve you."
        Y "And if I say yes?"
        Pe "Then I have a second date."
        Y "How convenient."
        Pe "Do you like spending time with me?"
        menu:
            "Yes. I like spending time with you.":
                N "Petro smiles."
                Pe "Good. Now I can stop pretending this was just a friendly date."
                $ Pe_relationship += 3
            
            "It depends... Are you going to ask me to dance again?":
                Pe "So there will be a next time."
                Y "That's not what I said."
                Pe "You didn't say no."
                Y "You are imposible."
                Pe "And you are still here."
                $ Pe_relationship += 1

            "I like spending time with you, but I don't think this is a date.":
                N "Petro stays in silence for a moment."
                Pe "I understand."
                Y "I didn't want to sound rude."
                Pe "You didn't. At least you were honest."
                Y "So... are we still friends?"
                Pe "I guess so."
                Y "You guess so?"
                Pe "Give me a moment. You just rejected me, I need to hold my dignity."

        stop music     
        scene black
        N "..."
        if Pe_relationship > C_relationship:
            image cel = "dt_240127_hand_smartphone_screen_night_800x450.jpg"
            scene cel with fade:
                fit "cover"
            N "It's late. You are at home when you receive a call."
            Pe "Where are you?"
            Y "My house. Why?"
            Pe "I need to talk to you."
            Y "Now?"
            scene black
            N "Before receiving an answer, the call was disconnected."
            play music "Music audio.mp3" volume 0.5 loop
            image patio = "d4b490ff8aa9c758aa93bc9d799c87d5.jpg"
            scene patio with fade:
                fit "cover"
            show Petro at center
            N "Few minutes later, you found Petro sitting outside your house."
            Y "Are you drunk?"
            Pe "No... (yes)"
            N "You sigh. You help him into your house and sit him down on the couch, which goes really badly."
            image sofa = "df18e16b8d5b58a63996dc9415ef585a.jpg"
            scene sofa:
                fit "cover"
                yoffset -400
            show Petro at left
            N "You both fall onto the couch, and Petro loses his balance, leaning toward you, resting his hand on the armrest, trapping you there."
            Pe "[name]... I have something to tell you..."
            Y "I listen."
            Pe "I like you..."
            Pe "..."
            Pe "A lot..."
            Y "... You should say that when you're sober..."
            Pe "No."
            Y "No?"
            Pe "Because when I'm sober, I think too much."
            Pe "I think about Cepeda. I think about Abelardo. I think about everything I should do and everything I shouldn't do..."
            Pe "Now..."
            Pe "The only thing I know it bothers me a lot when I see with someone else..."
            Y "That sounds like jealousy."
            Pe "Yes."
            Y "And what do you want me to do with that?"
            N "Petro gets closer, your noses brushing."
            Pe "Choose me."
            menu:
                "Yes. I choose you.":
                    scene black
                    N "END..."
                
                "Sorry, this is not what I wanted...":
                    Pe "I see..."
                    N "Petro lies down on top of you."
                    Pe "Just... let me be here..."
                    scene black
                    N "You didn't hear much from Petro after that."
                    N "Some time later, Cepeda invited you to Cartagena... and you accepted"
                    image mar = "6ae77f3a66b96677c7be0aff4abef44e.jpg"
                    play music "olas.mp3" volume 0.5 loop
                    scene mar with fade:
                        fit "cover"
                    show Cepeda at center
                    N "It's night time. You walk alongside Cepeda, barefoot on the sand. There was no noise from the polluted city, just waves crashing against each other."
                    Y "I still can't understand why did you bring me to Cartagena."
                    C "Because you said that you wanted to get to know a place where you can forget about everything."
                    Y "I don't remember saying that."
                    C "So maybe I just wanted to take you out for a walk."
                    N "You chuckle softly before looking around the beach."
                    Y "It's pretty..."
                    C "I can see something... or someone... prettier than the beach..."
                    N "Cepeda takes a piece of paper out of his pocket."
                    Y "What is that?"
                    C "A poem. Tha last one until I finish to say what I want to say."
                    N "Cepeda opens the paper."
                    Y "Is it about me?"
                    C "This time I won't pretend it isn't."
                    C "... Yes."
                    N "You found yourself marveling at how every word that came out of Cepeda's motuh was spoken with such intent that it made your heart skip a beat."
                    Y "..."
                    C "I probably should have put it more simply."
                    Y "No."
                    C "No?"
                    Y "I think it was romantic..."
                    C "Anyway, I'll put it more directly."
                    N "Silence."
                    C "It's not just because you're interesting. Or because you're different. I like talking to you. I like it when you argue. I like it when we disagree."
                    C "I like everything of you."
                    C "I want to keep getting to know you. No rush."
                    Y "And if I want the same thing?"
                    C "Then I guess this trip was worth it."
                    scene black
                    N "END..."

        elif C_relationship > Pe_relationship:
            play music "olas.mp3" volume 0.5 loop
            scene mar with fade:
                fit "cover"
            show Cepeda at center
            N "It's night time. You walk alongside Cepeda, barefoot on the sand. There was no noise from the polluted city, just waves crashing against each other."
            Y "I still can't understand why did you bring me to Cartagena."
            C "Because you said that you wanted to get to know a place where you can forget about everything."
            Y "I don't remember saying that."
            C "Then maybe I just wanted to take you out for a walk."
            N "You chuckle softly before looking around the beach."
            Y "It's pretty..."
            C "I can see something... or someone... prettier than the beach..."
            N "Cepeda takes a piece of paper out of his pocket."
            Y "What is that?"
            C "A poem. Tha last one until I finish to say what I want to say."
            N "Cepeda opens the paper."
            Y "Is it about me?"
            C "This time I won't pretend it isn't."
            C "... Yes."
            N "You found yourself marveling at how every word that came out of Cepeda's motuh was spoken with such intent that it made your heart skip a beat."
            Y "..."
            C "I probably should have put it more simply."
            Y "No."
            C "No?"
            Y "I think it was romantic..."
            C "Anyway, I'll put it more directly."
            N "Silence."
            C "It's not just because you're interesting. Or because you're different. I like talking to you. I like it when you argue. I like it when we disagree."
            C "I like everything of you."
            C "I want to keep getting to know you. No rush."
            Y "And if I want the same thing?"
            C "Then I guess this trip was worth it."
            scene black
            N "END..."

        elif C_relationship == Pe_relationship:
            scene patio with fade:
                fit "cover"
            show Cepeda at right
            show Petro at left
            N "You open the door to your house. In the entryway, Cepeda and Petro were standing in front of you."
            Pe "So... who are you choosing?"
            C "You don't have to answer inmediately."
            Pe "Of course she has to answer."
            C "Don't pressure her."
            Pe "You've been writing her poems for weeks."
            C "And you've been trying to compete with me for weeks."
            Pe "Because it works."
            C "It works?"
            Pe "She hasn't shut the door on us, has she?"
            menu:
                "I choose Petro.":
                    play music "Music audio.mp3" volume 0.5 loop
                    scene black
                    N "END..."

                "I choose Cepeda.":
                    play music "Music audio.mp3" volume 0.5 loop
                    scene black
                    N "END..."

                "Why do I have to choose?" if C_relationship >= 8:
                    N "Silence."
                    Pe "What?"
                    C "I think I understand what she's asking."
                    Pe "I don't"
                    Y "I like both of you."
                    Y "I don't want to have to decide which one I like better."
                    Y "I want to be with both of you."
                    N "Complete silence."
                    Pe "..."
                    C "..."
                    Y "Was that a no?"
                    play music "Music audio.mp3" volume 0.5 loop
                    Pe "I didn't said it was a no."
                    C "Neither did I."
                    Y "So what do we do?"
                    N "Cepeda smiles"
                    C "Give it a try."
                    Pe "All three of us?"
                    C "Exactly."
                    Pe "I'll still be competitive."
                    C "But it'll be fun."
                    scene black
                    N "END..."