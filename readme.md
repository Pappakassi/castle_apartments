# Castle Apartments

A real estate listing web application built with Django for the final project in the "Verklegt námskeið II" course.

## Project Overview

Castle Apartments is a platform for listing, browsing, and managing apartment listings and purchase offers. The application includes user roles for buyers and sellers, and supports multi-step offer finalization, filtering, and user interaction features.

## Extra Features Implemented

In addition to the base project requirements, we implemented the following extra features:

- **Create New Apartment**: Logged-in sellers can create apartment listings through a dedicated form.
- **Edit and Delete Apartments**: Available on the front-end for users with admin privilages.
- **Offer Filtering and Search**: The offers list supports filtering by status, keywords, and sorting.
- **Favorite Button**: Buyers can favorite apartments and toggle this from the apartment detail page.
- **Sellers List Page**: A public list of all sellers with links to their individual profiles.
- **Seller Profile Page**: Each seller has a profile with information, bio, and a list of their properties.
- **Search and Filtering on Apartments**: The apartment list page supports filtering by street, postal code, type, price, and order.
- **Search and Filtering on Offers**: The offers list page supports filtering by a few options.
- **Home Page Displays 3 properties**: When entering the home page there are three apartments selected to work with the home page and shown at the bottom.
- **Home Page Apartment Slideshow**: The carousel slideshow shows these 3 apartments in a slideshow.
- **Apartment Detail Page Slideshow**: Slideshow for all images for individual apartments.
- **Selected CSS Styles Linked in Block**: For selected CSS features, some styles are linked in base.html and for styles in individual pages they are linked using {{bloack extra_css}}.



## Setup Instructions

Make sure to install the required packages:

asgiref==3.8.1
Django==4.2.20
pillow==11.2.1
psycopg-binary==3.2.8
psycopg2-binary==2.9.10
setuptools==80.3.1
sqlparse==0.5.3
typing_extensions==4.13.2
tzdata==2025.2
wheel==0.45.1

pip install -r requirements.txt
