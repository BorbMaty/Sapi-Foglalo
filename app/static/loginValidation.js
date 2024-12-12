document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    try {
        // Send email and password to the backend
        const response = await fetch("http://127.0.0.1:8000/password/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        });

        if (response.ok) {
            const data = await response.json();
            // alert(`Welcome, ${data.name}!`); // Display user name from response

            localStorage.setItem("email", data.email);
            
            window.location.href = '/static/index.html';
        } else {
            const errorData = await response.json();
            document.getElementById("error-message").innerText = errorData.detail || "Invalid credentials.";
        }
    } catch (error) {
        document.getElementById("error-message").innerText = "An error occurred. Please try again.";
    }
});
