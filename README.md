# Cover image

A [Pelican](http://getpelican.com/) plugin that adds a `cover_image_url` attribute to articles and pages. Includes settings for local and default images.

## Installation

1. Download this plugin
2. Place it in your plugins directory
3. Add `pelican-cover-image` to `PLUGINS` in your settings file.

Or see the general [Plugin installation instructions](http://docs.getpelican.com/en/latest/plugins.html).

## Usage

Add the attribute `cover_image` to your article or page **metadata**:

```yaml
title: My super title
date: 2010-12-03 10:20
cover_image: https://images.unsplash.com/photo-1471644865643-fe726490270a # Can also be a local image file, see further

This is the content of my super blog post.
```

This will activate the `cover_image_url` attribute for all articles (including drafts) and pages (including hidden pages), which you can use in templates as follows:

**Article template:**

```html
<img src="{{ article.cover_image_url }}" alt="Cover image">
```

**Page template:**

```html
<img src="{{ page.cover_image_url }}" alt="Cover image">
```

[![Example image by Ray Hennessy](https://images.unsplash.com/photo-1471644865643-fe726490270a?w=1024)](https://unsplash.com/photos/DAHUS8W4rNE)

### Using local images

If you want to use local images in addition to full image URLs, you need to define in your **settings file** where those are stored:

```python
COVER_IMAGES_PATH = "static/cover_images" # No trailing slash
```

Make sure that path is included in `STATIC_PATHS` so Pelican will copy all cover images to the output directory (see [Pelican documentation](http://docs.getpelican.com/en/stable/settings.html#basic-settings)):

```python
STATIC_PATHS = ["static"] # Since /cover_images is a subdirectory of /static, it is included here
```

With the above settings, the `cover_image_url` for the following article will be `http://example.com/static/cover_images/unicorn.jpg` (format: `SITEURL`/`COVER_IMAGES_PATH`/`cover_image`):

```yaml
title: My super title
date: 2010-12-03 10:20
cover_image: unicorn.jpg

This is the content of my super blog post.
```

### Using a default image

By default `cover_image_url` will be empty if `cover_image` is not defined (either as URL or local file) in the article or page metadata. If you want to set a default image for all pages and articles, add one to your **settings file**:

```python
DEFAULT_COVER_IMAGE = "https://images.unsplash.com/photo-1489513963600-afa31b458fec"
```

`DEFAULT_COVER_IMAGE` can also be a local image file, using the same settings as described above.

```python
DEFAULT_COVER_IMAGE = "default_image.jpg" # Will look for image at COVER_IMAGES_PATH
```

### Give credit

Only use images you have the right to use. If you are using images licensed under [Creative Commons Attribution](https://creativecommons.org/licenses/by/4.0/) or alike, you can easily add extra attributes to your **metadata**:

```yaml
title: My super title
date: 2010-12-03 10:20
cover_image: https://images.unsplash.com/photo-1471644865643-fe726490270a
cover_image_by: Ray Hennessy
cover_image_link: https://unsplash.com/photos/DAHUS8W4rNE

This is the content of my super blog post.
```

And adapt your template to:

```html
<figure>
     <img src="{{ page.cover_image_url }}" alt="Cover image">
     <figcaption>Image by <a href="{{ page.cover_image_link }}">{{ cover_image_by }}</a></figcaption>
</figure>
```

## LICENSE

[LICENSE](LICENSE) 
