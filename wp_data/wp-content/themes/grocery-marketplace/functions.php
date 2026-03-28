<?php
/**
 * Grocery Marketplace functions and definitions
 *
 * @link https://developer.wordpress.org/themes/basics/theme-functions/
 *
 * @package Grocery Marketplace
 */

include get_theme_file_path( 'vendor/wptrt/autoload/src/Grocery_Marketplace_Loader.php' );

$Grocery_Marketplace_Loader = new \WPTRT\Autoload\Grocery_Marketplace_Loader();

$Grocery_Marketplace_Loader->grocery_marketplace_add( 'WPTRT\\Customize\\Section', get_theme_file_path( 'vendor/wptrt/customize-section-button/src' ) );

$Grocery_Marketplace_Loader->grocery_marketplace_register();

if ( ! function_exists( 'grocery_marketplace_setup' ) ) :

	function grocery_marketplace_setup() {

		/*
		 * Enable support for Post Formats.
		 *
		 * See: https://codex.wordpress.org/Post_Formats
		*/
		add_theme_support( 'post-formats', array('image','video','gallery','audio',) );

		load_theme_textdomain( 'grocery-marketplace', get_template_directory() . '/languages' );
		add_theme_support( 'woocommerce' );
		add_theme_support( "responsive-embeds" );
		add_theme_support( "align-wide" );
		add_theme_support( "wp-block-styles" );
		add_theme_support( 'automatic-feed-links' );
		add_theme_support( 'title-tag' );
		add_theme_support( 'post-thumbnails' );
        add_image_size('grocery-marketplace-featured-header-image', 2000, 660, true);

        register_nav_menus( array(
            'primary' => esc_html__( 'Primary','grocery-marketplace' ),
        ) );

		add_theme_support( 'html5', array(
			'search-form',
			'comment-form',
			'comment-list',
			'gallery',
			'caption',
		) );

		add_theme_support( 'custom-background', apply_filters( 'grocery_marketplace_custom_background_args', array(
			'default-color' => 'f7ebe5',
			'default-image' => '',
		) ) );

		add_theme_support( 'customize-selective-refresh-widgets' );

		add_theme_support( 'custom-logo', array(
			'height'      => 200,
			'width'       => 200,
			'flex-width'  => true,
		) );

		add_editor_style( array( '/editor-style.css' ) );
	}
endif;
add_action( 'after_setup_theme', 'grocery_marketplace_setup' );

function grocery_marketplace_content_width() {
	$GLOBALS['content_width'] = apply_filters( 'grocery_marketplace_content_width', 1170 );
}
add_action( 'after_setup_theme', 'grocery_marketplace_content_width', 0 );


/**
 * Register widget area.
 *
 * @link https://developer.wordpress.org/themes/functionality/sidebars/#registering-a-sidebar
 */
function grocery_marketplace_widgets_init() {
	register_sidebar( array(
		'name'          => esc_html__( 'Sidebar', 'grocery-marketplace' ),
		'id'            => 'sidebar',
		'description'   => esc_html__( 'Add widgets here.', 'grocery-marketplace' ),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
		'after_widget'  => '</section>',
		'before_title'  => '<h5 class="widget-title">',
		'after_title'   => '</h5>',
	) );

	register_sidebar( array(
		'name'          => esc_html__( 'Sidebar 1', 'grocery-marketplace' ),
		'id'            => 'sidebar1',
		'description'   => esc_html__( 'Add widgets here.', 'grocery-marketplace' ),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
		'after_widget'  => '</section>',
		'before_title'  => '<h5 class="widget-title">',
		'after_title'   => '</h5>',
	) );

	register_sidebar( array(
		'name'          => esc_html__( 'Sidebar 2', 'grocery-marketplace' ),
		'id'            => 'sidebar2',
		'description'   => esc_html__( 'Add widgets here.', 'grocery-marketplace' ),
        'before_widget' => '<section id="%1$s" class="widget %2$s">',
		'after_widget'  => '</section>',
		'before_title'  => '<h5 class="widget-title">',
		'after_title'   => '</h5>',
	) );

	register_sidebar( array(
		'name'          => esc_html__( 'Footer Column 1', 'grocery-marketplace' ),
		'id'            => 'grocery-marketplace-footer1',
		'description'   => '',
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h5 class="footer-column-widget-title">',
		'after_title'   => '</h5>',
	) );

	register_sidebar( array(
		'name'          => esc_html__( 'Footer Column 2', 'grocery-marketplace' ),
		'id'            => 'grocery-marketplace-footer2',
		'description'   => '',
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h5 class="footer-column-widget-title">',
		'after_title'   => '</h5>',
	) );

	register_sidebar( array(
		'name'          => esc_html__( 'Footer Column 3', 'grocery-marketplace' ),
		'id'            => 'grocery-marketplace-footer3',
		'description'   => '',
		'before_widget' => '<aside id="%1$s" class="widget %2$s">',
		'after_widget'  => '</aside>',
		'before_title'  => '<h5 class="footer-column-widget-title">',
		'after_title'   => '</h5>',
	) );
}
add_action( 'widgets_init', 'grocery_marketplace_widgets_init' );

/**
 * Enqueue scripts and styles.
 */
function grocery_marketplace_scripts() {

	wp_enqueue_style(
		'josefin-sans',
		grocery_marketplace_wptt_get_webfont_url('https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&display=swap'),  //    font-family: "Josefin Sans", sans-serif;
		array(),
		'1.0'
	);

	wp_enqueue_style(
		'poppins',
		grocery_marketplace_wptt_get_webfont_url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap'),  //    font-family: "Poppins", sans-serif;
		array(),
		'1.0'
	);

	wp_enqueue_style( 'grocery-marketplace-block-editor-style', get_theme_file_uri('/assets/css/block-editor-style.css') );
	wp_enqueue_style( 'owl.carousel-css', get_template_directory_uri() . '/assets/css/owl.carousel.css');

	// load bootstrap css
    wp_enqueue_style( 'bootstrap-css', get_template_directory_uri() . '/assets/css/bootstrap.css');

	wp_enqueue_style( 'grocery-marketplace-style', get_stylesheet_uri() );
	require get_parent_theme_file_path( '/custom-option.php' );
	wp_add_inline_style( 'grocery-marketplace-style',$grocery_marketplace_theme_css );

	// fontawesome
	wp_enqueue_style( 'fontawesome-style', get_template_directory_uri() .'/assets/css/fontawesome/css/all.css' );

    wp_enqueue_script('grocery-marketplace-theme-js', get_template_directory_uri() . '/assets/js/theme-script.js', array('jquery'), '', true );

    wp_enqueue_script( 'bootstrap', get_template_directory_uri() . '/assets/js/bootstrap.js',array('jquery'),'',true);

    wp_enqueue_script('owl.carousel-js', get_template_directory_uri() . '/assets/js/owl.carousel.js', array('jquery'), '', true );

	if ( is_singular() && comments_open() && get_option( 'thread_comments' ) ) {
		wp_enqueue_script( 'comment-reply' );
	}
}
add_action( 'wp_enqueue_scripts', 'grocery_marketplace_scripts' );

/**
 * Enqueue Preloader.
 */
function grocery_marketplace_preloader() {

  $grocery_marketplace_theme_color_css = '';
  $grocery_marketplace_preloader_bg_color = get_theme_mod('grocery_marketplace_preloader_bg_color');
  $grocery_marketplace_preloader_dot_1_color = get_theme_mod('grocery_marketplace_preloader_dot_1_color');
  $grocery_marketplace_preloader_dot_2_color = get_theme_mod('grocery_marketplace_preloader_dot_2_color');
  $grocery_marketplace_preloader2_dot_color = get_theme_mod('grocery_marketplace_preloader2_dot_color');
  $grocery_marketplace_logo_max_height = get_theme_mod('grocery_marketplace_logo_max_height');
  $grocery_marketplace_scroll_bg_color = get_theme_mod('grocery_marketplace_scroll_bg_color');
  $grocery_marketplace_scroll_color = get_theme_mod('grocery_marketplace_scroll_color');
  $grocery_marketplace_scroll_font_size = get_theme_mod('grocery_marketplace_scroll_font_size');
  $grocery_marketplace_scroll_border_radius = get_theme_mod('grocery_marketplace_scroll_border_radius');
  $grocery_marketplace_related_product_display_setting = get_theme_mod('grocery_marketplace_related_product_display_setting', true);

  	if(get_theme_mod('grocery_marketplace_logo_max_height') == '') {
		$grocery_marketplace_logo_max_height = '200';
	}

	if(get_theme_mod('grocery_marketplace_preloader_bg_color') == '') {
		$grocery_marketplace_preloader_bg_color = '#0C7735';
	}
	if(get_theme_mod('grocery_marketplace_preloader_dot_1_color') == '') {
		$grocery_marketplace_preloader_dot_1_color = '#ffffff';
	}
	if(get_theme_mod('grocery_marketplace_preloader_dot_2_color') == '') {
		$grocery_marketplace_preloader_dot_2_color = '#222222';
	}

	// Start CSS build
	$grocery_marketplace_theme_color_css = '';

	
	if (!$grocery_marketplace_related_product_display_setting) {
	    $grocery_marketplace_theme_color_css .= '
	        .related.products,
	        .related h2 {
	            display: none !important;
	        }
	    ';
	}

	$grocery_marketplace_theme_color_css .= '
		.custom-logo-link img{
			max-height: '.esc_attr($grocery_marketplace_logo_max_height).'px;
	 	}
		.loading{
			background-color: '.esc_attr($grocery_marketplace_preloader_bg_color).';
		 }
		 @keyframes loading {
		  0%,
		  100% {
		  	transform: translatey(-2.5rem);
		    background-color: '.esc_attr($grocery_marketplace_preloader_dot_1_color).';
		  }
		  50% {
		  	transform: translatey(2.5rem);
		    background-color: '.esc_attr($grocery_marketplace_preloader_dot_2_color).';
		  }
		}
		.load hr {
			background-color: '.esc_attr($grocery_marketplace_preloader2_dot_color).';
		}
		a#button{
			background-color: '.esc_attr($grocery_marketplace_scroll_bg_color).';
			color: '.esc_attr($grocery_marketplace_scroll_color).' !important;
			font-size: '.esc_attr($grocery_marketplace_scroll_font_size).'px;
			border-radius: '.esc_attr($grocery_marketplace_scroll_border_radius).'%;
		}
	';
    wp_add_inline_style( 'grocery-marketplace-style',$grocery_marketplace_theme_color_css );

}
add_action( 'wp_enqueue_scripts', 'grocery_marketplace_preloader' );

function grocery_marketplace_sanitize_select( $input, $setting ){
    $input = sanitize_key($input);
    $choices = $setting->manager->get_control( $setting->id )->choices;
    return ( array_key_exists( $input, $choices ) ? $input : $setting->default );
}

function grocery_marketplace_sanitize_checkbox( $input ) {
  // Boolean check
  return ( ( isset( $input ) && true == $input ) ? true : false );
}

/*radio button sanitization*/
function grocery_marketplace_sanitize_choices( $input, $setting ) {
    global $wp_customize;
    $control = $wp_customize->get_control( $setting->id );
    if ( array_key_exists( $input, $control->choices ) ) {
        return $input;
    } else {
        return $setting->default;
    }
}

function grocery_marketplace_sanitize_number_range( $number, $setting ) {
	
	// Ensure input is an absolute integer.
	$number = absint( $number );
	
	// Get the input attributes associated with the setting.
	$atts = $setting->manager->get_control( $setting->id )->input_attrs;
	
	// Get minimum number in the range.
	$min = ( isset( $atts['min'] ) ? $atts['min'] : $number );
	
	// Get maximum number in the range.
	$max = ( isset( $atts['max'] ) ? $atts['max'] : $number );
	
	// Get step.
	$step = ( isset( $atts['step'] ) ? $atts['step'] : 1 );
	
	// If the number is within the valid range, return it; otherwise, return the default
	return ( $min <= $number && $number <= $max && is_int( $number / $step ) ? $number : $setting->default );
}

function grocery_marketplace_sanitize_number_absint( $number, $setting ) {
	// Ensure $number is an absolute integer (whole number, zero or greater).
	$number = absint( $number );

	// If the input is an absolute integer, return it; otherwise, return the default
	return ( $number ? $number : $setting->default );
}

// Change number or products per row to 3
add_filter('loop_shop_columns', 'grocery_marketplace_loop_columns');
if (!function_exists('grocery_marketplace_loop_columns')) {
	function grocery_marketplace_loop_columns() {
		$columns = get_theme_mod( 'grocery_marketplace_products_per_row', 3 );
		return $columns; // 3 products per row
	}
}

//Change number of products that are displayed per page (shop page)
add_filter( 'loop_shop_per_page', 'grocery_marketplace_shop_per_page', 9 );
function grocery_marketplace_shop_per_page( $cols ) {
  	$cols = get_theme_mod( 'grocery_marketplace_product_per_page', 9 );
	return $cols;
}

// Filter to change the number of related products displayed
add_filter( 'woocommerce_output_related_products_args', 'grocery_marketplace_products_args' );
function grocery_marketplace_products_args( $args ) {
    $args['posts_per_page'] = get_theme_mod( 'custom_related_products_number', 6 );
    $args['columns'] = get_theme_mod( 'custom_related_products_number_per_row', 3 );
    return $args;
}

function grocery_marketplace_get_page_id_by_title($grocery_marketplace_pagename){
    $args = array(
        'post_type' => 'page',
        'posts_per_page' => 1,
        'post_status' => 'publish',
        'title' => $grocery_marketplace_pagename
    );
    $query = new WP_Query( $args );

    $page_id = '1';
    if (isset($query->post->ID)) {
        $page_id = $query->post->ID;
    }

    return $page_id;
}

/*dropdown page sanitization*/
function grocery_marketplace_sanitize_dropdown_pages( $page_id, $setting ) {
	$page_id = absint( $page_id );
	return ( 'publish' == get_post_status( $page_id ) ? $page_id : $setting->default );
}

function grocery_marketplace_remove_customize_register() {
    global $wp_customize;

    $wp_customize->remove_setting( 'pro_version_footer_setting' );
    $wp_customize->remove_control( 'pro_version_footer_setting' );

}
add_action( 'customize_register', 'grocery_marketplace_remove_customize_register', 11 );

if ( class_exists( 'WP_Customize_Control' ) ) {
	// Image Toggle Radio Buttpon
	class Grocery_Marketplace_Image_Radio_Control extends WP_Customize_Control {

	    public function render_content() {
	 
	        if (empty($this->choices))
	            return;
	 
	        $name = '_customize-radio-' . $this->id;
	        ?>
	        <span class="customize-control-title"><?php echo esc_html($this->label); ?></span>
	        <ul class="controls" id='grocery-marketplace-img-container'>
	            <?php
	            foreach ($this->choices as $value => $label) :
	                $class = ($this->value() == $value) ? 'grocery-marketplace-radio-img-selected grocery-marketplace-radio-img-img' : 'grocery-marketplace-radio-img-img';
	                ?>
	                <li style="display: inline;">
	                    <label>
	                        <input <?php $this->link(); ?>style = 'display:none' type="radio" value="<?php echo esc_attr($value); ?>" name="<?php echo esc_attr($name); ?>" <?php
	                          	$this->link();
	                          	checked($this->value(), $value);
	                          	?> />
	                        <img src='<?php echo esc_url($label); ?>' class='<?php echo esc_attr($class); ?>' />
	                    </label>
	                </li>
	                <?php
	            endforeach;
	            ?>
	        </ul>
	        <?php
	    } 
	}
}


require_once get_theme_file_path( 'inc/wptt-webfont-loader.php' );

/**
 * Custom template tags for this theme.
 */
require get_template_directory() . '/inc/template-tags.php';

/**
 * Functions which enhance the theme by hooking into WordPress.
 */
require get_template_directory() . '/inc/template-functions.php';

/**
 * Implement the Custom Header feature.
 */
require get_template_directory() . '/inc/custom-header.php';

/**
 * Customizer additions.
 */
require get_template_directory() . '/inc/customizer.php';

/**
* TGM
*/
require get_template_directory() . '/inc/tgm.php';

/**
 * Menu
 */

require get_template_directory() . '/inc/class-navigation-menu.php';



// add_action( 'grocery_marketplace_navigation_action','grocery_marketplace_single_post_navigation',30 );
if( !function_exists('grocery_marketplace_content_offcanvas') ):

    // Offcanvas Contents
    function grocery_marketplace_content_offcanvas(){ ?>

        <div id="offcanvas-menu">
            <div class="offcanvas-wraper">
                <div class="close-offcanvas-menu">
                    <div class="offcanvas-close">
                        <a href="javascript:void(0)" class="skip-link-menu-start"></a>
                        <button type="button" class="button-offcanvas-close">
                            <span class="offcanvas-close-label">
                                <i class="fas fa-times"></i>
                            </span>
                        </button>
                    </div>
                </div>
                <div id="primary-nav-offcanvas" class="offcanvas-item offcanvas-main-navigation">
                    <nav class="primary-menu-wrapper" aria-label="<?php esc_attr_e('Horizontal', 'grocery-marketplace'); ?>" role="navigation">
                        <ul class="primary-menu theme-menu">
                            <?php
                            if (has_nav_menu('primary')) {
                                wp_nav_menu(
                                    array(
                                        'container' => '',
                                        'items_wrap' => '%3$s',
                                        'theme_location' => 'primary',
                                        'show_toggles' => true,
                                    )
                                );
                            }else{

                                wp_list_pages(
                                    array(
                                        'match_menu_classes' => true,
                                        'show_sub_menu_icons' => true,
                                        'title_li' => false,
                                        'show_toggles' => true,
                                        'walker' => new grocery_marketplace_Menu_Page(),
                                    )
                                );
                            }
                            ?>
                        </ul>
                    </nav><!-- .primary-menu-wrapper -->
                </div>
                <a href="javascript:void(0)" class="skip-link-menu-end"></a>
            </div>
        </div>

    <?php
    }

endif;

add_action( 'grocery_marketplace_before_footer_content_action','grocery_marketplace_content_offcanvas',30 );


if ( ! function_exists( 'grocery_marketplace_sub_menu_toggle_button' ) ) :

    function grocery_marketplace_sub_menu_toggle_button( $args, $item, $depth ) {

        // Add sub menu toggles to the main menu with toggles
        if ( $args->theme_location == 'primary' && isset( $args->show_toggles ) ) {
            
            // Wrap the menu item link contents in a div, used for positioning
            $args->before = '<div class="submenu-wrapper">';
            $args->after  = '';

            // Add a toggle to items with children
            if ( in_array( 'menu-item-has-children', $item->classes ) ) {

                $toggle_target_string = '.menu-item.menu-item-' . $item->ID . ' > .sub-menu';

                // Add the sub menu toggle with Font Awesome icon
                $args->after .= '<button type="button" class="theme-aria-button submenu-toggle" data-toggle-target="' . esc_attr( $toggle_target_string ) . '" data-toggle-type="slidetoggle" data-toggle-duration="250" aria-expanded="false"><span class="btn__content" tabindex="-1"><span class="screen-reader-text">' . esc_html__( 'Show sub menu', 'grocery-marketplace' ) . '</span><i class="fas fa-chevron-down"></i></span></button>';

            }

            // Close the wrapper
            $args->after .= '</div><!-- .submenu-wrapper -->';

        } elseif ( $args->theme_location == 'primary' ) {

            if ( in_array( 'menu-item-has-children', $item->classes ) ) {

                $args->before = '<div class="link-icon-wrapper">';
                $args->after  = '<i class="fas fa-chevron-down"></i></div>';

            } else {

                $args->before = '';
                $args->after  = '';

            }

        }

        return $args;

    }

endif;

add_filter( 'nav_menu_item_args', 'grocery_marketplace_sub_menu_toggle_button', 10, 3 );
