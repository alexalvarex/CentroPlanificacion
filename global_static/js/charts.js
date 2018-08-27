 $(document).ready(function(){

      // GRAFICO DE TIPO DE ORDENES GENERAL
      var ctx4 = document.getElementById("myChart1").getContext('2d');
      var cantos1 = $('#cantos1').val();
      var cantoi1 = $('#cantoi1').val();
		var myChart4 = new Chart(ctx4, {
		    type: 'bar',
		    data: {
		        labels: ["Ordenes de Servicio", "Ordenes Internas"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [cantos1, cantoi1],
		            backgroundColor: [
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(54, 162, 235, 0.2)'
		            ],
		            borderColor: [
		                'rgba(255,99,132,1)',
		                'rgba(54, 162, 235, 1)'
		            ],
		            borderWidth: 1
		        }]
		    },
		    options: {
		        scales: {
		            yAxes: [{
		                ticks: {
		                    beginAtZero:true
		                }
		            }]
		        }
		    }
		});

		// GRAFICO DE TIPO DE ORDENES GENERAL
      var ctx5 = document.getElementById("familyChart1").getContext('2d');
      var cant5011 = $('#cant5011').val();
      var cant5021 = $('#cant5021').val();
      var cant5031 = $('#cant5031').val();
      var cant5041 = $('#cant5041').val();
      var cant5051 = $('#cant5051').val();
      var cant5061 = $('#cant5061').val();
      var cant5071 = $('#cant5071').val();
      var cant5081 = $('#cant5081').val();
      var cant5091 = $('#cant5091').val();
      var cant5101 = $('#cant5101').val();
      var cant5111 = $('#cant5111').val();
      var cant5121 = $('#cant5121').val();
      var cant5131 = $('#cant5131').val();
      var cant508TS1 = $('#cant508TS1').val();
      
		var myChart5 = new Chart(ctx5, {
		    type: 'bar',
		    data: {
		        labels: ["5011", "5021","5031","5041","5051","5061","5071","5081","5091","5101","5111","5121","5131","508TS1"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [cant5011, cant5021,cant5031,cant5041,cant5051,cant5061,cant5071,cant5081,cant5091,cant5101,cant5111,cant5121,cant5131,cant508TS1],
		            backgroundColor: [
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)'
		                
		            ],
		            borderColor: [
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)'
		                
		                
		            ],
		            borderWidth: 1
		        }]
		    },
		    options: {
		        scales: {
		            yAxes: [{
		                ticks: {
		                    beginAtZero:true
		                }
		            }]
		        }
		    }
		});	

		// GRAFICO DE MOTIVO GEMERAL
      var ctx6 = document.getElementById("gastoChart1").getContext('2d');
      var malop1 = $('#malop1').val();
      var accidente1 = $('#accidente1').val();
      var gasto1 = $('#gasto1').val();
		var myChart6 = new Chart(ctx6, {
		    type: 'bar',
		    data: {
		        labels: ["Mala Operación", "Accidente", "Gasto"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [malop1, accidente1, gasto1],
		            backgroundColor: [
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)',
		                'rgba(255, 99, 132, 0.2)'
		            ],
		            borderColor: [
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)',
		                'rgba(255,99,132,1)'
		            ],
		            borderWidth: 1
		        }]
		    },
		    options: {
		        scales: {
		            yAxes: [{
		                ticks: {
		                    beginAtZero:true
		                }
		            }]
		        }
		    }
		});

});