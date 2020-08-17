"""

Change the following list of lists to a list of concatenated strings:

names = [('Asabeneh', 'Yetaeyeh'), ('David', 'Smith'), ('Donald', 'Trump'), ('Bill', 'Gates')]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

"""
names = [('Asabeneh', 'Yetaeyeh'), ('David', 'Smith'), ('Donald', 'Trump'), ('Bill', 'Gates')]
full_names = [' '.join(w) for w in names]
print (full_names)