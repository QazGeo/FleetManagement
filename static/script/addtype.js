$(document).ready(
    function() {
        $("#typeForm").on("submit", function(event){
            $.ajax(
                {
                    data: {
                        type: $("#type").val() // get make from input
                    }// end data
                    ,
                    type: 'POST',
                    url: "/addtype"
                }
            )// end ajax

            // waiting for python response, no refresh

            .done(
                function(data) {
                    if(data.error1) {
                        $("#warningAlert").text(data.error1).show()
                        $("#errorAlert").hide()
                        $("#successAlert").hide()
                    }
                    else if(data.error1) {
                        $("#warningAlert").hide()
                        $("#errorAlert").text(data.error2).show()
                        $("#successAlert").hide()
                    }
                    else {
                        $("#warningAlert").hide()
                        $("#errorAlert").hide()
                        $("#successAlert").text(data.success).show()
                        $("#type").val("")
                    }
                }
            ) // end done

            event.preventDefault()

        })// end submit
    }
)// end ready