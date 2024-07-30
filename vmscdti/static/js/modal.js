const btnAddCam = document.getElementById("btnAddCam");
const btnRemoveCam = document.getElementById("btnRemoveCam");
const modalSection = document.querySelector(".modal-section");
const body = document.querySelector("body");

function showModal(type) {
  modalSection.innerHTML = "";
  body.classList.add("static-body");
  modalSection.classList.add("modal-on");

  if (type === "add") createAddCamModal(); 
}

function createAddCamModal () {
    const formAddCam = document.createElement("form");
    formAddCam.classList.add("form-modal");

    const header = document.createElement("header");
    header.classList.add("header-modal");



    const tituloHeader = document.createElement("div");
    tituloHeader.classList.add("title-header");
    tituloHeader.textContent = "Agregar cámara";

    header.appendChild(tituloHeader);

    formAddCam.appendChild(header);

    modalSection.appendChild(formAddCam);
}

btnAddCam.addEventListener("click", () => {
  showModal('add');
});

btnRemoveCam.addEventListener("click", () => {
  showModal();
});
