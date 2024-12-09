// Function to validate the login credentials by connecting to the server
function validateLogin(event) {
    event.preventDefault(); // Prevent form submission until validation is complete

    // Get the values from the input fields
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Get the element where we want to display the message
    var messageElement = document.getElementById('loginMessage');

    // Create an object for the login credentials
    var credentials = {
        username: username,
        password: password
    };

    // Make an API call to the server to check the credentials
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(credentials)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            // If the credentials are correct, show a success message
            messageElement.style.color = 'green';
            messageElement.textContent = 'Login successful!';
            // Optionally, you can submit the form here if backend validation is successful
            // document.getElementById('loginForm').submit();
        } else {
            // If the credentials are incorrect, show a failure message
            messageElement.style.color = 'red';
            messageElement.textContent = 'Login failed. Incorrect username or password.';
        }
    })
    .catch(error => {
        // Handle errors in the fetch request
        messageElement.style.color = 'red';
        messageElement.textContent = 'An error occurred. Please try again later.';
        console.error('Error:', error);
    });
}

// Add event listener to the form to validate when the login button is pressed
document.getElementById('loginForm').addEventListener('submit', validateLogin);
