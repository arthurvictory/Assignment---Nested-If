attendees = int(input("Enter number of attendees: "))
catering = input("Do you want vegetarian meals? (yes/no) ")
venue = "large hall" if attendees > 100 else "conference room"
audio = "audio system" if attendees > 100 else "projector"
meals = "Veggie Delight Caterers" if catering == "yes" else "Gourmet Meals Caterers"
print(venue)
print(audio)
print(meals)