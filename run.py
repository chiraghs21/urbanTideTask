from app import app

if __name__ == "__main__":
    # Run the Flask application on host 0.0.0.0 and port 5001
    # Setting debug to True for development purposes
    app.run(host="0.0.0.0", port=5001, debug=True)
