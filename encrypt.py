#!/usr/bin/python3

##############################################################
##		CS 2500( Fall 2016), Assignment #1, Question #1 	##
##			Script File Name	: encrypt.py                ##
##				Student Name	: Maria Diana Aloysius		##
##					Login Name	: mda184					##
##						MUN #	: 201150919					##
##############################################################	
"""Calculates the encrypted code for a file that needs to be
    ciphered

    Args:
        file: file containing data to be encrypted
        pad: One time PAD Cipher used to encrypt 
        pos: The position in the pad to start encrypting from
        fout: file containing encrypted data

    Returns:
        a file with an encrypted code

    Raises:
        Argument error if certain number of arguments are not passed in
"""

import sys

file = open(sys.argv[1]) #data to be encrypted
fout = open(sys.argv[4], 'w')
pad = open(sys.argv[2]).read()
pos = int(sys.argv[3])
string ="";

if len(sys.argv) != 5 :
    print('usage: python', sys.argv[0], "file file file int")
    sys.exit(1)

else:
    for line in file:
        for x in line:
            if x.isalpha():
                ascii = ord(x.upper()) - ord('A') #ascii for the message
                pad_ascii = ord(pad[pos]) - ord('A')  #ascii for the pad
                encodeascii = (ascii + pad_ascii) % 26
                encodemsg = chr(encodeascii +65) 
                string = string + encodemsg
                pos = pos +1
            elif x.isdigit():
                string += str(x)
    fout.write(string)






		