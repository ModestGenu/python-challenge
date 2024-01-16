import csv
import os


      #set path for read
budget_csv = os.path.join("/Users/mother/mod_3_challenge/python-challenge/PyBank/Resources/budget_data.csv")
      
      #lists for month count and profit/loss total
month =[]
Ploss = []
changes =[]

      #open file, remember there's a header
with open(budget_csv, newline="") as csvfile:
   csv_reader = csv.reader(csvfile)
      #save header as variable and print
   csv_header = next(csv_reader)
   #print(f"Header: {csv_header}")

      #start adding months and amounts
   for i in csv_reader:
      month.append(i[0])
      Ploss.append(int(i[1]))

      #preform easy operations
count_month= len(month)
net = sum(Ploss)

      #and trickier operations
changes=[Ploss[i+1]- Ploss[i] for i in range(len(Ploss)-1)]
average_changes = (sum(changes))/(count_month-1)

      #set variables for the greatest and least
greatest_Date= ""
least_Date =""
greatest_Amount=0
least_Amount=0

      #find greatest change and month
for i in range(len(changes)):
   if changes[i] > greatest_Amount:
      greatest_Amount = changes[i]
      greatest_Date = month[i + 1]

      #find greatest decrease
for i in range(len(changes)):
   if changes[i] < least_Amount:
      least_Amount = changes[i]
      least_Date = month[i + 1]

      #print results to terminal
seperator="-"
firstLine=(f"\nFinancial Analysis \n")
secondLine=(f"{seperator:-^26}\n")
thirdLine=(f"Total Months: {count_month}\n")
fifthLine=(f"Total: ${net:,}\n")
sixthLine=(f"Average Change: ${average_changes:,.2f}\n")
seventhLine=(f"Greatest Increase in Profits: {greatest_Date} (${greatest_Amount:,})\n")
eighthLine=(f"Greatest Decrease in Profits: {least_Date} (${least_Amount:,})\n")

      #set path for write
analysis_txt = open("/Users/mother/mod_3_challenge/python-challenge/PyBank/analysis/analysis.txt", "w+")
      #write formatted text to file
analysis_txt.write(firstLine)
analysis_txt.write(secondLine)
analysis_txt.write(thirdLine)
analysis_txt.write(fifthLine)
analysis_txt.write(sixthLine)
analysis_txt.write(seventhLine)
analysis_txt.write(eighthLine)
analysis_txt.close