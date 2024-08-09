# Capital Finder
## LAB - Class 16
### Project: Vercel + [Countries API](https://restcountries.com/#fields)
### Author: Maddie Amelia Lewis

### Links and Resources
[Deployment Link on Vercel](https://capital-finder-maddieamie.vercel.app/api/capital_finder)

To view the base repo:
[capital-finder repo](https://github.com/maddieamie/capital-finder)

### Setup

Install requirements.txt in a virtual environment, or go to [deployment link](https://capital-finder-maddieamie.vercel.app/api/capital_finder). 

[//]: # (### How to initialize/run your application &#40;where applicable&#41;)

To run a query, structure it like so: 
https://capital-finder-maddieamie.vercel.app/api/capital_finder?query=capital=Santiago

where "capital" could be that or "country", and "Santiago" can be replaced by either another country's capital's name or a country name with the country prompt. 

ex: query=capital=Santiago
for a capital city

ex: query=country=Chile
for a country 

### Tests

_How do you run tests?_
I would make small changes to my code and then push it up to the deployment server. 
Then, I would check the logs to see what error code occurred and where in my function code, and then make adjustments.
Since this lab is very short and the internet's pretty fast, I did not set up a local environment using Vercel CLI, though I would have in a more complicated API project. 

I also used [this resource](https://reqbin.com/) to test my API response online, to see what the general response would be once I got back an error code that my code format did not match the response format. 

_Any tests of note?_
N/A

_Describe any tests that you did not complete, skipped, etc_
I did not specifically write tests for this lab, just did trial and error debugging. 
