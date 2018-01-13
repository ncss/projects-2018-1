from templating.Syntax import render_profiles

# with open('templating/sample.html') as f:
#     f = f.read()
#     print(render_profiles(f, {}))
with open('index.html') as f:
    f = f.read()
    print(render_profiles(f, {}))
