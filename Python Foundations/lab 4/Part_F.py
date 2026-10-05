# Part F - Applied challenge: Event registration processor

# 1. Create functions to normalize a participant name,
# validate an age range using boolean return values,
# calculate a registration fee based on age/student status, and
# create a participant dictionary.
# 2. Create at least eight participant dictionaries using your functions.
# 3. Write a function that receives the participant list and returns the total expected registration revenue.
# 4. Write a function that returns only student participants.
# 5. Write a function that returns the oldest participant.
# 6. Write a function that creates a readable summary string for one participant.
# 7. Keep input/output responsibilities separate from calculation functions as much as possible.

#============================================================================================================


# 1
def participant_name(name):
    return name.strip().lower()

def validate_age(age):
    return age >= 18 and age <= 100

def registration_fee(age, student_status):
    if not validate_age(age):
        return 0
    elif student_status:
        return 100
    else:
        return 500

def participant(name, age, student_status):
    return {
        "name": participant_name(name),
        "age": age,
        "student": student_status,
        "fee": registration_fee(age, student_status)
    }

# 3
def expected_reg_revenue(partpnts):
    total = 0
    for participant in partpnts:
        total = total + participant["fee"]
    return total

# 4
def student_participants(partpnts):
    student_participants =[]
    for participant in partpnts:
        if participant["student"]:
            student_participants.append(participant["name"])
    return student_participants


# 5
def oldest_participant(partpnts):
    oldest = partpnts[0]["name"]
    age = partpnts[0]["age"]
    for participant in partpnts:
        if participant["age"] > age:
            age = participant["age"]
            oldest = participant["name"]
    return oldest, age


# 6
def participant_summary(partpnt):
    summary = f"""
    Participant Details :
    ==========================
    Name : {partpnt["name"]}
    Age : {partpnt["age"]}
    Student : {partpnt["student"]}
    Reg. Fees : {partpnt["fee"]}
"""
    return summary


if __name__ == "__main__":

    print("Q-1")
    print("Normalizing participant name, validating age, registration fees and creating participant dictionary are separate functions")
    print()

    # 2
    print("Q-2")
    participant_1 = participant("John", 18, True)
    participant_2 = participant("Bob", 17, True)
    participant_3 = participant("Alice", 22, False)
    participant_4 = participant("Vijay", 25, True)
    participant_5 = participant("Suriya", 24, False)
    participant_6 = participant("Ajith", 28, True)
    participant_7 = participant("Aishu", 50, False)
    participant_8 = participant("Ram", 13, True)
    participants =[participant_1, participant_2, participant_3, participant_4, participant_5, participant_6, participant_7, participant_8]
    # print(participants)
    print(f"Participants : \n{participant_1},\n{participant_2},\n{participant_3},\n{participant_4},\n{participant_5},\n{participant_6},\n{participant_7},\n{participant_8}")
    print()

    # 3
    print("Q-3")
    expected_registration_revenue = expected_reg_revenue(participants)
    print(f"Expected registration revenue : {expected_registration_revenue}")
    print()

    # 4
    print("Q-4")
    student_participant_list = student_participants(participants)
    print(f"Student participants list : {student_participant_list}")
    print()

    # 5
    print("Q-5")
    oldest, age = oldest_participant(participants)
    print(f"Oldest participant is {oldest}, age is {age}")
    print()

    # 6
    for p in participants:
        summary = participant_summary(p)
        print(summary)
