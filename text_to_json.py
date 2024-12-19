
import json

# Save event content from a txt file to a json file

event_dataset = []
years = []

with open("wch_data.txt") as new_file:
    for line in new_file: 

        line = line.replace("\n", "")
        
        # Treat singular and plural forms as the same concept (focusing on some keywords for now)
        if "woman" in line.lower():
            line = line.lower().replace("woman", "women")
        if "student " in line.lower():
            line = line.lower().replace("student ", "students ")
        if "miner " in line.lower():
            line = line.lower().replace("miner ", "miners ")
        if "soldier " in line.lower():
            line = line.lower().replace("soldier ", "soldiers ")
        if "mau mau" in line.lower():
            line = line.lower().replace("mau mau", "maumau")


        event = {} # each event is stored in a dictionary
        date_year = ""

        i = 0
        count_space = 0

        # Date is the substring before the 3rd space
        while i < len(line):  
            if line[i] == " ":
                count_space += 1
            i += 1
            if count_space == 3:
                break
        
        # Events are put in a dictionary; date as key, event text as value
        date_year = line[:i-1]
        event[date_year] = line[i:] 
        event_dataset.append(event) 
        years.append(int(date_year[-4:]))


# Write events in a json file
with open("wch_events.json", "w") as outfile:
    json.dump(event_dataset, outfile)


print(f"Latest record: {max(years)}")
print(f"Earliest record: {min(years)}")


'''
# Find events that contain certain keyword within a time range
events_range = []
count_range = 0
for event in event_dataset:
    for key, value in event.items():
        if "miners" in value.lower() and int(key[-4:]) >= 1900 and int(key[-4:]) <= 1920:
            events_range.append(event)
            count_range += 1

print(events_range)
print(count_range)

'''