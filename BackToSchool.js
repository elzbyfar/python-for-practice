//USE THIS FILE TO CODE YOUR ANSWERS TO THE QUESTIONS

//Test data for the problems
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

// Prompt 1 : cartPrice
function cartPrice(items){
  let total = 0;
  for(let i=0; i <items.length;i++){
    let item = items[i];
     total = total + item.price}
     return total}
// Prompt 2 : mostExpensiveItemName
function mostExpensiveItemName(items){
  let name = '';
  let maxPrice = 0;
  for(i=0; i < items.length; i++){
    if (items[i].price > maxPrice){
      maxPrice = items[i].price;
      name = items[i].itemName;
    }
  }
  return name
}
// Prompt 3 : priceLookup
function priceLookup(items, string){
  for(i=0; i < items.length; i++){
    if(items[i].itemName === string){
      return items[i].price
}
}
console.log(string);
  }



//This is to run the tests. You can ignore it but don't delete it!
require('./BackToSchool.test.js');(void 0);
