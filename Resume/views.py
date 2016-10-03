import os
from django.conf import settings
from django.http import Http404

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str

def resumePage(request):

    languages = [
        {
            "name": 'Python',
            "dayToDayComfort": True
        },
        {
            "name": 'C / C++',
            "dayToDayComfort": True
        },
        {
            "name": 'Javascript',
            "dayToDayComfort": True
        },
        {
            "name": 'Java',
            "dayToDayComfort": False
        },
        {
            "name": 'MySQL',
            "dayToDayComfort": False
        },
    ]

    dev_tools = [
        {
            "name": 'JetBrains IDEs',
            "dayToDayComfort": True
        },
        {
            "name": 'git version control',
            "dayToDayComfort": True
        },
        {
            "name": 'Django Framework',
            "dayToDayComfort": True
        },
        {
            "name": "Maven",
            "dayToDayComfort": False
        },
        {
            "name": "Django REST Framework",
            "dayToDayComfort": False
        },
        {
            "name": "Bootstrap Framework",
            "dayToDayComfort": True
        },
        {
            "name": "HTML/CSS",
            "dayToDayComfort": True
        },
        {
            "name": "Spark Framework",
            "dayToDayComfort": False
        },
        {
            "name": "Docker",
            "dayToDayComfort": False
        },
        {
            "name": "AJAX",
            "dayToDayComfort": True
        },
        {
            "name": "Unix Based OS",
            "dayToDayComfort": True
        },
        {
            "name": "Emacs",
            "dayToDayComfort": True
        },
        {
            "name": "UML",
            "dayToDayComfort": False
        },
        {
            "name": "Web Sockets",
            "dayToDayComfort": False
        },
        {
            "name": "VirtualBox",
            "dayToDayComfort": True
        },
        {
            "name": "Agile",
            "dayToDayComfort": False
        },
        {
            "name": "Scrum",
            "dayToDayComfort": False
        },
        {
            "name": "JSON",
            "dayToDayComfort": True
        },
        {
            "name": "AWS",
            "dayToDayComfort": False
        }
    ]

    decagon_experience = [
        {
            "name":"Collaborated with customers and product owner to design Decagon's new Data Logger REST API"
        },
        {
            "name":"Implemented Data Logger REST API"
        },
        {
            "name":"Designed and Implemented API web documentation, endpoint builder, and response preview"
        },
        {
            "name":"Performed large data set conversion"
        }
    ]
    context = {
                'languages': languages,
                'dev_tools': dev_tools,
                'decagon_experience':decagon_experience,
               }

    return render(request, 'resume.html', context)


def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, "static/ResumeCodyHelbling.pdf")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    else:
        raise Http404