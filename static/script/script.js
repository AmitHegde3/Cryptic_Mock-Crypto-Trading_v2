// Login Pop and close ------------------------------------------------------------------------------------
const wrapper = document.querySelector(".wrapper");

const btnpop = document.querySelector(".btn-login");

const btnclose = document.querySelector(".icon-close");

btnpop.addEventListener("click", () => {
  wrapper.classList.add("active-popup");
});

btnclose.addEventListener("click", () => {
  wrapper.classList.remove("active-popup");
});

// Parallax effect ------------------------------------------------------------------------------------

let text = document.getElementById("text");

window.addEventListener("scroll", () => {
  let value = window.scrollY;

  text.style.marginTop = value * 0.9 + "px";
});
