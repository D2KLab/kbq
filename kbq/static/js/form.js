$(document).ready(function() {


	$('#formEndpoint').on('submit', function(event) {

		//var modal = $('<div>').dialog({ modal: true });
        //    modal.dialog('widget').hide();
		//$('#ajax_loader').show();
		
		$.ajax({
			data : {
				endpoint : $('#endpoint').val(),
				form : 'endpoint'
			},
			type : 'POST',
			url : '/experiment'
			
		})
		.done(function(data) {

			if (data.error) {
				//$('#errorAlert').text(data.error).show();
				//$('#successAlert').hide();
			}
			else {
				//$('#successAlert').text(data.name).show();
				//$('#errorAlert').hide();
				//alert('success!');
				console.log(data);
				let datalist = $('#datalist-graph').empty();
				for (let i = 0; i < data.endpoint.length; i++) {
					let option = $('<option>');
					option.text(data.endpoint[i]);
					option.attr('value', data.endpoint[i]);
					datalist.append(option);
				}

			}

		});

		event.preventDefault();

	});

	$('#formGraph').on('submit', function(event) {

		$.ajax({
			data : {
				endpoint : $('#endpoint').val(),
				graph : $('#graph').val(),
				form: 'graph'
			},
			type : 'POST',
			url : '/experiment'
		})
		.done(function(data) {

			if (data.error) {
				//$('#errorAlert').text(data.error).show();
				//$('#successAlert').hide();
			}
			else {
				console.log(data);
				let datalist = $('#datalist-className').empty();
				for (let i = 0; i < data.className.length; i++) {
					let option = $('<option>');
					option.text(data.className[i]);
					option.attr('value', data.className[i]);
					datalist.append(option);
				}
			}

		});

		event.preventDefault();

	});
});

