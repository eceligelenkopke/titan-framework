(function( $ ) {
	wp.customize.bind( 'ready', function() {

		var optPrefix = '#customize-control-grocery_marketplace_options-';
		
		// Label
		function grocery_marketplace_customizer_label( id, title ) {

			// Site Identity

			if ( id === 'custom_logo' || id === 'site_icon' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Global Color Setting

			if ( id === 'grocery_marketplace_first_color' || id === 'grocery_marketplace_heading_color' || id === 'grocery_marketplace_paragraph_color') {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// General Setting

			if ( id === 'grocery_marketplace_scroll_hide' || id === 'grocery_marketplace_preloader_hide' || id === 'grocery_marketplace_sticky_header' || id === 'grocery_marketplace_products_per_row' || id === 'grocery_marketplace_scroll_top_position' || id === 'grocery_marketplace_products_per_row' || id === 'grocery_marketplace_width_option' || id === 'grocery_marketplace_nav_menu_text_transform')  {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Colors

			if ( id === 'grocery_marketplace_theme_color' || id === 'background_color' || id === 'background_image' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Header Image

			if ( id === 'header_image' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			//  Header
			
			if ( id === 'grocery_marketplace_header_search_setting' || id === 'grocery_marketplace_header_btn_text') {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}


			// Banner

			if ( id === 'grocery_marketplace_banner_section_setting' || id === 'grocery_marketplace_banner_review_head' || id === 'grocery_marketplace_banner_image1' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Products

			if ( id === 'grocery_marketplace_activities_section_setting' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Footer

			if ( id === 'grocery_marketplace_footer_widget_content_alignment' || id === 'grocery_marketplace_show_hide_copyright') {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Post Settings

			if ( id === 'grocery_marketplace_post_page_title' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}

			// Single Post Settings

			if ( id === 'grocery_marketplace_single_post_page_content' ) {
				$( '#customize-control-'+ id ).before('<li class="tab-title customize-control">'+ title  +'</li>');
			} else {
				$( '#customize-control-grocery_marketplace_options-'+ id ).before('<li class="tab-title customize-control">'+ title +'</li>');
			}
			
		}

	    // Site Identity
		grocery_marketplace_customizer_label( 'custom_logo', 'Logo Setup' );
		grocery_marketplace_customizer_label( 'site_icon', 'Favicon' );

		// Global Color Setting
		grocery_marketplace_customizer_label( 'grocery_marketplace_first_color', 'Global Color' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_heading_color', 'Heading Typography' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_paragraph_color', 'Paragraph Typography' );

		// General Setting
		grocery_marketplace_customizer_label( 'grocery_marketplace_preloader_hide', 'Preloader' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_scroll_hide', 'Scroll To Top' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_scroll_top_position', 'Scroll to top Position' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_products_per_row', 'woocommerce Setting' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_width_option', 'Site Width Layouts' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_nav_menu_text_transform', 'Nav Menus Text Transform' );

		// Colors
		grocery_marketplace_customizer_label( 'grocery_marketplace_theme_color', 'Theme Color' );
		grocery_marketplace_customizer_label( 'background_color', 'Colors' );
		grocery_marketplace_customizer_label( 'background_image', 'Image' );

		//Header Image
		grocery_marketplace_customizer_label( 'header_image', 'Header Image' );

		// Header 
		grocery_marketplace_customizer_label( 'grocery_marketplace_header_search_setting', 'Search' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_header_btn_text', 'Header Button' );

		//Slider
		grocery_marketplace_customizer_label( 'grocery_marketplace_banner_section_setting', 'Banner' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_banner_review_head', 'Client Review' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_banner_image1', 'Banner Images' );

		//Products
		grocery_marketplace_customizer_label( 'grocery_marketplace_service_section', 'Service Section' );

		//Footer
		grocery_marketplace_customizer_label( 'grocery_marketplace_footer_widget_content_alignment', 'Footer' );
		grocery_marketplace_customizer_label( 'grocery_marketplace_show_hide_copyright', 'Copyright' );

		//Post setting
		grocery_marketplace_customizer_label( 'grocery_marketplace_post_page_title', 'Post Settings' );

		//Single post setting
		grocery_marketplace_customizer_label( 'grocery_marketplace_single_post_page_content', 'Single Post Settings' );
	

	});

})( jQuery );
