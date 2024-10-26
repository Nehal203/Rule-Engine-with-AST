import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  # "operator" or "operand"
        self.left = left            # Reference to left child Node
        self.right = right          # Reference to right child Node
        self.value = value          # Optional value (e.g., number for comparisons)

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value})"

def create_rule(rule_string):
    tokens = re.split(r"(\band\b|\bor\b|\(|\))", rule_string)
    root = Node(node_type="operator", value="OR")
    # For simplicity, implement the logic to parse tokens and construct AST
    # Aap yahan token parsing ki logic add kar sakte hain
    return root

def combine_rules(rule_strings):
    if len(rule_strings) == 1:
        return create_rule(rule_strings[0])
    root = Node(node_type="operator", value="AND")
    root.left = create_rule(rule_strings[0])
    root.right = create_rule(rule_strings[1])
    return root

def evaluate_rule(rule_string, data):
    x = data.get('x')
    
    if x is None:
        return {"error": "x is required in data!"}, 400

    # Evaluation logic (same as before)
    if ">" in rule_string:
        threshold = int(rule_string.split(">")[1].strip())
        return {"result": x > threshold}
    elif "<" in rule_string:
        threshold = int(rule_string.split("<")[1].strip())
        return {"result": x < threshold}
    elif "==" in rule_string:
        threshold = int(rule_string.split("==")[1].strip())
        return {"result": x == threshold}
    else:
        return {"error": "Unknown rule!"}, 400
