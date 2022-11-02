$(document).ready(
    function() {
        $("#serviceForm").on("submit", function(event){
        $("#successAlert").text("Please wait...").show()
        var array = [];
        $("#list").find("option:selected").map(
            function() {
                // alert($(this).text())
                array.push($(this).text());
            }
        )
        console.log(array)
            $.ajax(
                {
                    data: {
                        // driver_id: $("#driver_id").val(),
                        reg_no: $("#reg_no").val(),
                        services: array,
                        // cache: $("#cache").val(),
                        scheduled_date: $("#scheduled_date").val(),
                        scheduled_time: $("#scheduled_time").val()
                    }// end data
                    ,
                    type: 'POST',
                    url: "/send_service/"+$("#reg_no").val()
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.error1) {
                        $("#errorAlert").text(data.error2).show()
                        $("#successAlert").hide()
                    }
                    else {
                        $("#errorAlert").hide()
                        $("#successAlert").text(data.success).show()
                        $("#reg_no").val("")
                        $("#service").val("")
                        $("#scheduled_date").val("")
                        $("#scheduled_time").val("")
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready