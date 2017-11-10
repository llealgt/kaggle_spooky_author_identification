import sys
import os
import csv
from nltk.tokenize import sent_tokenize

reload(sys)  
sys.setdefaultencoding('utf8')

def validatePathName(pathName):
	if(pathName.endswith('/')):
		return pathName
	else:
		return pathName + '/'

# once tokenized sentences, perform some line cleaning
def clean_line(line):
	#cleaning 1: remove new line characters
	line = line.replace('\n', ' ')
	
	return line

#devInputPath = '/home/erick/Documents/kaggle/edgar_philip_love_poe/corpus'
#devOutputPath = '/home/erick/Documents/kaggle/kaggle_spooky_author_identification/'
devInputPath = '/Users/erickdiaz/Documents/kaggle_spooky_author_identification/edgar_philip_love_poe/corpus'
devOutputPath = '/Users/erickdiaz/Documents/kaggle_spooky_author_identification/kaggle_spooky_author_identification/'
outputFileName = 'newData.csv'

sourcePath = validatePathName(devInputPath if ( len(sys.argv) < 2 ) else sys.argv[1])
outputPath = validatePathName(devOutputPath if (len(sys.argv) < 3) else sys.argv[2])

outFile = outputPath + outputFileName

if os.path.exists(outFile):
	os.remove(outFile)

authorsDict = {'poe' : 'EAP', 'lovecraft' : 'HPL','shelley':'MWS' }

print('Input path:',validatePathName(sourcePath))
print('Output path:',outputPath)

dirs = next(os.walk(sourcePath))[1]

for path in dirs:
	currentReadPath = validatePathName(sourcePath + path)
	author = authorsDict[path]
	print('-->' + path)
	files = os.listdir(currentReadPath)

	for file in files:
		if (file.endswith('txt')):
			print('|----------- ' + file)

			with open((currentReadPath+file), 'r') as f:
				text=f.read()
				
			print(text)
			newData = sent_tokenize(text)
			print(outFile)

			with open(outFile, 'a') as csvfile:
			    fieldnames = ['author', 'text']
			    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)

			    for text in newData:
					text = clean_line(text)
					print(author + '###########' + text)
					writer.writerow({'author': author, 'text': text})
