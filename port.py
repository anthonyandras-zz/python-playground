"""
port.py

example for parsing csv file and printing it's results
without the use of the csv library
"""
#f = open('Data/portfolio.csv', 'r')
total = 0.0

with open('Data/portfolio.csv', 'r') as f:
	headers = next(f)	# skip header
	for line in f:
		line = line.strip()
		parts = line.split(',')
		parts[0] = parts[0].strip('"')
		parts[1] = parts[1].strip('"')
		parts[2] = int(parts[2])
		parts[3] = float(parts[3])
		print(parts)
		total += parts[2] * parts[3]

print('Total cost:', total)
