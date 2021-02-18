from project import app, socketio
from flask_socketio import send
# if __name__ == '__main__':
#     app.run(debug=True)


@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
