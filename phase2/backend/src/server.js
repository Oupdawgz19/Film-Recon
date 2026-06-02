
const express=require('express');
const app=express();
app.use(express.json());

const products=[
{id:1,name:'FR Coverall',price:899}
];

app.get('/api/products',(req,res)=>res.json(products));

app.get('/api/inventory',(req,res)=>res.json([
 {sku:'FR001',qty:120}
]));

app.post('/api/orders',(req,res)=>{
 res.json({status:'received',order:req.body});
});

app.get('/api/tracking/:id',(req,res)=>{
 res.json({
  orderId:req.params.id,
  status:'Out For Delivery'
 });
});

app.listen(5000,()=>console.log('API running'));
