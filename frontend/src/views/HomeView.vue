<script setup>
import PoemDisplay from "@/components/sections/PoemDisplay.vue";
import PoemArchive from "@/components/sections/PoemArchive.vue";

</script>

<template>
  <section id="HomeViewSection">
    <PoemDisplay/>
    <PoemArchive/>
  </section>
</template>

<script>
export default {
  mounted: function displayArchiveLink(){
    let archive_link = document.querySelector('#archive_link');
    archive_link.style.display = "block";
  },
  unmounted: function hideArchiveLink(){
    let archive_link = document.querySelector('#archive_link');
    archive_link.style.display = "none";
  }


}
</script>
