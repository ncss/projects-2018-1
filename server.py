# The Server
from templating import render
from tornado.ncss import Server, ncssbook_log # ncssbook_log --> Optional | The logs will be more legible and easyer to follow / understand
from database.seeker import *
from database.position import Position, get_position, return_all_positions

#user = Seeker("James","Curran", "1/1/2012", "000", "james@ncss.com", "Sydney", ["Univeristy of Sydney - Bachelor of Science", "PhD in Computing Linguistics @ Sydeny Univeristy"], ["Coding","Running buisinesses","Reading storiess", "spelling"], ["Python", "everythgin"], ["NCSS"])

def index_handler (request):
    return render(request, 'index.html')

def profile_handler (request, user_id):
    '''
    if user_id == '1':
        with open('profile.html') as p:
            profile_html = p.read()
            profile_html = render(profile_html, {"user": user})
            request.write(profile_html)
    '''
    customer = get_seeker('./database/seekers_personal.db', user_id)
    if customer == None:
        render(request, "pagenotfound.html")
    else:
        render(request, "profile.html", {"user": customer})



def profilelistpage_handler(request):
    seekers = get_seekers('./database/seekers_personal.db')
    render(request, 'profilelistpage.html', {"seekers": seekers})

def searchresult_handler(request, query, querytype):
    positions = return_all_positions('./database/seekers_personal.db')
    results = []
    for position in positions:
        if (query.lower() in position.positionname.lower() or query.lower() in position.companyname.lower() or query.lower() in position.positionlength.lower() or query.lower() in position.address.lower()) and querytype.lower() in position.positiontype.lower():
            results.append(position)
    render(request, "positionlist.html", {"position": results})

def about_handler(request):
    request.write("Page Under Construction")

def positionlist_handler(request):
    positionlist = return_all_positions('./database/seekers_personal.db')
    render(request, "positionlist.html", {"position": positionlist})

def position_handler(request, page_id):
    position_information = get_position(page_id)
    review_information = get_review_by_position(page_id)
    render(request, "positioninformation.html", {'position': position_information, 'review': review_information})

def map_handler(request):
    request.write("Page Under Construction")

# Handler to display the form
def profile_creator_handler(request):
    render(request, 'createprofile.html')

# Handler for creating a new profile (for submiting the form, handle the returned post)
def finished_profile_handler(request):
    #add username later
    profile_fields = ['fname', 'lname', 'birthdate', 'phone', 'email', 'city', 'education', 'hobbies', 'skills', 'username', 'password', 'bio']
    field = []

    password = request.get_field('password')
    confpass = request.get_field('passwordconf')

    if password != confpass:
        request.redirect('/profilecreation/')

    for f in profile_fields:
        field.append(request.get_field(f))

    create_seeker(field)
    request.redirect('/')

def pagenotfound_handler(request):
    render(request, 'pagenotfound.html')


server = Server() # Create a server object
server.register(r'/', index_handler)
server.register(r'/about/', about_handler)
server.register(r'/profile/',profilelistpage_handler)
server.register(r'/searchresult/(.*)/(.+)/', searchresult_handler)
server.register(r'/position/', positionlist_handler)
server.register(r'/position/(\d+)/', position_handler) # Dynamic page | takes in a user id which is used
server.register(r'/profile/(\d+)/', profile_handler) # Dynamic page | takes in a user id which is used
server.register(r'/map/', map_handler)
server.register(r'/profilecreation/', profile_creator_handler, post = finished_profile_handler)
server.register(r'/.*', pagenotfound_handler)
server.run() # Runs Server
