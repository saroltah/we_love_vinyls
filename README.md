
# Live website: [We love vinyls](https://we-love-vinyls-b-74b4f31a8a78.herokuapp.com/) 

## Goal of the website
We love vinlys is an online platform dedicated to the buying, selling, and trading of second-hand vinyl records. Users can browse a wide range of vinyl records, connect with sellers, and negotiate exchanges or purchases. The site also features a directory of markets and events focused on vinyl records, providing users with information on where to find local or traveling vinyl fairs and meet-ups. The goal of we love vinyls is to create a vibrant community where vinyl enthusiasts can easily access and share their passion for music on vinyl.

# User experience

#### Importnace of the website:

- Access to Rare records:  Users can discover hard-to-find and rare vinyl records that might not be available in traditional stores.
- Convenient Trading and Selling: Users can easily sell or trade their vinyl records, helping them to refresh their collection .
- Event Information: The site offers information about local and international vinyl markets and events, giving users opportunities to engage in person, expand their network, and enjoy the vinyl community experience.
- Diverse Collection: With a wide range of genres and eras represented, users can explore and expand their musical horizons.



## Epics and user stories

I used GitHub projects to write down all the essential features I needed in my website using user stories. I divided my user stories into epics, making it easier to see my progress. I also labeled them by the MoSCoW prioritization: must-have should have, could have, won’t have. As I started/finished a task, I moved it from the to-do list to the in-progress and then the Done list.

<br>
Github project:
<br>

![github project](/readme/assets/github-project.png)
<br>


### Epics:

- Epic:  User authentication and verification: Provide users with a secure and user-friendly authentication and verification system, including sign-up, log-in, and password management.

- Epic: User profile management: Enable users to create, edit, view, and delete their profiles to provide a personalized experience.

- Epic: Vinyl records management: Allow users to post, edit, delete, comment on, and like vinyl records to actively participate in the community.

- Epic: Markets and events management: Enable users to create, edit, delete, attend, and comment on events to actively participate in vinyl community events.

- Miscellaneous features: Provide users with various confirmations and error messages to ensure a smooth and understandable user experience.

<br>

I provided acceptance criteria also for my user stories.
As my project involved, I changed some prioritization, but this is the original version of my plans and user stories:


### User stories:

<br>

#### Must have

<br>

**Authentication: Sign up:** As a user, I can sign up to use all the website's features.

**Authentication: Login/out:** As a user, I can log in and out to protect my data and privacy.

**Profile: Edit/delete profile:** As a user, I want to be able to edit or delete my profile so I can change my mind about using the page and edit my errors.

**Records: Details of the records:** As a user, I want to read details about the record so I can decide whether I like it.

**Records: Edit/Delete records:** As a user, I want to edit my post so I can correct my mistakes, also want to delete the post in case the information is no longer relevant.

**Markets: Details of the markets:** As a user, I want to see the place, time, and duration so I can attend.

**Markets: Edit/Delete records:** As a user, I want to edit my event so I can correct my mistakes, and I also want to delete the event in case the information is no longer relevant.

**Miscellaneous: Styling website:** As a user, I want an eye-catching but easy-to-follow design so it gives a remarkable user experience.

**Miscellaneous: Menu: Easy navigation:** As a user, I want to easily access the website’s options so it is clear how to use the page.

 **Admin: Supervision:** As an admin, I want to supervise the profile and content from the admin panel, so I can remove inappropriate content.

<br>

#### Should have

<br>

**Authentication: Forgotten password:** As a user, I can reset my password if I forget it.

**Profile: Uploaded records:** As a user, I want to see all the records the users uploaded so I can buy more at once. 

**Profile: Liked records:** As a user, I want to see all the records that I have liked so I can decide on them later.

**Profile: My events:** As a user, I want to see the events I want to attend (mark attend), so I don’t forget about them.

**Records: Like records:** As a user, I want to like a record so I can express what I like and others can also see that it is a good record. 

**Records: Filtering:** As a user I want to have a search option so I can filter out the records I am looking for.

**Markets: Attend button:** As a user, I want to mark that I attend the event so the organizers know who to expect. I also want to be able to cancel my attendance.

**Markets: Filtering:** As a user, I want to be able to search by location to find events near me.

**Records: Comment section**: As a user, I want to comment under the records so I can ask questions and make a deal. I also want to edit and delete them, in case I change my mind.

**Miscellaneous: Confirmation:** As a user, I want confirmation about posted, edited, or deleted posts.

**Miscellaneous: Error messages:** As a user, I want to receive error messages if something goes wrong so I know what went wrong.

<br>

 #### Could have

 <br>

**Authentication: Sign up with social media:** As a user I want to sign up with my social media account, so it is so much quicker.

**Profile: Past events:** As a user, I want to see the events I have attended so I remember.

**Records: Number of comments and likes**: As a user, I want to see the number of likes and comments so I can see how many people liked or commented on a particular record. This information can then refer me to more information about the product. 

**Markets: Number of attendees**: As a user, I want to see the number of attendees so I can determine the size of the event. 

**Miscellaneous: Menu: About and terms**: As a user, I want to read about the website's goals and how to use it.

**Profile: Messages:** As a user, I want to send private messages about the record I want to buy.

<br>

#### Won't have

<br>
 
Initially, I didn’t put anything here, just as the project involved. In the end, I put here the following, because I had no time to implement them:

- Profile: past events,
- Profile: messages
- Menu: about and terms
- Authentication: sign up with social media
- Authentication: forgotten password. 

However, to continue and evolve the project, I will revisit these items and put them in the next version.

I linked the back-end and front-end parts to the same project, and user stories only went to the “Done” section when they were all done in both parts. 
First, I wanted to separate them, but they connected so much that it made more sense.

### Existing features

<br>

**Authentication**:

- Sign up with username
- Log in with username
- Log out 

**Profile**

- See all the profiles created
- Edit own profile details
- Upload profile photo (change the default)

**Records**

- See all the records created
- Add a record
- Edit that record
- Delete that record
- Like a record
- Dislike a record
- Comment on a record - edit and delete the comment.
- Filter a record by genre
- Search for a record by artist or title
- See the records the user liked
- See the number of likes of a record
- See the number of comments of a record

**Markets**

- See all the markets created
- Add a market
- Edit that market
- Delete that market
- Mark your attendance on the market
- Delete your attendance on that market
- See the number of people attending on that market
- Filter a market by country and city
- See the markets the user attends on

**Admin functions**

- View, edit, and delete users.
- View, edit, and delete profiles.
- View, edit, and delete records.
- View, edit, and delete markets.
- View, edit, and delete comments.

**Error handling**:

- Error message sent when page is not found
- Error message sent when authentication details are not correct
- Error message sent when a field can not be left empty

### In progress (had no time for it)

- Add more default profile photo options

### Future features

- Improve the search field, so that multiple words can be looked at once (now the first word counts)

- Have private chat option


#### Ideas:

- Of course an online shopping cart and paying system would complete the website.

## Deployment and forking

-**Create Github project**
1. Create a new repository
2. In the menu click on project > Link a project > Create new project
3. Click on Board, and give a name > Create
4. Click on the three dots menu, choose workflows
5. Item added to project > Edit
6. Click on issue dropdown, select issue, unselect pull request
7. Status value: status to do > green button: Save and turn on workflow.
8. In your project’s three dots menu (exit workflow) click on Settings
9. In the danger zone section choose visibility.
10. Add user story template: Go to your repository’s settings > Features > Issues > Set template > Custom template (fill out) > Propose changes > Commit changes
11. Add user stories: In your repository’s menu click on issues > new issue > Get started! > Fill out, add labels, connect with your project > Submit a new issue

<br>

- **Github forking:**

1. Go to the selected repository, and click on Fork on the top right side.
2. Select an owner of the forked repository on the dropdown
3. Write a description and select the Default branch only for open-source projects.
4. Click on Create fork.
5. Go to your forked repository.
6. Click on Code, and copy the URL / or open with your Github desktop.
7. With the URL open your terminal, and write git clone and paste it. Enter.

<br>

- **Back-end Heroku deployment:**

1. On the Heroku dashboard create new app with unique name
2. Settings - reveal the config vars - Add the following keys:
<br>

![reveal-configvars](</readme/assets/config-vars.png>)
<br>
The values are unique to your project.

3. Update our code: install gunicorn, and refresh requirement.txt
4. Create Procfile in the root directory, and add: web: gunicorn your_project_name.wsgi
5. In settings.py set Debug = False, and add,'.herokuapp.com' to ALLOWED_HOSTS
6. Git add, commit, push to GitHub

7. On Heroku’s page click on the Deploy tab, and connect your app with your GitHub repository.

8. Click on deploy branch - manually or you can set it up automatically.

9. On the resources tab choose your plan (eco dinos). Verify that there is no existing Postgres database add-on, if so, click on Delete Add-on.

10. After having static files, always run the collectstatic command before deployment.

11. If any error occurs, can see the deployment log - on the top right side click on more, and choose view vlogs. Otherwise, view app.


## Work progress

I followed the agile methods and MoSCoW labeling - must have, should have, could have, and won't have. I prioritized and did first what was most important, then left the less important things to the end, setting up the won't have features as future features.

I started with the backend, since that is the base of the app, moved to the front end, and left styling for the end since I prioritized working features over style.

I was making notes continuously, so I wrote down new ideas, what was working, what was not, and where I needed to go back. Where I met with an error I couldn't handle, rather moved on due to the time frame I had and decided to return later.

(I always opened dev tools and source code to check how the data returned, look for different details, or try out different styles. It helped me find ID-s, understand the forms, and validate my html code.)

I worked on more user stories simultaneously.

I started coding in VSCode and then changed to GitPod in case I needed tutor help. When I made the transition, I set up a separate branch and worked on that for debugging. Then, I pulled and got back to the main branch. 

### Set up the project and back-end

1. Create Django We_love_vinyls projects.
2. Set up the .env file 
3. Set up Cloudinary
4. Create an entity relationship diagram model

<br>

![model-relationship](</readme/assets/model-relationship.png>)
<br>


5. Create user stories
6. Create models
7. Add signals

<br>
Signals working:
<br>

![Signals working](</readme/assets/signals-working.png>)
<br>

8. Create a superuser
9. Add serializers
10. Add AllRecords and AllProfiles views and URLs

<br>
Serializers working: 
<br>

![Serializers working](</readme/assets/serializer-working-1.png>)

![Serializers working](</readme/assets/serializers-working-2.png>)

<br>


11. Add OneRecord, OneProfile views, and URLs, put and get method.

<br>
404 error is working:
<br>

![404 is working](</readme/assets/404-is-working.png>)
<br>

	
For the profiles, I used slug since all usernames should be unique, but for the records, I used the primary key because the titles and artist names are not necessarily unique. 

Later, I changed the profile slug to id for simpler usage on the front end.

12. Create markets app, add AllMarkets, OneMarket views, URL,s put and get method. Add serializers.

13. Set up Django Rest authentication - log in and log out function and permissions to users app.

<br>
Rest permissions working:
<br>

![Rest permissions working](</readme/assets/rest-permissions-working.png>)
<br>

14. Add permission to the records and markets app, also.

15. Add image size validator.

16. Add the post method to records and views so that logged-in users can upload records or events.

17. Add delete method to be able to delete the record or event.

18. Add comment app with URLs, serializers, and views: AllComments & OneComment

19. Add like app with Likes and Attendance models, views, and serializers

20.  Add likes to record serializer, and attendance to market serializer. 

<br>
Can't attemnd twice on the same market
<br>

![Can’t attend twice on the same market](</readme/assets/cant-attend-twice.png>)

<br>

21. Change my user views to generic, so it is easier to look read and edit. Also add attended markets count, and liked record counts.

22. add generic views to markets, set up members attending count

23. add generic views to records plus members liking count

24. add get liked_record_id to user
25. add attended market count to users

26. add comment count to records

In comment count, I connected the comments with content, not the member, because one member can leave more comments.

27. add counts to all records and all markets too

28. add a search field to markets

29. add genre and filter to records

30. add filters

31. Add genre choices and put them in alphabetical order

32. Change filters by ID-s

<br>
Filter attendance by member ID
<br>

![filter attendance by member id](</readme/assets/filter-attendance-by-member-id.png>)
<br>

33. Deployment on Heroku

34. Fix authentication 

35. Validate

36. Test

At this point, I added the front end and accommodated the code for it:

37. Make search options case insensitive.

38. Set up chromes third-party cookies settings

39. Add log-out view and URL

40. Optimize serializers and views for the front end.


### Languages

- [Python](https://www.python.org/downloads/release/python-390/)

### Libraries and frameworks:

- Django, Django REST framework

### Tools, programs, and technologies

-  [VSCode](https://visualstudio.microsoft.com/downloads/)
- GitHub projects
- GitHub Desktop
- Heroku
- Cloudinary
- ElephantSQL
- [NodeJS](https://nodejs.org/en/download/package-manager)
- Gitpod 

### Validating

- [Python Validator](https://pep8ci.herokuapp.com/):

<br>
Comment models: <br>

![comment-models-validator.png](</readme/assets/comment-models-validator.png>)
<br>

<br>
Likes URLs:
<br>

![likes-url-validator.png](</readme/assets/likes-url-validator.png>)
<br>

<br>
Market serializers:
<br>

![market-serializers-validator.png](</readme/assets/market-serializers-validator.png>)
<br>

<br>
Record views.py:
<br>

![records-views-validator.png](</readme/assets/records-views-validator.png>)
<br>

<br>
User serializers:  
<br>

![users-serializer-validator.png](</readme/assets/users-serializer-validator.png>)
<br>

<br>
We love vinyls permissions: 
<br>

![we-love-vinyls-permissions-validator.png](</readme/assets/we-love-vinyls-permissions-validator.png>)
<br>


## Testing and validation


What to do | How to do | Expected outcome | Actual outcome
| :--- | :--: | :--: | :--:
| Open the page | Click on the URL | It shows a welcome message |  It shows a welcome message
| Get to log in page | Write /dj-rest-auth/login/ to the end of URL, hit enter |  It shows log in page |  It shows log in page
| Log in | Fill username & password, click on POST |  It shows my name and log out button |  It shows log in page | It shows my name and log out button
| Log in with wrong details | Fill in the wrong username & password, click on POST |  It shows me an error message. It says: "Unable to log in with provided credentials."
| Log in with missing details | Fill in the email, but not username and/or password, click on POST |  It shows me an error message | "Must include \"username\" and \"password\"."
| Log in without password | Fill in the username and/or email, click on POST |  It shows me an error message | "This field may not be blank."
| Go to log out page | Write /dj-rest-auth/logout/ to the end of URL, hit enter |  It shows the logout page |  It shows the log out page
| Log out | Click on POST |  It shows log in button, and not my name anymore |   It shows log in button, and not my name anymore
| See market lists | Put /markets/ to the end of the URL |  It brings me to the market page, where I can see the list of markets |  It brings me to the market page, where I can see the list of markets
| Add a market logged in | Under the list, I fill out the field and click on POST |  It brings me to the market page, where I can see my new market |  It brings me to the market page, where I can see my new market, it says http 201 created
| Add a market without logging in | I scroll down to find the field | Field is not shown | Field is not shown
| Go to one market page | I write to the end of the URL /markets/4 - the ID of the market |  It shows only that one market and editable fields with the details |  It shows only that one market and editable fields with the details
| Edit market if I am the organizer| I edit the form below and click on put |  It saves changes, and refreshes data |   It saves changes, and refreshes data 
| Delete market if I am the organizer | I see a field asking are you sure you want to delete? I click on delete. |  It deletes the data and goes back to the market list page  |  It deletes the data and goes back to the market list page
 | Edit market if I am not the organizer| I scroll down to find the editing field |  Field is not shown |  Field is not shown
| Delete market if I am not the organizer | I scroll to find deleting field | Field is not shown  |  Field is not shown 
| Filter market | I scroll down to filters and fill out county and/or city contains: fields. | Field shows the result, or writes out there is no match  |  I see matches, for no match I see an empty array
| Case insensitive search | I fill out country and city name with small letters only | Field shows the result (with big capital letters), or writes out there is no match  |  I see matches, for no match I see the empty array
| See record lists | Put /records/ to the end of the URL |  It brings me to the record page, where I can see the list of records |  It brings me to the record page, where I can see the list of markets
| Add a record logged in | Under the list, I fill out the field and click on POST |  It brings me to the record page, where I can see my new record |  It brings me to the record page, where I can see my new record, it says http 201 created
| Add a record without logged in | I scroll down to find the field | Field is not shown | Field is not shown
| Go to one record page | I write to the end of the URL /records/1 - the ID of the record |  It shows only that one record and editable fields with the details |  It shows only that one record and editable fields with the details
| Edit record if I am the advertiser | I edit the form below and click on put |  It saves changes, and refreshes data |  It saves changes, and refreshes data
| Delete record if I am the advertiser | I see a field asking are you sure you want to delete? I click on delete. |  It deletes the data and goes back to the record list page  |  It deletes the data and goes back to the record list page
| Edit record if I am not the advertiser | I scroll down to find the editing field |  Field is not shown |  Field is not shown
| Delete record if I am not the advertiser | I scroll to find deleting field | Field is not shown  |  Field is not shown 
| Search record | I fill out the search field with the name of an artist/album title. | Field shows the result, or writes out there is no match  |  I see matches, for no match I see an empty array. It only takes count the first word in the search
| Case insensitive search | I fill out search field with small letters only | Field shows the result (with big capital letters), or writes out there is no match  |  I see matches, for no match I see the empty array
| Filter by genre | I choose an option from genre-s, click on submit | Field shows the result, or writes out there is no match  |  I see matches, for no match I see the empty array
| Filter by advertiser ID | I write a number in the filter, click on submit | Field shows the result, or writes out there is no match  |  I see matches, for no match I see the empty array. I can also look for both advertiser ID and genre at the same time.
| See the list of likes | I write /likes/ at the end of the URL | It shows the list of likes sent  | It shows the list of likes sent
| Like something without logging in | Scroll for the field  | Field is not shown | Field is not shown
| Like something logged in | I choose which record I want to like from the list, then hit POST  | It says 201 Ok, created | It says 201 ok, created
| Like something twice | I choose the same record as before, then hit POST  | It throws error. | It says "detail": "possible duplicate"
| See who liked what | Fill out the filter with the member ID | It shows the likes of the member with the ID, or that ID is not found, or an empty array if the member hasn’t liked anything | I see matches, for no match I see the empty array
| Like is added to my liked items| I filter my name in the likes list, and check the list | It has the item on it, I have just liked. | It has the item on it, I have just liked.
| See if the like count is working | I go to the record’s page, and check it’s like count | It is now 1. | It shows 1. 
| See the list of attendance | I write /attendance/ at the end of the URL | It shows the list of event attendance  | It shows the list of event attendance
| Hit attend without logging in | Scroll for the field  | Field is not shown | Field is not shown
| Hit attend logged in | I choose which event I want to attend at, then hit POST  | It says 201 Ok, created | It says 201 ok, created
| Attend to something twice | I choose the same event as before, then hit POST  | It throws error. | It says "detail": "possible duplicate"
| See who attends to which market | Fill out the filter with the member ID | It shows the attendance of the member with the ID, or that ID is not found, or an empty array if the member hasn’t marked attend on anything | I see matches, for no match I see the empty array
| Attendance is added to attended markets | I filter my name in the likes list, and check the list | It has the item on it, I have just market to attend. | It has the item on it, I have just marked to attend.
| See if the attendance count is working | I go to the market’s page, and check its attendance count | It is now 1. | It shows 1. 
| See the list of comments | I write /comments/ at the end of the URL | It shows the list of comment sent  | It shows the list of comment sent
| Comment something without logging in | Scroll for the field  | Field is not shown | Field is not shown
| Comment something logged in | I choose which record I want to comment on from the list, then hit POST  | It says 201 Ok, created | It says 201 ok, created
| Comment something twice | I choose the same record as before, then hit POST  | My post is sent as many times as I POST| My post is sent as many times as I POST
| See the comments on a special record | Write the record’s ID to the filter field | It shows the comments for the record of that ID, if the record is not found, or noone liked, there is an empty array| I see matches, for no match I see the empty array
| See if the comment count is working | I go to the record’s page, and check its comment count | It is now 3. | It shows 3, as I sent 3 comments. 
| See the users lists | Put /users/ to the end of the URL |  It brings me to the users' page, where I can see the list of records |  It brings me to the users' page, where I can see the list of markets
| Add a record logged in | Under the list, I fill out the field and click on POST |  It brings me to the record page, where I can see my new record |  It brings me to the record page, where I can see my new record, it says HTTP 201 created
| Add a record without logged in | I scroll down to find the field | Field is not shown | Field is not shown
| Go to one record page | I write to the end of the URL /records/1 - the ID of the record |  It shows only that one record and editable fields with the details |  It shows only that one record and editable fields with the details
| Edit record if I am the advertiser | I edit the form below and click on put |  It saves changes and refreshes data |  It saves changes and refreshes data
| Delete record if I am the advertiser | I see a field asking are you sure you want to delete? I click on delete. |  It deletes the data and goes back to the record list page  |  It deletes the data and goes back to the record list page
| Edit record if I am not the advertiser | I scroll down to find the editing field |  Field is not shown |  Field is not shown
| Delete record if I am not the advertiser | I scroll to find deleting field | Field is not shown  |  Field is not shown 
| Search record | I fill out the search field with the name of an artist/album title. | Field shows the result, or writes out there is no match  |  I see matches, for no match I see an empty array. It only takes count the first word in the search
| Case insensitive search | I fill out search field with small letters only | Field shows the result (with big capital letters), or writes out there is no match  |  I see matches, for no match I see the empty array
| Filter by genre | I choose an option from genre-s, click on submit | Field shows the result, or writes out there is no match  |  I see matches, for no match I see the empty array
| Filter by advertiser ID | I write a number in the filter, and click on submit | Field shows the result, or writes out there is no match  |  I see matches, for no match I see the empty array. I can also look for both advertiser ID and genre at the same time.
| In the admin site I can see, edit, delete all profiles | I open admin and click on profiles, and choose the names. I edit fields and click on save or click on delete.| The profile is edited and/or deleted. | The profile is edited and/or deleted.
| In the admin site I add a new profile | I open admin click on records, and choose to add a profile. I edit fields and click on save. | The profile is added | The profile is added.
| In the admin site I can see, edit, delete all records | I open admin and click on records, and choose the record’s title. I edit fields and click on save or click on delete.| The record is edited and/or deleted. | The record is edited and/or deleted.
| In the admin site I add a new record | I open admin click on records, and choose to add a record. I edit fields and click on save. | The record is added | The record is added.
| In the admin site I can see, edit, and delete all markets | I open admin click on markets, and choose a market. I edit fields and click on save or click on delete.| The market is edited and/or deleted. | The market is edited and/or deleted.
| In the admin site I add a new market | I open admin click on markets, and choose to add a comment. I edit fields and click on save. | The market is added | The market is added.
| In the admin site I can see, edit, and delete all comments | I open admin click on comments, and choose a comment. I edit fields and click on save or click on delete.| The comment is edited and/or deleted. | The comment is edited and/or deleted.
| In the admin site I add a new comment | I open admin click on comments, and choose to add a comment. I edit fields and click on save. | The comment is added | The comment is added.

<br>
Welcome message:
<br>

![Welcome message](</readme/assets/welcome-message.png>)
<br>


<br>
Log in error:
<br>

![Log in error](</readme/assets/log-in-error.png>)
<br>

<br>
Market added: 
<br>

![Market added](</readme/assets/http-201-created-market.png>)
<br>

<br>
No match empty array
<br>

![No match empty array](</readme/assets/no-market-match-empty-array.png>)
<br>

<br>
Market match case insensitive:
<br>

![Market match case insensitive](</readme/assets/market-match-case-insensitive.png>)
<br>

<br>
Member 1 liked items list:
<br>

![Member 1 liked items list](</readme/assets/member-1-liked-items-list.png>)
<br>

<br>
Comment filter record 1
<br>

![Comment filter record 1](</readme/assets/comment-filter-record-1.png>)
<br>

<br>
Comment added from admin page:
<br>

![Comment added from admin page 1](</readme/assets/comment-added-from-admin-page.png>)
<br>


### Bugs and solutions

**1.**  Field name `id` is not valid for model `Profile` in `users.serializers.ProfileSerializer` - the id field is not created by itself. 

solution: It was not managed, so I set managed true in my model. 

class Meta:
        managed = True
        db_table = 'records_record'
        
        —That solves the record's ID, but the profile ID does not because the profile is automatically created when the User is. So, the user needs to be set to managed true.


I put id to read_only field, and now it is shown. 

id = serializers.ReadOnlyField(source='user.id')

 - Then I noticed, username has the primary key attribute. 


**2.** Permission is not working. It said market and record has no “member” field.

I chose different naming in all 3 apps because it makes more sense, but all of them refer to the user. (I could name them the same if I want it simpler.)

I did not want to repeat the same code three times, so I created a user_field variable that I could change for all three permission classes.
 
**3.** I changed my views to generic, and got this error since I was using slug: Expected view OneProfile to be called with a URL keyword argument named "pk". Solution: I added the lookup_field.

**4.** I got the like’s ID, not the record’s ID when I want to present which records the user liked. - through like id I can see the liked_record id. - solution: Set up filter by users to the like views..

**5.** When I want to show all the markets, user attends, only shows the first one. - add filters, in backend I have data separate, but in frontend I can put them on the same (or any) page

**6.** Can’t install django-rest-auth with social - Needed to downgrade my python, so I created a new virtual environment in my VS CODE and continued to code there. 

**7.** I wanted to login, got this error: 
Exception Value:
djangorestframework_jwt needs to be installed

Installed, still:

Method Not Allowed: /dj-rest-auth/login/
[30/Jun/2024 19:01:41] "GET /dj-rest-auth/login/ HTTP/1.1" 405 8605

Solution: JWT and PyJWT clashed, needed to uninstall both and install back PyJWT. 

**8.** The search field is case-sensitive.
The documentation says it should be insensitive by default, but it still doesn’t work. - Solution: Added django_filters contains.

**9.** Editing and deleting did not work.. On the local server, when I run from VSCode they do work, but when deployed on Heroku, they don’t. The GET Url has the edited version, it says the get method is allowed, still, the data is untouched.. I investigated cookies and token error, my Google Chrome blocked the third-party cookies, so I need to set up the settings.

<br>

![Edit and delete dont work](</readme/assets/edit-error-edit-in-url-still-not-shown.png>)
<br>

**Known bugs:**
 None.

## Credits and sources

### Content
 -  Some content like the readme setup or signals file setup is from my [Ghost Stories](https://github.com/saroltah/ghost_stories) project. I used my previous project as inspiration. 

- I share ReadMe content with the front-end side of my project

- Permission variables: [chatGPT](https://chat.openai.com/)

def __init__(self, user_field='member'): self.user_field = user_field
return getattr(obj, self.user_field) == request.user
def __init__(self): super().__init__(user_field='member')

- Lookup_field:[django-rest-framework.org](https://www.django-rest-framework.org/api-guide/generic-views/)

- key=lambda x:x[1]): [ChatGPT](https://chat.openai.com/)

- Learned a lot from [Django-rest-framework](https://www.django-rest-framework.org/tutorial/quickstart/)

- Set up django_filter MarketFilter class: [ChatGPT](https://chat.openai.com/)

- Followed along and adapted Code Institute’s walkthrough project: Moments.

### Images, fonts

**images:**
- profile picture: [undraw](https://undraw.co/)
- default record: Photo by [Brett Jordan](https://unsplash.com/@brett_jordan?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/black-and-white-vinyl-record-hrUhyFq6u-A?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)









