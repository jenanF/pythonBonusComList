students = [{"name" : "jenan", "age" : 17}, {"name" : "amal", "age" : 15}, {"name" : "ayah", "age" : 22}]

profile = [print("hello this is", s["name"],"i am", s["age"], "years old") for s in students]

people = [{"name" : "manal", "age" : 20}, {"name" : "salman", "age" : 29}, {"name" : "sarah", "age" : 13},{"name" : "ali", "age" : 19}]

adults = [p["name"] for p in people if p["age"] >=18 ]

adult = [print("welcome", p["name"],"you can enter") if p["age"] >=18 else print("sorry", p["name"], "you are under age") for p in people]

print(adults)