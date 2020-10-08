import random
import base64

def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    x = input("Enter a number")
    x= int(x)
    if(x % 2 == 0 ):
        print("even")
    else:
        print("odd")

def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    x = random.randrange(1,10)
    y = input("Guess a number")
    while(str(y) != "exit"):
        if(int(y) > x):
            print("too high")
        elif(int(y) < x):
            print("too low")
        else:
            print("correct!")
        y = input("Guess a number")


def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    x = input("Enter a string")
    y = x[::-1]
    if x == y:
        print("palindrome")
    else:
        print("not palindrome")



def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
    f = open(filename, 'wb')
    username = username.encode('ascii')
    password=password.encode('ascii')
    u = base64.b64encode(username)
    p = base64.b64encode(password)
    f.write(u)
    f.write(p)
    f.close()


def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    f = open(filename, 'rb')
    user = f.read()
    pwd = f.read()
    user = base64.b64decode(user)
    pwd = base64.b64decode(pwd)
    print(user)
    print(pwd)
    f.close()


if __name__ == "__main__":
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")