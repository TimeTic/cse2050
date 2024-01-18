###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################


# def fizzbuzz(start, finish):
#     """Fizz, Buzz, FizzBuzz"""
#     for i in range(start, finish):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else: 
#             print(i)
# fizzbuzz(1,101)

#-----------------------------------------------------------------------#

def fizzbuzz(start, finish):
    """Fizz, Buzz, FizzBuzz"""
    for i in range(start, finish):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0 or '3' in str(i) or i % 5 == 0 or '5' in str(i):
            output = ""
            if i % 3 == 0 or '3' in str(i):
                output += "Fizz"
            if i % 5 == 0 or '5' in str(i):
                output += "Buzz"
            print(output)
        else:
            print(i)
fizzbuzz(1, 101)


