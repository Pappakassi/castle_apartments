document.addEventListener("DOMContentLoaded", function () {
  const typeSelect = document.querySelector('select[name="type"]');
  const creditSection = document.querySelector('#credit-fields');
  const bankSection = document.querySelector('#bank-fields');
  const mortgageSection = document.querySelector('#mortgage-fields');

  function disableInputs(section, shouldDisable) {
    if (!section) return;
    const inputs = section.querySelectorAll('input, select, textarea');
    inputs.forEach(input => input.disabled = shouldDisable);
  }

  function toggleForms() {
    const selected = typeSelect.value;

    creditSection.style.display = selected === "credit_card" ? "block" : "none";
    bankSection.style.display = selected === "bank_transfer" ? "block" : "none";
    mortgageSection.style.display = selected === "mortgage" ? "block" : "none";

    disableInputs(creditSection, selected !== "credit_card");
    disableInputs(bankSection, selected !== "bank_transfer");
    disableInputs(mortgageSection, selected !== "mortgage");
  }

  if (typeSelect) {
    typeSelect.addEventListener("change", toggleForms);
    toggleForms(); // initialize on load
  }
});
