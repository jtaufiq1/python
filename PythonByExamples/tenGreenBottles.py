#!/usr/bin/python3

# Display the song '10 green bottles'
# Then ask 'How many green bottles will hanging on the wall?'
# If the user answers correctly
#+ Display 'There will be [num] green bottles hanging on the wall'
# If the answer is incorrect
#+ Display 'No, try again' until the answer is correct
# When the number of bottles gets down to 0
# + Display 'There are no more green bottles hanging on the wall'

remBottles = 10
while remBottles > 0:
    song = f'''SONG: 10 Green Bottles:
    \tThere are {remBottles} green bottles hanging on the wall
    \t{remBottles} green bottles hanging on the wall
    \tAnd if 1 green bottle should accidentally fall
    '''
    question = "\tHow many green bottles will be hanging on the wall? "

    print(song)
    ans = int(input(question))
    remBottles = remBottles - 1

    if ans == remBottles:
       if remBottles != 0:
            if remBottles == 1:
                b = "bottle"
            else:
                b = "bottles"
            print(f"\nThere will be {remBottles} green {b} hanging on the wall")
       else:
            print("\nThere are no more green bottles hanging on the wall")
    else:
       while ans != remBottles:
           ans = int(input("No, try again: "))
