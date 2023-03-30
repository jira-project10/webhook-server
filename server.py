from flask import Flask, request, render_template

app = Flask(name)

@app.route('https://example.com/rest/webhooks/webhook1', methods=['POST'])
def handle_webhook():
    data = request.json
    issue_id = data['issue']['id']
    issue_title = data['issue']['fields']['summary']
    issue_description = data['issue']['fields']['description']

    # Process the new ticket here, e.g. send a notification to Slack
    #print(f"New ticket created: ID {issue_id}, Title: {issue_title}, Description: {issue_description}")
    #return '', 200
    return render_template('ticket.html', issue_id=issue_id, issue_title=issue_title, issue_description=issue_description)

if name == 'main':
    app.run(debug=True, port=5000)