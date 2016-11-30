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
fiTCo = {}
regxFileType = re.compile(r'\.(\w)+$')
regxSpaces = re.compile(r'\s')

#TODO: Check if directory exists, throw error and stop script if not

outFile.write('Target directory: ' + tarDir + '\n')
for dirs, subdirs, files in os.walk(tarDir):
	files = [f for f in files if not f[0] == '.']
	subdirs[:] = [s for s in subdirs if not s[0] == '.']
	#dirs = [d for d in dirs if not d[0] == '.']
	
	newDir = regxSpaces.sub('_', dirs)
	outFile.write('Current directory: ' + dirs + '\n')
	outFile.write(newDir + '\n')
	#TODO: use newDir to rename directory instead of writing to file
	
	for fiName in files:
		newFName = regxSpaces.sub('_', fiName)
		outFile.write('File in ' + dirs + ': ' + fiName + '\n')
		outFile.write('CHANGED TO: ' + newFName + '\n')
		#TODO: Figure out how to exclude certain file types
		#TODO: use newFName to rename file instead of writing
		fiTMat = regxFileType.search(fiName)
		if fiTMat is not None:
			fiTCo.setdefault(fiTMat.group(), 0)
			fiTCo[fiTMat.group()] = fiTCo[fiTMat.group()] + 1
	
	outFile.write('::  \n')

outFile.write('==================================================\n')

for k, v in fiTCo.items():
	outFile.write('Key: ' + k + ' Value: ' + str(v) + '\n')

print('Done!')
outFile.close()

# === FOOTNOTES ===============================================================
# === END OF CODE =============================================================
