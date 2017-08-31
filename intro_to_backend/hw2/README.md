### Homework 2

This homework is about form validation and redirecting back to the form page with error messages.


## Routes

  * "/" GET: returns form.html template.
  * "/" POST: Validates the input.  If there were errors a dictionary of which inputs were invalid is used to render the form html with error messages.  The values of username and email that were posted in the form are repopulated into their textboxes.  If all inputs were valid redirect to the welcome route with the username
  * "/welcome/<string:username>": Displays, "Welcome {username}" where username is a value gathered from the URL by Flask.
