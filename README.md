# Project 5
### Unicorn Attractor.

- <a href="https://github.com/twdstudent/Project-5-Unicorn">Link to GitHub Repository.</a>
- <a href="https://project-5-unicornapp-td.herokuapp.com/">Link to live site on Heroku.</a>
- <a href="https://dashboard.heroku.com/apps/project-5-unicornapp-td">Heroku Repo</a>

[![Build Status](https://travis-ci.org/twdstudent/Project-5-Unicorn.svg?branch=master)](https://travis-ci.org/twdstudent/Project-5-Unicorn)

#### The Brief
The brief was to build a unicorn attractor app, an issue tracker similar to that of GitHub.
The service is primarly a free one, user can upvote bugs to help increase focus and thus you r attention given to fixing this bug.
Features will only be developed if enough money is offered.

### UX
(wire frames located in wire-frames directory)
This project is not functioning, i was simply unable to build a working application with the time I had left.
The project runs fine from cloud 9, the naviagation, forms and general layout is responsive.
The log in/log out functionality is working fine and all the reset password finctionality is also wokring fine.
However sadly the application wont open open up on Heroku.
Sadly there is not much else to write about this section due to it being incomplete and not being able to wire upuploading bugs 
an features.
Design intened to be simple and clean, simply drawing focus on what users add to the site.

### Features
back end logic for bugs and features is complete but was unable to wire it up to the templates.
Login/logout features along with reset password links working correctly when tested through C9.

### Features Left to Implement
To actually have the ability for users to add bugs and features for development, have a job status for each one.
Have a blog section where users can discuss ideas and theories.

### Technologies Used
This a django project which was installed via the command line.
Bootstrap was used for stlying of buttons, forms and responsive page layout.
font-awsome was used for icons used in the navigation ie the cart button for visual aid as to what the button does.
HTML used in templates.
STRIPE used for the hadling of card payments for when a user wishes to pay for a feature. 

### JQuery
used in the JS required for wiring up stripes backend logic.

### Testing
(some success in this area) Travis was used on the project, and is passing!
the import env in settings.py has been commented out as travis can't read the env.py file as it it's in the 
git ignore file. minor testing done in bugs app and feature app, see tests.py.

tested registration process and reset password links by actually registering with the site (running via C9)s
deliberately inputted an invalid email address and it wouldnt let me register.
Also followed the reset link process with success.

### Deployment
This project is backed up to GitHub and Heroku. (links at the top)

Heroku config variables
- DATABASE_URL (noy sharing value)
- DISABLE_COLLECTSTATIC 1
- SECRET_KEY (not sharing value)
- STRIPE_PUBLISHABLE (not sharing value)
- STRIPE_SECRET (not sharing value)

GitHub Deployment:
- intial commit, rebuilding repo with files removed
- setting up Travis intergrated testing
- app specific url files added
- tarvis issues
- fixed indentation in travis file
- trying something out
- travis issue again
- fixing requiremnets file
- added feature app
- added cart app and fixing url bug
- fixed bug in contexts.py file
- fixed urls.py file in root direcotory
- created checkout app and built models
- added checkout template, forms.py file and urls.py for checkout
- updated requirements.txt file for stripe
- fixed bug with checkout app and added icons
- updated settings.py file for travis testing
- installed gunicorn and created the Procfile
- added heroku to allowed hosts
- trying something out
- prepping for submission

enviroment variables were used (env.py file) to keep sensitive information hidden from production.
Git ignore file used so said variables didnt get pushed to GitHib.
Mentioned earlier that import env in the settings.py file has been commented out as travis can't see the 
gitingnore files thus the tests fail, so when working via C9 I remove the comment so a can continue development
and simply re-comment out the import env when backing up to GitHub.

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.


### Acknowledgements
Would like to thank Chris Zielinski for his support and guidence throught this course.