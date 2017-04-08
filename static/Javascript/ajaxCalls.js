$(function() {
    $('#btnEnterDateLimits').click(function() {
        $.ajax({
            url: '/enterDateLimits',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
				//alert(response[0].date)
                //response = [{"date":"QA","kms":"a@b","desc":"abc"},{"date":"QA","kms":"a@b","desc":"abc"}];
				if (response[0].desc.indexOf("ERROR") >= 0) {
					$("#dateLimitFormMessage").html(response[0].desc);
				} else {
					$("#dateLimitFormMessage").html('<table class="table table-striped"><thead><tr><th>Date</th><th>KMs</th><th>Description</th></tr></thead><tbody id="dateLimitFormData"></tbody></table>');
					for(var i = 0; i < response.length; i++){
						$("#dateLimitFormData").append("<tr><td>"+response[i].date+"</td><td>"+response[i].kms+"</td><td>"+response[i].desc+"</td></tr>");
					}
				}
            },
            error: function(error) {
                console.log(error);
				$("#dateLimitFormMessage").html("Failed to fetch record");
            }
        });
    });
	});
