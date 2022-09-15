# About
This is sample webapi written in python (django).

# pythonanywhere: https://www.pythonanywhere.com/
1. deploy use pa_autoconfigure_django
    ```commandline
    pip3.9 install --user pythonanywhere
    pa_autoconfigure_django.py --python=3.9 https://github.com/TakanariShimbo/sample_webapi_django.git
    ```

# How to create this
0. install python, something virtualenv

1. make and into project_directoy: sample_webapi_django
    ```commandline
    mkdir sample_webapi_django
    cd sample_webapi_django
    ```

2. activate virtualenv
    for exsample conda
    ```commandline
    conda create --name python3.9_sample_webapi_django python=3.9 -y
    conda activate python3.9_sample_webapi_django
    ```
    
3. install librarys
    ```commandline
    pip install django
    ```

4. start django project
    ```commandline
    django-admin startproject my_site .
    ```
   
    manage.py, my_site is created at current directory.

5. edit settings.py at my_site
    edit language, timezone
    ```python
    LANGUAGE_CODE = 'ja'
    TIME_ZONE = 'Asia/Tokyo'
    ```

6. start django app
    ```commandline
    python manage.py startapp my_app
    ```
   
    my_app is created at current directory.
   
7. edit urls.py
    edit urls.py at my_site
    ```python
    from django.contrib import admin
    from django.urls import path, include # add
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('my_app.urls')), # add
    ]
    ```
    
    create urls.py at my_app
    ```python
    from django.urls import path
    from . import views
    
    app_name = 'my_app'
    
    urlpatterns = [
        path('', views.index, name='index'),
        path('api/', views.api, name='api'),
    ]
    ```

8. edit views.py at my_app
    ```python
    from django.shortcuts import render
    from django.http import HttpResponse
    import json
    from django.http.response import JsonResponse
    from django.views.decorators.csrf import csrf_exempt
    
    
    def index(request):
        return HttpResponse("Hello, world!")
    
    
    @csrf_exempt
    def api(request):
        # if requested by get
        if request.method == 'GET':
            return HttpResponse("Error, use POST in stead of GET.")
    
        # get data from request
        data_get = json.loads(request.body)
        value1 = data_get["value1"]
        value2 = data_get["value2"]
    
        # return result as json
        data_send = {
            "value1": value1,
            "value2": value2
        }
        return JsonResponse(data_send)
    ```

9. edit setting.py at my_site
    allowed hosts
    ```python
    # user_id: please input your user id
    ALLOWED_HOSTS = ['user_id.pythonanywhere.com']
    ```