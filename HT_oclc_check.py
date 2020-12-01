import urllib, json, time, sys
print "***************************************\nWelcome to the HathiTrust OCLC Querier.\n***************************************\nThis tool allows you to determine whether HathiTrust holds an item.\n\nAt the prompts you will create or designate an output file (e.g. output.csv).\n\nOutput files must be in the same directory as the Python file or use full directory paths (untested).\n\nWhen inputting OCLC numbers, do not use spaces between commas.\n\nDebug mode allows you to view the progress of the queries.\n"
output = raw_input("Please input the name of the output file you wish to create or use (must be in this directory): ")
debugMode = raw_input("Debug mode: Y/N?")
oclcInput = raw_input("Please input comma-separated OCLC numbers (no space): ")
oclcList = oclcInput.split(",")
f = open(output, 'a')
if len(oclcList) > 50:
	computeTime = float(len(oclcList))/3
	print 'You entered', len(oclcList), 'numbers. This will take about', computeTime , 'seconds.'
for oclc in oclcList:
	oclcVar = 'oclc:' + oclc
	url="http://catalog.hathitrust.org/api/volumes/brief/json/" + oclcVar
	response=urllib.urlopen(url)
	data = json.loads(response.read())
	records = data[oclcVar]['records']
	if records == []:
		f.write(oclc)
		f.write (',no\n')
	else: 
		for record in records.values():
			titles = str(record['titles'])
			f.write(oclc)
			f.write(',yes,"')
			f.write(titles)
			f.write('"\n')
	if debugMode == 'y' or debugMode == 'Y' or debugMode == 'Yes' or debugMode == 'yes':
		print oclc, 'Successful'
	time.sleep(0.333)
print 'Done.'