# Homework 1

Homework 1 is a short assignment about form validation and redirection.

## My Solution
I used Flask to create to serve a simple application.  There are two methods in the application:

  * `def index()` - the empty "/" path with a GET request is routed here
  * `def submit()` - the empty "/" path with a POST request is routed here

### Index explanation
Index gathers the text argument from the URL using `request.args.get()`.  I used the get method so that I could set a default value of ""

### Submit explanation
Submit gathers the text from the form using the dictionary's get method as well.  It also gives an empty string if text is not a key in the dictionary.  I then use the `codecs.encode()` method to encode the text using rot13 encoding and redirect back to the empty "/" using the GET method.

### How I Hosted the App
To host this simple application I ran it on my laptop and used [ngrok](https://ngrok.com) to HTTP tunnel to my localhost.

### Other ways to write the application
* I could have used a single method to route "/" to.  Inside the function I could ask what method was used to get here and separate the POST and GET logic from eachother. If I went this route it might be more difficult in the future to separate the POST and GET logic and the function may start to smell.

