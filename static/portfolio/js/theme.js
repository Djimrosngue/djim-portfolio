document.addEventListener("DOMContentLoaded", function () {

    const toggle = document.getElementById("theme-toggle");
    const icon = document.getElementById("theme-icon");

    if (!toggle) {
        return;
    }


    const savedTheme =
        localStorage.getItem("theme");


    if (savedTheme === "dark") {

        document.documentElement
            .setAttribute(
                "data-theme",
                "dark"
            );

        icon.classList.remove("bi-moon");
        icon.classList.add("bi-sun");

    }


    toggle.addEventListener("click", function () {

        const currentTheme =
            document.documentElement
                .getAttribute("data-theme");


        if (currentTheme === "dark") {

            document.documentElement
                .removeAttribute("data-theme");

            localStorage.setItem(
                "theme",
                "light"
            );

            icon.classList.remove("bi-sun");
            icon.classList.add("bi-moon");

        } else {

            document.documentElement
                .setAttribute(
                    "data-theme",
                    "dark"
                );

            localStorage.setItem(
                "theme",
                "dark"
            );

            icon.classList.remove("bi-moon");
            icon.classList.add("bi-sun");

        }

    });

});