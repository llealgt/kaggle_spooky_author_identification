import sys
import os


def validatePathName(pathName):
	if(pathName.endswith('/')):
		return pathName
	else:
		return pathName + '/'


devInputPath = '/home/erick/Documents/kaggle/edgar_philip_love_poe/corpus'
devOutputPath = '/home/erick/Documents/kaggle/kaggle_spooky_author_identification/'

sourcePath = validatePathName(devInputPath if ( len(sys.argv) < 2 ) else sys.argv[1])
outputPath = validatePathName(devOutputPath if (len(sys.argv) < 3) else sys.argv[2])

authorsDict = {'poe' : 'EAP', 'lovecraft' : 'HPL' }

print('Input path:',validatePathName(sourcePath))
print('Output path:',outputPath)

dirs = next(os.walk(sourcePath))[1]

for path in dirs:
	currentReadPath = validatePathName(sourcePath+path)
	print('-->',path)
	files = os.listdir(currentReadPath)
	for file in files[:5]:
		if (file.endswith('txt')):
			print(file)
			with open((currentReadPath+file), 'r') as f:
				text=f.read()
			print(text.split('.')[:4])	