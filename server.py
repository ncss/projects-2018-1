# The Server

from tornado.ncss import Server, ncssbook_log

def index_handler (request):
    request.write("Placeholder")

def profile_handler (request, user_id):
    if user_id == '1':
        with open('profile.html') as p:
            profile_html = p.read()
            request.write(profile_html)
    else:
        request.write("User Not found")

server = Server()
server.register(r'/', index_handler)
server.register(r'/profile/(\d+)/', profile_handler)
server.run()
