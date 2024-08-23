from fivc.interfaces import IComponentSite
from . import (
    ComponentSite,
    ComponentSiteBuilder,
)


def load_component_site(
        filename: str,
        fmt: str = 'json',
) -> IComponentSite:
    site = ComponentSite()
    site_builder = ComponentSiteBuilder()
    with open(filename) as f:
        site_builder.loads(site, f, fmt=fmt)
    return site
