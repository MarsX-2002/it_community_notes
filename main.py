def inputNote():
    arrQuestion = []
    print(f'Type "exit" if you wanna stop and see notes')
    for i in range(100):
        userNote = input(f"Your #{i+1} note:\n")
        if userNote == 'exit':
            return arrQuestion
        arrQuestion.append(userNote)
    return arrQuestion

def outputNote(arrQuestion):
    for i in range(len(arrQuestion)):
        print(f'Note #{i+1}:\n{arrQuestion[i]}\n')

def noteStored():
    longText = """
NOTES BY https://www.linkedin.com/in/mirjalol-shavkatov/

Note #1:
4th March, TDIU, IT COMMUNITY UZBEKISTAN

Note #2:
Launch of an IT COMMUNITY OF UZBEKISTAN

Note #3:
I am a citizen of IT COMMUNITY OF UZBEKISTAN

Note #4:
6 guests

Note #5:
My Goal == network for my "PAYWAY" STARTUP

Note #6:
Mahliyo Muxsinova (Linkedin :))

Note #7:
2nd guest: Shavkat Karimov

Note #8:
programmers and criminals

Note #9:
1 programmer

Note #10:
Interested in IT = citizen of IT COMMUNITY

Note #11:


Note #12:
universities , companies, students, developers, founders, 

Note #13:
2000+ citizens

Note #14:
be active and join IT COMMUNITY

Note #15:
POST, SHARE, REACT, COMMENT

Note #16:
LUCKY SEATS :)

Note #17:
3rd guest: LEONID CHERNY  (director of data at UZUM)

Note #18:
motivation story: finish university, what you want (get a first job), salary,job but your education don't match, 2nd-motivation(money{}), 3rd-motivation(title > money),  lvl-4(proof you can be succesful in other field), 

Note #19:
lvl-5(what you give? knowledge)

Note #20:
lvl-6=TOP (part of smth new, smth big)

Note #21:
4th GUEST: BOBUR RAJABOV (CEO AT EVERBESTLAB)

Note #22:
infrastructure IT

Note #23:
mission: 1)meaning, 2)deing=movie (make it worth), 3)legacy | opportunity: | clients: 

Note #24:
mission(listen to signals=problems)

Note #25:
mission too big? quote="if you cant do great things, do small things in a great way!"; company mission(long-run: simon sinek book) 

Note #26:
OPPORTUNITY: choose one, walk into it,, don't look back

Note #27:
CLIENTS: b2b: "joanna clevo": imagine who is ideal client?; can you recommend our project to ONE person? reach out to previus clients; do volunteer work; work aggresivly = leave your step in this world

Note #28:
5th GUEST: AKMALJON MUSAYEV (CEO OF HYPERAPP): PM; broke, no feedback, called company for ceo, i am passionate, i want to work, he hired me, after 3 days fired (learned how company works), wanted to be PM (post facebook), TIMUR AZAMATOV, book(), if you ask they will help (don't afraid), problems(); lenovo day, MAKSIM SH., how can I interested this person, (i have a pain,i need CTO, consult); NEVER BE AFRAID TO ASK HELP

Note #29:
AI GAME (MIDJOURNEY): UZBEK, UPCOMING, VILLAGE, FUTURE, GREEN 

Note #30:
6th GUEST: ALENA VLADIMIRSKAYA (CEO OF iTALENT) {not english speech}; {fire stars}; {head hunter}; {our story}; {pirat=sell talents}; {right time, place, skills}; {igor babushkin=engineer AI Google -> Elon Musk hired him to make better chatGPT -> skill not enough -> be PUPLIC -> be super successful COMMERCIALLY -> now sits embrion of a SUPER STAR -> LINKEDIN + GITHUB + COMMUNITY -> talk your programs -> FORGET YOU'RE INTROVERT -> community helps}

Note #31:
RIGHT PLACE: UZBEKISTAN (world watches, world needs projects)

Note #32:
HONOR OF BEING UZBEK AND DOING UZBEK PROJECTS, world will invest in you

Note #33:
SKILLS: bad coders will be replaced by AI, be actual, don't stick with one skill, ENGLISH

Note #34:
IMPROVE YOUR network, projects with AI, they are ready to invest 

Note #35:
7th GUEST: MUNIRA BEKMURADOVA (toptal community leader): [bad student, chess with NATASHA, Galina Vladimirovna?? (my teacher), chess lead to math, physics and IT]

Note #36:
never stopped learning, 1st

Note #37:
1st (people who surrounds you); 2nd (great teachers= implified growth in future); 3rd (support from parents); 4th(accept difficulties = it makes you stronger); 5th(want to achieve smth big == send to much time on that ;; introvert == helps you make jobs) (concentrate to one thing {enjoy and don't focus on end goal}) ||| 

Note #38:
MIDJOURNEY SPEAKERS (FUTURISTIC + JOURNEY + TECHNOLOGY + IT + TALENTS + IDEA)

Note #39:
WE WILL INVITE ELON MUSK ONE DAY :)

Note #40:
APPLE, META, GOOGLE, NETFLIX, MICROSOFT

Note #41:
UZBEK COMPANIES

Note #42:
BALANCE IN OTHER REGIONS

Note #43:
SHAVKAT KARIMOV PLANS=GOALS (integrate with global IT, world class products, Make Uzbekistan known for IT)

Note #44:
build a bridge from Uzbekistan  to global IT; belarus(WOT), finland(angry birds), Uzbekistan (???)

Note #45:
chess (we made it = we are champions)

Note #46:
the same with IT (really strong at math)

Note #47:
shavkat karimov (from Karshi :) the same like ME)

Note #48:
why linkedin? telegram (mute never use again); linkedin (850M members, 160M senior leaders, 10M CEO, 55M companies, 2M groups); make LinkedIn popular in Uzbekistan; do useful for yourself, exchange of ideas (4 ideas), exchange netween everyone (MILLIONS); 

Note #49:
WIIFM? learn, share, gain exp, make career, networking, interview, education, BIGGEST COMMUNITY IN UZBEKISTAN

Note #50:
WORK TOGETHER = SUCCESS

Note #51:
I AM 182

Note #52:
(((

Note #53:
PIZZA PARTY

Note #54:


Note #55:
PHOTO

NOTES BY https://www.linkedin.com/in/mirjalol-shavkatov/

Process finished with exit code 0

    """
    userAnswer = input("Do you wanna see IT Community notes? [y]/[n]\n")
    if (userAnswer == 'y'):
        print(longText)



notes = inputNote()

outputNote(notes)

noteStored()