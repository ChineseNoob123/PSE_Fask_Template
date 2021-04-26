from website import create_app

ENV = 'dev'
app = create_app()


# Check if we are in dev mode to enable debugging etc
if ENV == 'dev':
    app.debug = True
else:
    app.debug = False

if __name__ == '__main__':
    app.run(debug=True)
