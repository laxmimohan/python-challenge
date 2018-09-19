import csv

# Files to load and output (Remember to change these)
file_to_load = "budget_data.csv"
file_to_output = "budget_analysis.txt"

# Track variousProfitLoss parameters
total_months = 0
prev_profitloss = 0
month_of_change = []
profitloss_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]
total_profitloss = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as profitloss_data:
    reader = csv.DictReader(profitloss_data)

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_profitloss = total_profitloss + int(row["Profit/Losses"])

        # Track theProfitLoss change
        profitloss_change = int(row["Profit/Losses"]) - prev_profitloss
        prev_profitloss = int(row["Profit/Losses"])
        profitloss_change_list.append(profitloss_change)
        month_of_change.append(row["Date"])

        # Calculate the greatest increase
        if (profitloss_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profitloss_change

        # Calculate the greatest decrease
        if (profitloss_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profitloss_change

# Calculate the AverageProfitLoss Change
profitloss_avg = sum(profitloss_change_list) / len(profitloss_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Profitloss: ${total_profitloss}\n"
    f"Average ProfitLoss Change: ${profitloss_avg}\n"
    f"Greatest Increase in ProfitLoss: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in ProfitLoss: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

