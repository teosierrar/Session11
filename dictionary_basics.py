d={}
print(d)

eng_to_spa={"one":"uno","two":"dos", "three":"tres"}
print(eng_to_spa)
print(eng_to_spa["one"])
eng_to_spa["tree"]="arbol"
print(eng_to_spa["tree"])
eng_to_spa.update({"yes":"si", "no":"no"})
print(eng_to_spa)

del eng_to_spa["yes"]
print(eng_to_spa)

print("These are the spanish words thatI know")
for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {eng_to_spa[]}")

print(dir(eng_to_spa))
eng_spa2=eng_to_spa.copy()
eng_to_spa.clear()
print(eng_spa2)
new_d=eng_spa2.fromkeys(eng_spa2,"YES")
print(new_d)

print(f"car in spanish is{eng_spa2('car','UNKNOWN')}")
print(list(eng_spa2.items()))
print(eng_spa2)
eng_spa2.setdefault("red","ROJO!!")
print(eng_spa2)