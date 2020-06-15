import csv

# Print csv file
def csvread(file1):
	with open(file1,newline='') as csvfile:
		spamreader = csv.reader(csvfile,delimiter=' ',quotechar='|')
		for rowA in spamreader:
			print(','.join(rowA))

# Add rows at bottom of csv
def rowdataread(file1, file2):
	with open(file2,newLine='') as datafile:
		reader = csv.reader(datafile)
		header = next(reader)
 		for row in reader:
  			if row[0] in my_dict.keys():
 	    		my_dict[row[0]].extend(row)
 	 		else:
     			my_dict[row[0]]=row
		for v in my_dict.values():
    		writer.writerow(v)

	with open(file1,newline='') as csvfile:
   		writer = csv.writer(csvfile)
   		writer.writerow(header)
   		for row in uniqueMaster:
       		writer.writerow(row) 

# Add rows to right of csv
def columndataread(file1, file2):
	all_filenames = [file1, file2]
	combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
	combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')


# execution order

file1 = input("Name of file1: ")
file2 = input("Name of file2: ")
mytype = input("Row or Column Merge (Type: 'R' or 'C'): ")

if mytype == "R":
	rowdataread(file1,file2)
	csvread(file1)
elif mytype == "C":
	columndataread(file1,file2)
	csvread(file1)
else:
	print("Error: Must type 'R' or 'C' (capitalized)")
