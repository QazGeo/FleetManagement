$(document).ready(
    function() {
        $("#myButton").click(
            function() {
                $("#navigation").toggleClass("hide")
            }
        )
        $("#logout").click(
        function() {
            alert("Logging out, please confirm")
        }
        )
    }
)