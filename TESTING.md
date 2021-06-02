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
#### Casual Users Wants

- easily navigate the site to find what I am looking for quickly:
    Homepage offers information about the organisation, menu and cats as well as links to cats page, shop, help page and contact page.

![Browse](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/browse.gif)

- view the site on all screen sizes:
    The site is highly responsive. Nav is fixed for small devices, image overlays display without hover where approproate on small devices.

![Responsive](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/inner-purr-responsive.JPG)

-  view information on the cafe such as opening hours and social media:
    Footer contains information such as opening hours and social media links.

![Footer](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/footer.JPG)

-  sign up to recieve news from the Inner Purr:
    A newsletter sign up allows users to notify admin of their wish to recieve newsletter.

![Newsletter](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/newsletter.gif)

-  search filter and sort products:
    shop page enables users to search and filter products on offer.

![Search](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/search.gif)

-  view details on products:
    Product details page gives information on sizes available as well as price rating and large product image.

![Details](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/product-details.JPG)

-  purchase products and see my actions throughout the process, review my order at checkout, make secure payments & receive email confirmation of my order:
    Users can add products to a bag, see totals accumulate as items are added and have toasts pop up to give users feedback on their actions. Payments are securely made using Stripe. An email is sent after a purchase is complete.

![Purchase](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/purchase.gif)

-  access contact details:
    Contact page displays relevant email addresses as well as a map while the footer displays an address and social media links.

![Contact](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/contact.JPG)

-  learn how I can help the work of the Inner Purr:
    Help Us page offers information on how donations can be made and volunteering roles. External links link to the parent charity of the Inner Purr (Phibsboro Cat Rescue).

![Help](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/help.JPG)

-  register for a user profile account by choosing a username and password:
    Users may register a profile and save their information to make future payments more convenient.

![Register](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/register.gif)

### Registered Story Testing
#### Registered User Wants

- log in and log out of my profile account:
    users may select to register from a dropdown in the navbar.

![Login](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/login.gif)

- update my details, store my address and order history:

![Profile](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/profile.JPG)

### Admin Story Testing
#### Admin User Wants

- add new products, menu items, volunteering roles etc:
    Products, cats, menu items, volunteering roles, donation options and contact addresses can all be added, edited and deleted through the django admin.

![Admin](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/admin.gif)

    Products can also be added using a form in the product management section of the site

![Products](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/product-add.JPG)

- edit products:
    Products can be edited using a form

![Edit](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/product-edit.gif)

- delete products:
    Products can be deleted via the products or product details page

![Delete](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/product-edit.gif)

- add notices for each page:
    Notices can be added for seperate pages to give relevant information on opening announcments, adoption waiting list news etc...

![Notice](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/notice.JPG)

- change the status of cats so that they can be categorized properly:
    by checking the relevant boxes cats can be placed in the Resident Cat Gallery, the Cats for adoption gallery or the adopted cat gallery as appropriate as well as the carousel of Resident Cats on the home page.

![Status](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/user-stories/status.gif)
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