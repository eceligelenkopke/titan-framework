<?php

    $grocery_marketplace_theme_css= "";

    /*--------------------------- Scroll to top positions -------------------*/

    $grocery_marketplace_scroll_position = get_theme_mod( 'grocery_marketplace_scroll_top_position','Right');
    if($grocery_marketplace_scroll_position == 'Right'){
        $grocery_marketplace_theme_css .='#button{';
            $grocery_marketplace_theme_css .='right: 20px;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_scroll_position == 'Left'){
        $grocery_marketplace_theme_css .='#button{';
            $grocery_marketplace_theme_css .='left: 20px;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_scroll_position == 'Center'){
        $grocery_marketplace_theme_css .='#button{';
            $grocery_marketplace_theme_css .='right: 50%;left: 50%;';
        $grocery_marketplace_theme_css .='}';
    }

    /*--------------------------- Footer Widget Heading Alignment -------------------*/

    $grocery_marketplace_footer_widget_heading_alignment = get_theme_mod( 'grocery_marketplace_footer_widget_heading_alignment','Left');
    if($grocery_marketplace_footer_widget_heading_alignment == 'Left'){
        $grocery_marketplace_theme_css .='#colophon h5, h5.footer-column-widget-title{';
        $grocery_marketplace_theme_css .='text-align: left;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_footer_widget_heading_alignment == 'Center'){
        $grocery_marketplace_theme_css .='#colophon h5, h5.footer-column-widget-title{';
            $grocery_marketplace_theme_css .='text-align: center;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_footer_widget_heading_alignment == 'Right'){
        $grocery_marketplace_theme_css .='#colophon h5, h5.footer-column-widget-title{';
            $grocery_marketplace_theme_css .='text-align: right;';
        $grocery_marketplace_theme_css .='}';
    }

    /*--------------------------- Footer Widget Content Alignment -------------------*/

    $grocery_marketplace_footer_widget_content_alignment = get_theme_mod( 'grocery_marketplace_footer_widget_content_alignment','Left');
    if($grocery_marketplace_footer_widget_content_alignment == 'Left'){
        $grocery_marketplace_theme_css .='#colophon ul, #colophon p, .tagcloud, .widget{';
        $grocery_marketplace_theme_css .='text-align: left;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_footer_widget_content_alignment == 'Center'){
        $grocery_marketplace_theme_css .='#colophon ul, #colophon p, .tagcloud, .widget{';
            $grocery_marketplace_theme_css .='text-align: center;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_footer_widget_content_alignment == 'Right'){
        $grocery_marketplace_theme_css .='#colophon ul, #colophon p, .tagcloud, .widget{';
            $grocery_marketplace_theme_css .='text-align: right;';
        $grocery_marketplace_theme_css .='}';
    }

    /*--------------------------- Copyright Content Alignment -------------------*/

    $grocery_marketplace_copyright_content_alignment = get_theme_mod( 'grocery_marketplace_copyright_content_alignment','Center');
    if($grocery_marketplace_copyright_content_alignment == 'Left'){
        $grocery_marketplace_theme_css .='.footer-menu-left{';
        $grocery_marketplace_theme_css .='text-align: left !important;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_copyright_content_alignment == 'Center'){
        $grocery_marketplace_theme_css .='.footer-menu-left{';
            $grocery_marketplace_theme_css .='text-align: center !important;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_copyright_content_alignment == 'Right'){
        $grocery_marketplace_theme_css .='.footer-menu-left{';
            $grocery_marketplace_theme_css .='text-align: right !important;';
        $grocery_marketplace_theme_css .='}';
    }

    /*---------------------------Width Layout -------------------*/

    $grocery_marketplace_width_option = get_theme_mod( 'grocery_marketplace_width_option','Full Width');
    if($grocery_marketplace_width_option == 'Boxed Width'){
        $grocery_marketplace_theme_css .='body{';
            $grocery_marketplace_theme_css .='max-width: 1140px; width: 100%; padding-right: 15px; padding-left: 15px; margin-right: auto; margin-left: auto;';
        $grocery_marketplace_theme_css .='}';
        $grocery_marketplace_theme_css .='.scrollup i{';
            $grocery_marketplace_theme_css .='right: 100px;';
        $grocery_marketplace_theme_css .='}';
        $grocery_marketplace_theme_css .='.page-template-custom-home-page .home-page-header{';
            $grocery_marketplace_theme_css .='padding: 0px 40px 0 10px;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_width_option == 'Wide Width'){
        $grocery_marketplace_theme_css .='body{';
            $grocery_marketplace_theme_css .='width: 100%;padding-right: 15px;padding-left: 15px;margin-right: auto;margin-left: auto;';
        $grocery_marketplace_theme_css .='}';
        $grocery_marketplace_theme_css .='.scrollup i{';
            $grocery_marketplace_theme_css .='right: 30px;';
        $grocery_marketplace_theme_css .='}';
    }else if($grocery_marketplace_width_option == 'Full Width'){
        $grocery_marketplace_theme_css .='body{';
            $grocery_marketplace_theme_css .='max-width: 100%;';
        $grocery_marketplace_theme_css .='}';
    }

    /*------------------ Nav Menus -------------------*/

    $grocery_marketplace_nav_menu = get_theme_mod( 'grocery_marketplace_nav_menu_text_transform','Capitalize');
    if($grocery_marketplace_nav_menu == 'Capitalize'){
        $grocery_marketplace_theme_css .='.main-navigation .menu > li > a{';
            $grocery_marketplace_theme_css .='text-transform:Capitalize;';
        $grocery_marketplace_theme_css .='}';
    }
    if($grocery_marketplace_nav_menu == 'Lowercase'){
        $grocery_marketplace_theme_css .='.main-navigation .menu > li > a{';
            $grocery_marketplace_theme_css .='text-transform:Lowercase;';
        $grocery_marketplace_theme_css .='}';
    }
    if($grocery_marketplace_nav_menu == 'Uppercase'){
        $grocery_marketplace_theme_css .='.main-navigation .menu > li > a{';
            $grocery_marketplace_theme_css .='text-transform:Uppercase;';
        $grocery_marketplace_theme_css .='}';
    }

    /*-------------------- Global First Color -------------------*/

    $grocery_marketplace_first_color = get_theme_mod('grocery_marketplace_first_color');
    $grocery_marketplace_second_color = get_theme_mod('grocery_marketplace_second_color');

    if ($grocery_marketplace_first_color) {
        $grocery_marketplace_theme_css .= ':root {';
        $grocery_marketplace_theme_css .= '--first-color: ' . esc_attr($grocery_marketplace_first_color) . ' !important;';
        $grocery_marketplace_theme_css .= '} ';
    }
    
    if ($grocery_marketplace_second_color) {
        $grocery_marketplace_theme_css .= ':root {';
        $grocery_marketplace_theme_css .= '--second-color: ' . esc_attr($grocery_marketplace_second_color) . ' !important;';
        $grocery_marketplace_theme_css .= '} ';
    }

    

    /*-------------------- Heading typography -------------------*/

    $grocery_marketplace_heading_color = get_theme_mod('grocery_marketplace_heading_color');
    $grocery_marketplace_heading_font_family = get_theme_mod('grocery_marketplace_heading_font_family');
    $grocery_marketplace_heading_font_size = get_theme_mod('grocery_marketplace_heading_font_size');
    if($grocery_marketplace_heading_color != false || $grocery_marketplace_heading_font_family != false || $grocery_marketplace_heading_font_size != false){
        $grocery_marketplace_theme_css .='h1, h2, h3, h4, h5, h6, .navbar-brand h1.site-title, h2.entry-title, h1.entry-title, h2.page-title, #latest_post h2, h2.woocommerce-loop-product__title, #top-slider .slider-inner-box h3, .featured h3.main-heading, .article-box h3.entry-title, .featured h4.main-heading, #colophon h5, .sidebar h5{';
            $grocery_marketplace_theme_css .='color: '.esc_attr($grocery_marketplace_heading_color).'!important; 
            font-family: '.esc_attr($grocery_marketplace_heading_font_family).'!important;
            font-size: '.esc_attr($grocery_marketplace_heading_font_size).'px !important;';
        $grocery_marketplace_theme_css .='}';
    }

    $grocery_marketplace_paragraph_color = get_theme_mod('grocery_marketplace_paragraph_color');
    $grocery_marketplace_paragraph_font_family = get_theme_mod('grocery_marketplace_paragraph_font_family');
    $grocery_marketplace_paragraph_font_size = get_theme_mod('grocery_marketplace_paragraph_font_size');
    if($grocery_marketplace_paragraph_color != false || $grocery_marketplace_paragraph_font_family != false || $grocery_marketplace_paragraph_font_size != false){
        $grocery_marketplace_theme_css .='p, p.site-title, span, .article-box p, ul, li{';
            $grocery_marketplace_theme_css .='color: '.esc_attr($grocery_marketplace_paragraph_color).'!important; 
            font-family: '.esc_attr($grocery_marketplace_paragraph_font_family).'!important;
            font-size: '.esc_attr($grocery_marketplace_paragraph_font_size).'px !important;';
        $grocery_marketplace_theme_css .='}';
    }

    /*---------------- Logo CSS ----------------------*/
    $grocery_marketplace_logo_title_font_size = get_theme_mod( 'grocery_marketplace_logo_title_font_size');
    $grocery_marketplace_logo_tagline_font_size = get_theme_mod( 'grocery_marketplace_logo_tagline_font_size');
    if( $grocery_marketplace_logo_title_font_size != '') {
        $grocery_marketplace_theme_css .='#masthead .navbar-brand a{';
            $grocery_marketplace_theme_css .='font-size: '. $grocery_marketplace_logo_title_font_size. 'px;';
        $grocery_marketplace_theme_css .='}';
    }
    if( $grocery_marketplace_logo_tagline_font_size != '') {
        $grocery_marketplace_theme_css .='#masthead .navbar-brand p{';
            $grocery_marketplace_theme_css .='font-size: '. $grocery_marketplace_logo_tagline_font_size. 'px;';
        $grocery_marketplace_theme_css .='}';
    }