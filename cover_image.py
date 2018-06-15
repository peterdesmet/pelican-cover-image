from pelican import signals

def cover_image(generator):
    """
    Adds cover_image_url and cover_image_caption attributes to each article/page, based on 
    metadata or pelican settings
    """

    # Create list of articles_or_pages
    articles = getattr(generator, "articles", [])
    drafts = getattr(generator, "drafts", [])
    pages = getattr(generator, "pages", [])
    hidden_pages = getattr(generator, "hidden_pages", [])
    articles_or_pages = articles + drafts + pages + hidden_pages

    for article_or_page in articles_or_pages:
        # Use cover_image from the article/page metadata if defined and not empty,
        # otherwise use the COVER_IMAGE_DEFAULT from the settings.
        if hasattr(article_or_page, "cover_image") and article_or_page.cover_image:
            cover_image = article_or_page.cover_image
        elif "COVER_IMAGE_DEFAULT" in generator.settings:
            cover_image = generator.settings["COVER_IMAGE_DEFAULT"]
        else:
            cover_image = ""

        # Then we set the cover_image_url, either directly from the cover_image (if it starts with http)
        # or by combining the SITEURL + COVER_IMAGES_PATH + cover_image (file name).
        if cover_image:
            if cover_image.startswith("http"):
                cover_image_url = cover_image
            elif "COVER_IMAGES_PATH" in generator.settings:
                cover_image_url = generator.settings["SITEURL"] + "/" + generator.settings["COVER_IMAGES_PATH"] + "/" + cover_image
            else:
                cover_image_url = "1"
        else:
            cover_image_url = "2"


        # Set cover_image_caption using COVER_IMAGE_CAPTION format and article/page metadata
        if "COVER_IMAGE_CAPTION" in generator.settings:
            cover_image_caption = generator.settings["COVER_IMAGE_CAPTION"]

            # Match {...} pattern in caption, e.g. cover_image_ref and cover_image_by in
            # "Image by <a href=\"{cover_image_ref}\">{cover_image_by}</a>"
            import re
            matches = re.findall(r"\{(.*?)\}", cover_image_caption)

            # For each match, check if metadata attribute of same name is present and replace with
            # its value in caption. If one of the attributes is missing, break and leave caption 
            # empty (to avoid half-populated captions)
            for match in matches:
                metadata_attribute = getattr(article_or_page, match, False)
                if metadata_attribute:
                    cover_image_caption = cover_image_caption.replace("{" + match + "}", metadata_attribute)
                else:
                    cover_image_caption = ""
                    break
        else:
            cover_image_caption = ""

        # Add cover_image_url and cover_image_caption as attributes to article or page:
        article_or_page.cover_image_url = cover_image_url
        article_or_page.cover_image_caption = cover_image_caption

def register():
    signals.article_generator_finalized.connect(cover_image)
    signals.page_generator_finalized.connect(cover_image)
