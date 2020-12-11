# Project - UrbanBeat

## Introduction
* this is a study project for Softuni course Python Web Framework - November 2020

## Functionalities:

* Anonymous users:
    * can see event list on home page (paginated by 12 events), search event by name, filter events by city and type, sort by date
    * can see event details about the event
    * sign up
    * sign in (redirected back to event detail page)
    * can see other users profiles 

* Logged in users
    * sign in and logout, change and reset password
    * edit the default profile
    * can create event
    * can like others events 
    * show interest in event or intention to go (one of them only) for others events
    * comment others event and reply to a comment (can't comment own event)

* Event hosts:
    * can edit and delete their own events
    * can not like, interested or go for own event
    * can't comment but can reply to comments

* Admin users:
    * 'Admins' role is assigned to an user from the admin by superuser
    * sign in and logout
    * can create, edit and delete their own events
    * can see a list of events, created bu all users 
    * can edit and delete event of all users
    * can edit their default profile
    * can see a list of all profiles
    * can view or edit all user's profiles
    * can't comment but can reply to comments
     
## External libraries, modules and resources used:

* customized Materialise CSS
* Cloudinary
* Google maps
* flatpickr for date input
* custom vanilla JS: same page position after page reload, hide/show reply to comment

## Design credit: 

[Behance - Kevin Wijaya](https://www.behance.net/gallery/87681559/Event-Landing-Page)