highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)
highlighted_poems_list = []
highlighted_poems_list = highlighted_poems.split(',')
#print("\n", highlighted_poems_list)

highlighted_poems_stripped = []
for i in highlighted_poems_list:
  stripped_name = i.strip()
  highlighted_poems_stripped.append(stripped_name)
  
#print('\n',highlighted_poems_stripped)

highlighted_poems_details = []

for i in highlighted_poems_stripped:
  new_item = i.split(":")
  highlighted_poems_details.append(new_item)
#print('\n',highlighted_poems_details)

titles = []
poets = []
dates = []

for list in highlighted_poems_details:
  titles.append(list[0])
  poets.append(list[1])
  dates.append(list[2])
  print("The poem {} was published by {} in {}.".format(list[0], list[1], list[2]))
  

print("\n", "Titles", "\n", titles)
print("\n","Poets", "\n", poets)
print("\n","Dates", "\n", dates)

