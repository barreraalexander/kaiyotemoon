<script setup>
import HeaderNav from '@/components/navbars/HeaderNav.vue';
import FooterNav from '@/components/navbars/FooterNav.vue';
import HiddenNav from '@/components/navbars/HiddenNav.vue';
</script>

<template>
  <section id="MainAppSection">
    <HeaderNav/>
    <HiddenNav/>
    <main>
      <router-view/>
    </main>
    <FooterNav v-show="false"/>
  </section>
</template>

<style lang="scss">
@import "@/assets/scss/base/base.scss";
@import "@/assets/scss/base/typography.scss";
</style>
