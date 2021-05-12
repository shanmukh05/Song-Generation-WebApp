$(function() {

	'use strict';

	// Form

	var contactForm = function() {

		if ($('#contactForm').length > 0 ) {
			$( "#contactForm" ).validate( {
				rules: {
					name: "required",
					linecount : {
						required: true,
						number : true
					},
					wordcount : {
						required: true,
						number : true
					},
					firstline : {
						required: true,
						number : true
					},
				},
				messages: {
					name: "Please enter start word",
					linecount : "Please enter valid number",
					wordcount: "Please enter valid number",
					firstline : "Please enter valid number",
				},
				
			} );
		}
	};
	contactForm();

});