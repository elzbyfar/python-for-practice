let items = [
	{
		itemName: 'Effective Programming Habits',
		type: 'book',
		price: 13.99
	},
	{
		itemName: 'Creation 3005',
		type: 'computer',
		price: 299.99
	},
	{
		itemName: 'Finding Your Center',
		type: 'book',
		price: 15.0
	}
];

// const mostExpensiveName = (items) => {
//   let maxPrice = 0
//   let name = ''
//   for (let i=0;i<items.length; i++) {
//     if (items[i].price > maxPrice) {
//       maxPrice = items[i].price
//       name = items[i].itemName
//     }
//   }
//   return name
// }

// const priceLookup = (items, name) => {
//   for (let i=0; i<items.length; i++) {
//     if (items[i].itemName === name) {
//       return items[i].price
//     }
//   }
// }

function priceLookup(items, string) {
	for (i = 0; i < items.length; i++) {
		if (items[i].itemName === string) {
			return items[i].price;
		} else {
			return 'No item found with that name';
		}
	}
}

console.log(priceLookup(items, 'Effective Programming Habit'));
