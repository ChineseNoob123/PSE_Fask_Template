from website import create_app

app = create_app()
ENV = 'dev'

# Check if we are in dev mode to enable debugging etc
if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

if __name__ == '__main__':
    app.run()


# Routes

@app.route('/')
def hello_world():
    return 'Hello World!'
