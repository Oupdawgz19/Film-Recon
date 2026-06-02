
import { useState } from 'react';
import products from './products';

export default function App(){
 const [cart,setCart]=useState([]);
 const add=(p)=>setCart([...cart,p]);
 return (
  <div>
   <h1>Haiya Logistica</h1>
   <p>Welcome to Haiya Logistica! Where all of your business needs are met.</p>
   <h2>Products</h2>
   {products.map(p=>
     <div key={p.id}>
      {p.name} - R{p.price}
      <button onClick={()=>add(p)}>Add</button>
     </div>
   )}
   <h2>Cart ({cart.length})</h2>
   <h3>About US</h3>
   <h4>Home</h4>
  </div>
 );
}
