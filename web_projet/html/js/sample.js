$(document).ready(function () {
    session = new QiSession("127.0.0.1:8002", "1.0");

    $('#page_empty').show();
    $('#page_choix').hide();
    $('#page_corbeille').hide();
    $('#page_fin').hide();
    $('#page_parti').hide();
    


    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("web_projet/Page0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                    $('#page_empty').show();
   		    $('#page_choix').hide();
    		    $('#page_corbeille').hide();
		    $('#page_fin').hide();
	            $('#page_parti').hide();
		    
            });
        });


        ALMemory.subscriber("web_projet/Page1").done(function(subscriber) {

            subscriber.signal.connect(function() {
              		$('#page_empty').hide();
   			$('#page_choix').show();
    		        $('#page_corbeille').hide();
			$('#page_fin').hide();
  			$('#page_parti').hide();
			

            });
        });

        ALMemory.subscriber("web_projet/Page2").done(function(subscriber) {

            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').show();
	       $('#page_fin').hide();
  	       $('#page_parti').hide();
	     
            });
        });

	ALMemory.subscriber("web_projet/Page3").done(function(subscriber) {

            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').hide();
	       $('#page_fin').show();
  	       $('#page_parti').hide();
	     
            });
        });

	ALMemory.subscriber("web_projet/Page4").done(function(subscriber) {

            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   	       $('#page_choix').hide();
    	       $('#page_corbeille').hide();
	       $('#page_fin').hide();
  	       $('#page_parti').show();
	     
            });
        });

	
	});

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
	raise('my_object','pizza')
        raise('web_projet/Button1', 1)
    });

    $('#pomme').on('click', function() {
        console.log("click 2");
	raise('my_object','pomme')
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
	raise('my_choice','0')
        raise('web_projet/Button8', 1)
    });


});