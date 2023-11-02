authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"
author_names = authors.split(",")
print("Authors' first and last names")
print(author_names)
author_last_names= []
for name in author_names:    
    split_author_name = name.split(" ")
    last_name = split_author_name[1]
    #print(author_last_names)
    author_last_names.append(last_name)
  
#author_last_names = ", ".join(author_last_names)
print(author_last_names)

  