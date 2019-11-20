import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.on('cpfValidation')
def my_message(sid, data):
    print('message ', data)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8081)), app)