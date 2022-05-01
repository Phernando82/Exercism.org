"""
Instructions
Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:

how many grains were on a given square, and
the total number of grains on the chessboard
For bonus points
Did you get the tests passing and the code clean? If you want to, these are some additional things you could try:

Optimize for speed.
Optimize for readability.
Then please share your thoughts in a comment on the submission. Did this experiment make the code better? Worse? Did you learn anything from it?

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should always include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. For situations where you know that the error source will be a certain type, you can choose to raise one of the built in error types, but should still include a meaningful message.

This particular exercise requires that you use the raise statement to "throw" a ValueError when the square input is out of range. The tests will only pass if you both raise the exception and include a message with it.

To raise a ValueError with a message, write the message as an argument to the exception type:

# when the square value is not in the acceptable range
raise ValueError("square must be between 1 and 64")

>>> square(8)
128

>>> total()
18446744073709551615

"""


########################################################################################################################

def square(number):
    res = 1
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    for i in range(number - 1):
        res = res * 2

    return res


print(square(64))


def total():
    res = 1
    for i in range(64):
        res = res * 2

    return res - 1

print(total())