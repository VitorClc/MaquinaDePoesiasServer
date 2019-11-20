import eventlet
import socketio
import json

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.on('cpfValidation')
def my_message(sid, data):
    foundCPF = False
    with open('data.json', 'r') as file:
        obj = json.load(file)
        for dict in obj:
            if dict['cpf'] == data:
                print("bbbb")
                foundCPF = True
            else:
                print("aa")
    
    file.close()

    if(foundCPF == False):
        sio.emit("cpfResponse", True)
    else:
        sio.emit("cpfResponse", False)

@sio.on('saveData')
def writeData(sid, data):
    receivedData = {
        "cpf": data[0],
        "name": data[1],
        "email": data[2],
        "phone": data[3],
        "ans1": data[4],
        "ans2": data[5],
        "ans3": data[6],
        "ans4": data[7],
        "ans5": data[8]
    }

    with open('data.json') as f:
        obj = json.load(f)
        obj.append(receivedData)
        with open('data.json', 'w') as outfile:
            json.dump(obj, outfile)
        
        sio.emit("finished", True)
        outfile.close()
    f.close()

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8081)), app)