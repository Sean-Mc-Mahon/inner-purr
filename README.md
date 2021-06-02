# The Inner Purr

### [Live Site](https://inner-purr.herokuapp.com/)

### [GitHub](https://github.com/Sean-Mc-Mahon/inner-purr)

**Please note**: To open any links in this document in a new browser tab, please press `CTRL + Click`.

![Various Devices](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/inner-purr-responsive.JPG)

The Inner Purr is a Milestone 4 project, it is part of the Fullstack Software Development Course of [Code Institute](https://codeinstitute.net/).

#### For testing the following credentials can be used:
* User Credentials:  
  - Username: bobby  
  - Password: passbob1 
  - Email: test@test.com 

* Card payments:
  - Card number: 4242 4242 4242 4242
  - Zip & CCV must be filled out with any integers

# Table of Contents

**<details><summary>Project overview</summary>**
* [**_Project overview_**](#project-overview)
* [**_User Stories_**](#user-stories)
* [**_Admin Stories_**](#admin-stories)
</details>

**<details><summary>UX</summary>**
* [**_Strategy Plane_**](#strategy-plane)
* [**_Scope Plane_**](#scope-plane)
* [**_Structure Plane_**](#structure-plane)
* [**_Skeleton Plane_**](#skeleton-plane)
* [**_Surface Plane_**](#surface-plane)
    * [_Color Scheme_](#color-scheme)
    * [_Typography_](#typography)
    * [_Media_](#Media)
    * [_Wireframes_](#wireframes)
</details>

**<details><summary>Features</summary>**
* [**_Existing Features_**](#existing-features)
* [**_Features Left to Implement_**](#features-left-to-implement)
</details>

**<details><summary>Technologies Used</summary>**
* [**_Libraries_**](#libraries)
* [**_Version Control_**](#version-control)
</details>

**<details><summary>Accessibility</summary>**
* [**_Semantics_**](#semantics)
* [**_Labels_**](#labels)
* [**_Contrast_**](#contrast)
* [**_Keyboard_**](#keyboard)
</details>

**<details><summary>Database Structure</summary>**
* [**_Cats App_**](###Cats-app)
* [**_Checkout App_**](###Checkout-app)
* [**_Contact App_**](###Contact-app)
* [**_Help App_**](###Help-app)
* [**_Home App_**](###home-app)
* [**_Products App_**](###products-app)
* [**_Profiles App_**](###profiles-app)
</details>

**<details><summary>Testing</summary>**
* [**_Testing_**](#testing)
</details>

**<details><summary>Deployment</summary>**
* [**Deployment**](#deployment)
</details>

**<details><summary>Credits</summary>**
* [**_Content_**](#content)
* [**_Acknowledgements_**](#acknowledgements)
</details>

---

# Project Overview

The Inner Purr is an e-commerce site for the center of the same name. The Inner Purr is the public face of PCR(Phibsboro Cat Rescue), a charity that rescues stray cats around Dublin. The Inner Purr is a place where people can interact with cats under PCR supervision. The Inner Purr also houses a shop and cafe.  <br> 
The purpose of the site is to sell the products on offer by the Inner Purr as well as provide a service where people may book a time slot with the cats.

---

### User Stories

|      As a/an...       |                         I want the ability to...                          |
|:---------------------:|:-------------------------------------------------------------------------:|
|                       |                                                                           |
|          ---          |                                    ---                                    |
| Casual User           | easily navigate the site to find what I am looking for quickly            |             
| Casual User           | view the site on all screen sizes                                         |
| Casual User           | view information on the cafe such as opening hours and social media       |
| Casual User           | Sign up to recieve news from the Inner Purr                               |
| Casual User           | search, filter and sort products                                          |
| Casual User           | view details on products                                                  |
| Casual User           | purchase products and see my actions throughout the process, 
review my order at checkout, make secure payments & receive email confirmation of my order          |
| Casual User           | access contact details                                                    |
| Casual User           | learn how I can help the work of the Inner Purr                           |
| Casual User           | register for a user profile account by choosing a username and password   |
|          ---          |                                    ---                                    |
| Registered user       | log in and log out of my profile account                                  |
| Registered user       | update my details, store my address and order history                     |
|          ---          |                                    ---                                    |
| Site admin/superuser  | add new products, menu items, volunteering roles etc...                   |
| Site admin/superuser  | update and delete products                                                |
| Site admin/superuser  | add notices for each page                                                 |
| Site admin/superuser  | change the status of cats so that they can be categorized properly        |

---

## Opportunities arising from user stories

<div align="center">
 
|Opportunities | Importance | Viability / Feasibility
|-----|:------:|:-----:|
|**Simple Clean UI** | 5 | 5 |
|**Clearly indicate purpose** | 5 | 5 |
|**Clear Simple Instructions** | 5 | 5 |
|**Simple creation of products** | 5 | 5 |
|**Simple edit of products** | 5 | 5 |
|**Search/filter/sort Feature** | 2 | 5 |

</div>

---

## UX Planes

### Strategy Plane

- Business Goals:  Provide a revenue stream for the Inner Purr through online purchases as well as raising awareness for the work done at the Inner Purr and by it's parent charity Phibsboro Cat Rescue.

- Audience: The audience are cat lovers throughout Dublin and across Ireland, capitalizing on the existing audience of social media channels of Phibsboro Cat Rescue.

### Scope Plane

- 


### Structure Plane

- The site uses a consistent structure, a navbar is at the top of the page which allow a user to navigate the site and login if needed. A burger menu is used for small devices.
- The products page has a search bar, filter and sort feature.
- The content is consistant with text kept to a minimum.
- A footer at the bottom provides copyright information and links to social media pages and newsletter signup. 
- The number of clicks needed to reach any page is kept to a minimum. Sections such as user profiles will not be visible to users who are not logged in.
- Buttons/modals/links are consistant in design.

### Skeleton Plane
#### Wireframes

I Figma to create the [wireframes](https://github.com/Sean-Mc-Mahon/inner-purr/tree/main/wireframes/figma-wire-home).

Various alterations were made along the way such as removing the parallax above the footer for all pages except the home page and the additon of a page for information about donations and volunteering.

### Surface Plane

- The number is fonts is kept at a minimum as well as using a limited and consistant color scheme.

#### Design

A standard layout is fully responsive on mobile devices and larger screens.

#### Color Scheme

Colors are kept to a minimum and reflect the existing branding of the Phibsboro Cat Rescue. Color scheme can be found on my Coolors profile: [Coolors](https://coolors.co/u/sean_mcmahon)

![Color Palette](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/color-scheme.JPG)

#### Typography

2 [Google Fonts](https://fonts.google.com/) were used across the site:
- [Architects Daughter](https://fonts.google.com/specimen/Architects+Daughter?query=architects) : Logo & Headings, used for it's sketch-like relaxed style.
- [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montse) : Body, used for it's excellent readability.

#### Media

All images are the authors own unless. Logos are also produced by the author using Affinity Design using the existing Phibsboro Cat Rescue Logo as a template.


- [Affinity Designer Logo Process](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/head.png)

##### back to [top](#table-of-contents)

---

# Features

## Existing Features

### Elements on every page
#### Navbar

![Navbar](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/nav.JPG)

- The navigation bar features a logo and name in the top left corner, both are links to the home page. Navigation links are in the top right. On loading the homepage Mr.Buttons, the PCR mascot will raise his head from the bottom of the nav. While the mouse is moving his eyes and paws follow the mouse.

- For all visitors to the site list item links are available for them to use.
    1. The Purr
    2. Cats
    3. Shop
    4. Help Us
    4. Contact

When a link is hovered over Mr.Buttons will reach out a paw towards it.

![Small Navbar](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/nav-sm.JPG)

On the smaller resolutions (tablet, mobile) the navbar is collapsed into a burger icon. A slide out menu opens when the burger icon is clicked. The navbar is fixed to the top on small devices.

- On all resoltions a drop down menu provides links to profile pages. For users who are not logged in the options are:
    1. Login
    2. Register

- For Logged in users the options are:
    1. My Profile
    2. Logout

- For Logged in superusers the options are:
    1. Product Management
    2. My Profile
    3. Logout

- On all resoltions a basket icon represents a link to the user's bag and a grand total will be displayed next to the bag.

#### Footer

![Footer](https://github.com/Sean-Mc-Mahon/inner-purr/blob/main/wireframes/footer.JPG)

The footer features:
    - Newsletter signup: Users may submit an email to request a newsletter.
    - Opening Hours
    - Links to social media platforms.  

### Individual Pages

### Home
- An Image slider highlights aspects of the Inner Purr.
- The home page offers information about the Inner Purr as well as Phibsboro Cat Rescue. 
- A menu title is displayed over a parralax image.
- Menu items added through the django admin are displayed in the menu section
- Resident cats of the Inner Purr as defined through the django admin are displayed in a carousel.
- An instagram feed displays instagram posts.
- A parrallax containing a quote is above the footer.

### Cats
- An Image slider highlights cats currently residing in the purr as defined through the django admin. The images are links to individual profiles.
- Cat cards of cats currently awaiting adoption as defined through the django admin. The images are links to individual profiles.
- A grid of images of adopted cats as defined through the django admin. The images are links to individual profiles.

### Products
- Product cards of products added through the django admin or via the add_product page are displayed here. The images are links to individual products. A super user has options to edit or delete products here.
- The index page has a search bar, filter and sort feature. The search feature searches for keywords in titles and descriptions. If a user performs a search they will be able to sort the search results.
- The sort feature allows users to sort the results by A-Z, Z-A, price, category and rating.
- The filter allows users to display recipes under the categories set out using django admin.

### Help Us
- Volunteering roles as well as Donation options as defined through django admin are listed on this page along with links to the relevant pages of the Phibsboro Cat Rescue website.

### Contact
- Various email addresses as set out using django admin are listed on this page along with a map outlining the location of the Inner Purr using the PCR logo as the pin.

### My Profile
- A form allows users to update their personal details and an order history section lists previous orders.

### Bag
- The bag page gives information on the products in a user's bag as well as details on the grand total and shipping, links bring users back to the products page or the checkout page.

##### back to [top](#table-of-contents)

# Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - HTML5 is the latest version of Hypertext Markup Language, the code that describes web pages.
- [CSS (Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) - CSS describes how HTML elements are to be displayed on screen. 
- [Python](https://www.python.org/) - Used throughout the site 
- [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design 
- [JavaScript](https://www.javascript.com/) - Used for various animations and functions.
- [Materialize](https://materializecss.com/) - Used to aid responsive design and for componants such as sliders and carousels.
- [Heroku](https://dashboard.heroku.com/) - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Heroku PostGres](https://www.heroku.com/postgres) - Heroku Postgres is a managed SQL database service provided directly by Heroku.
- [Google Fonts](https://fonts.google.com/) - Google Fonts is a library of free licensed font families.
- [Stripe payments](https://stripe.com/docs) - Stripe offers payment processing software and application programming interfaces for e-commerce websites and mobile applications.
- [Gitpod](https://code.visualstudio.com/) - Code Editor used to create the site.
- [GitHub](https://github.com/) - Used to host repos for the site.
- [Screen Recorder](https://chrome.google.com/webstore/detail/screen-recorder/hniebljpgcogalllopnjokppmgbhaden?hl=en) - Used to make GIFs for README.
- [Chrome/Firefox/Bing DevTools](https://developers.google.com/web/tools/chrome-devtools) - Regularly used to test the site (Primarily Chrome).
- [W3C Markup Validation Service](https://validator.w3.org/https://jigsaw.w3.org/) - Used to test code for errors.
- [Affinity Designer](https://affinity.serif.com/en-gb/) - Illustration software used to create logos and icons.
- [Figma](https://figma.com) - Collaborative interface design tool used for creating wireframes as well logos and SVGs.
- [Tinypng](https://tinypng.com/) - Used to compress images.
- [Croppola](https://croppola.com/) - Used to crop images.
- [Randomkeygen](https://randomkeygen.com/) - Used to generate random keys.
- [Kaffeine](https://kaffeine.herokuapp.com/) - Used to keep Heroku app from falling asleep.
- [Elfsight](https://elfsight.com/instagram-feed-instashow/) - Used to provide an instagram widget on the homepage.
- [Google Maps](https://developers.google.com/maps) - Used to provide a map in the contact page.

### Libraries

- [Materialize](https://materializecss.com/) - is a framework for building responsive, mobile-first websites. I used materialize to create grid layouts, navbar, cards, forms, buttons and modals as well as features such as collapsibles, materialbox, tooltips and tabs.

- [JQuery](https://jquery.com/) - is a Javascirpt library. I primarily used JQuery to add and remove classes on hover states as well as run various Materialize functions.


- [Jinja](https://flask.palletsprojects.com/en/1.1.x/) - is a templating language for Python. I primarily used it to display data from the backend in HTML.

- [dnspython](https://pypi.org/project/dnspython/) - is a DNS toolkit for Python.

### Version Control

- [Git](https://git-scm.com/) - used for version control

- Branches were used to experiment with ...

---

# Accessibility

### Semantics

- HTML5 Semantics used throughout (header, nav, main etc...)
- Titles used throughout ( etc...)
- Language is set to english (`<html lang="en">`)

### Labels

- Aria labels used throughout eg `<button id="submit" aria-label="submit" type="submit">`
- Alt Text: Alt text dynamically applied to images eg `alt="{{...}} image"`

### Contrast

- All pages have been checked for contrast issues using [Lighthouse](https://developers.google.com/web/tools/lighthouse) and contrast adjusted as necessary throughout.

### Keyboard

- All clickable elements are focusable with classes such as `.focus-outline`, `.focus-background` etc... added in `style.css` in order to make the site smoothly navigable without the use of a mouse.
  
# Testing
All testing and validation is contained within a separate .md file. 

<br> [View TESTING.md](TESTING.md)

# **Database Structure**

During development SQLite3 was used as the database, which is the default database used by Django. For deployment of this project, PostgreSQL database was used, as an add-on using Heroku.

Using Django Allauth and it's default `django.contrib.auth.models`, provided me with the the **User model** used in the profile app.

The structure of the Product and Checkout apps are guided by the Code Institute's walkthrough project, **Boutique Ado**.

## Data Models

### Cats app

#### Sex model

| Name          | Database Key  | Field Type        | Validation                             |
| ------------- | ------------- | ----------------- | -------------------------------------- |
| Sex           | sex           | models.CharField  | max_length=254                         |

#### Product model

| Name          | Database Key  | Field Type          | Validation                                                                              |
| ------------- | ------------- | ------------------- | ----------------------------------------------------------------------------------------|
| Name          | name          | models.CharField    | max_length=254                                                                          |
| Sex           | sex           | models.ForeignKey   | 'Sex', null=True, blank=True, on_delete=models.SET_NULL                                 |
| Age           | age           | models.CharField    | max_length=254, help_text="Age when rescued"                                            |
| Rescued       | rescued       | models.DateField    | null=True, blank=True                                                                   |
| Description   | description   | models.CharField    | max_length=254, help_text="Physical Description", null=True blank=True                  |
| Profile       | profile       | RichTextField       | null=True, blank=True                                                                   |
| Neutered      | neutered      | models.BooleanField | null=True, blank=True                                                                   |
| Microchipped  | microchipped  | models.BooleanField | null=True, blank=True                                                                   |
| Vaccinated    | vaccinated    | models.BooleanField | null=True, blank=True                                                                   |
| Adopted       | adopted       | models.BooleanField | null=True, blank=True                                                                   |
| Resident      | resident      | models.BooleanField | null=True, blank=True                                                                   |
| Tagline       | tagline       | models.CharField    | max_length=254, help_text="One line character description...", null=True, blank=True    |
| Health_checked| health_checked| models.BooleanField | null=True, blank=True                                                                   |
| Image url     | image_url     | models.URLField     | max_length=1024, null=True, blank=True                                                  |
| Image         | image         | models.ImageField   | null=True, blank=True                                                                   |

#### Notice model

| Name          | Database Key  | Field Type            | Validation                             |
| ------------- | ------------- | --------------------- | -------------------------------------- |
| Notice        | notice        | models.TextField      | null=True, blank=True                  |

### Checkout app

#### Order model

| Name                     | Database Key    | Field Type           | Validation                                                                          |
| ------------------------ | --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| Order number             | order_number    | models.CharField     | max_length=32, null=False, editable=False                                           |
| User profile             | user_profile    | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True,related_name='orders' |
| Full name                | full_name       | models.CharField     | max_length=50, null=False, blank=False                                              |
| Email                    | email           | models.EmailField    | max_length=254, null=False, blank=False                                             |
| Phone number             | phone_number    | models.CharField     | max_length=20, null=False, blank=False                                              |
| Country                  | country         | CountryField         | blank_label='Country *', null=False, blank=False                                    |
| Postcode                 | postcode        | models.CharField     | max_length=20, null=True, blank=True                                                |
| Town or city             | town_or_city    | models.CharField     | max_length=40, null=False, blank=False                                              |
| Street address1          | street_address1 | models.CharField     | max_length=80, null=False, blank=False                                              |
| Street address2          | street_address2 | models.CharField     | max_length=80, null=False, blank=False                                              |
| County                   | county          | models.CharField     | max_length=80, null=True, blank=True                                                |
| Date                     | date            | models.DateTimeField | auto_now_add=True                                                                   |
| Delivery cost            | delivery_cost   | models.DecimalField  | max_digits=6, decimal_places=2, null=False, default=0                               |
| Order total              | order_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Grand total              | grand_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Original Bag             | original_bag    | models.TextField     | null=False, blank=False, default=''                                                 |
| Stripe pid               | stripe_pid      | models.CharField     | max_length=254, null=False, blank=False, default=''                                 |

#### Order Line Item model

| Name            | Database Key   | Field Type          | Validation                                                                         |
| --------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Order           | order          | models.ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | models.ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size    | product_size   | models.CharField    | max_length=2, null=True, blank=True                                                |
| Quantity        | quantity       | models.IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            |

### Contact app

#### EmailContacts model

| Name      | Database Key  | Field Type        | Validation                            |
| --------- | ------------- | ----------------- | ------------------------------------- |
| Directory | directory     | models.CharField  | max_length=254                        |
| Email     | Email         | models.CharField  | max_length=254                        |

#### Notice model

| Name          | Database Key  | Field Type            | Validation                             |
| ------------- | ------------- | --------------------- | -------------------------------------- |
| Notice        | notice        | models.TextField      | null=True, blank=True                  |

### Help app

#### Volunteer model

| Name          | Database Key  | Field Type        | Validation                            |
| ------------- | ------------- | ----------------- | ------------------------------------- |
| Role          | role          | models.CharField  | max_length=254                        |
| Description   | description   | RichTextField     | null=True, blank=True                 |
| Image url     | image_url     | models.URLField   | max_length=1024, null=True, blank=True|
| Image         | image         | models.ImageField | null=True, blank=True                 |

#### Donations model

| Name              | Database Key      | Field Type        | Validation            |
| ----------------- | ----------------- | ----------------- | --------------------- |
| Donation Option   | donation_option   | models.CharField  | max_length=254        |
| Description       | description       | RichTextField     | null=True, blank=True |

#### Notice model

| Name          | Database Key  | Field Type            | Validation                             |
| ------------- | ------------- | --------------------- | -------------------------------------- |
| Notice        | notice        | models.TextField      | null=True, blank=True                  |

### Home app

#### Drink model

| Name          | Database Key  | Field Type            | Validation                            |
| ------------- | ------------- | --------------------- | ------------------------------------- |
| Name          | name          | models.CharField      | max_length=254                        |
| Price         | price         | models.DecimalField   | max_digits=6, decimal_places=2        |
| Category      | category      | models.CharField      | max_length=254, null=True, blank=True |

#### Food model

| Name          | Database Key  | Field Type            | Validation                            |
| ------------- | ------------- | --------------------- | ------------------------------------- |
| Name          | name          | models.CharField      | max_length=254                        |
| Price         | price         | models.DecimalField   | max_digits=6, decimal_places=2        |
| Category      | category      | models.CharField      | max_length=254, null=True, blank=True |
| Description   | description   | RichTextField         | null=True, blank=True                 |

#### Treats model

| Name          | Database Key  | Field Type            | Validation                            |
| ------------- | ------------- | --------------------- | ------------------------------------- |
| Name          | name          | models.CharField      | max_length=254                        |
| Price         | price         | models.DecimalField   | max_digits=6, decimal_places=2        |
| Category      | category      | models.CharField      | max_length=254, null=True, blank=True |
| Description   | description   | RichTextField         | null=True, blank=True                 |

#### Notice model

| Name          | Database Key  | Field Type            | Validation                             |
| ------------- | ------------- | --------------------- | -------------------------------------- |
| Notice        | notice        | models.TextField      | null=True, blank=True                  |

### Products app

#### Category model

| Name          | Database Key  | Field Type        | Validation                             |
| ------------- | ------------- | ----------------- | -------------------------------------- |
| Name          | name          | models.CharField  | max_length=254                         |
| Friendly name | friendly_name | models.CharField  | max_length=254, null=True, blank=True  |

#### Product model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Category    | category     | models.ForeignKey   | 'Category', default='', blank=True, on_delete=models.SET_NULL |
| Sku         | sku          | models.CharField    | max_length=254, null=True, blank=True                         |
| Name        | name         | models.CharField    | max_length=254                                                |
| Description | description  | models.TextField    |                                                               |
| Has sizes   | has_sizes    | models.BooleanField | default=False, null=True, blank=True                          |
| Price       | price        | models.DecimalField | max_digits=6, decimal_places=2                                |
| Rating      | rating       | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True         |
| Image url   | image_url    | models.URLField     | max_length=1024, null=True, blank=True                        |
| Image       | image        | models.ImageField   | null=True, blank=True                                         |

#### Notice model

| Name          | Database Key  | Field Type            | Validation                             |
| ------------- | ------------- | --------------------- | -------------------------------------- |
| Notice        | notice        | models.TextField      | null=True, blank=True                  |

### Profiles app

#### UserProfile model

| Name             | Database Key           | Field Type           | Validation                                          |
| ---------------- | ---------------------- | -------------------- | --------------------------------------------------- |
| User             | user                   | OneToOneField 'User' | on_delete=models.CASCADE                            |
| Phone Number     | default_phone_number   | models.CharField     | max_length=20, default='', blank=True               |
| Street Address 1 | default_street_address1| models.CharField     | max_length=80, default='', blank=True               |
| Street Address 2 | default_street_address2| models.CharField     | max_length=80, default='', blank=True               |
| Town or City     | default_town_or_city   | models.CharField     | max_length=40, default='', blank=True               |
| County           | default_county         | models.CharField     | max_length=80, default='', blank=True               |
| Postcode         | default_postcode       | models.CharField     | max_length=20, default='', blank=True               |
| Country          | default_country        | models.CharField     | blank_label='Select Country', null=True, blank=True |


# Deployment

1. This repository may be cloned directly into an editor by pasting the following command into the terminal:   
`git clone https://github.com/Sean-Mc-Mahon/inner-purr`    
Alternatively, you can save a copy of this repository by clicking the green button "Clone or download" , then "Download Zip" button, and after extract the Zip file to your folder.
2. In the terminal window change directory (CD) to the correct file location (directory that you have just created).
3. Set up environment variables:
    - Create **.env** file in the root directory.
    - On the top of the file add `import os` to set the environment variables in the operating system.
    - Set the connection to your MongoDB database(MONGO_URI) and a SECRET_KEY with the following syntax:
    `os.environ["SECRET_KEY"] = "YourSecretKey"`   
    `os.environ["MONGO_URI"] = "YourMongoURI"`  
    .
4. Install all requirements from the **requirements.txt** file putting this command into your terminal:   
`pip3 install -r requirements.txt`  
*Note: GitPod does not require `sudo`, so if you use another IDE, you will need to include `sudo` in the beginning of the command: `sudo pip3 install -r requirements.txt`.*

7. You will now be able to run the application using the following command `python3 run.py`. 

### Heroku Deployment
To deploy the project to [Heroku](https://heroku.com/) the following steps need to be completed:
1. Create a **requirement.txt** file, which contains a list of the dependencies, using the following command in the terminal:  
`pip3 freeze > requirements.txt`
2. Create a **Procfile**, in order to tell Heroku how to run the project, using the following command in the terminal:   
`echo web: python run.py > Procfile`
3. `git add`, `git commit` and `git push` these files to GitHub repository
4. Create a **new app** in Heroku, assigning a name (must be unique) and set a region (for my project I set Europe)
5. From the Heroku dashboard link the new Heroku app to your GitHub repository:    
    - "Deploy" -> "Deployment method" -> "GitHub"
    - then "Enable automatic deployment"
6. To start the web process, put the following command into the terminal: `heroku ps:scale web=1` to scale dynos
7. In the **Settings** tab of the new Heroku app, click on "Reveal Config Vars" and set the following config vars:
    - **IP** : 0.0.0.0
    - **PORT** : 8080
    - **MONGO_URI** : `<link to your MongoDB database>`
    - **SECRET_KEY** : `<your secret key>`
    - **DEBUG**: **FALSE**  
*Note: your MONGO_URI and SECRET_KEY must match the ones you entered in .env.py file*

8. The app will be deployed and ready to run. Click "Open App" to view the app.   

**Note**: if you have not linked GitHub and Heroku following step **5**, alternatively as the last step of deployment, you can put the following command into your terminal:   
 `heroku login`, after a successful log in `git push heroku master` - to push the app to Heroku, and finally click "Open App" in Heroku dashboard to view the app.

---

# Credits

### Content

1.  Google Fonts for font styles; https://fonts.google.com/

2.  Youtube; Various resources for Materialize taken from [The Net Ninja](https://www.youtube.com/playlist?list=PL4cUxeGkcC9gGrbtvASEZSlFEYBnPkmff)

3.  Github; Format of README modified from [AJGreaves](https://github.com/AJGreaves/thehouseofmouse)

4.  Button icons sourced from [Fontawesome](https://fontawesome.com/)

 

### Acknowledgements

1.  My mentor Adegbenga Adeye for his support and input.

2.  My peers on slack for their generosity in sharing their knowledge and experience.

---

This project is for educational use only

##### back to [top](#table-of-contents)