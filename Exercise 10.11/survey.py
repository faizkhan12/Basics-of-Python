class AnnonymousSurvey():
    """collect annonymous answer to a survey question"""

    def __init(self,question):
        self.question=question
        sef.responses=[]

    def show_question(self):
        print(question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_results(self):
        print("Survey Results:")
        for response in responses:
            print(response)
