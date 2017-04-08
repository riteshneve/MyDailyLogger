from flask import Flask, redirect, url_for, request, render_template, json, jsonify
import collections
from flaskext.mysql import MySQL
import datetime
from math import ceil

mysql = MySQL()
app = Flask(__name__)
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'myDailyLogger'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

def getDoneKMs():
	print "[INFO] IN GET DONE KMS"
	doneKMs = 0
	
	cursor = conn.cursor()
	query = "SELECT kms from info"
	cursor.execute(query)
	
	result = list(cursor.fetchall())
	for element in result:
		if element[0] != "":
			doneKMs += int(element[0])
	print "[INFO] Completed KMs: "+str(doneKMs)
	return doneKMs

def getDailyKMsData():
	print "[INFO] IN GET DAILY DATA"
	dailyKMsDict = {}
	cursor = conn.cursor()
	query = "SELECT dates,kms from info"
	cursor.execute(query)
	
	result = list(cursor.fetchall())
	for element in result:
		dateFormat = int(str(element[0])[0:4]+str(element[0])[6:]+str(element[0])[4:6])
		if dailyKMsDict.has_key(dateFormat):
			dailyKMsDict[dateFormat] += int(element[1])
		else:
			dailyKMsDict[dateFormat] = int(element[1])
			
	dailyKMsDict = collections.OrderedDict(sorted(dailyKMsDict.items()))
	#print dailyKMsDict
	output = "["
	for dailyKey in dailyKMsDict.keys():
		output += "[Date.UTC("+str(dailyKey)[0:4]+","+str(int(str(dailyKey)[4:6])-1)+","+str(dailyKey)[6:]+"),"+str(dailyKMsDict[dailyKey])+"],"
	output = output[:-1]
	output += "]"
	#print output
	#return "[[Date.UTC(2017,0,28),470],[Date.UTC(2017,1,05),3],[Date.UTC(2017,1,23),3]]"
	return output

def getWeeklyKMsData():
	print "[INFO] IN GET WEEKLY DATA"
	weeklyKMs = []
	cursor = conn.cursor()
	query = "SELECT dates,kms from info"
	cursor.execute(query)
	
	for i in range(53):
		weeklyKMs.append(0)
	result = list(cursor.fetchall())
	for element in result:
		yearVal = int(str(element[0])[0:4])
		monthVal = int(str(element[0])[6:])
		dateVal = int(str(element[0])[4:6])
		kmVal = int(element[1])
		if monthVal == 1 and dateVal == 1:
			continue
		weekNumber = datetime.date(yearVal, monthVal, dateVal).isocalendar()[1]
		if weekNumber < 53:
			weeklyKMs[weekNumber] += kmVal
			
	#print weeklyKMs
	output = str(weeklyKMs)
	#print "[INFO] WeeklyKMs: "+output
	return output

def getWeekOfMonth(dt):
    first_day = dt.replace(day=1)
    dom = dt.day
    adjusted_dom = dom + first_day.weekday()
    return int(ceil(adjusted_dom/7.0))

def getMonthlyKMsData():
	print "[INFO] IN GET MONTHLY DATA"
	monthlyKMs = []
	cursor = conn.cursor()
	query = "SELECT dates,kms from info"
	cursor.execute(query)
	
	for i in range (6):
		monthlyKMs.append([0,0,0,0,0,0,0,0,0,0,0,0])
	
	result = list(cursor.fetchall())
	for element in result:
		yearVal = int(str(element[0])[0:4])
		monthVal = int(str(element[0])[6:])
		dateVal = int(str(element[0])[4:6])
		weekVal = getWeekOfMonth(datetime.datetime(yearVal, monthVal, dateVal))
		kmVal = int(element[1])
		if weekVal < 7:
			if monthVal < 12:
				monthlyKMs[weekVal-1][monthVal-1] += kmVal

	#print monthlyKMs
	output = monthlyKMs
	#print "[INFO] MonthlyKMs : "+str(output)
	return output

def getLatestData():
	print "[INFO] IN GET LATEST DATA"
	dateInput = datetime.datetime.now().strftime("%Y%d%m")
	currDate = datetime.datetime.now()
	for i in range (6):
		currDate = datetime.datetime.now() + datetime.timedelta(days=-(i+1))
		dateInput += " OR dates="+currDate.strftime("%Y%d%m")
	cursor = conn.cursor()
	query = "SELECT dates,kms,summary from info where dates="+dateInput
	#print query
	cursor.execute(query)
	
	latestData = []
	result = list(cursor.fetchall())
	result1 = []
	for element in result:
		targetDate = int(str(element[0])[0:4] + str(element[0])[6:] + str(element[0])[4:6])
		result1.append((targetDate, element[1], element[2]))
	result1 = sorted(result1,key=lambda l:l[0], reverse=True)
	for element in result1:
		yearVal = int(str(element[0])[0:4])
		monthVal = int(str(element[0])[4:6])
		dateVal = int(str(element[0])[6:])
		kmVal = int(element[1])
		descVal = str(element[2])
		latestData.append([str(dateVal)+"/"+str(monthVal)+"/"+str(yearVal), kmVal, descVal])
	#print latestData
	return latestData

@app.route("/")
def main():
	targetKMs = 10000
	doneKMs = getDoneKMs()
	dailyKMsData = getDailyKMsData()
	weeklyKMsData = getWeeklyKMsData()
	monthlyKMsData = getMonthlyKMsData()
	latestData = getLatestData()
	return render_template('index.html', targetKMs=targetKMs, doneKMs=doneKMs, dailyKMsData=dailyKMsData, weeklyKMsData=weeklyKMsData, monthlyKMsData=monthlyKMsData, latestData=latestData)

@app.route('/enterData', methods=['POST'])
def enterData():
	print "[INFO] IN ENTER DATA"
    # read the posted values from the UI
	inDate = str(request.form['inputDate'])
	inKMs = str(request.form['inputKMs'])
	inDesc = str(request.form['inputDesc'])
	print "[INFO] input Date:"+inDate+" inKMS"+inKMs+" inDesc"+inDesc
	
	if not inDate:
		return jsonify({'message':'Date is not entered'})
	if not inKMs:
		return jsonify({'message':'KMs is not entered'})
	if not inDesc:
		return jsonify({'message':'Description is not entered'})
	
	splitedString = inDate.split("-")
	inDate = splitedString[0]
	inDate += splitedString[2]
	inDate += splitedString[1]
	#print "[INFO] Date converted to :"+inDate
	
	cursor = conn.cursor()
	#cursor = mysql.get_db().cursor()
	#cursor.callproc('sp_createUser',('qwe','qwe','qwe'))
	#data = cursor.fetchall()

	query = "INSERT INTO info (dates, kms, summary) VALUES ("+inDate+", "+inKMs+", '"+inDesc+"')"
	cursor.execute(query)
	conn.commit()
	#print "[INFO] Query Executed"
	return jsonify({'message':'Record entered successfully!'})

@app.route('/enterDateLimits', methods=['POST'])
def enterDateLimits():
	print "[INFO] IN ENTER DATE LIMITS"
	inStartDate = str(request.form['inputStartDate'])
	inEndDate = str(request.form['inputEndDate'])
	if not inStartDate:
		return jsonify([{'date':'', 'kms':'', 'desc':'ERROR : Start date is empty'}])
	if not inEndDate:
		return jsonify([{'date':'', 'kms':'', 'desc':'ERROR : End date is empty'}])
	print "[INFO] input StartDate: "+inStartDate+" EndDate: "+inEndDate
	splitedString = inStartDate.split("-")
	startDate = datetime.date(int(splitedString[0]), int(splitedString[1]), int(splitedString[2]))
	splitedString = inEndDate.split("-")
	endDate = datetime.date(int(splitedString[0]), int(splitedString[1]), int(splitedString[2]))
	if startDate > endDate:
		return jsonify([{'date':'', 'kms':'', 'desc':'ERROR : Start date is less than end date'}])
	
	dateInput = startDate.strftime("%Y%d%m")
	while startDate != endDate:
		startDate = startDate + datetime.timedelta(days=1)
		dateInput += " OR dates="+startDate.strftime("%Y%d%m")
	cursor = conn.cursor()
	query = "SELECT dates,kms,summary from info where dates="+dateInput
	#print query
	cursor.execute(query)
	
	latestData = []
	result = list(cursor.fetchall())
	result1 = []
	for element in result:
		targetDate = int(str(element[0])[0:4] + str(element[0])[6:] + str(element[0])[4:6])
		result1.append((targetDate, element[1], element[2]))
	result1 = sorted(result1,key=lambda l:l[0])
	for element in result1:
		yearVal = int(str(element[0])[0:4])
		monthVal = int(str(element[0])[4:6])
		dateVal = int(str(element[0])[6:])
		kmVal = int(element[1])
		descVal = str(element[2])
		latestData.append({'date':str(dateVal)+"/"+str(monthVal)+"/"+str(yearVal), 'kms':str(kmVal), 'desc':descVal})
	#print latestData
	if len(latestData) == 0:
		latestData.append({'date':'', 'kms':'', 'desc':'ERROR : No data found'})
	return jsonify(latestData)

if __name__ == '__main__':
	app.run(debug = True)