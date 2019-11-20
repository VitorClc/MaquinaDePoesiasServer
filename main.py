import eventlet
import socketio
import json

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.on('cpfValidation')
def my_message(sid, data):
    with open('data.json', 'r') as fp:
        obj = json.load(fp)
        for dict in obj:
            if dict['cpf'] == data:
                sio.emit("cpfResponse", False)
            else:
                sio.emit("cpfResponse", True)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8081)), app)