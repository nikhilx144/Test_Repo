from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "You have successgully built a project with docker and jenkins!\nA docker image ois made every time new changes to the code are pushed upstream, then the docker image is pushed to dockerhub and finally a container is run from the image."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
