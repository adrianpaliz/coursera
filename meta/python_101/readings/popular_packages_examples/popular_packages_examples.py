# Popular packages
# Numpy
'''
import numpy as np

six_zeros = np.zeros(6)
print(six_zeros)

variable_2 = np.full ((2, 10), 0.7)
print(variable_2)

variable_3 = np.linspace(0, 25, 7)
print(variable_3)

print(type(variable_3))
'''

# Pandas
'''
import pandas as pd

variable = pd.DataFrame({'Animals' : ['Dog', 'Cat', 'Lion', 'Cow', 'Elephant'],
                         'Sounds' : ['Barks', 'Meow', 'Roars', 'Moo', 'Trumpet']})

print(variable)
print(variable.describe())

variable_2 = pd.DataFrame({
    'Letters' : ['a', 'b', 'c', 'd', 'e', 'f'],
    'Numbers' : [12, 7, 9, 3, 5, 1]})

print(variable_2.sort_values(by = 'Numbers'))
variable_2 = variable_2.assign(new_values = variable_2['Numbers'] * 3)
print(variable_2)
'''
# NLTK
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."

# Print statement 1
print(word_tokenize(text))

# Print statement 2
print(nltk.tokenize.sent_tokenize(text))

stopwords = stopwords.words("english")
new_text = []
for word in text.split():
    if word not in stopwords:
        new_text.append(word)

# Print statement 3
print(new_text)

