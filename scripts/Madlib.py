"""
In this program
we will play a game
called Mad Libs.
"""
print "Mad Libs is starting now!"
name = raw_input("Name the main character: ")
adj1 = raw_input("Type the first adjective: ")
adj2 = raw_input("Type the second adjective: ")
adj3 = raw_input("Type the third adjective: ")
verb1 = raw_input("Type the first verb: ")
verb2 = raw_input("Type the second verb: ")
verb3 = raw_input("Type the third verb: ")
noun1 = raw_input("Type the first noun: ")
noun2 = raw_input("Type the second noun: ")
noun3 = raw_input("Type the third noun: ")
noun4 = raw_input("Type the forth noun: ")
animal = raw_input("Type an animal: ")
food = raw_input("Type a food: ")
fruit = raw_input("Type a fruit: ")
number = raw_input("Type a number: ")
superhero = raw_input("Type a superhero name: ")
country = raw_input("Type a country name: ")
dessert = raw_input("Type a dessert: ")
year = raw_input("Type a year: ")

#The template for the story
STORY = "This morning I woke up and felt %s because %s was going to finally %s over the big %s %s. On the other side of the %s were many %ss protesting to keep %s in stores. The crowd began to %s to the rythym of the %s, which made all of the %ss very %s. %s tried to %s into the sewers and found %s rats. Needing help, %s quickly called %s. %s appeared and saved %s by flying to %s and dropping %s into a puddle of %s. %s then fell asleep and woke up in the year %s, in a world where %ss ruled the world."
print STORY % (adj1, name, verb1, adj2, noun1, noun2, animal, food, verb2, noun3, fruit, adj3, name, verb3, number, name, superhero, superhero, name, country, name, dessert, name, year, noun4)
