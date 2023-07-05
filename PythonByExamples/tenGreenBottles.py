#!/usr/bin/python3

# Display the song '10 green bottles'
# Then ask 'How many green bottles will hanging on the wall?'
# If the user answers correctly
#+ Display 'There will be [num] green bottles hanging on the wall'
# If the answer is incorrect
#+ Display 'No, try again' until the answer is correct
# When the number of bottles gets down to 0
# + Display 'There are no more green bottles hanging on the wall'

greenBottlesN = 10
song = "There are [N] green bottles hanging on the wall, " + str(greenBottlesN) + " green bottles hanging on the wall, and if 1 green bottle should accidentally fall"

question = "How many green bottles will be hanging on the wall? "
answerCorrect = "There will be " + str(greenBottlesN) + " green bottles hanging on the wall"
answerWrong = "No, Try Again!"
bottlesFinished = "There are no more green bottles hanging on the wall"

print(song[:10], greenBottlesN)
print(song[14:])
#while greenBottlesN != 0:
#    print(song)
#    ans = int(input(question))
#
#    print("[DEBUG]", ans)
#    if ans == (greenBottlesN-1):
#        greenBottlesN = greenBottlesN - 1
#        print(answerCorrect)
#    else:
#        print(answerWrong)
#
#print(bottlesFinished)
