<template>
    <div class="border rounded bg-danger shadow p-4">
        The new value is: {{ name }}
        <div>
            <input class="form-control" v-model="name">
            <button class="btn btn-sm btn-success mt-3">Save</button>
        </div>
    </div>
</template> 

<script>
    export default {
        data() {
            return {
                name: ""
            }
        },
        methods: {
            async saveNewName() {
                // ajax request with new name put
            }
        }
    }
</script>
