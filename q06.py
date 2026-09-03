s = "  Life is too short, you need Python  "
s_1 = s.strip()

print(len(s), len(s_1))
print(s_1.count("o"))
print(s_1.find("short"), s_1.find("Java"))
print(s_1.replace("Python", "Java"))
print(s_1.split())
print(len(s_1.split()))