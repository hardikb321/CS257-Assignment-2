document
  .getElementById("registrationForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    let userId = document.getElementById("userId").value;
    let password = document.getElementById("password").value;

    if (userId.length < 5) {
      document.getElementById("message").textContent =
        "User ID must be at least 5 characters long.";
    } else if (password.length < 6) {
      document.getElementById("message").textContent =
        "Password must be at least 6 characters long.";
    } else {
      document.getElementById("message").textContent =
        "Registration successful!";
    }
  });
