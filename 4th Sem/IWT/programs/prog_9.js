// Copying, passing, and comparing by value
let num1 = 5;
let num2 = num1;
console.log(`num1: ${num1}, num2: ${num2}`); // num1: 5, num2: 5
num1 = 10;
console.log(`num1: ${num1}, num2: ${num2}`); // num1: 10, num2: 5

// Copying, passing, and comparing by reference
let obj1 = {value: 5};
let obj2 = obj1;
console.log(`obj1: ${obj1.value}, obj2: ${obj2.value}`); // obj1: 5, obj2: 5
obj1.value = 10;
console.log(`obj1: ${obj1.value}, obj2: ${obj2.value}`); // obj1: 10, obj2: 10

// References themselves are passed by value
let obj3 = {value: 5};
let obj4;
function changeValue(obj) {
  obj.value = 10;
  obj = {value: 15};
}
changeValue(obj3);
console.log(`obj3: ${obj3.value}`); // obj3: 10
obj4 = obj3;
changeValue(obj4);
console.log(`obj3: ${obj3.value}`); // obj3: 10

