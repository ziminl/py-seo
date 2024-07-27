from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree



urls = ['https://example.com/page1', 'https://example.com/page2']



urlset = Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
for url in urls:
    url_element = SubElement(urlset, 'url')
    loc = SubElement(url_element, 'loc')
    loc.text = url


tree = ElementTree(urlset)
tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)
