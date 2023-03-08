<template>
  <div class="home">
    <formComponent />
  </div>
</template>

<script>
// @ is an alias to /src
import formComponent from "@/components/form-component.vue";

export default {
  name: "HomeView",
  components: {
    formComponent,
  },
};
</script>
