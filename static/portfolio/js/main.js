const menuButton =
    document.getElementById(
        "menu-button"
    );

const navMenu =
    document.getElementById(
        "nav-menu"
    );


menuButton.addEventListener(
    "click",
    () => {

        navMenu.classList.toggle(
            "active"
        );

    }
);


document
    .querySelectorAll(
        "#nav-menu a"
    )
    .forEach(
        link => {

            link.addEventListener(
                "click",
                () => {

                    navMenu.classList.remove(
                        "active"
                    );

                }
            );

        }
    );