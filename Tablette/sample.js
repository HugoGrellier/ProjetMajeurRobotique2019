$(document).ready(function () {
    session = new QiSession();

    $('#mpage_empty').show();
    $('#page_choix').hide();
    $('#page_corbeille').hide();


    session.service("ALMemory").done(function(ALMemory) {

        ALMemory.subscriber("Tablette/Page0").done(function(subscriber) {

            subscriber.signal.connect(function() {
                    $('#page_empty').show();
   				 	$('#page_choix').hide();
    				$('#page_corbeille').hide();
            });
        });


        ALMemory.subscriber("Tablette/Page1").done(function(subscriber) {

            subscriber.signal.connect(function() {
              		$('#page_empty').hide();
   				 	$('#page_choix').show();
    				$('#page_corbeille').hide();

            });
        });

        ALMemory.subscriber("Tablette/Page2").done(function(subscriber) {

            subscriber.signal.connect(function() {
               $('#page_empty').hide();
   			   $('#page_choix').hide();
    		   $('#page_corbeille').show();
            });
        });
    });
	

    function raise(event, value) {
        session.service("ALMemory").done(function(ALMemory) {
            ALMemory.raiseEvent(event, value);
        });
    }

	$('#pizza).on('click', function() {
        console.log("click 1");
        raise('Tablette/Page2', 1)
    });

    $('#pomme').on('click', function() {
        console.log("click 2");s
        raise('Tablette/Page2', 1)
    });

    $('#vin').on('click', function() {
        console.log("click 3");
        raise('Tablette/Page2', 1)
    });

    $('#rouge').on('click', function() {
        console.log("click 4");
        raise('TablettePage1', 1)
    });
	
	 $('#bleue').on('click', function() {
        console.log("click 5");
        raise('Tablette/Page1', 1)
    });
	
	 $('#verte').on('click', function() {
        console.log("click 6");
        raise('Tablette/Page1', 1)
    });


});
