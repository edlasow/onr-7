
d={"name":"python","age":1991,"trend":"yes"}
print(d)
print(d.get("age"))
print(d.keys())
print(d.values())
print(d.items())
print(help(dict.update))
d.update(name="balayya",age=23)
print(d)
d.setdefault("practice","done")
print(d)
d.setdefault("age",2000)
print(d)
d.setdefault("time")
print(d)

