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
Media queries used for styling on mobile devices.

### Features
A user can firstly create an account with ability to reset password if they forget.
When posting a bug, a user can upload an screen shot to help better display an issue they're having. But the images can only be
viewed when "read more" is clicked, this is to aid screen layout and design consistency.
Onyl individual users can edit/update the status of there own features and bugs. This is done throught the users individual
profile page where they can only view their own posts.
On the feature/bugs page users can view all post posted by all users. but can't change all users psts
Both bugs and features have a status update feature so users can see there progress.
User can alo post features to which other users can opt to pay to speed up the process of having the feature developed.
Full check out and paying services are also built into this site.
Each post is equiped with published date feature, the user who posted it, the ability to like/upvote and see number views (when people
click read more).

### Features Left to Implement
Would like to add a live chat room where users can talk to each other and share tips/best practice etc.
and have a section with graphs where users can see rate of completeion of bug fixes and feature devlopment.

### Technologies Used
This a django project which was installed via the command line, django template logic was used along with if statements used 
for displaying features and bugs.
Bootstrap is used for stlying of buttons, forms and responsive page layout.
font-awsome was used for icons used in the navigation ie the cart button for visual aid as to what the button does.
HTML used in templates and css used for styling.
STRIPE used for the hadling of card payments for when a user wishes to pay for a feature. 

### JQuery
used in the JS required for wiring up stripes backend logic.

### Testing
Travis was used on the project, and is passing.
the import env in settings.py has to be commented out as travis can't read the env.py file as it it's in the 
git ignore file. 
testing was carried out on bugs/features forms, models and views. This is to help manage testing more cleary.
Accounts, tetsing carried out on login rquired, user form and registration forms.
Cart, test_get_cart_page, test_add_to_cart, test_adjust_cart were carried out and all passing.
Checkout, TestMakePaymentForm, TestOrderForm carried with diffrent variances to test that only valid forms an pass through.
in total, 29 test were carried out and are all passing.

Tested registration process and reset password links by actually registering with the site (running via C9)s
deliberately inputted an invalid email address and it wouldnt let me register.
Also followed the reset link process with success.

Created multiple users too and posted bugs/features on both accounts so we can see content from multiple users.

### Deployment
This project is backed up to GitHub and Heroku. (links at the top)
They're are both linked, so when i back up to GitHub it automatically builds in Heroku.

Heroku config variables
- DATABASE_URL (noy sharing value)
- DISABLE_COLLECTSTATIC 1
- SECRET_KEY (not sharing value)
- STRIPE_PUBLISHABLE (not sharing value)
- STRIPE_SECRET (not sharing value)

GitHub Commits:

- <a target="_blank" href="https://github.com/twdstudent/Project-5-Unicorn/commits/master">GitHub Commits</a>

Click link to see details of my commits as there is simply too may to type out.
I made commits after each app was built, major functionality was built, a bug had been fixed, significant styling was completed,
tests on components was carried out and passing and little things such as commenting out the env.py file in settings.py so that 
it can be built in Heroku and travis testing can pass.

enviroment variables were used (env.py file) to keep sensitive information hidden from production.
Git ignore file used so said variables didnt get pushed to GitHib.
Mentioned earlier that import env in the settings.py file has been commented out as travis can't see the 
gitingnore files thus the tests fail, so when working via C9 I remove the comment so a can continue development
and simply re-comment out the import env when backing up to GitHub.

When working with C9, the env.py file has to be uncommented so I can continue to work locally.
Also within the env.py file itself I have to comment out the data base url variable as the tests wont run with this in effect.
When commiting i un comment this variable so desired data base is used.


### Acknowledgements
Would like to thank Chris Zielinski for his support and guidence through this course.