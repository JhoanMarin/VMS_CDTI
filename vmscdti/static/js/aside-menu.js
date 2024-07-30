//AsideMenu
const aside = document.querySelector(".sidebar");
const arrowToggle = document.querySelector(".arrowToggle");
const titleSidebar = document.querySelector(
  ".main-cameras .sidebar header .title h3"
);

arrowToggle.addEventListener("click", (e) => {
  aside.classList.toggle("showSideBar");
  arrowToggle.classList.toggle("rotateArrow");
  titleSidebar.classList.toggle("d-block");
});
