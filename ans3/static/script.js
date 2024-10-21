document
  .getElementById("registrationForm")
  .addEventListener("submit", function (event) {
    let userId = document.getElementById("userId").value;
    let mobileNumber = document.getElementById("mobileNumber").value;
    let password = document.getElementById("password").value;

    if (userId.length < 5) {
      event.preventDefault();
      document.getElementById("message").textContent =
        "User ID must be at least 5 characters long.";
    } else if (!/^\d{10}$/.test(mobileNumber)) {
      event.preventDefault();
      document.getElementById("message").textContent =
        "Mobile number must be exactly 10 digits.";
    } else if (password.length < 6) {
      event.preventDefault();
      document.getElementById("message").textContent =
        "Password must be at least 6 characters long.";
    }
  });
