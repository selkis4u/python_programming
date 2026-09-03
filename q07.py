email = "hong.gildong@example.com"
id = email[:email.find("@")]
domain = email[email.find("@")+1:]

print(id, domain)

print(email.find("@"))
print(email[0:12], email[13:])
print(email.split("@")[0], email.split("@")[1])
print(id.upper(), domain.split(".")[0])