#Beautiful Binary String
""" Alice has a binary string. She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a 0 to a 1 or vice versa. Count and print the minimum number of steps needed to make Alice see the string as beautiful.

For example, if Alice's string is  she can change any one element and have a beautiful string.

Function Description
Complete the beautifulBinaryString function in the editor below. It must return an integer representing the minimum number of moves required.

Input format
b = "binary string"

Output format
Minimum number of steps required to make the string beautiful
"""

def beautifulBinaryString(s):
    count = 0
    i = 0
    while i <= len(s)-3:
        if "010" == s[i:i+3]:
            count+=1
            i+=3
        else:
            i+=1
    return count



if __name__ == "__main__":
    string = "010"
    print(beautifulBinaryString(string))