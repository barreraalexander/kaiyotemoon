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
                    data-status="hidden"
                    src="@/assets/images/icons/close.svg"
                    alt=""
                    @click="toggleHiddenMenu($event)"
                >
            </ul>
        </nav>
    </section>
</template>

<script>
import gsap from 'gsap';

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

            let menu_timeline = gsap.timeline({
                // paused: true
            })

            menu_timeline.to(
                hidden_nav,
                {
                    duration: .1,
                    opacity: 1,
                    display: 'block',
                    // ease: easeInOut,

                }
            )

            menu_timeline.to(
                menu_icon,
                {
                    duration: .1,
                    opacity: 0,
                    display: 'none',
                    // ease: Sine.easeInOut,
                }
            )

            menu_timeline.to(
                close_icon,
                {
                    duration: .1,
                    opacity: 1,
                    display: 'block'
                }
            )


            if (event.target===menu_icon){
                menu_timeline.play()
                // hidden_nav.dataset.status = ''
                // menu_icon.dataset.status = 'hidden';
                // close_icon.dataset.status = '';
                // alert('this')
            } else {
                menu_timeline.reverse()
                // alert('running')
                // hidden_nav.dataset.status = 'hidden'
                // menu_icon.dataset.status = '';
                // close_icon.dataset.status = 'hidden';
            }
        }

    },
    components: {MainLinks}
}

</script>


<style lang="scss">
@import '@/assets/scss/navbars/HeaderNav.scss';
</style>