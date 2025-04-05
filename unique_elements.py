#This code of code takes a list with duplicates and returns only the list
#This is one way to solve this 

itemsListing = ['Pineapple', 'Apple','Bread','Apple', 'Milk', 'Apple', 'Segar']
#Casting the current listItems into a set to get rid of the duplicates
unique_list = set(itemsListing)

print(unique_list)
