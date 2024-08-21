'''this is the frameworks needed to work with the server'''
import csv
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home_page():
    '''this function renders the home page of our website'''
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    '''renders the template of the index.html file as the home file'''
    return render_template(page_name)

def linkshortener(my_token, website_link):
    '''Shortens the link using Bitly API'''
    headers = {
        'Authorization': f'Bearer {my_token}',
        'Content-Type': 'application/json',
    }

    data = {"long_url": website_link, "domain": "bit.ly"}

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', json=data, headers=headers, timeout=50)

    if response.status_code == 200:
        return response.json().get("link")
    return None

def write_to_csv(data):
    '''helps to write into the csv file'''
    with open('./database.csv', mode='a', newline='', encoding='utf-8') as csvfile:
        subject = data['subject'],
        email = data['email']
        message = data['message']
        
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fieldnames = [subject, email, message]

        csv_writer.writerow(fieldnames)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    '''Handles form submission and link shortening'''
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        website_link = request.form['subject']
        load_dotenv()
        my_token= os.getenv('API_KEY')
        shortened_url = linkshortener(my_token, website_link)

        if shortened_url:
            return render_template('shortened.html', shortened_url=shortened_url)
        return "Something went wrong. Please try again."
    return 'Invalid request method. Please use POST.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
