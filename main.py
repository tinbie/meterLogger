import matplotlib as mlp
import matplotlib.pyplot as plt
from meter import Meter

meter = Meter()

def startScreen():
	print('	Meterlogger')
	print('*******************')
	print('\nChoose an Option!')

def createNewMeter():
	_name = input('Name your meter! ')
	_count = input('... metercount? ')
	meter.createMetertable(_name, _count)

# Convert table[[a1,b1],[a2,b2]] to table[[a1,a2],[b1,b2]],
# which is necessary to plot the metercounts.
def plotMetercounts(_meterList):
	_dateList = []
	_countList = []

	for date, count in _meterList:
		_dateList.append(date)
		_countList.append(count)

	_dateList.pop(0)
	_countList.pop(0)
	plt.plot(_dateList, _countList)
	plt.grid(True)
	plt.show()

def addMetercount(_meterName):
	_collectingDate = input('Date: ')
	_collectingCount = input('Count: ')
	meter.setMetercount(_meterName, _collectingDate, _collectingCount)

def main():
	choose = "0"
	choose = input("1 - New meter\n2 - Existing meter\n")

	if choose == "1":
		createNewMeter()

	elif choose == "2":
		existingMeters = meter.getExistingMetertables()
		print('Existing Meters are: ', *existingMeters, sep = '\n')
		name = input('Data of which one? ')
		meterList = meter.openMetertable(name)
		print(meterList)
		plotMetercounts(meterList)

	while True:
		chooseToEdit = input('Adding new count? [y/n] ')
		if chooseToEdit == "y":
			addMetercount(name)			
		else:
			break

#*************************START************************

if __name__ == '__main__':
	startScreen()
	main()
	input('\nPress ENTER to exit')