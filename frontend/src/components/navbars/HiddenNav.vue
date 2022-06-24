<script setup>
// import '@/components/pieces/ArchiveList.vue'
import ArchiveList from '@/components/pieces/ArchiveList.vue';
import MainLinks from '../pieces/MainLinks.vue';
</script>

<template>
    <section id="HiddenNavSection">
        <h2>
            Archive
        </h2>
        <ul class="hidden_nav_main_links">
            <MainLinks/>
        </ul>
        <ArchiveList/>
    </section>
</template>

<style lang="scss">
@import "@/assets/scss/navbars/HiddenNav.scss";
</style>