# Random-Tweet-Bot-with-MySQL
This is a program which randomly selects an entry from a MySQL database and sends it to your connected Twitter account to post.

In my particular case, I was using it to post trivia facts about technology and gaming randomly to a Twitter account.

#Dependencies
You will need a Database that can connect to your program. In this case, I was using MySQL with this Python program.

Modules:

SQLalchemy: https://pypi.org/project/SQLAlchemy/
Flask: https://pypi.org/project/Flask/
Flask_sqlalchemy: https://pypi.org/project/Flask-SQLAlchemy/
Twitter: https://pypi.org/project/twitter/


You will also need Keys and Tokens from a Twitter Dev Account, which you can sign up for here: https://developer.twitter.com/en.

I would first run TriviaFactModelsforTwitterBot and comment out everything below the TriviaFacts model class for now, so that you can create the table for your Model in your Database. The integer after "db.String" in the triviafact column is the number of characters allowed in the string you store there.

Go over to the TriviaFactListandUploader file. You can then put all the items (strings) you would like to load into your database, separated by commas, into an array. In this program, the array is initialized by the "trivia" variable.
Have the program call the TriviaFunction() function at the bottom, and then run this file.
This will load all of your items into the Database and give them sequential ID numbers.

Back in the TriviaFactModels file, you can uncomment out the gettriv() and posttweet() functions, as well as the code that comes after the TriviaFacts model. This code counts all of the entries in the MySQL table and sets it as the variable "result". In gettriv(), a random number is chosen as the ID number for the item it will retrieve from the table in your database. The item is then sent to post on your Twitter account in posttweet().
