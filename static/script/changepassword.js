$(document).ready(
    function() {
        $("#changeForm").on("submit", function(event){
            $.ajax(
                {
                    data: {
                        current_pswd: $("#current_pswd").val(),
                        new_pswd: $("#new_pswd").val(),
                        con_pswd: $("#con_pswd").val()
                    }// end data
                    ,
                    type: 'POST',
                    url: "/changepassword"
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.currentwrong) {
                        $("#currentwrong").text(data.currentwrong).show()
                        $("#newwrong").hide()
                        $("#errorpswd").hide()
                        $("#consuccess").hide()
                        $("#conwrong").hide()
                    }
                    else if(data.newwrong) {
                        $("#currentwrong").hide()
                        $("#newwrong").text(data.newwrong).show()
                        $("#errorpswd").hide()
                        $("#consuccess").hide()
                        $("#conwrong").hide()
                    }
                    else if(data.errorpswd) {
                        $("#currentwrong").hide()
                        $("#newwrong").hide()
                        $("#errorpswd").text(data.errorpswd).show()
                        $("#consuccess").hide()
                        $("#conwrong").hide()
                    }
                    else if(data.conwrong) {
                        $("#currentwrong").hide()
                        $("#newwrong").hide()
                        $("#errorpswd").hide()
                        $("#consuccess").hide()
                        $("#conwrong").text(data.conwrong).show()
                    }
                    else {
                        $("#currentwrong").hide()
                        $("#newwrong").hide()
                        $("#errorpswd").hide()
                        $("#consuccess").text(data.consuccess).show()
                        $("#conwrong").hide()
                        $("#current_pswd").val("")
                        $("#new_pswd").val("")
                        $("#con_pswd").val("")
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready