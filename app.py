from flask import Flask, request, jsonify, render_template
from models import db, Rule
from rule_ast import create_rule, evaluate_rule
from common import some_function
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules.db'
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')  # HTML file serve karne ke liye

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({"error": "Rule string is required!"}), 400

    new_rule = Rule(rule_string=rule_string)
    db.session.add(new_rule)
    db.session.commit()
    return jsonify({"message": "Rule created successfully!"}), 201

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided!"}), 400
    
    rule = Rule.query.first()
    if not rule:
        return jsonify({"error": "No rules found!"}), 404
    
    result = evaluate_rule(rule.rule_string, data)
    return jsonify({"result": result}), 200

if __name__ == "__main__":
    app.run(debug=True)
