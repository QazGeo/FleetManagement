$(document).ready(
    function() {
        $("#vehicleForm").on("submit", function(event){
        $("#success").text("Please wait...").show()
        var form_data = new FormData()
        form_data.append(
            "files[]",
            document.getElementById("vehicle_pic").files[0]
            )
        form_data.append("reg_no", $("#reg_no").val())
        form_data.append("type_id", $("#type_id").val())
        form_data.append("make_id", $("#make_id").val())
        form_data.append("model_id", $("#model_id").val())
        form_data.append("capacity_id", $("#capacity_id").val())
        form_data.append("color", $("#color").val())
        form_data.append("weight", $("#weight").val())
        form_data.append("no_of_pass", $("#no_of_pass").val())
        form_data.append("yom", $("#yom").val())
        form_data.append("owner_id", $("#owner_id").val())
        form_data.append("chassis_no", $("#chassis_no").val())

            $.ajax(
                {
                    data: form_data,
                    type: 'POST',
                    url: "/addvehicle/"+$("#owner_id").val(),
                    cache: false,
                    contentType: false,
                    processData: false
                }
            // $.ajax(
            //     {
            //         data: {
            //             fname: $("#fname").val(),
            //             lname: $("#lname").val(),
            //             surname: $("#surname").val(),
            //             phone: $("#phone").val(),
            //             email: $("#email").val(),
            //             dl_no: $("#dl_no").val(),
            //             passport_pic: $("#passport_pic").val(),
            //             dob: $("#dob").val(),
            //             loc_id: $("#loc_id").val()
            //         }// end data
            //         ,
            //         type: 'POST',
            //         url: "/adddriver"
            //     }
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


        $(document).ready(
            function() {
                
            }
        )


    }
)// end ready