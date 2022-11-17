# base of kobold ai 
# https://github.com/KoboldAI/KoboldAI-Client


# Terminal tags for colored text
class colors:
    PURPLE    = '\033[95m'
    BLUE      = '\033[94m'
    CYAN      = '\033[96m'
    GREEN     = '\033[92m'
    YELLOW    = '\033[93m'
    RED       = '\033[91m'
    END       = '\033[0m'
    UNDERLINE = '\033[4m'


# Start flask & SocketIO
print("{0}Initializing Flask... {1}".format(colors.PURPLE, colors.END), end="")
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET KEY'] = 'secret!'
socketio = SocketIO(app)
print("{0}OK!{1}".format(colors.GREEN, colors.END))

# Set up Flask routes
@app.route('/')
def index():
    return render_template('index.html')




#==================================================================#
# Event triggered when browser SocketIO is loaded and connects to server
#==================================================================#
@socketio.on('connect')
def do_connect():
    print("{0}Client connected!{1}".format(colors.GREEN, colors.END))
    emit('from_server', {'cmd': 'connected'})

#==================================================================#
# Event triggered when browser SocketIO sends data to the server
#==================================================================#
@socketio.on('message')
def get_message(msg):

    print("{0}Data recieved:{1}{2}".format(colors.GREEN, msg, colors.END))
    # Submit action
    if(msg['cmd'] == "???"):
        emit('from_server', {'cmd': '???', 'data':"???"})




#==================================================================#
#  Final startup commands to launch Flask app
#==================================================================#
if __name__ == "__main__":
    # Start Flask/SocketIO (Blocking, so this must be last method!)
    print("{0}Server started!\rYou may now connect with a browser at http://127.0.0.1:5035/{1}".format(colors.GREEN, colors.END))
    socketio.run(app, host='0.0.0.0', port=5035)
    #socketio.run(app)