import requests

response = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
if (response.status_code == requests.codes.ok):
	print(len(response.text))
	print(response.text[:250])

res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try :
	res.raise_for_status()
except Exception as exc:
	print("There was a problem %s" % (exc)) 