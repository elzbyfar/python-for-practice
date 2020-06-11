Back to School Shopping
The beginning of the new school year is fast approaching. To get ready, let's create a few functions to analyze a shopping cart.

Example data set
The functions and tests will use a data set like this one: an array of item objects. The objects will have the these keys, but there might be more of them, and they might have different values.

let items = [
  {
    itemName: "Effective Programming Habits",
    type: "book",
    price: 13.99
  },
  {
    itemName: "Creation 3005",
    type: "computer",
    price: 299.99
  },
  {
    itemName: "Finding Your Center",
    type: "book",
    price: 15.00
  }
]
let items = [
  {
    itemName: "Effective Programming Habits",
    type: "book",
    price: 13.99
  },
  {
    itemName: "Creation 3005",
    type: "computer",
    price: 299.99
  },
  {
    itemName: "Finding Your Center",
    type: "book",
    price: 15.00
  }
]
Problem 1 - Cart Price
Create a function called cartPrice to find the total cost of all the items in the list. The function should accept the array of items and return the total cost of the items as a number.

cartPrice(items) //=> 328.98
cartPrice(items) //=> 328.98
Problem 2 - Most Expensive Item Name
Create a function called mostExpensiveItemName to find the most expensive item. The function should accept the array of items as a parameter and return the name of the most expensive item.

mostExpensiveItemName(items) //=> "Creation 3005"
mostExpensiveItemName(items) //=> "Creation 3005"
Problem 3 - Lookup a Price
Create a function called priceLookup to find the price of a single item. The function should accept the array of items and an item name (string) as parameters, and return the price of the item with that name. If the item cannot be found, return the string "No item found with that name".

priceLookup(items, "Effective Programming Habits") //=> 13.99
priceLookup(items) //=> "No item found with that name"