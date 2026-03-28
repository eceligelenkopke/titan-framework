<?php
/**
 * Displays main header
 *
 * @package Grocery Marketplace
 */
?>

<div class="main-header text-center text-md-start">
    <div class="container">
        <div class="row nav-box">
            <div class="col-lg-3 col-md-6 col-sm-7 logo-box align-self-center">
                <div class="all-categories">
                    <?php if(class_exists('woocommerce')){ ?>
                        <button class="cat-btn"><span><i class="fas fa-bars"></i></span><?php esc_html_e('browse all categories','grocery-marketplace'); ?> <i class="fas fa-chevron-down"></i></button>
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
            </div>
            <div class="col-lg-9 col-md-6 col-sm-5 align-self-center header-box">
                <?php get_template_part('template-parts/navigation/nav'); ?>
            </div>
        </div>
    </div>
</div>
