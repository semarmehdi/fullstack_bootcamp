class Quiz:
    def __init__(self):
        self.answer = ["Tom Waits", "Madonna", "Nico"]
        self.question = [
            "Quelle est le chanteur moins connu ?",
            "Quelle est la chanteuse plus connue ?",
            "Quelle est la chanteuse la moins connue? "
        ]
        self.question_counter = 3

    def respond_question(self):
        for i in range(len(self.question)):
            entered = input(self.question[i] + " ")
            while entered != self.answer[i]:
                self.question_counter -= 1
                if self.question_counter == 0:
                    print("Game over")
                    return
                print("Wrong answer")
                entered = input(self.question[i] + " ")
        print("Congratulations! You answered all questions correctly.")

        quizz = Quiz()
        quizz.respond_question()
