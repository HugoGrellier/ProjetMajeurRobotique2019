$(document).ready(function () {
    session = new QiSession("127.0.0.1:8002", "1.0"); // création d'une session Qi

// Au démarrage de la tablette on choisi, ci-dessous, de montrer la page "page_empty" 
//(celle avec le bouton "GO")	

    $('#page_empty').show();
    $('#page_choix').hide();
    $('#page_corbeille').hide();
    $('#page_fin').hide();
    $('#page_parti').hide();
    

// On définit ensuite un certain nombre de pages caractérisées par le choix de montrer (.show())
// ou de cacher (. hide() ) une des divisions défini dans le html (index.html). 
    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("web_projet/Page0").done(function(subscriber) {
			
 // on montre la page empty
			
            subscriber.signal.connect(function() {
                    $('#page_empty').show();
   		    $('#page_choix').hide();
    		    $('#page_corbeille').hide();
		    $('#page_fin').hide();
	            $('#page_parti').hide();
		    
            });
        });


        ALMemory.subscriber("web_projet/Page1").done(function(subscriber) {
			
 // on montre la page du choix des objets
			
            subscriber.signal.connect(function() {
              		$('#page_empty').hide();
   			$('#page_choix').show();
    		        $('#page_corbeille').hide();
			$('#page_fin').hide();
  			$('#page_parti').hide();
			

            });
        });

        ALMemory.subscriber("web_projet/Page2").done(function(subscriber) {

 // on montre la page du choix de la corbeille  
			subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').show();
	       $('#page_fin').hide();
  	       $('#page_parti').hide();
	     
            });
        });

	ALMemory.subscriber("web_projet/Page3").done(function(subscriber) {

// on montre la page de la validation des choix
		
            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').hide();
	       $('#page_fin').show();
  	       $('#page_parti').hide();
	     
            });
        });

	ALMemory.subscriber("web_projet/Page4").done(function(subscriber) {
		
// on montre la page de fin, celle qui s'affiche si les choix ont été validés

            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').hide();
	       $('#page_fin').hide();
  	       $('#page_parti').show();
	     
            });
        });

	
	});

	
// on définit ci-dessous un certain nombre de cliques; en effet, chaque clique va être défini ici
// puis utilisé dans le ".top" pour mener à bien notre scénario
	
    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }

    $('#go').on('click', function() {
        console.log("click Start");
        raise('web_projet/Start', 1) 
    });


    $('#pizza').on('click', function() {
        console.log("click 1");
	raise('my_object','pizza')  //De plus, on définit un ALMemory afin de récupérer la valeur 
							   //du clique et ainsi de savoir quel objet et quelle corbeille ont été choisis pour que le robot puisse
							  //effectuer sa tâche
		
        raise('web_projet/Button1', 1) 
    });

    $('#banane').on('click', function() {
        console.log("click 2");
	raise('my_object','banane')
        raise('web_projet/Button2', 1)
    });

    $('#vin').on('click', function() {
        console.log("click 3");
	raise('my_object','vin')
        raise('web_projet/Button3', 1)
    });

    $('#rouge').on('click', function() {
        console.log("click 4");
	raise('my_object','rouge')
        raise('web_projet/Button4', 1)
    });
	
    $('#jaune').on('click', function() {
        console.log("click 5");
	raise('my_object','jaune')
        raise('web_projet/Button5', 1)
    });
	
    $('#verte').on('click', function() {
        console.log("click 6");
	raise('my_object','verte')
        raise('web_projet/Button6', 1)
    });

    $('#end').on('click', function() {
        console.log("click 7");
	raise('my_choice','1')
        raise('web_projet/Button7', 1)
    });

    $('#restart').on('click', function() {
        console.log("click 8");
	raise('my_choice','0') // On définit un ALMemory "my_choice" nous permettant de savoir si la simulation peut démarrer
        raise('web_projet/Button8', 1)
    });


});