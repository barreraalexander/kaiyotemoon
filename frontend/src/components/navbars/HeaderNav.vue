<template>
    <section id="HeaderNavSection">
        <nav>
            <ul>
                <img
                    id="kai_logo"
                    src="@/assets/images/icons/kaiyote1.svg"
                    alt="Kaiyote Moon Logo"
                >
                <h3>
                    Kaiyote Moon
                </h3>
                <div class="main_links">
                    <MainLinks/>
                    <!-- <a id="archive_link" @click="handleArchiveLink">Archive</a> -->
                </div>
                <img
                    id="menu_icon"
                    src="@/assets/images/icons/menu.svg"
                    alt="Hidden Menu Icon"
                    @click="toggleHiddenMenu($event)"
                >
                <img
                    id="close_icon"
                    src="@/assets/images/icons/close.svg"
                    alt=""
                    @click="toggleHiddenMenu($event)"
                >
            </ul>
        </nav>
        <HiddenNav/>
    </section>
</template>

<script>
import HiddenNav from "@/components/navbars/HiddenNav.vue";
import MainLinks from "@/components/pieces/MainLinks.vue";
var showing_menu = false;
export default{
    methods: {
        handleArchiveLink() {
            let archive_section = document.querySelector("#PoemArchive");
            archive_section.style.display = "block";
        },
        toggleHiddenMenu() {
            let hidden_nav = document.querySelector('#HiddenNavSection');
            hidden_nav.style.display = 'block';
            if (showing_menu){
                hidden_nav.style.display = 'none';
                showing_menu = false;
            } else  {
                showing_menu = true;
            }
        }
    },
    components: { HiddenNav, MainLinks }
}

</script>


<style lang="scss">
@import '@/assets/scss/navbars/HeaderNav.scss';
</style>