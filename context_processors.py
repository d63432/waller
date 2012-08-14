from django.conf import settings

def site_sections(request):
    sections = [
            {'name': 'Home', 'path': '/'},
            {'name': 'News', 'path': '/news/'},
            {'name': 'About', 'path': '/about/'},
            {'name': 'Products', 'path': '/products/'},
            {'name': 'Photos', 'path': '/photos/'},
    ]
    for section in reversed(sections):
        if request.path.startswith(section['path']):
            section['is_current'] = True
            current_section = section
            break
    return {'LayoutSections': sections, 'CurrentSection': current_section}
