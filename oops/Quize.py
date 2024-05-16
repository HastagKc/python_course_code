class Quize:
    def __init__(self,question,answer) -> None:
        self.question=question
        self.answer=answer


questions=[
    "what is the full form of OOP?\n a.object oriented programming\n b.nothing \n c.none of the above \n d.object oriented python",
    "what is the Full form of ABC?\n a.Apple ball cow \n b.abstract base class \n c.abstarct basic clss \n d.nothing",
    "what is color of orange?\n a.orange color\n b.yellow color \n c.black color \n d.nothing"

]

Quize_list=[
    Quize(questions[0],"a"),
    Quize(questions[1],"b"),
    Quize(questions[2],"a"),

]

def show(lst):
    score=0
    for i in lst:
        user=input(f"{i.question}\n")
        if user==i.answer:
            score+=1
        else:
            print(f"you enter wrong option ,The correct answer is {i.answer}")
    print(f"you score {score}/{len(questions)}")
            

show(Quize_list)