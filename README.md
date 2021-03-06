[![Build Status](https://travis-ci.org/brookk16/Nordlander.svg?branch=master)](https://travis-ci.org/brookk16/Nordlander)

# Nordlander 

See the deployed site [here](https://nordlander.herokuapp.com)

This site is designed to showcase the "Nordlander" game, a free to play solo action rpg. Users can use the site to: purchase dlc, see the game's progress with charts and get support for the game.

This is the 5th milietone project required as part of the Code Institute’s full stack web developer course, showcasing skills in: e-commerce, django, full stack development, e.t.c

> Note: The Nordlander game and any bugs or features do not exist, in addition the stripe payment features of this app are set to test and therefore only work with the test card (please see [stripe](https://stripe.com) for more info)

**Index:**
1. [UX](#UX)
2. [Components](#Components )
3. [Technologies](#Technologies)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)


## UX

This website is designed for new and current users of the Nordlander game to: 

- download the game 
- purchase features
- get support for their game. 

The site is designed to not only facilitate these requirements, but also to help influence the creation of future features. 
To ensure that users have access to any feature they may want,  we have a dedicated performance page which alongside your social media posts, influences the design of future features. 

To maintain transparency, users have access to this data in the performance page. Users inlfuence future features by purchasing features they want and/or liking the features. 

We try to develop and release new features as soon as we can, therefore to help solve any bugs we have a support page. Users can search for bugs, see and add comments and also add their own bugs too. These results can also be seen on the performance page. 

The decision to implement these primary features on the website were guided by user requirements, a sample of which can be seen below: 

- **User A**: I want to be able to be able to find and purchase features that interest me.

- **User B**: I want adequate support if anything goes wrong with the game or my account.

- **User C**: I want to be able to see how stable the game is before I buy, and how many features there are.

Click below to see the wireframes for this project 

<details> 
<summary>Wireframes</summary> 
<br> 

![index/welcome page1](https://github.com/brookk16/Nordlander/blob/master/wireframes/home-1.png)

![index/welcome page2](https://github.com/brookk16/Nordlander/blob/master/wireframes/home-2.png)

![index/welcome page3](https://github.com/brookk16/Nordlander/blob/master/wireframes/home-3.png)

![index/welcome page4](https://github.com/brookk16/Nordlander/blob/master/wireframes/home-4.png)

![bugs](https://github.com/brookk16/Nordlander/blob/master/wireframes/bugs.png)

![bugsInfo](https://github.com/brookk16/Nordlander/blob/master/wireframes/bugs-info.png)

![features](https://github.com/brookk16/Nordlander/blob/master/wireframes/features.png)

![featuresInfo](https://github.com/brookk16/Nordlander/blob/master/wireframes/features-info.png)

![cart](https://github.com/brookk16/Nordlander/blob/master/wireframes/cart.png)

![checkout](https://github.com/brookk16/Nordlander/blob/master/wireframes/checkout.png)

![performance page1](https://github.com/brookk16/Nordlander/blob/master/wireframes/performance-1.png)

![performance page2](https://github.com/brookk16/Nordlander/blob/master/wireframes/performance-2.png)

![performance page3](https://github.com/brookk16/Nordlander/blob/master/wireframes/performance-3.png)

![performance page4](https://github.com/brookk16/Nordlander/blob/master/wireframes/performance-4.png)

![users features](https://github.com/brookk16/Nordlander/blob/master/wireframes/users-features.png)

![login etc](https://github.com/brookk16/Nordlander/blob/master/wireframes/login-etc.png)

</details>

## Components 

### Existing Components 

New arrivals to the Nordlander site can only have access to the  features page without an account, accessing all the sites components requires making a free account.

<details> 
<summary>**Instructions on how to make a free account**</summary> 
<br> 

> Note: Before logging in, the only options available in the top nav are: "Register", "Log in", "Features" and "Cart". After logging in, users have access to: "Profile", "Support", "Features" and "Cart".

1.	Click on “Register” in the top navbar
2.	Fill out all the fields in the form
3.	Click on the 'Create account' button
4.	You will now be taken back to the home page, logged in to your free account

</details>

Once logged in, users are able to access 3 main components of the site: Account, Features and Support. 

Each are described below:

**1.	Account**:

<details>
<summary>Log in</summary> 
<br> 

1. Click on the "Log in" button in the top nav
2. Enter your username and password
3. Click the "Log in" button
4. The user will then be redirected back to the homepage, with the message "You have successfully logged in, welcome 'user'"

</details>

<details> 
<summary>Log out</summary> 
<br> 

1. Click on the "Profile" dropdown menu in the top nav
2. Click on the "Log out" option
3. The user will then be redirected back to the homepage, with the message "You have successfully logged out, goodbye 'user'"

</details>

<details> 
<summary>Password retrieval</summary> 
<br> 

1. Click on the "forgot my password" link in the login page
2. This will redirect you to another page, where you must supply your user email
3. An email will then be sent to the supplied email, with details on how to reset your password, and a link to reset your password
4. Clicking on the link redirects the user to another page, where you must supply a new password (must be supplied twice for authentication)
5. If successful the user is redirected to another page where this message is displayed: "Your password has been set. You may go ahead and log in now." and click to log in.

- If the link did not work another message will be displayed instead of the password reset from, i.e: "The password reset link was invalid, possibly because it has already been used. Please request a new password reset.""

</details>

<details> 
<summary>See user’s purchased features</summary> 
<br> 

1. Click on the "Profile" dropdown menu in the top nav
2. Click on the "'users' features" option
3. This will redirect the user to another page, displaying a list of all the features that the logged in user has purchased (with links to the features full information)

- If the user hesn't yet purchased any features, this message will be displayed: "You haven't bought any features yet".

</details>


**2. Features:**

> Note: as features are paid items, users are not able to create them. To create a new feature product, use the Django admin panel. For more information click [here](https://docs.djangoproject.com/en/2.2/ref/contrib/admin/ )

All following feature component explanations begin on the "features.html" page. Which is accessed by clicking on the "Features" link in the top nav.

<details> 
<summary>Search for features</summary> 
<br> 

1. Search options are available in the search bar, just below the "Features welcome message"
2. Users may search using any combination of the three search inputs: search by name, search by feature type and search by feature's current status. 
    - Ex: A user could search for a feature where the name contains "sword", the type is "Item" and the status is "Available", then click the "search" button. The search would still function if the user removed any one or two of the inputs.

3. Users can reset the search items by clicking on the "reset" button.

</details>

<details> 
<summary>Like features</summary> 
<br> 

1. Click on a feature's "See more" button
2. Scroll down to the "thumbs up" icon
3. Click on the icon to like the feature
4. The like counter will then increment by one, showing the like

- If the user has already liked the feature, the like will not be counted and the page will refreash and a message will appear ("You have already liked this")

</details>

<details> 
<summary>Purchase features</summary> 
<br> 

1. Click on a feature's "See more" button
2. Scroll down to the "add to cart" button (this will only be accessible if the features current status is "Available")
3. Click to add the item to your cart, the 'Cart' icon in the top nav will then increment by one (or will show a "1" if it was previously empty)
4. Click on the "Cart" icon to be taken into the user's cart
5. The user's cart items will then be displayed, along with the total amount due and a checkout button (this option will only be accessible if the cart is not empty)
6. Click on the "checkout" button
7. This will redirect users to the checkout page, containing two forms: one for the users information and the other for payment information.
8. Fill in all the fields in each form (a prompt will arise if left empty)
9. Click on the "Submit Payment" button.
10. If the payment is sucessful, the user is redirected to another page, displaying a success message and a link to go back to the "features" page.

> Note: Please be aware that the stripe payment processing is only currently set up to process payments using the test card. Therefore, error messages will not be displayed for incorrect information in the "payment form". If incorrect information is input and the "Submit payment" button is clicked, nothing will appear to happen.

</details>

<details> 
<summary>See current statuses of features</summary> 
<br> 

1. Click on the "Support" dropdown in the top nav.
2. Click on the "Performance" option.
3. The user will then be redirected to the "Performance" page, where all the charts are displayed.
4. There are 4 charts for features: Top 5 features by user likes, Current feature types, Amount of bugs per features and the popularity of each types of feature. 

- You can see more information about the chart by hovering over the "?" icon by the chart title
- In addition to the numerical values displayed in the charts, hovering over each bar/point/segment will show additional information.

</details>


**3. Support:**

All following bug component explanations begin on the "bugs.html" page. Which is accessed by clicking on the "Support" dropdown in the top nav, then click on the "Bugs" option.

<details> 
<summary>Search for bugs</summary> 
<br> 

1. Search options are available in the search bar, just below the "Bugs welcome message"
2. Users may search using any combination of the three search inputs: search by name, search by bug type and search by bug's current status. 
    - Ex: A user could search for a bug where the name contains "Base game", the type is "Base game" and the status is "Fixed", then click the "search" button. The search would still function if the user removed any one or two of the inputs.

3. Users can reset the search items by clicking on the "reset" button.

</details>

<details> 
<summary>Upvote a bug</summary> 
<br> 

1. Click on a bug's "See more" button
2. Scroll down to the "bug" icon
3. Click on the icon to upvote the bug
4. The upvote counter will then increment by one, showing the upvote

- If the user has already upvoted the bug, the upvote will not be counted and the page will refreash and a message will appear ("You have already upvoted this").

</details>

<details> 
<summary>Comment on a bug</summary> 
<br> 

1. Click on a bug's "See more" button
2. Scroll down to the comments section
3. Click on the "Add comment"
4. A modal window will appear with an area to input the comment and a "Save" button
5. Add your comment and click the "Save" button
6. The modal window will disappear and the comment will be displayed at the top of the comments section (including the user's name and date posted) 

</details>

<details> 
<summary>Add a bug</summary> 
<br> 

1. Click on the "Add bug" button
2. A modal window will appear with a form for inputting the bugs information
3. Once the "Add bug" button is clicked, the modal window disappears and the users bug is displayed at the top of the bugs section.

> Note: The status of new bugs is always "To do" and is to be changed by the admin the user panel.

</details>

<details> 
<summary>See current status of bugs and user activity</summary> 
<br> 

1. Click on the "Support" dropdown in the top nav.
2. Click on the "Performance" option.
3. The user will then be redirected to the "Performance" page, where all the charts are displayed.
4. There are 3 charts for features: Top 5 bugs by user upvotes, new bugs uploaded in the past week and current bug statuses (no. of bugs To do, Doing and fixed)  


- You can see more information about the chart by hovering over the "?" icon by the chart title
- In addition to the numerical values displayed in the charts, hovering over each bar/point/segment will show additional information.

</details>

### Components Left to Implement

1. Expand on the options available for users in their profile page. In keeping with ux design, this would involve hearing from users to ask for what features they would want the most. 


2. Write more thorough automated tests for the app, to facilitate development at a later date. This was not implemented to the fullest due to the developer’s lack of knowledge in this area.

3. Add functionality to allow users to download the game. As making an app/game was not required as part of this project, no accompanying code was written to allow users to download the app/game. Therefore nothing happens when users click the download links in the home.html template.



## Technologies 

[Font awesome](https://fontawesome.com):
* Provided the icons for the project 

[Python3](https://www.python.org/download/releases/3.0/) (3.4.3):
* Used to write the logic for this app 

[JQuery](https://jquery.com)(3.2.1) and [JQuery-ui](https://jqueryui.com)(1.12.0)
* Provides DOM manipulation, and allows use of Jquery code effects (code stored in AWS S3 bucket not github)

[Bootstrap](https://getbootstrap.com/docs/3.3/)(3.3.7)
* Provides a responisve grid system, and form styling (with django-forms-bootstrap(3.1.0)

[Stripe](https://stripe.com):
* Provides the payment processing and payment authentication for e-commerce components (i.e: purchasing of features)

[Django](https://docs.djangoproject.com/en/2.2/releases/1.11/)(1.11):
* This framework provides the basis for the web app, upon which all other components are built upon.

[Sqlite3](https://docs.python.org/3/library/sqlite3.html):
* Is the relational SQL database used in the local environment.

[Heroku Postgres SQL](https://www.heroku.com/postgres):
* Is the relational SQL databse used in the Heroku deployed site.

[AWS S3](https://aws.amazon.com/s3/):
* Used as a repository to serve all the static files (css, images and javascript/jquery code). Also holds the images uploaded for each new feature product.

The code editor used to create the project was [Cloud9](https://c9.io/signup).

The project uses [Git](https://git-scm.com) for version control.

For the additional tools and libraries needed to run the app, please refer to [requirements.txt]()


## Testing

The website conforms with user focused design by adhering to the user requirements, set out in the user experience section.
A mix of automated and manual testing was conducted on the website:

1.	Initial testing involving: checking all code, validating code using online html and css validators and running Google chrome audits.

2.	Automated tests were written to test the basic rendering of each of the html templates, when a certain url is requested

3.	Manual testing was conducted on all features (described in the features section) as well as all other functionality of the site. 


4.  Final user tests to ensure all website functionality is satisfactory and provides a positive user experience.

<details> 
<summary>**Click below to see automated tests and how to run** </summary> 
<br> 

#### Automated-tests

- Each app has it's own 'tests.py' containing the tests for that particular app. As mentioned in ['Components left to implement'](#leftToImplement2), these automated tests only check whether the correct page is rendered correctly.

- To run the tests, type into the console:

~~~

python3 manage.py run test

~~~

- All the tests will then run and provide feedback in the console.
- To test that the tests can fail, there is a test designed to fail [here](https://github.com/brookk16/Nordlander/blob/master/accounts/tests.py). Uncomment out the 'FAIL test' and then re-run tests to see the test failing.

</details>

<details> 
<summary>**Click below to see details of these manual tests**</summary> 
<br> 

#### Manual tests

- Manual tests were conducted on all the components (descirbed in [components](#Components)) and on the JQuery code for the site. All manual tests for the comppnents follow the instructions given in [components](#Components), and thus these test descriptions will only provide the results of each test.

**Tests for major components:** 
1. Account
- Form for registering a new user will only submit if all fields are full, and contains the correct information (i.e: password 1 and 2 must match and be longer than 6 characters). The provided username and email must also be unique.
- When user tries to log in with correct information, they are logged into the corret account. If fields are empty or incorrect (not in the databse) the user is not logged in.
- The "forgot my password" button correctly redirects users to a page where they must supply their email. The email then sends to the correct email address (using the created email template). The link supplied in the email then works to redirect users to a new page where they can input a new password. This newly created password can then be used to log in correctly.
- When a user clicks on "username's features" they are shown a list of the features that they have bought, or an error message if they haven't yet bought any features.

2. Features:
- When users hover over the "thumbs up" icon on the feature's information page (featuresInfo.html) the icon becomes green. Clicking on the icon will then increment the like counter by 1. Users who have clicked are saved in a list, so that if they click it again, an error message appears.
- Once the user has items in their cart the "checkout" button on checkout.html becomes available and users can go to the checkout page. Leaving any form input empty will prompt a "Field required" message. Using the correct information (user and credit card) will redirect the user to a "payment complete" page and a message will be displayed at the top (with a correct payment message).

> Note: The stripe payment processing is set to test currently, therefore only the test card information will allow a purchase. In addition, the error messages will not display whilst in test mode, therefore no error messages are displayed if incorrect data is put into the form, the form just won't be submitted until correct info is used. To learn more see the [stripe documents](https://stripe.com/docs).

3. Support:
- Hovering over the 'bug' symbol changes the colour to green, and clicking on this symbol will then increment the upvote number by one. If a user who has already upvoted that bug tries to upvote again, it will not work and an error message is displayed. 
- Clicking the 'add a comment' button displays the correct modal window, and the submit button then saves the comment. The comment is then correctly displayed (with the correct username and time of posting). Adding new comments pushes the older ones down the page. 
- CLicking the "add a bug" button correctly displays the modal window, with all required inputs. Once submitted, the new bug correctly displays on the bugs page, with new bugs offsetting older bugs down the page. The correct information for the bug is also displayed (i.e: the status, date of creation, type of bug and number of upvotes).

 > Note: As the performance and search apps are separate from bugs and features, their tests are described below.

4. Other:
- Users are able to search for any bug/feature using the search bar, using any combination of the 3 search inputs. The correct results are displayed, from the correct database (i.e: if searching from bugs page, only bugs are displayed). The correct search information messages are also displayed when a search is made. 

- The performance page results were then checked manually to ensure that the data displayed reflects the actual databse values. The hover messages and numerical values were also checked, and are displaying correctly.

</details>



## Deployment

The code is deployed on [here](https://nordlander.herokuapp.com)

**To deploy the code onto Heroku:**

Deploying to Heroku consisted of X stages:

<details>
<summary>1. Set-up of the deployed database:</summary> 
<br> 
- Heroku's SQL Postgres database was set up on Heroku

- dj-database-url and psycopg2 was installed to facilitate communication bewteen our django app and the Heroku database

- The code was updated in "settings.py" as to change between the deployed and local databases (depending on whether the environmental varibales come from a local env.py file or the deployed environment)

- The database was then migrated over to the deployed database.

</details>

<details>
<summary>2. Set-up and use of S3 bucket:</summary> 
<br>
> Note: requires set up of free AWS developper account

- Created an S3 bucket (for complete instructions, click [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html))
    - set to "static website hosting"
    - Added a [bucket policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/example-bucket-policies.html) and [CORS configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html)
    - Then created a user (with a "AmazonS3FullAccess" policy attatched)
    - Downloaded the 'credentials.csv' file and input the keys into the code.

- Integrated S3 and Django (for complete instructions, click [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html))
     - updated "settings.py" by adding "storages" to INSTALLED_APPS.
     - And added variables required (descirbed in [instructions](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html))
- Also hosted our "media" files (images uploaded for use in 'features'):
    - A 'custom_storages.py' file was created (code [here](https://github.com/brookk16/Nordlander/blob/master/custom_storages.py))
    - Following variables were added to 'settings.py': STATICFILES_STORAGE = "custom_storages.StaticStorage" and STATICFILES_LOCATION = 'static'
    
</details>

<details>
<summary>3. Final set up of Heroku:</summary> 
<br>

- Linked up the Github repository to the Heroku (follow these [instructions](https://devcenter.heroku.com/articles/github-integration))

- Created a requirements.txt file:

~~~
sudo pip3 freeze --local > requirements.txt 
~~~

- Installed gunicorn (to allow us to connect to Heroku)

- Created a Procfile:

~~~
echo web: gunicorn nordlander.wsgi:application > Procfile
~~~

- Following varibales set in Heroku: AWS_SECRET_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, EMAIL_ADDRESS, EMAIL_PASSWORD, SECRET_KEY, STRIPE_PUBLISHABLE, STRIPE_SECRET and DISABLE_COLLECTSTATIC = 1 (this stops Heroku from trying to re-upload the static files)

- 'import env' in 'settings.py' was then commented out
- The code was then added, commited and pushed to Github

> Note: There will be an error until you add the site to ALLOWED_HOSTS in 'settings.py'.

</details>

**To run the code locally:**

You will need a django app set up. Copy the code from this repository and then install the requirements from the file. 

To then run the code you will need to:
1.	Uncomment “import env.py” in Nordlander > settings.py
2.	Add your own “env.py” to the top level directory. Add the following environmental variables: AWS_SECRET_ACCESS_KEY, AWS_SECRET_ACCESS_KEY, EMAIL_ADDRESS, EMAIL_PASSWORD, SECRET_KEY, STRIPE_PUBLISHABLE and STRIPE_SECRET
3.	Type “run” into the console and hit enter


## Credits
The Images used in the project were taken from the following sources: 
- [Home page background image](https://www.deviantart.com/janphilippeckert/art/Darksouls-Fanart-Wallpaper-451273547) 

-Home page carousel images: [character creation](http://expeditionsseries.com), [quests](https://www.reddit.com/r/ImaginaryLandscapes/comments/as9ahc/fantasy_landscape_by_viktor_mukhin/) and [weapons](https://society6.com/danielnyari)

- Home page features section: [new worlds](http://mentalfloss.com/article/64152/gorgeous-and-extensive-video-game-map), [new weapons](http://sf.co.ua/id63667) and [new quests](https://www.videogamesartwork.com/games/elder-scrolls-online/dungeon)

-[Backgound image for home page features section and cart background image](https://the-world-of-nyrondie.fandom.com/wiki/The_Scalelands)

-[Background image for features page](https://www.wallpaperup.com/212136/TERA_ONLINE_fantasy_adventure_game_(72).html)

-	The [collumns](https://jooinn.com/castle-column.html) used on featuresInfo.html, bugs.html and bugsInfo.html

-[Performance](https://stmed.net/fantasy/dark-fantasy-wallpapers) background image


The fonts used in this project come from the following sources (and may be found within the fonts folder of the static directory): 

- [Stempel Garmon](http://legionfonts.com/fonts/stempelgaramondltstd-bold)
- [Nordlander](https://www.fontspace.com/joel-carrouche/norse) (normal and bold)

