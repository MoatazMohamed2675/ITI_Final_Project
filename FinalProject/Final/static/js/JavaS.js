  function addItem() {
        let container = document.getElementById("items-container");
        let template = document.getElementById("item-template").innerHTML;

        // create a new row from template
        let newRow = document.createElement("div");
        newRow.innerHTML = template;
        container.appendChild(newRow.firstElementChild);
    }

    function removeItem(button) {
        let container = document.getElementById("items-container");
        let rows = container.querySelectorAll(".item-row");

        // allow removing only if more than 1 row exists
        if (rows.length > 1) {
            button.parentElement.remove();
        } else {
            alert("You must have at least one item in the order.");
        }
    }


function searchProduct() {
            let query = document.getElementById("search-input").value;

            fetch(`/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    let content = document.getElementById("message-content");

                    if (data.results.length > 0) {
                        let list = "<ul>";
                        data.results.forEach(p => {
                            list += `<li><strong>${p.name}</strong> - $${p.price} - ${p.description}</li>`;
                        });
                        list += "</ul>";
                        content.innerHTML = list;
                    } else {
                        content.innerHTML = "<p style='color:red;'>No products found!</p>";
                    }

                    document.getElementById("message-box").style.display = "block";
                })
                .catch(error => {
                    document.getElementById("message-content").innerHTML =
                        "<p style='color:red;'>Error: " + error + "</p>";
                    document.getElementById("message-box").style.display = "block";
                });
        }
     function closeMessage() {
            document.getElementById("message-box").style.display = "none";
        }