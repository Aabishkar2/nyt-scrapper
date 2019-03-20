# nyt-scrapper
This python code scraps some of the news of New York times based on the url input and displays the output in JSON format.

Install the JSON viewer chrome extension for the pretty result.

The running instances of this application is hosted on Digital Ocean Droplets.

To see the scrapped output of latest section of the technology page go to:
http://134.209.144.7/

To see the scrapped output of latest section of the economy page go to:
http://134.209.144.7?category=business/economy

Similarly for science category do:
http://134.209.144.7?category=science

To see the output with all the contents of technology page as well, go to:
http://134.209.144.7/content

To see the output with all the contents of economy page as well, go to:
http://134.209.144.7/content?category=business/economy

To implement this locally, install docker and then do docker-compose up in your directory.
