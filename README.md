# Project 5
### Unicorn Attractor.

- <a target="_blank" href="https://github.com/twdstudent/Project-5-Unicorn">Link to GitHub Repository.</a>
- <a target="_blank" href="https://project-5-unicornapp-td.herokuapp.com/">Link to live site on Heroku.</a>
- <a target="_blank" href="https://dashboard.heroku.com/apps/project-5-unicornapp-td">Heroku Repo</a>

[![Build Status](https://travis-ci.org/twdstudent/Project-5-Unicorn.svg?branch=master)](https://travis-ci.org/twdstudent/Project-5-Unicorn)

#### The Brief
The brief was to build a unicorn attractor app, an issue tracker similar to that of GitHub.
The service is primarly a free one, user can upvote bugs to help increase focus and thus you r attention given to fixing this bug.
Features will only be developed if enough money is offered.

### UX
This is a responsive application, with the use of BootStraps Grid system and colapsable navigation menu, 
the lay out and navigation is responisve to deivce usage.
When a user posts a feature and/or bug, only said user can can edit/update the status of the feature/bugs via their profile page.
All bugs and features that are posted by all user display on their respective pages and all can be expanded to read all detail,
This was to help save on screen retail and consitantcy of the application appearance. Bugs and features can't be edited/updated 
on these pages as I didnt want all users to be able to change other users posts.

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
- <a target="_blank" href="https://github.com/twdstudent/Project-5-Unicorn/commits/master">GitHub Commits</a>

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