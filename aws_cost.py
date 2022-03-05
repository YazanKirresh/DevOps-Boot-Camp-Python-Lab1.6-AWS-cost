

# This function will calculate the cost of the selected server depending on how many hours the user enters here. It will also show a cheaper server if found
def calculate_cost(hourly_cost,selected_server):

    rent_hours = input("Enter how many hours you want to rent the server for: ")
    rent_hours = int(rent_hours)
    total_cost = round(rent_hours * hourly_cost,5)
    print("This server will cost: " + str(total_cost) + " for: " + str(rent_hours) + " hour(s)") 
    server_costs = []
    cheaper_servers = []
    j = 1
    cheapest = True
    while j != 7:
        possible_new_cost = round(server[j].get("cost") * rent_hours,5)
        if possible_new_cost < total_cost :
            print("Server (" + str(j) + "), is cheaper than the current server (" + str(selected_server) +"). It will cost " + str(possible_new_cost) + ", instead of " +str(total_cost))
            cheapest = False
        server_costs.append(possible_new_cost)
        j = j + 1
    if cheapest == True:
       print("The server you choose is the cheapest available server!")



# Dictionaries
server = {
    1: {"server_id": 1, "region": "eu-central-1", "location": "Frankfurt", "zone": "3", "cost": 0.012},
    2: {"server_id": 2, "region": "eu-west-1", "location": "Ireland", "zone": "3", "cost": 0.0114},
    3: {"server_id": 3, "region": "eu-west-2", "location": "London", "zone": "3", "cost": 0.0118},
    4: {"server_id": 4, "region": "eu-south-1", "location": "Milan", "zone": "3", "cost": 0.012},
    5: {"server_id": 5, "region": "eu-west-3", "location": "Paris", "zone": "3", "cost": 0.0118},
    6: {"server_id": 6, "region": "eu-north-1", "location": "Stockholm", "zone": "3", "cost": 0.0108}}

# Printing the current list of available servers
print("1) " + server[1].get('location'))
print("2) " + server[2].get('location'))
print("3) " + server[3].get('location'))
print("4) " + server[4].get('location'))
print("5) " + server[5].get('location'))
print("6) " + server[6].get('location'))

i = 0
current_cost = 0


""" will loop untill the user chooses a server, then it will print the chosen server details and will call the function that calculates the cost of the selected server. 
It will need the user to enter how many hours they want to rent the server for.
"""
while (i == 0):
    selected_server = input("Enter a number from 1 to 6 to select a region: ")
    selected_server = int(selected_server)
    if 1 > selected_server > 6:
        print("Please enter a valid region 'Between 1 and 6' ")
    else:
        i=1
        print("Server Location: " + str (server[selected_server].get('location')))
        print("Server region: " + str (server[selected_server].get('region')))
        print("Server cost/h: " + str (server[selected_server].get('cost')))
        current_cost = calculate_cost(server[selected_server].get('cost'),selected_server)

