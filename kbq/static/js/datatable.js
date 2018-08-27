$(document).ready(function() {
    $('#active-list').DataTable();

} );



$(document).ready(function() {

    
    var table = $('#example').DataTable();
    
    var table = $('#example2').DataTable();
    
    var table = $('#example3').DataTable();
         
    $('#example tbody').on( 'click', 'tr', function () {
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
    } );

    $.LoadingOverlay("hide");

} );