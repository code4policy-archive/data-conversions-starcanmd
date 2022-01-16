#!/usr/bin/env python3

import csv
import datetime

# 1. load input.csv into a variable called `polls`

with open('input.csv', 'r') as f:

    reader = csv.DictReader(f)

    polls = list(reader)

# 2. write a new file called output.csv and write a row with two headers: "date" and "approve"

with open('output.csv', 'w') as f:

    writer = csv.writer(f)

    writer.writerow(['date', 'approve'])

# 3. Loop through each row of `polls` 

    for row in polls:

#4. and within that loop... convert the format of `enddate` from "1/22/2017" to "22-Jan-17"

        input_date_format = '%m/%d/%Y'

        output_date_format = '%-d-%b-%y'

        date = datetime.datetime.strptime(row['enddate'], input_date_format)

        new_date = date.strftime(output_date_format)

# 5. write a new row of data with the transformed date and value for "approve" 

        writer.writerow([new_date, row['approve']])
