# Reflection
#
# 1. In Excel I would have to open the file, add a total column, filter
#    it, and copy the rows into a new sheet by hand every time. Python can
#    redo the whole thing in one click on a new file, and it handles huge
#    files that would slow Excel down. Excel is still easier when I just
#    want to look at the data, make a quick chart, or fix a few cells.
#
# 2. A store could keep a daily sales log where a script adds one line
#    with the date and that day's total revenue every night. Append mode
#    is the right tool because it adds the new line to the end without
#    erasing the earlier days, so the file builds a full history over time.

import csv
from datetime import datetime

# Exercise 1: Get the file
# sales.csv is in the data folder, with columns product, price, quantity.
file_path = "data/sales.csv"
with open(file_path) as f:
    print("Opened", file_path, "with no errors")

# Exercise 2: Read and print raw rows
print("\nExercise 2")
with open(file_path) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3: Skip the header
print("\nExercise 3")
with open(file_path) as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: Compute totals
print("\nExercise 4")
total_revenue = 0
with open(file_path) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Filter and write
print("\nExercise 5")
original_count = 0
written_count = 0
with open(file_path) as f_in, open("data/cleaned.csv", "w", newline="") as f_out:
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count += 1
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([row[0], f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count += 1
print(f"Wrote {written_count} of {original_count} rows to data/cleaned.csv")

# Exercise 6: csv.DictReader
# csv.reader is fine for small files where you know the column order.
# DictReader is better when there are many columns or the order might change.
print("\nExercise 6")
dict_total = 0
with open(file_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${dict_total:.2f}")
print("Matches Exercise 4:", round(dict_total, 2) == round(total_revenue, 2))

# Exercise 7: Sales summary by product
print("\nExercise 7")
summary = {}
with open(file_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + line_total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# Exercise 8: Append mode log
print("\nExercise 8")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as log:
    log.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")
print("Added a line to data/run_log.txt")
