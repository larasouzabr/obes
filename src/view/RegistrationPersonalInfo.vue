<template>
  <PersonalData :type="registration"></PersonalData>
</template>

<script>
import PersonalData from "@/components/formRegistrationPersonalInfo/PersonalData.vue";
export default {
  components: {
    PersonalData,
  },
  data: () => {
    return {
      registration: [
        {
          congratTextMain:
            "Nós do Obes juntamente com as instituições agradecemos a sua doação! ",
          congratTextUnder:
            "Você receberá um e-mail quando alguma instituição solicitar a doação. Atente-se ao seu telefone e realize a entrega com responsabilidade!",
        },
      ],
    };
  },
  mounted() {
    document.body.style.background = "#F9F2FF";
  },
};
</script>

<style scoped>
body {
  background-color: #e9dffc;
}
</style>
