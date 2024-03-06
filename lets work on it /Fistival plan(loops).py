'''
plan for event festival and there is many booth types 
and activity and you have to make a task to iterate each of task with specific booth
'''
# use the for loop to iterate the booth types:
# for each booth type print the type of booth, the schedule time, and the item needed.
# ensure that each booth type match with the correct schedul time and item needed for list provided.


boot_types = ("foods", "games", "music", "crafts")
schedul_times = ("10:00 AM", "1:00 om", "3:00 PM", "5:00 PM")
item_needed = ("Grill", "tickets", "instruments", "paint")

for i in range(len(boot_types)):
    booth = boot_types[i]
    time = schedul_times[i]
    item = item_needed[i]
    print(f"{booth} Booth - Shcedul: {time}, Item needed: {item}")








