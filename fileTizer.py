#! python3

# === BOILERPLATE =============================================================
#
#  FileTizer
#  Matthew Chenoweth
#  2016/11/30

# --- Declarations ------------------------------------------------------------
import os, shutil#, re

# --- Logic -------------------------------------------------------------------
print('Enter directory location')
tarDir = input()
outFile = open('output.txt', 'w')
#regxIgnore = re.compile(r'^[.]', re.I)

#TODO: Check if directory exists, throw error and stop script if not

outFile.write('Target directory: ' + tarDir + '\n')
for dirs, subdirs, files in os.walk(tarDir):
	#dirMat = regxIgnore.search(dir)
	files = [f for f in files if not f[0] == '.']
	subdirs[:] = [s for s in subdirs if not s[0] == '.']
	#dirs = [d for d in dirs if not d[0] == '.']
	
	outFile.write('Current directory: ' + dirs + '\n')
	
#	for dirName in subdirs:
#		outFile.write('Sub-directory of ' + dirs + ': ' + subdirs + '\n')
	
	for fiName in files:
		#fiMat = regxIgnore.search(fiName)
		outFile.write('File in ' + dirs + ': ' + fiName + '\n')
	
	outFile.write('::  \n')

print('Done!')
outFile.close()

# === FOOTNOTES ===============================================================
# === END OF CODE =============================================================
