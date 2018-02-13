## Reading csv file
import csv
import pathlib
import os.path

newCSV = open("newFileToWrite.csv", 'w', newline='')
                                        # 'w' for erase all and write as new, newline='' for removing blank next lines
writer = csv.writer(newCSV)
with open('train.csv') as csvFile:      # open csv file to read the data from it
    readCSV = csv.reader(csvFile)       # save opened file to variable
    firstRow = next(readCSV)            # read only the first row in the file
    writer.writerow(firstRow)           # write the 1st row that is on variable

    for row in readCSV:                 # read row by row in a loop
        rows = row[0] + '.png'          # append '.png' (any string if needed) extension with the names in the first column of the csv file
        joined_path = os.path.join("C:/", rows)  # join path with variable filename. This is to check 'if file exists' in later line of code.
        path = pathlib.Path(joined_path)  # list the file names row exists in the given directory
        if path.exists():               # check if the file exists or not
            writer.writerow((row))  # write each rows to new file
newCSV.close();                         # close the opened new csv