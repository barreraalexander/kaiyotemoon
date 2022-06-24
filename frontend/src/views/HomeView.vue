<script setup>
import PoemDisplay from "@/components/sections/PoemDisplay.vue";
import PoemArchive from "@/components/sections/PoemArchive.vue";

</script>

<template>
  <section id="HomeViewSection">
    <div class="homeview_subdivision">
      <PoemArchive/>
      <PoemDisplay/>
    </div>
  </section>
</template>

<style lang="scss">
@import '@/assets/scss/views/HomeView.scss';
</style>