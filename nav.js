document.addEventListener('DOMContentLoaded', ()=> {

    let menu_icon = document.getElementById("nav-menu-button");
    menu_icon.addEventListener("click", () => {
        let menu = document.getElementById("nav-menu-content");
        if (menu.style.display === "none") {
            menu.style.display = "block";
        } else {
            menu.style.display = "none";
        }
        menu_icon.style.zIndex = "1";
    })
})