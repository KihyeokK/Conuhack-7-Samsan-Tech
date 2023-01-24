# Concuhack-7-Samsan-Tech

## Description

This project was built at Conuhacks VII. Our web application asks users to upload an image of their diary or type their diary directly into our web app, sends it to the backend, converts the diary image to text with the help of Google Cloud Vision API, analyzes emotions from the diary entry using OpenAI's API, uses Spotify API to get recommended songs based on the analyzed emotions, then sends those information back to the frontend to display.

`Diary image` -> `Text` -> `Extract emotions` -> `Get songs based on the emotion keywords` -> `Display`

Technologies used: JavaScript, Python, React, Django, Django REST framework, Google Cloud Vision API, Spotify API, ChatGPT API, Axios, Git, CSS

Check out our project on Devpost:

* https://devpost.com/software/dr-m

Team Members: Jaewon Moon, Enna Lee, Benjamin Tan, Kihyeok Kim

## Program Screenshot ##

<img width="1363" alt="Screen Shot 2023-01-23 at 3 49 01 PM" src="https://user-images.githubusercontent.com/96888460/214181563-2c42687d-3f5d-4fb3-981e-aa65c31e2986.png">

## Video Demo ##

* https://youtu.be/Krxvm5JhXx4

## Roles ##

* Kihyeok Kim: Worked on frontend, built React components and helped connecting to Django backend.
* Jaewon Moon: Worked on backend using Django Rest Framework and used the AI part with the data sent from frontend.
* Benjamin Tan: Worked on AI part using Python libraries for NLP and extracting emotion from human face.
              Helped the other developers use Github to work as a team more efficiently.
* Enna Lee: Designed the UI, researched on "~", presented our project.

Enna Lee: Designer

## Run Frontend ##

1. cd into Frontend directory
2. Enter `npm install` in terminal
3. Enter `npm start` in terminal

## Run Backend ##

1. `cd` into the directory where `manage.py` is in
2. Enter `python manage.py makemigrations` in terminal
3. Enter `python manage.py migrate --run-syncdb` in terminal
4. Enter `python manage.py runserver`
5. Copy the local host url from the terminal
5. Open your brower and paste the url
6. ctr-C in terminal to stop hosting the local server
7. `python manage.py createsuperuser`
8. `python manage.py runserver`
9. press login button in the browser


## Design ##

Current Design
* https://www.figma.com/file/r3YiHvXOB9VhKbetV99dyf/ConUHack7?node-id=0%3A1&t=tMrJKwyhlQyIn26t-1

Developed Design
* https://www.figma.com/file/Oq4qpUf2UqNvT72cNBW7Zk/ConUHack7-Future?node-id=0%3A1&t=HFOyVUxgRhvEk3y3-1
