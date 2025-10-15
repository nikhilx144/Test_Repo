from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Successfully built a project with docker and jenkins!\nA docker image is made every time new changes to the code are pushed upstream (github repo), a docker image of the repo is pushed to dockerhub and finally a docker container is run from the image."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
