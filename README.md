# blog
Djangoblog
A Blogging Application A
web application that allows a user to manage their own blog. A
blog is simply a collection of "posts" (textual content), typically displayed in reverse
chronological order.

The purpose of this web application is to give a user the ability to run their own blog. A blog is just a
series of posts made by an author. Each post has a title, a published date, an author, and textual
(HTML) content. When first loading the application at the root URL, the user should be presented with a
list of available posts listed in reverse chronological order (newest posts first). The application should
allow a user to login via the ‘/login’ URL, which gives that user the ability to make changes to the blog.
After logging in, the user should be sent to the ‘/dashboard’ page, which presents the user with an
interface that:
1. Shows a list of their posts in a table. This list just shows the title of the post, with buttons
labeled ‘Edit’ and ‘Delete’. This edit button will take the user to a page that allows them to
update the post. The delete button will simply delete that post.
2. Allows the user to add a new post (This can be done either directly on the dashboard page
or on a new page).

1. Extend the application to support multiple users: You do not have to worry about supporting
a full registration workflow. Use a table in the database to store users and their credentials,
and use this table to support logins from many accounts. Please note: storing passwords
that are unencrypted is a bad idea, security wise. However, there is no need for us to delve
into that.
