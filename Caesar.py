alphabet=("abcdefghijklmnopqrstuvwxyz")
alphabet=[character for character in alphabet]
print(alphabet)

'''
#another alt to split it into different characters
alphabet=[]
for character in alphabet1:
    alphabet.append(character)
print(alphabet)

'''
direction=input("Type 'encode' to encrypt and 'decode' to decrypt:\n").lower()
text=input("Type your message:\n")
shift=int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes 'original_text" and 'shift_amount' as 2 inputs.
#TODO-2:Inside the 'encrypt()' function,shift each letter of the 'original_text' forwards in the alphabet
#TODO-4:What happens of you try to shift z forwards by 9? Can you fix the code?
#TODO-3:Call the 'encrypt()' function and pass in the user inputs.You should be able to test the code and encrypt a message


def encrypt(original_text,shift_amount):
    cipher_text=''
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text+= alphabet[shifted_position%25]
    print(f"Here is the encoded result: {cipher_text}")

encrypt(original_text=text,shift_amount=shift)


#TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shifted_amount' as inputs


#TODO-2: Inside the 'decrypt()' function,shift each letter of the 'original_text' *backwards* in the alphabet by the shift amount and print the decrypted text.


#TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called caesar().
#Use the value of the user chosen direction variable to determine which funcctionality touse.
#Call the caesar function instead of the encrypt/decrypt and pass it to all the variables direction/shift/text.
