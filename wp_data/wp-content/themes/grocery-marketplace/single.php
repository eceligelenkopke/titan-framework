<?php
/**
 * The template for displaying all single posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 * @package Grocery Marketplace
 */

get_header(); ?>

    <div id="skip-content">
        <div class="feature-header">
            <div class="feature-post-thumbnail">
                <div class="slider-alternate">
                  <img src="<?php echo get_stylesheet_directory_uri() . '/assets/img/banner.png'; ?>">
                </div>
                <h1 class="post-title feature-header-title"><?php the_title(); ?></h1>
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div id="primary" class="content-area <?php echo is_active_sidebar('sidebar') ? "col-lg-9 col-md-8" : "col-lg-12"; ?>">
                    <main id="main" class="site-main module-border-wrap mb-4">
                        <?php while (have_posts()) : the_post();
                            get_template_part('template-parts/content', 'single'); ?>

                            <?php if (!is_singular('attachment')):
                                the_post_navigation();
                                endif;
                                // If comments are open or we have at least one comment, load up the comment template.
                                if (comments_open() || get_comments_number()) :
                                    comments_template();
                                endif; ?>
                            <?php endwhile; // End of the loop.
                        ?>
                    </main>
                </div>
                <div class="col-lg-3 col-md-3">
                    <?php get_sidebar(); ?>
                </div>
            </div>
        </div>
    </div>

<?php get_footer();