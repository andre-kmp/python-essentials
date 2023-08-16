#!/usr/bin/env python3

# This program returns how many words are there in a message. It is NOT part of the Python Essentials course from LinuxTips.
msg = input("Write your message: ")
word_count = len(msg.rsplit())
if word_count != 0:
	if word_count == 1: agreement = "word"
	if word_count > 1: agreement = "words"
	print(f"It seems that your message has {word_count} {agreement}.\n\nThank you for requesting!\n\nLeaving...")
else:
	print(f"There was nothing as input! Try again!")
