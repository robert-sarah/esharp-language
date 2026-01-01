import math;

class Calculator {
    function add(a: int, b: int): int { return a + b; }
    function sub(a: int, b: int): int { return a - b; }
    function sqrt(a: float): float { return math.sqrt(a); }
}

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

// Main execution
let levi = Person("Levi", 12);
print(levi.greet());

let calc = Calculator();
print(calc.add(5, 3));   // 8
print(calc.sqrt(16.0));  // 4.0

let square = (x: int) => x * x;
print(square(4)); // 16
