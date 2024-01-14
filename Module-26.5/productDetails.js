const loadProductDetails = () => {
    const params = new URLSearchParams(window.location.search).get("id");
  fetch(`https://fakestoreapi.com/products/${params}`)
    .then((res) => res.json())
    .then((data) => {
      displayProductDetail(data);
    });
};

const displayProductDetail = (product) => {
    console.log(product)
    const parent=document.getElementById("products")
    parent.innerHTML = `
        <div class="col-md-4">
            <img src="${product.image}" class="img-fluid w-75 m-auto" alt="">
        </div>
        <div class="col-md-8">
            <h2>Name: ${product.title}</h2>
            <h3>Price: ${product.title}</h3>
            <p>Description:${product.description} <br/>
            <button class="btn btn-primary">Buy Now</button>
        </div>
    `;

}

loadProductDetails()