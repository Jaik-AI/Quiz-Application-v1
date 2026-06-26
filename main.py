questions = [{"question":"What is the capital of India?","Options":["A. Mumbai","B. Delhi","C. Chennai","D. Kolkata"],"Answer":"B"},
             {"question":"What is 2 + 2?","Options":["A. 3","B. 5","C. 4","D. 6"],"Answer":"C"},
             {"question":"Which data type stores key-value pairs in Python?","Options":["A. List","B. Tuple","C. Set","D. Dictionary"],"Answer":"D"},
             {"question":"Which keyword is used to define a function in Python?","Options":["A. function","B. define","C. def","D. fun"],"Answer":"C"},
             {"question":"Which loop is used when the number of iterations is known?","Options":["A.while","B. for","C. do-while","D. repeat"],"Answer":"B"}]
score = 0
total_questions = len(questions)
print(f"Welcome to Python Quiz\nTotal Questions : {total_questions}\nPassing Marks : 40%\nLet's begin!\n")
for i in questions:
    print(i["question"])
    for j in i["Options"]:
        print(j)
    n = input("Select answer:").upper()
    valid_inputs = ["A","B","C","D"]
    
    while(n not in valid_inputs):
        print("Please select A,B,C or D.")
        n = input("Select answer:").upper() 

    if(n==i["Answer"]):
        print("Correct Answer!\n")
        score += 1
    else:
        print(f"Wrong Answer!\nCorrect Answer is {i['Answer']}.\n")

percentage = (score/total_questions)*100

print(f"\nCorrect Answers : {score}")
print(f"\nWrong Answers : {total_questions-score}")
print(f"\nTotal Score : {score}/{total_questions}")
print(f"\nPercentage : {percentage}%")
if(percentage<40):
    print("Result : Fail")
else:
    print("Result : Pass")


    
