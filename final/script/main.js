// change theme based on variable in localstorage
if (localStorage) {
    if (localStorage.getItem("theme") === "dark") {
        document.documentElement.setAttribute("data-theme", "dark");
    } 
    if (localStorage.getItem("theme") === "light") {
        document.documentElement.setAttribute("data-theme", "light");
    }
} else {
    // if localstorage isnt defined just set the theme to light
    document.documentElement.setAttribute("data-theme", "light");
    localStorage.setItem("theme", "light");
}

// change theme on click
function btnclick() {
    if (localStorage.getItem("theme") === "dark") {
        document.documentElement.setAttribute("data-theme", "light");
        localStorage.setItem("theme", "light");
        console.log(localStorage)
    } 
    else if (localStorage.getItem("theme") === "light") {
        document.documentElement.setAttribute("data-theme", "dark");
        localStorage.setItem("theme", "dark");
        console.log(localStorage)
    }
}