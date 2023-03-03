#!/usr/bin/env python3

import sqlite3

connection = sqlite3.connect("Social_Network.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    user_id         INTEGER PRIMARY KEY,
    user_email      TEXT NOT NULL,
    color           TEXT NOT NULL,
    name            TEXT NOT NULL,
    follower_count       INTEGER DEFAULT 0,
    UNIQUE(user_email)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS post (
    post_id         INTEGER PRIMARY KEY,
    text            TEXT NOT NULL,
    user_id         INTEGER NOT NULL,
    likes           INTEGER DEFAULT 0,
    time            DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES user(user_id)
)
""")
#follow name needs an alternative name
cursor.execute("""
CREATE TABLE IF NOT EXISTS follow (
    follower_id  INTEGER NOT NULL,
    followed_id  INTEGER NOT NULL,
    PRIMARY KEY(follower_id, followed_id),
    FOREIGN KEY(follower_id) REFERENCES user(user_id),
    FOREIGN KEY(followed_id) REFERENCES user(user_id)
)
""")

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS someone_followed
AFTER INSERT ON follow
BEGIN
    UPDATE user SET follower_count = follower_count + 1
    WHERE user.user_id = new.followed_id;
END
""")

cursor.execute("""
CREATE TRIGGER IF NOT EXISTS someone_unfollowed
AFTER DELETE ON follow
BEGIN
    UPDATE user SET follower_count = follower_count - 1
    WHERE user.user_id = old.followed_id;
END
""")


connection.commit()
connection.close()
