$(document).ready(function() {
  // Selecciona los elementos usando jQuery
  const $aside = $(".sidebar");
  const $arrowToggle = $(".arrowToggle");
  const $titleSidebar = $(".main-cameras .sidebar header .title h3");

  // Añade el evento click utilizando jQuery
  $arrowToggle.on("click", function() {
      $aside.toggleClass("showSideBar");
      $arrowToggle.toggleClass("rotateArrow");
      $titleSidebar.toggleClass("d-block");
  });
});
