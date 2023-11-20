passage ="""The Chennai Super Kings won a record-equalling fifth Indian Premier League title on Monday 
night, beating 2022 champions Gujarat Titans in a thrilling game in Ahmedabad. The side registered 
victory on the final ball of the match, with Ravindra Jadeja hitting a four when the team required as 
many to seal the title. The CSK required 10 runs off the last two deliveries of the game after Mohit 
Sharma, the Titans bowler, had only conceded three off the first four. Jadeja, however, smashed a
 six off the fifth ball before ending the game in style with a four towards fine leg.The foundation
  of CSK's win was laid by Devon Conway (47) at the start, and then by Ambati Rayudu as he played a
 bright cameo in his last IPL innings. Rayudu stayed at the crease for only 8 deliveries but scored
 a valuable 19 runs for the side as he arrived to bat in the 11th over (the game was shortened to 15 
overs due to rain). Rayudu smashed a four and two sixes in his knock before departing two overs later
"""
x = passage.split()
print(x)
di={}

print(di)
print(di.keys())
for word in x:
    if word not in di.keys():
        di[word] =1 # di["The"]
    else:
        di[word]=di[word]+ 1
print(di)
print(di.items())
kvp = list(di.items())
print(kvp)
def cussort(t):
    return t[0]

sort_kvp=sorted(kvp,key=cussort,reverse=True)
print(sort_kvp)

for tup in sort_kvp:
 print(tup[-1])

