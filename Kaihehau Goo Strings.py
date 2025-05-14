### Kaihehau Goo Strings
import re
# This is a Python script that generates a list of strings based on the input string.
course= """ Today you will be reading my extended rant on why Cars 2 is actually a good movie. Cars 2 often gets a bad rap compared to other Pixar films, but it actually has several qualities that make it an enjoyable and underrated movie — especially if you view it on its own terms. Here's why Cars 2 is a good movie: Instead of following the formula of the first movie. Cars 2 shifts into spy thriller territory. Essentially turning into an animated James Bond-style adventure.
This bold genre change brings fast-paced action, global stakes, and high-tech gadgets, which is refreshing for a family film. Mater, the comic relief in the first film, becomes the heart of this one. His character evolves from a bumbling sidekick to someone who saves the day by staying true to himself.
The film explores themes of identity, self-worth, and friendship in a surprisingly meaningful way. The racing sequences are exciting and dynamic, especially with the “World Grand Prix” format.
There are tons of car-related Easter eggs and references for automobile fans. Notably the film features a variety of international cars, showcasing different cultures and designs.
The animation is top-notch, with stunning visuals and vibrant colors. The attention to detail in the car designs and environments is impressive.
The voice cast is stellar, with returning actors like Owen Wilson and Larry the Cable Guy reprising their roles as Lightning McQueen and Mater, respectively. Newcomers like Emily Mortimer as Holley Shiftwell and John Turturro as Francesco Bernoulli add depth to the story.
Michael Caine as British spy Finn McMissile is a standout. He brings charm and gravitas.It doesnt try to be emotional. It leans into being a fun, flashy action-comedy that’s more aboutIn short, if you accept Cars 2 as a spy-action adventure rather than a traditional Pixar coming-of-age story, it’s actually a pretty fun ride."""
#2. Count the number of times "e" appears in the string
print("this is the number of characters:", len(course))
target_e= "e"
course_lower=course.lower()
sum=(course_lower.count("e")+course_lower.count("E"))
print("this is the number of eʻs", sum)

#3. Count the number of times "b" appears in the string
#print("this is the number of bʻs", (course.count("b"))+course.count("B"))
course= course.lower()
sum_b= course.count("b")
print(sum_b)


#4 print the first 20 characters after the first occurrence of "e" 
# (I set the keyword to "e" because I thought it would be good to use a keyword funct.)
target_occurence= "e"
# Find the first occurrence of the keyword
position = course.find(target_occurence)
# Check if the keyword was found
if position != -1:
    print(f"This is the number of characters before the first '{target_occurence}':", position)
    
    # Find where the target_occurance ends

    end_of_target_occurence = position + len(target_occurence)
    
    # Slice the original course string to get text after keyword

    text_after = course[end_of_target_occurence:(end_of_target_occurence+20)]
    # Print the first 20 characters or i guess units of text, idk what the right word is, after the first occurrence of the keyword
    print(f"Text after the first '{target_occurence}':", text_after.strip())
    # Find the last occurrence of the keyword
    #last_position = course.rfind(keyword)
    # this line is redundant and it might be better to js use the else
else:
    print(f"The keyword '{target_occurence}' was not found.")


#5 find the number of words
print("this is the number of words", len(course.split(" ")))
#or at least the number of spaces between letter characters. Honestly, I don't know what happened with that message text so it might be off.

#6 find the number of sentences
print("this is the number of sentences", len(course.split(".")))
#or at least the number of periods

#6 find the shortest sentence
# Split the course into sentences using regex (was I allowed to use regex? I don't know)
# I guess I could have used the split method but this is something I wanted to try because I had used split before
# and I wanted to see if I could do something different. 
sentences = re.split(r'(?<=[.!?]) +', course)
shortest_sentence = min(sentences, key=lambda s: len(s.split()))
print("This is the shortest sentence:", shortest_sentence)

#7 count the number of unique words
course = course.lower()
# Convert the whole course to lowercase
words = course.replace(".", " ").replace(",", " ").split()
# Remove duplicates by converting to a set and splitting by whitespace
unique_words = set(words)
# Count the number of unique words
print("Number of unique words:", len(unique_words))
# Print the unique words


#7 again lol capitalize all the H's
course = course.lower()
# Convert the whole course to lowercase
course = course.replace("h", "H")
#replace all occurrences of 'h' with 'H'
print(course)
# This is a Python script with all the H's capitalized.


