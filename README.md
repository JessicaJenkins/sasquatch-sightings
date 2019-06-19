# Seeking Sasquatch

## Summary

Deployed at: www.seeking-sasquatch.com

**Seeking Sasquatch** is a web app that displays an interactive map of recorded bigfoot sightings previously submitted to the BFRO (Bigfoot Field Research Organization). Each marker contains the date the sighting took place, and a link to a full description of the event as recorded by the eye witness. 

Those lucky enough to site the elusive Bigfoot can create an account to record the location, description, and an image they took documenting their own experience.

## About the Developer

Jessica Jenkins (they/them) is an artist and software engineer based in the Bay Area. You can learn more about them on [LinkedIn](https://www.linkedin.com/in/jessicarjenkins/)

## Technologies

Python, Flask, SQLAlchemy, Jinja2, JavaScript, JQuery, AJAX, JSON, HTML, CSS, Bootstrap

**APIs used:** Google Maps, Cloudinary

## Features

**The home page gives users the ability to navigate to sign up, or view the map without an account.**
![alt text](https://github.com/JessicaJenkins/sasquatch-sightings/blob/master/static/images/homepage.png "Seeking Sasquatch home page")
<br /><br />

**The interactive map displays markers placed at the location of each recorded sighting that included geolocation data.**
![alt text](https://github.com/JessicaJenkins/sasquatch-sightings/blob/master/static/images/map.png "Seeking Sasquatch map page")
<br /><br />

**Clicking on a map icon shows a default image if none are associated with the event, the event date, and a link to view written details.**
![alt text](https://github.com/JessicaJenkins/sasquatch-sightings/blob/master/static/images/marker.png "Seeking Sasquatch map marker expanded")
<br /><br />

**Pages containing the description also included a static map, with a marker placed at the exact location.**
![alt text](https://github.com/JessicaJenkins/sasquatch-sightings/blob/master/static/images/description.png "Seeking Sasquatch event description")
<br /><br />

**Users can sign up for an account to submit their own experience through the 'Record a sighting' page, where they can add the event location, description and upload an image if they captured one.**
![alt text](https://github.com/JessicaJenkins/sasquatch-sightings/blob/master/static/images/record-sighting.png "Seeking Sasquatch home page")
<br /><br />

## For Version 2.0
1. A profile page that gives users the ability to view their submitted sightings in list form, and manage their presence.

2. Could be pie-in-the-sky, but there's a strong community of believers, and I'd like to support that through the implementation of a forum or chat feature. 