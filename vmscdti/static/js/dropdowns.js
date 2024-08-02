$(document).ready(function() {
  // Selecciona los elementos usando jQuery
  const $bloquesItem = $("#menuSidebar .item-dp");

  // Añade el evento click utilizando jQuery
  $bloquesItem.on("click", function() {
      const $item = $(this);

      // Si el elemento clicado ya tiene la clase "open-dp"
      if ($item.hasClass("open-dp")) {
          // Eliminamos la clase "open-dp" de todos los elementos
          $bloquesItem.removeClass("open-dp");
      } else {
          // Primero, eliminamos la clase "open-dp" de todos los elementos
          $bloquesItem.removeClass("open-dp");

          // Luego, aplicamos la clase "open-dp" solo al elemento clicado
          $item.addClass("open-dp");
      }
  });
});

