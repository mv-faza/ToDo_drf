# ToDo_drf
This is simple ToDO app, made with help of DRF for constucting API and for DB I used PostgreSql.

1) In order to see the results run venv:
    `venv\scripts\activate`
2) Than run server
    `pyhton manage.py runserver`
3) Now, you will get this error:

    ![image](https://user-images.githubusercontent.com/80515538/173546788-59f11e71-11ae-47ec-b6f0-df0eb69c33bf.png)

    - So go now to this url  `http://127.0.0.1:8000/admin/`  where you will get admin site

    ![image](https://user-images.githubusercontent.com/80515538/173560280-19fa2ae5-1acc-4481-9149-a257b9430b43.png)

    - For Username: `user`
    - For pass: `1`
4) Now, go to the task

    ![image](https://user-images.githubusercontent.com/80515538/173548045-9184a84b-b93c-40e5-b711-6b262db06e75.png)

    - On the right corner you will see `add Task+` button

    ![image](https://user-images.githubusercontent.com/80515538/173548331-e9638ba8-1b91-41fe-ac78-c805f46dd30a.png)

    - Where you will see this interface

    ![image](https://user-images.githubusercontent.com/80515538/173548595-f70261d1-46f9-4488-bc3b-13607e4c9cb8.png)

    - So fill all data that you need and `SAVE`
    - Ex: 

    ![image](https://user-images.githubusercontent.com/80515538/173549424-63aecb4e-a290-4419-8ef2-70c96b8e24fd.png)

    - Well, that's it. Now we created new task
5) In order to see how DRF works go to this link  `http://127.0.0.1:8000/api/` 
    - You will get following scrin

    ![image](https://user-images.githubusercontent.com/80515538/173549956-7a9e879b-b69a-40fe-b697-826584cfe6c6.png)

    - Where you will find all path's for CRUD metod.
    - Just for example: got to  `http://127.0.0.1:8000/api/tasks/` 

    ![image](https://user-images.githubusercontent.com/80515538/173550906-5472f083-1bdd-41c0-9d7b-7e9ad18ce0c3.png)

    - And you will get all data entered by you.
