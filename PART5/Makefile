PYTHON = python3

# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help setup

# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help
	
run:
	@${PYTHON} plain_cipher_text_generation.py $(path)
	@${PYTHON} Cryptanalysis_decoder.py $(path)

