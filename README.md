# Final-Project

Web Programming with Python and JavaScript


# Introduction

This website is a Guitar Chords Website platform powered by Django. In this websie, users can search for songs arbitrarily or browse the latest songs in the home page.

For editors and artists, they can upload songs in a format of HTML.

This is the final project for CS50's Web Programming with Python and JavaScript.


#### Features

1. Search Song.
2. Get the full lyrics including chords of the song by clicking the song.
3. Like and unlike songs.
4. User's Profile.
5. Login and Register.
6. Author Songs Page to view all songs by that author.
7. Favourite Songs Page to view all the songs you have liked.

#### Files & Directories

- `Main Directory`

  - `guitar_website` - Contains settings and main url file.
  - `urls.py` - Contains all url paths for songs' views, home, admin site and all url paths for authentication, like login, sign up as well as logout.


  - `screenshot` - Contains all the screenshots of all pages of the website


  - `songs` - Main application directory
    - `static` - Holds all static files.
      -`songs`
        -`images` - Holds all static images and icons
          -`guitar.png` - favicon image.
        -`main.css` - Contains styles for all pages.
    - `templates` - Holds all html files.
    - `forms.py` - Contains two form classes `UserRegisterForm` and `ProfileForm` which has all the fields of the forms.
    - `models.py` - Contains two classes `Songs` and `Profile` which has all information about the songs and user.  
    - `views.py` - Contains all view functions for `home` to render the home page, `SongListView` to render all the songs with pagination by using Django's `Class-based Views` such as `SongDetailView` to open a detailed render with all the chords of the song,  `AuthorSongListView` to render all the songs by that author with pagination, `login` to render the login page, `register` to render the register page, `add_to_fav_songs` to add the song in favourite songs list, `Fav_songs` to render all the users' favourite songs, `Profile` to render users' profile, as well as `about`.  

    
  - `requirements.txt` - Project dependencies.



# Project Structure

## Home Page

In the home page, you can search text in any part of songs by inputting any words in the search box, and click "Search" button. 

Besides, if you just want the chords to something new, just click "Songs" Button and you will get some songs randomly. Additionally, you don't need to log in for those actions.

![main page](/screenshot/home.png) 

## Result Page

In the result page, you can get songs with title and its author. If you aren't satisfied with those results, you can continue to search in the top search bar.

If are are interested in some songs from the search result, you can click the title of the card, and you will be redirected to the full song detail page.

![Result page](/screenshot/search_results.png)

## Song Detail Page

In the song detail page, the detail of one song will be displayed, such as the title, author, and the most important part, the full lyrics and the chords. 

![song sample1](/screenshot/song_sample1.png)

Besides, if you are not logged in, it will also display a login prompt to the far right.

![song sample2](/screenshot/song_sample2.png)


## Author Songs Page

If a user likes songs of a specific author, the user can click the author's name to go to the `Author Songs Page` to view all the songs of that author.

![author songs page](/screenshot/author_songs_page.png)


## Login Page

Before you can like songs, you need to login to allow the platform to remember you. Just input the username and password in the form below.

![Login page](/screenshot/login.png)

Don't have an account? No worries, as there is a link to the register page in the `signup` button below the form where new users can get registered as well.



## Register Page 

New users can get registered by filling out the `UserRegisterForm` and then they will be redirected back to the login page when they can then login to start liking songs.

![register page](/screenshot/register.png)

 Users can now view their `profile`.



## Like Songs 

After logging in, users can now like songs so that they don't have to search that song every time.
A song can be liked by clicking the red `heart` icon on the top right of the song card.

![like songs](/screenshot/like.png)


## Favorite Songs Page

After liking songs the user can then go to `Favorite Songs` Page to view their favorite songs which is much quicker and easier than scrolling through all the songs or searching the song.

 ![fav songs](/screenshot/fav_song.png) 



## Pagination in Home Page and Liked Songs Page 

I have included pagination in home page,liked songs and author songs page by using Django's `Class-based Views`.

![pagination sample](/screenshot/pagination.png)


## Profile Page

The `Profile` Page allows users to see their liked songs.

![profile](/screenshot/profile.png)


## About Page

The  `About` Page contains information about the website like when was it created and some other stuff.

![about](/screenshot/about.png)


# Back End

## Super User

Super user is a feature provided by Django. The super user can manipulate all data in the Backend Management Dashboard.

![Admin](/screenshot/admin.png)

Super user can also view all the details of all users.

![Users](/screenshot/users.png)

## Songs

Admin is the person who can upload songs and has the authority and ability to add/change/delete/view songs in the backend dashboard.

![Songs](/screenshot/songs.png)


## Song_view

Song_view is one of the most important entities of the platform. Song_view has fields like title, lyrics, author, favorited_by, track_image.

![Add song](/screenshot/song_view.png)

And then, the song will be saved and become visitable.

![Added song](/screenshot/shape_of_you.png)




## Distinctiveness and Complexity

  This project is distinct from all previous projects so far. Why?

  - More models with complex relation between them.
  - Uses ajax functionality, fetch data without reloading the page.
  - Send password reset code using email.
  - Completely Mobile responsive.

## How to run the application
* Install project dependencies by running `pip install -r requirements.txt`
* Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.


# Finally

Thanks to all the people for making [CS50's Web Programming with Python and JavaScript](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript) for us. Especially, thanks to [Brain Yu](https://www.edx.org/bio/brian-yu)'s excellent lecture and his "great question", which motivated me to finish the course.

August 22, 2022
