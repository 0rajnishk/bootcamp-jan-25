<template>
    <div class="home">
        <h1>Bootcamp App Dev</h1>
        <div>
            <p>
                <RouterLink to="/login">Login</RouterLink>
            </p>
            <p>
                <RouterLink to="/signup">Sign Up</RouterLink>
            </p>
        </div>
    </div>
</template>

<script setup>
// No script needed for this basic setup
</script>

<style scoped>
.home {
    text-align: center;
    margin-top: 50px;
}

h1 {
    font-size: 2rem;
    margin-bottom: 20px;
}

p {
    margin: 10px 0;
}

a {
    text-decoration: none;
    color: #42b983;
    font-weight: bold;
}
</style>
