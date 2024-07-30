// MiniMenu
const toogleBtn = document.querySelector(".btnToggle");
const miniMenu = document.querySelector(".group-btn");

toogleBtn.addEventListener("click", (e) => {
  miniMenu.classList.toggle("showMiniMenu");
});