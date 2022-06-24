<template>
    <section id="HeaderNavSection">
        <nav>
            <ul class="header_ul">
                <div class="logo_banner_ctnr">
                    <img
                        id="kai_logo"
                        src="@/assets/images/icons/kaiyote1.svg"
                        alt="Kaiyote Moon Logo"
                    >
                    <h3>
                        Kaiyote Moon
                    </h3>
                </div>
                <div class="main_links">
                    <MainLinks/>
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
export default{
    methods: {
        handleArchiveLink() {
            let archive_section = document.querySelector("#PoemArchive");
            archive_section.style.display = "block";
        },
        toggleHiddenMenu(event) {
            let hidden_nav = document.querySelector('#HiddenNavSection');
            let menu_icon = document.querySelector('#menu_icon');
            let close_icon = document.querySelector('#close_icon');
            if (event.target===menu_icon){
                hidden_nav.style.display = 'block';
                menu_icon.style.display = 'none';
                close_icon.style.display = 'block';
            } else {
                hidden_nav.style.display = 'none';
                menu_icon.style.display = 'block';
                close_icon.style.display = 'none';
            }
        }
    },
    components: { HiddenNav, MainLinks }
}

</script>


<style lang="scss">
@import '@/assets/scss/navbars/HeaderNav.scss';
</style>