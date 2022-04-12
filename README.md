# IDI Colorz
*Open Data Management &amp; the Cloud exam project*

Website is available @ *link*

## Intro
**IDI Colorz** is a website dedicated to the most famous artists of the last millennium.   
In it, the user can read about all their paintings and drawings, with an insight on the color composition of each piece.  

The name of the project comes from the initials of its creators: Irene Ferfoglia, Daniele Irto, and Isacco Zinna.


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
* make sure Docker is up and running
* clone this repo
* `cd` into the folder `IDI_Colorz`
* open up a terminal window
* type `docker-compose up`

After a few minutes, the terminal should show something similar to this:
```
web_1  | System check identified no issues (0 silenced).
web_1  | April 12, 2022 - 15:37:43
web_1  | Django version 4.0.3, using settings 'vg_site.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```
To reach the website, simply go to `http://0.0.0.0:8000/` or `http://localhost:8000`.
## License
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
