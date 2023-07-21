# Contact Form

This Python-based web application is developed using Flask, HTML, CSS, and various other modules. The primary goal of creating this project is to help with learning more about HTML, CSS, and Flask. This ultimately resulting in the creation of a functional and user-friendly contact form web page. For the demo website, please visit the <a href='http://slkat.pythonanywhere.com/' target='blank'>Contact Form Website</a>

## Features

* The web page allows users to submit their information and message through a website contact form.
* User's Information and messages are stored in a database using SQLAlchemy. Additionally, the application sends the recipient an email containing the submitted message.
* The contact form web page is well structured utilizing HTML/CSS, ensuring an interactive and user-friendly experience. Plus a formatted table is used to present information, messages, and timestamps of submitted data.
* A secure log-in function is implemented to provide admin authentication, allowing access to private data/messages

## Setup

* Configure Email Server in the `config.py` file. Setup your email server, username, and password.
* Customize the admin authentication in the `main.py`. By default, username is set to 'admin', and password is set to 'password'.
* Create the necessary tables for the database. You can do so by executing specific commands in the terminal.

## Visual

![form](https://i.gyazo.com/365f74e7dd74a39bcd158dbdaac8aa2b.png)
![messages](https://i.gyazo.com/84c7d3f9aba27e94dc6557457058983f.png)