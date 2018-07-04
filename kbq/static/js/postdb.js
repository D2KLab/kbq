$(document).ready(function() {


    var $endpointDom = $('#endpoint');
    var $graphDom = $('#graph');
    var $classNameDom = $('#className');

    var $msg = $('#msg');

    var msgTemplate = "<li> Experiment Created. Please Send an Email to mohammad.rashid@polito.it to activate the process.</li>";
    function addMsg(msg){

        //$msg.append(Mustache.render(msgTemplate,msg));

        $msg.append('<li> Experiment Created. Please Send an Email to mohammad.rashid@polito.it to activate the process.</li>')
    }



    $.ajax({
       
    });

    $('#btnEndpoint').on('click',function(){
        
        $.LoadingOverlay("show");

        var postData = {
            endpoint: $endpointDom.val(),
            form: 'endpoint',
        };

        $.ajax({
            
            type: 'POST',
            url: '/experiment',
            data: postData,
            success: function(data){
                console.log(data);
				let datalist = $('#datalist-graph').empty();
				for (let i = 0; i < data.endpoint.length; i++) {
					let option = $('<option>');
					option.text(data.endpoint[i]);
					option.attr('value', data.endpoint[i]);
					datalist.append(option);
                }
                $.LoadingOverlay("hide");
            },
            error: function(){
                alert('server error')
                $.LoadingOverlay("hide");
            }
            
        });  
        event.preventDefault(); 
    });

    $('#btnGraph').on('click',function(){
        
        $.LoadingOverlay("show");

        var postDataGraph = {
            endpoint: $endpointDom.val(),
            graph: $graphDom.val(),
            form: 'graph',
        };

        $.ajax({
            
            type: 'POST',
            url: '/experiment',
            data: postDataGraph,
            success: function(data){
                console.log(data);
				let datalist = $('#datalist-className').empty();
				for (let i = 0; i < data.className.length; i++) {
					let option = $('<option>');
					option.text(data.className[i]);
					option.attr('value', data.className[i]);
					datalist.append(option);
                }
                $.LoadingOverlay("hide");
            },
            error: function(){
                alert('server error')
                $.LoadingOverlay("hide");
            }
            
        });  
        event.preventDefault(); 
    });

    $('#btnRunExp').on('click',function(){
        
        $.LoadingOverlay("show");

        var postDataClass = {
            endpoint: $endpointDom.val(),
            graph: $graphDom.val(),
            className: $classNameDom.val(),
            form: 'runexpriment',
        };

        $.ajax({
            
            type: 'POST',
            url: '/experiment',
            data: postDataClass,
            success: function(data){
 
                console.log(data);

                //$("#dialog").dialog();

                $msg.append('<div class="alert alert-dismissible alert-primary">'+
                            '<p>Experiment Status: Create </p>'+
                            '<p>Experiment ID:'+ data.expId +'</p>'+
                            '<p>Please Send an Email to mohammad.rashid@polito.it to activate the process.</p>'+
                            '</div>');
            

                $.LoadingOverlay("hide");

                //var $dialog = $('<div></div>') .html('This dialog will show every time!') .dialog({ autoOpen: false, title: 'Basic Dialog' });

                //$("<div>hello!</div>").dialog();

            },
            error: function(){
                alert('server error')
                $.LoadingOverlay("hide");
            }
            
        });  
        event.preventDefault(); 
    });
});