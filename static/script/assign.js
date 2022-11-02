$(document).ready(
    function() {
        $("#assignForm").on("submit", function(event){
            $.ajax(
                {
                    data: {
                        driver_id: $("#driver_id").val(),
                        reg_no: $("#reg_no").val(),
                        from: $("#from").val(),
                        to: $("#to").val(),
                        scheduled_date: $("#scheduled_date").val(),
                        scheduled_time: $("#scheduled_time").val()
                    }// end data
                    ,
                    type: 'POST',
                    url: "/assign/"+$("#driver_id").val(),
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.error) {
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else {
                        $("#warningAlert").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").text(data.success).show()
                        $("#from").val("")
                        $("#to").val("")
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready