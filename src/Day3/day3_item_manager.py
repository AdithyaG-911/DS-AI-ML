inventory=['Appples','Bananas','Carrots','Dates']
print("Items :",inventory)

inventory.append('Eggs')
print("New Inventory After Eggs Arrived :\n",inventory)

inventory.remove('Bananas')
print("Inventory After Bananas sold out :\n",inventory)

inventory.sort()
print("Sorted Inventory items :\n",inventory)
