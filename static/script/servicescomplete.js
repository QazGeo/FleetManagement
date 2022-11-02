$(document).ready(
    function() {
        $("#processForm").on("submit", function(event){
        $("#successAlert").text("Please wait...").show()
        var services = $('input[name="name[]"]').map(
            function() {
                return this.value;
            }
        ).get();
        console.log(services);
            $.ajax(
                {
                    data: {
                        service_id: $("#service_id").val(),
                        reg_no: $("#reg_no").val(),
                        'name[]': services
                    }// end data
                    ,
                    type: 'POST',
                    url: "/servicescomplete/"+$("#service_id").val()
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
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready