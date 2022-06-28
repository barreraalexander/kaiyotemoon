<script setup>
// import '@/components/pieces/ArchiveList.vue'
import ArchiveList from '@/components/pieces/ArchiveList.vue';
import MainLinks from '../pieces/MainLinks.vue';
</script>

<template>
    <section id="HiddenNavSection">
        <div class="hidden_nav_ctnr">
            <div class="empty">                
            </div>
            <div class="navigation_ctnr">
                <h2>
                        Navigate
                </h2>
                <ul class="hidden_nav_main_links">
                    <MainLinks/>
                </ul>
                <ArchiveList/>
            </div>
        </div>
    </section>
</template>

<style lang="scss">
@import "@/assets/scss/navbars/HiddenNav.scss";
</style>