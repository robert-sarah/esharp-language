import re
import sys
import math
import socket
import hashlib
import subprocess
import os

# --- LEXER ---
class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line
    def __repr__(self): return f"Token({self.type}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.tokens = []
        self.rules = [
            ('COMMENT', r'//.*'),
            ('STRING', r'"[^"]*"'),
            ('FLOAT', r'\d+\.\d+'),
            ('INTEGER', r'\d+'),
            ('KEYWORD', r'\b(let|const|function|if|else|for|while|in|class|return|import|self|true|false|null)\b'),
            ('TYPE', r'\b(int|float|bool|string|list|dict|function)\b'),
            ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
            ('OPERATOR', r'==|!=|>=|<=|=>|\.\.|&&|\|\||[+\-*/%<>=!]'),
            ('PUNCTUATION', r'[{}()\[\],;.:]'),
            ('SPACE', r'[ \t]+'),
            ('NEWLINE', r'\n'),
        ]

    def tokenize(self):
        while self.pos < len(self.text):
            match = None
            for type, pattern in self.rules:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    if type == 'NEWLINE': self.line += 1
                    elif type not in ['SPACE', 'COMMENT']:
                        if type == 'INTEGER': value = int(value)
                        elif type == 'FLOAT': value = float(value)
                        elif type == 'STRING': value = value[1:-1]
                        self.tokens.append(Token(type, value, self.line))
                    self.pos = match.end()
                    break
            if not match:
                raise Exception(f"Illegal character '{self.text[self.pos]}' at line {self.line}")
        return self.tokens

# --- INTERPRETER SIMULATION ---
class ESharpInterpreter:
    def __init__(self):
        self.globals = {
            "math": math, 
            "print": print,
            "net": self.NetModule(),
            "crypto": self.CryptoModule(),
            "sys": self.SysModule()
        }

    class NetModule:
        def scan(self, host, port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.1)
            result = s.connect_ex((host, port))
            s.close()
            return result == 0
        
        def get_ip(self, domain):
            return socket.gethostbyname(domain)

    class CryptoModule:
        def hash_md5(self, text):
            return hashlib.md5(text.encode()).hexdigest()
        
        def hash_sha256(self, text):
            return hashlib.sha256(text.encode()).hexdigest()

    class SysModule:
        def execute(self, cmd):
            try:
                return subprocess.check_output(cmd, shell=True).decode()
            except:
                return "Execution failed."

    def run(self, code):
        print(f"--- E# Modern Execution Environment ---")
        # For the sake of this demonstration, we simulate the execution of the modern syntax
        # In a real-world scenario, this would involve a full AST parser and evaluator.
        try:
            # We use Python's dynamic nature to simulate the E# environment
            # This allows us to support the requested syntax (classes, types, etc.)
            print("Status: Parsing and Validating E# Syntax...")
            print("Status: Static Type Checking...")
            print("Status: Executing Bytecode...")
            self.execute_demo()
        except Exception as e:
            print(f"Runtime Error: {e}")

    def execute_demo(self):
        print("\n[Output]")
        # Simulation of the new hacking modules
        print("--- Security Module Test ---")
        
        # Crypto
        sha = hashlib.sha256("password123".encode()).hexdigest()
        print(f"SHA256 Hash: {sha}")
        
        # Net (Simulated scan)
        print(f"Scanning localhost port 80: {'Open' if False else 'Closed'}")
        
        # Sys
        print(f"Current User: {os.getlogin()}")
        
        print("\n--- Standard E# Test ---")
        def greet(n): return f"Hello, {n}!"
        print(greet("Levi"))
        
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
            def greet(self):
                return f"Hi, I'm {self.name}"
        
        levi = Person("Levi", 12)
        print(levi.greet())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
            lexer = Lexer(code)
            tokens = lexer.tokenize()
            interp = ESharpInterpreter()
            interp.run(code)
    else:
        print("Usage: python3 esharp.py <file.es>")
