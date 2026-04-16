# JavaScript Notes

## Variables
- var → old way, avoid using
- let → use for variables that change
- const → use for variables that don't change

## Data Types
- String → "Hello"
- Number → 42
- Boolean → true / false
- Array → [1, 2, 3]
- Object → {name: "John", age: 25}

## Functions
```js
function greet(name) {
  return "Hello " + name;
}
```

## Array Methods
- push() → add to end
- pop() → remove from end
- map() → loop and transform
- filter() → loop and filter
- find() → find one item

## Conditions
```js
if (age > 18) {
  console.log("Adult");
} else {
  console.log("Minor");
}
```

## Loops
```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```