# Task 3: Catering Choices

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" 
# if yes, otherwise recommend "Gourmet Meals Caterers".




attendees = int(input("Enter number of attendees: "))

venue= "large hall" if attendees > 100 else "conference room"

print(venue)

additional_items= "audio system" if attendees > 100 else "projector"

print(additional_items)

vegetarian = int(input("would you like veggie delight caterers?" ))

if vegetarian: "yes"
print("veggie delight caterers")

vegetarian== "no"
print("Gormet meal caterers")