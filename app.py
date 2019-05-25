from flask import request
from flask_api import FlaskAPI

app = FlaskAPI(__name__)


@app.route('/example/')
def example():
    """
    This is just an example
    """
    return {'hello': 'world'}


@app.route('/file-list/')
def file_list():
    """
    Returns the list of files
    """
    
    return {'list': 'tbd'}


if __name__ == "__main__":
    app.run(debug=True)
