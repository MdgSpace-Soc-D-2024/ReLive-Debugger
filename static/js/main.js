// Wait for DOM to load before running the script
document.addEventListener("DOMContentLoaded", function() {

    // Handle form submission for file upload and debug
    document.getElementById("file-form").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission
        
        let formData = new FormData();
        formData.append("file", document.getElementById("file").files[0]);

        fetch("/debug_file", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                updateSnapshotButtons(data.snapshots);
            }
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });

    // Function to dynamically update the snapshot buttons
    function updateSnapshotButtons(snapshots) {
        const container = document.getElementById("snapshot-buttons");
        container.innerHTML = ""; // Clear existing content

        if (snapshots.length === 0) {
            container.innerHTML = "<p>No snapshots available</p>";
        } else {
            snapshots.forEach((_, index) => {
                const button = document.createElement("button");
                button.textContent = `Load Snapshot ${index}`;
                button.onclick = () => loadSnapshot(index);
                container.appendChild(button);
            });
        }
    }

    // Function to load a snapshot
    function loadSnapshot(index) {
        console.log("Requesting snapshot index:", index); // Debugging log

        // Show loading state
        const display = document.getElementById("snapshot-display");
        display.innerHTML = ""; // Clear previous snapshot data
        display.classList.add("loading"); // Add loading class to display loading animation

        fetch("/load_snapshot", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ index: index }),
        })
        .then(response => {
            console.log("Response status:", response.status); // Debugging log
            return response.json();
        })
        .then(data => {
            console.log("Received data:", data); // Debugging log
            display.classList.remove("loading"); // Remove loading state

            if (data.status === "success") {
                const snapshot = data.snapshot;
                display.innerHTML = `
                    <p><strong>File to be debugged:</strong> ${snapshot.filename}</p>
                    <p><strong>Breakpoint:</strong> ${snapshot.line_number}</p>
                    <p><strong>Variables:</strong></p>
                    <pre>${JSON.stringify(snapshot.local_variables, null, 2)}</pre>
                `;
            } else {
                display.innerHTML = `<p style="color: red;">${data.message}</p>`;
            }
        })
        .catch(error => {
            console.error("Error loading snapshot:", error);
            display.classList.remove("loading");
            display.innerHTML = "<p style='color: red;'>Failed to load snapshot. Please try again.</p>";
        });
    }

});
