$(document).ready(function () {
  // Agregar cámara (Modal)
  $("#btnAddCam").on("click", function () {
    $.ajax({
      url: "/cameras/modal_new/",
      type: "GET",
      success: function (response) {
        $("#modal-section").addClass("modal-on");
        $("#modal-section").html(response);
      },
      error: function (xhr, status, error) {
        console.error("Error en la solicitud AJAX:", status, error);
      },
    });
  });

  // Elimnar cámara (Modal)
  $("#btnRemoveCam").on("click", function () {
    $.ajax({
      url: "/cameras/modal_remove/",
      type: "GET",
      success: function (response) {
        $("#modal-section").addClass("modal-on");
        $("#modal-section").html(response);
      },
      error: function (xhr, status, error) {
        console.error("Error en la solicitud AJAX:", status, error);
      },
    });
  });

  // Delegación de eventos para cerrar modales
  $(document).on("click", "#btnCloseModal", function () {
    $("#modal-section").removeClass("modal-on").html("");
  });
});
