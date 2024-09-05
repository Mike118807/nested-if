# Based on the corrected code from Task 1, further enhance your code to recommend additional things like 
# "audio system" or "projector" based on the number of attendees.



attendees = int(input("Enter number of attendees: "))

venue= "large hall" if attendees > 100 else "conference room"

print(venue)

additional_items= "audio system" if attendees > 100 else "projector"

print(additional_items)