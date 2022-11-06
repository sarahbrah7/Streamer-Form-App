<template>
  <div>
    HELLO WORLD {{ name }}
    <div>{{ counter }}</div>
    <button @click="counter++">Increment</button>
  </div>
</template>

<script>
export default{
  data() {
    return {
      name: "TITLE",
      counter: 0,
    }
  }
}
</script>
