# Create, define and edit meter and metercounts with this class
# with pickle as a database. 

import pickle
import os

class Meter:
	def __init__(self):
		print()

	# Check for existing tables and return names.
	def checkForTables(self):
		_existingMeters = []
		for filename in os.listdir():
			if filename.count(".pkl")>0:
				_existingMeters.append(filename[:-4])
		return(_existingMeters)

	# Create table and pickles.
	def createTable(self, _tableName, _count):
		_meterData = [["Name", _tableName], ["22.07", _count]]
		pickle.dump(_meterData, open(_tableName+".pkl", "wb"))

	# Open existing table per name and returns it.
	def openTable(self, _tableName):
		_meterTable = pickle.load(open(_tableName+".pkl", "rb"))
		return(_meterTable)

	# Set counter for existing meter.
	def setCounter(self, _tableName, _date, _count):
		_meterTable = pickle.load(open(_tableName+".pkl", "rb"))
		_collectingInfos = [_date] + [_count]
		_meterTable.append(_collectingInfos)
		pickle.dump(_meterTable, open(_tableName+".pkl", "wb"))
		