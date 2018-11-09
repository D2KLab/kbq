$(document).ready(function() {

    //Disbale attributes
    //$("#btnRunExp").prop("disabled", true);
    document.getElementById("graph").disabled = true;
    document.getElementById('btnGraph').disabled = true;
    
    document.getElementById('btnRunExp').disabled = true;
    document.getElementById("className").disabled = true;

    document.getElementById("btnReset").disabled = true;
    

    var $endpointDom = $('#endpoint');
    var $graphDom = $('#graph');
    var $classNameDom = $('#className');

    var $msg = $('#notify_msg');

    var msgTemplate = "<li> Experiment Created. Please Send an Email to mohammad.rashid@polito.it to activate the process.</li>";
    function addMsg(msg){
        //$msg.append(Mustache.render(msgTemplate,msg));
        $msg.append('<p> Experiment Created. Please Send an Email to mohammad.rashid@polito.it to activate the process.</p>')
    }


    $('#btnEndpoint').on('click',function(){
             
        var postData = {
            endpoint: $endpointDom.val(),
            form: 'endpoint',
        };

        if($endpointDom==""|| $endpointDom==null){
            alert('Please Enter a Valid SPARQL endpoint');
            return false;  
        }
        else{
        $.LoadingOverlay("show");
        $.ajax({
            
            type: 'POST',
            url: 'experiment',
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

                //Change div color
                $('#one').css('background-color', 'black');
        
                //Remove color
                //$('#two').css('background-color', '');
                
                document.getElementById("graph").disabled = false;
                document.getElementById("btnGraph").disabled = false;
                document.getElementById("btnReset").disabled = false;

                // focus next button
                // $( "#btnGraph" ).focus();
                $(this).next("#btnGraph").focus();

                $.LoadingOverlay("hide");
            },
            error: function(){
                alert('server error')
                $.LoadingOverlay("hide");
            }
        });
        }  
        event.preventDefault(); 
    });

    $('#btnGraph').on('click',function(){
 
        var postDataGraph = {
            endpoint: $endpointDom.val(),
            graph: $graphDom.val(),
            form: 'graph',
        };

        var names = $graphDom.val();

        if(names=="" || names==null){
            alert('Please Select a Graph Name');
            return false;         
        }
        else{
        $.LoadingOverlay("show");    
        $.ajax({ 
            type: 'POST',
            url: 'experiment',
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

                $('#two').css('background-color', 'black');
                document.getElementById("btnRunExp").disabled = false;
                document.getElementById("className").disabled = false;

                $.LoadingOverlay("hide");
            },
            error: function(){
                $.LoadingOverlay("hide");
                alert('Error in acessing the Graph Data. Please check name of the Graph.')
            }
            
        });
        }  
        event.preventDefault(); 
    });

    $('#btnRunExp').on('click',function(){
        
        var postDataClass = {
            endpoint: $endpointDom.val(),
            graph: $graphDom.val(),
            className: $classNameDom.val(),
            form: 'runexpriment',
        };

        var classVal = $classNameDom.val();

        if(classVal==""|| classVal==null){
            
            alert('Please Select a Class Name');
            return false;
            
        }
        else{
        $.LoadingOverlay("show");    
        $.ajax({
            
            type: 'POST',
            url: 'experiment',
            data: postDataClass,
            success: function(data){
 
                console.log(data);

                //$("#dialog").dialog();

                if(data.Flag){

                   $msg.empty(); 

                    $msg.append('<div>'+
                                '<p>Experiment Status:'+data.status+'</p>'+
                                '<p>Experiment ID:'+ data.expId +'</p>'+
                                '<p>Please Send an Email to mohammad.rashid@polito.it to activate the process.</p>'+
                                '</div>');    
                }else{
                    //alert('Experiment Already Exists')
                    $msg.empty(); 

                    $msg.append('<div>'+
                                '<p>Experiment Status:'+data.status+'</p>'+
                                '<p>Experiment ID:'+ data.expId +'</p>'+
                                '<p>This experiment is in the waiting list for activation. Please Send an Email to <a href="mailto::mohammad.rashid@polito.it">mohammad.rashid@polito.it</a> to activate the process</p>'+
                                '<p>All <a href="/active"> Active Experiments</a></p>'+
                                '</div>');   
                }
              
                $.LoadingOverlay("hide");
                $('#three').css('background-color', 'black');
                $('#four').css('background-color', 'black');

                document.getElementById("btnReset").disabled = false;

                //var $dialog = $('<div></div>') .html('This dialog will show every time!') .dialog({ autoOpen: false, title: 'Basic Dialog' });
                //$("<div>hello!</div>").dialog();

            },
            error: function(){
                alert('server error')
                $.LoadingOverlay("hide");
            }
            
        });
        }  
        event.preventDefault(); 
    });

    $('#btnReset').on('click',function(){

        document.getElementById("graph").value = '';

        $("datalist-graph").empty();
        $('#one').css('background-color', '');
        $('#two').css('background-color', '');
        $('#three').css('background-color', '');
        $('#four').css('background-color', '');

        $msg.empty(); 

        document.getElementById("graph").disabled = true;
        document.getElementById("btnGraph").disabled = true;
        
        //document.getElementById("className").innerHTML = '';
        document.getElementById("className").value = '';

        document.getElementById("className").disabled = true;
        document.getElementById("btnRunExp").disabled = true;

        document.getElementById("btnReset").disabled = true;

        event.preventDefault(); 
    });

}); 