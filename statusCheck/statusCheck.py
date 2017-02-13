

class statusCheck:

    def __init__(self, userInput, correctCode):

        self.__userInput = userInput
        self.__correctCode = correctCode # Get correct code from database.

    def checkCorrectCode(self):

        if self.__userInput == self.__correctCode:

            # change the status on the database
            # do something here

            # do something to make the bot say this
            print("\nThe confirmation code is correct! \nWelcome to McBot!")
            return True

        else:

            # do something to make the bot say this
            print("\nThe confirmation code is not correct.")
            return False

    def getUserInput(self):

        return self.__userInput

    def getCorrectCode(self):

        return self.__correctCode

    def setUserInput(self, newUserInput):

        self.__userInput = newUserInput

    def setCorrectCode(self, newCorrectCode):

        self.__correctCode = newCorrectCode
