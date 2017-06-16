;(function($){
    $.fn.mk_thumbnails = function(options){

        return this.each(function(){
            var opts = $.extend({}, $.fn.mk_thumbnails.defaults, options);

            var thumbnailSet = $(this).find('a').wrap('<section>');
            var thumbnail = $(this).wrapInner('<div>').children().addClass('thumbnailSet');

            var mk_thumbnail = function(){
                var thumbnail_w,
                    thumbnailSet_w = $('#thumbnail').width()-1,
                    section_w,
                    margin = thumbnailSet_w*0.01;

                section_w = (thumbnailSet_w/opts.thumbnail_count);
                thumbnail_w = section_w - (margin*2 + 2 + opts.padding*2);

                $('.thumbnailSet section, .thumbnailSet a').css({
                    'width': thumbnail_w,
                    'height': thumbnail_w
                });
                $('.thumbnailSet a').css({
                    'display': 'table-cell',
                    'vertical-align': 'middle',
                });
                $('.thumbnailSet section').css({
                    'background': '#FFF',
                    'border': '1px solid #CCC',
                    'box-shadow': '1px 1px 1px #CCC',
                    'float': 'left',
                    'margin': margin,
                    'padding': opts.padding
                });
                $('.thumbnailSet').find('img').css({
                    'max-width': '100%',
                    'height': 'auto'
                });

                };

            mk_thumbnail();
            $(window).on("resize",function(){
                setTimeout(function(){
                    mk_thumbnail();
                }, 300);
            });     
        });
    };

    $.fn.mk_thumbnails.defaults = {
        padding: 5,
        thumbnail_count: 4
    };

})(jQuery);
