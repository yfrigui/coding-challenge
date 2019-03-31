# Ambassador Coding Challenge

Problem:
Tim needs a simple, automated referral system to grow support for the World Wide Web.

Solution:
Tim's solution is a web app containing two pages: one to create, edit, delete, and track referral links and another to serve as a landing page for the links that promotes the World Wide Web. 
To use the referral software, navigate to 'codingchallenge/referralsite' and run the command 'python manage.py runserver'. Then visit http://127.0.0.1:8000 with your browser. 
This solution focuses on back-end.

Technical Choices:
I decided to implement my solution using Django Rest Framework/Python, because they are used at Ambassador. Due to my lack of experience with Django, I based the structure of my project on this [tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/).

Possible Improvements:
If I were to spend additional time on the project, I would:
-	Definitely add test cases. I did test the project in my browser, but I think writing a set of formal test cases would be more robust.
-	Add error messages. Currently, the site will not accept invalid inputs (such as empty strings or link titles that already exist), but an error message would be more helpful to the user.
-	Add a 'back' button on each landing page and edit page.
-	Make the UI look better.