from meter import Meter

meter = Meter()

def startScreen():
	print('	Meterlogger')
	print('*******************')
	print('\nChoose an Option!')

def createNewMeter():
	_name = input('Name your meter! ')
	_count = input('... metercount? ')
	meter.createTable(_name, _count)

def defineExistingMeter():

def main():
	choose = "0"
	choose = input("1 - New meter\n2 - Existing meter\n")

	if choose == "1":
		createNewMeter()

	elif choose == "2":
		existingMeters = meter.checkForTables()
		print('Existing Meters are: ', *existingMeters, sep = '\n')
		name = input('Data of which one? ')
		print(meter.openTable(name))
		
		chooseToEdit = input('Editing? [y/n] ')
		
		if chooseToEdit == "y": 
			collectingDate = input('Date: ')
			collectingCount = input('Count: ')
			meter.setCounter(name, collectingDate, collectingCount)

		else:
			return()

#*************************START************************

if __name__ == '__main__':
	startScreen()
	main()
	input('\nPress ENTER to exit')