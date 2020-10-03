from textblob import TextBlob 

text1 ="Python is a great tool."
text = " All infedals will go to hell "

obj1 = TextBlob(text1)
obj2 = TextBlob(text)

print(obj1.sentiment.polarity())
print(obj2.sentiment.polarity())
