document.addEventListener("DOMContentLoaded", function () {

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {

        if (window.scrollY > 30) {

            navbar.classList.add("navbar-scrolled");

        } else {

            navbar.classList.remove("navbar-scrolled");

        }

    });


    const links = document.querySelectorAll(".nav-link");

    links.forEach(function (link) {

        link.addEventListener("click", function () {

            const navbarCollapse =
                document.querySelector(".navbar-collapse");

            if (
                navbarCollapse &&
                navbarCollapse.classList.contains("show")
            ) {

                const bsCollapse =
                    bootstrap.Collapse.getInstance(
                        navbarCollapse
                    );

                if (bsCollapse) {
                    bsCollapse.hide();
                }

            }

        });

    });

});