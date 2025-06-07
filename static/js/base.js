// Toggle mobile menu
const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile-view");

hamburger.addEventListener("click", () => {
  mobileMenu.classList.toggle("active");
});

// Close mobile menu when clicking a nav link
document.querySelectorAll(".mobile-nav-menu .nav-link").forEach((link) => {
  link.addEventListener("click", () => {
    mobileMenu.classList.remove("active");
  });
});

// Dropdown logic: only if user-icon and user-dropdown exist
const userIcon = document.querySelector(".user-icon");
const userDropdown = document.getElementById("user-dropdown");

if (userIcon && userDropdown) {
  // Toggle dropdown on user icon click
  userIcon.addEventListener("click", function (event) {
    event.preventDefault();
    event.stopPropagation();
    if (userDropdown.classList.contains("show")) {
      userDropdown.style.display = "none";
      userDropdown.classList.remove("show");
    } else {
      userDropdown.style.display = "block";
      userDropdown.classList.add("show");
    }
  });

  // Prevent dropdown from closing when clicking inside it
  userDropdown.addEventListener("click", function (event) {
    event.stopPropagation();
  });

  // Close dropdown when clicking outside
  document.addEventListener("click", function (event) {
    if (userDropdown.classList.contains("show")) {
      userDropdown.classList.remove("show");
      userDropdown.style.display = "none";
    }
  });
}
