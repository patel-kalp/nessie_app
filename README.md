# nessie_app
http://api.nessieisreal.com/

# How to Run
1. Please make sure you are using Python 3.8 as it might cause compatibility issues with package versions (use one of the following 3 commands depending on your python installation):  
- `python --version`  
- `python3 --version`  
- `python3.8 --version`  
2. Install the required packages (use one of the following 3 commands depending on your python installation):  
- `pip install -r requirements.txt`
- `pip3 install -r requirements.txt`
- `python3.8 -m pip install -r requirements.txt`
3. Create a file called `.env` in the main project directory and add your API_KEY. The `.env` file should look like:  
`API_KEY=<your_api_key>`  
4. Start the Flask app!   
`python app.py` (you might have to do `python3.8 app.py`)

