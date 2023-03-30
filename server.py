from flask import Flask, request

app = Flask(name)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    issue_id = data['issue']['id']
    issue_title = data['issue']['fields']['summary']
    issue_description = data['issue']['fields']['description']

    # Process the new ticket here, e.g. send a notification to Slack
    print(f"New ticket created: ID {issue_id}, Title: {issue_title}, Description: {issue_description}")

    return '', 200

if name == 'main':
    app.run(debug=True, port=5000)