# The Server
from templating import render
from tornado.ncss import Server, ncssbook_log # ncssbook_log --> Optional | The logs will be more legible and easyer to follow / understand
from database.seeker import Seeker
from database.seeker import create_seeker
from database.seeker import get_seeker

#user = Seeker("James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", ["Univeristy of Sydney - Bachelor of Science", "PhD in Computing Linguistics @ Sydeny Univeristy"], ["Coding","Running buisinesses","Reading storiess", "spelling"], ["Python", "everythgin"], ["NCSS"])


def index_handler (request):
    with open('index.html') as i:
        index_html = i.read()
        request.write(index_html) # TEMPORARY STAND IN HTML AND CSS FILE

def profile_handler (request, user_id):
    '''
    if user_id == '1':
        with open('profile.html') as p:
            profile_html = p.read()
            profile_html = render(profile_html, {"user": user})
            request.write(profile_html)
    '''
    with open('profile.html') as p:
        try:
            profile_html = p.read()
            customer = get_seeker(user_id)
            profile_html = render(profile_html, {"user":customer})
            request.write(profile_html)
        except:
            with open("usernotfound.html") as u:
                usernotfound_html = u.read()
                request.write(usernotfound_html)


def about_handler(request):
    request.write("Page Under Construction")

def searchresult_handler(request):
    request.write("Page Under Construction")

def position_handler(request, page_id):
    request.write("Page Under Construction")

def map_handler(request):
    request.write("Page Under Construction")

# Handler to display the form
def profile_creator_handler(request):
    with open('profile_creator.html') as i:
        profile_creator_html = i.read()
        request.write(profile_creator_html) # TEMPORARY STAND IN HTML AND CSS FILE

# Handler for creating a new profile (for submiting the form, handle the returned post)
def finished_profile_handler(request):
    #add username later
    profile_fields = ['fname', 'lname', 'birthdate', 'phone', 'email', 'city', 'education', 'hobbies', 'skills']
    field = []

    for f in profile_fields:
        field.append(request.get_field(f))

    create_seeker(field)
    request.redirect('/')

server = Server() # Create a server object
server.register(r'/', index_handler)
server.register(r'/about/', about_handler)
server.register(r'/searchresult/', searchresult_handler)
server.register(r'/positioninformation/(\d+)', position_handler) # Dynamic page | takes in a user id which is used
server.register(r'/profile/(\d+)/', profile_handler) # Dynamic page | takes in a user id which is used
server.register(r'/map/', map_handler)
server.register(r'/profilecreation/', profile_creator_handler, post = finished_profile_handler)
server.run() # Runs Server
