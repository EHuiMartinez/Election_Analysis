print("Hello World")
counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties = ["Arapahoe", "Denver", "Jefferson"]
if 'El Paso' in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahow" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

#different ways to get dictionary with loop
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

for county, voters in counties_dict.items():
    print(county, voters)

#to display key values with string!
for county, voters in counties_dict.items():
    print(county + " county has ", str(voters) + "registered voters.")

#to display key values with comma!
for county, voters in counties_dict.items():
    print(county, " county has ", voters, "registered voters.")

#get dictionary in list of dictionaries
voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, 
                {"county": "Denver", "registered_voters": 463353}, 
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#use range()
for i in range(len(voting_data)):
    print(voting_data[i])

#use nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#get number of registered voters from dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])

#get only county name from dictionary
for county_dict in voting_data:
    print(county_dict['county'])

#print using f-string
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#print multi line f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the elction was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

#Import the datetime class from the datetime module.
import datetime as dt
#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# print present time
print("The time right now is ", now)
