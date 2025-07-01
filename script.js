function generatePassword() {
  const lengthInput = document.getElementById("length");
  const useDigits = document.getElementById("digits").checked;
  const useLetters = document.getElementById("letters").checked;
  const useSymbols = document.getElementById("symbols").checked;

  let length = parseInt(lengthInput.value);
  if (isNaN(length) || length < 4) {
    alert("La longueur doit être un nombre supérieur ou égal à 4.");
    return;
  }

  let characters = "";
  if (useDigits) characters += "0123456789";
  if (useLetters) characters += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (useSymbols) characters += "!@#$%^&*()_+-=[]{}|;:',.<>?";

  if (characters.length === 0) {
    alert("Veuillez sélectionner au moins un type de caractère.");
    return;
  }

  let password = "";
  for (let i = 0; i < length; i++) {
    password += characters.charAt(Math.floor(Math.random() * characters.length));
  }

  document.getElementById("result").textContent = password;
}
