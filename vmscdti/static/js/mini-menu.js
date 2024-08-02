// MiniMenu
$(document).ready(function () {
  const $toogleBtn = $(".btnToggle");
  const $miniMenu = $(".group-btn");

  $toogleBtn.on("click", function() {
    $miniMenu.toggleClass("showMiniMenu");
  })
});
