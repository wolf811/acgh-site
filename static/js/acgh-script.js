let size = 130,
    newsContent = $('.news-content');

newsContent.each(
    function(el) {
        console.log(el, $(this));
        if ($(this).text().length > size) {
            let newText = $(this).text().slice(0, size) + " ...";
            $(this).text(newText);
        }
    }
);