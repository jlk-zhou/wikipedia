from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 
    })


def entry(request, name):
    content = util.get_entry(name)

    entries = util.list_entries()
    for i in range(len(entries)): 
        entries[i] = entries[i].lower()
    
    return render(request, "encyclopedia/entry.html", {
        "entry": name, 
        "content": content, 
        "error": "404", 
    })

def query(request): 
    # If user submitted the form
    if request.method == "POST": 

        # Get user response
        query = dict(request.POST)["q"][0]

        matches = []

        for entry in util.list_entries(): 
            # Display view right away if user typed exact entry name
            if query.lower() == entry.lower(): 
                return redirect(f"./{entry}")
            
            # Append to search results if there are any matches
            elif query.lower() in entry.lower(): 
                matches.append(entry)
        
        # If you get to this point, you didn't typed exact entry name
        return render(request, "encyclopedia/query.html", {
            "matches": matches
        })

def new_page(request): 
    return render(request, "encyclopedia/new_page.html")

def save_entry(request): 
    return HttpResponse("success")