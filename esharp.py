import re
import sys

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.tokens = []
        self.keywords = [
            'ESTABLISH', 'AS', 'END', 'CALCULATE', 'WITH', 'AND', 'STORE', 'IN',
            'TRANSMIT', 'TO', 'CONSOLE', 'SECURE', 'OTHERWISE', 'IF', 'IS',
            'GREATER', 'THAN', 'THEN', 'ELSE', 'INTEGER', 'STRING', 'ADD', 'SUBTRACT',
            'ALLOCATE', 'MEMORY', 'FOR', 'DEALLOCATE', 'LOCK', 'RESISTANT', 'EXECUTION',
            'INITIALIZE', 'SERVER', 'ON', 'PORT', 'LISTEN', 'REQUEST', 'RESPOND'
        ]

    def tokenize(self):
        while self.pos < len(self.text):
            char = self.text[self.pos]
            if char.isspace():
                self.pos += 1
            elif char == '#':
                while self.pos < len(self.text) and self.text[self.pos] != '\n':
                    self.pos += 1
            elif char.isalpha():
                word = ""
                while self.pos < len(self.text) and (self.text[self.pos].isalnum() or self.text[self.pos] == '_'):
                    word += self.text[self.pos]
                    self.pos += 1
                if word in self.keywords:
                    self.tokens.append(Token('KEYWORD', word))
                else:
                    self.tokens.append(Token('IDENTIFIER', word))
            elif char.isdigit():
                num = ""
                while self.pos < len(self.text) and self.text[self.pos].isdigit():
                    num += self.text[self.pos]
                    self.pos += 1
                self.tokens.append(Token('INTEGER_LITERAL', int(num)))
            elif char == '"':
                self.pos += 1
                string = ""
                while self.pos < len(self.text) and self.text[self.pos] != '"':
                    string += self.text[self.pos]
                    self.pos += 1
                self.pos += 1
                self.tokens.append(Token('STRING_LITERAL', string))
            else:
                # Unknown character
                self.pos += 1
        return self.tokens

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.memory_allocated = False
        self.locked_vars = set()
        self.server_socket = None

    def run(self, nodes):
        for node in nodes:
            self.execute(node)

    def execute(self, node):
        method_name = f'execute_{node["type"]}'
        method = getattr(self, method_name, self.no_method)
        return method(node)

    def no_method(self, node):
        raise Exception(f"No execute_{node['type']} method defined")

    def execute_ALLOCATE(self, node):
        self.memory_allocated = True

    def execute_DEALLOCATE(self, node):
        self.memory_allocated = False
        self.variables.clear()

    def execute_SECURE(self, node):
        try:
            for stmt in node['body']:
                self.execute(stmt)
        except Exception as e:
            for stmt in node['otherwise']:
                self.execute(stmt)

    def execute_ESTABLISH(self, node):
        if not self.memory_allocated:
            raise Exception("CRITICAL ERROR: Memory not allocated. Access denied.")
        name = node['name']
        if name in self.locked_vars:
            raise Exception(f"RESISTANCE ERROR: Variable '{name}' is locked and resistant to change.")
        val = node['value']
        self.variables[name] = val
        if node.get('resistant'):
            self.locked_vars.add(name)

    def execute_TRANSMIT(self, node):
        if not self.memory_allocated:
            raise Exception("CRITICAL ERROR: Memory not allocated. Access denied.")
        val = node['target']
        if isinstance(val, str) and val in self.variables:
            print(self.variables[val])
        else:
            print(val)

    def execute_CALCULATE(self, node):
        if not self.memory_allocated:
            raise Exception("CRITICAL ERROR: Memory not allocated. Access denied.")
        dest = node['dest']
        if dest in self.locked_vars:
            raise Exception(f"RESISTANCE ERROR: Variable '{dest}' is locked and resistant to change.")
        v1 = self.variables.get(node['left'], node['left'])
        v2 = self.variables.get(node['right'], node['right'])
        if node['op'] == 'ADD':
            res = v1 + v2
        elif node['op'] == 'SUBTRACT':
            res = v1 - v2
        self.variables[dest] = res
        return res

    def execute_INITIALIZE_SERVER(self, node):
        import socket
        port = self.variables.get(node['port'], node['port'])
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('0.0.0.0', port))
        self.server_socket.listen(1)
        print(f"SERVER INITIALIZED ON PORT {port}")

    def execute_LISTEN_REQUEST(self, node):
        if not self.server_socket:
            raise Exception("SERVER ERROR: Server not initialized.")
        client, addr = self.server_socket.accept()
        data = client.recv(1024).decode()
        self.variables[node['store']] = data
        self.current_client = client
        print(f"REQUEST RECEIVED FROM {addr}")

    def execute_RESPOND(self, node):
        if not hasattr(self, 'current_client'):
            raise Exception("SERVER ERROR: No active request to respond to.")
        msg = self.variables.get(node['message'], node['message'])
        self.current_client.sendall(msg.encode())
        self.current_client.close()
        del self.current_client

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self, val=None):
        token = self.peek()
        if not token: raise Exception("Unexpected EOF")
        if val and token.value != val: raise Exception(f"Expected {val} got {token.value}")
        self.pos += 1
        return token

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        token = self.peek()
        if token.value == 'SECURE':
            return self.parse_secure()
        elif token.value == 'ESTABLISH':
            return self.parse_establish()
        elif token.value == 'TRANSMIT':
            return self.parse_transmit()
        elif token.value == 'CALCULATE':
            return self.parse_calculate()
        elif token.value == 'ALLOCATE':
            return self.parse_allocate()
        elif token.value == 'DEALLOCATE':
            return self.parse_deallocate()
        elif token.value == 'INITIALIZE':
            return self.parse_initialize_server()
        elif token.value == 'LISTEN':
            return self.parse_listen_request()
        elif token.value == 'RESPOND':
            return self.parse_respond()
        else:
            raise Exception(f"Unknown statement: {token.value}")

    def parse_initialize_server(self):
        self.consume('INITIALIZE')
        self.consume('SERVER')
        self.consume('ON')
        self.consume('PORT')
        port = self.consume().value
        self.consume('END')
        return {'type': 'INITIALIZE_SERVER', 'port': port}

    def parse_listen_request(self):
        self.consume('LISTEN')
        self.consume('FOR')
        self.consume('REQUEST')
        self.consume('STORE')
        self.consume('IN')
        store = self.consume().value
        self.consume('END')
        return {'type': 'LISTEN_REQUEST', 'store': store}

    def parse_respond(self):
        self.consume('RESPOND')
        self.consume('WITH')
        message = self.consume().value
        self.consume('END')
        return {'type': 'RESPOND', 'message': message}

    def parse_allocate(self):
        self.consume('ALLOCATE')
        self.consume('MEMORY')
        self.consume('FOR')
        self.consume('EXECUTION')
        self.consume('END')
        return {'type': 'ALLOCATE'}

    def parse_deallocate(self):
        self.consume('DEALLOCATE')
        self.consume('MEMORY')
        self.consume('END')
        return {'type': 'DEALLOCATE'}

    def parse_secure(self):
        self.consume('SECURE')
        body = []
        while self.peek() and self.peek().value != 'OTHERWISE':
            body.append(self.parse_statement())
        self.consume('OTHERWISE')
        otherwise = []
        while self.peek() and self.peek().value != 'END':
            otherwise.append(self.parse_statement())
        self.consume('END')
        return {'type': 'SECURE', 'body': body, 'otherwise': otherwise}

    def parse_establish(self):
        self.consume('ESTABLISH')
        resistant = False
        if self.peek().value == 'RESISTANT':
            self.consume('RESISTANT')
            resistant = True
        vtype = self.consume().value # INTEGER or STRING
        name = self.consume().value # identifier
        self.consume('AS')
        val_token = self.consume()
        val = val_token.value
        self.consume('END')
        return {'type': 'ESTABLISH', 'vtype': vtype, 'name': name, 'value': val, 'resistant': resistant}

    def parse_transmit(self):
        self.consume('TRANSMIT')
        target = self.consume().value
        self.consume('TO')
        self.consume('CONSOLE')
        self.consume('END')
        return {'type': 'TRANSMIT', 'target': target}

    def parse_calculate(self):
        self.consume('CALCULATE')
        op = self.consume().value
        self.consume('WITH')
        left = self.consume().value
        self.consume('AND')
        right = self.consume().value
        self.consume('STORE')
        self.consume('IN')
        dest = self.consume().value
        self.consume('END')
        return {'type': 'CALCULATE', 'op': op, 'left': left, 'right': right, 'dest': dest}

def run_code(code):
    try:
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        interpreter = Interpreter()
        interpreter.run(ast)
    except Exception as e:
        print(f"FATAL INTERPRETER ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            run_code(f.read())
    else:
        # Default test code
        code = """
        SECURE
            ALLOCATE MEMORY FOR EXECUTION END
            ESTABLISH RESISTANT INTEGER x AS 10 END
            ESTABLISH INTEGER y AS 20 END
            CALCULATE ADD WITH x AND y STORE IN z END
            TRANSMIT z TO CONSOLE END
            
            SECURE
                TRANSMIT "Attempting to change resistant variable x..." TO CONSOLE END
                ESTABLISH INTEGER x AS 50 END
            OTHERWISE
                TRANSMIT "FAILED: Variable x is resistant to change." TO CONSOLE END
            END
            
            DEALLOCATE MEMORY END
        OTHERWISE
            TRANSMIT "CRITICAL SYSTEM FAILURE" TO CONSOLE END
        END
        """
        run_code(code)
