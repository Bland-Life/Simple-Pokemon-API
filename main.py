import pokeapp as pk

app = pk.create_app()

pk.create_db(app)

if __name__ == "__main__":
    app.run(debug=True)