import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
link = 'https://www.myfitnesspal.com/food/search?page=1&search='

all_data = []

# READ DATA FROM CSV FILE------------------------------------------
with open('indian_food.csv') as indian_food:
	csv_food = csv.reader(indian_food, delimiter=',')
	next(csv_food)
	all_items = []
	for item in csv_food:
		all_items = all_items + (item[1].split(","))
		all_unique_items = list(set(all_items))


data = []
for ingredient in all_unique_items:

	ingred = ingredient.strip()
	n_link = driver.get(link + ingred)		## remove whitespace and concat with the link
	
	time.sleep(5)
	try:
		type_item_0 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[1]/div[2]').text
		split_type_and_weight = type_item_0.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_0 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[1]/div[3]').text
		split_three_values = nutrients_0.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)


	except Exception as e:
		# print(data)
		pass

	try:
		type_item_1 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[2]/div[2]').text
		split_type_and_weight = type_item_1.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_1 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[2]/div[3]').text
		split_three_values = nutrients_1.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_2 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[3]/div[2]').text
		split_type_and_weight = type_item_2.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_2 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/div[1]/div[3]/div[3]').text
		split_three_values = nutrients_2.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass
	


	try:
		type_item_3 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[1]/div[2]').text
		split_type_and_weight = type_item_3.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_3 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[1]/div[3]').text
		split_three_values = nutrients_3.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_4 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[2]/div[2]').text
		split_type_and_weight = type_item_4.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_4 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[2]/div[3]').text
		split_three_values = nutrients_4.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_5 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[3]/div[2]').text
		split_type_and_weight = type_item_5.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_5 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[3]/div[3]').text
		split_three_values = nutrients_5.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_6 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[4]/div[2]').text
		split_type_and_weight = type_item_6.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_6 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[4]/div[3]').text
		split_three_values = nutrients_6.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_7 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[5]/div[2]').text
		split_type_and_weight = type_item_7.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_7 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[5]/div[3]').text
		split_three_values = nutrients_7.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass


	try:
		type_item_8 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[6]/div[2]').text
		split_type_and_weight = type_item_8.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_8 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[6]/div[3]').text
		split_three_values = nutrients_8.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass
		


	try:
		type_item_9 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[7]/div[2]').text
		split_type_and_weight = type_item_9.split(',')
		type_of_item = split_type_and_weight[0]
		quantity = split_type_and_weight[1]

		nutrients_9 = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[1]/div/section/div[7]/div[3]').text
		split_three_values = nutrients_9.split('•')

		nutrient_list = []
		for i in split_three_values:
			single_nutrient = i.split(":")
			nutrient_list.append(single_nutrient[0].strip())
			nutrient_list.append(single_nutrient[1].strip())

# ['Calories', '357', 'Carbs', '74g', 'Fat', '1g', 'Protein', '11g']



		nutrient_details = {
			"Item": ingred,
			"Type": type_of_item,
			"Quantity": quantity,
			"Calories": nutrient_list[1],
			"Carbohydrate": nutrient_list[3],
			"Fat": nutrient_list[5],
			"Protein": nutrient_list[7]
		}
		data.append(nutrient_details)

	except Exception as e:
		# print(data)
		pass
		
	# all_data.append(data)

print("all_data::", data)
driver.close()


with open('extracted_ingredients.csv', 'w') as data:
	fieldnames = ['Item', 'Type', 'Quantity', 'Calories', 'Carbohydrate', 'Fat', 'Protein']
	the_writer = csv.DictWriter(data, fieldnames=fieldnames)
	writer.writeheader()
	# the_writer.writerow(['Item', 'Type', 'Quantity', 'Calories', 'Carbohydrate', 'Fat', 'Protein'])

	for i in range(len(all_data)):
		the_writer.writerows({'Item': all_data[i]['Item'], 'Type': all_data[i]['Type'], 'Quantity': all_data[i]['Quantity'], 'Calories': all_data[i]['Calories'], 'Carbohydrate': all_data[i]['Carbohydrate'], 'Fat': all_data[i]['Fat'], 'Protein':all_data[i]['Protein']})