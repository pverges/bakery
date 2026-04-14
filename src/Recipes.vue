<template>
  <div class="recipes-page">
    <header class="header">
      <h1 class="logo">Vergés <span class="logo-sub">Recipes</span></h1>
      <nav class="nav">
        <a href="/" class="nav-link">Store</a>
      </nav>
    </header>

    <section class="intro">
      <p>Private recipe collection. Not indexed for SEO.</p>
    </section>

    <section class="recipe-list">
      <div v-for="product in products" :key="product.id" class="recipe-card">
        <div class="recipe-header">
          <h2 class="recipe-name">{{ product.name }}</h2>
          <span class="recipe-category">{{ product.category }}</span>
        </div>
        
        <div class="recipe-section">
          <h3>Ingredients</h3>
          <ul>
            <li v-for="(ingredient, index) in product.ingredients" :key="index">
              {{ ingredient }}
            </li>
          </ul>
        </div>

        <div class="recipe-section">
          <h3>Execution Details</h3>
          <p class="placeholder-text">[Add execution steps for {{ product.name }}]</p>
        </div>

        <div class="recipe-section">
          <h3>Cost Breakdown</h3>
          <table class="cost-table">
            <tr>
              <td>Flour</td>
              <td>$--</td>
            </tr>
            <tr>
              <td>Butter</td>
              <td>$--</td>
            </tr>
            <tr>
              <td>Other ingredients</td>
              <td>$--</td>
            </tr>
            <tr class="total">
              <td>Total cost</td>
              <td>$--</td>
            </tr>
          </table>
        </div>

        <div class="recipe-section">
          <h3>Pricing</h3>
          <div class="pricing-grid">
            <div class="pricing-item">
              <span class="label">Selling price</span>
              <span class="value">${{ product.price }}</span>
            </div>
            <div class="pricing-item">
              <span class="label">Cost</span>
              <span class="value">$--</span>
            </div>
            <div class="pricing-item">
              <span class="label">Margin</span>
              <span class="value">--%</span>
            </div>
          </div>
        </div>

        <div class="recipe-section">
          <h3>Notes</h3>
          <p class="placeholder-text">[Add notes for {{ product.name }}]</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import productsData from './data/products.json'

export default {
  name: 'Recipes',
  data() {
    return {
      products: productsData.products
    }
  }
}
</script>

<style scoped>
.recipes-page {
  min-height: 100vh;
  background: var(--bg);
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 4rem;
  border-bottom: 1px solid var(--border);
}

.logo {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 500;
}

.logo-sub {
  font-weight: 300;
  color: var(--text-light);
  margin-left: 0.5rem;
}

.nav-link {
  font-size: 0.875rem;
  color: var(--text-light);
  text-decoration: none;
}

.intro {
  text-align: center;
  padding: 1.5rem;
  font-size: 0.75rem;
  color: var(--text-light);
  background: rgba(196, 167, 125, 0.1);
}

.recipe-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 2rem;
  padding: 2rem 4rem 4rem;
  max-width: 1400px;
  margin: 0 auto;
}

.recipe-card {
  background: white;
  border-radius: 8px;
  padding: 2rem;
  box-shadow: var(--shadow);
}

.recipe-header {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 1.5rem;
  padding-bottom: 1rem;
  border-bottom: 1px solid var(--border);
}

.recipe-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
}

.recipe-category {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-light);
}

.recipe-section {
  margin-bottom: 1.5rem;
}

.recipe-section h3 {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-light);
  margin-bottom: 0.75rem;
}

.recipe-section ul {
  list-style: none;
  padding-left: 0;
}

.recipe-section li {
  font-size: 0.875rem;
  padding: 0.25rem 0;
  border-bottom: 1px dashed var(--border);
}

.placeholder-text {
  font-size: 0.875rem;
  color: var(--text-light);
  font-style: italic;
}

.cost-table {
  width: 100%;
  font-size: 0.875rem;
}

.cost-table tr {
  border-bottom: 1px dashed var(--border);
}

.cost-table td {
  padding: 0.5rem 0;
}

.cost-table td:last-child {
  text-align: right;
}

.cost-table .total {
  font-weight: 500;
  border-bottom: 2px solid var(--text);
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.pricing-item {
  text-align: center;
  padding: 1rem;
  background: var(--bg);
  border-radius: 4px;
}

.pricing-item .label {
  display: block;
  font-size: 0.625rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--text-light);
  margin-bottom: 0.25rem;
}

.pricing-item .value {
  font-family: 'Playfair Display', serif;
  font-size: 1.25rem;
}

@media (max-width: 768px) {
  .header {
    padding: 1.5rem 2rem;
  }
  
  .recipe-list {
    grid-template-columns: 1fr;
    padding: 2rem;
  }
}</style>