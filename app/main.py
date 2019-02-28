from flask import Flask, jsonify, request
from flask_cors import CORS
import os

# Start the app and setup the static directory for the html, css, and js files.
app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)

# This is your 'database' of scripts with their blocking info.
# You can store python dictionaries in the format you decided on for your JSON
   # parse the text files in script_data to create these objects - do not send the text
   # files to the client! The server should only send structured data in the sallest format necessary.
scripts = []

### DO NOT modify this route ###
@app.route('/')
def hello_world():
    return 'Theatre Blocking root route'

### DO NOT modify this example route. ###
@app.route('/example')
def example_block():
    example_script = "O Romeo, Romeo, wherefore art thou Romeo? Deny thy father and refuse thy name. Or if thou wilt not, be but sworn my love And I’ll no longer be a Capulet."

    # This example block is inside a list - not in a dictionary with keys, which is what
    # we want when sending a JSON object with multiple pieces of data.
    return jsonify([example_script, 0, 41, 4])


''' Modify the routes below accordingly to 
parse the text files and send the correct JSON.'''

## GET route for script and blocking info
@app.route('/script/<int:script_id>')
def script(script_id):
    count = 0;
    # right now, just sends the script id in the URL
    path = "/app/script_data/"
    example_script = ""
    new_list = ""
    parsething = {}
    fp = open("/app/actors.csv","r")
    actor_dic = {}
    csv_line = fp.readline()
    while csv_line:
        actor = csv_line.split(',')
        csv_line = fp.readline()
        if csv_line:
            actor_name = actor[1][:-1]
            actor_number = actor[0]
            actor_dic[actor_name] = actor_number
           
        else:
            actor_name = actor[1]
            actor_number = actor[0]
            actor_dic[actor_name] = actor_number           
    fp.close()
    for filename in os.listdir(path):
        current = path + filename
        f = open(current,"r")
        line = f.readline()
        if int(line) == int(script_id):
            while line:
                if line == '\n':
                    count = count + 1
                else:
                    if count == 1:
                        example_script = line
                    elif count == 2:
                        # example_script = line
                        partial_value = line.split(' ')
                        value = partial_value[0][:-1]
                        start = int(partial_value[1][:-1])
                        end = int(partial_value[2][:-1])
                        part = ''.join(value)
                        parsething[part] = {}
                        parsething[part]["script"] = example_script
                        parsething[part]["start"] = start
                        parsething[part]["end"] = end
                        for i in range(3,len(partial_value)):
                            if i != len(partial_value) -1:
                                total = partial_value[i][:-1].rstrip()
                            else:
                                total = partial_value[i]
                            new_list = total.split('-')
                            name = new_list[0]
                            position = new_list[1]
                            parsething[part][actor_dic[name]] = [int(position),name] 

                line = f.readline()       

            f.close()
        f.close() 
    return jsonify(parsething)



## POST route for replacing script blocking on server
# Note: For the purposes of this assignment, we are using POST to replace an entire script.
# Other systems might use different http verbs like PUT or PATCH to replace only part
# of the script.
@app.route('/script', methods=['POST'])
def addBlocking():
    # right now, just sends the original request json
    data = request.json
    name = "hamlet" + data["scriptNum"] + ".txt"
    path = "/app/script_data/" + name
    fp = open(path,"w")
    fp.write(data["scriptNum"] + '\n')
    fp.write('\n')
    fp.write(data["script"] + '\n')
    fp.write('\n')
    index = 0;
    line = ""
    for key in data:
        if (key != "scriptNum") and (key != "script"):
            line = line + str(key) + "." + " " + str(data[key]["start"]) + "," + " " + str(data[key]["end"]) + "," + " "
            for key_d in data[key]:
                if(key_d != "end") and  (key_d != "start"):
                    if(index < len(data[key])-1):
                        line = line + str(data[key][key_d]) + "," + " "
                    else:
                        line = line + str(data[key][key_d])
                index = index + 1
            index = 0;
            fp.write(line + "\n")


            line = ""
    fp.close()

    # f = open(path,"r")
    # line_1 = f.readlines()
    # # while line:
    # #     line = line + "\n" + f.readline();
    # f.close()
    # a = len(data[key])

    return jsonify(request.json)



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))

