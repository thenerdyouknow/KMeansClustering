import random
import string
import csv

final_transactions = []
for i in range(10000):
	current_transaction = []
	number_of_items = 2
	for j in range(number_of_items):
		random_item = random.uniform(-21000,21000)
		if random_item not in current_transaction:
			current_transaction.append(random_item)
	final_transactions.append(current_transaction)

with open('dummy_dataset.csv','w') as open_file:
	csv_writer = csv.writer(open_file)
	for each_transaction in final_transactions:
		csv_writer.writerow(each_transaction)
