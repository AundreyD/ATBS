# Dictionary is object with key value pairs
# Unordered unlike lists
# It all the key value pairs are similar regardless of position, two dictionaries will be considered similar

#character counting program
import pprint
 
message = 'It was a bright cold day in April, and the clocks were striking sixteen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1
# pprint.pprint(count)

#Data structures

#Tic Tac Toe board
theBoard = {'top-l': ' ','top-m': ' ','top-r': ' ','mid-l': ' ','mid-m': ' ','mid-r': ' ','low-l': ' ','low-m': ' ','low-r': ' '}

def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print('-----')
    print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
    print('-----')
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])


printBoard(theBoard)