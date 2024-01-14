const loadCategory = () => {
    fetch("https://fakestoreapi.com/products/categories")
      .then((res) => res.json())
      .then((data) => displayCategory(data));
}

const displayCategory = (categories) => {
    const categoryBtn =document.getElementById("category")
    categories.forEach((category) => {
        const cate = document.createElement("div");
        cate.innerHTML = `
        <button class="btn btn-primary" onClick="loadAllProducts('${category}')">${category}</button>
        `;
        categoryBtn.appendChild(cate);
    })
 }

const loadAllProducts = (name) => {
    if (name) {
        fetch(`https://fakestoreapi.com/products/category/${name}`)
          .then((res) => res.json())
          .then((data) => {
            displayProducts(data);
          });
    }
    else {
        fetch("https://fakestoreapi.com/products")
          .then((res) => res.json())
          .then((data) => {
            displayProducts(data);
          });
    }
}

const displayProducts = (products) => {
    const cardContainer = document.getElementById("all-data");
    cardContainer.innerHTML = "";
    products.forEach((product) => {
        const card = document.createElement("div");
        card.classList.add("col")
        card.innerHTML = `
        <div class="card">
            <img src="${
              product.image
            }" class="card-img-top w-75 m-auto mt-3 img-fluid" 
             style="height: 250px;" alt="..." />
            <div class="card-body">
              <h5 class="card-title">${product.title}</h5>
              <h5 class="card-title">Price: ${product.price}</h5>
              <p class="card-text">
                ${product.description.slice(0, 100)}
              </p>
              <button class="btn btn-warning" onClick="productDetails('${product.id}')">Detail</button>
            </div>
          </div>
        `;
        cardContainer.appendChild(card)
    } )
}
const productDetails = (productId) => {
  window.location.href = `productDetails.html?id=${productId}`;
};
loadAllProducts()
loadCategory()