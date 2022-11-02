$(document).ready(
    function() {

        var x = ""
        $(".gender").click(
            function() {
                x = $(this).val()
            }
        )

        $("#userForm").on("submit", function(event){

            $.ajax(
                {
                    data: {
                        fname: $("#fname").val(),
                        lname: $("#lname").val(),
                        surname: $("#surname").val(),
                        gender : x,
                        role: $("#role").val(),
                        phone: $("#phone").val(),
                        email: $("#email").val(),
                    }// end data
                    ,
                    type: 'POST',
                    url: "/adduser"
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.errorfname) {
                        $("#errorfname").text(data.errorfname).show()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").hide()
                        $("#erroremail").hide()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.errorlname) {
                        $("#errorfname").hide()
                        $("#errorlname").text(data.errorlname).show()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").hide()
                        $("#erroremail").hide()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    // else if(data.errorsurname) {
                    //     $("#errorfname").hide()
                    //     $("#errorlname").hide()
                    //     $("#errorsurname").text(data.errorsurname).show()
                    //     $("#errorrole").hide()
                    //     $("#errorphone").hide()
                    //     $("#erroremail").hide()
                    //     $("#errorgender").hide()
                    //     $("#errorAlert").hide()
                    //     $("#successAlert").hide()
                    // }
                    else if(data.errorphone) {
                        $("#errorfname").hide()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").text(data.errorphone).show()
                        $("#erroremail").hide()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.erroremail) {
                        $("#errorfname").hide()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").hide()
                        $("#erroremail").text(data.erroremail).show()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.errorrole) {
                        $("#errorfname").hide()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").text(data.errorrole).show()
                        $("#errorphone").hide()
                        $("#erroremail").hide()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.errorgender) {
                        $("#errorfname").hide()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").hide()
                        $("#erroremail").hide()
                        $("#errorgender").text(data.errorgender).show()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.error2) {
                        $("#errorAlert").text(data.error2).show()
                        $("#errorfname").hide()
                        $("#errorlname").hide()
                        $("#errorsurname").hide()
                        $("#errorrole").hide()
                        $("#errorphone").hide()
                        $("#erroremail").hide()
                        $("#errorgender").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else {
                        $("#errorAlert").hide()
                        $("#successAlert").text(data.success).show()
                        $("#fname").val("")
                        $("#lname").val("")
                        $("#surname").val("")
                        $("#gender").val("")
                        $("#role").val("")
                        $("#email").val("")
                        $("#phone").val("")
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready