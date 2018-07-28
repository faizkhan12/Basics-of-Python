from survey import AnnonymousSurvey
question="What language you know?"
my_survey=AnnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' at any time to quit!!")
flag=True
while flag:
    response=input("Language:")
    if response=='q':
        break
    my_survey.store_response(response)
print("Thank you")
my_survey.show_results()
