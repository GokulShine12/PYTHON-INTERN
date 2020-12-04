#Create a JSON of all object types and import the JSON into a SQL Database
import json
#dictionary
print(json.dumps({"Name":"Gokul","doe":20}))
#list
print(json.dumps(["panner","mushroom"]))
#string
print(json.dumps(("DOMINOS","KFC")))
#tuple
print(json.dumps("Shine"))
#integer
print(json.dumps(100))
#float
print(json.dumps(45.4))
#True
print(json.dumps(True))
#False
print(json.dumps(False))
#None
print(json.dumps(None))

