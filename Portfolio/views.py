from django.shortcuts import render


languages = [
    {
        "name": 'Python',
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": False,
    },
    {
        "name": 'C / C++',
        "dayToDayComfort": True,
        "decagon": False,
        "senior_proj": False,
    },
    {
        "name": 'Javascript',
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": 'Java',
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": 'MySQL',
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": False,
    },
]

dev_tools = [
    {
        "name": 'JetBrains IDEs',
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": 'git version control',
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": 'Django Framework',
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": False,
    },
    {
        "name": "Maven",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "Django REST Framework",
        "dayToDayComfort": False,
        "decagon": True,
        "senior_proj": False,
    },
    {
        "name": "Bootstrap Framework",
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": "HTML/CSS",
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": "Spark Framework",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "Docker",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "AJAX",
        "dayToDayComfort": True,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "Unix Based OS",
        "dayToDayComfort": True,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "Emacs",
        "dayToDayComfort": True,
        "decagon": False,
        "senior_proj": True,
    },
    {
        "name": "UML",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": False,
    },
    {
        "name": "Web Sockets",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": False,
    },
    {
        "name": "VirtualBox",
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": "Agile",
        "dayToDayComfort": False,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": "Scrum",
        "dayToDayComfort": False,
        "decagon": True,
        "senior_proj": False,
    },
    {
        "name": "JSON",
        "dayToDayComfort": True,
        "decagon": True,
        "senior_proj": True,
    },
    {
        "name": "AWS",
        "dayToDayComfort": False,
        "decagon": False,
        "senior_proj": True,
    }
]


def portfolioPage(request):
    print "PORTFOLIO!!!!!"
    projects = [
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'REST API',
            "path_name" : 'RESTfulAPI',
        },
        {
            "image_name": 'SeniorProject.png',
            "name"      : 'HP MPS',
            "path_name" : 'SeniorProject',
        },
        {
            "image_name": 'WebIDE.png',
            "name"      : 'Web IDE',
            "path_name" : 'WebIDE.png',
        },
    ]
    context = {
                'test_context'  : 'test!',
                'projects'      : projects,
                'name'          : 'RESTfulAPI.png'
               }
    return render(request, 'portfolio.html', context)


def RESTfulAPIPage(request):
    print "PORTFOLIO RESTAPI!!!!!"
    context = {
                'dev_tools': dev_tools,
                'languages': languages
               }
    return render(request, 'projects/RESTfulAPI.html', context)


def SeniorProjectPage(request):
    print "PORTFOLIO Senior Project!!!!!"
    context = {
                'dev_tools': dev_tools,
                'languages': languages
               }
    return render(request, 'projects/SeniorProject.html', context)