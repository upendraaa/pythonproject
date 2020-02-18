print("My python");

car =["Honda city","Nexon","Eco sport"]
print("All cars: ",car)
print("Number of cars ",len(car))
print("First car ",car[0])
print("Pop  first car ",car.pop(0))
print("Append car ",car.append("Santro"));


print("\n"+"Iterate all cars")
for car_mode in car:
    print(car_mode)

    count = 0
    while count < len(car):
        print(car[count])
        count = count+1
print("List inside the list")

address = ['India',['Karnataka',['Bangalore',['Kudlu gate']]]]

print(address[1][1][1][0])


def iterateList(l_list):
    for itemList in l_list:
        if isinstance(itemList, list):
            iterateList(itemList)
        else:
            print(itemList)

            iterateList(address)

for country_item in address:
    if isinstance(country_item,list):
        for state_item in country_item:
            if isinstance(state_item,list):
                for capital_item in state_item:
                    if isinstance(capital_item,list):
                        for item in capital_item:
                            if isinstance(item,list):
                                for suItem in item:
                                    print(suItem)
                                else:
                                    print(item)
                            else:
                                print(capital_item)
                    else:
                        print(state_item)
                else:
                    print(country_item)
"""Here is my commentx"""






