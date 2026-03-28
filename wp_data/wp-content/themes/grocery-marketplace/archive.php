<?php
/**
 * The template for displaying archive pages
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/
 *
 * @package Grocery Marketplace
 */

get_header(); ?>

    <div id="skip-content" >
        <div class="feature-header">
            <div class="feature-post-thumbnail">
                <div class="slider-alternate">
                  <img src="<?php echo get_stylesheet_directory_uri() . '/assets/img/banner.png'; ?>">
                </div>
                <h1 class="post-title feature-header-title"><?php esc_html_e('Archive Post','grocery-marketplace'); ?></h1>
            </div>
        </div>    
        <div class="container">
            <div id="primary" class="content-area">
                <main id="main" class="site-main">
                    
                    <?php if (have_posts()) { 
                        if (is_home() && !is_front_page()) : ?>
                            <header>
                                <h1 class="page-title screen-reader-text"><?php single_post_title(); ?></h1>
                            </header>
                        <?php endif; ?>

                    <div class="row">
                        <?php
                            get_template_part( 'template-parts/patterns');

                        } else {

                            get_template_part('template-parts/content', 'none');

                        } ?>
                    </div>

                </main>
            </div>
        </div>
    </div>

<?php get_footer();