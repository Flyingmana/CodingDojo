import os, parser, time

os.system('clear')
while True:
	f = open('pattern')
	patterns = parser.parse(f.read())
	f.close()

	for delay, pattern in patterns:
		for i in range(0,4):
			print pattern[i*4:i*4+4]
		time.sleep(delay)
		os.system('clear')
