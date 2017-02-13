from statusCheck import statusCheck

realCode = "12345"

while True:

    inputCode = input("Your input:")

    check = statusCheck(inputCode, realCode)

    if check.checkCorrectCode() == True:

        break

    else:

        while True:

            answer = input("\nDo you want to us reset the code? Yes/No:")

            if answer.lower() == "yes":

                realCode = input("\nSet the new code: ")
                print("")
                break

            elif answer.lower() == "no":

                print("\nBye! ")
                break

        if answer.lower() == "no":
            break




