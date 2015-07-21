import pkg_resources

from orangecanvas import config

from . import discovery
from . import workflow

WIDGETS_ENTRY = "orange.widgets"
ADDONS_ENTRY = "orange.addon"


class orangeconfig(config.default):
    @staticmethod
    def widgets_entry_points():
        """
        Return an `EntryPoint` iterator for all 'orange.widget' entry
        points plus the default Orange Widgets.

        """
        dist = pkg_resources.get_distribution("Orange")
        ep = pkg_resources.EntryPoint("Orange Widgets", "Orange.widgets",
                                      dist=dist)
        return iter((ep,) +
                    tuple(pkg_resources.iter_entry_points(WIDGETS_ENTRY)))

    @staticmethod
    def addon_entry_points():
        return pkg_resources.iter_entry_points(ADDONS_ENTRY)

    @staticmethod
    def addon_pypi_search_spec():
        return {"keywords": ["orange3 add-on"]}

    widget_discovery = discovery.WidgetDiscovery
    workflow_constructor = workflow.WidgetsScheme
