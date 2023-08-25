<template>
    <v-snackbar
      :timeout="2000"
      v-model="showSnackbar"
    >
      {{ message }}
    </v-snackbar>
</template>
<style>
</style>
<script>
 import { ref } from 'vue';

export default {
    props: {
        timeout: {
        type: Number,
        default: 2000,
        },
    },
    emits: ['update:showSnackbar'],
    // eslint-disable-next-line no-unused-vars
    setup(props) {
        const showSnackbar = ref(false);
        const message = ref('');
        return {
            showSnackbar,
            message,
        };
    },
    };
</script>