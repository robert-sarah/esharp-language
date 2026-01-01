# E# (E-Sharp) – Modern & Powerful Programming Language

E# is a modern, high-level programming language designed for clarity, power, and safety. It combines the simplicity of Python with the rigor of C#.

## Features
- **Clarity**: Simple and readable syntax.
- **Power**: Supports Object-Oriented, Functional, and Procedural programming.
- **Safety**: Static but flexible typing.
- **Versatility**: Suitable for web, apps, games, and scripting.

## Quick Start

### Variables and Types
```e_sharp
let age: int = 12;
let name: string = "Levi";
const pi: float = 3.14;
```

### Functions
```e_sharp
function greet(name: string): string {
    return "Hello, " + name + "!";
}
```

### Classes
```e_sharp
class Person {
    let name: string;
    let age: int;

    function init(name: string, age: int) {
        self.name = name;
        self.age = age;
    }

    function greet(): string {
        return "Hi, I'm " + self.name;
    }
}
```

### Lambdas
```e_sharp
let square = (x: int) => x * x;
```

## Running E#
The E# interpreter is written in Python.
```bash
python3 esharp.py main.es
```

## License
MIT License
