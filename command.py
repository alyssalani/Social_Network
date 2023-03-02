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
	UPDATE posts
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
	INSERT OR REPLACE INTO posts (user_id, text) 
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
	FROM follows JOIN users ON followed_id = user_id
	WHERE follower_id = ?
	""", id1)

	print(cursor.fetchone()[0])

	cursor.execute("""
	SELECT name 
	FROM follows JOIN users ON followed_id = user_id
	WHERE follower_id = ?
	""", id1)

	userList = cursor.fetchall()

	for x in userList:
	print(x[0])

	connection.commit()
	connection.close()

elif sys.argv[1] == '