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

    **Performance**
    - Some inages compressed to improve performance, as the site heavily involves user input I have chosen not to compress all images as this may not reflect how the site may be used in the future. This partly explains why lighthouse performance scores are comparitvely low.

    **Accessability**
    - Contrast: Alpha level on .blank-image was set to 0.6 which did not offer sufficient contrast with white text. Alpah level rasied to 0.8.
    - Aria labels: Aria labels added to buttons such as increment and decrement quatity buttons in bag.
    - Alt Text: Alt text added to images such as home page full slider images.
    
    **Best Practices**
    - Bag and Profile icons in navbar redesigned and resized to a correct ratio.
    
    **SEO**
    - Description meta tag added on all pages.


    Page | Performance | Accessability | Best Practices | SEO
    ------------ | --------------- | --------- | --------- | ---------
    **home** |82|100|100|99
    **login** |92|90|100|100
    **logout** |87|98|100|100
    **register** |94|98|100|100
    **reset password** |95|98|100|100
    **reset password sent** |94|98|100|100
    **view_profile** |57|100|93|99
    **All Products** |82|90|100|100
    **product details** |66|98|100|100
    **bag** |64|96|100|100
    **help** |91|98|100|100
    **contact** ||||

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

## Functionality

### Header and Footer
#### base.html

action taken | expected result | pass/fail
------------ | --------------- | ---------    
**Logo** |
Clicked Logo | Display index view, browser tab displays 'The Inner Purr Home' | pass
Clicked Logo | Image Logo head rises | pass
Move Mouse | Eyes and Paws follow mouse | pass
**Lower Nav** |
When on displays >= 992px: lower nav | The Purr/Cats/Shop/Help Us/Contact links should display | pass
Clicked The Purr within topnav | Display index view, browser tab displays 'The Inner Purr Cats' | pass
Clicked Cats within topnav | Display all_cats view, browser tab displays 'The Inner Purr Home'  | pass
Clicked Shop within topnav | Display all_products view, browser tab displays 'The Inner Purr Products'  | pass
Clicked Help Us within topnav | Display help view, browser tab displays 'The Inner Purr Help Us'  | pass
Clicked Contact within topnav | Display contact view, browser tab displays 'The Inner Purr Contact'  | pass
**Side Nav** |
When on displays < 992px: lower nav | Burger menu should display and when clicked reveal side nav | pass
Clicked The Purr within topnav | Display index view, browser tab displays 'The Inner Purr Cats' | pass
Clicked Cats within side nav | Display all_cats view, browser tab displays 'The Inner Purr Home'  | pass
Clicked Shop within side nav | Display all_products view, browser tab displays 'The Inner Purr Products'  | pass
Clicked Help Us within side nav | Display help view, browser tab displays 'The Inner Purr Help Us'  | pass
Clicked Contact within side nav | Display contact view, browser tab displays 'The Inner Purr Contact'  | pass
**Dropdown Nav** |
Clicked profile-drop within Dropdown Nav | Display links Product Management (if superuser), My Profile (if logged in), Logout (if logged in), Login (if not logged in), Register (if not logged in) | pass
Clicked Product Management within topnav | Display add_product view, browser tab displays 'The Inner Purr Add Product' | pass
Clicked My Profile within Dropdown Nav | Display profile view, browser tab displays 'The Inner Purr Profile' | pass
Clicked Logout within Dropdown Nav | Display account_logout view, browser tab displays 'The Inner Purr Profile' | pass
Clicked Login within Dropdown Nav | Display account_login view, browser tab displays 'The Inner Purr Login' | pass
Clicked Register within Dropdown Nav | Display account_signup view, browser tab displays 'The Inner Purr Register'| pass
**Footer** |
Enter valid email address and submit #form-contact | Alert displayed thanking user for signing up. Email sent. | pass
Enter email adress without an '@' and submit #form-contact | Alert is displayed informing user that a '@' is required | pass
Enter incomplete email address and submit #form-contact | Alert is displayed informing user that address is incomplete | pass
Clicked 'All Done' on modal following newsletter signup | Modal is closed | pass
Clicked LinkedIn icon | LinkedIn profile opened in new tab | pass
Clicked Instagram icon | Instagram profile opened in new tab | pass
Clicked Facebook icon | Facebook profile opened in new tab | pass

**Notices** |
for various view: | Notice displayed and removed when close button clicked | pass

### Cats App
#### all_cats view
action taken | expected result | pass/fail
------------ | --------------- | ---------
Resident Kitties | Slider displays Images with cats name and a tagline. Another image displayed after 10 seconds or when relevant indicator is clicked on|pass
Images clicked on slider or Kitties for adoption images | Relevant cat profile displayed |pass
Links clicked | New tabs opened on relevant external pages |pass
**On displays =< 600px**|
Kitties for Adoption | gallery-items displayed occupying 12 columns, item displays as square image with name and gender dispayed at bottom of image. Image zoomed on hover|pass
Adopted Kitties | Gallery-items displayed occupying 6 columns, item displays as square image. Name dispayed and image zoomed in on hover|pass
**On displays > 600px**|
Kitties for Adoption | gallery-items displayed occupying 6 columns, item displays as square image with name and gender dispayed at bottom of image. Image zoomed on hover|pass
Adopted Kitties | Gallery-items displayed occupying 3 columns, item displays as square image. Name dispayed and image zoomed in on hover|pass
**On displays > 992px**|
Kitties for Adoption | gallery-items displayed occupying 4 columns, item displays as square image with name and gender dispayed and image zoomed on hover|pass
**On displays > 1200px**|
Kitties for Adoption | gallery-items displayed occupying 3 columns|pass
Adopted Kitties | Gallery-items displayed occupying 2 columns |pass

#### cat_details view
action taken | expected result | pass/fail
------------ | --------------- | ---------
On displays =< 600px | Image and details occupy 12 columns. Name and bio occupy 12 columns|pass
On displays > 600px | Image and details occupy 4 columns. Name and bio occupy 8 columns|pass

### Shop App
#### all_products view 
action taken | expected result | pass/fail
------------ | --------------- | ---------
product clicked | redirected to correct product_details view |pass
super user logged in | edit and delete options below products |pass

**Search, Sort By and Filter**|
On displays =< 600px |Search, Sort By and Categories occuppy 12 columns|pass
On displays > 600px  |Search coccupies 12 columns, Sort By and Categories occupy 6 columns|pass
On displays > 992px  |Search, sort by and filter all occupy 4 columns|pass
**Search**|
Entered a value into #search form and submitted it. | all_products view loads with query results, number of results are displayed as well as the searched term | pass
**Sort By**|
'Sort By' option chosen. | all_products view loads with query results in order specified, number of results are displayed as well as the searched term (if any) | pass
**Filter**|
'Filter' option chosen. | all_products view loads with query results in order specified (if specified), number of results are displayed as well as the searched term (if any) | pass

#### product_details view 
action taken | expected result | pass/fail
------------ | --------------- | ---------
increment/decrement buttons clicked | quantities altered accordingly |pass
image clicked | image opened in new window |pass
'keep shopping' button clicked | return to all_products view |pass
category link clicked | return to all_products view with relevant products |pass
'add to bag' clicked | toast displays correct bag information and grand total updated in nav |pass
super user logged in | edit and delete options below products |pass

#### add_product view 
action taken | expected result | pass/fail
------------ | --------------- | ---------
required fields not filled in | prompted to fill all required fileds |pass
required fields filled in | product added, toast displayed and redirected to product_detail view |pass

#### edit_product view 
action taken | expected result | pass/fail
------------ | --------------- | ---------
required fields filled in | product edited, toast displayed and redirected to product_detail view |pass

#### delete_product view 
action taken | expected result | pass/fail
------------ | --------------- | ---------
delete button clicked | product deleted, toast displayed and redirected to pall_products view |pass

### Bag App
#### view_bag view
action taken | expected result | pass/fail
------------ | --------------- | ---------
bag icon clicked | displays correct bag information |pass
increment/decrement buttons clicked | quantities altered accordingly |pass
Update/Remove buttons clicked | quantities and grand total altered accordingly |pass
'keep shopping' button clicked | return to all_products view |pass
'adjust bag' button clicked | return to bag view |pass
'secure checkout' clicked | redirected to checkout with prefilled delivery information if available and product info available |pass
form filled and 'complete order' clicked | loading spinner commences, redirected to checkout successful page, toast displays order information |pass
form filled incorrectedly and 'complete order' clicked | info box displays required fields |pass
card info incorrect | Incomplete card message appears in payment box |pass

### Help App
#### help view
action taken | expected result | pass/fail
------------ | --------------- | ---------
external links clicked | redirected to external page with a new window |pass

### Contact App
#### contact view
action taken | expected result | pass/fail
------------ | --------------- | ---------
Map pin clicked | map zooms on location with address displayed |pass

### Profile App
#### contact view
action taken | expected result | pass/fail
------------ | --------------- | ---------
Form edited | Details altered accordingly |pass

##### back to [top](#testing)