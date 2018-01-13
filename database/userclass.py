from seeker import *
#user = Seeker("James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", "Univeristy of Sydney - Bachelor of Science,PhD in Computing Linguistics @ Sydeny Univeristy", "Coding,Running buisinesses,Reading storiess,spelling", "Python,everythgin","NCSS")
#print(user.fname)
#user.new_user()

#print(get_seeker())
create_seeker(["James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", "Univeristy of Sydney - Bachelor of Science,PhD in Computing Linguistics @ Sydeny Univeristy", "Coding,Running buisinesses,Reading storiess,spelling", "Python,everythgin", "jamie", "123", "my name is james"])

var = get_seeker(1)

#exp = Experience("GOOGLE", "Intern", "5/5", var.id)
#exp.save()

var.add_review("0/5", "terrible")
print(get_review(1))

print(get_seekers()[0])

##
