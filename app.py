from flask import Flask, request, render_template
import os
import mysql.connector

app = Flask(__name__)

# Connect to the MySQL database on AWS
cnx = mysql.connector.connect(
    user='admin',
    password='company_project10',
    host='database-1.ced1eyf8wcxc.us-east-2.rds.amazonaws.com',
    database='database-1'
)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/webhook1', methods=['POST'])
def handle_webhook():
    data = request.json
    issue_id = data['issue']['id']
    issue_title = data['issue']['fields']['summary']
    issue_description = data['issue']['fields']['description']
    
    app.loggger.info(data)
    app.logger.info('issue id=%s', issue_id)
    app.logger.info('issue title=%s',issue_title)
    app.logger.info('issue description=%s', issue_description)

    # Insert the new ticket data into the database
    cursor = cnx.cursor()
    insert_query = "INSERT INTO tickets (id, title, description) VALUES (%s, %s, %s)"
    insert_values = (issue_id, issue_title, issue_description)
    cursor.execute(insert_query, insert_values)
    cnx.commit()
    cursor.close()

    return 'Ticket created'

if __name__ == '__main__':
    app.run(debug=True, port=os.environ.get('PORT', 5000))
