# Hackeriot Workshop #10
Intro to web bots and mitigation tactics

## Level 0 - Running a Web Server
What are HTTP response codes? which code should be added? fix the `server.py` file.
Bonus: why are we binding our server with a high port number?

## Level 1 - An Automated Request
What is the server address? fix the `client.py` file, note that we might need to specify a port.

## Level 2 - Custom Responses
Are there other HTTP codes you are familiar with? add the code for redirecting a user to the relevant function at the server-side. Alter the flow so a user will be redirected to a different website when she is browsing to the sever.

## Level 3 - Detecting the bot
Add the missing part to `bot-analysis.py`, do you think it is a good solution?

## Level 4 - Evading detection
Find a legitimate `user-agent` string and embed it as part of the client side.

## Level 5 - Detecting the bot V2
In what other ways you can differentiate between a request from your browser and the client?

## BONUS Points
Your code should now be similar to the files found at the "Solution" folder.\
Improve your client to look more like a real browser and improve the detections on the server's side.\
You may use WireShark or any other tool you prefer.