/* =============================================================================
   NAV.JS — Mobile Hamburger Menu Toggle
   =============================================================================
   Simple script. Toggles the CSS class "open" on the .nav-links element
   when the hamburger button (.nav-toggle) is clicked.

   The styling for the open/closed state is in css/nav.css.
   This works on ALL pages — loaded via <script src="js/nav.js"> in every HTML file.

   DEPENDENCY: Requires .nav-toggle and .nav-links elements to exist in the DOM.
   ============================================================================= */
const toggle = document.querySelector(".nav-toggle");
const links = document.querySelector(".nav-links");

toggle.addEventListener("click", () => {
    links.classList.toggle("open");
});
