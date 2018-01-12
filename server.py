# The Server
from templating import render
from tornado.ncss import Server, ncssbook_log # ncssbook_log --> Optional | The logs will be more legible and easyer to follow / understand
from database.seeker import Seeker


user = Seeker(1,"James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", ["Univeristy of Sydney - Bachelor of Science", "PhD in Computing Linguistics @ Sydeny Univeristy"], ["Coding","Running buisinesses","Reading storiess", "spelling"], ["Python", "everythgin"], ["NCSS"])


def index_handler (request):
    with open('index.html') as i:
        index_html = i.read()
        request.write(index_html) # TEMPORARY STAND IN HTML AND CSS FILE

def profile_handler (request, user_id):
    if user_id == '1':
        with open('profile.html') as p:
            profile_html = p.read()
            profile_html = render(profile_html, {"test": user})
            request.write(profile_html)
    else:
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
def ESP_handler(request):
    with open('ExampleSeekerProfile.html') as i:
        ESP_html = i.read()
        request.write(ESP_html) # TEMPORARY STAND IN HTML AND CSS FILE

# Handler for creating a new profile (for submiting the form, handle the returned post)
def new_esp_handler(request):
    variable = request.get_field("username")
    print(variable)

server = Server() # Create a server object
server.register(r'/', index_handler)
server.register(r'/about/', about_handler)
server.register(r'/searchresult/', searchresult_handler)
server.register(r'/positioninformation/(\d+)', position_handler) # Dynamic page | takes in a user id which is used
server.register(r'/profile/(\d+)/', profile_handler) # Dynamic page | takes in a user id which is used
server.register(r'/map/', map_handler)
server.register(r'/ExampleSeekerProfile/', ESP_handler, post = new_esp_handler)
server.run() # Runs Server
