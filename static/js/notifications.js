// =========================
// SHOW NOTIFICATION
// =========================

function showNotification(message, type="success") {

    // REMOVE OLD

    let old =
    document.querySelector(".toast-notification");

    if(old) {

        old.remove();
    }


    // CREATE

    let toast =
    document.createElement("div");

    toast.className =
    "toast-notification";


    // ICONS

    let icon = "✅";

    if(type === "error") {

        icon = "❌";
    }

    if(type === "cart") {

        icon = "🛒";
    }

    if(type === "wishlist") {

        icon = "❤️";
    }

    if(type === "payment") {

        icon = "💳";
    }


    // CONTENT

    toast.innerHTML = `

        <div class="toast-content">

            <span class="toast-icon">

                ${icon}

            </span>

            <span class="toast-message">

                ${message}

            </span>

        </div>

    `;


    // ADD

    document.body.appendChild(toast);


    // SHOW

    setTimeout(() => {

        toast.classList.add("show");

    }, 100);


    // REMOVE

    setTimeout(() => {

        toast.classList.remove("show");

        setTimeout(() => {

            toast.remove();

        }, 500);

    }, 3000);
}