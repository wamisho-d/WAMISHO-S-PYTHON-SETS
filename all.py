# Question 1 Task:Flight Route Comparison.
#1.Destinations that both airlines fly to.  
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
common_destinations = our_routes.intersection(competitor_routes )
print("Destinations that both airlines fly to:", common_destinations)

#2 Destinations unique to your airline. 
unique_to_your_airline = our_routes.difference(competitor_routes)
print("Destinations unique to your airline:", unique_to_your_airline)

#3 Whether there are any destinations that neither airline shares. 
all_possible_destinations = {"LAX", "JFK", "CDG", "DXB", "LHR", "BKK"}
niether_airline_destinations = all_possible_destinations.difference(our_routes.union(competitor_routes))
print("Destinations that neither airline shares:", niether_airline_destinations)

# Question 2 Task 1:  Duplicate Entries Cleanup
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = set(customer_ids)
print(unique_customer_ids )