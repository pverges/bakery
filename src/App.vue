<template>
  <div class="app">
    <header class="header">
      <h1 class="logo">Vergés</h1>
      <nav class="nav">
        <a href="/recipes.html" class="nav-link">Recipes</a>
      </nav>
    </header>

    <section class="hero">
      <h2 class="hero-title">Fresh every Saturday at 11am</h2>
      <p class="hero-subtitle">Order by {{ bakery.orderDeadline }}</p>
    </section>

    <section class="products">
      <div v-for="category in categories" :key="category.name" class="category-section">
        <h2 class="category-title">{{ category.name }}</h2>
        <div class="products-grid">
          <div v-for="product in productsByCategory(category.key)" :key="product.id" class="product-card">
            <div class="product-image">
              <img :src="product.image" :alt="product.name" />
            </div>
            <div class="product-info">
              <h3 class="product-name">{{ product.name }}</h3>
              <p class="product-ingredients">{{ product.ingredients.join(', ') }}</p>
              <div class="product-tags">
                <span 
                  v-for="tag in product.tags" 
                  :key="tag" 
                  class="tag"
                  :class="tag"
                >
                  {{ tag }}
                </span>
              </div>
              <div class="product-footer">
                <span class="product-price">${{ product.price }}</span>
                <a :href="googleFormUrl" class="order-btn" target="_blank">Pre-order</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <footer class="footer">
      <p>Saturday pickup at 11am</p>
    </footer>
  </div>
</template>

<script>
import productsData from './data/products.json'

export default {
  name: 'App',
  data() {
    return {
      products: productsData.products,
      bakery: productsData.bakery,
      categories: [
      { name: 'Breads', key: 'bread' },
      { name: 'Cookies', key: 'cookie' },
      { name: 'Tarts', key: 'tart' }
    ],
      googleFormUrl: 'YOUR_GOOGLE_FORM_URL_HERE'
    }
  },
  mounted() {
    console.log('Products:', this.products)
    console.log('Categories:', this.categories)
  },
  methods: {
    productsByCategory(category) {
      const cat = category.toLowerCase()
      return this.products.filter(p => p.category === cat)
    }
  }
}
</script>