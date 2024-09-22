#!/usr/bin/env python3

import requests
import string

url='http://10.10.158.48/'
char_set=string.ascii_uppercase

for char in char_set:
	agent={
	'User-Agent':char
	}
	r=requests.get(url,headers=agent)

	print(f"Useragent is {char}")
	print(r.text)
	print(f"Url of this agent is {r.url}")
