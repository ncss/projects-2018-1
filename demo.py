from templating import render

print(render("<h1>{{hello}}</h1>", {"hello": "WOw!"}))


'''
    First Parameter is The HTML file that we need to render.
    E.g: profile_html = render(profile_html, {"test": "Hello, World!"})

    Second Parameter must be a dictionary, the key is a variable name and the value is whath the variable is initialised to .
'''
