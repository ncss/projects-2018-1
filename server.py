# The Server
from templating import render
from tornado.ncss import Server, ncssbook_log # ncssbook_log --> Optional | The logs will be more legible and easyer to follow / understand
from database.seeker import Seeker
from database.seeker import create_seeker
from database.seeker import get_seeker
from database.position import Position
from database.position import get_position

#user = Seeker("James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", ["Univeristy of Sydney - Bachelor of Science", "PhD in Computing Linguistics @ Sydeny Univeristy"], ["Coding","Running buisinesses","Reading storiess", "spelling"], ["Python", "everythgin"], ["NCSS"])

def index_handler (request):
    return render(request, 'index.html')

def profile_handler (request, user_id):
    #try:
    customer = get_seeker(user_id)
    render(request, "profile.html", {"user": customer})
    #except:
        #render(request, "usernotfound.html")
def about_handler(request):
    request.write("Page Under Construction")

def searchresult_handler(request):
    request.write("Page Under Construction")

def position_handler(request, page_id):
    position_information = get_position(user_id)
    render(request, "positioninformation.html", {'position': position_information})

def map_handler(request):
    request.write("Page Under Construction")

# Handler to display the form
def profile_creator_handler(request):
    with open('createprofile.html') as i:
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

def pagenotfound_handler(request):
    with open('pagenotfound.html') as n:
        pagenotfound_html = n.read()
        request.write(pagenotfound_html) # TEMPORARY STAND IN HTML AND CSS FILE

server = Server() # Create a server object
server.register(r'/', index_handler)
server.register(r'/about/', about_handler)
server.register(r'/searchresult/', searchresult_handler)
server.register(r'/positioninformation/(\d+)/', position_handler) # Dynamic page | takes in a user id which is used
server.register(r'/profile/(\d+)/', profile_handler) # Dynamic page | takes in a user id which is used
server.register(r'/map/', map_handler)
server.register(r'/profilecreation/', profile_creator_handler, post = finished_profile_handler)
server.register(r'/.*', pagenotfound_handler)
server.run() # Runs Server
