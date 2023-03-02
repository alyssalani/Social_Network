#!/usr/bin/env python3

import sqlite3
import sys

if sys.argv[1] == 'checkFeed':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	id1 = sys.argv[2]

	cursor.execute("""
	SELECT post.text, name
	FROM follow 
	JOIN post ON followed_id = post.user_id
	JOIN user ON posts.user_id = user.user_id
	WHERE follower_id = ?
	ORDER BY post.time DESC
	LIMIT 10;
	""", (id1))

	userList = cursor.fetchall()

	for x in userList:
		print(x[1]+ " says " + x[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == 'createUser': #user email  must be unique
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()


	name = sys.argv[2];
	email = sys.argv[3];
	color = sys.argv[4];

	try: 
		cursor.execute("""
		INSERT INTO user (name, user_email, color) VALUES (?, ?, ?)
		""", (name, email, color))
		print("User added successfully.")
	except:
		print("This email is already in use.")

	connection.commit()
	connection.close()


elif sys.argv[1] == 'follow':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()


	follower_id = sys.argv[2]	#alternative could be ids = sys.argv[1:], and use ids for VALUES
	followed_id = sys.argv[3]

	cursor.execute("""
	INSERT INTO follow (follower_id,followed_id) VALUES (?,?)
	""", follower_id, followed_id)


	connection.commit()
	connection.close()

elif sys.argv[1] == 'likePost':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()


	user_id = sys.argv[2]
	post_id = sys.argv[3]

	cursor.execute("""
	UPDATE post
	SET likes = likes + 1
	WHERE user_id = ? AND post_id = ?
	""", (user_id, post_id))

	if cursor.rowcount == 0:
		print("Invalid user ID or post ID.")
	else:
		print("Post liked successfully.")

	connection.commit()
	connection.close()

elif sys.argv[1] == 'makePost':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	user_id = sys.argv[2]
	text = sys.argv[3]

	cursor.execute("""
	INSERT OR REPLACE INTO post (user_id, text) 
	VALUES (?,?)
	""", (user_id, text))

	if cursor.rowcount == 0:
	   print("Invalid.")
	else:
		print("Posted successfully.")

	connection.commit()
	connection.close()

elif sys.argv[1] == 'showFollowing':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	id1 = sys.argv[2];

	cursor.execute("""
	SELECT count(*)
	FROM follow JOIN user ON followed_id = user_id
	WHERE follower_id = ?
	""", id1)

	print(cursor.fetchone()[0])

	cursor.execute("""
	SELECT name 
	FROM follow JOIN user ON followed_id = user_id
	WHERE follower_id = ?
	""", id1)

	userList = cursor.fetchall()

	for x in userList:
	print(x[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == 'showFollowers':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	id1 = sys.argv[2];

	cursor.execute("""
	SELECT count(*)
	FROM follow JOIN user ON follower_id = user_id
	WHERE followed_id = ?
	""", id1)

	print(cursor.fetchone()[0])
	cursor.execute("""
	SELECT name 
	FROM follow JOIN user ON follower_id = user_id
	WHERE followed_id = ?
	""", id1)

	userList = cursor.fetchall()

	for x in userList:
		print(x[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == 'showLikes':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	post_id = sys.argv[2]

	cursor.execute("""
	SELECT likes 
	FROM post
	WHERE post_id = ? 
	""", (post_id,))

	print(cursor.fetchone()[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == 'showPosts':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	user_id = sys.argv[2]

	cursor.execute("""
	SELECT user.user_id, user.name, post.text, post.time, post.post_id
	FROM post
	JOIN user ON post.user_id = user.user_id
	WHERE user.user_id= ?
	ORDER BY post.time DESC
	""", (user_id,))

	postList = cursor.fetchall()
	for x in postList:
		print(x)

	connection.commit()
	connection.close()


elif sys.argv[1] == 'showUsers':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	cursor.execute("""
	SELECT name FROM user""")
	userList = cursor.fetchall()

	for x in userList:
		print(x[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == 'suggest':
	connection = sqlite3.connect("Social_Network.db")
	cursor = connection.cursor()

	id1 = sys.argv[2]

	#For each user 1 who has a common friend 3 with another user 2, suggest user 2 as a friend option. 
	cursor.execute("""
	SELECT F1.followed_id
	FROM follow F1
	WHERE (F1.followed_id != ?) AND F1.follower_id IN (
	SELECT F2.followed_id
	FROM follow F2
	WHERE F2.follower_id =?)
	AND F1.followed_id NOT IN (
	SELECT F3.followed_id
	FROM follow F3
	WHERE F3.follower_id=?);
	""", (id1, id1, id1))

	userList = cursor.fetchall()
	for x in userList:
		print("It is suggested that you follow " + str(x[0]))

	connection.commit()
	connection.close()
