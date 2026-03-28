<?php
/**
 * Displays top header
 *
 * @package Grocery Supermarket
 */
?>

<div class="top-info text-end py-2">
    <div class="container">
        <div class="row">
            <div class="col-lg-3 col-md-4 col-sm-12 col-12 align-self-center btn-box text-start">
                <div class="track-btn"> <i class="fas fa-truck"></i><?php echo esc_html('Track Your Order','grocery-marketplace'); ?>
                    <?php if(get_theme_mod('grocery_marketplace_track_order_shortcode') != ''){ ?>
                        <div class="track-form"> 
                            <?php echo do_shortcode(get_theme_mod('grocery_marketplace_track_order_shortcode')); ?>
                        </div>
                    <?php }?>
                </div>
                <div class="newsletter-btn">
                    <?php echo esc_html(' Newsletter','grocery-marketplace'); ?>
                    <?php if(get_theme_mod('grocery_marketplace_newsletter_shortcode') != ''){ ?>
                        <div class="newsletter-form"> 
                            <?php echo do_shortcode(get_theme_mod('grocery_marketplace_newsletter_shortcode')); ?>
                        </div>
                    <?php }?>
                </div>
            </div>
            <div class="col-lg-6 col-md-4 col-sm-7 col-12 center-text align-self-center topbar-text">
                <?php if ( get_theme_mod('grocery_marketplace_topbar_text') != "" ) {?>
                    <p class="m-0"><?php echo esc_html(get_theme_mod('grocery_marketplace_topbar_text')); ?></p>
                <?php }?>
            </div>
            <div class="col-lg-3 col-md-4 col-sm-5 col-12 align-self-center right-box">
                <?php if(class_exists('woocommerce')){ ?>
                    <span class="user-btn">
                        <?php if ( is_user_logged_in() ) { ?>
                            
                            <a class="account-btn" href="<?php echo esc_url( get_permalink( get_option('woocommerce_myaccount_page_id') ) ); ?>" title="<?php esc_attr_e('Account','grocery-marketplace'); ?>"><i class="fas fa-user"></i><?php esc_html_e('Account','grocery-marketplace'); ?></a>
                        <?php } 
                        else { ?>
                            
                            <a class="account-btn" href="<?php echo esc_url( get_permalink( get_option('woocommerce_myaccount_page_id') ) ); ?>" title="<?php esc_attr_e('Account','grocery-marketplace'); ?>"><i class="fas fa-user"></i><?php esc_html_e('Account','grocery-marketplace'); ?></a>
                        <?php } ?>
                    </span>
                <?php }?>
                <?php if ( defined('YITH_WCWL') ) { ?>
                    <a class="wishlist-view" href="<?php echo YITH_WCWL()->get_wishlist_url(); ?>" title="<?php esc_attr_e('Wishlist','grocery-marketplace'); ?>">
                        <i class="fas fa-solid fa-heart"></i><?php echo esc_html('WishList','grocery-marketplace'); ?>
                    </a>
                <?php } ?>
            </div>
        </div>
    </div>
</div>