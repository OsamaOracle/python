class test:

    teamcolor  = "Blue"
    points = 0

    def tellscore(self):
        print ("I am", self.teamcolor,",", " we have ", self.points, " Points!")
    def goal(self):
        self.points += 1
    def printscore(self):
         print("The", self.teamcolor, "contender has", self.__points, "points!")


def fucntion_main():
    word = test ()
    word.goal()
    word.tellscore()

if __name__ == '__main__':
    fucntion_main()
