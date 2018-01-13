from seeker import Seeker, create_seeker, get_seeker, get_experience, Experience, get_seekers
from position import Position, create_position, get_position
#user = Seeker("James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", "Univeristy of Sydney - Bachelor of Science,PhD in Computing Linguistics @ Sydeny Univeristy", "Coding,Running buisinesses,Reading storiess,spelling", "Python,everythgin","NCSS")
#print(user.fname)
#user.new_user()

#print(get_seeker())
create_seeker(["James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", "Univeristy of Sydney - Bachelor of Science,PhD in Computing Linguistics @ Sydeny Univeristy", "Coding,Running buisinesses,Reading storiess,spelling", "Python,everythgin", "jamie", "123", "my name is james"])
#create_seeker(["James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", "Univeristy of Sydney - Bachelor of Science,PhD in Computing Linguistics @ Sydeny Univeristy", "Coding,Running buisinesses,Reading storiess,spelling", "Python,everythgin"])

#var = get_seeker(1)

#print(get_experience(16).companyname)

create_position(["Junior", "Google", "3 months", "Internship", "Sydney, Australia", "google.com/internposition", "for a person at Uni"])

print(get_position(1).positionname)

#exp = Experience("GOOGLE", "Intern", "5/5", var.id)
#exp.save()

print(get_seekers()[0])

##
