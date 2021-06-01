# Testing

[return to README.md](https://github.com/Sean-Mc-Mahon/McTasticRecipes)


**<details><summary>Testing</summary>**
* [**_User Testing_**](#user-testing)
* [**_Problems and Solutions_**](#problems-and-solutions)
* [**_Validators_**](#validators)
* [**_Manual Testing_**](#manual-testing)
</details>

---

# User Testing

### User Story Testing

_- User Story A:_ As a casual user I would to easily browse recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-a.gif)

User can search by ingredient, sort results, hover over an image to preview information with the help of tooltips, navigate to the recipe, enlarge the image and check off ingredients and steps as they make the recipe.

_- User Story B:_ As a user I would like to create a profile and delete it if I no longer want it.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-b.gif)

User can navigate to registration, enter a username and password and if they are valid and the username is not taken she can create a profile and be redirected to their new profile with a flash message to wwelcome them. They can later delete the profile after clicking past a warning from a modal and will be notified by a flash message that the profile has been deleted.

_- User Story C:_ As a registered user I would like to add, edit, update or delete my own recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-c.gif)

User can input information, choose categories and preview image prior to adding recipe. User may then edit the recipe or delete it.

_- User Story D:_ As a registered user I would like to view what recipes other users have created.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-d.gif)

User can navigate to users page and view any user to browse their reciepes, they may also click the 'Created By' link on any recipe to view the corresponding profile.

_- User Story E:_ I would like to be able to view the recipes clearly regardless of the type of device I use.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-e.gif)

The app is fully resonsive and a user can use the app comfortably on any device size.

_- User Story F:_ I would like to be able to easily share recipes.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-f.gif)

User can hover or click on the share icon on the bottom right of the screen and choose what platform thay would like to use to share the page.

_- User Story G:_ I would to be able to convert units from metric to imperial and vice versa.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-g.gif)

User can click on any field of a card on the conversions section and any figures they input will be converted to all other units on that card.

_- User Story H:_ As a registered user I would like to add, edit, update or delete my own ingredients.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/story-h.gif)

User can click add button on units page to add ingredient using a modal, if fields are filled and ingredient name is not in use the ingredient will be added and the user may edit or delete the ingredient as long as they are logged in.

### Admin Story Testing

_- Admin Story A:_ As the admin I would like to be able to delete any user along with all recipes created by that user.

![Browse](https://github.com/Sean-Mc-Mahon/McTasticRecipes/blob/master/wireframes/admin-story-a.gif)

Admin may access any profile by the 'Created By' link in a single_recipe page or by the corresponding 'view' button on the users page and after confirming the intention to delete in a modal the user will be deleted along with any recipe they created.

---

# Manual Testing

1. **Developer Tools:** Chrome, Firefox and Microsoft Edge web dev tools using iPhone 5 and Ipad as toggle devices to test responsiveness.

2. **Lighthouse:** A number of issues were resolved using lighthouse.

    Page | Performance | Accessability | Best Practices | SEO
    ------------ | --------------- | --------- | --------- | ---------
    **index.html** |82|100|100|99
    **login.html** |93|90|100|100
    **register.html** |93|98|100|100
    **view_profile.html** |57|100|93|99
    **insert_recipe.html** |89|92|100|98
    **edit_recipe.html** |87|92|100|98
    **single_recipe.html** |54|99|93|100
    **users.html** |94|100|100|99
    **units.html** |94|100|100|100

    **Performance**
    - Script.js broken into seperate files as unnused Javascript was the biggest factor in low performance scores.

    **Accessability**
    - Contrast: Alpha level on .blank-image was set to 0.6 which did not offer sufficient contrast with white text. Alpah level rasied to 0.8.
    - Aria labels: Aria labels added to buttons such as #search-button and #submit
    - Alt Text: Alt text dynamically applied to images eg `alt="{{recipe.recipe_name}} image"`
    - Lists: headers moved from inside pagination `<ul>` to above the list.
    
    **Best Practices**
    - Logo image resized.
    
    **SEO**
    - Description meta tag added on all pages.

3. **Mobile Devices:** I used my Google Pixel 3a phone and Amazon Fire tablet to test the site.

4. **amiresponsive:** [Am I Responsive](http://ami.responsivedesign.is/) Used to test responsiveness across a range of devices.

5. **Friends and family:** I asked for feedback from friends and family in order to get a users perspective.

## Functionality

### Header and Footer
#### base.html

action taken | expected result | pass/fail
------------ | --------------- | ---------    


---

# Problems and Solutions

#### URL Issue
- Problem: url not found for checkouts although all urls seemed in order in the checkouts url file.
- Solution: A typo in the project level urls which was also copied and pasted into the stripe endpoints was the source of the problem.

#### Database Migrations
- Problem: Database would not migrate to Postgres
- Solution: Dumping old orders with a full country name prior to installing CountryField was causing an issue as the model was expecting two chareacters. I instead dumped data only for the models I required (products/cats etc...) and the migrations performed as expected.

#### Media Files not displaying on Deployed Site
- Problem: Some media files not displaying on deployed site
- Solution: Syntax corrected in src attribute for images in index.html file from '..media/example.jpg' '{{ MEDIA_URL }}example.jpg'

#### Media Files not displaying on Deployed Site
- Problem: After adding additional models to apps a server 500 error was displayed on deployed site.
- Solution: Running migrations and performing a data dump solved the issue.


### Currently Unsolved Problems

#### Login Form Checkbox
- Problem: Unable to locate form used in login template.
- Solution:

#### Materialize Toast Function
- Problem: Console error triggered by Materialize 'M' function.
- Solution:
---

# Validators

1. **HTML:** [W3C HTML Validator](https://validator.w3.org/) Used to identify HTML errors

2. **CSS:** [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) Used to identify CSS errors

3. **Javascript:** [JSHint](https://jshint.com/) Used to identify Javascript errors.

4. **Python:** [Pep8](http://pep8online.com/) Used to check that python files are PEP8 compliant
---

##### back to [top](#testing)