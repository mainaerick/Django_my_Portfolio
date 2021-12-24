const links = document.querySelectorAll(".nav-item");
const sections = document.querySelectorAll("section");

const section_home = document.getElementById("home");
const section_about = document.getElementById("about_");
const section_contact = document.getElementById("contact");
// const section_experience = document.getElementById("experience");
const section_project = document.getElementById("projects");
const section_skill = document.getElementById("skills");
let activeLink = 0;
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu");
const navLink = document.querySelectorAll(".nav-item");

hamburger.addEventListener("click", mobileMenu);
navLink.forEach((n) => n.addEventListener("click", closeMenu));

function mobileMenu() {
  hamburger.classList.toggle("active");
  navMenu.classList.toggle("active");
}

function closeMenu() {
  hamburger.classList.remove("active");
  navMenu.classList.remove("active");
}

links.forEach((link, i) => {
  link.addEventListener("click", () => {
    if (activeLink != i) {
      links[activeLink].classList.remove("active");
      link.classList.add("active");
      // sections[activeLink].classList.remove("active");
      if (i == 1 || i == 2) {
        document.getElementsByTagName("body")[0].style.overflowY = "auto";
      } else {
        document.getElementsByTagName("body")[0].style.overflowY = "hidden";
      }
      setTimeout(() => {
        activeLink = i;
        if (i == 0) {
          //home menu
          section_home.classList.add("active");
          section_about.classList.remove("active");
          section_contact.classList.remove("active");
          // section_experience.classList.remove("active");
          section_project.classList.remove("active");
          section_skill.classList.remove("active");
          //home
          // sections[1].classList.remove("active");
          // sections[2].classList.remove("active");
          // sections[3].classList.remove("active");
          // sections[4].classList.remove("active");
          // sections[5].classList.remove("active");
          // home link index
          // sections[0].classList.add("active");
        } else if (i == 1) {
          //about menu
          section_about.classList.add("active");
          section_skill.classList.add("active");
          // section_experience.classList.add("active");
          section_home.classList.remove("active");
          section_contact.classList.remove("active");
          section_project.classList.remove("active");
          // //about
          // sections[0].classList.remove("active");
          // sections[4].classList.remove("active");
          // sections[5].classList.remove("active");
          // //about link index
          // sections[1].classList.add("active");
          // sections[2].classList.add("active");
          // sections[3].classList.add("active");
        } else if (i == 2) {
          //project menu
          section_home.classList.remove("active");
          section_about.classList.remove("active");
          section_contact.classList.remove("active");
          // section_experience.classList.remove("active");
          section_project.classList.add("active");
          section_skill.classList.remove("active");

          // sections[0].classList.remove("active");
          // sections[1].classList.remove("active");
          // sections[2].classList.remove("active");
          // sections[3].classList.remove("active");
          // sections[5].classList.remove("active");
          // sections[4].classList.add("active");
        } else if (i == 3) {
          //contact menu
          section_home.classList.remove("active");
          section_about.classList.remove("active");
          section_contact.classList.add("active");
          // section_experience.classList.remove("active");
          section_project.classList.remove("active");
          section_skill.classList.remove("active");
          // sections[0].classList.remove("active");
          // sections[1].classList.remove("active");
          // sections[2].classList.remove("active");
          // sections[3].classList.remove("active");
          // sections[4].classList.remove("active");
          // sections[5].classList.add("active");
        }
      }, 100);
    }
  });
});
