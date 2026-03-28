<?php
/**
 * Grocery Marketplace Theme Customizer
 *
 * @link: https://developer.wordpress.org/themes/customize-api/customizer-objects/
 *
 * @package Grocery Marketplace
 */

if ( ! function_exists( 'grocery_marketplace_file_setup' ) ) :

    function grocery_marketplace_file_setup() {

        if ( ! defined( 'GROCERY_MARKETPLACE_URL' ) ) {
            define( 'GROCERY_MARKETPLACE_URL', esc_url( 'https://www.themagnifico.net/products/marketplace-wordpress-theme', 'grocery-marketplace') );
        }
        if ( ! defined( 'GROCERY_MARKETPLACE_TEXT' ) ) {
            define( 'GROCERY_MARKETPLACE_TEXT', __( 'Grocery Marketplace Pro','grocery-marketplace' ));
        }
        if ( ! defined( 'GROCERY_MARKETPLACE_BUY_TEXT' ) ) {
            define( 'GROCERY_MARKETPLACE_BUY_TEXT', __( 'Buy Grocery Marketplace Pro','grocery-marketplace' ));
        }

    }
endif;
add_action( 'after_setup_theme', 'grocery_marketplace_file_setup' );

use WPTRT\Customize\Section\Grocery_Marketplace_Button;

add_action( 'customize_register', function( $manager ) {

    $manager->register_section_type( Grocery_Marketplace_Button::class );

    $manager->add_section(
        new Grocery_Marketplace_Button( $manager, 'grocery_marketplace_pro', [
            'title'       => esc_html( GROCERY_MARKETPLACE_TEXT,'grocery-marketplace' ),
            'priority'    => 0,
            'button_text' => __( 'GET PREMIUM', 'grocery-marketplace' ),
            'button_url'  => esc_url( GROCERY_MARKETPLACE_URL )
        ] )
    );

} );

// Load the JS and CSS.
add_action( 'customize_controls_enqueue_scripts', function() {

    $version = wp_get_theme()->get( 'Version' );

    wp_enqueue_script(
        'grocery-marketplace-customize-section-button',
        get_theme_file_uri( 'vendor/wptrt/customize-section-button/public/js/customize-controls.js' ),
        [ 'customize-controls' ],
        $version,
        true
    );

    wp_enqueue_style(
        'grocery-marketplace-customize-section-button',
        get_theme_file_uri( 'vendor/wptrt/customize-section-button/public/css/customize-controls.css' ),
        [ 'customize-controls' ],
        $version
    );

} );

/**
 * Add postMessage support for site title and description for the Theme Customizer.
 *
 * @param WP_Customize_Manager $wp_customize Theme Customizer object.
 */
function grocery_marketplace_customize_register($wp_customize){

    // Pro Version
    class Grocery_Marketplace_Customize_Pro_Version extends WP_Customize_Control {
        public $type = 'pro_options';

        public function render_content() {
            echo '<span>For More <strong>'. esc_html( $this->label ) .'</strong>?</span>';
            echo '<a href="'. esc_url($this->description) .'" target="_blank">';
                echo '<span class="dashicons dashicons-info"></span>';
                echo '<strong> '. esc_html( GROCERY_MARKETPLACE_BUY_TEXT  ,'grocery-marketplace' ) .'<strong></a>';
            echo '</a>';
        }
    }

    // Custom Controls
    function grocery_marketplace_sanitize_custom_control( $input ) {
        return $input;
    }

    $wp_customize->get_setting('blogname')->transport = 'postMessage';
    $wp_customize->get_setting('blogdescription')->transport = 'postMessage';

    $wp_customize->add_setting('grocery_marketplace_logo_title_text', array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_logo_title_text',array(
        'label'          => __( 'Enable Disable Title', 'grocery-marketplace' ),
        'section'        => 'title_tagline',
        'settings'       => 'grocery_marketplace_logo_title_text',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_logo_title_font_size',array(
        'default'   => '',
        'sanitize_callback' => 'grocery_marketplace_sanitize_number_absint'
    ));
    $wp_customize->add_control('grocery_marketplace_logo_title_font_size',array(
        'label' => esc_html__('Title Font Size','grocery-marketplace'),
        'section' => 'title_tagline',
        'type'    => 'number'
    ));

    $wp_customize->add_setting('grocery_marketplace_theme_description', array(
        'default' => false,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_theme_description',array(
        'label'          => __( 'Enable Disable Tagline', 'grocery-marketplace' ),
        'section'        => 'title_tagline',
        'settings'       => 'grocery_marketplace_theme_description',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_logo_tagline_font_size',array(
        'default'   => '',
        'sanitize_callback' => 'grocery_marketplace_sanitize_number_absint'
    ));
    $wp_customize->add_control('grocery_marketplace_logo_tagline_font_size',array(
        'label' => esc_html__('Tagline Font Size','grocery-marketplace'),
        'section'   => 'title_tagline',
        'type'      => 'number'
    ));

    //Logo
    $wp_customize->add_setting('grocery_marketplace_logo_max_height',array(
        'default'   => '200',
        'sanitize_callback' => 'grocery_marketplace_sanitize_number_absint'
    ));
    $wp_customize->add_control('grocery_marketplace_logo_max_height',array(
        'label' => esc_html__('Logo Width','grocery-marketplace'),
        'section'   => 'title_tagline',
        'type'      => 'number'
    ));

    // Global Color Settings
     $wp_customize->add_section('grocery_marketplace_global_color_settings',array(
        'title' => esc_html__('Global Settings','grocery-marketplace'),
        'priority'   => 28,
    ));

    $wp_customize->add_setting( 'grocery_marketplace_first_color', array(
        'default' => '#0C7735',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_first_color', array(
        'label' => __('Select Your First Color', 'grocery-marketplace'),
        'description' => __('Change the global color of the theme in one click.', 'grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'settings' => 'grocery_marketplace_first_color',
    )));

    $wp_customize->add_setting( 'grocery_marketplace_second_color', array(
        'default' => '#E7461D',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_second_color', array(
        'label' => __('Select Your Second Color', 'grocery-marketplace'),
        'description' => __('Change the global color of the theme in one click.', 'grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'settings' => 'grocery_marketplace_second_color',
    )));

    //Typography option
    $grocery_marketplace_font_array = array(
        ''                       => 'No Fonts',
        'Abril Fatface'          => 'Abril Fatface',
        'Acme'                   => 'Acme',
        'Anton'                  => 'Anton',
        'Architects Daughter'    => 'Architects Daughter',
        'Arimo'                  => 'Arimo',
        'Arsenal'                => 'Arsenal',
        'Arvo'                   => 'Arvo',
        'Alegreya'               => 'Alegreya',
        'Alfa Slab One'          => 'Alfa Slab One',
        'Averia Serif Libre'     => 'Averia Serif Libre',
        'Bangers'                => 'Bangers',
        'Boogaloo'               => 'Boogaloo',
        'Bad Script'             => 'Bad Script',
        'Bitter'                 => 'Bitter',
        'Bree Serif'             => 'Bree Serif',
        'BenchNine'              => 'BenchNine',
        'Cabin'                  => 'Cabin',
        'Cardo'                  => 'Cardo',
        'Courgette'              => 'Courgette',
        'Cherry Swash'           => 'Cherry Swash',
        'Cormorant Garamond'     => 'Cormorant Garamond',
        'Crimson Text'           => 'Crimson Text',
        'Cuprum'                 => 'Cuprum',
        'Cookie'                 => 'Cookie',
        'Chewy'                  => 'Chewy',
        'Days One'               => 'Days One',
        'Dosis'                  => 'Dosis',
        'Droid Sans'             => 'Droid Sans',
        'Economica'              => 'Economica',
        'Fredoka One'            => 'Fredoka One',
        'Fjalla One'             => 'Fjalla One',
        'Francois One'           => 'Francois One',
        'Frank Ruhl Libre'       => 'Frank Ruhl Libre',
        'Gloria Hallelujah'      => 'Gloria Hallelujah',
        'Great Vibes'            => 'Great Vibes',
        'Handlee'                => 'Handlee',
        'Hammersmith One'        => 'Hammersmith One',
        'Inconsolata'            => 'Inconsolata',
        'Indie Flower'           => 'Indie Flower',
        'IM Fell English SC'     => 'IM Fell English SC',
        'Julius Sans One'        => 'Julius Sans One',
        'Josefin Slab'           => 'Josefin Slab',
        'Josefin Sans'           => 'Josefin Sans',
        'Kanit'                  => 'Kanit',
        'Lobster'                => 'Lobster',
        'Lato'                   => 'Lato',
        'Lora'                   => 'Lora',
        'Libre Baskerville'      => 'Libre Baskerville',
        'Lobster Two'            => 'Lobster Two',
        'Merriweather'           => 'Merriweather',
        'Monda'                  => 'Monda',
        'Montserrat'             => 'Montserrat',
        'Muli'                   => 'Muli',
        'Marck Script'           => 'Marck Script',
        'Noto Serif'             => 'Noto Serif',
        'Open Sans'              => 'Open Sans',
        'Overpass'               => 'Overpass',
        'Overpass Mono'          => 'Overpass Mono',
        'Oxygen'                 => 'Oxygen',
        'Orbitron'               => 'Orbitron',
        'Patua One'              => 'Patua One',
        'Pacifico'               => 'Pacifico',
        'Padauk'                 => 'Padauk',
        'Playball'               => 'Playball',
        'Playfair Display'       => 'Playfair Display',
        'PT Sans'                => 'PT Sans',
        'Philosopher'            => 'Philosopher',
        'Permanent Marker'       => 'Permanent Marker',
        'Poiret One'             => 'Poiret One',
        'Quicksand'              => 'Quicksand',
        'Quattrocento Sans'      => 'Quattrocento Sans',
        'Raleway'                => 'Raleway',
        'Rubik'                  => 'Rubik',
        'Roboto'                 => 'Roboto',
        'Rokkitt'                => 'Rokkitt',
        'Russo One'              => 'Russo One',
        'Righteous'              => 'Righteous',
        'Slabo'                  => 'Slabo',
        'Source Sans Pro'        => 'Source Sans Pro',
        'Shadows Into Light Two' => 'Shadows Into Light Two',
        'Shadows Into Light'     => 'Shadows Into Light',
        'Sacramento'             => 'Sacramento',
        'Shrikhand'              => 'Shrikhand',
        'Tangerine'              => 'Tangerine',
        'Ubuntu'                 => 'Ubuntu',
        'VT323'                  => 'VT323',
        'Varela Round'           => 'Varela Round',
        'Vampiro One'            => 'Vampiro One',
        'Vollkorn'               => 'Vollkorn',
        'Volkhov'                => 'Volkhov',
        'Yanone Kaffeesatz'      => 'Yanone Kaffeesatz'
    );

    // Heading Typography
    $wp_customize->add_setting( 'grocery_marketplace_heading_color', array(
        'default' => '',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_heading_color', array(
        'label' => __('Heading Color', 'grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'settings' => 'grocery_marketplace_heading_color',
    )));

    $wp_customize->add_setting('grocery_marketplace_heading_font_family', array(
        'default'           => '',
        'capability'        => 'edit_theme_options',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices',
    ));
    $wp_customize->add_control( 'grocery_marketplace_heading_font_family', array(
        'section' => 'grocery_marketplace_global_color_settings',
        'label'   => __('Heading Fonts', 'grocery-marketplace'),
        'type'    => 'select',
        'choices' => $grocery_marketplace_font_array,
    ));

    $wp_customize->add_setting('grocery_marketplace_heading_font_size',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_heading_font_size',array(
        'label' => esc_html__('Heading Font Size','grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'setting' => 'grocery_marketplace_heading_font_size',
        'type'  => 'text'
    ));

    // Paragraph Typography
    $wp_customize->add_setting( 'grocery_marketplace_paragraph_color', array(
        'default' => '',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_paragraph_color', array(
        'label' => __('Paragraph Color', 'grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'settings' => 'grocery_marketplace_paragraph_color',
    )));

    $wp_customize->add_setting('grocery_marketplace_paragraph_font_family', array(
        'default'           => '',
        'capability'        => 'edit_theme_options',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices',
    ));
    $wp_customize->add_control( 'grocery_marketplace_paragraph_font_family', array(
        'section' => 'grocery_marketplace_global_color_settings',
        'label'   => __('Paragraph Fonts', 'grocery-marketplace'),
        'type'    => 'select',
        'choices' => $grocery_marketplace_font_array,
    ));

    $wp_customize->add_setting('grocery_marketplace_paragraph_font_size',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_paragraph_font_size',array(
        'label' => esc_html__('Paragraph Font Size','grocery-marketplace'),
        'section' => 'grocery_marketplace_global_color_settings',
        'setting' => 'grocery_marketplace_paragraph_font_size',
        'type'  => 'text'
    ));

    // Post Layouts Settings
     $wp_customize->add_section('grocery_marketplace_post_layouts_settings',array(
        'title' => esc_html__('Post Layouts Settings','grocery-marketplace'),
        'priority'   => 30,
    ));

    $wp_customize->add_setting('grocery_marketplace_post_layout',array(
        'default' => 'pattern_two_column_right',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control(new Grocery_Marketplace_Image_Radio_Control($wp_customize, 'grocery_marketplace_post_layout', array(
        'type' => 'select',
        'label' => __('Blog Post Layouts','grocery-marketplace'),
        'section' => 'grocery_marketplace_post_layouts_settings',
        'choices' => array(
            'pattern_one_column' => esc_url(get_template_directory_uri()).'/assets/img/1column.png',
            'pattern_two_column_right' => esc_url(get_template_directory_uri()).'/assets/img/right-sidebar.png',
            'pattern_two_column_left' => esc_url(get_template_directory_uri()).'/assets/img/left-sidebar.png',
            'pattern_three_column' => esc_url(get_template_directory_uri()).'/assets/img/3column.png',
            'pattern_four_column' => esc_url(get_template_directory_uri()).'/assets/img/4column.png',
            'pattern_grid_post' => esc_url(get_template_directory_uri()).'/assets/img/grid.png',
    ))
    ));

    // General Settings
     $wp_customize->add_section('grocery_marketplace_general_settings',array(
        'title' => esc_html__('General Settings','grocery-marketplace'),
        'priority'   => 30,
    ));

     $wp_customize->add_setting('grocery_marketplace_width_option',array(
        'default' => 'Full Width',
        'transport' => 'refresh',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_width_option',array(
        'type' => 'select',
        'section' => 'grocery_marketplace_general_settings',
        'choices' => array(
            'Full Width' => __('Full Width','grocery-marketplace'),
            'Wide Width' => __('Wide Width','grocery-marketplace'),
            'Boxed Width' => __('Boxed Width','grocery-marketplace')
        ),
    ) );

    $wp_customize->add_setting('grocery_marketplace_nav_menu_text_transform',array(
        'default'=> 'Capitalize',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_nav_menu_text_transform',array(
        'type' => 'radio',
        'choices' => array(
            'Uppercase' => __('Uppercase','grocery-marketplace'),
            'Capitalize' => __('Capitalize','grocery-marketplace'),
            'Lowercase' => __('Lowercase','grocery-marketplace'),
        ),
        'section'=> 'grocery_marketplace_general_settings',
    ));

    $wp_customize->add_setting('grocery_marketplace_preloader_hide', array(
        'default' => 0,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_preloader_hide',array(
        'label'          => __( 'Show Theme Preloader', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_general_settings',
        'settings'       => 'grocery_marketplace_preloader_hide',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting( 'grocery_marketplace_preloader_bg_color', array(
        'default' => '#0C7735',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_preloader_bg_color', array(
        'label' => esc_html__('Preloader Background Color','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'settings' => 'grocery_marketplace_preloader_bg_color'
    )));

    $wp_customize->add_setting( 'grocery_marketplace_preloader_dot_1_color', array(
        'default' => '#ffffff',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_preloader_dot_1_color', array(
        'label' => esc_html__('Preloader First Dot Color','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'settings' => 'grocery_marketplace_preloader_dot_1_color'
    )));

    $wp_customize->add_setting( 'grocery_marketplace_preloader_dot_2_color', array(
        'default' => '#222222',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_preloader_dot_2_color', array(
        'label' => esc_html__('Preloader Second Dot Color','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'settings' => 'grocery_marketplace_preloader_dot_2_color'
    )));

    $wp_customize->add_setting('grocery_marketplace_scroll_hide', array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_scroll_hide',array(
        'label'          => __( 'Show Theme Scroll To Top', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_general_settings',
        'settings'       => 'grocery_marketplace_scroll_hide',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_scroll_top_position',array(
        'default' => 'Right',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_scroll_top_position',array(
        'type' => 'radio',
        'section' => 'grocery_marketplace_general_settings',
        'choices' => array(
            'Right' => __('Right','grocery-marketplace'),
            'Left' => __('Left','grocery-marketplace'),
            'Center' => __('Center','grocery-marketplace')
        ),
    ) );

    $wp_customize->add_setting( 'grocery_marketplace_scroll_bg_color', array(
        'default' => '',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_scroll_bg_color', array(
        'label' => esc_html__('Scroll Top Background Color','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'settings' => 'grocery_marketplace_scroll_bg_color'
    )));

    $wp_customize->add_setting( 'grocery_marketplace_scroll_color', array(
        'default' => '',
        'sanitize_callback' => 'sanitize_hex_color'
    ));
    $wp_customize->add_control( new WP_Customize_Color_Control( $wp_customize, 'grocery_marketplace_scroll_color', array(
        'label' => esc_html__('Scroll Top Color','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'settings' => 'grocery_marketplace_scroll_color'
    )));

    $wp_customize->add_setting('grocery_marketplace_scroll_font_size',array(
        'default'   => '16',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_scroll_font_size',array(
        'label' => __('Scroll Top Font Size','grocery-marketplace'),
        'description' => __('Put in px','grocery-marketplace'),
        'section'   => 'grocery_marketplace_general_settings',
        'type'      => 'number'
    ));

    $wp_customize->add_setting('grocery_marketplace_scroll_border_radius',array(
        'default'   => '0',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_scroll_border_radius',array(
        'label' => __('Scroll Top Border Radius','grocery-marketplace'),
        'description' => __('Put in %','grocery-marketplace'),
        'section'   => 'grocery_marketplace_general_settings',
        'type'      => 'number'
    ));

    // Product Columns
    $wp_customize->add_setting( 'grocery_marketplace_products_per_row' , array(
       'default'           => '3',
       'transport'         => 'refresh',
       'sanitize_callback' => 'grocery_marketplace_sanitize_select',
    ) );

    $wp_customize->add_control('grocery_marketplace_products_per_row', array(
       'label' => __( 'Product per row', 'grocery-marketplace' ),
       'section'  => 'grocery_marketplace_general_settings',
       'type'     => 'select',
       'choices'  => array(
           '2' => '2',
           '3' => '3',
           '4' => '4',
       ),
    ) );

    $wp_customize->add_setting('grocery_marketplace_product_per_page',array(
        'default'   => '9',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_product_per_page',array(
        'label' => __('Product per page','grocery-marketplace'),
        'section'   => 'grocery_marketplace_general_settings',
        'type'      => 'number'
    ));

    // Product Columns
    $wp_customize->add_setting('custom_related_products_number_per_row',array(
        'default'           => '3',
        'transport'         => 'refresh',
        'sanitize_callback' => 'sanitize_text_field',
    ));

    $wp_customize->add_control('custom_related_products_number_per_row',array(
        'label'       => esc_html__('Related Products Column Count', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_general_settings',
        'type'        => 'number',
        'input_attrs' => array(
            'step' => 1,
            'min'  => 1,
            'max'  => 4,
        ),
    ));

    // Product Columns
    $wp_customize->add_setting('custom_related_products_number',array(
        'default'           => '3',
        'transport'         => 'refresh',
        'sanitize_callback' => 'sanitize_text_field',
    ));

    $wp_customize->add_control('custom_related_products_number',array(
        'label'       => esc_html__('Number of Related Products Per Page', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_general_settings',
        'type'        => 'number',
        'input_attrs' => array(
            'step' => 1,
            'min'  => 1,
            'max'  => 10,
        ),
    ));

    $wp_customize->add_setting('grocery_marketplace_related_product_display_setting', array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_related_product_display_setting',array(
        'label'          => __( 'Show Related Products', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_general_settings',
        'settings'       => 'grocery_marketplace_related_product_display_setting',
        'type'           => 'checkbox',
    )));

    //Woocommerce shop page Sidebar
    $wp_customize->add_setting('grocery_marketplace_woocommerce_shop_page_sidebar', array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_woocommerce_shop_page_sidebar',array(
        'label'          => __( 'Hide Shop Page Sidebar', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_general_settings',
        'settings'       => 'grocery_marketplace_woocommerce_shop_page_sidebar',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_shop_page_sidebar_layout',array(
        'default' => 'Right Sidebar',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_shop_page_sidebar_layout',array(
        'type' => 'select',
        'label' => __('Woocommerce Shop Page Sidebar','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'choices' => array(
            'Left Sidebar' => __('Left Sidebar','grocery-marketplace'),
            'Right Sidebar' => __('Right Sidebar','grocery-marketplace'),
        ),
    ) );

    //Woocommerce Single Product page Sidebar
    $wp_customize->add_setting('grocery_marketplace_woocommerce_single_product_page_sidebar', array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_woocommerce_single_product_page_sidebar',array(
        'label'          => __( 'Hide Single Product Page Sidebar', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_general_settings',
        'settings'       => 'grocery_marketplace_woocommerce_single_product_page_sidebar',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_single_product_sidebar_layout',array(
        'default' => 'Right Sidebar',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_single_product_sidebar_layout',array(
        'type' => 'select',
        'label' => __('Woocommerce Single Product Page Sidebar','grocery-marketplace'),
        'section' => 'grocery_marketplace_general_settings',
        'choices' => array(
            'Left Sidebar' => __('Left Sidebar','grocery-marketplace'),
            'Right Sidebar' => __('Right Sidebar','grocery-marketplace'),
        ),
    ) );

    //Header
    $wp_customize->add_section('grocery_marketplace_header',array(
        'title' => esc_html__('Header Option','grocery-marketplace')
    ));

    $wp_customize->add_setting('grocery_marketplace_topbar_text',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_topbar_text',array(
        'label' => esc_html__('Topbar Text','grocery-marketplace'),
        'section' => 'grocery_marketplace_header',
        'setting' => 'grocery_marketplace_topbar_text',
        'type'  => 'text'
    ));

    $wp_customize->add_setting('grocery_marketplace_track_order_shortcode',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_track_order_shortcode',array(
        'label' => esc_html__('Track Order Shortcode','grocery-marketplace'),
        'section' => 'grocery_marketplace_header',
        'setting' => 'grocery_marketplace_track_order_shortcode',
        'type'  => 'text'
    ));

    $wp_customize->add_setting('grocery_marketplace_newsletter_shortcode',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_newsletter_shortcode',array(
        'label' => esc_html__('Newsletter Shortcode','grocery-marketplace'),
        'section' => 'grocery_marketplace_header',
        'setting' => 'grocery_marketplace_newsletter_shortcode',
        'type'  => 'text'
    ));

    $wp_customize->add_setting('grocery_marketplace_header_phone_text',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_header_phone_text',array(
        'label' => esc_html__('Phone Text','grocery-marketplace'),
        'section' => 'grocery_marketplace_header',
        'setting' => 'grocery_marketplace_header_phone_text',
        'type'  => 'text'
    ));

    $wp_customize->add_setting('grocery_marketplace_header_phone_number',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_header_phone_number',array(
        'label' => esc_html__('Phone Number','grocery-marketplace'),
        'section' => 'grocery_marketplace_header',
        'setting' => 'grocery_marketplace_header_phone_number',
        'type'  => 'text'
    ));

    //Slider
    $wp_customize->add_section('grocery_marketplace_top_slider',array(
        'title' => esc_html__('Slider Settings','grocery-marketplace'),
        'description' => esc_html__('Here you have to add 3 different pages in below dropdown. Note: Image Dimensions 1400 x 550 px','grocery-marketplace')
    ));

    $wp_customize->add_setting('grocery_marketplace_top_slider_setting', array(
        'default' => 0,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_top_slider_setting',array(
        'label'          => __( 'Enable Disable Slider', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_top_slider',
        'settings'       => 'grocery_marketplace_top_slider_setting',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_slider_title_setting', array(
        'default' => 1,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_slider_title_setting',array(
        'label'          => __( 'Enable Disable Slider Title', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_top_slider',
        'settings'       => 'grocery_marketplace_slider_title_setting',
        'type'           => 'checkbox',
    )));

    $wp_customize->add_setting('grocery_marketplace_slider_button_setting', array(
        'default' => 1,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control( new WP_Customize_Control($wp_customize,'grocery_marketplace_slider_button_setting',array(
        'label'          => __( 'Enable Disable Slider Button', 'grocery-marketplace' ),
        'section'        => 'grocery_marketplace_top_slider',
        'settings'       => 'grocery_marketplace_slider_button_setting',
        'type'           => 'checkbox',
    )));

    for ( $grocery_marketplace_count = 1; $grocery_marketplace_count <= 3; $grocery_marketplace_count++ ) {

        $wp_customize->add_setting( 'grocery_marketplace_top_slider_page' . $grocery_marketplace_count, array(
            'default'           => '',
            'sanitize_callback' => 'grocery_marketplace_sanitize_dropdown_pages'
        ) );
        $wp_customize->add_control( 'grocery_marketplace_top_slider_page' . $grocery_marketplace_count, array(
            'label'    => __( 'Select Slide Page', 'grocery-marketplace' ),
            'description' => __('Slider image size (1400 x 550 px)','grocery-marketplace'),
            'section'  => 'grocery_marketplace_top_slider',
            'type'     => 'dropdown-pages'
        ) );
    }

    //Slider Short Heading
    $wp_customize->add_setting('grocery_marketplace_slider_short_heading',array(
        'default'=> '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_slider_short_heading',array(
        'label' => __('Slider Short Heading','grocery-marketplace'),
        'section'=> 'grocery_marketplace_top_slider',
        'type'=> 'text'
    ));

    //Slider Delivery Heading
    $wp_customize->add_setting('grocery_marketplace_slider_free_delivery_heading',array(
        'default'=> '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_slider_free_delivery_heading',array(
        'label' => __('Slider Delivery Heading','grocery-marketplace'),
        'section'=> 'grocery_marketplace_top_slider',
        'type'=> 'text'
    ));

    //Slider Offer Heading
    $wp_customize->add_setting('grocery_marketplace_slider_offer_heading',array(
        'default'=> '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_slider_offer_heading',array(
        'label' => __('Slider Offer Heading','grocery-marketplace'),
        'section'=> 'grocery_marketplace_top_slider',
        'type'=> 'text'
    ));

    //Slider button text
    $wp_customize->add_setting('grocery_marketplace_slider_button_text',array(
        'default'=> '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_slider_button_text',array(
        'label' => __('Slider Button Text','grocery-marketplace'),
        'section'=> 'grocery_marketplace_top_slider',
        'type'=> 'text'
    ));

    // Trending Product
    $wp_customize->add_section('grocery_marketplace_best_sells',array(
        'title' => esc_html__('Trending Product Option','grocery-marketplace')
    ));

    $wp_customize->add_setting('grocery_marketplace_best_sells_section_heading',array(
        'default' => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_best_sells_section_heading',array(
        'label' => __('Heading','grocery-marketplace'),
        'section' => 'grocery_marketplace_best_sells',
        'setting' => 'grocery_marketplace_best_sells_section_heading',
        'type'    => 'text'
    ));

    $wp_customize->add_setting('grocery_marketplace_tab_number',array(
        'default'           => '',
        'sanitize_callback' => 'sanitize_text_field'
    ));
    $wp_customize->add_control('grocery_marketplace_tab_number',array(
        'label'   => __('Types of Trending Product to show','grocery-marketplace'),
        'section' => 'grocery_marketplace_best_sells',
        'setting' => 'grocery_marketplace_tab_number',
        'type'    => 'number'
    ));

    $increse =  get_theme_mod('grocery_marketplace_tab_number');


    for($i=1; $i<= $increse; $i++) {
    

        $wp_customize->add_setting('grocery_marketplace_slideproduct_tab1title'.$i,array(
          'default' => '',
          'sanitize_callback' => 'sanitize_text_field',
        ));
        $wp_customize->add_control('grocery_marketplace_slideproduct_tab1title'.$i,array(
          'label' => __('Tab Heading','grocery-marketplace').$i,
          'section' => 'grocery_marketplace_best_sells',
          'setting' => 'grocery_marketplace_slideproduct_tab1title'.$i,
          'type'  => 'text'
        ));
        $args = array(
           'type'                     => 'product',
            'child_of'                 => 0,
            'parent'                   => '',
            'orderby'                  => 'term_group',
            'order'                    => 'ASC',
            'hide_empty'               => false,
            'hierarchical'             => 1,
            'number'                   => '',
            'taxonomy'                 => 'product_cat',
            'pad_counts'               => false
        );
      $categories = get_categories($args);
      $cat_posts = array();
      $m = 0;
      $cat_posts[]='Select';
      foreach($categories as $product){
        if($m==0){
          $default = $product->slug;
          $m++;
        }
        $cat_posts[$product->slug] = $product->name;
      }

      $wp_customize->add_setting('grocery_marketplace_cate_tab'.$i,array(
        'default' => 'select',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices',
      ));

      $wp_customize->add_control('grocery_marketplace_cate_tab'.$i,array(
        'type'    => 'select',
        'choices' => $cat_posts,
        'label' => __('Select category to display Trending Product ','grocery-marketplace').$i,
        'section' => 'grocery_marketplace_best_sells',
      ));
    }

    // Post Settings
     $wp_customize->add_section('grocery_marketplace_post_settings',array(
        'title' => esc_html__('Post Settings','grocery-marketplace'),
        'priority'   =>40,
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_title',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_title',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Post Page Title', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable title on post page.', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_meta',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_meta',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Post Page Meta', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable meta on post page.', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_thumb',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_thumb',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Post Page Thumbnail', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable thumbnail on post page.', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_content',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_content',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Post Page Content', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable content on post page.', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_excerpt_length',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_number_range',
        'default'           => 30,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_excerpt_length',array(
        'label'       => esc_html__('Post Page Excerpt Length', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'type'        => 'range',
        'input_attrs' => array(
            'step'             => 1,
            'min'              => 1,
            'max'              => 50,
        ),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_excerpt_suffix',array(
        'sanitize_callback' => 'sanitize_text_field',
        'default'           => '[...]',
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_excerpt_suffix',array(
        'type'        => 'text',
        'label'       => esc_html__('Post Page Excerpt Suffix', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('For Ex. [...], etc', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_post_page_pagination',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_post_page_pagination',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Post Page Pagination', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable pagination on post page.', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_single_post_page_content',array(
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox',
        'default'           => 1,
    ));
    $wp_customize->add_control('grocery_marketplace_single_post_page_content',array(
        'type'        => 'checkbox',
        'label'       => esc_html__('Enable Single Post Page Content', 'grocery-marketplace'),
        'section'     => 'grocery_marketplace_post_settings',
        'description' => esc_html__('Check this box to enable content on single post page.', 'grocery-marketplace'),
    ));
    
    // Footer
    $wp_customize->add_section('grocery_marketplace_site_footer_section', array(
        'title' => esc_html__('Footer', 'grocery-marketplace'),
    ));

    $wp_customize->add_setting('grocery_marketplace_footer_widget_content_alignment',array(
        'default' => 'Left',
        'transport' => 'refresh',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_footer_widget_content_alignment',array(
        'type' => 'select',
        'label' => __('Footer Widget Content Alignment','grocery-marketplace'),
        'section' => 'grocery_marketplace_site_footer_section',
        'choices' => array(
            'Left' => __('Left','grocery-marketplace'),
            'Center' => __('Center','grocery-marketplace'),
            'Right' => __('Right','grocery-marketplace')
        ),
    ) );

    $wp_customize->add_setting('grocery_marketplace_show_hide_copyright',array(
        'default' => true,
        'sanitize_callback' => 'grocery_marketplace_sanitize_checkbox'
    ));
    $wp_customize->add_control('grocery_marketplace_show_hide_copyright',array(
        'type' => 'checkbox',
        'label' => __('Show / Hide Copyright','grocery-marketplace'),
        'section' => 'grocery_marketplace_site_footer_section',
    ));

    $wp_customize->add_setting('grocery_marketplace_footer_text_setting', array(
        'sanitize_callback' => 'sanitize_text_field',
    ));
    $wp_customize->add_control('grocery_marketplace_footer_text_setting', array(
        'label' => __('Replace the footer text', 'grocery-marketplace'),
        'section' => 'grocery_marketplace_site_footer_section',
        'type' => 'text',
    ));

    $wp_customize->add_setting('grocery_marketplace_copyright_content_alignment',array(
        'default' => 'Center',
        'transport' => 'refresh',
        'sanitize_callback' => 'grocery_marketplace_sanitize_choices'
    ));
    $wp_customize->add_control('grocery_marketplace_copyright_content_alignment',array(
        'type' => 'select',
        'label' => __('Copyright Content Alignment','grocery-marketplace'),
        'section' => 'grocery_marketplace_site_footer_section',
        'choices' => array(
            'Left' => __('Left','grocery-marketplace'),
            'Center' => __('Center','grocery-marketplace'),
            'Right' => __('Right','grocery-marketplace')
        ),
    ) );
}
add_action('customize_register', 'grocery_marketplace_customize_register');

/**
 * Render the site title for the selective refresh partial.
 *
 * @return void
 */
function grocery_marketplace_customize_partial_blogname(){
    bloginfo('name');
}

/**
 * Render the site tagline for the selective refresh partial.
 *
 * @return void
 */
function grocery_marketplace_customize_partial_blogdescription(){
    bloginfo('description');
}

/**
 * Binds JS handlers to make Theme Customizer preview reload changes asynchronously.
 */
function grocery_marketplace_customize_preview_js(){
    wp_enqueue_script('grocery-marketplace-customizer', esc_url(get_template_directory_uri()) . '/assets/js/customizer.js', array('customize-preview'), '20151215', true);
}
add_action('customize_preview_init', 'grocery_marketplace_customize_preview_js');

/*
** Load dynamic logic for the customizer controls area.
*/
function grocery_marketplace_panels_js() {
    wp_enqueue_style( 'grocery-marketplace-customizer-layout-css', get_theme_file_uri( '/assets/css/customizer-layout.css' ) );
    wp_enqueue_script( 'grocery-marketplace-customize-layout', get_theme_file_uri( '/assets/js/customize-layout.js' ), array(), '1.2', true );
}
add_action( 'customize_controls_enqueue_scripts', 'grocery_marketplace_panels_js' );