<?php
/**
 * Displays top header 1
 *
 * @package Grocery Supermarket
 */
?>

<div class="top-header py-2">
	<div class="container">
        <div class="row">
            <div class="col-lg-3 col-md-5 col-sm-5 col-12 align-self-center">
                <div class="navbar-brand text-center text-md-start">
                    <?php if ( has_custom_logo() ) : ?>
                        <div class="site-logo"><?php the_custom_logo(); ?></div>
                    <?php endif; ?>
                    <?php $grocery_marketplace_blog_info = get_bloginfo( 'name' ); ?>
                        <?php if ( ! empty( $grocery_marketplace_blog_info ) ) : ?>
                            <?php if ( is_front_page() && is_home() ) : ?>
                                <?php if( get_theme_mod('grocery_marketplace_logo_title_text',true) != ''){ ?>
                                    <h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
                                <?php } ?>
                            <?php else : ?>
                                <?php if( get_theme_mod('grocery_marketplace_logo_title_text',true) != ''){ ?>
                                    <p class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></p>
                                <?php } ?>
                            <?php endif; ?>
                        <?php endif; ?>
                        <?php
                            $grocery_marketplace_description = get_bloginfo( 'description', 'display' );
                            if ( $grocery_marketplace_description || is_customize_preview() ) :
                        ?>
                        <?php if( get_theme_mod('grocery_marketplace_theme_description',false) != ''){ ?>
                            <p class="site-description"><?php echo esc_html($grocery_marketplace_description); ?></p>
                        <?php } ?>
                    <?php endif; ?>
                </div>
            </div>
            <div class="col-lg-5 col-md-7 col-sm-7 col-12 align-self-center product-search text-end">
                <div class="all-categories">
                    <?php if(class_exists('woocommerce')){ ?>
                        <button class="cat-btn"><?php esc_html_e('All Categories','grocery-marketplace'); ?> <i class="fas fa-chevron-down"></i></button>
                        <div class="home_product_cat">
                          <?php $grocery_marketplace_args = array(
                              'number'     => '',
                              'orderby'    => 'title',
                              'order'      => 'ASC',
                              'hide_empty' => '',
                              'include'    => ''
                          );
                          $grocery_marketplace_product_categories = get_terms( 'product_cat', $grocery_marketplace_args );
                          $grocery_marketplace_count = count($grocery_marketplace_product_categories);
                            if ( $grocery_marketplace_count > 0 ){
                              foreach ( $grocery_marketplace_product_categories as $product_category ) {
                              echo '<h4><a href="' . get_term_link( $product_category ) . '">' . $product_category->name . '</a></h4>';
                              $grocery_marketplace_args = array(
                                'posts_per_page' => -1,
                                'tax_query' => array(
                                  'relation' => 'AND',
                                  array(
                                    'taxonomy' => 'product_cat',
                                    'field' => 'slug',
                                    'terms' => $product_category->slug
                                  )
                                ),
                                'post_type' => 'product',
                                'orderby' => 'title,'
                              );
                            }
                          }?>
                        </div>
                    <?php }?>
                </div>
                <?php if(class_exists('woocommerce')){ ?>
                    <?php get_product_search_form(); ?>
                <?php }?>
            </div>
            <div class="col-lg-2 col-md-6 col-sm-6 col-12 align-self-center text-center text-md-end">
                <div class="header-phone">  
                    <?php if ( get_theme_mod('grocery_marketplace_header_phone_number') != "" ) {?>
                        <div class="contact-box">
                            <div class="icon-call">
                                <i class="fas fa-headset"></i>
                            </div>
                            <div class="contact-text">
                                <?php if ( get_theme_mod('grocery_marketplace_header_phone_text') != "" ) {?>
                                    <h6><?php echo esc_html(get_theme_mod('grocery_marketplace_header_phone_text')); ?></h6>
                                <?php }?>
                                <a href="tel:<?php echo esc_attr(get_theme_mod('grocery_marketplace_header_phone_number')); ?>"><?php echo esc_html(get_theme_mod('grocery_marketplace_header_phone_number')); ?></a>
                            </div>   
                        </div>
                    <?php }?>
                </div>
            </div>
            <div class="col-lg-2 col-md-6 col-sm-6 col-12 btn-box align-self-center text-end">
                <span class="cart_no">
                    <?php if ( class_exists( 'WooCommerce' ) ) { ?>
                        <a class="cart-customlocation" href="<?php echo esc_url( wc_get_cart_url() ); ?>">
                            <div class="icon">
                                <i class="fas fa-cart-plus"></i>
                                <span class="cart-value">
                                    <?php echo WC()->cart->get_cart_contents_count(); ?>
                                </span>
                            </div>
                            <div class="cart-text-count">
                                <span class="cart-amount">
                                    <?php echo WC()->cart->get_cart_total(); ?>
                                </span>
                                <br>
                                <span class="cart-text"><?php esc_html_e('MY CART','grocery-marketplace'); ?></span>
                            </div>
                        </a>
                    <?php } ?>
                </span>
            </div>
        </div>
	</div>
</div>