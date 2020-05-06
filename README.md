FlaskRating is an service application that will add and update data in a csv file via flask API. FlaskRating Contains Following Files:

1) JobData.csv contains DataSets for all sector's jobs, tendors, and freelancing for professional work.
2) rating.csv contains all the Datasets for the ratings collected by the users on that server.
3) ratingUpd.py file contains all the python programming to add ratings.
4) app.py is flask service based api using port:5000

Testing:
For testing the application you have to install Postman (You can try any HTTP API testing tool, This is just my preference). After installing launch it and enter the URL for the flask route we just created and change the request type to POST. Then click on body and select x-www-form-urlencoded and enter the keys as show in the image below and click on send. You will get responses such as “added”, “updated”, “error”, “invalid”.
