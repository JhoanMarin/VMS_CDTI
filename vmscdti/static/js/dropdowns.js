//Dropdowns
const bloquesItem = document.querySelectorAll("#menuSidebar .item-dp");

bloquesItem.forEach((item) => {
  item.addEventListener("click", (e) => {
    // Primero, eliminamos el color de fondo de todos los elementos
    bloquesItem.forEach((i) => {
      i.classList.remove("open-dp");
    });

    // Luego, aplicamos el color de fondo solo al elemento clicado
    item.classList.add("open-dp");
  });
});