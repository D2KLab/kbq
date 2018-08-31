$(document).ready(function() {

    $('#active-list').DataTable();

    
    var table = $('#example').DataTable();
    
    var table2 = $('#example2').DataTable();
    
    var table3 = $('#example3').DataTable();

    var $query = $('#modelBody');

    // Table select

    /*$('#example tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
    } );

    $('#modal_button_id').click(function (event) {
        $('#myModal').modal('show');
        $query.empty();
        var ids = $.map(table.rows('.selected').data(), function (item) {
            return item[0]
        });
        $query.append('<p> SPARQL Query:</br>'+'SELECT ?s ?o </br> WHERE{ ?s <'+ ids
        +'>}</p>');
    });*/

  
         
   /* $('#example tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
        
    } );
    
    $('#example2 tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
        
    } );
    
    $('#example3 tbody').on( 'click', 'tr', function () {
        $(this).toggleClass('selected');
    } );
    
    
    $('#button').click( function () {
        alert( table.rows('.selected').data().length +' row(s) selected' );
    } );*/

    $.LoadingOverlay("hide");

} );