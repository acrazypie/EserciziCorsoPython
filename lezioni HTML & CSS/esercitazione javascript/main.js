const title = document.getElementById("title");
const helloBtn = document.getElementById("hello-btn");
const out = document.getElementById("out");
const toggleBtn = document.getElementById("toggle-theme");

helloBtn.addEventListener("click", () => {
  out.innerText = "Hai cliccato " + new Date().toLocaleTimeString();
});

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

const dec = document.querySelector("#dec");
const inc = document.querySelector("#inc");
const reset = document.querySelector("#reset");
const count = document.querySelector("#count");
let counter = 0;

const renderCount = () => {
  count.innerText = String(counter);
};

dec.addEventListener("click", () => {
  counter--;
  renderCount();
});

inc.addEventListener("click", () => {
  counter++;
  renderCount();
});

reset.addEventListener("click", () => {
  counter = 0;
  renderCount();
});

const form = document.querySelector("#signup");
const formMsg = document.querySelector("#formMsg");

form.addEventListener("submit", (e) => {
  const email = document.querySelector("#email").value;
  const password = document.querySelector("#pwd").value;

  if (!email.includes("@")) {
    formMsg.innerText = "Email non valida.";
    return;
  }

  if (password.length < 6) {
    formMsg.innerText = "Password troppo corta.";
    return;
  }

  if (!password.match(/[A-Z]/)) {
    formMsg.innerText = "Almeno una lettera maiuscola.";
    return;
  }

  formMsg.innerText = `Registrazione avvenuta! Benvenuto ${email}`;
  form.reset();
});

const dogBtn = document.querySelector("#loadDog");
const dog = document.querySelector("#dog");

async function fetchDogImage() {
  try {
    dogBtn.disabled = true;
    dogBtn.innerText = "Caricamento...";
    const res = await fetch("https://dog.ceo/api/breeds/image/random");

    if (!res.ok) {
      throw new Error("Errore nel caricamento.");
    }

    const data = await res.json();
    dog.src = data.message;
  } catch (err) {
    alert("Si e verificato un errore");
    console.error(err);
  } finally {
    dogBtn.disabled = false;
    dogBtn.innerText = "Nuova foto 🐶";
  }
}

dogBtn.addEventListener("click", fetchDogImage);
