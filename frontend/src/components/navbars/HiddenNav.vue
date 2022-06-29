<script setup>
// import '@/components/pieces/ArchiveList.vue'
import ArchiveList from '@/components/pieces/ArchiveList.vue';
import MainLinks from '@/components/pieces/MainLinks.vue';
import SearchBar from '@/components/pieces/SearchBar.vue';
</script>

<template>
    <section id="HiddenNavSection" data-status='hidden'>
        <div class="hidden_nav_ctnr">
            <div class="navigation_ctnr">
                <ul class="hidden_nav_main_links">
                    <MainLinks/>
                    <SearchBar/>
                </ul>
                <ArchiveList v-show="false"/>
            </div>
        </div>
    </section>
</template>


<script>

// let archive_link = document.querySelector('#mainlinks_archive')
// console.log(archive_link)


</script>

<style lang="scss">
@import "@/assets/scss/navbars/HiddenNav.scss";
</style>