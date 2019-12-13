# realside
This project is intended to build off of another text generation project. News articles will be generated under fictitious accounts and posted on a daily basis. The api app will allow someone to pull articles from the site.


------------
The following the previous project idea, which I still plan to do at some other time.
# metapi

This project has two parts.

The first is an api that turns uploaded code into a usable api. This is the business logic for metapi, which will be kept in the `api` app. It will accept a zipped file containing code, which is presumably intended to be used as an api. At the root directory, there must be a driver, called `metamain.py`, and a dependencies file called `requirements.txt`. When code is uploaded, the client will create a named id, which can be any alphanumeric string optionally containing "-" and "\_". This id will be the way the client calls their api.

The second part is the `meta` app, which holds the presentation logic for metapi. Ideally, `meta` would handle auth, an interface for uploading new code and viewing simple stats about the user's existing APIs.
