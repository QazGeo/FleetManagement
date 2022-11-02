$(document).ready(
    function() {
        $("#ownerForm").on("submit", function(event){
        $("#success").text("Please wait...").show()

        var form_data = new FormData()
        form_data.append(
            "files[]",
            document.getElementById("passport_pic").files[0]
            )
        form_data.append("fname", $("#fname").val())
        form_data.append("lname", $("#lname").val())
        form_data.append("surname", $("#surname").val())
        form_data.append("id_no", $("#id_no").val())
        form_data.append("phone", $("#phone").val())
        form_data.append("email", $("#email").val())
        form_data.append("address", $("#address").val())
        form_data.append("dob", $("#dob").val())
        form_data.append("loc_id", $("#loc_id").val())

            $.ajax(
                {
                    data: form_data,
                    type: 'POST',
                    url: "/addowner",
                    cache: false,
                    contentType: false,
                    processData: false
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.error) {
                        $("#error").text(data.error).show()
                        $("#error2").hide()
                        $("#success").hide()
                    }
                    else if(data.error2) {
                        $("#error").hide()
                        $("#error2").text(data.error2).show()
                        $("#success").hide()
                    }
                    else {
                        $("#error").hide()
                        $("#error2").hide()
                        $("#success").text(data.success).show()
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready