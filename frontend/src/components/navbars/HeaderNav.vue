
<template>
    <section id="HeaderNavSection">
        <nav>
            <router-link to="/">Home</router-link> |
            <router-link to="/about">About</router-link>
            <a id="archive_link" @click="handleArchiveLink">Archive</a>
        </nav>
    </section>
</template>

<script>
// let archive_link = document.querySelector("#archive_link")
// console.log(archive_link)
export default{
    methods: {
        handleArchiveLink(){
            let archive_section = document.querySelector('#PoemArchive');
            archive_section.style.display = "block"
        }
    },

}

</script>


<style lang="scss">
@import '@/assets/scss/navbars/HeaderNav.scss';
</style>