import datetime

current_time = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
status = {
    1:'Add',
    2:'View',
    3:'Delete',
    4:'Exit'
}
# function for add log file
def write_log(log):
    file = open('log.txt', 'a')
    file.write(log)
    file.close()

# empty question list
ques_List = []

print("\nwelcome to tops quiz gaming challenge\n".upper().center(20," "))
while True:
    print("select your role".upper().center(60,"-"))
    print("-> Quiz Master   (press 1)".center(60," "))
    print("-> Quiz Cracker  (press 2)".center(60," "))
    print("-> Exit          (press 3)".center(60," "))
    ask = input("Enter your role: ")
    if ask.isdigit():
        ask = int(ask)
        # exit from outer loop
        if ask == 3:
            break
        # after press 1 
        if ask == 1:  
            print() 
            print("welcome master".upper().center(60,"-"))
            print("shake your brain and add some challenging questions...".upper())
           
            # this loop is for question master
            while True:
                ques_dict = {}
                print("MENU".center(60,"-"))
                print("press 1 for add questions".center(60," "))
                print("press 2 for view questions".center(60," "))
                print("press 3 for delete questions".center(62," "))
                print("press 4 for exit".center(50," "))
                masterAsk = input("\nwhich operation you want to perform: ")
                if masterAsk.isdigit():
                    masterAsk = int(masterAsk)
                    if 1<=masterAsk<=4:
                        # for exit form question master loop
                        if masterAsk == 4:
                            print("GoodBye Master !!")
                            log_msg = f'{current_time} - [{status[4]}]\n'
                            write_log(log_msg)
                            break

                        # for add question 
                        if masterAsk == 1:
                            addQue = input("\nEnter question: ").lower()
                            print("you can add only 2 options !!")
                            addOp1 = input("Enter option 1: ").lower()
                            # this loop is for user add same option 
                            while True:
                                addOp2 = input("Enter option 2: ").lower()
                                if addOp2 !=addOp1:
                                    break
                                else:
                                    print("Both option are same\nplease enter different option !!".upper())
                            while True:
                                addAns = input("Enter right answer: ").lower()
                                if addAns == addOp1 or addAns == addOp2:
                                    break
                                else:
                                    print(f"Please enter right answer either [option1:{addOp1}] or [option2:{addOp2}]")

                            ques_dict['question'] = addQue
                            ques_dict['option1'] = addOp1
                            ques_dict['option2'] = addOp2
                            ques_dict['answer'] = addAns

                            if ques_dict not in ques_List:     
                                ques_List.append(ques_dict)
                            else:
                                print("this question is already present!!")

                            log_msg = f'{current_time} - [{status[1]}]\n'
                            write_log(log_msg)
                                
                            print("Question is added Successfully !!")

                        # for view question
                        if masterAsk == 2:
                            if len(ques_List) == 0:
                                print("Question list is empty\nplease add some question then you can perform view operation".upper())
                            elif len(ques_List)>=1:
                                quesNo = 1
                                for i in ques_List:
                                    print(f"Q{quesNo}.) {i['question']}".upper())
                                    print(f"A) {i['option1']}".upper())
                                    print(f"B) {i['option2']}".upper())
                                    print(f"Answer: {i['answer']}".upper())
                                    quesNo +=1
                                    print()
                        # for delete question
                        if masterAsk == 3:  
                            if len(ques_List) == 0:
                                print("Question list is empty\nplease add some question then you can perform delete operation".upper())
                            elif len(ques_List)>=1:
                                queDel = input("Which Question you want to delete: ").lower()
                                for i in ques_List:
                                    if i['question'] == queDel:
                                        confirDel = input("Are you sure to delete this question?(y/n): ").lower()
                                        if confirDel == 'y':
                                            log_msg = f'{current_time} - [{status[3]}]\n'
                                            write_log(log_msg)
                                            ques_List.remove(i)
                                            print("ThankYou for your confirmation\nThis question will deleted")
                                            break
                                        else:
                                            print("ThankYou for your confirmation no question will deleted.") 
                                else:
                                    print("No question was found !!")                  
                    else:
                        print("please enter valid choice !!".upper())                   
                else:
                    print("please enter valid choice !!".upper())
        # for attempt quiz 
        if ask == 2:
            totalQues = len(ques_List)
            marks = 0
            ques_no = 1
            if len(ques_List)==0:
                print("Question list is empty !!")
                print("Please add some questions")
                print("To add some question press 1 !!")
            elif len(ques_List)>=1:
                for i in ques_List:
                    print(f"Q{ques_no}.) {i['question']}".upper())
                    print(f"A) {i['option1']}".upper())
                    print(f"B) {i['option2']}".upper())
                    answer_input = input("Enter your answer: ").lower()
                    if answer_input == i['answer']:
                        print("Correct !!")
                        print()
                        marks = marks + 1
                    else:
                        print("Incorrect !!")
                        print()
                    ques_no += 1
                print(f"Your score is: {marks} , Out of: {totalQues}")
                yesNo = input("Do you want to play more?(y/n): ").lower()
                if yesNo != 'y':
                    break

    else:
        print("please enter valid choice".upper()) 