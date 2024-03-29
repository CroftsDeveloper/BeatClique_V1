### Table of Contents

- [Project Overview](#project-overview)
- [UX](#ux)
  - [Strategy](#strategy)
    - [User Stories](#user-stories)
    - [Design Decisions](#design-decisions)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks & Libraries](#frameworks--libraries)
  - [Stripe-API](#stripe-api)
  - [Deployment](#deployment)
  - [Tools & Services](#tools--services)
  - [Development Tools](#development-tools)
- [Testing](#testing)
  - [Known Issues](#known-issues)
  - [Lighthouse Performance Checks](#lighthouse-performance-checks)
  - [Manual Testing](#manual-testing)
  - [Security Measures](#security-measures)
- [Future Development](#future-development)
- [Credits](#credits)
- [Contact](#contact)
- [Licence](#Licence)

# Project Overview

I am pleased to present BeatClique (MVP), a bespoke digital platform designed for a small, private group of UK music producers, of which I run. This project was created as the fourth and final project for my Code Institute course.

BeatClique seeks to transform the way our group distributes our unique sound kits and sample content. This platform aims to make it simple for vendors (chosen BeatClique members as SuperUsers) to manage their products, including adding new sound kits. The platform prioritises simplicity, freeing up more time for product creation instead of focusing on email and Dropbox sales.

BeatClique aims to provide a simple, hassle-free shopping experience for customers. A seamless and customised experience is ensured by safe transactions made through Stripe (test mode) and immediate download access to sound kits that have been purchased. The user interface is simple and clear, emphasising our products without needless extras.

The website was designed with a simple but responsive layout, ensuring optimal viewing and interaction across various devices, including tablets, desktop computers, and mobile devices.

The [GitHub repository](https://github.com/CroftsDeveloper/BeatClique_V1) contains all the assets and source code for the website. [See the deployed BeatClique site here](https://beatclique-project-46280e8c4cc2.herokuapp.com/)

**Note to assessor:** If you want to test the vendor upload functionality on the site, you can use the mock files provided in the following Dropbox link: [Mock Files for Vendor Upload](https://www.dropbox.com/scl/fo/l0hzkss08zuz3x13qgu2h/h?rlkey=tuua0opc3yvlrie0tspo6hons&dl=0)

# UX

## Strategy

Here are the User Stories that I set out to meet and the outcome upon finalised MVP :

## User Stories

| User Stories | Fulfillment |
| ------------ | ----------- |
| **Music Producers (Users)** |  |
| Discover Sound Kits: "I want to explore a range of sound kits tailored to various music production needs, ensuring I discover unique sounds for my projects." | BeatClique presents a user-friendly interface for browsing available sound Kits. |
| Manage Account: "I want to create an account to purchase sound kits and track my purchase history." | Producers can create accounts on BeatClique and view any purchased content from their accounts. |
| Complete Secure Checkout: "I want to complete purchases using a trusted provider, like Stripe, ensuring the protection of my payment information." | Stripe's secure infrastructure has been implemented into my project (Test Mode). |
| Access Downloads: "I want to easily download my purchased sound kits directly from my account after completing a purchase, ensuring immediate access to my content." | Users can immediately download their sound kits from their accounts post-purchase |
| **BeatClique Member / Super User** |  |
| Secure Admin Access: "I want security measures in place to restrict access to administrative features, safeguarding the platform's integrity." | Security measures restrict administrative feature access, with Django's permissions and groups system ensuring only the authorised Super User has access. |
| Direct Sound Kit Upload: "I want to easily upload sound kits, including images and ZIP files, streamlining the process of adding new content." | Super Users can easily upload sound kits directly through the platform, simplifying the process of making new content avaliable to our audience. |
| Instant Upload Feedback: "I want immediate feedback upon successful addition or update of a sound kit." | Immediate feedback is provided upon successful addition or update of sound Kits. They become avaliable on the Vendor Dashboard with full CRUD capabilities. |
| Manage Listings: "I want to edit, and remove sound kits from the platform, ensuring our catalog remains relevant and up-to-date." | Super Users can edit and remove sound kits, ensuring the catalog remains current and relevant. The content will dynamically update accordingly. |
| Monitor Orders: "I want a dashboard that offers a quick overview of recent orders to check what is selling well." | A dashboard is build into the SuperUser view and offers Super Users a quick overview of recent orders, aiding in monitoring sales and product performance. This will be improved in future developments|

## Design Decisions

#### Wireframes

Below are the wireframes designed for BeatClique's key pages, illustrating the planned layout and user flow for both vendor and customer views.

#### Vendor Structure

| Page               | Wireframe Link       |
|--------------------|----------------------|
| Home               | [Wireframe](https://www.dropbox.com/scl/fi/txpq3bh12a3yk60bc5lml/1-Homepage.jpg?rlkey=q4xb4v19c6vvopy9zbemz974o&dl=0)            |
| Login              | [Wireframe](https://www.dropbox.com/scl/fi/gwfd8h5vhptubszn2q98e/2-Login.jpg?rlkey=to3r1nytfu6syfk5o1hsnjqmu&dl=0)            |
| Vendor Dashboard  | [Wireframe](https://www.dropbox.com/scl/fi/ielmcr5cwns0yl9jdqxip/3-Vendor-Dashboard.jpg?rlkey=ejm9nqkegrwzt8t18ce3ljg4p&dl=0)            |
| Account            | [Wireframe ](https://www.dropbox.com/scl/fi/4asrh0ufouw86dmhevnt2/4-Accounts.jpg?rlkey=r2kl6o22wpw5aktpog4zbcpml&dl=0)            |

#### Customer Structure

| Page                   | Wireframe Link |
|------------------------|----------------|
| Home                   | [Wireframe](https://www.dropbox.com/scl/fi/txpq3bh12a3yk60bc5lml/1-Homepage.jpg?rlkey=q4xb4v19c6vvopy9zbemz974o&dl=0) |
| Available Soundkits    | [Wireframe](https://www.dropbox.com/scl/fi/s3gyqkvlfmf2k8tie0zt4/Avaliable-Soundkit.jpg?rlkey=r9g45jjf82gvhy7tkn2t2hz1i&dl=0) |
| Detailed Soundkit View | [Wireframe](https://www.dropbox.com/scl/fi/4svrfeovvhf88ua8rsnuq/Detailed-Soundkit.jpg?rlkey=3jqqc22qtf3ws5mq46h7ip6b6&dl=0) |
| Registration           | [Wireframe](https://www.dropbox.com/scl/fi/scxpwdzpbuuetgxkmth8d/Register.jpg?rlkey=yo7ek2ywlevfl1fsfqoqt0fmm&dl=0) |
| Login                  | [Wireframe](https://www.dropbox.com/scl/fi/gwfd8h5vhptubszn2q98e/2-Login.jpg?rlkey=to3r1nytfu6syfk5o1hsnjqmu&dl=0) |
| Cart                   | [Wireframe](https://www.dropbox.com/scl/fi/hla4b5y6vx79va2avdmn8/Cart.jpg?rlkey=fty974n2j4fmfglvn9gtcyy9i&dl=0) |
| Purchase History       | [Wireframe](https://www.dropbox.com/scl/fi/5w7hk4s5nxvav2wqd4edt/Purchase-History.jpg?rlkey=wu2mr85kjlnbq8cb4aabjtdh0&dl=0) |


#### Scope

- **Skeleton**: The layout design prioritised simplicity and intuitive navigation, with a responsive design ensuring accessibility across various devices.
- **Structure**: Information architecture was planned to minimise clutter and user clicks required to reach desired content, with sound kits clearly presdented for easy browsing.

#### Accessibility and Usability

- **Accessible Navigation**: The platform was designed to be navigable for users with disabilities, adhering to WCAG guidelines for accessibility.
- **Mobile-First Approach**: Prioritising mobile user, the design offers a seamless experience on smaller screens without compromising functionality. I relied heavily on Boostrap for this.

#### Fonts and Colors

- **Fonts**:
  - *Primary Font*: Lato, chosen for its clarity and versatility, is used for body text and general information.
  - *Secondary Font*: Roboto, selected for headings and accents, added readability to titles and buttons.
- **Color Scheme**:
  - *Primary Colors*: A dark slate (#212529) for backgrounds creates a simple but professional and immersive environment, paired with white (#FFFFFF) for text to ensure high readability. Our logo is black background with a stand out white logo, so I have attempted to make the site have a simular feel.
  - *Accent Colors*: Blue (#007bff) is used for buttons and interactive elements to clearly signal action points to users, while green (#28a745) is employed for success messages or confirmations.

## Features and Functionalities

#### From the Perspective of a BeatClique member:

- To enable easy management of products for vendors (selected BeatClique members as SuperUsers), including the CRUD functionality for sound kits
- To facilitate direct purchases on the platform, ensuring a smooth transaction process for customers.

#### From the Perspective of Users:

- To browse the platform to see what products BeatClique has to offer
- To explore detailed product information for each sound kit, including price, description, and cover image.
- To register for an account on BeatClique and receive confirmation emails upon successful registration.
- To easily log in or log out from the platform.
- To have a convenient password recovery process in case of forgetfulness. (Will be implemented in future updates)
- To add chosen items to a cart, customising quantities where applicable.
- To complete purchases seamlessly within the cart feature via Stripe (Test Mode - Will be refined in future updates).
- To access personalised order history and download purchased files.

### Structure

#### Vendor Structure / Flow

| Page               | Description                                                                                                                                   | Link       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Home               | A vendor navigates to the homepage which consists of a hero section, carousel displaying sound kits, testimonial section, and FAQs section. | [View](https://www.dropbox.com/scl/fi/8mpwbdjrzxs65pplkp7qk/Logout-view.PNG?rlkey=21o5a3v789p3775a1bjesc8l2&dl=0)            |
| Login              | A vendor can use the navbar to navigate to login and login with a valid SuperUser username and password.                                      | [View](https://www.dropbox.com/scl/fi/j974kcih2msry6uph265o/Login.JPG?rlkey=qcqnfnul6351c3q5zxjr07quq&dl=0)            |
| Vendor Dashboard  | Once logged in, the vendor is taken to the vendor dashboard, where the sound kits CRUD functionality lives, along with a section for recent user purchases accessible via an accordion dropdown to save space | [View](https://www.dropbox.com/scl/fi/ea0fz601j6af1jav9hobj/Vendor-Dashbord.PNG?rlkey=bhivijze2z4883al26l3buvkj&dl=0)            |
| Account            | A vendor can navigate to the account icon in the navbar where they can log out after completing the necessary actions                          | [View](https://www.dropbox.com/scl/fi/i69wgtdwf5iq8k4ro14v7/Account.JPG?rlkey=4620jpe4jc5joeg0zows9m8zm&dl=0)            |

#### Customer Structure / Flow

| Page                   | Description                                                                                                                                   | Link |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------|
| Home                   | A customer navigates to the homepage which consists of a hero section, carousel displaying sound kits, testimonial section, and FAQs section. They do not need to be logged in to view our products.  | [View](https://www.dropbox.com/scl/fi/8mpwbdjrzxs65pplkp7qk/Logout-view.PNG?rlkey=21o5a3v789p3775a1bjesc8l2&dl=0) |
| Available Soundkits    | Customers can click the 'Explore Soundkits' button to be taken to a list of available products. They have the option of choosing more info or adding to cart | [View](https://www.dropbox.com/scl/fi/p5awwli7e5yod7q8aeia0/Soundkit-view-logged-in.PNG?rlkey=yskdt4aqfjwplg916ecf7uv0q&dl=0) |
| Detailed Soundkit View | If they choose to see more information, they will be taken to a detailed view of the chosen soundkit. They have the option of clicking 'more soundkits' to return to the available soundkits, or adding a soundkit to cart, which will prompt them to login | [View](https://www.dropbox.com/scl/fi/4hr6kqh4bkjheets4jdi4/Soundkit-detailed-view-logged-in.PNG?rlkey=ur8xi9sa5s0zqvxuv6r9qyg2f&dl=0) |
| Registration           | If customers are not registered users, they can navigate to registration to register by following the visual prompt                                                      | [View](https://www.dropbox.com/scl/fi/oqrzhxhci47dta9shyxkn/Registration-Successful.PNG?rlkey=6kmf6k6l9hxpbxdhrd9qligz5&dl=0) & [Email Confirmation](https://www.dropbox.com/scl/fi/jn8spj4sg3r6iq0zcz5l8/Registration-Email-Confirmation.PNG?rlkey=3j7aynfk9p6fprdc8tfsodm8j&dl=0) |
| Login                  | If they are already registered users, they can log in to their accounts account                                                                                                  | [View](https://www.dropbox.com/scl/fi/j974kcih2msry6uph265o/Login.JPG?rlkey=qcqnfnul6351c3q5zxjr07quq&dl=0) |
| Cart                   | Once logged in, customers can browse the website again, choose their items, and navigate to the cart, where they can purchase via Stripe (test mode). | [View Cart](https://www.dropbox.com/scl/fi/mvy0gm1gyu9oowj5399h4/Cart-view.PNG?rlkey=b7uy0cz2fjnh5cegcu9ndazkh&dl=0) & [Stripe View](https://www.dropbox.com/scl/fi/8fne6ebu3iajeeqejm6lg/Stripe-view.PNG?rlkey=p7oeawz0tdqi1k4ek1t15owzf&dl=0) & [Payment Successful](https://www.dropbox.com/scl/fi/0kqvpciwu029c19ze7eqj/Payment-successful.PNG?rlkey=4fq0fuekcmp19o90aww16jnrd&dl=0) & [Download View](https://www.dropbox.com/scl/fi/yhkg5dltf6r27qbjbels5/Download-view.PNG?rlkey=vw7pqlsl5x7732mxmi8jfv59f&dl=0) |
| Purchase History       | After purchasing an item, customers can navigate to their account and download the item through purchase history                                | [View](https://www.dropbox.com/scl/fi/3w74zv0sdl04t77c5pnv6/Payment-History.PNG?rlkey=7fsm2u643hpspfsbmixbuysy8&dl=0) |

#### Error Handling

To improve user experience, I have included custom error handling to BeatClique for 500 (Internal Server Error) and 404 (Page Not Found) responses.

**404 Not Found**

Users are informed that the page they are looking for cannot be found when they navigate to a nonexistent page and are shown a bespoke 404 error page. For convenience, there is a link on this page that takes them back to their home view.

***Implementation***:

The views.py file of the project defines the handler404 view function in order to enable custom 404 error handling.

The handler404 method generates a 404.html custom template to show the error message and offer alternatives for navigation.

**500 Error Handling**

Users are redirected to a bespoke 500 error page in the event of internal server failures, indicating a problem on our end. Like the 404 error page, it has a link that takes users back to their home view. 

***Implementation***:

To handle 500 errors in a custom way, I have create a handler500 view function in the views.py the beatclique_project app.

The error message and navigation options are displayed using a custom template (500.html) rendered by the handler500 function.

## Database Model

I have created a number of models in my Django project that provide the basis for the functionalities of the application, such as user accounts, vendor profiles, sound kits, payments, and carts. Every model is designed to complement the overall functioning of the application, providing an easy development interface. 

A detailed overview of each model used in the project can be seen below :

## `VendorProfile`

- **User**: Links to the Django user model, establishing a one-to-one relationship for authentication.
- **Profile Picture**: Stores a profile image for the vendor, with a default placeholder (although unused in final project but will be in future versions and has been kept in for this reason)
- **Bio**: Provides a space for vendors to introduce themselves (although unused in final project but will be in future versions and has been kept in for this reason)

## `SoundKit`

- **Name**: The name of the sound kit.
- **Description**: Detailed information about what the sound kit includes.
- **Price**: The price of the sound kit, with precision up to two decimal places.
- **Image**: An image representing the sound kit.
- **Zip File**: A ZIP file containing the sound kit, validated to ensure correct file format.

## `Order` and `OrderItem`

- **User**: Connects to the user who places the order.
- **Items**: Links to the sound kits being purchased through a many-to-many relationship.
- **Total**: The total price of the order.
- **Creation Date**: When the order was placed.
- **Payment Status**: Indicates whether the order has been paid for.

`OrderItem` specifies the quantity of each sound kit in the order, providing a link between `Order` and `SoundKit`.

## `Cart` and `CartItem`

- **User**: Establishes a one-to-one relationship with the user, ensuring a unique cart per user.
- **Creation Date**: Marks when the cart was created.

`CartItem` details the sound kits added to the cart, including their quantity, linking back to the `Cart`.

## `CustomUser`

- **Bio**: Optional field for user biography (although unused in final project but will be in future versions and has been kept in for this reason).
- **Email Verified**: Indicates whether the user's email address has been verified.
- **Groups and Permissions**: Enhances user role management through detailed access control.

# Technologies Used

## Languages
- **Python 3.12**: Serves as the backbone for the Django-based application, handling back-end logic, data manipulation, and serving the Django application.
- **HTML5**: Structures the content of the web application, ensuring semantic markup for web pages.
- **CSS3**: Styles the presentation of the web application to enhance the user interface and user experience.
- **JavaScript**: Enhances interactivity within the web application, providing a dynamic user experience.

## Frameworks & Libraries
- **Django 4.2.4**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Stripe**: Integrated for secure online payment processing (although only test mode is functional and without Webhooks in this MVP).
- **Boto3**: Used for AWS S3 integration, handling file storage for static and media files.
- **Bootstrap**: A front-end framework used for developing responsive and mobile-first web pages.

# Stripe-api

BeatClique integrates a payments app, which manages customer payments with Stripe (Test Mode) to offer a secure and user-friendly payment solution. To integrate this I completed the following steps:

1. **Creating a Stripe Account:** To get started, I signed up for a Stripe account on [Stripe's website](https://stripe.com). This allowed me to access the necessary tools for integrating Stripe into BeatClique.

2. **Obtaining API Keys:** After setting up my account, I navigated to the Developers section in the Stripe Dashboard to obtain my API keys, including the Publishable Key and Secret Key. These keys are essential for securely connecting BeatClique with Stripe and are securely managed outside the codebase, ensuring confidentiality and safeguarding sensitive information. I securely stored the Stripe API keys as environment variables within my Django project settings (`settings.py`). Here's how it's configured:

    ```python
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    ```

## Creating a Checkout Session

BeatClique initiates a checkout session for users when they proceed to purchase sound kits from their cart. The process involves creating line items for each cart item and then creating a Stripe Checkout Session.

This is handled in the `create_checkout_session` view function in my payments app, where we specify the payment method types, line items (including the sound kit names and prices), and the URLs to redirect to upon success or cancellation. During this process:

- **Payment Method Types**: BeatClique specifies that the accepted payment method is a credit or debit card (although Stripe is only set up via test mode currently).
- **Line Items**: Each sound kit in the user's cart is added as a line item, including details like the name and price of the sound kit.
- **Mode**: The mode is set to 'payment', indicating that this checkout session is intended for processing a payment.
- **Payment Success Handling (`payment_success`)**: Post-successful payment, BeatClique creates an order, sends a confirmation email, and clears the user's cart for future purchases. Users are redirected to a specific URL that confirms the successful transaction, which has been created as a HTML template called payment_success.HTML
- **Cancellation Management (`payment_cancelled`)**: In case of payment failure or cancellation, users are redirected to a different URL, which has been created as a HTML template called payment_cancelled.HTML
- **Order Tracking (`order_history`)**: Users can track their order history, including essential details like order ID, total amount, and purchase date.
- **File Downloads (`download_product_file`)**: This feature securely redirects users to an AWS S3 URL to download purchased product files, if available.

This functionality ensures a trusted user-friendly payment experience on BeatClique, from checkout initiation to product access. Note that I have not integrated webhooks due to time constraints, however, I was advised by CodeInstitute staff that these are not required for this specific project. I will integrate them into future developments.

### Payment Testing with Stripe

To ensure the reliability of BeatClique's payment processing, comprehensive testing was conducted using Stripe's test card details. This was achieved through the creation of multiple mock user accounts via [TempMail](https://temp-mail.org/en/), simulating a variety of transaction scenarios to thoroughly test the application's payment handling capabilities. 

The key details used for Stripe's test transactions are as follows:

- **Card Number:** `4242 4242 4242 4242`
- **Expiry Date:** Any future date
- **CVC:** Any 3 digits

#### Key Test Outcomes:

- **Transaction Cancellation:** Users who exit the transaction process are redirected to a [Payment Cancelled](https://www.dropbox.com/scl/fi/lqtbwd89sdua8a9htnxdi/Payment-Cancelled.JPG?rlkey=wn6plyv7nqvcjgz6r4edzxtls&dl=0) page, ensuring a clear communication of the transaction status.
- **Successful Payment Confirmation:** A visual confirmation of a successful payment is available [here](https://www.dropbox.com/scl/fi/0kqvpciwu029c19ze7eqj/Payment-successful.PNG?rlkey=4fq0fuekcmp19o90aww16jnrd&dl=0), showcasing the user-friendly feedback provided upon completing a purchase.
- **Stripe Dashboard Update:** The Stripe [Dashboard](https://www.dropbox.com/scl/fi/ysrzn8kll10cu6u5nyfao/Stripe-Dashboard.JPG?rlkey=hxlwx2bu1ayrbb1iu0gd0snk8&dl=0) reflects the accepted payment, demonstrating the backend functionality and record-keeping accuracy.
- **Email Confirmation:** Following a purchase, a confirmation email is sent to the user, with an example viewable [here](https://www.dropbox.com/scl/fi/gte0ru8dghb4aox6x12qh/Confirmation-Email.JPG?rlkey=p1p0jwdqjojf10egcsdrj8wuo&dl=0), reinforcing the system's reliability and enhancing user experience.
- **Order History Access:** Users can access their order history within their [Account](https://www.dropbox.com/scl/fi/x9w0tixsx48dl2nwdznsz/Updated-Order-Historyu.JPG?rlkey=fd70p6zh39hta7wokf2wtt4vn&dl=0), providing a transparent and convenient overview of past transactions.

# Deployment

## General guide

### Prerequisites
- GitHub account
- Heroku account
- AWS account with S3 access
- Local development environment with Python and pip installed

### Step 1: Clone the Repository
Clone the BeatClique project [Repository](https://github.com/CroftsDeveloper/BeatClique_V1.git) from GitHub to your local machine. Use the Git command:

```python
git clone https://github.com/CroftsDeveloper/BeatClique_V1.git
cd BeatClique_V1
```
Step 2: Virtual Environment
Create and activate a virtual environment to isolate project dependencies:

```python
python -m venv venv
source venv/bin/activate or `venv\Scripts\activate`
```

Step 3: Install Dependencies
Install the project dependencies from requirements.txt:

```python
pip install -r requirements.txt
```

Step 4: Environment Variables
Set up necessary environment variables. Create a .env file (and add it to .gitignore) in the project root with your  keys:

```python
DEBUG=False
DJANGO_SECRET_KEY='your_django_secret_key'
DATABASE_URL='your_database_url'
AWS_ACCESS_KEY_ID='your_aws_access_key'
AWS_SECRET_ACCESS_KEY='your_aws_secret_access_key'
AWS_STORAGE_BUCKET_NAME='your_s3_bucket_name'
AWS_S3_REGION_NAME='your_s3_region'
STRIPE_PUBLIC_KEY='your_stripe_public_key'
STRIPE_SECRET_KEY='your_stripe_secret_key'
EMAIL_HOST='your_email_host'
EMAIL_PORT=your_email_port
EMAIL_HOST_USER='your_email_username'
EMAIL_HOST_PASSWORD='your_email_password'
EMAIL_USE_TLS=True or False
```
Step 5: Run migrations to initialise your database schema:

```python
python manage.py migrate
```
Step 6: Collect static files into a single directory for deployment (This command prepares your static files for uploading to AWS S3):

```python
python manage.py collectstatic
```
Step 7: Log in to Heroku and create a new app. Install the Heroku CLI and log in through your terminal:

```python
heroku login
heroku create chosen_app_name
```
Step 8: Set up Heroku to use your .env variables (ensuring no sensitive data is committed to your repository):

```python
heroku config:set DEBUG=False
```
Replace '...' with all other environment variables from your .env file

Step 9: Deploy your project to Heroku:

```python
git push heroku main
  ```

Step 10 : Once your dyno is up and running, you should be able to access your application through the URL provided by Heroku

### My Heroku journey

### Initial Steps:

**Preparing the Application:** Ensuring that BeatClique was deployment-ready involved checks of dependencies, settings, and local development environment functionality.

**Heroku CLI:** Using Heroku Command Line Interface, I established a new app on Heroku, assigning it a unique name aligned with the project.

**Configuration Variables:** To ensure security and functionality, I migrated all sensitive data and configuration specifics (such as DJANGO_SECRET_KEY, database credentials, and AWS keys) to Heroku's config vars. This safeguards sensitive information from exposure in the codebase, enhancing security measures. Prior to this it was held inside a .env file that was ignored by a .gitignore file.

**Database Migration:** Transitioning to a new database was facilitated by employing dj_database_url to dynamically configure database settings in settings.py, ensuring seamless switching between development and production environments. The database that I used for live production was provided via the CodeInstitute POSTGRESQL tool. I will not link it here for security reasons.

**Static and Media Files:** Configuring Django to utilise Amazon S3 for serving static and media files was important for scalability and reliability. By integrating django-storages and boto3, I linked BeatClique to an S3 bucket, efficiently managing static asset delivery. Configuring bucket policies and CORS settings ensured secure yet accessible file management. I also set up IAM Policies to refine access permissions further.

**Deployment:** With the application configured and prepped, deploying to Heroku was a process of pushing the codebase to the Heroku git remote. The automatic detection of the Procfile and requirements.txt file simplified dependency installation and application launch. I initially had issues deploying but this was rectified by fixing the text in the Procfile from web: gunicorn beatclique-project.wsgi to web: gunicorn beatclique_project.wsgi

## Tools & Services

- **Git**: Version control system for tracking changes in source code during development.
- **GitHub**: Hosts the code repository and provides tools for project management.
- **Heroku**: Cloud platform used to deploy and run the application.
- **AWS S3**: Cloud storage service used for storing static and media files, ensuring they are accessible over the Internet.
- **PostgreSQL**: Used as the database for development, storing application data.

## Development Tools
- **Visual Studio Code**: My development environment (IDE) for writing and editing code.

# Manual Testing

- **Browsers Tested**: Chrome, Firefox, and Safari.
- **Devices Tested**: Desktop (Windows and macOS), Tablet (iPad), and Mobile (iPhone and Android devices).

Throughout the development of BeatClique, I conducted a series of stress tests to evaluate the platform's resilience under demanding circumstances. Here are the scenarios tested and the outcomes observed:
| #  | Scenario | Result |
|----|----------|--------|
| 1  | **Button Rapid Clicks**: I tested the durability of buttons, especially the homepage's "Explore Soundkits" button as this will likely be the most clicked, by rapidly clicking it multiple times. | The application efficiently queued requests, maintaining stability without crashes. I also asked my girlfriend and colleagues to do the same and they confirmed that the functionality worked as expected |
| 2  | **Repeated Cart Modifications**: I tested the cart's robustness by repeatedly adding and removing items and adjusting quantities. | Cart was not responding correctly so I decided to remove the automatic up and down arrows for the MVP and left it so the user would need to manually update. After this, updates were processed accurately, reflecting changes as expected in the UI. Note that I will improve this feature in future updates. |
| 3  | **Backing Out Of Cart**: I tested exiting out of the transaction process to ensure that it was handled correctly. | Payment transactions were stopped and I was automatically navigated to the correct HTML page. |
| 4  | **Rapid Navigation Through Pages**: Assessed the website's responsiveness by quickly navigating through various pages, including sound kit listings, detailed views, and user account sections. | Pages loaded without significant delays or errors. |
| 5  | **Mobile View**: I visited the site on my mobile, as well as my partner's mobile and checked each page to ensure responsiveness. I also viewed the site with multiple browsers' mobile views using Developer Tools. | Site performed well and was responsive throughout. This is largely due to the implemented Bootstrap throughout. |
| 6  | **Registration Process**: Tested the registration form using both valid and invalid data to ensure correct validation and feedback messages. | Confirmed that users could log in successfully after registering. |
| 7  | **Login Functionality**: Attempted login with both correct and incorrect credentials to verify forms and access and checked logout functionality to ensure proper sign-out. | Refreshed page to ensure I was not automatically signed back in. |
| 8  | **Sound Kit Listing**: Verified that all available sound kits were displayed correctly on the listing page and tested responsiveness across different screen sizes. | Listings worked well across different screen sizes as expected. |
| 9  | **Sound Kit Detail Page**: Accessed individual sound kit pages to ensure accurate display of information. | Information was displayed accurately. |
| 10 | **Adding Items to Cart**: Added various sound kits to the cart to confirm correct item and quantity display. Tested updating quantities and removing items to ensure accuracy. | Functionality worked as expected. |
| 11 | **Sound Kit Management**: Logged in as a SuperUser to access the vendor dashboard. Conducted CRUD operations on sound kits to ensure proper administrative functionality. | Login and CRUD functionality worked as expected. Account page highlights that user is a SuperUser. |
| 12 | **Order History and Downloads**: Reviewed recent orders as a SuperUser to confirm accurate sales data display. | Recent orders are updated as they are made, indicating that the process is working as intended. |
| 13 | **Navigation / Accessibility**: Utilised keyboard navigation and screen readers to assess accessibility features. | I was able to navigate through the page effectively. |

### Results and Adjustments

The manual testing process uncovered an expected level of functionality and user satisfaction across the platform. There were some issues with button placements on various devices, which were promptly addressed and fixed in subsequent commtis.

### Known Issues

- Email Delivery : Occasionally, verification emails may be delayed or filtered into spam folders, impacting new user registrations.

- Identified Chrome Safety Alert : Users may encounter a safety alert in Google Chrome when attempting to log-in to the BeatClique platform, which could potentially deter them from proceeding. [View the Dangerous-page Chrome safety alert here](https://www.dropbox.com/scl/fi/ltmgr4b9x1tgy4itrmk7h/Dangerous-page.JPG?rlkey=fa65vs0wva9bas5i2ehdtdkjw&dl=0) .However, this issue hasn't been observed in other browsers such as Firefox and Edge. I have carried out investigation using Chrome Developer Tools' Security tab, it has been verified that the SSL certificate is valid and the connection to the site is [secure](https://www.dropbox.com/scl/fi/1yeq1vaeyps1uzztr641o/Security.JPG?rlkey=lzeng9cq1h54x97jiglcia5qx&dl=0). Additionally, all resources are served securely over HTTPS without any mixed content issues. While the platform functions securely, the concern appears to be specific to Chrome's security checks. I have been trying to find a fix for this, however, I cannot seem to resolve it for this MVP but it will be a focus on future development.

- Update Email: I had implemented a feature where a user could update their email to another address. However, it was not as intuitive as I would have liked it to be and felt redundant, so I removed it in commit `8106a7b`. This was done by deleting the AccountUpdateForm, account_update view, and account_update URL pattern, as well as removing the form for updating email from the account.html template. I will likely add this back in the future, but I don't think it's necessary for the MVP.

- Kindle Fire HDX Format : The 2nd testimonial on homepage does not format correctly in line with others when viewing from Kindle Fire HD view in developer tools, however, works fine on all other devices. I have decided not to fix this in this version in order not to impact the other views which would be more popular. I will look into this in future development. 

## Validation Reports

Ensuring compliance with web standards and best practices, BeatClique was put through validation for HTML, CSS, and JavaScript. Here are the results:

### HTML Validation (Normal User & Vendor Views)

HTML validation was performed using the [W3C Markup Validation Service](https://validator.w3.org/). Except for a design decision on the homepage, all pages passed validation without issues.

#### Normal User View
- **Homepage**: [View Report](https://www.dropbox.com/scl/fi/z8ook93okxufoxk2xro2c/1-Homepage.pdf?rlkey=xewjty5n91r9ggnyisld7y7ud&dl=0) - Note: Suggestion for adding a heading above the carousel was ignored due to design choice.
- **Register**: [View Report](https://www.dropbox.com/scl/fi/62qsrtaxofvr9is4c2ze1/2-Register.pdf?rlkey=hm7e7z5x32neegm7cxmcqoini&dl=0)
- **Login**: [View Report](https://www.dropbox.com/scl/fi/hgksnori8l6b9v28hgqkg/3-Login-No-issues.pdf?rlkey=dkrfa6l3fgqlxlop31h53whsg&dl=0)
- **Soundkit Detail**: [View Report](https://www.dropbox.com/scl/fi/gfpu7y2ahe2l8cy7c71lh/4-Soundkit-Detail.pdf?rlkey=3j3qzkvggseks3jcg0x2wjakt&dl=0)
- **Soundkit List**: [View Report](https://www.dropbox.com/scl/fi/y7z6ddod6h95kjo9d0mol/5-Soundkit-List.pdf?rlkey=whmw7xop9t53w7abfkobuzhk7&dl=0)
- **Cart**: [View Report](https://www.dropbox.com/scl/fi/zq4tx5ycrzqxfbuke1xnb/6-Cart.pdf?rlkey=uwtm1fm6kyp4vtn9dfkcx41f9&dl=0)
- **Account**: [View Report](https://www.dropbox.com/scl/fi/m4lxyujwo8b3c3gm0lejy/7-Account.pdf?rlkey=fk2e7lmb95fhhbszgfjec342v&dl=0)
- **Order History**: [View Report](https://www.dropbox.com/scl/fi/oqkj1hak12wa172o15yub/8-Order-History.pdf?rlkey=f33szcjyszj2s0jibpcna18ag&dl=0)

#### Vendor (SuperUser) View
- **Dashboard**: [View Report](https://www.dropbox.com/scl/fi/irb5p6q032130lyws8vcr/Vendor-Dashboard.pdf?rlkey=btvjhocp2z3qts06l4yw2qqh4&dl=0)
- **Add Soundkit**: [View Report](https://www.dropbox.com/scl/fi/30m6ctul6e9m2wctxxk7b/Add-Soundkit.pdf?rlkey=pvmie5f5i0i0f1gykrft5oebx&dl=0)
- **Edit Soundkit**: [View Report](https://www.dropbox.com/scl/fi/ykd4iyxdog6d8ef37b0dg/Edit-Soundkit.pdf?rlkey=jpbwv90zzdr293zt06qtj54d6&dl=0)
- **Delete Soundkit**: [View Report](https://www.dropbox.com/scl/fi/6mbk9jtr8vll6bmukpof5/Delete-Soundkit.pdf?rlkey=lf8beg5w80ydxi8108v6rezvw&dl=0)
- **Vendor Account**: [View Report](https://www.dropbox.com/scl/fi/gsw7w0zyh8qjnpyyqghiq/Vendor-Account-Validator-Ignored.pdf?rlkey=j7103ly6filb7r7l6lxqady10&dl=0) - Note: Minor notice ignored for design choice.

### CSS Validation

CSS validation was performed using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/). The main stylesheet passed validation after minor adjustments.

- **Main Styles**: [View Report](https://www.dropbox.com/scl/fi/uircsz52num1sj37t1geq/Main-styles.pdf?rlkey=3b2lolrbtt6f9gwuegnl1kn1l&dl=0) - Fixed with commit `cfa7d38`.

### JavaScript Validation

JavaScript validation was conducted using [JSHint](https://jshint.com/). The main script passed validation after adjustments.

- **Main Scripts**: [View Report](https://www.dropbox.com/scl/fi/u9szyqpyyb5ujzocqp0ka/Main-Scripts.pdf?rlkey=del5x2py0e8f8f9u7vdff5z0w&dl=0) - Fixed with commit `15de603`.

## Lighthouse Performance Checks

In the context of BeatClique, Lighthouse was used to assess the performance and user experience of various pages from both the perspective of a normal user and a vendor (SuperUser). The following links provide access to screenshots of the Lighthouse checks conducted on different views of the platform.

The majority of the scores were 95+, however, the Soundkits View was at 76 on performance. This is something that I would look to address in future development.

### Normal User (Shopper) Lighthouse Checks

- **Register View**: [View Results](https://www.dropbox.com/scl/fi/y4c8mbks7hwfd7i9favk2/1-Register.png?rlkey=7c30zpkou5b4vn15t2zdxuxb9&dl=0)
- **Login View**: [View Results](https://www.dropbox.com/scl/fi/o7stwe9l85e3i9za3t44i/2-Login.png?rlkey=5bojzldzyt1neh1uu9ghs0keq&dl=0)
- **Home View**: [View Results](https://www.dropbox.com/scl/fi/d8ooa54uks8sulzs8ars9/3-Home.png?rlkey=r8uflti1mk7k1liin7ch9u7ew&dl=0)
- **Soundkits View**: [View Results](https://www.dropbox.com/scl/fi/1luev0ra5hjgq1pyu1oy8/4-Soundkits.png?rlkey=kkpiu6f34wkhl00y6bxbnwolj&dl=0)
- **Soundkit Detail View**: [View Results](https://www.dropbox.com/scl/fi/hq0u1a8xb7hmt1jpuve7w/5-Soundkit-Detail.png?rlkey=zuhizqzynrcqgo5x7nq2olt2i&dl=0)
- **Cart View**: [View Results](https://www.dropbox.com/scl/fi/fumz55qngx4jwbk8ogw3i/6-Cart.png?rlkey=9oofhlsxqwulb0htk9gm2co21&dl=0)
- **Payment Successful View**: [View Results](https://www.dropbox.com/scl/fi/w5r8ef0sxr86kutpy4dmi/7-Payment-Successful.png?rlkey=astv73nafqzqlk59czyf16m32&dl=0)
- **Payment Cancelled View**: [View Results](https://www.dropbox.com/scl/fi/korkn7ofm3dq4b2jppjl1/8-Payment-Cancelled.png?rlkey=o6c28if9fip0t5ey82ew19qeb&dl=0)
- **Account View**: [View Results](https://www.dropbox.com/scl/fi/5xu4n90gq0srrt4322dus/9-Account.png?rlkey=7tb9cc62ong9l2n4zpsjj5kr4&dl=0)
- **Order History View**: [View Results](https://www.dropbox.com/scl/fi/pembtago3qar8uz9c7pb5/10-Order-History.png?rlkey=pv54x3ln5p28c8yb4j2o79xaj&dl=0)

### Vendor (SuperUser) Lighthouse Checks

- **Dashboard View**: [View Results](https://www.dropbox.com/scl/fi/926wnmlznan1jck7c5yh6/Dashboard.png?rlkey=9hsy0rhm3cnvr6wl2362fj5ub&dl=0)
- **Add Soundkit View**: [View Results](https://www.dropbox.com/scl/fi/zlna7fslmb4twea6h9ip5/Add-Soundkit.jpg?rlkey=n9t8t67icfsqeiwwq1ls0ztvf&dl=0)
- **Edit Soundkit View**: [View Results](https://www.dropbox.com/scl/fi/eycnf58uob28c35gm6a7u/Edit-Soundkit.jpg?rlkey=jp6totpxj74ytbao44gi18o1x&dl=0)
- **Delete Soundkit View**: [View Results](https://www.dropbox.com/scl/fi/mw9ltqsq4vjludq88tnja/Delete-Soundkit.jpg?rlkey=c13s0w5duipzpvqb6eg47gx6t&dl=0)
- **Vendor Account View**: [View Results](https://www.dropbox.com/scl/fi/ipb56uc7qpjl312j39gxa/Vendor-Account.jpg?rlkey=u1xxy9mwds883ftm62urir5wv&dl=0)

## Security Measures

The project incorporates several Django security best practices and configurations to protect against common vulnerabilities and threats:

- **HTTPS Enforcement**: By setting `SECURE_SSL_REDIRECT` to True, all requests are redirected to HTTPS, ensuring data transmitted between the client and server is encrypted.

- **Secure Cookies**: With `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` set to True, cookies are marked as "secure," meaning they are only sent over HTTPS connections. This reduces the risk of cookie theft via man-in-the-middle attacks.

- **Environment Variables for Sensitive Settings**: Sensitive settings like the `SECRET_KEY`, database credentials, and third-party service keys are stored in environment variables in Heroku. This prevents hard-coded credentials within the codebase and allows for secure configuration management.

- **Database Security**: The use of `dj_database_url` for database configuration with environment variables further secures database access credentials.

- **AWS S3 for Static and Media Files**: Integration with AWS S3 for static and media files storage provides scalability and also leverages AWS's security measures.

- **Stripe for Secure Payments**: - [Stripe's](https://stripe.com/docs/api) payment processing integration ensures secure handling of payment information. The project is currently set up in test mode, with plans to implement webhooks for enhanced security in future production.

# Future Development

The BeatClique platform, although functional in its MVP form, has significant potential for expansion and improvement in future iterations. Some key areas for future development include:

- **Password Recovery**: Introducing a password recovery mechanism to allow users to regain access to their accounts in case of forgotten passwords. This is the top of my list of development needs.
- **Enhanced User Experience**: Implementing additional features to enhance the platform's usability and engagement, such as user reviews and soundkit ratings.
- **Enhanced Vendor Tools**: Implement multiple vendor accounts, replacing SuperUser, as well as providing more tools and analytics to track sales, manage inventory, and optimise bundle offerings.
- **Expanded Payment Options**: Integrating additional payment gateways and methods to offer users more flexibility and convenience during checkout. Also revamping the whole Stripe implementation to use webhooks and live environments.

# Credits

- **Media Files**: All sound kits, images, and other media content used on the platform were sourced and created by me using photoshop from free resources. The soundkit covers were made a few years ago for BeatCliques brand products. Any images of musical artists used were purchased from [Producer Grind](https://producergrind.com/) Photshop FX packs and are royalty free.
- **Inspiration**: An inspiration for this platform was [The Producer Crate](https://theproducercrate.com/), although I found their site to be too complex hard to navigate. Seeing this helped me decide to slim down the features of BeatClique and focus on a simple UX/UI.
- **TempMail**: [TempMail](https://temp-mail.org/en/) is a disposable temporary email service which allowed me to create multiple emails to test my project without clogging up my personal emails
- **Readme.so**: [Readme.so](https://readme.so/) is simple online README.md editor that allowed to customise my projects readme conveniently online and see the visual outcome immediately. This gave a well needed break from VSCODE
- **Bootstrap**: [Official Documents](https://getbootstrap.com/docs/4.1/getting-started/introduction/) were reviewed at multiple points throughout this project and were essential for me to be able to finalise it.

# Contact

For any questions or feedback regarding the BeatClique project, please feel free to reach out to me at :

- **Name**: Samuel Crofts
- **Email**: samcrofts2020@gmail.com

Thank you for reviewing BeatClique!

# Licence

All Rights Reserved

- This project is the intellectual property of Samuel Crofts & BeatClique and made for the purpose of a project submission, and should not be reproduced, distributed, or modified without my explicit permission (outside of assessment marking)

