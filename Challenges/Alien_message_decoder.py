'''
Challenge 2: Alien Message Decoder
Concepts: Strings, Loops

The player encounters an alien terminal displaying a scrambled message.
They must write a loop to reverse the string and reveal the secret message.
'''
def message_decoder(message):
    formatted_message = message.replace(" ","").lower()
    return formatted_message[::-1]

input_msg = input("Enter the Alien messages here : ")
result = message_decoder(input_msg)
print(result)