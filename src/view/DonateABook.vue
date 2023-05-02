<template>
  <multi-step-form :type="donation"></multi-step-form>
</template>

<script>
import MultiStepForm from "@/components/preview/MultiStepForm.vue";
export default {
  components: {
    MultiStepForm,
  },
  data: () => {
    return {
      donation: [
        {
          isSelling: false,
          typeofAction: "doar",
          congratTextMain:
            "Nós do Obes juntamente com as instituições agradecemos a sua doação! ",
          congratTextUnder:
            "Você receberá um e-mail quando alguma instituição solicitar a doação. Atente-se ao seu telefone e realize a entrega com responsabilidade!",
        },
      ],
    };
  },
};
</script>

<style scoped>
body {
  background-color: #e9dffc;
}
</style>
