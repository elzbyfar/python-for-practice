//DO NOT MODIFY THIS FILE

const fs = require('fs')
let code = fs.readFileSync('./index.js', 'utf8')
eval(code)

let empty = []
let cart = [
  { itemName: "Effective Programming Habits", type: "book", price: 18.99},
  { itemName: "Creation 3005", type: "computer",price: 399.99},
  { itemName: "Orangebook Pro", type: "computer",price: 899.99},
  { itemName: "Finding Your Center", type: "book", price: 15.00},
  { itemName: "Fabulous Algorithms", type: "book",price: 29.99},
  { itemName: "School Logo Hat", type: "clothes",price: 25.00}
]
let items = [
  {itemName: "Effective Programming Habits", type: "book", price: 13.99 },
  { itemName: "Creation 3005", type: "computer", price: 299.99 },
  { itemName: "Finding Your Center", type: "book", price: 15.00 }
]
let cheapItems = [
  {itemName: "Pencil Case", type: "supplies", price: 2.99 },
  { itemName: "Spiral Notebook", type: "supplies", price: 4.99 },
  { itemName: "Pack of 10 Pencils", type: "supplies", price: 8.20 },
  { itemName: "Ballpoint Pen", type: "supplies", price: 2.20 },
]

test(cartPrice(cart), 1388.96, "Problem 1: cartPrice" )
test(cartPrice(items), 328.98, "Problem 1: cartPrice" )

test(mostExpensiveItemName(cart), "Orangebook Pro", "Problem 2: mostExpensiveItemName")
test(mostExpensiveItemName(items), "Creation 3005", "Problem 2: mostExpensiveItemName")
test(mostExpensiveItemName(cheapItems), "Pack of 10 Pencils", "Problem 2: mostExpensiveItemName")

for (let itemPlace = 0; itemPlace < 5; itemPlace ++) {
  test(priceLookup(cart, cart[itemPlace].itemName), cart[itemPlace].price, "Problem 3: priceLookup")
}
test(priceLookup(cart, "Not an item"), "No item found with that name", "Problem 3: priceLookup")

function test(actual, expected, problem) {
  if(actual === expected){
    console.log(`✅\t${problem} passing`)
  }else{
    console.log(`❌\t${problem} not passing the test. Currently ${problem} is returning:\n${JSON.stringify(actual)}\nit should return:\n${JSON.stringify(expected)}`)
  }
}
