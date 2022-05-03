# IDI Colorz
*Open Data Management &amp; the Cloud exam project*

Website is available @ http://idicolorz.it, https://idicolorz.herokuapp.com/

## Intro
**IDI Colorz** is a website dedicated to the most famous artists of the last millennium.   
In it, the user can read about all their paintings and drawings, with an insight on the color composition of each piece.  

The name of the project comes from the initials of its creators: **I**rene Ferfoglia, **D**aniele Irto, and **I**sacco Zinna.


## Artists
As of right now, the website contains the work of 6 artists:
* **Claude Monet**
* **Hilma af Klint**
* **Leonardo da Vinci**
* **Salvador Dalì**
* **Vincent Van Gogh**
* **William Blake**

For each one of them, the user can learn about the place of birth and death along with the dates. Moreover, a picture or self-portrait of the artist is provided, along with the *Wikipedia* link for futher reading. 

A clickable list can be found by following the **Artists** button on the sidebar.

## Pictures
There are two ways to access a picture: randomly or by search.

### Randomly
To access a picture randomly, it is as simple as clicking the **Random Picture** button on the sidebar. This will lead to the detail page of a random picture, so the user can discover new amazing pieces of art.

### By search
The other way to access a given picture is by using the search engine. By clicking the **Pictures** button, the user will be presented with a view of all the pictures in the database, organized first by year, then alphabetically. 

Through the search engine, the pictures can be filtered by one or more fields:
* **Title**: the title of the painting or picture;
* **Year**: the year in which the piece was created;
* **Artist**: the creator of the piece;
* **Gallery**: where the picture is located, when available;
* **Painted in**: place where the artist created the piece, when available;
* **Keyword**: word describing the piece, useful for filtering by content;
* **Color**: a color picker appears where the user can select whichever color they like, and the pictures will be filtered by whether or not that color is in the 5 most predominant in the piece. 

## Provenance of data
All data comes from [*WikiArt*](https://www.wikiart.org), scraped using [this tool](https://github.com/lucasdavid/wikiart).  
The color extraction has been performed using a python script inspired by [this tutorial](https://www.alessandroai.com/extract-and-analyze-colors-from-any-image/).

## Data export
All data used to create the website can be exported in *csv*, *json* and *xml*, by following the link in the picture list and artist list.  
To download a picture, a link can be found in the detail page.  
To download a list of pictures, download the *json* file containing them and run 
```
python image_downloader.py path/to/pictures_json
```
which can be found in the **image_downloader** folder.

## Containerization

It's possible to run a containerized version of this project using [Docker](https://www.docker.com). 

Here's the steps to do it:
* make sure the Docker daemon is up and running
* open up a terminal window
* type `docker run -d -e "PORT=8000" -e "DEBUG=0" -p 8000:8000 isaccoz/idicolorz`
* wait a few minutes for the download of the image (~5 GB of data) 
* go to `http://0.0.0.0:8000` or `http://localhost:8000` using a web browser

If running on an ARM system (e.g. a Macbook with Apple M1 chip), the 3rd step should be replaced with
* type `docker run -d -e "PORT=8000" -e "DEBUG=0" -p 8000:8000 --platform linux/amd64 isaccoz/idicolorz`
  
To check all the available versions of the image, go to: https://hub.docker.com/r/isaccoz/idicolorz/tags

## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
