# Release
# Codename
# Release date
# End of life
# HWE
# End of Full Support
# End of Maintenance Support 1
# End of Extended Life-cycle Support
# Support
# Version

def newFields(eachRowJson):
	if eachRowJson["Release"] is not None: 
		OS_Release = eachRowJson["Release"].split() 
		if len(OS_Release) == 3:
			eachRowJson["Support"] = OS_Release[2]
			eachRowJson["Version"] = OS_Release[1]
		if len(OS_Release) == 2:
			eachRowJson["Version"] = OS_Release[1]
		if len(OS_Release) > 3 and OS_Release[0] == "Windows":
			eachRowJson["Version"] = OS_Release[2]

	return eachRowJson
                        
def checkFields(eachRowJson):
	headerList = eachRowJson.keys()

	checkList = []
	for line in open('field_list.config', 'r'):
		fieldName = line.strip('\n')
		checkList.append(fieldName)

	missingList = list(set(checkList) - set(headerList))

	for item in missingList:
		eachRowJson[item] = None

	return eachRowJson

 
