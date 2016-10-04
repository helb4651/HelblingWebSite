from django.shortcuts import render

def homePage(request):
    projects = [
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'REST API'
        },
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'Web IDE'
        },
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'HP MPS'
        },
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'Proj 4'
        },
        {
            "image_name": 'RESTfulAPI.png',
            "name"      : 'Proj 5'
        },
    ]
    context = {
                'test_context'  : 'test!',
                'projects'      : projects,
                'name'          : 'RESTfulAPI.png'
               }
    return render(request, 'home.html', context)
