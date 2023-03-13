// this is just a sample data to ensure that the front end works, replace with data from database
import caixinhua from './assets/caixinhua.jpg';
import thaibasil from './assets/thaibasil.jpg';
import kangkong from './assets/kangkong.jpg';

// fake data
export const products = [{
    id: '1',
    name: 'Cai Xin Hua',
    shelfLife: '2023-12-31',
    price: '2.00',
    quantityInStock: '10',
    imageURL: caixinhua,
}, {
    id: '2',
    name: 'Thai Basil',
    shelfLife: '2023-12-31',
    price: '2.50',
    quantityInStock: '5',
    imageURL: thaibasil,
}, {
    id: '3',
    name: 'Kang Kong',
    shelfLife: '2023-12-31',
    price: '1.50',
    quantityInStock: '20',
    imageURL: kangkong,
}];

// referencing the above products array, fake data for cart
export const cartItems = [
    products[0],
    products[1]
];