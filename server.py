# The Server

from tornado.ncss import Server, ncssbook_log

def get_recommendations(user_id):
    recommendations = {
1: ["Google", "Wisetech", "Freelancer"], 2: ["Macquarie", "Commonwealth Bank", "Optiver"]}

def index_handler (request):
    request.write("Placeholder")

def profile_handler (request, user_id):
    with open('profile.html') as p:
        profile_html = p.read()
        request.write(profile_html)

server = Server()
server.register(r'/', index_handler)
server.register(r'/profile/(\d+)/', profile_handler)
server.run()
