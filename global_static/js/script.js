 $(document).ready(function(){

 	$('.actuales').hide()
 	$('.general').hide()

 	$('#btnactuales').on('click',function() {			        
       $('.actuales').Show()
      });

      $( "select" ).change(function(){
        var proveedor = $('#nombreprove').val()
        $('#numprove').val(proveedor)
      });

      $("#myInput").on("keyup", function() {
	    var value = $(this).val().toLowerCase();
	    $(".dropdown-menu option").filter(function() {
	      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	    });
	  });

	  $("#myInput2").on("keyup", function() {
	    var value = $(this).val().toLowerCase();
	    $(".dropdown-menu2 option").filter(function() {
	      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	    });
	  });
	  $("#myInput3").on("keyup", function() {
	    var value = $(this).val().toLowerCase();
	    $(".dropdown-menu3 option").filter(function() {
	      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	    });
	  });

	  $("#myInput4").on("keyup", function() {
	    var value = $(this).val().toLowerCase();
	    $(".dropdown-menu4 option").filter(function() {
	      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	    });
	  });
		

});