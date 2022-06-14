# ToDo_drf
This is simple ToDO app, made with help of DRF for constucting API and for DB I used PostgreSql.

1)In order to see the results run venv:
venv\scripts\activate
2)Than run server
pyhton manage.py runserver
3)Now, you will get this error:
        ![image](https://user-images.githubusercontent.com/80515538/173546788-59f11e71-11ae-47ec-b6f0-df0eb69c33bf.png)
4)So go now to this url " http://127.0.0.1:8000/admin/ " where you will get admin site
        ![image](https://user-images.githubusercontent.com/80515538/173552651-1f455ec6-1982-49ba-a90f-d6cd970d19c2.png)
5)For Username: user
6)For pass: 1
7)Now, go to the task
        ![image](https://user-images.githubusercontent.com/80515538/173548045-9184a84b-b93c-40e5-b711-6b262db06e75.png)
8)On the right corner you will see " add Task+ " buttn
        ![image](https://user-images.githubusercontent.com/80515538/173548331-e9638ba8-1b91-41fe-ac78-c805f46dd30a.png)
9)Where you will see this interface
        ![image](https://user-images.githubusercontent.com/80515538/173548595-f70261d1-46f9-4488-bc3b-13607e4c9cb8.png)
10)So fill all data that you need and SAVE
11)Ex: 
        ![image](https://user-images.githubusercontent.com/80515538/173549424-63aecb4e-a290-4419-8ef2-70c96b8e24fd.png)
12)Well, that's it. Now we created new task
13)In order to see how DRF works go to this link " http://127.0.0.1:8000/api/ "
14)You will get following scrin
        ![image](https://user-images.githubusercontent.com/80515538/173549956-7a9e879b-b69a-40fe-b697-826584cfe6c6.png)
15)Where you will find all path's for CRUD metod.
16)Just for example: got to " http://127.0.0.1:8000/api/tasks/ "
        ![image](https://user-images.githubusercontent.com/80515538/173550906-5472f083-1bdd-41c0-9d7b-7e9ad18ce0c3.png)
17)And you will get all data entered by you.
