# Social_Network
Creates and manages a social network database

This program is still under construction, but currently has basic functionality. 

**NOTE: While all commands were created as separate executable files, they have been condensed into one file for readability purposes

This social network is made up of 3 tables. The tables are: user, post, and follow. 

The user table consists of user_id (PRIMARY_KEY), user_email, color, name, and follower_count.
The post table consists of post_id (PRIMARY_KEY), text, user_id, likes, and time. 
The follow table consists of follower_id, and followed_id which both reference user_id. 

Command options:
  - createUser
  - showUsers
  - follow
  - showFollowing
  - showFollowers
  - makePost
  - showPosts
  - showLikes
  - likePost
  - checkFeed
  - suggest

'createUser' takes a name, email, and color and adds the user to the database. All users must have a different email. 

'showUsers' takes no arguments displays a list of all of the names of all users.

'follow' takes two user_ids and adds the first id to the follow table as a follower_id, and adds the second id to the follow table as a followed_id

'showFollowing' takes a user_id and displays the count of and the names of the users that the given id is following. 

'showFollowers' takes a user_id and displays the count of and the names of the users that are following the given id. 

'makePost' takes a user_id and a string, and gives the text a post_id and timestamp and adds it to the database.

'showPosts' takes a user_id and displays all of the user's posts with all of their information. 

'showLikes' takes a post_id and displays the amount of likes the post has. 

'likePost' takes the user_id and post_id and adds a like to the post
 
'checkFeed' takes a user id and checks the 10 most recent posts made by users the given id follows

'suggest' takes a user_id and returns suggested users for the id to follow
