# Part G - Applied Challenge: Console study tracker

# 1
print("Q-1")
study_sessions = [
    {
        "subject" : "Python Fundamentals",
        "minutes" : 30
    },
    {
        "subject" : "SQL",
        "minutes" : 30
    },
    {
        "subject" : "Object Oriented Programming",
        "minutes" : 40
    },
    {
        "subject" : "JavaScript",
        "minutes" : 30
    },
    {
        "subject" : "Swedish SFI",
        "minutes" : 15
    },
    {
        "subject" : "Machine Learning",
        "minutes" : 60
    },
    {
        "subject" : "Deep Learning",
        "minutes" : 50
    },
    {
        "subject" : "API",
        "minutes" : 20
    },
    {
        "subject" : "Testing",
        "minutes" : 20
    },
    {
        "subject" : "Automation",
        "minutes" : 30
    }
]
print()

# 2
print("Q-2")
total = 0
for session in study_sessions :
    total = total + session["minutes"]
print(total)
print()


# 3
print("Q-3")
subject_sessions = {}
for session in study_sessions:
    subject = session["subject"]   # assigning subject's value to subject variable
    minutes = session["minutes"]   # assigning minutes's value to minutes variable
    if subject not in subject_sessions:  # looping empty dictionary and assigning
        subject_sessions[subject] = 0
    subject_sessions[subject] += minutes

print(subject_sessions)
print()

# 4
print("Q-4")
max_session = study_sessions[0]["minutes"]
subject_name = study_sessions[0]["subject"]
for session in study_sessions :
    if max_session < session["minutes"] :
        max_session = session["minutes"]
        subject_name = session["subject"]
print(f"{subject_name} : {max_session}")
print()


# 5
print("Q-5")
longer_session = 45
for session in study_sessions :
    if session["minutes"] > longer_session :
        print(f"{session['subject']} : {session['minutes']}")
print()


# 6
print("Q-6")
menu = input("Select option from menu : \n 1. view all sessions \n 2. view total \n 3. filter by subject \n 4. quit \n")
print()
while menu != "4" :
    if menu == "1" :
        for session in study_sessions :
            print(f"{session["subject"]} : {session["minutes"]} mins")
    elif menu == "2" :
        total = 0
        for session in study_sessions :
            total = total + session["minutes"]
        print(total)
    elif menu == "3" :
        for i, session in enumerate(study_sessions, start=1):
            print(f"{i}. {session["subject"]}")
        print()
        choice = input("Select the subject number: ")
        chosen = study_sessions[int(choice)-1]
        print(f"{chosen["subject"]} : {chosen["minutes"]}")
    menu = input("Select option from menu : \n 1. view all sessions \n 2. view total \n 3. filter by subject \n 4. quit \n")
print()


# 7
print("Q-7")
while True:
    menu = input("Select option from menu : \n 1. view all sessions \n 2. view total \n 3. filter by subject \n 4. quit \n")

    if menu == "4":
        break

    if menu == "1":
        for session in study_sessions:
            print(f"{session['subject']} : {session['minutes']} mins")
    elif menu == "2":
        total = 0
        for session in study_sessions:
            total += session["minutes"]
        print(total)
    elif menu == "3":
        for i, session in enumerate(study_sessions, start=1):
            print(f"{i}. {session['subject']}")
        choice = input("Select the subject number : ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(study_sessions)):
            print("Invalid number, try again")
            continue
        chosen = study_sessions[int(choice) - 1]
        print(f"{chosen['subject']} : {chosen['minutes']} mins")
    else:
        print("Invalid option, try again")
        continue
