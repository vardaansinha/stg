<html lang="{{ site.lang | default: "en-US" }}">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>LOGIN OR SIGN UP!</title>
    <style>
        h1 {
          text-align: center;
          font-size: 40px;
          font-weight: 700;
          color: #fcf6d9;
          font-family: verdana;
        }
        input.login {
          font-family: verdana;
          margin-top: 5%;
          position: inline;
          width: 40%;
          margin-left: 29%;
          margin-right: 40%;
          padding: 2%;
          font-size: 20px;
          background-color: #fcf6d9;;
          color: #888888;
          border: none;
        }
        button {
          outline: none;
          -webkit-tap-highlight-color: transparent;
          font-family: verdana;
          font-size: 20px;
          margin-top: 4%; 
          margin-bottom: 4%;
          position: inline;
          width: 40%;
          margin-left: 30%;
          margin-right: 30%;
          padding: 2%;
          border-radius: 8px;
          background-color: #302f2f;
          color: #888888;
          border: none;
        }
        div.newaccount {
          margin-top: 4%;
          margin-left: 25%;
          margin-right: 25%;
          position: inline;
          width: 50%;
        }
        #noacc {
          font-family: verdana;
          font-size: 25px;
          text-align: center;
          margin-bottom: 0%;          
        }
    </style>
    

  </head>
  <body>
    <h1 class="header">
      SIGN UP!
    </h1>
    <input type="username" class="login" id="uname" placeholder="Enter username here..">
    <input type="password" class="login" id="pwd" placeholder="Enter password here..">
     <input type="password" class="login" id="pwd" placeholder="Confirm password..">
    <div>
    <br>
      <button id="enter" type="button" onclick="window.location.href='{{ site.baseurl }}/';">Sign me up!</button>
      <button id="login" type="button" onclick="window.location.href='{{ site.baseurl }}/login';">I already have an account, login.</button>
    </div>
    
  </body>
  <script>
      // Get the input field
      var input = document.getElementById("pwd");
      // Execute a function when the user presses a key on the keyboard
      input.addEventListener("keypress", function(event) {
        // If the user presses the "Enter" key on the keyboard
        if (event.key === "Enter") {
          event.preventDefault();
          // Trigger the button element with a click
          document.getElementById("enter").click();
        }
      });
    </script>
</html>