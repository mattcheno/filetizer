#! python3

# === BOILERPLATE =============================================================
#
#  FileTizer
#  Matthew Chenoweth
#  2016/11/30

# --- Declarations ------------------------------------------------------------
import os, shutil

# --- Logic -------------------------------------------------------------------
print('Enter directory location')
tarDir = input()

#TODO: Check if directory exists, throw error and stop script if not

#TODO: write this output to a text file instead of the shell

print('Target directory: ' + tarDir)
for dir, subdirs, fileNames in os.walk(tarDir):
	print('Current directory: ' + dir)
	
	for dirName in subdirs:
		print('Sub-directory of ' + dir + ': ' + dirName)
	
	for fiName in fileNames:
		print('File in ' + dir + ': ' + fiName)
	
	print(':: ')

# === FOOTNOTES ===============================================================
# === END OF CODE =============================================================