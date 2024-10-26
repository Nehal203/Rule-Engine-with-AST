def parse_operand(operand_string):
    key, operator, value = operand_string.split(' ')
    value = int(value) if value.isdigit() else value.strip("'")
    return key, operator, value

def evaluate_condition(attribute_value, operator, value):
    if operator == '>':
        return attribute_value > value
    elif operator == '<':
        return attribute_value < value
    elif operator == '=':
        return attribute_value == value
    return False

def evaluate_rule(json_data, node):
    if node.node_type == "operand":
        key, operator, value = parse_operand(node.value)
        return evaluate_condition(json_data[key], operator, value)
    
    elif node.node_type == "operator":
        if node.value == "AND":
            return evaluate_rule(json_data, node.left) and evaluate_rule(json_data, node.right)
        elif node.value == "OR":
            return evaluate_rule(json_data, node.left) or evaluate_rule(json_data, node.right)
    
    return False
