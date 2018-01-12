# The Server
from templating import render
from tornado.ncss import Server, ncssbook_log # ncssbook_log --> Optional | The logs will be more legible and easyer to follow / understand


def index_handler (request):
    with open('index.html') as i:
        index_html = i.read()
        request.write(index_html) # TEMPORARY STAND IN HTML AND CSS FILE

def profile_handler (request, user_id):
    if user_id == '1':
        with open('profile.html') as p:
            profile_html = p.read()
            profile_html = render(profile_html, {"test": "Hello, World!"})
            request.write(profile_html)
    else:
        request.write("User Not found")

def about_handler(request):
    request.write("Page Under Construction")

def searchresult_handler(request):
    request.write("Page Under Construction")

def position_handler(request, page_id):
    request.write("Page Under Construction")

def map_handler(request):
    request.write("Page Under Construction")

server = Server() # Create a server object
server.register(r'/', index_handler)
server.register(r'/about/', about_handler)
server.register(r'/searchresult/', searchresult_handler)
server.register(r'/positioninformation/(\d+)', position_handler) # Dynamic page | takes in a user id which is used
server.register(r'/profile/(\d+)/', profile_handler) # Dynamic page | takes in a user id which is used
server.register(r'/map/', map_handler)
server.run() # Runs Server
