questions = (("1. Whats My name ?:"),
             ("2. Whats my favourite Colour?:"),
             ("3. What is my Birthday month?:"),
             ("4. Whats my favorite food?:"))

options = (
           ("A. Osborn",    "B. Sam",     "C. Kobby", "D. James"),
           ("A. Red",       "B. Yellow",  "C. Black", "D. Orange"),
           ("A. April" ,    "B. February", "C. March", "D. January"),
           ("A. Fried-rice","B. Noodles",  "C. Kenkey", "D. Jollof")
           
           )
guess = []
answers = ("A","C","C","A").upper()

question_num = 0 


for question in questions:
    print("-----------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    question_num += 1
