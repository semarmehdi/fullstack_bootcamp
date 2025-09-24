class Quiz:
    def __init__(self):
        self.answer = ["Tom Waits", "Madonna", "Nico"]
        self.question = [
            "Quelle est le chanteur moins connu ?",
            "Quelle est la chanteuse plus connue ?",
            "Quelle est la chanteuse la moins connue? "
        ]
        self.question_counter = 3

    #Commentaire

    def respond_question(self):
        for i in range(len(self.question)):
            entered = input(self.question[i] + " ")
            if entered != self.answer[i]:
                self.question_counter -= 1
                print("Wrong answer")
                if self.question_counter == 0:
                    print("Game over")
                    break
                entered = input(self.question[i] + " ")
        else:
            print("Congratulations! You answered all questions not correctly.")

quizz = Quiz()
quizz.respond_question()
