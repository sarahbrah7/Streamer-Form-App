<template>
  <div>
    The new value is: {{ name }}
    <div>
      <input class="form-control" v-model="name">
    </div>
  </div>
</template>


<script>
  export default{
    data() {
      return {
        name: ""
      }
    }
  }
</script>

