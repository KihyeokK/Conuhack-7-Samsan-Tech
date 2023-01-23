# Concuhack-7-Samsan-Tech

This project was built at Conuhacks VII. Our web application asks users to upload an image of their diary or type their diary directly into our web app, sends it to the backend, converts the diary image to text with the help of Google Cloud Vision API, analyzes emotions from the diary entry using OpenAI's API, uses Spotify API to get recommended songs based on the analyzed emotions, then sends those information back to the frontend to display.

Diary image -> Text -> Extract emotions -> Get songs based on the emotion keywords -> Display

Technologies used: JavaScript, Python, React, Django, Django REST framework, Google Cloud Vision API, Spotify API, ChatGPT API, Axios, Git, CSS

Check out our project on Devpost and Youtube:
https://devpost.com/software/dr-m

https://youtu.be/Krxvm5JhXx4

Team Members: Jaewon Moon, Enna Lee, Benjamin Tan, Kihyeok Kim

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

## Run Frontend ##

1. cd into Frontend directory
2. Enter `npm install` in terminal
3. Enter `npm start` in terminal

