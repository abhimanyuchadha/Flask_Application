from flask import Flask
from flask import request
from itertools import permutations	


app =	Flask(__name__)

@app.route("/")
def index():
 return  "This is a web application for calculating permutations"

@app.route("/calculate", methods=['GET', 'POST'])
def permutaions():
	message=request.args.get('message')
	if len(message)<2 or len(message)>9:
		return "Please enter at-least 2 & at-most 9 alphabets!!!"
	print message+"----------------------------------------------------------------------------"
	perms = [''.join(p) for p in permutations(message)]
	print "......................................................................."+perms[0]
	unique=set()

	for stri in perms:
	    unique.add(stri.encode('ascii', 'ignore'))

	listOfUniqueNames=list(unique)
	return str(listOfUniqueNames)
	

if __name__ == "__main__":
 app.run()

