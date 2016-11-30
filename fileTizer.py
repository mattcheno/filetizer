#! python3

# === BOILERPLATE =============================================================
#
#  FileTizer
#  Matthew Chenoweth
#  2016/11/30

# --- Declarations ------------------------------------------------------------
import os, shutil, re

# --- Logic -------------------------------------------------------------------
print('Enter directory location')
tarDir = input()
outFile = open('output.txt', 'w')
regxIgnore = re.compile(r'^[.]', re.I)

#TODO: Check if directory exists, throw error and stop script if not

outFile.write('Target directory: ' + tarDir + '\n')
for dir, subdirs, fileNames in os.walk(tarDir):
	dirMat = regxIgnore.search(dir)
	outFile.write('Current directory: ' + dirmat.group() + '\n')
	
#	for dirName in subdirs:
#		outFile.write('Sub-directory of ' + dir + ': ' + dirName + '\n')
	
	for fiName in fileNames:
		fiMat = regxIgnore.search(fiName)
		outFile.write('File in ' + dir + ': ' + fiMat.group() + '\n')
	
	outFile.write('::  \n')

print('Done!')
outFile.close()

# === FOOTNOTES ===============================================================
# === END OF CODE =============================================================