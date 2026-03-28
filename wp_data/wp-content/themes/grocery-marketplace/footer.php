<?php
/**
 * The template for displaying the footer
 *
 * Contains the closing of the #content div and all content after.
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package Grocery Marketplace
 */
do_action('grocery_marketplace_before_footer_content_action');

?>

<footer id="colophon" class="site-footer border-top">
    <div class="container">
    	<div class="footer-column">
	      	<div class="row">
		        <div class="col-lg-3 col-md-6 col-sm-6 col-12">
		          	<?php if (is_active_sidebar('grocery-marketplace-footer1')) : ?>
                        <?php dynamic_sidebar('grocery-marketplace-footer1'); ?>
                    <?php else : ?>
                        <aside id="search" class="widget" role="complementary" aria-label="<?php esc_attr_e( 'firstsidebar', 'grocery-marketplace' ); ?>">
                            <h5 class="widget-title"><?php esc_html_e( 'About Us', 'grocery-marketplace' ); ?></h5>
                            <div class="textwidget">
                            	<p><?php esc_html_e( 'Nam malesuada nulla nisi, ut faucibus magna congue nec. Ut libero tortor, tempus at auctor in, molestie at nisi. In enim ligula, consequat eu feugiat a.', 'grocery-marketplace' ); ?></p>
                            </div>
                        </aside>
                    <?php endif; ?>
		        </div>
		        <div class="col-lg-3 col-md-6 col-sm-6 col-12">
		            <?php if (is_active_sidebar('grocery-marketplace-footer2')) : ?>
                        <?php dynamic_sidebar('grocery-marketplace-footer2'); ?>
                    <?php else : ?>
                        <aside id="pages" class="widget">
                            <h5 class="widget-title"><?php esc_html_e( 'Useful Links', 'grocery-marketplace' ); ?></h5>
                            <ul class="mt-4">
                            	<li><a href="#"><?php esc_html_e( 'Home', 'grocery-marketplace' ); ?></a></li>
                            	<li><a href="#"><?php esc_html_e( 'Tournaments', 'grocery-marketplace' ); ?></a></li>
                            	<li><a href="#"><?php esc_html_e( 'Reviews', 'grocery-marketplace' ); ?></a></li>
                            	<li><a href="#"><?php esc_html_e( 'About Us', 'grocery-marketplace' ); ?></a></li>
                            </ul>
                        </aside>
                    <?php endif; ?>
		        </div>
		        <div class="col-lg-3 col-md-6 col-sm-6 col-12">
		            <?php if (is_active_sidebar('grocery-marketplace-footer3')) : ?>
                        <?php dynamic_sidebar('grocery-marketplace-footer3'); ?>
                    <?php else : ?>
                        <aside id="pages" class="widget">
                            <h5 class="widget-title"><?php esc_html_e( 'Information', 'grocery-marketplace' ); ?></h5>
                            <ul class="mt-4">
                            	<li><?php esc_html_e( 'FAQ', 'grocery-marketplace' ); ?></li>
                            	<li><?php esc_html_e( 'Site Maps', 'grocery-marketplace' ); ?></li>
                            	<li><?php esc_html_e( 'Privacy Policy', 'grocery-marketplace' ); ?></li>
                            	<li><?php esc_html_e( 'Contact Us', 'grocery-marketplace' ); ?></li>
                            </ul>
                        </aside>
                    <?php endif; ?>
		        </div>
		        <div class="col-lg-3 col-md-6 col-sm-6 col-12">
		            <?php if (is_active_sidebar('grocery-marketplace-footer4')) : ?>
                        <?php dynamic_sidebar('grocery-marketplace-footer4'); ?>
                    <?php else : ?>
                        <aside id="pages" class="widget">
                            <h5 class="widget-title"><?php esc_html_e( 'Get In Touch', 'grocery-marketplace' ); ?></h5>
                            <ul class="mt-4">
                            	<li><?php esc_html_e( 'Via Carlo Montù 78', 'grocery-marketplace' ); ?><br><?php esc_html_e( '22021 Bellagio CO, Italy', 'grocery-marketplace' ); ?></li>
                            	<li><?php esc_html_e( '+11 6254 7855', 'grocery-marketplace' ); ?></li>
                            	<li><?php esc_html_e( 'support@example.com', 'grocery-marketplace' ); ?></li>
                            </ul>
                        </aside>
                    <?php endif; ?>
		        </div>
	      	</div>
		</div>
    	<?php if (get_theme_mod('grocery_marketplace_show_hide_copyright', true)) {?>
	        <div class="site-info">
	            <div class="footer-menu-left text-center">
	            	<?php  if( ! get_theme_mod('grocery_marketplace_footer_text_setting') ){ ?>
					    <a target="_blank" href="<?php echo esc_url('https://wordpress.org/'); ?>">
							<?php
							/* translators: %s: CMS name, i.e. WordPress. */
							printf( esc_html__( 'Proudly powered by %s', 'grocery-marketplace' ), 'WordPress' );
							?>
					    </a>
					    <span class="sep mr-1"> | </span>

					    <span>
		              		<?php
			                /* translators: 1: Theme name,  */
			                printf( esc_html__( ' %1$s ', 'grocery-marketplace' ),'Grocery Marketplace WordPress Theme' );
			              	?>
				          	<?php
				              /* translators: 1: Theme author. */
				              printf( esc_html__( 'by %1$s.', 'grocery-marketplace' ),'TheMagnifico'  );
				            ?>

	        			</span>
					<?php }?>
					<?php echo esc_html(get_theme_mod('grocery_marketplace_footer_text_setting')); ?>
	            </div>
	        </div>
		<?php } ?>
	    <?php if(get_theme_mod('grocery_marketplace_scroll_hide',true)){ ?>
	    	<a id="button"><?php esc_html_e('TOP','grocery-marketplace'); ?></a>
	    <?php } ?>
    </div>
</footer>
</div>

<?php wp_footer(); ?>

</body>
</html>