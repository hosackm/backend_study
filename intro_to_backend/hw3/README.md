# Homework 3: Blog backed by SQL database

This homework is to build a very minimal blog.  It has a frontpage that shows the most recent blog posts.  There should also be a submissions page where you can submit a title and blog post.  The website is to be backed by a SQL database that will store all the posts.

## My Design Choices

### Database Design

In order to meet all the required features of the blog assignment I've decided the database should store the following information:

    * Title - Text entry for displaying the title on the page
    * Post - Text entry for display the blog content on the page
    * Unique ID - An integer that can be used as a permalink to the post
    * Created Date - A Date value so that we can sort by most recent for displaying on the homepage

### Application Design

The following routes should be exposed

    * /blog - the landing page of the blog.  There should be a link to the submission page
    * /submit - this page will contain a form.  It will do validation on the form when it is submitted and interact with the database
    * /posts/<int:permalink> - for each blog entry we will have a dynamic route to fetch it from the database


### Template Design

There are three types of pages in this blog.

    1. Homepage
    2. Submit Page
    3. Blog Page

All three should share the header of the blog.  Each of them will have its own content.

       base.html          welcome.html         submit.html               post.html
    +--------------+    +--------------+     +--------------+         +--------------+
    | <--Header--> |    | extends base |     | extends base |         | extends base |
    +--------------|    +--------------+     +--------------+         +--------------+
    |{%            |    |   Title 1    |     |    Form      |         |    Title     |
    | Empty Content|    +--------------|     |   ------     |         +--------------+
    |     Block    |    |    Post 1    |     |   ------     |         |     Post     |
    |            %}|    |              |     |  [ submit ]  |         |   ------- -  |
    +--------------+    |     .....    |     |              |         |   -----  --  |
                        +--------------+     +--------------+         +--------------+
                        |    Title n   |
                        +--------------+
                        |    Post n    |
                        |              |
                        |              |
                        +--------------+
