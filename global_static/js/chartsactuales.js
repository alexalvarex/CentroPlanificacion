 $(document).ready(function(){

      // GRAFICO DE TIPO DE ORDENES GENERAL
      var ctx = document.getElementById("myChart").getContext('2d');
      var cantos = $('#cantos').val();
      var cantoi = $('#cantoi').val();
		var myChart = new Chart(ctx, {
		    type: 'bar',
		    data: {
		        labels: ["Ordenes de Servicio", "Ordenes Internas"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [cantos, cantoi],
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
      var ctx2 = document.getElementById("familyChart").getContext('2d');
      var cant501 = $('#cant501').val();
      var cant502 = $('#cant502').val();
      var cant503 = $('#cant503').val();
      var cant504 = $('#cant504').val();
      var cant505 = $('#cant505').val();
      var cant506 = $('#cant506').val();
      var cant507 = $('#cant507').val();
      var cant508 = $('#cant508').val();
      var cant509 = $('#cant509').val();
      var cant510 = $('#cant510').val();
      var cant511 = $('#cant511').val();
      var cant512 = $('#cant512').val();
      var cant513 = $('#cant513').val();
      var cant508TS = $('#cant508TS').val();
      
		var myChart2 = new Chart(ctx2, {
		    type: 'bar',
		    data: {
		        labels: ["501", "502","503","504","505","506","507","508","509","510","511","512","513","508TS"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [cant501, cant502,cant503,cant504,cant505,cant506,cant507,cant508,cant509,cant510,cant511,cant512,cant513,cant508TS],
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
      var ctx3 = document.getElementById("gastoChart").getContext('2d');
      var malop = $('#malop').val();
      var accidente = $('#accidente').val();
      var gasto = $('#gasto').val();
		var myChart3 = new Chart(ctx3, {
		    type: 'bar',
		    data: {
		        labels: ["Mala Operación", "Accidente", "Gasto"],
		        datasets: [{
		            label: 'Cantidades',
		            data: [malop, accidente, gasto],
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