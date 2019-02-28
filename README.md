# docker
To start:

`docker build -t a1-301 .`

`docker run -d --name a1-301-container -p 80:80 a1-301:latest`

`docker start a1-301-container`

To stop/remove container:

`docker stop a1-301-container`

`docker rm a1-301-container`

# heroku
`heroku login`

`heroku create --app <app-server-name>`

`heroku container:login`

`heroku container:push web --app <app-server-name>`

`heroku container:release web --app <app-server-name>`

`heroku open --app <app-server-name>`

# Write your documentation below


heroku url : https://csc301-yangsiq1.herokuapp.com/actor.html

# objective statement
	Theatre Blocking application should allowed certain type of user(such as actor) to check their position on the specific script then they don't need to search entire script to find a specific script blocking information. 

	It should also support certain type of user(such as director) to modify the specific script's blocking information and save it to let other users know.

# personas

	Jerry: actor, he always forget his position on a certain script.

	Mike: director, he always want to make changes of actors' position on some scripts.

	Jenny: actress age 23

# user stories
	Jerry: as a forgetful actor, I want to check a certain script blocking information for my own parts. So that I don't need to go through all the script then find my blocking information.

	Mike: as a director, I think I should able to modify the blocking for all parts of the script when I want. Also, I want to see the block information of a certain script, and I should able to modify that blocking information. Also I want to store these changes, and I don’t need to change again.

	Jenny: as a actress, I want to see my blocking information in a specific script, and it should include all the part of the script. I should immediately see the changes when the blocking information has been changed by director.

#acceptance criteria
	For Jerry’s stories:  The blocking information for a specific script and specific actor should be displayed.

	For Mike’s stories:  The blocking information of any script and any actor can be changed.
			       		 The blocking information of specific script and specific actor can be changed.
			        	 The blocking information that has been changed should be store.

	For Jenny’s stories: Screen always display the newest blocking information.

#JSON
	script_get_data.json
	I use the dictionary to store whole data that I want.In the first dictionary, I have two keys "1" and "2", and this represent the part number, in order to make my life easier on the later steps. I can easily know which part of script I'm getting. Then the value of each key would be the same format, I create another dictionary to be the value.In the second dictionary, I have keys to represent the actor's id which is I read from actors.csv, the value for these key would be the position and the actor name. Also, I have the entry to represent the start position and end position for current part. Finally I have the entire script sentence. I use the start and end position to cut the sentence in right place.

	script_post_data.json

	I use dictionary to represent the data in post function. I have keys to represent the part number and value of these keys I use another dictionary to represent it. In the inner dictionary I have the actor's name as key and "name-position" format as their value. It will let me more easier to write data in same format.Also I have the keys to represent the end and start position. I uses these two to put into the txt file.
	In the outer dictionary, I have another two keys. One is the total script, it helps me to write script sentence to the txt file. And the scriptNum, it helps me to put the scriptNum at the beginning of the file. 















